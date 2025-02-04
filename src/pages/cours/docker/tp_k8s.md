---
title: Kubernetes
date: 2024 / 2025
correction: false
---

# Introduction à Kubernetes®

Dans cette partie, nous allons utiliser l’orchestrateur de conteneurs Kubernetes pour gérer le déploiement, la configuration et l’équilibrage de charge des conteneurs créés par Docker. Le déploiement se fera dans un mono-cluster de test.

## Installation

### Installer Minikube ou k3s

Le déploiement de Kubernetes dans un environnement de production est une étape complexe, nécessitant de nombreuses questions sur le paramétrage (nombre de noeuds, redondance, services de stockage distribués, …).

Pour tester l’utilisation de Kubernetes, vous pouvez :

- Utiliser `Minikube` (Windows / MacOS / Linux), qui permet de déployer un noeud simple dans une instance locale. Minikube peut utiliser différents types de drivers (VirtualBox, KVM, Docker, …) et crée tout le cluster dans une VM (ou dans un conteneur). Les ressources sont donc plus limitées : <https://kubernetes.io/fr/docs/tasks/tools/install-minikube/>
- Utiliser `k3s` (Linux uniquement, par exemple dans une VM) qui permet de déployer une vraie instance légère de Kubernetes (mono-noeud par défaut) : <https://docs.k3s.io/quick-start>

:::tip
Un cluster k8s complet peut être un peu gourmand en ressources et suivant les installations, Minikube est très restrictif. Ajouter les options suivantes **à la création du cluster** :

```sh
minikube start --cpus 4 --memory 8192
```
:::

### Installer Kubectl

kubectl est l’interface en ligne de commande de configuration de Kubernetes. Installer kubectl sur la même machine que Minikube :

<https://kubernetes.io/docs/tasks/tools/>

:::tip
`kubectl` est la CLI de Kubernetes. Pour l'utiliser avec Minikube, on utilisera la notation suivante :

```sh
minikube kubectl -- …
```

Attention à bien ajouter les caractères `--` qui permettent de séparer la sous-commande `kubectl` de `minikube` des paramètres passés à `kubectl`. Par exemple : `minikube kubectl -- get po -A`.

Dans la suite du TP, on utilisera uniquement la notation `kubectl` : attention à bien taper `minikube kubectl --` puis la suite de la commande.
:::

### Dashboard de Kubernetes

Pour vérifier simplement le bon déroulement du TP, on peut déployer le dashboard Web de Kubernetes. En pratique, ce dashboard est rarement utilisé (on lui préfère les commandes `kubectl` beaucoup plus puissantes), mais celui-ci est assez utile pour tester k8s.

Minikube permet de déployer et lancer le dashboard très simplement :

```sh
minikube dashboard
```

### Exécution bac à sable en ligne

En cas de souci avec l'installation du cluster, il est possible de tester l'utilisation de Kubernetes depuis un environnement en ligne :

- <https://labs.play-with-k8s.com/>
- <https://killercoda.com/playgrounds/scenario/kubernetes>

## Prise en main d’un cluster Kubernetes

### Premier pod

Dans ces exemples, nous allons exécuter de la manière la plus simple possible des conteneurs en utilisant l’unité de base d’un cluster k8s : le `pod`.

Ensuite, nous exposerons un `service` k8s pour pouvoir accéder à nos conteneurs et nous verrons finalement comment configurer l’équilibrage de charge sur nos pods.

**Dans la suite du TP, nous utiliserons une image `nginx` pour simuler un serveur Web. Cette image peut être remplacée par l'image de test : `paulbouwer/hello-kubernetes:1.8` qui permet d'afficher le `Node` et le `Pod` en cours d'exécution pour du débug.**

:::exo
1. En utilisant la cheatsheet k8s, créer un fichier décrivant un Pod utilisant une image `nginx` pour créer un pod nommé `web`.
2. Récupérer l'adresse IP du pod créé.
3. Créer un 2e pod nommé `test` et utilisant une image `alpine`. On exécutera une commande `sleep 9999` pour faire tourner ce pod en continue.
4. Se connecter au pod `test` et exécuter un `ping` du pod `web`.
5. Détruire le conteneur de test
:::

:::correction
```yaml
# 1. Configuration du Pod web
#web-pod.yml
apiVersion: v1
kind: Pod
metadata:
  name: web
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
```
```sh
# Création du Pod web
kubectl apply -f web-pod.yaml

# 2. Récupération de l'adresse IP
kubectl get pod web -o wide
#NAME   READY   STATUS    RESTARTS   AGE   IP            NODE       NOMINATED NODE   READINESS GATES
#web    1/1     Running   0          20s   10.244.0.34   minikube   <none>           <none>

# ou :
kubectl describe po/web
#Name:             web
#…
#IP:               10.244.0.34
#IPs:
#IP:  10.244.0.34

# 3. Création du Pod de test
kubectl run test -it --image busybox -- sh
# 4. Ping du pod web
ping 10.244.0.34
# 5. Nettoyage du pod
kubectl delete test --force=true
```
:::

### Premier service

