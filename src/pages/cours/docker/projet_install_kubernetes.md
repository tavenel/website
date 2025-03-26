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

#### Pré-requis

Sur chaque `Node` :

- Désactiver le swap : `swapoff -a` et `fstab`
- Synchroniser les horloges
- Charger les modules noyau (avec `modprobe`) suivants : `overlay` et `br_netfilter`
- `sysctl -w net.netfilter.nf_conntrack_max=1000000`
- `echo "net.netfilter.nf_conntrack_max=1000000" >> /etc/sysctl.conf`
- Un runtime de conteneurs : `containerd`, `CRI-O`, `Docker`, …
- `Kubeadm`, `Kubelet` et `Kubectl`

Configuration réseau :

- Tous les _Node_ :
  - `kubelet` : 10250
  - Si utilisation de `BGP` : 179
- _Control Plane_ uniquement : 
  - `kube-apiserver` : 6443
	- `scheduler` : 10251
	- `controller-manager` : 10252
- Les _Node_ doivent pouvoir communiquer entre eux.

:::tip
On pourra tester la compatibilité d'un noeud du cluster avec le _Node Conformance Test_. Remplacer `$CONFIG_DIR` par le chemin du manifeste du kubelet :  `/etc/kubernetes/kubelet`,  `/etc/default/kubelet`,  `/etc/systemd/system/kubelet.service`, … `$LOG_DIR` est le chemin où stocker les résultats du test.

Pour plus d'information : <https://kubernetes.io/docs/setup/best-practices/node-conformance/>

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

#### Procédure

Les installations de clusters Kubernetes sont assez hétérogènes en fonction de l'environnement cible, du _CNI_ utilisé et de la distribution choisie (spécificités `k3s`, …). On retrouve cependant un schéma assez standard :

