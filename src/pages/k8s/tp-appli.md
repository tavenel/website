---
title: TP Kubernetes - Création de manifestes et déploiement d'une application containerisée avec kubectl
date: 2025 / 2026
---

Exemple de création de manifestes et déploiement Kubernetes avec `kubectl` étape par étape, basé sur une mini-application à **2 services + 1 SGBDR containerisé**.

## 🧭 Objectifs pédagogiques

- Comprendre et manipuler les principaux objets Kubernetes : **Pod, Deployment, Service, ConfigMap, Secret, Namespace, PVC, StatefulSet**
- Déployer une application multi-services à la main avec `kubectl`
- Écrire des manifestes YAML structurés et cohérents
- Comprendre la logique réseau entre Pods, Services et la couche ingress interne
- Gérer un SGBDR containerisé dans Kubernetes via un StatefulSet

## 📦 Mini-application à déployer

L'application se compose de **deux services applicatifs** + **une base de données relationnelle** :

1. **frontend** – une API Web simple
2. **backend** – un service métier qui parle au SGBDR
3. **db** – une base MariaDB containerisée

👉 Les images utilisées sont fournies dans le registre Docker Hub public :

- Frontend : `nginx:stable-alpine` : servira une page statique ou un build (React/Vue/…) placé dans `/usr/share/nginx/html`.
- Backend : `tiangolo/uwsgi-nginx-flask:python3.12` : app Flask "Hello World" : expose l'API sur port 80.
- SGBDR : `mariadb:11` ou `postgres:16`

## 📚 Préparation du cluster et de l'environnement

### Créer un namespace dédié

- Créer un fichier `namespace.yaml` (nom : `tp-kube-app`)
- Appliquer le manifeste.

### Définir le contexte kubectl

- Configurer `kubectl` pour travailler par défaut dans ce namespace.

## 💼 Déploiement du backend

### Créer un ConfigMap contenant

- Fichier : `backend-config.yaml`
- Nom d'hôte de la base : `db`
- Port de la base

### Créer un Deployment pour le backend

- Fichier : `backend-deploy.yaml`
- Image : `tiangolo/uwsgi-nginx-flask:python3.12`
- Variables d'environnement :
  - Récupérer infos ConfigMap + Secret via `envFrom`
- Probes :
  - `livenessProbe`: `/health` port 8080
  - `readinessProbe`: `/ready` port 8080
- Réplicas : **2**

### Créer un Service (ClusterIP)

- Fichier : `backend-service.yaml`
- Nom : `backend`

## 🖥️ Déploiement du frontend

### Créer le Deployment du frontend

- Fichier : `frontend-deploy.yaml`
- Image : `nginx:stable-alpine`
- Variables d'environnement :
  - URL du backend : `http://backend:8080`
- Réplicas : **2**

### Créer le Service (NodePort ou ClusterIP selon cluster)

- Fichier : `frontend-service.yaml`
- Si cluster local :
  - `NodePort` pour exposition
- Sinon :
  - `ClusterIP` + Ingress (bonus)

## ⚙️ Déploiement du SGBDR via StatefulSet + PVC

### Créer un Secret pour le mot de passe

- Fichier : `db-secret.yaml`
- Clé : `DB_PASSWORD`

### Version 1 : Déploiement simple (1 réplica)

#### Créer un PVC pour le stockage persistant

- Fichier : `db-pvc.yaml`
- Taille : **1Gi**

#### Créer un Deployment pour la base de données

- Fichier : `db-deployment.yaml`
- Image : `mariadb:11` (ou PostgreSQL selon le choix)
- Variables d'environnement :
  - `MYSQL_ROOT_PASSWORD` ou `POSTGRES_PASSWORD`
- _VolumeMount_ du PVC `db-pvc` dans `/var/lib/mysql`

### Version 2 : Cas réel - créer un StatefulSet pour la base de données

- Fichier : `db-statefulset.yaml`
- Image : `mariadb:11` (ou PostgreSQL selon le choix)
- Variables d'environnement :
  - `MYSQL_ROOT_PASSWORD` ou `POSTGRES_PASSWORD`
- _VolumeMount_ du PVC dans `/var/lib/mysql`

### Créer le Service associé (ClusterIP pour Deployment ou Headless pour StatefulSet)

- Fichier : `db-service.yaml` ou `db-headless-service.yaml`
- Nom : `db`

## 📡 Tests et validation

:::exo

1. Vérifier que tous les Pods sont `Running`
2. Vérifier que les endpoints des Services sont corrects
3. Tester la résolution DNS via un Pod temporaire :

   ```bash
   kubectl run tmp --rm -it --image=busybox -- nslookup backend
   ```

4. Tester l'application :

   - Accéder au frontend (NodePort)
   - Vérifier la communication backend → db

:::

## ⭐ Bonus

- Ajouter un Ingress HTTP
- Ajouter des ressources (limits/requests)
- Ajouter un HPA sur le backend
- Ajouter des labels et annotations

## Ressources Kubernetes (Yaml)

