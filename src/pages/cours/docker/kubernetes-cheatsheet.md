---
title: Cheatsheet Kubernetes®
---

# Cheatsheet Kubernetes

## Commandes

### Lister les types de ressources supportées

```sh
kubectl api-resources -o wide
kubectl explain [--recursive] RESOURCE_NAME # documentation
```

### Vérifier la présence d'un composant k8s

```sh
kubectl get apiservices | grep metrics-server
```

### dry-run : simule la commande sans modification du cluster

```sh
kubectl … --dry-run
```

### Sorties `yaml` ou `json` et sélecteur `jsonpath`

```sh
kubectl -o yaml …
kubectl -o json …
kubectl -o jsonpath='{.items[0].metadata.name}' …
```

### Créer un template de fichier de ressource en Yaml

```sh
kubectl create … -o yaml > mon_fichier.yml
```

### Gérer le contexte

```sh
kubectl config get-contexts

kubectl config use-context …
```

### Monitoring

```sh
kubectl top nodes
kubectl top pods
```

### Créer une ressource (pod, service, ...)

```sh
kubectl apply -f monFichier.yml
```

### Lister les ressources créés (pod, service, storage, ...)

```sh
kubectl get deployments,svc,pods,pv,pvc,nodes [--all-namespaces]
```

### Inspecter des ressources

```sh
kubectl describe deployment myapp1

kubectl describe po/mon-pod

kubectl describe svc myapp1-sv
```

### Lister les conteneurs d'un pod (i.e. namespace==default)

```sh
kubectl describe po/mon-pod -n default
```

### Port-Forward (pour débug uniquement)

```sh
kubectl port-forward MON_POD PORT_HOST:PORT_CONTAINER
```

### Exposer un Pod (créer un service)

```sh
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
```

### kubectl exec : exécuter une commande dans un pod déjà en activité

```sh
kubectl exec -it MON_POD -c MON_CONTENEUR MA_COMMANDE
```

### kubectl debug démarrer un nouveau conteneur dans un Pod pour du débug

```sh
kubectl debug mypod -it --image=busybox
kubectl debug mypod -it --image=paulbouwer/hello-kubernetes:1.8
```

Voir : <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_debug/#examples>

### kubectl attach : s'attacher à la sortie du PID=1 (commande de lancement du conteneur)

```sh
kubectl attach MON_POD
```

### Gestion des labels

```sh
kubectl label MA_RESSOURCE MON_LABEL=MA_VALEUR
kubectl label MA_RESSOURCE MON_LABEL- # supprime le label
```

### Namespace

```sh
kubectl create namespace MON_NAMESPACE
kubectl get namespaces
kubectl config set-context minikube --namespace=MON_NAMESPACE [--cluster=…]
```

### ConfigMap

```sh
# Créer un ConfigMap depuis un fichier de conf existant
kubectl create configmap ma-conf --from-file=mon_fichier.conf

# Créer un ConfigMap depuis un fichier d'environnement (clé=valeur) existant
kubectl create configmap ma-conf-env --from-env-file=mon_fichier.env
```

### (Auto)scaling

```sh
# Voir fichier de déploiement

# Scaling manuel
kubectl scale deployment php-apache --replicas=3

# Scaling automatique
kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10

kubectl get hpa
```

### Rollout

```sh
kubectl rollout status deployment my-app
kubectl rollout history deployment my-app [--revision=2]
kubectl rollout undo deployment my-app [--to-revision=2]
kubectl rollout pause/resume deployment my-app
kubectl rollout restart deployment my-app-deployment # recrée les pods
```

## Structure d'un fichier k8s

```yaml
apiVersion: v1 # Version de l'APIServer k8s
kind: … # Le type de ressource à gérer : Pod, Deployment, Service, …
metadata: # Métadatas de la ressource
  name: … # nom (interne) de la ressource à créer et/ou monitorer
  namespace: mon-namespace # Namespace spécial (optionnel - sinon default)
  labels: # ajout de labels (optionnel)
    ma-cle: ma-valeur 
  […]
spec: # Les spécifications de la ressource. Différent pour chaque type de ressource
  […]
```

