---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Haute Disponibilité d'un Cluster Kubernetes
layout: '@layouts/CoursePartLayout.astro'
tags:
- kubernetes
- devops
- HA
---

## Objectifs

- **Éliminer le point de défaillance unique (SPOF)** de l'API server : ne pas dépendre d'un seul nœud pour l'accès au Kubernetes API.
- **Assurer la continuité de l'orchestration** : scheduler, contrôleurs et autoscaler doivent pouvoir continuer à fonctionner même si une instance tombe.
- **Maintenir l'état du cluster** : etcd doit rester disponible avec un quorum minimal de membres pour garantir cohérence et tolérance aux pannes.
- **Servir les workloads applicatifs** même si le control plane est partiellement indisponible.

---

## Architecture de référence HA

- 🛠 Control Plane multiples
- 🧠 Base d'état etcd distribuée
- L'accès aux nœuds du control plane (`api-server`) se fait via un **point d'accès unique hautement disponible** (`ControlPlaneEndpoint`) en utilisant :
  - un **load balancer** TCP (`HAProxy` + `keepalived`) externe ou stacké dans les control-plane
  - une **virtual IP** (`kube-vip`)
  - un DNS _round-robin_ (non supporté officiellement mais fonctionne)
  - H/A API endpoint dans un cluster managé, virtual IP Cloud, tunnel _Node_ <-> _API Server_ (`k3s`), …
- Dans de rares cas (par exemple _k3s_), il est possible de passer d'un cluster mono control-plane à un cluster H/A à tout moment.

:::link
Voir aussi :

- <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/>
- <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/>
- <https://kifarunix.com/setup-highly-available-kubernetes-cluster-with-haproxy-and-keepalived/>

:::

---

## Perte d'un Control Plane

- Contexte : un nœud _control-plane_ est brutalement arrêté ou ne répond plus
- Plusieurs composants et boucles de contrôle interviennent en parallèle :
  - kubelet / Node Lease
  - etcd
  - API Server + Load Balancer
  - Controller Manager
  - Scheduler
  - Node Lifecycle Controller
- Les délais dépendent surtout :
  - des heartbeats
  - des leases
  - des taints
  - des tolérances de pods

---

### Effet immédiat

- Le nœud arrêté ne peut donc plus :
  - Renouveler son **Node Lease**
  - Envoyer son **Node Status**
  - Exécuter les **static pods** du control-plane
- Le cluster ne réagit pas encore.

---

### Health Check du Load Balancer

Le Load Balancer externe :

- détecte que l'API Server du nœud est mort
- le retire de la rotation
- Les clients Kubernetes (`kubectl`, …) retentent automatiquement sur les autres API Servers.
- Timing dépendant du load-balancer (typiquement 10 à 30 secondes)

---

### etcd

Si etcd est **stacké** sur les control-planes :

- Si le quorum reste valide : rien de bloquant
- Si quorum perdu : **écritures bloquées immédiatement**

---

### Réélection des leaders

- Leader election via _Lease API_
- `kube-controller-manager`
- `kube-scheduler`
- `cloud-controller-manager` (si présent)

---

### Node `NotReady`

- Le _Node Lifecycle Controller_ :
  - Marque le nœud `NotReady` :
    - `NodeMonitorGracePeriod` (défaut 40 s)
    - `NodeStatusUpdateFrequency` (défaut 10 s)
  - Puis applique des taints :
    - `node.kubernetes.io/not-ready:NoExecute`
    - `node.kubernetes.io/unreachable:NoExecute`
- Les pods tolèrent ces taints par défaut pendant 5 min (`tolerationSeconds=300s`) :
  - Pods toujours `Running`
  - Le service peut être dégradé.
  - Le scheduler ne lance pas de remplaçant immédiatement.
- Rescheduling des Pods après expiration des 300 s :
  - `Deployment` / `ReplicaSet` / `StatefulSet` recréent les pods
  - Le `Scheduler` les place sur un autre nœud

---

### Static Pods et Suppression du Node

- Static Pods situés dans `/etc/kubernetes/manifests` :
  - **Ne sont pas recréés ailleurs**
  - HA assuré car chaque control-plane a déjà ses pods
  - Aucune migration automatique.
- Kubernetes **ne supprime pas automatiquement** le Node :
  - `kubectl delete node <nodeName>`

---

### Noeud Worker

- Contexte : arrêt brutal / perte d'un Worker
- Comportement global similaire (mais pas d'etcd, leader, …)
- Spécificité des `PersistantVolumeClaim` utilisés : le CSI détache le volume du node mort puis l'attache ailleurs

---

### Timeline

| Temps après panne | Événement                       |
| ----------------- | ------------------------------- |
| 0–5 s             | Silence kubelet                 |
| 1–2 s             | Réélection leader etcd          |
| 5–30 s            | LB retire API Server            |
| 10–15 s           | Réélection scheduler/controller |
| ~40 s             | Node `NotReady`                 |
| 40–60 s           | Taints appliqués                |
| 300 s             | Pods recréés ailleurs           |

Pour réduire le MTTR :

- `--node-monitor-grace-period`
- `--pod-eviction-timeout`
- `tolerationSeconds` des pods :
  - en HA, **300 s → 30–60 s**
- Paramètres leader election
- Health checks du Load Balancer

---
