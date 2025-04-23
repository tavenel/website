---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Pré-requis
layout: '@layouts/CoursePartLayout.astro'
---

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