## Pod

### Exemple minimal de fichier de description d'un Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp # nom du Pod
spec:
  containers:
  - name: front-end # nom du conteneur
    image: nginx # image Docker
    ports:
    - containerPort: 80 # port dans le conteneur
```

### Exemple avancé de fichier de description d'un Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: webapp # nom du Pod
  labels:
    app: web # optionnel - pour utiliser un service
  namespace: mon-namespace # optionnel - dans un namespace dédié
spec:
  containers:
  - name: main-container # nom du conteneur
    image: nginx # image Docker
    imagePullPolicy: Always # re-pull la dernière version d'image à la (re)création du Pod
    command: ["printenv"] # The command to start the container
    args: ["HOSTNAME", "KUBERNETES_PORT"] # args for the command
    restartPolicy: Always # restart toujours si stoppé
    restartPolicy: OnFailure # restart seulement si erreur
    restartPolicy: Never
    env: # Variables d'environnement à injecter dans le conteneur
    - name: MA_VAR # variable $MA_VAR
      value: 42 # MA_VAR=42
    - name: LOG_LEVEL # variable $LOG_LEVEL
      valueFrom: # récupération de la valeur de $LOG_LEVEL à injecter
        configMapKeyRef: #env de type ConfigMap (`ma-config-map-env` déjà créée avec `log_level=…`)
          name: ma-config-map-env # où récupérer la valeur ?
          key: log_level # la valeur de $LOG_LEVEL à injecter
    ports: # Ports à exposer
    - containerPort: 80 # port dans le conteneur
    resources:
      requests: # ressources minimum
        memory: 50Mi
        cpu: 0.2
      limits: # ressources maximum
        memory: 250Mi
        cpu: 0.5
    readinessProbe: # check du démarrage
      httpGet:
        path: /monitor/status
        port: 8080
        scheme: HTTPS
      initialDelaySeconds: 2
      periodSeconds: 1
    livenessProbe: # check pendant fonctionnement (healthcheck)
      httpGet:
        path: /monitor/status
        port: 8080
        scheme: HTTPS
      initialDelaySeconds: 20
      periodSeconds: 10
    securityContext:
      readOnlyRootFilesystem: true
    volumeMounts: # montage de volume
    - name: mon-volume # on monte une configuration de volume appelée 'mon-volume'
      mountPath: "/mon/montage/dans/le/conteneur" # point de montage à l'intérieur du conteneur
    - name: log-volume
      mountPath: "/log"
    - name: tmpfs-volume
      mountPath: "/tmp"
  - name: sidecar-container
    image: busybox
    command: ["sh", "-c", "tail -f /logs/app.log"]
    volumeMounts:
    - name: log-volume
      mountPath: "/log"
  initContainers:
  - name: wait-for-myservice
    image: busybox:1.28
    command: ['sh', '-c', "until nslookup myservice.$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace).svc.cluster.local; do echo waiting for myservice; sleep 2; done"]
  volumes:
  - name: mon-volume # le nom de la configuration de volume à utiliser
    configMap: #volume de type ConfigMap (`ma-config-map` déjà créée)
      name: ma-config-map # où récupérer la configuration ?
  - name: log-volume
    emptyDir: {}
  - name: tmpfs-volume
    emptyDir:
      medium: "Memory"
  affinity: # Affinité : Pod / Node
    nodeAffinity: # Affinité de Node
      # [1] affinité "hard" : requis sinon échec
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: environment
                operator: In
                values:
                  - production
      # ou [2] affinité "soft" : si possible sinon non respecté
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 1
          preference:
            matchExpressions:
              - key: environment
                operator: In
                values:
                  - production
    podAffinity: # Affinité de Pod (ou `podAntiAffinity`)
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchLabels:
              cle: valeur # label à matcher
          topologyKey: "kubernetes.io/hostname"
```