- Les noeuds _worker_ (noeuds qui exécutent les applications) n'ont besoin que d'un `kubelet` et d'un `kube-proxy` (le `kube-proxy` est optionnel dans de rares cas, par exemple si l'on utilise `Cilium` ou un `kube-router`). Les `kubelet` n'ont finalement besoin que d'un enregistrement auprès de l'`API Server`. La configuration du `kube-proxy` est en général assez simple car le _CNI_ s'occupe des couches basses (à vérifier auprès du _CNI_).
- Le(s) _control plane_ sont les noeuds d'administration. Ils servent donc à déployer un `API Server` qui permet de communiquer avec le client `kubectl` qui permet de gérer le cluster une fois déployé. Celui-ci a besoin de stocker de l'état : c'est le but du composant `etcd`. Il faut ensuite lui ajouter un `Control Manager` qui exécute l'intelligence du cluster par un ensemble de _controllers_ et un `Scheduler` qui permet de choisir le _Node_ qui exécutera un _Pod_. On ajoute normalement un `Kubelet` afin de gérer les _Pods_ du _control plane_ (il est possible de ne pas déployer les services du _control plane_ dans des _Pods_ mais d'utiliser par exemple `systemd`. Les clusters gérés par des fournisseurs de Cloud utilisent en général ce genre de déploiement, qui est assez rare _on-premise_). Le `Control Manager`, le `Scheduler` et le `Kubelet` n'ont besoin que d'être raccordés à l'`API Server`.
- Seul l'`etcd` (ou éventuellement la BDD dans le cas de `k3s`) gère l'**état** du cluster : c'est donc le composant critique, celui responsable majoritairement de la résilience du cluster : attention à ses pré-requis !

On effectue donc en principe l'odre de déploiement suivant :

- Création d'un 1er noeud _control plane_ (aussi appelé _master_) :
  - déploiement `etcd` (ou BDD).
  - déploiement `api-server` utilisant l'`etcd`.
	- création de la configuration du `kubelet`, déploiement et enregistrement auprès de l'`api-server`.
	- déploiement `control-manager` et `scheduler` et enregistrement auprès de l'`api-server`
- Création des autres _control plane_ :
  - déploiement des composants (similaire au 1er noeud) mais enregistrement des composants HA auprès du 1er _control plane_, notamment `api-server` et `etcd`.
  - choisir une solution de load balancing adaptée : `kube-vip`, `MetalLB`, …
  - mettre en place une stratégie de sauvegarde régulière de la base etcd et prévoir des mécanismes de restauration en cas de défaillance.
- Création des workers :
	- création de la configuration du `kubelet`, déploiement et enregistrement auprès de l'`api-server`.

##### Exemple de procédure d'installation sans haute disponibilité

```sh
# Init du control plane
kubeadm init --control-plane-endpoint "<IP_Bastion>:6443" --pod-network-cidr=192.168.0.0/16 --upload-certs --cri-socket unix:///run/containerd/containerd.sock
# Ajout des Node Worker en récupérant la sortie de la commande précédente
kubeadm join <IP_bastion>:6443 --token <TOKEN> --discovery-token-ca-cert-hash sha256:<HASH>
# Puis retour au control plane

# Config kubectl
sudo cat /etc/kubernetes/admin.conf > ~/.kube/config

# Le Node doit être NotReady
kubectl get nodes -A
NAME      STATUS     ROLES           AGE   VERSION
cplane1   NotReady   control-plane   51s   v1.31.6

# Installation du CNI (par exemple, Calico)
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml

# Passage du Node en Ready
kubectl get nodes -A
cplane1   Ready    control-plane   113s   v1.31.6
```

Ou par fichier de configuration :

```yaml
# kubeadm-config.yaml
kind: ClusterConfiguration
apiVersion: kubeadm.k8s.io/v1beta4
kubernetesVersion: v1.21.0
---
kind: KubeletConfiguration
apiVersion: kubelet.config.k8s.io/v1beta1
cgroupDriver: systemd
[…]
```

```sh
$ kubeadm init --config kubeadm-config.yaml
```


##### Avec H/A

```bash
# pré-requis : Bastion => Installation d'un HAProxy entre les OS des Control Plane

# Init du 1e master
kubeadm init --control-plane-endpoint "<IP_bastion>:6443" --pod-network-cidr=192.168.0.0/16 --upload-cert
# Join des autres control-plane
kubeadm join "<IP_bastion>:6443" --token "<TOKEN>" --discovery-token-ca-cert-hash "sha256:<HASH>" --control-plane --certificate-key "<HASH_CERT>"
# Join des workers
kubeadm join "<IP_bastion>:6443" --token "<TOKEN>" --discovery-token-ca-cert-hash "sha256:<HASH>"
# calico, …
```

#### API Server H/A

Chaque _Node_ : `kubelet`, `kube-proxy`, `kube-router`, … doivent se lier à l'`API Server` **dont l'accès doit être H/A**, avec plusieurs possibilités :

1. **Load Balancer externe** devant les _API Server_
  - _Kubelet_ pointe sur ce _load balancer_
  - si infra Cloud, souvent géré par le Cloud Provider
2. **Load Balancer local** : `Nginx`, `HAProxy`, … sur chaque _Node_ pour atteindre les _API Server_
  - _Kubelet_ pointe sur `localhost`
3. **round-robin DNS** pour tous les _API Server_ (officiellement non supporté)
4. H/A API endpoint dans un cluster managé, virtual IP, tunnel _Node_ <-> _API Server_ (`k3s`), …

#### Pods statiques

:::tip
Déployer le _Control Plane_ dans des _Pods_ permet de les gérer avec toute la puissance de Kubernetes… mais recquiert un cluster opérationnel !
Pour contourner cette limite, Kubernetes permet de déployer des _Pods_ directement dans le _Kubelet_ (sans passer par l'_API Server_) en utilisant des _manifest_. Le _Kubelet_ réconcilie les _Pods_ en cas de changement(s) dans le _manifest_. Voir [ces slides](https://2021-05-enix.container.training/5.yml.html#227) pour plus d'information.
:::

#### Sizing

:::tip
Dimensionner un cluster Kubernetes est très compliqué. Il est possible de redimensionner dynamiquement un cluster pendant son cycle de vie : voir ces slides sur le [Sizing de Cluster et le ClusterAutoscaler de Nodes](https://2021-05-enix.container.training/4.yml.html#248) et [Scaling with custom metrics](https://2021-05-enix.container.training/4.yml.html#334).
:::

#### Supervision

Voir [ces slides](https://2021-05-enix.container.training/5.yml.html#217) pour plus d'information sur les APIs internes et de monitoring

On pourra notamment monitorer a minima ces endpoints (`HTTP/tcp`, non authentifié) :

- `etcd` :
  - 2381 `/health` et `/metrics`
- `kubelet` :
  - 10248 `/healthz` retourne "ok"
- `kube-proxy` :
  - 10249 `/healthz` retourne "ok", `/configz`, `/metrics`
  - 10256 `/healthz` avec timestamp
- `kube-controller` & `kube-scheduler` :
  - 10257 (`kube-controller`) et 10259 (`kube-scheduler`) : `/healthz` (et `/configz` & `/metrics` en `HTTPS` avec authentification)

#### Contraintes

:::warn
Attention, on demande bien d'installer un cluster **production-ready** ! Celui-ci devra donc être en haute disponibilité (Load balancer devant l'API Server, …) et on réfléchira aux procédures d'administration, de sauvegarde, … On pourra cependant s'affranchir d'utiliser HTTPS, notamment pour la communication entre les différents composants (ce qui est bien sûr une obligation dans une "vraie" production).
:::

:::link
- Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/installation/>
- Documentation de référence : <https://kubernetes.io/docs/setup/production-environment/>
- Pour tester la sécurité du cluster, on pourra utiliser <https://github.com/aquasecurity/kube-bench> pour passer le benchmark CIS. 
:::

#### Exercice

:::exo
Réaliser l'installation du cluster Kubernetes en H/A :

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
4. On **testera** la partie H/A du `control-plane` :
   - Déconnecter ou simuler la défaillance d'un `control-plane` pour observer la capacité du cluster à basculer automatiquement.
   - Lancer un test de restauration de `etcd` à partir d'une sauvegarde et vérifier la cohérence du cluster.
:::

#### Administration

:::warn
Administrer un cluster Kubernetes ne se limite pas à son installation : il faut gérer les mises à jour, les maintenances, la sécurité, l'observabilité du cluster, … Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/administration/>
:::

##### Upgrade

```bash
apt-mark unhold kubeadm && apt-get update && apt-get install -y kubeadm='1.31.x-y.y' && apt-mark hold kubeadm
# Upgrade 1e control plane
kubeadm upgrade plan
kubeadm upgrade apply vX.Y.Z
systemctl restart kubelet
# Upgrade autres control plane
kubeadm upgrade apply
# Upgrade workers
kubectl drain "<node-name>" --ignore-daemonsets # retire tous les Pods
apt-get update && apt-get install -y kubelet kubectl && apt-mark hold kubelet kubectl
systemctl restart kubelet
kubectl uncordon "<node-name>" # fin du drainage
```

##### Renouvellement des certificats

```bash
kubectl get csr
kubeadm alpha certs renew all
```



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

:::exo
On testera la partie H/A du déploiement applicatif :

- Tester la suppression d'un conteneur / Pod
- Tester la déconnexion d'un _worker node_
- Vérifier la réconciliation des ressources
- Vérifier le _scaling_ automatique en cas de pic de charge
:::

## 📜 Livrables

- 📂 **Rapport détaillé** avec étapes et configurations
- 📜 **Code source** des manifestes Kubernetes
- 🎤 **Présentation** des résultats et démonstration

## Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- K8s® is a registered trademark of The Linux Foundation in the United States and/or other countries.

