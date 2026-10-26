---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Projet installation du cluster
type: projet
sidebar:
  order: 3
description: Projet installation du cluster
---

## 🎯 Objectifs

- Comprendre les concepts fondamentaux de Kubernetes
- Installer et configurer un cluster Kubernetes
- Administrer un cluster et gérer son cycle de vie
- Déployer et superviser une application dans Kubernetes

## 🛠️ Étapes du Projet

### Phase 1 : Installation du Cluster Kubernetes

Le but de cette partie est d'installer un cluster Kubernetes. Le cluster devra être composé d'au moins 2 noeuds : 2 worker, le `ControlPlane` peut éventuellement être installé sur le même noeud qu'un `Worker` pour limiter les ressources nécessaires.

:::tip
Il n'est pas demandé de gérer précisément la sécurité du cluster, ni la supervision et le logging, ces parties seront abordées plus tard.
:::

:::tip
On demande à installer une "vraie" distribution Kubernetes pouvant être déployée en production : `k8s` via `kubeadm`, `rke`, `k3s`, … On évitera donc les versions orientées développeur à déployer uniquement sur sa machine personnelle : ~`Docker Desktop`, `Minikube`, …~
:::

:::exo
Réaliser l'installation du cluster Kubernetes :

1. **Choix de l'environnement**
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
4. **Cluster H/A uniquement** : on testera la partie **H/A du `control-plane`** :
   - Déconnecter ou simuler la défaillance d'un `control-plane` pour observer la capacité du cluster à basculer automatiquement.
     :::

:::caution
Attention, on demande bien d'installer un cluster **production-ready** !
:::

:::note

- Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/installation/>
- Documentation de référence : <https://kubernetes.io/docs/setup/production-environment/>
- Pour tester la sécurité du cluster, on pourra utiliser <https://github.com/aquasecurity/kube-bench> pour passer le benchmark CIS.
- Voir aussi : <https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/>

  :::

### Phase 2 : Déploiement d'une Application

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

:::exo
On testera la résilience du déploiement applicatif (et du `control-plane` **pour un cluster H/A uniquement**) :

1. Déconnecter ou simuler la défaillance d'un `control-plane` pour observer la capacité du cluster à basculer automatiquement (**si cluster H/A**).
2. Tester la suppression d'un conteneur / Pod
3. Tester la déconnexion d'un _worker node_
4. Vérifier la réconciliation des ressources
5. Vérifier le _scaling_ automatique en cas de pic de charge

   :::

## 📜 Livrables

- 📂 **Rapport détaillé** avec étapes et configurations
- 📜 **Code source** des manifestes Kubernetes
- 🎤 **Présentation** des résultats et démonstration