Un `Service` permet d'exposer les ports d'un pod. Nous allons voir comment exposer le plus simplement un Pod :

- Dans le cluster via un `ClusterIP` (via le nom du service), en utilisant une IP interne du cluster ;
- Vers l'extérieur via un `NodePort` pour configurer l'accès au port d'un conteneur en attribuant un port sur chaque nœud du cluster.

:::exo
1. En utilisant la ligne de commande `kubectl`, exposer un port du pod `nginx`
2. Modifier le pod `web` pour lui ajouter un label : `app=web-app`. Ce label permettre de lier le Pod aux Services.
3. Créer un service de type `ClusterIP` pour exposer `nginx` dans le cluster. Tester la connexion depuis un 2e Pod.
4. Créer un service de type `NodePort`. Tester l'accès à `nginx` depuis la machine hôte sur le port choisi.
:::

:::correction
```sh
# 1. Port Forward
kubectl port-forward web 8181:80
# Ou (plus propre)
kubectl expose web --type="NodePort" --port 8181
# Dans un navigateur ou wget/curl : localhost:8181 => Welcome to nginx!
```

```yaml
# 2. Ajout du label
#web-pod-label.yml 
# Configuration du Pod web
apiVersion: v1
kind: Pod
metadata:
  name: web
  labels:
    app: web-app  # Pour l'utiliser dans l'affinité
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
```

```sh
kubectl -f web-pod-label.yml apply
#pod/web configured

kubectl describe po/web
#Name:             web
#…
#Labels:           app=web-app
```
:::

:::correction
```yaml
# 3. ClusterIP
#web-cluster-ip.yml
apiVersion: v1
kind: Service
metadata:
  name: web-clusterip
  labels:
    app: web-app
spec:
  type: ClusterIP
  selector:
    app: web-app
  ports:
    - port: 8182        # Port interne exposé par le service
      targetPort: 80   # Port interne sur lequel le conteneur écoute
```

```sh
kubectl -f web-cluster-ip.yml apply   
#service/web-clusterip created

kubectl run test --rm -it --image alpine:latest
wget web-clusterip:8182
#Connecting to web-clusterip:8182 (10.103.248.90:8182)
#saving to 'index.html'
#index.html           100% |******************************************************************************|   615  0:00:00 ETA
#'index.html' saved
```
:::

:::correction
```yaml
# 4. NodePort
#web-node-port.yml
apiVersion: v1
kind: Service
metadata:
  name: web-clusterip
  labels:
    app: web-app
spec:
  type: NodePort
  selector:
    app: web-app
  ports:
    - protocol: TCP
      port: 82        # Port interne exposé par le service
      targetPort: 80   # Port sur lequel le conteneur écoute
      nodePort: 30001    # Port sur lequel le service sera accessible depuis l'extérieur du cluster
```

```sh
kubectl -f web-node-port.yml apply
#service/web-clusterip configured

minikube ip
#192.168.39.48

wget http://192.168.39.48:30001 # ou dans un navigateur
#Connecting to 192.168.39.48:30001 (192.168.39.48:30001)
#saving to 'index.html'
#index.html           100% |******************************************************************************|   615  0:00:00 ETA
#'index.html' saved
```
:::

### Affinité de Node

Pour créer un pod avec une affinité pour un nœud ayant un label spécifique, vous devez utiliser les affinités de nœud dans la définition du pod. Kubernetes vous permet de définir une affinité de type "soft" (préférence) ou "hard" (obligation) - voir la cheatsheet.

:::exo
1. Ajouter un nouveau label à l'un des `WorkerNode`.
1. Créer un pod avec une affinité pour ce `WorkerNode`.
1. Vérifier que le Pod a été démarré sur le bon Node.
:::

:::tip
Dans Minikube, il n'y a qu'1 seul `Node`, mais sur un vrai cluster on peut sélectionner le Node qui nous intéresse !
:::

:::correction
```sh
# 1. Ajout de label
kubectl get nodes              
#NAME       STATUS   ROLES           AGE   VERSION
#minikube   Ready    control-plane   11d   v1.31.0

kubectl label node minikube mon-app=web

kubectl get nodes --show-labels
#NAME       STATUS   ROLES           AGE   VERSION   LABELS
#minikube   Ready    control-plane   11d   v1.31.0   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=minikube,kubernetes.io/os=linux,minikube.k8s.io/commit=210b148df93a80eb872ecbeb7e35281b3c582c61,minikube.k8s.io/name=minikube,minikube.k8s.io/primary=true,minikube.k8s.io/updated_at=2024_10_12T00_40_48_0700,minikube.k8s.io/version=v1.34.0,mon-app=web,node-role.kubernetes.io/control-plane=,node.kubernetes.io/exclude-from-external-load-balancers=
```

```yaml
# 2. Configuration du Pod avec affinité
#web-pod-affinity.yml 
apiVersion: v1
kind: Pod
metadata:
  name: web-affinity-node
spec:
  containers:
    - name: nginx-affinity-node
      image: nginx:latest
      ports:
        - containerPort: 80
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: mon-app
                operator: In
                values:
                  - web
```

