---
title: 📌 Projet Installation d'un Cluster Kubernetes et déploiement d'une application
date: 2024 / 2025
---

## 🎯 Objectifs

- Comprendre les concepts fondamentaux de Kubernetes  
- Installer et configurer un cluster Kubernetes  
- Administrer un cluster et gérer son cycle de vie  
- Déployer et superviser une application dans Kubernetes  

## 🛠️ Étapes du Projet

### Phase 1 : Installation du Cluster Kubernetes

Le but de cette partie est d'installer un cluster Kubernetes. Le cluster devra être composé d'au moins 2 noeuds : 2 worker, le `ControlPlane` peut éventuellement être installé sur le même noeud qu'un `Worker` pour limiter les ressources nécessaires.

Note 1 : il n'est pas demandé de gérer précisément la sécurité du cluster, ni la supervision et le logging, ces parties seront abordées durant le second module Kubernetes.

Note 2 : On demande à installer une "vraie" distribution Kubernetes pouvant être déployée en production : `k8s` via `kubeadm`, `rke`, `k3s`, … On évitera donc les versions orientées développeur à déployer uniquement sur sa machine personnelle : ~`Docker Desktop`, `Minikube`, …~

1. **Choix de l’environnement**
   - Déploiement sur des machines virtuelles (VirtualBox, VMware).
   - Déploiement sur le cloud (GCP, AWS, Azure, …). Oracle OCI propose une offre gratuite suffisante pour ce projet.
2. **Installation des prérequis**
   - Machine Linux
   - Container runtime (`Docker` ou `containerd` ou autre)
   - Outils Kubernetes : `kubeadm`, `kubelet`, `kubectl`, …
3. **Mise en place du cluster**
   - Initialisation du cluster avec `kubeadm` ou autre
   - Ajout de noeuds workers
   - Configuration du réseau avec un CNI (`Flannel`, `Calico`, …)

:::warn
Attention, on demande bien d'installer un cluster **production-ready** ! Celui-ci devra donc être en haute disponibilité (Load balancer devant l'API Server, …) et on réfléchira aux procédures d'administration, de sauvegarde, … On pourra cependant s'affranchir d'utiliser HTTPS.
:::

:::link
- Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/installation/>
- Documentation de référence : <https://kubernetes.io/docs/setup/production-environment/>
- Pour tester la sécurité du cluster, on pourra utiliser <https://github.com/aquasecurity/kube-bench> pour passer le benchmark CIS. 
:::

:::tip
On pourra tester la compatibilité d'un noeud du cluster avec le _Node Conformance Test_. Remplacer `$CONFIG_DIR` par le chemin du manifeste du kubelet :  `/etc/kubernetes/kubelet`,  `/etc/default/kubelet`,  `/etc/systemd/system/kubelet.service`, … `$LOG_DIR` est le chemin où stocker les résultats du test.

```sh
sudo docker run -it --rm \
  --privileged \
  --net=host \
  -v /:/rootfs \
  -v $CONFIG_DIR:$CONFIG_DIR \
  -v $LOG_DIR:/var/result \
  registry.k8s.io/node-test:0.2
```
:::

### Phase 2 : Déploiement d’une Application

Le but de cette partie est de déployer dans le cluster un projet personnel existant qui se compose de plusieurs composants (par exemple, une application web front-end, une API back-end, une base de données, etc.). On recommande l'utilisation de fichiers de manifeste `yml` pour créer les ressources Kubernetes.

1. **Création des manifestes Kubernetes**
   - Déploiement (`Deployment`)
   - Service (`Service`)
   - Bonus : Ingress Controller
2. **Gestion des configurations et secrets**
   - `ConfigMaps` et `Secrets`
3. **Scalabilité et tolérance aux pannes**
   - Autoscaling avec `Horizontal Pod Autoscaler`
   - Rolling updates et rollback

## 📜 Livrables

- 📂 **Rapport détaillé** avec étapes et configurations
- 📜 **Code source** des manifestes Kubernetes
- 🎤 **Présentation** des résultats et démonstration

## Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- K8s® is a registered trademark of The Linux Foundation in the United States and/or other countries.