Pour un `podAffinity`, le champ `topologyKey` spécifie la "topologie" sur laquelle vous voulez appliquer l'affinité. Ici, `kubernetes.io/hostname` signifie que les pods doivent être planifiés sur le même nœud (identifié par le nom d'hôte). Autres exemples : `topology.kubernetes.io/zone` pour contraindre les pods à être répartis sur plusieurs zones de disponibilité (si le cluster est multi-zone, comme dans les environnements cloud) ou `topology.kubernetes.io/region` pour répartir les pods dans différentes régions géographiques (pour les clusters multi-régions).

### Priorité, réquisition et limitation de ressources

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: test
    image: alpine
    priority: 0 # schédulé en dernier
    resources:
      requests: # ressources minimum
        memory: 50Mi
        cpu: 0.2
      limits: # ressources maximum
        memory: 250Mi
        cpu: 0.5
```

Pour récupérer la classe de QoS :

```sh
kubectl get pod <POD_NAME> -o jsonpath='{ .status.qosClass}{"\n"}'
```

#### Qualité de Service (QoS)

Les définition de `resources requests` et `resources limits` permettent de gérer de la QoS dans Kubernetes.

Il existe 3 classes de QoS :

- `Guaranteed` : tous les conteneurs du Pod doivent définir des `resource` `requests` (`memory`, `cpu`) et les mêmes valeurs en `limits`.
  - Ressources garanties en permanence pour le pod.
  - Prioritaires pour l'accès aux ressources et derniers à être évincés en cas de pression sur les ressources.
- sinon : `Burstable` : au moins 1 conteneur du Pod a une `resource request` ou `limit`
  - Garantie minimale de ressources définie par leurs demandes.
  - Peuvent utiliser plus de ressources que leur demande si elles sont disponibles sur le nœud.
  - Évincés après les pods `BestEffort` mais avant les pods `Guaranteed`.
- sinon : `BestEffort`: priorité la plus basse, ressources allouées en fonction de leur disponibilité.
  - Aucune garantie de ressources.
  - Premiers à être évincés.

##### Exemple de QoS Guaranteed

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: test
    image: alpine
    resources:
      requests: # ressources minimum
        memory: 250Mi
        cpu: 0.5
      limits: # ressources maximum
        memory: 250Mi
        cpu: 0.5
```

##### Exemple de QoS Burstable

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: test
    image: alpine
    resources:
      requests: # ressources minimum
        memory: 50Mi
      limits: # ressources maximum
        memory: 250Mi
```

##### Exemple de QoS BestEffort

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: test
    image: alpine
```

### Priorité, Tolerations et Terminaison d'un Pod

```yaml
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: test
    image: alpine
    terminationGracePeriodSeconds: 60 # shutdown timeout before kill
    # Logs écrits à la destruction d'un Pod
    terminationMessagePath: /dev/termination-log # défaut
    terminationMessagePolicy: File # défaut
    terminationMessagePolicy: FallbackToLogsOnError # utilise les logs du Pod
    # Tolerations
    tolerations:
    - effect: NoExecute
      key: node.kubernetes.io/not-ready # Node : not ready
      key: node.kubernetes.io/unreachable # Node : unreachable
      operator: Exists
      tolerationSeconds: 300 # Le Pod peut rester 300s sur un Node "NotReady" ou "Unreachable"
```

Voir aussi :

- <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/>
- <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/>
- <https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/>
- <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/>
- <https://medium.com/@prateek.malhotra004/demystifying-taint-and-toleration-in-kubernetes-controlling-the-pod-placement-with-precision-d4549c411c67>

## Stockage k8s

### Exemple de montage d'un volume hostPath

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
      type: DirectoryOrCreate # Type de volume
```

Valeurs possible de `type` de `hostPath` : `DirectoryOrCreate`, `Directory`, `FileOrCreate`, `File`, `Socket`, `CharDevice`, `BlockDevice`

### Exemple de montage d'un PersistantVolume

```yaml
apiVersion: v1
kind: PersistentVolume
spec:
  capacity:
    storage: 1Gi  # Capacité du volume
  accessModes:
    - ReadWriteOnce  # Seul un pod peut monter ce volume en lecture/écriture à la fois
  hostPath:
    path: "/mnt/data"  # Chemin sur le Node où les données seront stockées
