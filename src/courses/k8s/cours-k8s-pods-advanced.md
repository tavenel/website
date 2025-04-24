---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Configuration avancée des Pods
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

## Sondes Healthcheck

- `ReadinessProbe`
  - remplacement du Pod si défectueux
  - exemple : dépendance service externe
  - laisser de la marge : ne pas tuer en boucle un conteneur qui démarre !
- `LivenessProbe`
  - monitoring du Pod
  - kill du conteneur si échec
	- et donc (souvent) redémarrage automatique du Pod
  - jamais de dépendance vers l'extérieur du Pod
- `StartupProbe`
  - doit renvoyer un échec tant que l'application n'est pas initialisée
- 3 modes : `exec` (commande), `httpGet`, `tcpSocket`
- si vérification > 1 seconde, préférer précalculer (asynchrone) et retourner un cache

Voir aussi : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/probes/>

---

### ⚠️ Healthcheck exec : processus orphelins 

- En Linux, quand un processus se termine : 
  - son parent gère son _exit status_ (`wait()`/`waitpid()`) => état _zombie_
  - si le processus a été tué, ses enfants sont rattachés au `PID=1` (responsable de tuer les zombies)
  - OK sur système "standard" (`/sbin/init`, …) mais ici `PID=1` est le processus principal du conteneur
- Besoin d'un tueur de zombies en cas d'`exec`
  - <https://github.com/krallin/tini> : utiliser un mini `init`
  - Ou [partager le namespace PID entre tous les conteneurs du Pod](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) : `gcr.io/pause` tuera les zombies

---

## Limiter les ressources d'un Pod

- Ressources :
  - `ResourceRequirements` : limite le CPU et/ou la mémoire
    - dans les fichiers `Deployment`, `StatefulSet`, `DaemonSet`
    - block `resource:`
  - `LimitRange` : limites par défaut du cluster
- 2 types de limites :
  - `requests` : minimum requis par conteneur
    - pour la répartition sur les Node (`Scheduler`)
  - `limits` : maximum par `Pod`
    - pour la santé des Pod (`Kubelet`)
- Requirement: installer un `MetricsServer` dans le cluster
- Utilise les fonctionnalités de Docker : voir le [cours Docker sur le site](https://www.avenel.pro/cours/docker)

---

## Scaling

- Scaling horizontal : plusieurs instances de l'application
  - commande `kubectl`
  - ou automatiquement `HorizontalPodAutoscaler` (`HPA`) : natif k8s mais requiert un [Metrics Server](https://github.com/kubernetes-sigs/metrics-server)
- Scaling vertical : redimensionner les ressources de l'application (mémoire, CPU)
  - par mise à jour du déploiement et création d'un nouveau Pod
  - ou automatiquement : `VerticalPodAutoscaler` [extension à installer](https://github.com/kubernetes/autoscaler/tree/9f87b78df0f1d6e142234bb32e8acbd71295585a/vertical-pod-autoscaler)

---

## Sécurité

- Appliquer un `SecurityContext` : 
  - changer le `UID`, `GID`
	- drop de _capabilities_
	- filesystem _R/O_
	- …

---

## Stratégies de déploiements

- k8s propose 2 stratégies de déploiements :
  - **rolling update** :
    1. création pod v2 en coexistance avec v1
    2. intégration v2
    3. suppression v1
  - **recreate** (sans coexistance) :
    1. suppression v1
    2. création v2

---

- autres stratégies manuelles ou en ajoutant d'autres outils :
  - **blue/green** : coexistance des 2 versions (dont la nouvelle pour test)
  - **canary deployment** : coexistance avec migration progressive des requêtes vers v2 : avec Ingress [Nginx](https://kubernetes.github.io/ingress-nginx/examples/canary/) ou [Traefik](https://2021-05-enix.container.training/2.yml.html#658)
- Utiliser un outil comme <https://github.com/weaveworks/flagger> pour des déploiements plus poussés

---

## Assigner un Pod à un Node spécifique

- _NodeName_ : assigner un _Pod_ à un _Node_ (test uniquement)
- _Node Selector_ : sélectionner un _Node_ par _Label_, ex : CI/CD, Node spécialisé stockage pour Pod BDD, …
- _Node Affinity_ : contraintes sur les _Label_ du _Node_, ex : répartition géographique, possédant un GPU, …
- _Pod Affinity_ : regrouper des pods pour améliorer les perfs, par ex d'une même stack applicative, …
- _Anti-Affinity_ : éloigner des pods pour augmenter la robustesse, par ex instances de H/A, …
- _Taints_ et _Tolerations_ : réserver des _Node_ pour des workloads spécifiques : le _taint_ empêche de déployer des _Pod_ sur un _Node_ en l'absence de _toleration_) : `NoSchedule` (_Control Plane_, …), `PreferNoSchedule`, `NoExecute` (expulsion)

---

# Pods multi-conteneurs

---

## Sidecars et autres patterns

- Conteneur(s) classiques supplémentaire(s) dans le Pod
- Points d'accès entrée et/ou sortie à la place du conteneur principal
- Utilise les volumes partagés ou la couche réseau pour travailler avec le conteneur principal
- Souvent injectés par des opérateurs k8s
- Abstraction théorique : pas de modèle kubernetes [mais une implémentation est en beta](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)

---

- `sidecar` : étends les fonctionnalités du conteneur principal : logs, monitoring, …
- `adapter` : adapte la donnée avant de la fournir au conteneur principal (ex: CSV to JSON)
- `ambassador` : authentification, (reverse)proxy, sécurité (HTTPS), …

---

## initcontainer

- Type de conteneur Kubernetes spécifique : `initContainers`
- Lancés dans l'ordre de spécification
- Le(s) conteneur(s) classiques démarrent après (si succès uniquement)
- usage : chargement de données, migration BDD, génération de configs, attente dépendances, … (tous les pré-requis du conteneur)

---