```sh
# Création du Pod avec affinité
kubectl -f web-pod-affinity.yml apply

# 3. Vérification : NODE==minikube
kubectl get po/web-affinity-node -o wide
#NAME                READY   STATUS    RESTARTS   AGE   IP            NODE       NOMINATED NODE   READINESS GATES
#web-affinity-node   1/1     Running   0          29s   10.244.0.38   minikube   <none>           <none>
```
:::

### Affinité de Pod

En Kubernetes, vous pouvez définir des affinités inter-pods pour lier deux pods ensemble, c'est-à-dire pour forcer la planification de deux pods sur les mêmes nœuds (ou pour les séparer selon des critères définis). Ces affinités sont gérées via des règles `podAffinity` (affinité) ou `podAntiAffinity` (anti-affinité).

:::exo
1. Ajouter un label `app=web-app` au Pod `web` et vérifier l'ajout.
2. Créer un Pod `cache` tournant un conteneur `redis` avec une affinité pour le Pod `web`. Vérifier l'affinité.
3. Créer un Pod `antagoniste` tournant un conteneur `alpine` avec une anti-affinité pour le Pod `web`. Vérifier la non-affinité.
:::

:::correction
```yaml
# 1. Ajout du label
#web-pod-label.yml 
# Configuration du Pod web
apiVersion: v1
kind: Pod
metadata:
  name: web
  labels:
    app: web-app  # Pour l'utiliser dans l'affinité
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
```

```sh
kubectl -f web-pod-label.yml apply
#pod/web configured

kubectl describe po/web
#Name:             web
#…
#Labels:           app=web-app
```
:::

:::correction
```yaml
# 2. Créer un Pod `cache` avec une affinité pour le Pod `web`.
#web-pod-cache-affinity.yml 
apiVersion: v1
kind: Pod
metadata:
  name: cache
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              app: web-app # label du pod `web`
          topologyKey: "kubernetes.io/hostname" # même noeud
  containers:
    - name: cache-container
      image: redis:latest
```

```sh
kubectl -f web-pod-cache-affinity.yml apply
pod/cache created

kubectl get po                             
#NAME                              READY   STATUS              RESTARTS      AGE
#cache                             0/1     ContainerCreating   0             5s
#web                               1/1     Running             0             48m
```
:::

:::correction
```yaml
# 3. Créer un Pod `antagoniste` avec une anti-affinité pour le Pod `web`.
#web-pod-antagoniste-affinity.yml 
apiVersion: v1
kind: Pod
metadata:
  name: antagoniste
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              app: web-app # label du pod `web`
          topologyKey: "kubernetes.io/hostname" # même noeud
  containers:
    - name: antagoniste-container
      image: alpine:latest
```

```sh
kubectl -f web-pod-antagoniste-affinity.yml apply
#pod/antagoniste created

kubectl get po                                   
#NAME                              READY   STATUS    RESTARTS      AGE
#antagoniste                       0/1     Pending   0             111s

kubectl describe po/antagoniste
#Events:
#  Type     Reason            Age   From               Message
#  ----     ------            ----  ----               -------
#  Warning  FailedScheduling  18s   default-scheduler  0/1 nodes are available: 1 node(s) didn't match pod anti-affinity rules. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod.

# Le pod n'a pas pu être lancé sur Minikube.
# C'est normal, on ne dispose que d'1 seul Node
# et on ne veut pas d'affinité avec Web !
```
:::

### Limiter les ressources d'un Pod

:::exo
1. Recréer le Pod `web` en ajoutant une limite des ressources (CPU et mémoire). Vérifier la limitation.
:::

:::correction
```yaml
#web-pod-limits.yml 
# Configuration du Pod web avec limitation de ressources
apiVersion: v1
kind: Pod
metadata:
  name: web
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      resources: # limitation de ressources
        limits:
          cpu: 500m # 0.5 unités CPU
          memory: 200Mi
```

```sh
# Création du Pod aux ressources limitées
kubectl -f web-pod-limits.yml apply
#pod/web created

kubectl describe po/web
#…
#    Limits:
#      cpu:     500m
#      memory:  200Mi
```
:::

## Création de ressources par Deployment

Les ressources de type `Pod` sont en réalité rarement utilisées - on leur préfère le `Deployment`, bien plus puissant. Celui-ci permet de déployer un grand nombre de ressources différentes (dont des Pods, en utilisant les syntaxes vues précédemment).

:::exo
1. Utiliser un `Deployment` pour recréer le Pod `web`. Inclure un service exposant le webserveur `nginx` dans le même fichier.
2. Détruire le Pod créé par le déploiement. Lister les Pods : que remarque-t-on ?
:::

:::correction
```yaml
#web-deployment.yml 
# Deployment pour Pod Web et Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deploy
spec:
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-container
        image: nginx:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: web-svc
  labels:
    app: web-app
spec:
  ports:
  - port: 80
  selector:
    app: web-app
```
:::