```

### Exemple de PersistanceVolumeClaim

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
spec:
  accessModes:
    - ReadWriteOnce  # Mode d'accès similaire à celui du PV
  resources:
    requests:
      storage: 500Mi  # La quantité de stockage demandée par ce PVC
```

## Network k8s

### Exemple de fichier de ClusterIP

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-clusterip-service
  labels:
    app: my-app
spec:
  type: ClusterIP
  selector:
    app: my-app
  ports:
    - port: 80          # Port interne exposé par le service
      targetPort: 8080   # Port interne sur lequel le conteneur écoute
```

Pour accéder au service : <http://my-clusterip-service> (même namespace) ou <http://my-clusterip-service.nom-du-namespace.svc.cluster.local>

### Exemple de fichier de NodePort

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
  labels:
    app: my-app
spec:
  type: NodePort
  selector:
    app: my-app
  ports:
    - port: 8080      # Port interne exposé par le service
      targetPort: 80  # Port sur lequel le conteneur écoute
      nodePort: 30007 # Port sur lequel le service sera accessible depuis l'extérieur du cluster (facultatif)
```

`nodePort` est facultatif : Kubernetes définiera un port aléatoire si cet attribut n'est pas renseigné. Assurez-vous que le port `NodePort` choisi est dans la plage autorisée par votre configuration Kubernetes (généralement entre 30000 et 32767).

### Exemple de fichier LoadBalancer

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
  labels:
    app: my-app
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
    - port: 8080      # Port interne exposé par le service
      targetPort: 80  # Port sur lequel le conteneur écoute
      nodePort: 30007 # Port sur lequel le service sera accessible depuis l'extérieur du cluster (facultatif)
```

### DNS spécifique

Par défaut, un Pod utilise le DNS de Kubernetes.

Pour une configuration plus poussée, voir : <https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/>

## Deployment

### Exemple de fichier de Déploiement et de Service

```yaml
# From: https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/application/php-apache.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-apache
spec:
  selector:
    matchLabels:
      run: php-apache
  template:
    metadata:
      labels:
        run: php-apache
    spec:
      containers:
      - name: php-apache # Requis
        image: registry.k8s.io/hpa-example # Requis
        ports:
        - containerPort: 80
        startupProbe: […] # sonde de démarrage
        livenessProbe: […] # sonde de healthcheck
        readinessProbe: […] # sonde d'état "Ready"
        resources: # limitation de ressources pour auto-scaling
          limits:
            cpu: 500m # 0.5 unités CPU
          requests:
            cpu: 200m # 0.2 unités CPU
---
apiVersion: v1
kind: Service
metadata:
  name: php-apache
  labels:
    run: php-apache
spec:
  ports:
  - port: 80
  selector:
    run: php-apache
```

### Exemple de stratégie

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3  # 3 réplicas du pod
  strategy:
    type: RollingUpdate  # Stratégie par défaut, sinon `Recreate`
    rollingUpdate:
      maxUnavailable: 25%  # Maximum 25% de pods indisponibles pendant la mise à jour
      maxSurge: 25%        # Maximum 25% de nouveaux pods créés en plus des réplicas prévus
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image: my-app-image
```

Kubernetes "met à jour" le Déploiement en cas de changement dans la configuration : version de l'image, … Il faut donc avoir des tags différents dans les images pour mettre à jour le(s) conteneur(s) (par exemple : `mon-image-docker:v1`, `mon-image-docker-v2`, … ).

### Exemple de fichier de ReplicaSet

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-replicaset
  labels:
    app: my-app
spec:
  replicas: 3  # Nombre de réplicas (pods) à maintenir
  selector: # Le ReplicaSet doit surveiller les pods avec le label app: my-app.
    matchLabels:
      app: my-app
  template: # Modèle pour créer les pods si nécessaire
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app-container
        image: nginx:latest 
        ports:
        - containerPort: 80
