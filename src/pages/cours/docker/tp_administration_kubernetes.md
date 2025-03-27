---
title: 📌 Administration de cluster Kubernetes
date: 2024 / 2025
---

## Objectifs

Administrer un cluster Kubernetes ne se limite pas à son installation : il faut gérer les mises à jour, les maintenances, la sécurité, l'observabilité du cluster, …

Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/administration/>.

## Supervision

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

## Renouvellement des certificats

Exemple de procédure pour renouveller les certificats du cluster en utilisant `kubeadm` :

```bash
kubectl get csr
kubeadm alpha certs renew all
```

## Upgrade

### Versions et upgrade

- Kubernetes suit un versionning _sémantique_ vMAJOR.MINOR.PATCH (ex 1.28.9).
- Il est _recommandé_ (pas obligatoire) d'exécuter des versions homogènes sur l'ensemble du cluster mais :
- Les `APIServer` (en H/A) peuvent avoir différentes versions
- Différents _Node_ peuvent exécuter différentes versions de `Kubelet`
- Différents _Node_ peuvent exécuter différentes versions du noyau
- Différents _Node_ peuvent exécuter différents engines de conteneurs
- Les composants peuvent être mis à niveau un par un sans problème.
- Il est toujours possible de combiner différentes versions de _PATCH_ (par exemple, 1.28.9 et 1.28.13 sont compatibles) mais il est recommandé de toujours mettre à jour vers la dernière version de _PATCH_
- **L'`APIServer` doit être plus récent** que ses clients (`Kubelet` et _Control Plane_), donc **être mis à jour en premier**
- Tous les composants supportent (au moins) une **différence d'une version _MINEURE_** => upgrade à chaud possible
- Voir [la documentation sur les versions non homogènes](https://kubernetes.io/releases/version-skew-policy/)
- Mettre à jour avec **le même outil qui a servi à l'installation du composant** : gestionnaire de package, `kubeadm`, Pod, conteneur, …
- En moyenne, **une mise à jour tous les 3 mois**

### Procédure

:::link
L'upgrade d'un cluster suit [la procédure officielle de la documentation](https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/)
:::

:::warn
- Lors de l'upgrade d'un `Kubelet`, il est recommandé de le _boucler_ (_cordon_) par la commande `kubectl drain` pour retirer tous les Pods exécutés sur celui-ci au préalable.
- Le déplacement de pods _stateful_ (BDD, …) peut entraîner des interruptions de service ! Utiliser la réplication de BDD (switch de l'instance _primaire_ sur le _Node_ non impacté) - certains `Operator` (ex [CNPG](https://cloudnative-pg.io/)) effectuent ce basculement automatiquement lorsqu'ils détectent qu'un _Node_ devient _cordon_.
:::

Exemple simplifié de procédure d'upgrade avec `kubeadm` (pour plus d'information, suivre [la documentation officielle](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)). Voir aussi [la formation de Jérôme Petazzo](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/cluster-upgrade.md)

```bash
# Upgrade kubeadm
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

## Backup de clusters

- Les sauvegardes peuvent avoir plusieurs objectifs :
  - Reprise après sinistre (serveurs ou stockage détruits ou inaccessibles)
  - Reprise après incident (données altérées ou corrompues par un humain ou un processus)
  - Clonage d'environnements (pour tests, validation…)
- Kubernetes :
  - facilite la reprise après sinistre (primitives de réplication)
  - facilite la réplication d'environnements (toutes les ressources peuvent être décrites avec des manifests)
  - n'offre **aucune aide sur la reprise après incident** : continuez les sauvegardes de données (BDD, storage, disques), voir même backup complet du _Control Plane_
- **Sauvegardez les informations TLS** (minimum : clé et certificat du CA + de l'APIServer)
  - si installé par `kubeadm`, dans `/etc/kubernetes/pki`
- **Sauvegardez les `PersistentVolume`** :
  - par le système de stockage (SAN, Cloud, …)
  - par des outils dédiés : voir [outils Kubernetes](/tools#-kubernetes-specific)
  - par [l'API Kubernetes](https://kubernetes.io/docs/concepts/storage/volume-snapshots/)

:::tip
Automatiser le (re)déploiement d'un cluster (GitOps) peut être une procédure de recovery efficace mais risquée (ne rien oublier !) : continuez les backup d'`etcd`.
:::

### Backup etcd

- Contient tous les objets du cluster (metadata : taille faible)
- **ne sauvegarde pas** les PV ni les données stockées localement dans les _Node_

#### Procédure pour clusters `kubeadm`

- Choisir un _control plane_
- Trouver l'image _etcd_
- `etcdctl snapshot` dans un _debug container_ car :
  - le système de fichiers hôte est monté dans `/host`,
  - le _Pod_ de debug utilise le réseau de l'hôte
- Transférer le _snapshot_ grâce à un autre debug container_ en _base64_ pour éviter toute corruption.
- Source et crédits : [Backup Cluster - Jérôme Petazzo](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/cluster-backup.md)

```sh
# Obtenir le nom d'un _Node_ du _Controle Plane_ :
NODE=$(kubectl get nodes \
--selector=node-role.kubernetes.io/control-plane \
-o jsonpath={.items[0].metadata.name})

# Obtenir l'image etcd :
IMAGE=$(kubectl get pods --namespace kube-system etcd-$NODE \
-o jsonpath={..containers[].image})

# Exécuter `etcdctl` dans un _Pod_ de debug :
kubectl debug --attach --profile=general \
node/$NODE --image $IMAGE -- \
etcdctl --endpoints=https://[127.0.0.1]:2379 \
--cacert=/host/etc/kubernetes/pki/etcd/ca.crt \
--cert=/host/etc/kubernetes/pki/etcd/healthcheck-client.crt \
--key=/host/etc/kubernetes/pki/etcd/healthcheck-client.key \
snapshot save /host/tmp/snapshot

# Transférer le snapshot :
kubectl debug --attach --profile=general --quiet \
node/$NODE --image $IMAGE -- \
base64 /host/tmp/snapshot | base64 -d > snapshot
```

### Restauration etcd

:::warn
Pas de restauration d'etcd si des `APIServer` sont en cours d'exécution !

1. Arrêter toutes les instances d'`APIServer`
2. Restaurer l'état de toutes les instances `etcd`
3. Redémarrer toutes les instances d'`APIServer`

Il est également recommandé de redémarrer les composants Kubernetes (`kube-scheduler`, `kube-controller-manager`, `kubelet`) afin de s'assurer qu'ils ne reposent pas sur des données obsolètes (normalement automatique car la restauration prend du temps et les composants perdent leur lien vers l'etcd donc redémarrent).
:::

:::warn
`etcdutl restore` crée un nouveau répertoire de données à partir du snapshot mais ne met pas à jour le serveur `etcd` en cours d'exécution.
:::

- Voir aussi la [documentation etcd snapshot and restore](https://coreos.com/etcd/docs/latest/op-guide/recovery.html#snapshotting-the-keyspace)
- Source et crédits : [Backup Cluster - Jérôme Petazzo](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/cluster-backup.md)

#### Procédure kubeadm

```bash
# 1. Créer un nouveau répertoire de données à partir du snapshot :
sudo rm -rf /var/lib/etcd
docker run --rm -v /var/lib:/var/lib -v $PWD:/vol $IMAGE \
etcdutl snapshot restore /vol/snapshot --data-dir=/var/lib/etcd

# 2. Provisionner le _Control Plane_ à l'aide de ce répertoire :
sudo kubeadm init \
--ignore-preflight-errors=DirAvailable--var-lib-etcd

# 3. Rejoindre les autres nœuds
```