:::correction
```sh
# Utilisation d'un Deployment
kubectl -f web-deployment.yml apply        
#deployment.apps/web-deploy created
#service/web-svc created

kubectl get po                     
NAME                              READY   STATUS    RESTARTS      AGE
web-deploy-85c575ffc9-hmnz4       1/1     Running   0             3s

kubectl get po
#NAME                              READY   STATUS    RESTARTS      AGE
#web-deploy-85c575ffc9-hmnz4       1/1     Running   0             13s

kubectl get svc              
#NAME             TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
#web-svc          ClusterIP      10.99.83.92      <none>        80/TCP           20s

kubectl get deploy
#NAME             READY   UP-TO-DATE   AVAILABLE   AGE
#web-deploy       1/1     1            1           27s

kubectl delete po/web-deploy-85c575ffc9-hmnz4
kubectl get po
#NAME                              READY   STATUS    RESTARTS      AGE
#web-deploy-85c575ffc9-7sjtm       1/1     Running   0              4s

# Après destruction, un nouveau Pod a été créé automatiquement par le Déploiement
```
:::

### Mise à jour d'un Pod

La politique de déploiement par défaut dans Kubernetes pour les objets de type `Deployment` utilise la stratégie de mise à jour appelée `RollingUpdate`. Cette stratégie permet de mettre à jour les réplicas de manière progressive, un ou plusieurs pods à la fois, afin de minimiser les interruptions de service. Elle remplace progressivement les anciennes instances du pod par de nouvelles instances, sans nécessiter d'arrêt complet du service

Bien que `RollingUpdate` soit la stratégie par défaut, il existe une autre stratégie appelée `Recreate`, qui arrête tous les pods existants avant de créer les nouveaux. Cela peut être utile si votre application ne supporte pas l'exécution simultanée de plusieurs versions.

:::tip
La commande `kubectl rollout` est utilisée pour gérer et surveiller les déploiements progressifs (ou `rollouts`) de nouvelles versions d'une application. Elle vous permet de suivre et contrôler les mises à jour d’un `Deployment` ou d'un autre objet Kubernetes tel qu'un `DaemonSet` ou un `StatefulSet`. Cette commande est souvent utilisée pour vérifier l’état d’un déploiement, annuler une mise à jour défaillante ou observer l’évolution d’une nouvelle version.
:::

:::exo
1. Changer le Deployment (par exemple, la version de `nginx` utilisée), appliquer la modification et vérifier le résultat.
2. Effectuer un rollback du déploiement par la ligne de commande.
3. Effectuer un déploiement en utilisant la stratégie `Recreate` et analyser le changement de comportement.
:::

:::correction
```yaml
#1.
#…
        image: nginx:stable-perl
#…
```

```sh
kubectl -f web-deployment.yml apply
#deployment.apps/web-deploy configured
#service/web-svc unchanged

kubectl get po
#NAME                          READY   STATUS              RESTARTS   AGE
#web-deploy-6c5c648c79-5gr4v   0/1     ContainerCreating   0          10s
#web-deploy-85c575ffc9-mj4tc   1/1     Running             0          2m10s

kubectl get po
#NAME                          READY   STATUS    RESTARTS   AGE
#web-deploy-6c5c648c79-5gr4v   1/1     Running   0          20s

kubectl rollout status deploy/web-deploy
#Waiting for deployment spec update to be observed...
#Waiting for deployment spec update to be observed...
#Waiting for deployment "web-deploy" rollout to finish: 0 out of 1 new replicas have been updated...
#Waiting for deployment "web-deploy" rollout to finish: 0 out of 1 new replicas have been updated...
#Waiting for deployment "web-deploy" rollout to finish: 1 old replicas are pending termination...
#Waiting for deployment "web-deploy" rollout to finish: 1 old replicas are pending termination...
#deployment "web-deploy" successfully rolled out

# Un nouveau Pod est créé, puis le Pod précédent est supprimé.
```
:::

:::correction
```sh
#2. rollback
kubectl rollout history deploy/web-deploy
#deployment.apps/web-deploy 
#REVISION  CHANGE-CAUSE
#1         <none>
#2         <none>

kubectl rollout undo deploy/web-deploy --to-revision=1
#deployment.apps/web-deploy rolled back

kubectl describe po/web-deploy-85c575ffc9-g2mwj
#…
#  Normal  Pulling    17s   kubelet            Pulling image "nginx:latest"
```
:::

## Gestion du réseau

Nous avons déjà vu comment utiliser un `Service` de type `ClusterIP` ou `NodePort` pour accéder facilement à un `Pod` depuis l'intérieur ou l'extérieur du cluster. Il existe des configurations plus évoluées :

### Externel IP

En Kubernetes, le champ `externalIPs` dans la configuration d'un `Service` permet d'associer une ou plusieurs adresses IP externes à ce service. Ces adresses IP sont généralement utilisées pour rendre un service accessible depuis l'extérieur du cluster, mais sans avoir besoin d'utiliser un load balancer ou un service de type `NodePort`.

Lorsque vous définissez un ou plusieurs `externalIPs` pour un service, Kubernetes redirige automatiquement le trafic provenant de ces adresses IP externes vers le service interne.

