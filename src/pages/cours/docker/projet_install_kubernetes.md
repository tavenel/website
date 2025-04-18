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
- **Synchroniser les horloges**
- Un runtime de conteneurs : `containerd`, `CRI-O`, `Docker`, …
- `Kubeadm`, `Kubelet` et `Kubectl`

:::tip
Kubernetes impose un peu de tuning du noyau Linux : 

- Charger les modules noyau `overlay` et `br_netfilter`
- Appliquer les paramètres de configuration du noyau (`sysctl`) suivants :

```ini
kernel.panic=10
kernel.panic_on_oops=1
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
net.netfilter.nf_conntrack_max=1000000
vm.overcommit_memory=1
```
:::

:::warn
Si vous tournez le cluster sur votre machine personnelle dans des VMs, Kubernetes peut être très gourmand en I/O. 

Appliquer également les paramètres suivants :

```ini
fs.inotify.max_user_instances=1024
fs.inotify.max_user_watches=1048576
```
:::

:::warn
Docker n'est plus supporté nativement par Kubernetes, il faut un _Container Runtime Interface_ (CRI), par exemple `cri-dockerd`. On utilise souvent `containerd` directement (sans Docker). Voir : <https://kubernetes.io/docs/setup/production-environment/container-runtimes/>
:::

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

##### Avec H/A

