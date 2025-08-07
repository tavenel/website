---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Configuration avancée des Pods
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

## 🛠️ Sondes Healthcheck
- `ReadinessProbe`
  - 🔄 Remplacement du Pod si défectueux
  - 🌐 Exemple : dépendance service externe
  - ⏳ Laisser de la marge : ne pas tuer en boucle un conteneur qui démarre !
- `LivenessProbe`
  - 📊 Monitoring du Pod
  - ☠️ Kill du conteneur si échec
	- 🔄 Et donc (souvent) redémarrage automatique du Pod
  - 🚫 Jamais de dépendance vers l'extérieur du Pod
- `StartupProbe`
  - ❌ Doit renvoyer un échec tant que l'application n'est pas initialisée
- 🔢 3 modes : `exec` (commande), `httpGet`, `tcpSocket`
- ⏱️ Si vérification > 1 seconde, préférer précalculer (asynchrone) et retourner un cache

:::link
Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/probes/>
:::

---

### ⚠️ Healthcheck exec : processus orphelins
- 🐧 En Linux, quand un processus se termine :
  - Son parent gère son _exit status_ (`wait()`/`waitpid()`) => état _zombie_
  - Si le processus a été tué, ses enfants sont rattachés au `PID=1` (responsable de tuer les zombies)
  - ✅ OK sur système "standard" (`/sbin/init`, …) mais ici `PID=1` est le processus principal du conteneur
- 🧟 Besoin d'un tueur de zombies en cas d'`exec`
  - <https://github.com/krallin/tini> : utiliser un mini `init`
  - 🔄 Ou [partager le namespace PID entre tous les conteneurs du Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) : `gcr.io/pause` tuera les zombies

---

## 📏 Limiter les ressources d'un Pod

- 💻 Ressources :
  - `ResourceRequirements` : limite le CPU et/ou la mémoire
    - Dans les fichiers `Deployment`, `StatefulSet`, `DaemonSet`
    - Block `resource:`
  - `LimitRange` : limites par défaut du cluster
- 📊 2 types de limites :
  - `requests` : minimum requis par conteneur
    - Pour la répartition sur les Node (`Scheduler`)
  - `limits` : maximum par `Pod`
    - Pour la santé des Pod (`Kubelet`)