Les `externalIPs` ne sont pas gérés par Kubernetes (ce ne sont pas des adresses IP dynamiques attribuées automatiquement comme dans un `LoadBalancer`). Il s'agit d'adresses IP statiques que vous devez configurer manuellement en dehors du cluster.

```yml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: ClusterIP
  selector:
    app: my-app
  ports:
    - port: 80           # Le port exposé par le service
      targetPort: 8080    # Le port sur lequel l'application dans le pod écoute
  externalIPs:
    - 192.168.1.100       # IP externe statique
    - 192.168.1.101       # Une autre IP externe statique
```

### LoadBalancer

Un `LoadBalancer` distribue le trafic entrant entre plusieurs pods, ce qui permet d'optimiser l'utilisation des ressources et de prévenir la surcharge d'un seul pod. Cela aide à assurer une réponse rapide même sous des charges élevées.

En cas de défaillance d'un pod, le `LoadBalancer` redirige automatiquement le trafic vers les autres pods sains. Cela augmente donc également la disponibilité de l'application, car le service reste accessible même si certains composants échouent.

Le type `LoadBalancer` est souvent utilisé dans des environnements cloud (comme AWS, GCP, Azure) qui prennent en charge la création automatique de load balancers, ce qui offre une intégration transparente avec d'autres services (comme la gestion de certificats SSL, les groupes de sécurité, etc.).

## Gestion de la persistance

### HostPath

En Kubernetes, un volume `hostPath` permet à un pod d'accéder directement à un répertoire sur le nœud (host) où le pod est exécuté. Cela signifie que le pod peut lire et écrire dans un répertoire du système de fichiers du nœud Kubernetes. Le volume `hostPath` est utilisé pour des cas spécifiques où vous devez partager des fichiers entre le conteneur et le nœud hôte.

Cependant, l'utilisation de `hostPath` peut présenter des risques de sécurité, car un pod a accès aux fichiers système du nœud. Il est donc recommandé de l'utiliser uniquement dans des cas spécifiques, comme pour des nœuds de confiance ou des environnements contrôlés (test, …).

:::exo
1. Utiliser un `hostPath` pour monter un fichier du noeud dans le pod. Le fichier doit exister.
2. Utiliser un `hostPath` pour monter un répertoire du noeud dans le pod. Créer le répertoire s'il n'existe pas.
:::

:::correction
```yaml
apiVersion: v1
kind: Pod
[…]
spec:
  containers:
  - name: front-end # nom du conteneur
    image: nginx # image Docker
    volumeMounts: # montage de volume
    - name: mon-volume # on monte une configuration de volume appelée 'mon-volume'
      mountPath: "/mon/montage/dans/le/conteneur" # point de montage à l'intérieur du conteneur
  volumes:
  - name: mon-volume # le nom de la configuration de volume à utiliser
    hostPath:
      path: /data/nginx # Chemin sur le nœud hôte
      type: File # pour 1. // DirectoryOrCreate pour 2.
```
:::

### PersistantVolume

Dans Kubernetes, un `PersistentVolume` (PV) est une ressource de stockage qui existe indépendamment des pods et qui peut être utilisée pour stocker des données de manière persistante. Un `PersistentVolumeClaim` (PVC) est une demande de stockage faite par un utilisateur ou une application pour utiliser un PV.

Dans cet exemple, nous allons utiliser un moyen de persister les données de nos conteneurs en utilisant des `PersistantVolumes`. Nous verrons également comment créer des `PersistantVolumesClaims` pour réclamer l’utilisation de ces volumes.

:::tip
Dans Kubernetes, les `accessModes` définissent comment un volume peut être monté et utilisé par un ou plusieurs pods. Il existe trois modes principaux d'accès à un PersistentVolume (PV) :

- `ReadWriteOnce` (RWO) : le volume peut être monté en lecture/écriture par un seul pod à la fois.
- `ReadOnlyMany` (ROX) : le volume peut être monté en lecture seule par plusieurs pods simultanément.
- `ReadWriteMany` (RWX) : le volume peut être monté en lecture/écriture par plusieurs pods simultanément.
  - Attention, ce mode n'est pas pris en charge par tous les types de stockage. Par exemple, les volumes de stockage locaux comme `hostPath` ne supportent pas le mode RWX.
- Il est possible de définir plusieurs modes d'accès autorisés pour un volume
:::

:::exo
1. Pour utiliser un stockage local sur minikube, créer un PV qui utilise un chemin du disque local de Node Minikube. On pourra utiliser la commande `minikube ssh` pour se connecter au Node. Vérifier la création du PV.
2. Créer un PVC afin de permettre de réclamer un PV en fonction des besoins d'une application. Vérifier la création du PVC.
3. Maintenant que le PVC est créé, vous pouvez l'utiliser dans un pod en le montant en tant que volume. Tester l'accès aux fichiers du dossier hôte dans le conteneur.
:::