:::exo
**Ordre recommandé** :

1. `namespace.yaml`
2. `backend-config.yaml`
3. `backend-deploy.yaml` + `backend-service.yaml`
4. `frontend-deploy.yaml` + `frontend-service.yaml`
5. `db-secret.yaml`
6. `db-pvc.yaml`
7. `db-deployment.yaml` + `db-service.yaml`
8. `db-statefulset.yaml` + `db-headless-service.yaml`

:::

### `namespace.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: tp-kube-app
```

### `backend-config.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: backend-config
  namespace: tp-kube-app
data:
  DB_HOST: "db"
  DB_PORT: "3306"
  # Ajoutez d'autres variables si nécessaire
```

### `backend-deploy.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  namespace: tp-kube-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
        - name: backend
          image: tiangolo/uwsgi-nginx-flask:python3.12
          ports:
            - containerPort: 8080
              name: http
          envFrom:
            - configMapRef:
                name: backend-config
            - secretRef:
                name: db-secret
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 10
            timeoutSeconds: 2
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 2
```

### `backend-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend
  namespace: tp-kube-app
  labels:
    app: backend
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
    - name: http
      port: 8080
      targetPort: 8080
```

### `frontend-deploy.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  namespace: tp-kube-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
        - name: frontend
          image: nginx:stable-alpine
          ports:
            - containerPort: 80
              name: http
          env:
            - name: BACKEND_URL
              value: "http://backend:8080"
          livenessProbe:
            httpGet:
              path: /health
              port: 80
            initialDelaySeconds: 10
            periodSeconds: 10
            timeoutSeconds: 2
          readinessProbe:
            httpGet:
              path: /
              port: 80
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 2
```

### `frontend-service.yaml` (NodePort - utile en cluster local)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend
  namespace: tp-kube-app
  labels:
    app: frontend
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
      name: http
```

### `db-secret.yaml`

> **Remplacer** `change-me-please` par le mot de passe réel avant déploiement.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
  namespace: tp-kube-app
type: Opaque
stringData:
  DB_PASSWORD: "change-me-please"
```

### SGBDR Version 1 : _Deployment_ + _Volume_ (PVC pré-créé)

- Modèle simple :
  - PVC créé en amont
  - Le Deployment monte directement ce PVC.
  - Attention : **un PVC ReadWriteOnce ne supporte qu'un seul Pod par nœud** : `replicas: 1`.

#### `db-pvc.yaml`

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: db-pvc
  namespace: tp-kube-app
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

#### `db-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: db
  namespace: tp-kube-app
  labels:
    app: db
spec:
  replicas: 1   # Un PVC RWO = un seul Pod
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
        - name: mariadb
          image: mariadb:11
          ports:
            - containerPort: 3306
          env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: DB_PASSWORD
          volumeMounts:
            - name: db-storage
              mountPath: /var/lib/mysql
      volumes:
        - name: db-storage
          persistentVolumeClaim:
            claimName: db-pvc
```

#### `db-service.yaml` (service ClusterIP pour accès classique)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db
  namespace: tp-kube-app
  labels:
    app: db
spec:
  type: ClusterIP
  selector:
    app: db
  ports:
    - port: 3306
      targetPort: 3306
      name: mysql
```

### SGBDR Version 2 : _StatefulSet_ avec _volumeClaimTemplates_

- **La bonne pratique Kubernetes** :
  - Le _StatefulSet_ crée automatiquement un _PVC_ **par Pod**.
  - Le stockage est persistant et unique pour chaque instance.
  - Possibilité de scaler (ex : `replicas: 3`) → chaque Pod aura son propre PVC (`db-0`, `db-1`, …).

#### `db-statefulset.yaml`

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: db
  namespace: tp-kube-app
spec:
  serviceName: db-headless   # obligatoire pour StatefulSet
  replicas: 1
  selector:
    matchLabels:
      app: db
  template:
    metadata:
      labels:
        app: db
    spec:
      containers:
        - name: mariadb
          image: mariadb:11
          ports:
            - containerPort: 3306
              name: mysql
          env:
            - name: MYSQL_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: DB_PASSWORD
          volumeMounts:
            - name: db-data
              mountPath: /var/lib/mysql
  volumeClaimTemplates:
    - metadata:
        name: db-data
      spec:
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Gi
```

#### `db-headless-service.yaml` (service headless requis pour StatefulSet)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db-headless
  namespace: tp-kube-app
  labels:
    app: db
spec:
  clusterIP: None
  selector:
    app: db
  ports:
    - port: 3306
      name: mysql
```

## Vérifications utiles

```bash
kubectl -n tp-kube-app get all
kubectl -n tp-kube-app describe pod <pod-name>
kubectl -n tp-kube-app logs <backend-pod> -c backend
kubectl -n tp-kube-app exec -it $(kubectl -n tp-kube-app get pod -l app=backend -o jsonpath='{.items[0].metadata.name}') -- sh
# test DNS
kubectl -n tp-kube-app run -it --rm --restart=Never busybox --image=busybox -- nslookup backend
```
