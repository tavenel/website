---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Procédure d'installation
layout: '@layouts/CoursePartLayout.astro'
---

Les installations de clusters Kubernetes sont assez hétérogènes en fonction de l'environnement cible, du _CNI_ utilisé et de la distribution choisie (spécificités `k3s`, …). On retrouve cependant un schéma assez standard :

- Les noeuds _worker_ (noeuds qui exécutent les applications) n'ont besoin que d'un `kubelet` et d'un `kube-proxy` (le `kube-proxy` est optionnel dans de rares cas, par exemple si l'on utilise `Cilium` ou un `kube-router`). Les `kubelet` n'ont finalement besoin que d'un enregistrement auprès de l'`API Server`. La configuration du `kube-proxy` est en général assez simple car le _CNI_ s'occupe des couches basses (à vérifier auprès du _CNI_).
- Le(s) _control plane_ sont les noeuds d'administration. Ils servent donc à déployer un `API Server` qui permet de communiquer avec le client `kubectl` qui permet de gérer le cluster une fois déployé. Celui-ci a besoin de stocker de l'état : c'est le but du composant `etcd`. Il faut ensuite lui ajouter un `Control Manager` qui exécute l'intelligence du cluster par un ensemble de _controllers_ et un `Scheduler` qui permet de choisir le _Node_ qui exécutera un _Pod_. On ajoute normalement un `Kubelet` afin de gérer les _Pods_ du _control plane_ (il est possible de ne pas déployer les services du _control plane_ dans des _Pods_ mais d'utiliser par exemple `systemd`. Les clusters gérés par des fournisseurs de Cloud utilisent en général ce genre de déploiement, qui est assez rare _on-premise_). Le `Control Manager`, le `Scheduler` et le `Kubelet` n'ont besoin que d'être raccordés à l'`API Server`.
- Seul l'`etcd` (ou éventuellement la BDD dans le cas de `k3s`) gère l'**état** du cluster : c'est donc le composant critique, celui responsable majoritairement de la résilience du cluster : attention à ses prérequis !

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

## Exemple de procédure d'installation sans haute disponibilité

```sh
# Init du control plane
kubeadm init --cri-socket unix:///run/containerd/containerd.sock --upload-certs
# Ajout des Node Worker en récupérant la sortie de la commande précédente
kubeadm join "<IP_control_plane>:6443" --token "<TOKEN>" --discovery-token-ca-cert-hash "sha256:<HASH>"
# Puis retour au control plane

# Config kubectl
sudo cat /etc/kubernetes/admin.conf > ~/.kube/config

# Le Node doit être NotReady
kubectl get nodes -A
NAME      STATUS     ROLES           AGE   VERSION
cplane1   NotReady   control-plane   51s   v1.31.6

# Installation du CNI, par exemple :
## Flannel : https://github.com/flannel-io/flannel
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
## Calico : https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/onpremises
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.29.3/manifests/tigera-operator.yaml
curl https://raw.githubusercontent.com/projectcalico/calico/v3.29.3/manifests/custom-resources.yaml -o calico.yaml
kubectl create -f calico.yaml # modifier le fichier avant (bgp: Disabled, CIDR, …)

# Passage du Node en Ready
kubectl get nodes -A
cplane1   Ready    control-plane   113s   v1.31.6
```

Ou par fichier de configuration :

```yaml
# kubeadm-config.yaml
# A retrouver après installation dans : /var/lib/kubelet/config.yaml
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
kubeadm init --config kubeadm-config.yaml --upload-certs
```

:::warn
Forcer un CIDR pour le réseau des pods peut être obligatoire pour certains CNI (_Calico_) :

```sh
kubeadm init … –pod-network-cidr=100.0.0/16
```
:::

## Avec H/A

```sh
# prérequis : Bastion =>
# - Soit : Installation d'un HAProxy entre les OS des Control Plane
# - Soit : Déploiement d'un kube-vip en utilisant un manifest de Pod statique pendant l'init
# - Soit : Déférer le H/A après l'installation du 1er control plane (k3s)

# Init du 1e master
kubeadm init --control-plane-endpoint "<IP_bastion>:6443" --pod-network-cidr=100.0.0.0/16 --upload-certs
# Join des autres control-plane
kubeadm join "<IP_bastion>:6443" --token "<TOKEN>" --discovery-token-ca-cert-hash "sha256:<HASH>" --control-plane --certificate-key "<HASH_CERT>"
# Join des workers
kubeadm join "<IP_bastion>:6443" --token "<TOKEN>" --discovery-token-ca-cert-hash "sha256:<HASH>"
# calico, …
```


## Pods statiques

:::tip
Déployer le _Control Plane_ dans des _Pods_ permet de les gérer avec toute la puissance de Kubernetes… mais recquiert un cluster opérationnel !
Pour contourner cette limite, Kubernetes permet de déployer des _Pods_ dits _statiques_ directement dans le _Kubelet_ (sans passer par l'_API Server_) en utilisant des _manifest_ : c'est ce que fait _kubeadm_ à l'initialisation du cluster : fichiers `/etc/kubernetes/manifests/`. Le _Kubelet_ réconcilie les _Pods_ en cas de changement(s) dans le _manifest_. Voir [ces slides](https://2021-05-enix.container.training/5.yml.html#227) pour plus d'information.
:::

## Sizing

:::tip
Dimensionner un cluster Kubernetes est très compliqué. Il est possible de redimensionner dynamiquement un cluster pendant son cycle de vie : voir ces slides sur le [Sizing de Cluster et le ClusterAutoscaler de Nodes](https://2021-05-enix.container.training/4.yml.html#248) et [Scaling with custom metrics](https://2021-05-enix.container.training/4.yml.html#334). Pour information, la base `etcd` ne doit normalement pas dépasser 2GB.
:::

