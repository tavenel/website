---
title: 🏆 Administration de cluster Kubernetes
date: 2024 / 2025
type: tp
sidebar:
  order: 250
description: 🏆 Administration de cluster Kubernetes
---
## Objectifs

Administrer un cluster Kubernetes ne se limite pas à son installation : il faut gérer les mises à jour, les maintenances, la sécurité, l'observabilité du cluster, …

:::note
Voir aussi :

- <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/administration/>.
- <https://kubernetes.io/docs/tasks/debug/debug-cluster/> et les sous-sections

:::

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

:::note
Des outils dédiés permettent de faire un backup de cluster : _Stash_, _Velero_, …
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
- Source et crédits : [Backup Cluster - Jérôme Petazzoni](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/cluster-backup.md)

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

:::caution
Pas de restauration d'etcd si des _APIServer_ sont en cours d'exécution !

1. Arrêter toutes les instances d'_APIServer_
2. Restaurer l'état de toutes les instances _etcd_
3. Redémarrer toutes les instances d'_APIServer_

Il est également recommandé de redémarrer les composants Kubernetes (`kube-scheduler`, `kube-controller-manager`, `kubelet`) afin de s'assurer qu'ils ne reposent pas sur des données obsolètes (normalement automatique car la restauration prend du temps et les composants perdent leur lien vers l'etcd donc redémarrent).
:::

:::tip
Si _etcd_ est démarré en Pod statique par le _kubelet_ (cluster _kubeadm_), il suffit d'enlever **temporairement** le manifest `/etc/kubernetes/manifests/etcd.yaml` pour arrêter temporairement l'_etcd_ et continuer à tourner le cluster (attendre ~ 1 minute).

Vérifier avec le runtime de conteneurs que l'etcd est arrêté, par exemple :

```sh
crictl ps
```
:::

:::caution
`etcdutl restore` crée un nouveau répertoire de données à partir du snapshot mais ne met pas à jour le serveur `etcd` en cours d'exécution.
:::

:::note

- Voir aussi la [documentation etcd snapshot and restore](https://coreos.com/etcd/docs/latest/op-guide/recovery.html#snapshotting-the-keyspace)
- Un [environnement de test pour etcd](https://kodekloud.com/playgrounds/playground-ha-etcd-cluster)
- Source et crédits : [Backup Cluster - Jérôme Petazzoni](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/cluster-backup.md)

:::

#### Procédure kubeadm

```sh
# 1. Créer un nouveau répertoire de données à partir du snapshot :
sudo rm -rf /var/lib/etcd
docker run --rm -v /var/lib:/var/lib -v $PWD:/vol $IMAGE \
etcdutl snapshot restore /vol/snapshot --data-dir=/var/lib/etcd

# 2. Provisionner le _Control Plane_ à l'aide de ce répertoire :
sudo kubeadm init \
--ignore-preflight-errors=DirAvailable--var-lib-etcd

# 3. Rejoindre les autres nœuds
```

#### Procédure k3s

:::note
Voir : <https://docs.k3s.io/cli/etcd-snapshot?etcdsnap=Multiple+Servers#restoring-snapshots>
:::

### Exercice

:::exo

1. Assurer la sauvegarde et la résilience : Mettre en place une stratégie de sauvegarde régulière de la base etcd et prévoir des mécanismes de restauration en cas de défaillance.
2. Lancer un test de restauration de `etcd` à partir d'une sauvegarde et vérifier la cohérence du cluster.

:::

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

:::note
L'upgrade d'un cluster suit [la procédure officielle de la documentation](https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/)
:::

:::caution

- Lors de l'upgrade d'un `Kubelet`, il est recommandé de le _boucler_ (_cordon_) par la commande `kubectl drain` pour retirer tous les Pods exécutés sur celui-ci au préalable.
- Le déplacement de pods _stateful_ (BDD, …) peut entraîner des interruptions de service ! Utiliser la réplication de BDD (switch de l'instance _primaire_ sur le _Node_ non impacté) - certains `Operator` (ex [CNPG](https://cloudnative-pg.io/)) effectuent ce basculement automatiquement lorsqu'ils détectent qu'un _Node_ devient _cordon_.

:::

Exemple simplifié de procédure d'upgrade avec `kubeadm` (pour plus d'information, suivre [la documentation officielle](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)). Voir aussi [la formation de Jérôme Petazzoni](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/cluster-upgrade.md)

```sh
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

### Exercice

:::exo

1. Décrire une procédure de mise à jour pour votre cluster.
2. Tester la procédure en mettant à jour votre cluster.

:::

## Supervision

Un cluster Kubernetes doit bien sûr être supervisé. On utilise très majoritairement le couple _Prometheus_ / _Grafana_ : voir [le TP dédié pour l'installation de Prometheus & Grafana via Helm](/k8s/tp-prometheus-grafana).

### Endpoints

:::note
Voir [ces slides](https://2021-05-enix.container.training/5.yml.html#217) pour plus d'information sur les APIs internes et de monitoring
:::

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

### node-problem-detector

De nombreux problèmes peuvent affecter les Pods exécutés sur le Node, tels que :

- Problèmes de daemon d'infrastructure : service NTP indisponible ;
- Problèmes matériels : processeur, mémoire ou disque défectueux ;
- Problèmes de noyau : deadlock du noyau, système de fichiers corrompu ;
- Problèmes d'exécution du conteneur : démon d'exécution qui ne répond pas ;
- …

Ces problèmes sont invisibles pour les composants de gestion du cluster : Kubernetes continuera donc à planifier les Pods vers les Nodes défectueux.

Pour résoudre ce problème, _node-problem-detector_ introduit un nouveau _daemon_ qui collecte les problèmes de Nodes provenant de différents daemons et les rend visibles pour les composants d'administration du cluster.

Concrètement, _node-problem-detector_ utilise les _Event_ et les _NodeCondition_ pour signaler les problèmes à l'_apiserver_ :

- `NodeCondition` : un problème permanent rendant le Node indisponible pour les Pods
- `Event` : un problème temporaire ayant un impact limité sur le Pod, mais présentant un intérêt informatif

Un système de correction (_Remedy system_) est un ou plusieurs processus conçus pour tenter de résoudre les problèmes détectés par le _node-problem-detector_. Les systèmes de correction observent les _Event_ et/ou les _NodeCondition_ émis et prennent les mesures nécessaires pour rétablir l'intégrité du cluster Kubernetes.

:::note
Pour plus d'information, voir le dépôt du projet : <https://github.com/kubernetes/node-problem-detector>
:::

#### Installation

Une façon simple d'installer le _node-problem-detector_ consiste à passer par une _Helm Chart_. Celle-ci déploie un `DaemonSet` (sur chacun des _Node_ du cluster).

```sh
helm repo add deliveryhero https://charts.deliveryhero.io/
helm install --generate-name deliveryhero/node-problem-detector
```

### Exercice

:::exo

1. Mettre en place la supervision du cluster en installant une stack _Prometheus_ / _Grafana_.
2. Créer un (ou plusieurs) tableau(x) de bord dans Grafana de supervision de votre cluster et de votre application.
3. Déployer un _node-problem-detector_ sur chaque _Node_ du cluster
4. (Bonus) mettre en place des systèmes de correction en cas de problème sur un _Node_.

:::

## Sécurité

### Sécurisation du cluster

De nombreux composants acceptent les connexions (et les requêtes) d'autres composants : `api-server`, `etcd`, `Kubelet`
Nous devons sécuriser ces connexions pour refuser les requêtes non autorisées et pour empêcher l'interception de secrets, de _tokens_ et d'autres informations sensibles
Sécuriser les control-plane en mettant en place une communication sécurisée entre composants (voir cours).

### Renouvellement des certificats

Exemple de procédure pour renouveller les certificats du cluster en utilisant `kubeadm` :

```sh
kubeadm certs check-expiration
kubectl get csr
# If you are running cluster with a replicated control plane, this command
# needs to be executed on all the control-plane nodes.
kubeadm alpha certs renew all
```

:::note
Pour la procédure complète, voir la documentation : <https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/#manual-certificate-renewal>
:::

### Role-Based Access Control (RBAC)

Mettre en place un système de role pour :

- Sécuriser votre application
- Créer un compte de support ayant le droit d'afficher des informations sur le cluster mais pas de le modifier.

### NetworkPolicies

Par défaut, un Pod peut communiquer avec tout autre Pod/Service de tout Namespace, ce qui n'est pas idéal ! Les `NetworkPolicies` permettent de segmenter le traffic réseau (voir cours).

:::tip
Certains CNI ne supportent pas (totalement) les `NetworkPolicies` : la ressource est appliquée mais sans effet ! C'est le cas par exemple de _Flannel_ (même s'il est possible de lui ajouter une partie de _Calico_ pour fixer ce problème : _Canal_ ou d'utiliser [Kube Network Policies](https://github.com/flannel-io/flannel/blob/master/Documentation/netpol.md) ).

Dans notre cas, on ne demande pas de réinstaller un nouveau CNI mais de définir des NetworkPolicies pour le projet (par exemple, dans le plan de changer un jour de CNI).
:::

:::caution
Attention à ne pas bloquer les communications attendues par Kubernetes ! Par exemple, on ne demande pas de définir de NetworkPolicy dans le Namespace: `kube-system`.
:::

### Audit

Une fois le cluster sécurisé, nous allons auditer les rôles disponibles sur celui-ci.

Cet audit peut se réaliser par des plugins `kubectl` (installables par `krew`) :

- `kubectl who-can` / [kubectl-who-can](https://github.com/aquasecurity/kubectl-who-can) by Aqua Security
- `kubectl access-matrix` / [Rakkess (Review Access)](https://github.com/corneliusweig/rakkess) by Cornelius Weig
- `kubectl rbac-lookup` / [RBAC Lookup](https://github.com/FairwindsOps/rbac-lookup) by FairwindsOps
- `kubectl rbac-tool` / [RBAC Tool](https://github.com/alcideio/rbac-tool) by insightCloudSec

Il est bien entendu également nécessaire d'auditer les actions réellement réalisées sur le cluster, à intégrer à la supervision.

### Sealed Secret

:::caution
Par défaut, les secrets Kubernetes ne sont pas chiffrés mais seulement encodés en base 64 !
:::

Des outils externes permettent d'ajouter du chiffrement, on pourra par exemple utiliser _Kubeseal_ pour que seul le cluster soit capable de déchiffrer un secret.

:::note

- Voir la [cheatsheet Kubernetes sur Kubeseal](/k8s/cheatsheet#kubeseal)
- Sur K3s, on peut aussi utiliser la capacité de chiffrage des secrets intégrée à k3s : <https://docs.k3s.io/security/secrets-encryption>

:::

### Ingress SSL

Pour pouvoir accéder à l'application en HTTPS, on utilisera un Ingress SSL. Pour cela, il faut :

- Un contrôleur Ingress installé (ex : `Traefik`)
- Option 1 : générer un certificat manuellement => il faudra gérer manuellement son cycle de vie !
- Option 2 : utiliser `cert-manager` pour automatiser la génération du certificat :
  - par _Let's Encrypt_ si le nom de domaine pointe vers l'IP publique du contrôleur Ingress
  - en test, on pourra [simuler la génération de certificats HTTPS avec Pebble](https://blog.manabie.io/2021/11/simulate-https-certificates-acme-k8s/)

:::tip
Pour générer un certificat SSL manuellement :

1. Générer un certificat SSL

```sh
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -out tls.crt -keyout tls.key \
  -subj "/CN=example.com/O=example"
```

2. Créer un Secret Kubernetes TLS

```sh
kubectl create secret tls example-tls \
  --cert=tls.crt \
  --key=tls.key \
  -n default
```

:::

:::note
Voir aussi :

- La [cheatsheet Kubernetes](/k8s/cheatsheet#tls--clusterissuer-lets-encrypt)
- [Traefik Ingress Controller : TLS](https://doc.traefik.io/traefik/reference/routing-configuration/kubernetes/ingress/#tls)
- [Documentation Cert-Manager](https://cert-manager.io/docs/)

:::

### Exercice

:::exo

1. Sécuriser les control-plane en mettant en place une communication sécurisée entre composants.
2. Mettre en place et tester une procédure de renouvellement des certificats.
3. Mettre en place et tester des rôles de sécurité (RBAC) pour :

- sécuriser votre application ;
- créer un compte de support pouvant lister les ressources principales du cluster sans pouvoir y apporter de modification.

4. Mettre en place des NetworkPolicies pour votre application.
5. Mettre en place un audit des droits sur le cluster.
6. Chiffrer les secrets avec _Kubeseal_.
7. (Bonus) Configurer un Ingress en HTTPS pour accéder à votre application.

:::