```

### Exemple de fichier HorizontalPodAutoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: php-apache
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: php-apache
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50 # 50% de CPU
```

## Exemple de fichier de Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: mon-namespace
```

## Exemple de RBAC (Role-Based Access Control)

### (Cluster)Role

Un `Role` (resp. `ClusterRole`) définit les permissions spécifiques qu'un utilisateur ou un système peut avoir. Un `Role` est limité à un seul namespace alors qu'un `ClusterRole` définit les permissions sur l'ensemble du cluster.

Les `verbs` possibles sont : `get`, `list`, `watch`, `create`, `update`, `delete`.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role # ou ClusterRole
metadata:
  name: example-role
  namespace: production # uniquement pour Role
rules:
  # Règle pour créer des pods dans le cluster
  - apiGroups: ["apps"]
    resources: ["pods"]
    verbs: ["create", "get", "list", "watch"]

  # Règle pour utiliser les services de réseau
  - apiGroups: [""]
    resources: ["services"]
    verbs: ["use"]

  # Règle pour créer des ConfigMaps et Secrets
  - apiGroups: [""]
    resources: ["configmaps", "secrets"]
    verbs: ["create"]
 
  # Règle pour utiliser les endpoints
  - apiGroups: [""]
    resources: ["endpoints"]
    verbs: ["get", "list", "watch"]
```

### (Cluster)RoleBinding

Le `RoleBinding` (resp. `ClusterRoleBinding`) lie un `Role` (resp. `ClusterRole`) à un sujet spécifique (utilisateur, groupe, objets) dans un namespace donné.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding # ou ClusterRoleBinding
metadata:
  name: example-rolebinding
subjects:
  - kind: User
    name: example-user
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role # ou ClusterRole
  name: example-role
  apiGroup: rbac.authorization.k8s.io
```

## Autres commandes

Pour plus d’information sur les différentes commandes de k8s, voir : <https://kubernetes.io/fr/docs/home/>

---

# Cheatsheet Helm

## Parcourir le hub et les répos

```sh
helm search hub prometheus
helm repo list
```

## Récupérer et déployer un chart tout fait

```sh
helm repo add …
helm install [--set …] <chart_name>
```

## Historique, rollback

```sh
helm show all <chart_name>
helm history …
helm upgrade <chart_name>
helm rollback <chart_name>
```

---

# Cheatsheet FluxCD

## Bootstrap d'un nouveau dépôt

<https://fluxcd.io/flux/installation/bootstrap/>

## Ajouter un dépôt Git existant

```sh
flux create source git flux-system \
  --url=https://github.com/MON_GITHUB_USER/MON_GITHUB_REPO \
  --branch=main \
  --interval=1m \
  --namespace=flux-system
```

## Déployer des manifestes Kubernetes à partir de ce dépôt

```sh
flux create kustomization flux-system \
  --target-namespace=default \
  --source=flux-system \
  --path="./clusters/my-cluster" \
  --prune=true \
  --interval=10m \
  --namespace=flux-system
```

## Lister les HelmRelease

```sh
flux get helmreleases --all-namespaces
```

## Suivre les kustomizations

```sh
flux get kustomizations --watch
```

## Suspendre / reprendre la MAJ depuis une kustomization

```sh
flux suspend/resume kustomization nom-de-la-kusto
```

## Appliquer une kustomization manuellement

### Tester les modifications (dry-run)

```sh
kubectl kustomize path/to/local/kustomization
```

### Appliquer la kustomization depuis un fichier local (test)

```sh
kubectl apply -k path/to/local/kustomization
```

---

# Cheatsheet Kyverno

Exemple simple de politique `Kyverno` qui refuse la création de pods s'ils n'ont pas de label `app` :

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-app-label
spec:
  validationFailureAction: enforce
  rules:
    - name: check-for-label
      match:
        resources:
          kinds:
            - Pod
      validate:
        message: "Le label 'app' est requis pour tous les pods."
        pattern:
          metadata:
            labels:
              app: "?*"
```


# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.