- ⚙️ Requirement: installer un `MetricsServer` dans le cluster
- 📚 Utilise les fonctionnalités de Docker : voir le [cours Docker sur le site](https://www.avenel.pro/docker)

---

:::warn
### Attention aux limits

- Les **requests** CPU/mémoire sont indispensables pour garantir un minimum de ressources et éviter l'éviction.
- Les **limits** sont plus polémiques et plusieurs écoles s'affrontent.
  - **CPU : souvent pas de limits** :
		- Limiter le CPU peut causer du **throttling** inutile, surtout pour les apps multithread.
		- Pourtant, dans certains cas (ex : apps sensibles à la latence ou I/O-bound), un contrôle via limit permet d'isoler les workloads et garantir des performances prévisibles.
  - **Mémoire : limites généralement conseillées**
    - La mémoire est **non compressible** : dépasser un `limit` implique un *OOM kill*, ce qui peut protéger le _Node_ entier.
    - Fixer `memory limit == request` permet d'éviter la surconsommation par certains pods, et d'alerter quand il faut ajuster les allocations via monitoring + OOM kills
💸 Sources : [1](https://medium.com/@carlosalbertoalvesscorreia/would-the-kubernetes-cpu-limit-be-an-anti-pattern-2b07d92d7bd8) [2](https://www.perfectscale.io/blog/kubernetes-cpu-limits) [3](https://home.robusta.dev/blog/stop-using-cpu-limits) [4](https://medium.com/directeam/kubernetes-resources-under-the-hood-part-3-6ee7d6015965) [5](https://stormforge.io/blog/flexibility-matters-when-setting-kubernetes-resource-limits/?utm_campaign=FY25_Q3_Learnk8s&utm_medium=newsletter&utm_source=Learnk8s)
:::

---

:::warn
### Workloads dynamiques

- Certains workloads (ex. _JVM_) ont des besoins variables : pic au démarrage, heap lié à memory limit, etc.
- Des limits statiques peuvent soit **empêcher le démarrage**, soit surprovisionner. Ex: pour le CPU, certaines versions de Java utilisent tous les cœurs du _Node_ à moins de définir `XX:ActiveProcessorCount`, ce qui peut provoquer du throttling.
- Privilégier donc une **limitation dynamique** en fonction du cycle de vie et des caractéristiques de l'application.
:::

---

## 📈 Scaling

- 🔄 Scaling horizontal : plusieurs instances de l'application
  - 🛠️ Commande `kubectl`
  - Ou automatiquement `HorizontalPodAutoscaler` (`HPA`) : natif k8s mais requiert un [Metrics Server](https://github.com/kubernetes-sigs/metrics-server)
- 📊 Scaling vertical : redimensionner les ressources de l'application (mémoire, CPU)
  - 🔄 Par mise à jour du déploiement et création d'un nouveau Pod
  - Ou automatiquement : `VerticalPodAutoscaler` [extension à installer](https://github.com/kubernetes/autoscaler/tree/9f87b78df0f1d6e142234bb32e8acbd71295585a/vertical-pod-autoscaler)

---

## 🔒 Sécurité

- 🛡️ Appliquer un `SecurityContext` :
  - Changer le `UID`, `GID`
	- Drop de _capabilities_
	- Filesystem _R/O_
	- …

---

## 🔄 Stratégies de déploiements

- 🛠️ k8s propose 2 stratégies de déploiements :
  - **Rolling update** :
    1. Création pod v2 en coexistance avec v1
    2. Intégration v2
    3. Suppression v1
  - **Recreate** (sans coexistance) :
    1. Suppression v1
    2. Création v2

---

- 🔄 Autres stratégies manuelles ou en ajoutant d'autres outils :
  - **Blue/Green** : coexistance des 2 versions (dont la nouvelle pour test)
  - **Canary deployment** : coexistance avec migration progressive des requêtes vers v2 : avec Ingress [Nginx](https://kubernetes.github.io/ingress-nginx/examples/canary/) ou [Traefik](https://2021-05-enix.container.training/2.yml.html#658)
- 🛠️ Utiliser un outil comme <https://github.com/weaveworks/flagger> pour des déploiements plus poussés

---

## 🎯 Assigner un Pod à un Node spécifique

- `NodeName` : assigner un `Pod` à un `Node` (test uniquement)
- `Node Selector` : sélectionner un `Node` par `Label`, ex : CI/CD, Node spécialisé stockage pour Pod BDD, …
- `Node Affinity` : contraintes sur les `Label` du `Node`, ex : répartition géographique, possédant un GPU, …
- `Pod Affinity` : regrouper des pods pour améliorer les perfs, par ex d'une même stack applicative, …
- `Anti-Affinity` : éloigner des pods pour augmenter la robustesse, par ex instances de H/A, …
- `Taints` et `Tolerations` : réserver des `Node` pour des workloads spécifiques : le `taint` empêche de déployer des `Pod` sur un `Node` en l'absence de `toleration`) : `NoSchedule` (_Control Plane_, …), `PreferNoSchedule`, `NoExecute` (expulsion)

---

# 🧩 Pods multi-conteneurs

---

## 🚗 Sidecars et autres patterns

- Conteneur(s) classique(s) supplémentaire(s) dans le Pod
- Points d'accès entrée et/ou sortie à la place du conteneur principal
- Utilise les volumes partagés ou la couche réseau pour travailler avec le conteneur principal
- Souvent injectés par des opérateurs k8s
- Voir la [documentation](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)

---

- `sidecar` : étends les fonctionnalités du conteneur principal : logs, monitoring, …
- `adapter` : adapte la donnée avant de la fournir au conteneur principal (ex: CSV to JSON)
- `ambassador` : authentification, (reverse)proxy, sécurité (HTTPS), …

---

## 🛠️ InitContainer

- Type de conteneur Kubernetes spécifique : `initContainers`
- Lancés dans l'ordre de spécification
- Le(s) conteneur(s) classiques démarrent après (si succès uniquement)
- Usage : chargement de données, migration BDD, génération de configs, attente dépendances, … (tous les prérequis du conteneur)

---

