---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Installation H/A
layout: '@layouts/CoursePartLayout.astro'
---

## 📌 Haute Disponibilité d'un Cluster Kubernetes

Dans un contexte de **production**, un cluster Kubernetes doit être conçu pour **tolérer la panne de composants critiques** sans interruption significative du service. La haute disponibilité (HA) couvre **le control plane** et la **résilience de l'etcd** - le datastore distribué qui contient tout l'état du cluster.

### Objectifs

La haute disponibilité dans un cluster Kubernetes vise à :

- **Éliminer le point de défaillance unique (SPOF)** de l'API server : ne pas dépendre d'un seul nœud pour l'accès au Kubernetes API.
- **Assurer la continuité de l'orchestration** : scheduler, contrôleurs et autoscaler doivent pouvoir continuer à fonctionner même si une instance tombe.
- **Maintenir l'état du cluster** : etcd doit rester disponible avec un quorum minimal de membres pour garantir cohérence et tolérance aux pannes.
- **Servir les workloads applicatifs** même si le control plane est partiellement indisponible.

### Architecture de référence HA

Un cluster Kubernetes HA conçu avec `kubeadm` repose sur les composants suivants :

- 🛠 Control Plane multiples
- 🧠 Base d'état etcd distribuée
- L'accès aux nœuds du control plane (`api-server`) se fait via un **point d'accès unique hautement disponible** (`ControlPlaneEndpoint`) en utilisant :
  - un **load balancer** TCP (`HAProxy` + `keepalived`)
  - une **virtual IP** (`kube-vip`)
  - un DNS _round-robin_
  - …

:::link
Voir aussi :

- <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/>
- <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/>

:::

## API Server H/A

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

## etcd H/A

`etcd` est le composant qui contient toutes les données du cluster, c'est donc le plus critique et il doit bien entendu être déployé en H/A (nombre impair, **5 recommandé**, 3 supporté).

Voir les documentations officielles : [HA etcd with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/) et [HA topology](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/) et [configure & upgrade etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)

:::tip
Il est possible de configurer `etcd` en H/A de 2 manières différentes (voir la documentation HA topology) :

- _stacked etcd_ : chaque _control plane_ possède un `APIServer` lié à un (et un seul) `etcd` installé dans le _control plane_.
- _external etcd_ : le cluster `etcd` est externe aux _control plane_ : chaque `APIServer` est connecté au cluster de tous les `etcd`.

:::

![Stacked etcd](@assets/k8s/kubeadm-ha-topology-stacked-etcd.svg)

<div class="caption">etcd en stack dans les control-plane. Source: https://kubernetes.io/images/kubeadm/kubeadm-ha-topology-stacked-etcd.svg</div>

![External etcd](@assets/k8s/kubeadm-ha-topology-external-etcd.svg)
<div class="caption">etcd externes. Source: https://kubernetes.io/images/kubeadm/kubeadm-ha-topology-external-etcd.svg</div>

:::link
Source des diagrammes et plus d'information : <https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/ha-topology/>
:::

## Procédure d'installation H/A

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