```bash
# pré-requis : Bastion =>
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

#### API Server H/A

Chaque _Node_ : `kubelet`, `kube-proxy`, `kube-router`, … doivent se lier à l'`API Server` **dont l'accès doit être H/A**, avec plusieurs possibilités. Dans tous les cas, `kubectl` doit utiliser l'accès H/A publique.

1. **Load Balancer externe** devant les _API Server_
  - _Kubelet_ pointe sur ce _load balancer_
  - si infra Cloud, souvent géré par le Cloud Provider
  - voir : <https://kifarunix.com/setup-highly-available-kubernetes-cluster-with-haproxy-and-keepalived/>
2. **Load Balancer local** : `Nginx`, `HAProxy`, … sur chaque _Node_ pour atteindre les _API Server_
  - _Kubelet_ pointe sur `localhost`
3. **round-robin DNS** pour tous les _API Server_ (officiellement non supporté mais aucun impact sur Kubernetes)
4. **Autres** : H/A API endpoint dans un cluster managé, virtual IP Cloud, tunnel _Node_ <-> _API Server_ (`k3s`), …

:::tip
À l'initialisation du cluster (fichier `ClusterConfiguration` ou ligne de commande) :

- `localAPIEndpoint` est l'endpoint local de l'instance de l'api-server sur le noeud courant.
- Dans un cluster comportant plusieurs instances de _control-plane_, le champ `controlPlaneEndpoint` doit contenir l'adresse "publique" du cluster, par exemple _load-balancer_ externe placé devant les instances du _control-plane_.
- Dans un cluster sans haute disponibilité, `controlPlaneEndpoint` et `localAPIEndpoint` ont la même valeur.
- Voir : [ClusterConfiguration: localAPIEndpoint et controlPlaneEndpoint](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#considerations-about-apiserver-advertise-address-and-controlplaneendpoint)
:::

:::tip
Dans de rares cas (par exemple _k3s_), il est possible de passer d'un cluster mono control-plane à un cluster H/A à tout moment.

Mais la plupart du temps (_kubeadm_ par exemple) il n'est pas supporté de changer le `controlPlaneEndpoint`. Une solution est d'utiliser systématiquement un nom DNS dans `controlPlaneEndpoint` qui pourra être :

- Temporairement, l'IP du _control plane_ principal
- Ensuite, la Virtual IP du Load Balancer, …
:::

:::tip
_kube-vip_ permet de déployer un _load-balancer_ pour des control plane H/A, et pour faire office de service `LoadBalancer` :

- Si cluster installé par `kubeadm` : néessite une _virtual IP_ à l'installation : la _VIP_ est déployée en _Static Pod_ et stackée dans le 1er _control-plane_.
  - les autres _control-plane_ rejoignent la _VIP_ et _kube-vip_ gère la réplication de la _VIP_.
- Si cluster _k3s_, la _VIP_ n'a pas besoin d'être présente à l'initialisation du cluster : celle-ci peut être déployée en `DaemonSet` sur chacun des _Node_.
:::

![Diagramme HA Proxy en frontal de l'api-server](https://cdn.jsdelivr.net/gh/b0xt/sobyte-images/2021/09/27/6c1e741a356141a5964e3a64a241ce86.png)

<div class="caption">Diagramme HA Proxy en frontal de l'api-server.</div>

![Diagramme kube-vip stacké dans le control-plane](https://cdn.jsdelivr.net/gh/b0xt/sobyte-images/2021/09/27/6cc2dccc26ac4260bb564a9a4a002670.png)

<div class="caption">Diagramme kube-vip stacké dans le control-plane.</div>

:::link
- Source des diagrammes et plus d'information : <https://www.sobyte.net/post/2021-09/use-kube-vip-ha-k8s-lb/>
- Voir aussi : <https://kifarunix.com/setup-highly-available-kubernetes-cluster-with-haproxy-and-keepalived/>
- Pour K3s, voir <https://docs.k3s.io/architecture#high-availability-k3s>
:::

#### etcd H/A

`etcd` est le composant qui contient toutes les données du cluster, c'est donc le plus critique et il doit bien entendu être déployé en H/A (nombre impair, **5 recommandé**, 3 supporté).

Voir les documentations officielles : [HA etcd with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/) et [HA topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/) et [configure & upgrade etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)

:::tip
Il est possible de configurer `etcd` en H/A de 2 manières différentes (voir la documentation HA topology) :

- _stacked etcd_ : chaque _control plane_ possède un `APIServer` lié à un (et un seul) `etcd` installé dans le _control plane_.
- _external etcd_ : le cluster `etcd` est externe aux _control plane_ : chaque `APIServer` est connecté au cluster de tous les `etcd`.
:::

![Stacked etcd](https://kubernetes.io/images/kubeadm/kubeadm-ha-topology-stacked-etcd.svg)

<div class="caption">etcd en stack dans les control-plane</div>

![External etcd](https://kubernetes.io/images/kubeadm/kubeadm-ha-topology-external-etcd.svg)
<div class="caption">etcd externes</div>

:::link
Source des diagrammes et plus d'information : <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/>
:::

#### Pods statiques

:::tip
Déployer le _Control Plane_ dans des _Pods_ permet de les gérer avec toute la puissance de Kubernetes… mais recquiert un cluster opérationnel !
Pour contourner cette limite, Kubernetes permet de déployer des _Pods_ dits _statiques_ directement dans le _Kubelet_ (sans passer par l'_API Server_) en utilisant des _manifest_ : c'est ce que fait _kubeadm_ à l'initialisation du cluster : fichiers `/etc/kubernetes/manifests/`. Le _Kubelet_ réconcilie les _Pods_ en cas de changement(s) dans le _manifest_. Voir [ces slides](https://2021-05-enix.container.training/5.yml.html#227) pour plus d'information.
:::

#### Sizing

:::tip
Dimensionner un cluster Kubernetes est très compliqué. Il est possible de redimensionner dynamiquement un cluster pendant son cycle de vie : voir ces slides sur le [Sizing de Cluster et le ClusterAutoscaler de Nodes](https://2021-05-enix.container.training/4.yml.html#248) et [Scaling with custom metrics](https://2021-05-enix.container.training/4.yml.html#334). Pour information, la base `etcd` ne doit normalement pas dépasser 2GB.
:::

#### Versions et upgrade

- Kubernetes suit un versionning _sémantique_ vMAJOR.MINOR.PATCH (ex 1.28.9).
- Il est _recommandé_ (pas obligatoire) d'exécuter des versions homogènes sur l'ensemble du cluster mais :
- Les `APIServer` (en H/A) peuvent avoir différentes versions
  - et donc le résultat de `kubectl` peut être … exotique !
- Différents _Node_ peuvent exécuter différentes versions de `Kubelet` et/ou du noyau Linux et/ou différents engines de conteneurs
- Les composants peuvent être mis à niveau un par un sans problème (c'est même recommandé).
- Il est toujours possible de combiner différentes versions de _PATCH_ (par exemple, 1.28.9 et 1.28.13 sont compatibles) mais il est recommandé de toujours mettre à jour vers la dernière version de _PATCH_
- **L'`APIServer` doit être plus récent** que ses clients (`Kubelet` et _Control Plane_), donc **être mis à jour en premier**
- Tous les composants supportent (au moins) une **différence d'une version _MINEURE_** => upgrade à chaud possible
- Voir [la documentation sur les versions non homogènes](https://kubernetes.io/releases/version-skew-policy/)
- Mettre à jour avec **le même outil qui a servi à l'installation du composant** : gestionnaire de package, `kubeadm`, Pod, conteneur, …
- En moyenne, **une mise à jour tous les 3 mois**

#### Debug

- Tester localement kubectl sur un control plane

```sh
export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl get nodes -o wide
```

- Vérifier les logs du kubelet

```sh
systemctl kubelet
journalctl -xeu kubelet
```

- Inspecter les conteneurs

```sh
crictl --runtime-endpoint unix:///run/containerd/containerd.sock ps -a | grep -v pause
crictl --runtime-endpoint unix:///run/containerd/containerd.sock logs …
```

:::tip
En _k3s_, le _kubelet_ est directement intégré dans le service de _k3s_ => dans le service systemd `k3s` (_master_) ou `k3s-agent` (_worker_).
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

:::warn
Attention, on demande bien d'installer un cluster **production-ready** ! Celui-ci devra donc être en haute disponibilité (Load balancer devant l'API Server, …) et on réfléchira aux procédures d'administration, de sauvegarde, … On pourra cependant s'affranchir d'utiliser HTTPS, notamment pour la communication entre les différents composants (ce qui est bien sûr une obligation dans une "vraie" production).
:::

:::link
- Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/installation/>
- Documentation de référence : <https://kubernetes.io/docs/setup/production-environment/>
- Pour tester la sécurité du cluster, on pourra utiliser <https://github.com/aquasecurity/kube-bench> pour passer le benchmark CIS. 
- Voir aussi : <https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/>
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

:::exo
On testera la partie H/A du `control-plane` et du déploiement applicatif :

- Déconnecter ou simuler la défaillance d'un `control-plane` pour observer la capacité du cluster à basculer automatiquement.
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

