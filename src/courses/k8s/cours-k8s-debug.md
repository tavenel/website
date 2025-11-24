---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: 🧪 Débug dans Kubernetes
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
- debug
---

## 🧭 Stratégie de Débug en Kubernetes 🔍🔧

- Approche du **bas vers le haut** :
  - Commencer **au niveau du pod**
  - Puis valider chaque niveau **jusqu'à l'utilisateur final**.
  - Permet de **remonter progressivement** vers la source du problème.

---

### 🧱 1. **Infrastructure applicative** : Pod → ReplicaSet → Deployment (ou autre)

#### Pod

```sh
kubectl logs pod
kubectl describe pod
kubectl exec -it pod -- /bin/sh
kubectl debug -it pod --image=paulbouwer/hello-kubernetes:1.8
```

:::link
Voir [la cheatsheet](/k8s/cheatsheet#debug)
:::

#### ReplicaSet

```sh
kubectl describe rs
kubectl get rs -o wide
```

#### Deployment / CronJob / StatefulSet

```sh
kubectl describe deployment my-app
kubectl get deploy/statefulset/cronjob
```

---

### 🌐 2. **Exposition réseau** : Pod → Service → Ingress

#### Pod

```sh
curl localhost:port
# Vérifier les ports exposés
```

#### Service

```sh
kubectl get svc
kubectl get endpoints
kubectl describe svc my-service
curl my-service:port # depuis un autre pod
```

#### Ingress

```sh
kubectl describe ingress
kubectl logs ingress-controller

# Tester le nom de domaine + vérification DNS
```

---

### 🧰 3. **Outils** utiles à tous les niveaux

```sh
kubectl get all
kubectl describe
kubectl logs
kubectl exec
kubectl get events --sort-by=.metadata.creationTimestamp`

# Depuis un Pod
nslookupcurl
ping
```

---

## 🧭 Déterminer la cause de l'échec d'un Pod 💥

---

1. 🔍 **Inspecter l'état du pod**

```sh
kubectl get pod my-pod
```

:::tip
Rechercher les états : `CrashLoopBackOff`, `Error`, `Pending`.
:::

---

2. 📜 **Examiner les événements du pod**

```sh
kubectl describe pod my-pod
# Vérifier les erreurs d'ordonnancement ou d'image.
```

---

3. 📦 **Consulter les logs**

```sh
kubectl logs my-pod

# Avec plusieurs conteneurs :
kubectl logs my-pod -c my-container
```

---

4. 🐚 **Redémarrer un pod en mode interactif**

```sh
# Ouvrir un terminal sur le Pod :
kubectl run -it --rm debug --image=busybox -- sh
```

---

5. ⚠️ **Vérifier les probes**
   - Readiness / Liveness mal configurées ?

---

6. 🧰 **Utiliser les outils CLI**
   - `kubectl exec`, `kubectl cp`, `kubectl port-forward` pour un diagnostic plus poussé.

---

:::link

- Voir la cheatsheet pour les commandes de diagnostic.
- Voir les liens de cours pour des exemples d'images de conteneurs utiles pour le debug.

:::

---

## 🐳 Pods en erreur : problèmes courants ⚠️

---

### 🐳 Erreur `ImagePullBackOff` 📦🚫

#### 🛑 Diagnostic

```sh
kubectl get pods
# STATUS: ImagePullBackOff
```

```sh
kubectl describe pod my-pod
# Vérifier l'erreur exacte dans les events
```

---

#### 🔍 Causes fréquentes

- ❌ **Nom d'image invalide**
- 🔖 **Tag inexistant ou mal orthographié**
- 🔐 **Problème d'accès à une registry privée**
  - Le pod n'a pas accès à la registry (DockerHub, GitHub Container Registry, etc.)
  - Solution : Créer un `Secret` de type `docker-registry` :

    ```sh
    kubectl create secret docker-registry regcred \
      --docker-server=DOCKER_SERVER \
      --docker-username=DOCKER_USER \
      --docker-password=DOCKER_PASS \
      --docker-email=EMAIL
    ```

  - L'utiliser dans le `spec` :

    ```yaml
    imagePullSecrets:
    - name: regcred
    ```

  - Tester le **pull manuel** :

    ```sh
    docker pull myregistry.com/myimage:tag
    ```

---

### 🔁 Erreur `CrashLoopBackOff` 🔄💥

#### 🛑 Diagnostic

```sh
kubectl get pods
# STATUS: CrashLoopBackOff
```

```sh
kubectl describe pod my-pod
kubectl logs my-pod --previous
```

- Utiliser `--previous` pour voir les logs **du dernier conteneur planté**

---

#### 🔍 Causes fréquentes

- 💥 L'application dans le conteneur **crashe au démarrage**
- 🔂 Kubernetes tente de la redémarrer… encore et encore
- ⏱️ Les probes `readiness` ou `liveness` échouent systématiquement
- 🐚 La commande `command` ou `args` du pod est incorrecte

---

#### ✅ Résolution

- Vérifier les variables d'environnement attendues
- Tester l'image manuellement en local :

  ```sh
  docker run -it myimage:tag /bin/sh
  ```

---

### 💣 Erreur `OOMKilled` (Out Of Memory) 🧠🔥

#### 🛑 Symptôme

```sh
kubectl get pod my-pod
kubectl describe pod my-pod
# State: Terminated, Reason: OOMKilled
```

---

#### 🔍 Causes

- 🚫 Le conteneur a dépassé la **limite de mémoire définie**
- Kubernetes l'a **tué automatiquement**

#### 💡 Exemple de spec mémoire

```yaml
resources:
  limits:
    memory: "128Mi"
  requests:
    memory: "64Mi"
```

---

#### ✅ Solutions

- 🔍 Augmenter la mémoire disponible si nécessaire
- 🧪 Optimiser la consommation mémoire de l'application
- 📊 Mettre en place du **monitoring mémoire** (Prometheus, cAdvisor, etc.)

---

### 🚫 Erreur `RunContainerError` 🐚🐳

#### 🛑 Diagnostic

```sh
kubectl get pods
# STATUS: RunContainerError
```

```sh
kubectl describe pod my-pod
# Événement : `Failed to start container`
```

- Le **conteneur** n'a pas pu être créé
  - Problème de configuration du conteneur
  - Inutile de regarde les logs…
    - …L'application n'a pas encore démarré !

---

#### 🔍 Causes fréquentes

- ❗ **Erreur dans la commande de démarrage**
  - Commande ou binaire inexistant dans l'image :

    ```yaml
    command: ["/start.sh"]  # mais start.sh n'existe pas ?
    ```

- 🐚 Shell absent ou mauvaise syntaxe :

  ```yaml
  command: ["bash", "-c", "my-command"]  # mais bash n'est pas dans l'image ?
  ```

- 🔧 Entrée `args:` mal formée ou mal utilisée avec `command:`
- 🔐 **Volumes montés incorrectement** ou fichiers attendus absents
- ⚙️ Permissions insuffisantes (exécuter un script non-exécutable)

---

#### ✅ Résolution

- 🔍 Tester localement avec Docker :

  ```sh
  docker run -it myimage /bin/sh
  ```

- 🔧 Vérifier le binaire ou script dans l'image :

  ```sh
  docker run myimage ls /start.sh
  ```

- ✅ Rendre les scripts exécutables (`chmod +x`)
- 🧪 Privilégier des images de debug (`alpine`, `busybox`, etc.) pour tester

---

### ⏳ Pod bloqué en état `Pending` 💤📦

#### 🛑 Diagnostic

```sh
kubectl get pods
# STATUS: Pending
```

```sh
kubectl describe pod my-pod
```

- Chercher la cause précise dans les **Events** :

  - `0/3 nodes are available: 3 Insufficient memory`
  - `no matching tolerations`
  - `failed to bind volumes`

---

#### 🔍 Causes fréquentes

- 🧠 **Pas assez de ressources disponibles** (CPU / RAM) sur les noeuds du cluster
- 🚫 **Tolerations / nodeSelector / affinity** trop restrictifs (aucun noeud éligible)
  - ⚠️ cause la plus probable !
- 📦 **PVC non lié** (volume non encore attaché ou indisponible)
- 🌩️ Problèmes avec le **CNI** (plugin réseau non fonctionnel)
- 🏷️ **Taints sans tolerations** : le pod ne peut pas s'installer sur un noeud

---

#### ✅ Solutions

- 📉 **Réduire les ressources demandées** :

  ```yaml
  resources:
    requests:
      memory: "1Gi"
      cpu: "1"
  ```

- 🔧 Adapter `nodeSelector`, `affinity`, ou `tolerations` :

  ```yaml
  nodeSelector:
    disktype: ssd
  ```

- 🧰 Vérifier les volumes :

  ```sh
  kubectl get pvc
  ```

- 🌐 Vérifier le plugin réseau (CNI) :

  ```sh
  kubectl get pods -n kube-system
  ```

---

### 🟢 Pod `Running` mais `NotReady` 🏃❌

#### 🛑 Diagnostic

```sh
kubectl get pods
# STATUS: Running
# READY: 0/1
```

```sh
kubectl describe pod my-pod
```

- Chercher dans les **Events** :
  - `Unhealthy` : `Readiness probe failed: connection refused`
  - `HTTP probe failed with statuscode: 500`

```sh
kubectl get endpoints my-service
```

- Vérifier si le DNS du service attendu par le pod est bien **résolu et joignable**

---

#### 🔍 Causes fréquentes

- 🧪 **Probes d'état (`readinessProbe`) qui échouent**
- ⏳ **Service dépendant non encore accessible** (ex: base de données)
- ⚠️ **Configuration manquante ou incorrecte** (ex : variables d'environnement non définies)
- 🔐 **Problèmes d'accès réseau ou DNS**
- 📦 Attente de **volume monté** ou de service externe

---

#### ✅ Bonnes pratiques

- ✔️ Testez les probes en local :

  ```yaml
  readinessProbe:
    httpGet:
      path: /health
      port: 8080
  ```

- 🧪 Lancez un shell dans le pod pour tester vous-même :

  ```sh
  kubectl exec -it my-pod -- curl http://localhost:8080/health
  ```

- 📊 Activez les logs d'application pour voir si un service manque ou crashe au démarrage
- 🐌 Désactivez temporairement la `readinessProbe` pour identifier si elle est responsable

---

## 🐙 Problèmes réseau

- 🚨 Cause fréquente de dysfonctionnement dans un cluster Kubernetes :
  - 🔌 Connexions entre Pods qui échouent.
  - 🚫 Services qui ne répondent pas.
  - ❓ Résolution DNS qui échoue.

---

### 🧪 Vérifier la connectivité entre Pods 🔍

- 🛠️ Utiliser des outils comme `curl`, `wget`, `telnet` ou `netcat` (`nc`).
- ✅ Exemple :

  ```sh
  kubectl exec -it pod-a -- curl http://pod-b:8080
  ```

- 🔎 Vérifier l'IP du pod cible :

  ```sh
  kubectl get pod pod-b -o wide
  ```

---

### 🧪 Vérifier la connectivité entre Pods et Services 🌉

- 📋 Assurez-vous que le Service cible existe :

  ```sh
  kubectl get svc
  ```

- 🌐 Tester l'accès via le nom DNS du service :

  ```sh
  kubectl exec -it pod-a -- curl http://my-service.namespace.svc.cluster.local
  ```

- 🧬 Vérifiez les endpoints associés :

  ```sh
  kubectl get endpoints my-service
  ```

---

### 🧪 Vérifier la résolution DNS 🔎📡

- 🧰 Tester le DNS avec `nslookup` ou `dig` :

  ```sh
  kubectl exec -it pod-a -- nslookup my-service
  ```

- 📡 Le DNS est géré par `CoreDNS`, vérifiez qu'il est actif :

  ```sh
  kubectl get pods -n kube-system -l k8s-app=kube-dns
  ```

---

### 🛠️ Débug avec un pod utilitaire 🧰

- 🚀 Déployer un pod utilitaire avec des outils réseau :

  ```sh
  kubectl run nettools --image=busybox:1.28 --rm -it --restart=Never -- sh
  ```

- 🔧 Utiliser `wget`, `nslookup`, `telnet`, … pour diagnostiquer.

---

### 🔐 Vérifier les NetworkPolicies 🚫📡

- 🛡️ Des politiques réseau peuvent bloquer la communication.
- 🔍 Vérifier s'il existe des `NetworkPolicy` :

  ```sh
  kubectl get networkpolicy
  ```

- 📑 Inspectez leur contenu :

  ```sh
  kubectl describe networkpolicy my-policy
  ```

---

### 🎯 Pas de routage réseau

- Service mal configuré
- 🌐 Vérifier les ports exposés : `port` / `targetPort` / `containerPort` 🎯

```yaml
apiVersion: v1
kind: Service
spec:
  ports:
    - port: 80         # Port du service
      targetPort: 8080 # Port du conteneur
```

```yaml
containerPort: 8080  # ✅ Doit correspondre au targetPort du Service
```

- 🧪 Vérification :

```sh
kubectl describe svc my-service
kubectl describe pod my-pod
```

---

### 🎯 Le Service ou le Deployment ne cible aucun Pod

- ⚙️ Vérifier les correspondances `label` / `selector` 🔗

#### 🔍 Exemple pour un Service

  ```yaml
  selector:
    app: web
  ```

- ✅ Vérifier que les Pods ont les bons labels :

  ```sh
  kubectl get pods --show-labels
  ```

#### 🧪 Exemple pour un Deployment

```yaml
selector:
  matchLabels:
    app: myapp
template:
  metadata:
    labels:
      app: myapp  # 🔥 doit correspondre exactement
```

---

### 🛣️ Déboguer un Ingress Controller 🌐🧪

#### 🛑 Symptôme

- L'application est inaccessible via l'URL publique (erreur 404, 502, connexion refusée).
- Le nom de domaine pointe bien vers l'IP du cluster, mais la route ne fonctionne pas.

---

#### 🧪 Étapes de diagnostic

✅ **1. Vérifier que l'Ingress Controller est bien installé :**

```sh
kubectl get pods -n traefik
```

- Exemple de pod : `traefik-ingress-controller-7d6f4c5d6-abcde`
- Vérifier qu'il est **Running** et **Ready**

✅ **2. Vérifier l'Ingress lui-même :**

```sh
kubectl get ingress
kubectl describe ingress my-ingress
```

- Voir les règles (`rules:`), chemins (`paths:`), et services cibles.
- ⚠️ Chercher les erreurs dans les events (ex : "no endpoints").
- Vérifier la cohérence de : `service.name` et `service.port.number` :

```yaml
rules:
- http:
    paths:
    - path: /api
      pathType: Prefix
      backend:
        service:
          name: my-service  # ✅ nom du Service
          port:
            number: 80      # ✅ port exposé par le Service
```

✅ **3. Vérifier le Service backend :**

- Le service mentionné dans l'Ingress doit exister et être exposé sur le bon port.
- Vérifier la cohérence de : `service.name` et `service.port.number` :

```sh
kubectl get svc
kubectl get endpoints my-service
```

✅ **4. Vérifier la résolution DNS interne :**

```sh
kubectl exec -it some-pod -- nslookup my-service
```

✅ **5. Tester l'accès depuis un pod dans le cluster :**

```sh
kubectl exec -it some-pod -- curl http://my-service:port
```

---

#### 🔐 Autres points à contrôler

- 📦 **Annotations** spécifiques au type d'Ingress Controller (non génériques), ex :

  ```yaml
  kubernetes.io/ingress.class: nginx
  nginx.ingress.kubernetes.io/rewrite-target: /
  ```

- 🔧 **TLS actif ?** Si oui, vérifier le certificat :

  ```sh
  kubectl get secret tls-secret
  ```

- 🪵 **Logs du contrôleur :**
  - Erreurs de routing ou d'accès backend (`upstream unavailable`, `host not found`, etc.)

```sh
kubectl logs -n traefik deploy/traefik-ingress-controller
```

---