:::correction
```yaml
# pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-exemple
spec:
  capacity:
    storage: 1Gi  # Capacité du volume
  accessModes:
    - ReadWriteOnce  # Seul un pod peut monter ce volume en lecture/écriture à la fois
  hostPath:
    path: "/mnt/data"  # Chemin sur le nœud minikube où les données seront stockées
---
# pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-exemple
spec:
  accessModes:
    - ReadWriteOnce  # Mode d'accès similaire à celui du PV
  resources:
    requests:
      storage: 500Mi  # La quantité de stockage demandée par ce PVC
---
# pod-using-pvc.yaml
apiVersion: v1
kind: Pod
metadata:
  name: pvc-pod
spec:
  containers:
  - name: pvc-container
    image: nginx
    volumeMounts:
    - mountPath: "/shared"
      name: storage-volume
  volumes:
  - name: storage-volume
    persistentVolumeClaim:
      claimName: pvc-exemple  # Le PVC créé précédemment
```
:::

## ConfigMap : gestion des configurations

### ConfigMap depuis un fichier de configuration

Soit le fichier de configuration pour mon infrastructure :

```ini
#ma_conf_test.conf
[dev]
server1=192.168.0.1
server2=192.168.0.2

[prod]
server1=10.166.10.1
server2=10.166.10.2
```

:::exo
1. Utiliser la ligne de commande pour créer une `ConfigMap` depuis ce fichier de configuration.
2. Ajouter cette ConfigMap dans un Pod et vérifier que la configuration est bien disponible.
:::

:::correction
```sh
kubectl create configmap ma-conf-test --from-file=./ma_conf_test.conf
#configmap/ma-conf-test created

kubectl get cm                                                       
#NAME               DATA   AGE
#kube-root-ca.crt   1      12d
#ma-conf-test       1      7s

kubectl describe cm/ma-conf-test
#Name:         ma-conf-test
#Namespace:    default
#Labels:       <none>
#Annotations:  <none>
#
#Data
#====
#ma_conf_test.conf:
#----
#[dev]
#server1=192.168.0.1
#server2=192.168.0.2
#
#[prod]
#server1=10.166.10.1
#server2=10.166.10.2
#…
```

```yaml
# Configuration du Pod avec Volume ConfigMap
apiVersion: v1
kind: Pod
metadata:
  name: config-map
spec:
  containers:
    - name: nginx-env
      image: nginx:latest
      volumeMounts:
      - name: mon-volume # voir ci-dessous
        mountPath: "/configs" # point de montage à l'intérieur du conteneur
  volumes:
  - name: mon-volume # idem conteneur
    configMap: # ConfigMap déjà créée
      name: ma-conf-test # où récupérer la configuration ?
```
:::

:::correction
```sh
kubectl -f pod-with-conf-volume.yml apply
#pod/config-map created

kubectl get po                           
#NAME                          READY   STATUS              RESTARTS      AGE
#config-map                    0/1     ContainerCreating   0             3s
#env                           1/1     Running             0             8m53s
#pvc-pod                       1/1     Running             0             22m
#web-deploy-85c575ffc9-dg7dm   1/1     Running             1 (11h ago)   11h
#web-deploy-85c575ffc9-kn5gh   1/1     Running             1 (11h ago)   11h

kubectl exec -it config-map -- bash
root@config-map:/# cat /configs/ma_conf_test.conf 
#[dev]
#server1=192.168.0.1
#server2=192.168.0.2
#
#[prod]
#server1=10.166.10.1
#server2=10.166.10.2
```
:::

### ConfigMap depuis un fichier env

:::exo
Injecter le fichier d'environnement suivant dans un conteneur. Vérifier que la variable d'environnement est bien injectée dans le conteneur.
:::

```dotenv
serveur1=1.2.3.4
serveur2=1.2.3.5
```

:::correction
```sh
kubectl create configmap ma-conf-env --from-env-file=./ma_conf.env      
#configmap/ma-conf-env created

kubectl describe cm/ma-conf-env                                   
#Name:         ma-conf-env
#Namespace:    default
#Labels:       <none>
#Annotations:  <none>
#
#Data
#====
#serveur2:
#----
#1.2.3.5
#
#serveur1:
#----
#1.2.3.4
#
#
#BinaryData
#====
#
#Events:  <none>
```

```yaml
# Configuration du Pod avec variable d'environnement
#pod-with-env.yml
apiVersion: v1
kind: Pod
metadata:
  name: env
spec:
  containers:
    - name: nginx-env
      image: nginx:latest
      env: # Variables d'environnement à injecter dans le conteneur
      - name: MON_SERVEUR # variable $MON_SERVEUR
        valueFrom:
          configMapKeyRef:
            name: ma-conf-env # où récupérer la valeur ?
            key: serveur1 # la valeur de $LOG_LEVEL à injecter
```

```sh
kubectl -f pod-with-env.yml apply
kubectl exec -it env -- bash
root@env:/# env | grep MON_SERVEUR
#MON_SERVEUR=1.2.3.4
```
:::

## Réplicas et scaling

Un réplica fait référence à une instance d'un pod qui exécute une application. Kubernetes utilise les réplicas pour assurer la haute disponibilité et la tolérance aux pannes. Plus le nombre de réplicas est élevé, plus il y a d'instances d'une application fonctionnant en parallèle. Ceci permet de gérer une charge plus élevée et d'améliorer la résilience en cas de panne d'un ou plusieurs pods.

Le scaling horizontal (ou mise à l’échelle) est l'action d'augmenter ou de réduire le nombre de réplicas d'un pod en fonction de la charge de travail ou des besoins. On utilise alors un `LoadBalancer` pour accéder de manière unifiée à l'ensemble des Pods.

À l'inverse, le scaling vertical (ou mise à l'échelle verticale) se réfère à l'augmentation des ressources d'un seul pod ou d'un seul nœud dans un cluster Kubernetes. Contrairement au scaling horizontal, qui consiste à ajouter plus de pods pour répartir la charge, le scaling vertical implique d'augmenter la capacité d'un pod existant en lui attribuant plus de ressources (CPU, mémoire, etc.).

:::tip
On préfère généralement effectuer du scaling vertical sur des machines virtuelles, et du scaling horizontal sur des conteneurs (voir la philosophie _Pet vs Cattle_ du DevOps). Kubernetes est donc l'outil idéal pour faire du scaling **horizontal**.
:::

### Scaling horizontal manuel 

:::exo
1. Utiliser le commande `kubectl` pour effectuer un scaling du déploiement de `nginx`. Modifier si besoin le service du déploiement pour utiliser un LoadBalancer.
2. Modifier le fichier `/usr/share/nginx/html/index.html` dans chaque conteneur pour savoir quel Pod répond : `POD 1` dans le 1e Pod et `POD 2` dans le 2nd. Tester de nombreuses requêtes pour vérifier le load balancing.
:::

:::correction
```sh
kubectl scale deployment web-deploy --replicas=2
#deployment.apps/web-deploy scaled

kubectl get po
#NAME                          READY   STATUS    RESTARTS   AGE
#web-deploy-85c575ffc9-bzlxn   1/1     Running   0          35s
#web-deploy-85c575ffc9-kws8w   1/1     Running   0          5s

kubectl exec -it web-deploy-85c575ffc9-bzlxn -- bash
#root@web-deploy-85c575ffc9-bzlxn:/# echo 'POD 1' > /usr/share/nginx/html/index.html 

kubectl exec -it web-deploy-85c575ffc9-kws8w -- bash
#root@web-deploy-85c575ffc9-kws8w:/# echo 'POD 2' > /usr/share/nginx/html/index.html

minikube service list
#| default              | web-svc                            |           80 | http://192.168.39.48:30001 |

while true; do curl http://192.168.39.48:30001; done
#POD 2
#POD 2
#POD 2
#POD 1
#POD 1
#POD 2
#POD 2
#POD 2
#POD 2
#POD 2
#POD 2
#POD 2
```
:::

### ReplicaSet

:::exo
1. Utiliser un fichier `ReplicaSet` pour effectuer le scaling depuis un fichier de configuration.
:::

:::correction
Voir cours
:::

### Équilibrage de charge

Une des fonctionnalités les plus intéressantes de Kubernetes est sa capacité à gérer l'équilibrage de nos applications : équilibrage horizontal ou vertical des pods, et même scaling des nœuds du cluster !

Pour pouvoir effectuer un équilibrage automatique, il faut disposer d'un [Metrics Server](https://github.com/kubernetes-sigs/metrics-server) :

```sh
minikube addons enable metrics-server
```

:::exo
1. En utilisant la ligne de commande `kubectl`, configurer nginx pour un scaling de 2 à 10.
2. Vérifier que les requêtes n'arrivent pas toutes sur le même pod.
:::

:::correction
```sh
kubectl autoscale deployment monnginx --min=2 --max=10
```
:::

#### Scaling horizontal automatique 

Un Horizontal Pod Autoscaler (HPA) en Kubernetes permet de redimensionner dynamiquement le nombre de réplicas d'un déploiement en fonction de l'utilisation des ressources (CPU, mémoire, etc.) ou de métriques personnalisées. Voici un exemple simple de HPA basé sur l'utilisation du CPU.

:::exo
1. Créez d'abord un déploiement avec une application simple, avec des ressources allouées (`requests`) et limitées (`limits`). Ajouter un `LoadBalancer` sur le port `80` du conteneur.
2. Ajouter un `HorizontalPodAutoscaler` pour augmenter le nombre de pods à partir de 3% de CPU consommé.
3. Envoyer des requêtes sur le service. Vérifier que le status du HPA, vérifier que le nombre de pods suit le scaling et que le service assure bien la livraison des requêtes après le scaling.
:::

:::tip
On pourra utiliser l'image `registry.k8s.io/hpa-example` qui est faite pour créer un gros pic de charge CPU à chaque requête sur le port 80.
:::

:::correction
```yaml
#hpa-base.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hpa-test
spec:
  selector:
    matchLabels:
      app: hpa
  template:
    metadata:
      labels:
        app: hpa
    spec:
      containers:
      - name: hpa-exemple
        image: registry.k8s.io/hpa-example
        ports:
          - containerPort: 80
        resources:
          requests:
            cpu: "200m"
          limits:
            cpu: "500m"
---
apiVersion: v1
kind: Service
metadata:
  name: hpa-svc
  labels:
    app: hpa
spec:
  type: LoadBalancer
  ports:
  - port: 80
    nodePort: 30002    # Port sur lequel le service sera accessible depuis l'extérieur du cluster
  selector:
```
:::

:::correction
```yaml
#hpa-reel.yml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: hpatest-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: hpa-test
  minReplicas: 1
  maxReplicas: 3
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 3 # 3% CPU max
```

```sh
kubectl -f hpa-base.yml apply   
#deployment.apps/hpa-test created
#service/hpa-svc created

kubectl -f hpa-reel.yml apply
#horizontalpodautoscaler.autoscaling/haptest-hpa created

kubectl get po                   
#NAME                        READY   STATUS    RESTARTS   AGE
#hpa-test-5446fc6b74-4wklp   1/1     Running   0          3m7s

kubectl get hpa
#NAME          REFERENCE               TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
#haptest-hpa   Deployment/hpa-test     cpu: 0%/20%          1         3         1          66s

minikube service list
#|----------------------|----------------------------------------------------|--------------|----------------------------|
#|      NAMESPACE       |                        NAME                        | TARGET PORT  |            URL             |
#|----------------------|----------------------------------------------------|--------------|----------------------------|
#| default              | hpa-svc                                            |           80 | http://192.168.39.48:30002 |

kubectl get hpa
#NAME          REFERENCE             TARGETS        MINPODS   MAXPODS   REPLICAS   AGE
#hpatest-hpa   Deployment/hpa-test   cpu: 215%/3%   1         3         3          3m36s

kubectl get po 
#NAME                       READY   STATUS    RESTARTS   AGE
#hpa-test-6d5d4548f-m8jsp   1/1     Running   0          23s
#hpa-test-6d5d4548f-mltbc   1/1     Running   0          23s
#hpa-test-6d5d4548f-vz7qr   1/1     Running   0          4m3s
```
:::

## Namespace

:::exo
1. Utiliser le namespace du dashboard pour lister les ressources spécifiques au dashboard kubernetes.
2. Créer un nouveau namespace et déployer un Pod dans ce namespace.
:::

:::correction
```sh
# Namespace du dashboard

kubectl get namespace   

# NAME                   STATUS   AGE
# […]
# kubernetes-dashboard   Active   94m

kubectl get pods -n kubernetes-dashboard

# NAME                                        READY   STATUS    RESTARTS   AGE
# dashboard-metrics-scraper-c5db448b4-gkbll   1/1     Running   0          94m
# kubernetes-dashboard-695b96c756-7kddw       1/1     Running   0          94m
```
:::

:::correction
```sh
kubectl create namespace my-namespace
```

```yaml
# Création d'un Pod dans un namespace dédié
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: my-namespace
spec:
  containers:
    - name: my-container
      image: nginx:latest
      ports:
        - containerPort: 80
```
:::

## Configuration du cluser

:::exo
1. À l'aide de commandes `kubectl`, afficher le plus d'informations possible sur la configuration du cluster.
:::

:::correction
```sh
kubectl config get-contexts    

# CURRENT   NAME       CLUSTER    AUTHINFO   NAMESPACE
# *         minikube   minikube   minikube   default

kubectl get namespace   

# NAME                   STATUS   AGE
# default                Active   13h
# ingress-nginx          Active   86m
# kube-node-lease        Active   13h
# kube-public            Active   13h
# kube-system            Active   13h
# kubernetes-dashboard   Active   94m

kubectl get pods -n kube-system

# NAME                               READY   STATUS    RESTARTS      AGE
# coredns-6f6b679f8f-zk6m4           1/1     Running   0             13h
# etcd-minikube                      1/1     Running   0             13h
# kube-apiserver-minikube            1/1     Running   0             13h
# kube-controller-manager-minikube   1/1     Running   0             13h
# kube-proxy-6n9q9                   1/1     Running   0             13h
# kube-scheduler-minikube            1/1     Running   0             13h
# metrics-server-84c5f94fbc-bhfvm    1/1     Running   0             81m
# storage-provisioner                1/1     Running   1 (13h ago)   13h
```
:::

:::correction
```sh
kubectl config view

# apiVersion: v1
# clusters:
# - cluster:
#     certificate-authority: /home/tom/.minikube/ca.crt
#     extensions:
#     - extension:
#         last-update: Sat, 12 Oct 2024 00:40:49 CEST
#         provider: minikube.sigs.k8s.io
#         version: v1.34.0
#       name: cluster_info
#     server: https://192.168.39.48:8443
#   name: minikube
# contexts:
# - context:
#     cluster: minikube
#     extensions:
#     - extension:
#         last-update: Sat, 12 Oct 2024 00:40:49 CEST
#         provider: minikube.sigs.k8s.io
#         version: v1.34.0
#       name: context_info
#     namespace: default
#     user: minikube
#   name: minikube
# current-context: minikube
# kind: Config
# preferences: {}
# users:
# - name: minikube
#   user:
#     client-certificate: /home/tom/.minikube/profiles/minikube/client.crt
#     client-key: /home/tom/.minikube/profiles/minikube/client.key
```
:::


# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.

