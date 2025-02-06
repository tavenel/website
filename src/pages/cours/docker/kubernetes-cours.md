---
title: Cours Kubernetes
theme: the-unnamed
# layout: cover
layout: '@layouts/SlideLayout.astro'
---

# Kubernetes

_Tom Avenel_

<https://www.avenel.pro/>

---
layout: section
---

# Présentation de Kubernetes

---

`Kubernetes` `k8s` est un orchestrateur de déploiement et de gestion de conteneurs applicatifs dans un cluster de machines virtuelles.

* Indépendant de Docker® mais même runtime `containerd` => peut tourner les mêmes images
* Configure et gère un cluster applicatif complexe : nœuds du cluster, réseau, stockage, ...

---

* De loin l'orchestrateur le plus utilisé avec Docker®
* D'autres orchestrateurs existent : `OpenShift`, `Swarm`, `Apache Mesos`, …

---

* Possibilité de gérer tout le cluster via API `kubectl`
* Mais configuration recommandée via `Yaml` / `Json` pour audit

---

# Recommandations

* `Docker®` seul / `docker compose` pour CI/CD et outils internes
* `k8s®` pour gestion applicative de l'environnement de production
* `k8s®` duplique des fonctionnalités de Docker® => préférer 100% Docker® ou k8s®

---

# Technologies de conteneurs supportées

1. `containerd` : projet open-source créé pour Kubernetes (runtime de `Docker` : _Docker sans la CLI_)
2. `Docker Engine` : _Docker avec la CLI_
3. `Podman` : alternative _serverless_ à Docker
4. `CRI-O` : conteneurs légers
5. `Mirantis Container Runtime (MCR)` (anciennement _Docker Enterprise_)

---
layout: section
---

# Distributions Kubernetes

---

1. Rancher :
   - Plateforme complète pour gérer des clusters Kubernetes
   - Propose des fonctionnalités avancées comme la gestion multi-cluster
   - Offre une interface graphique intuitive

---

2. K3s :
   - Version allégée de Kubernetes conçue pour les environnemets embarqués
   - Consomme moins de ressources que Kubernetes standard
   - Idéal pour les systèmes à faible puissance

---

3. OpenShift :
   - Distribution propriétaire de Red Hat basée sur Kubernetes
   - Inclut des fonctionnalités supplémentaires comme l'orchestration d'applications
   - Forte sécurité et conformité

---

4. Docker Kubernetes Service (DKS)
   - Surveillance intégrée du cluster et des applications.
   - Nombreux drivers storage

---

5. MicroK8s :
   - Distribution légère et sécurisée de Kubernetes
   - Conçue pour les environnemets Ubuntu
   - Propose des fonctionnalités avancées comme l'installation de paquets

---

6. Minikube : 
   - Version légère pour le développement et le test
   - Fonctionne sur un seul ordinateur
   - Idéal pour débutants et environnement de développement

---

7. Docker Desktop :
   - Intègre Kubernetes nativement
   - Offre une expérience utilisateur simplifiée
   - Adapté aux développeurs utilisant Docker

---

8. Kind (Kubernetes IN Docker) :
   - Déploie Kubernetes dans un conteneur pour le développement et le test
   - Crée rapidement un ou plusieurs clusters localement
   - Utile pour tester plusieurs clusters : upgrade, changements d'infrastructure, …

---

# Plateformes managées

- Amazon Elastic Kubernetes Service (EKS)
- Google Kubernetes Engine (GKE)
- Azure Kubernetes Services (AKS) 
- Oracle Kubernetes Engine (OKE)
- IBMCloud K8s
- OVHCloud K8s

---
layout: section
---

# Architecture

---

# Installation

- `kubeadm` : l'outil officiel (installation de chaque composant séparément)
- Intégré dans la distribution : `k3s`, `minikube`, `microk8s`, …
- Versions managées : outils dédiés au fournisseur de Cloud

---

# Modèle

* Un cluster k8s est composé de plusieurs `Node`
* Chaque `Node` fait tourner des `Pod` (ensemble de conteneurs - c'est l'unité atomique de k8s !)
* Un `Deployment` gère _déclarativement_ des ressources à déployer (pods, replicas, mise à jour, … )
* Un `Service` permet d'exposer les ports d'un pod (interne ou externe)
  - _Aucun lien avec un `service` de `docker-compose` !_

---

## Types de Nodes

* Node de rôle `master` : le `control pane`, gère le cluster (orchestration, API server, …)
* Node de type `worker` (sans rôle) : exécute les pods et leur fournit les ressources

---

# Limites

- k8s est fait pour gérer de gros clusters :
- limitations Kubernetes v1.31 :
  - < 5,000 Node
  - < 110 Pod / Node
  - < 150,000 Pod (total)
  - < 300,000 Containers (total)

---

![](https://kubernetes.io/images/docs/kubernetes-cluster-architecture.svg)

<!-- _class: legende -->
_Architecture d'un cluster Kubernetes (source: kubernetes.io)_

---

# Composants

* `APIServer` : API de gestion du cluster
* `etcd` : stockage de la configuration du cluster
* `Controller Manager` : gère les `WorkerNode` depuis le `MasterNode`
* `Kubelet` : exécute et gère les conteneurs sur les `WorkerNode`
* `Kube-proxy` : équilibre le trafic sur chaque `Node`
* `Scheduler` : assigne les `Pod` à un `Node`

---

# etcd

- Backend k8s : état du cluster
  - store clé=valeur
- Dans ou en dehors du cluster
- 1 leader (par consensus)
  - déployer un nombre impair d'instances
- Jamais utilisé directement (`APIServer`)
- Critique !

---

# ControllerManager

- Compare l'état désiré (déclaratif) à l'état actuel
- En déduit (et applique) les actions nécessaires (`APIServer`)
- Beaucoup de contrôleurs différents
  - possibilité d'installer des contrôleurs externes pour gérer de nouvelles ressources (`Custom Resource Definition`)
  - ex: Load Balancer AWS, …
- Boucles de réconciliation :
  - reconstruit des ressources si besoin pendant le cycle de vie du cluster
  - sans besoin d'intervention

---

# Scheduler

- Assigne les `Pod` aux `Node`
    - Change le `nodeName` du `Pod`
- Calcule de score par _filtrage_ puis _score_ :
    1. _filtrage_ : capacité, tolérance, affinité, sélecteurs, …
    2. _score_ : load-balancing, …
- Possibilité d'installer un `Scheduler` customisé

---

# Kubelet

- 1 `Kubelet` par `Node`
- Connexion permanente à l'`APIServer`
- Déploie le `Pod` s'il a le `nodeName` du `Node` courant :
    1. Récupération de l'image (format `OCI`)
    2. Création des ressources : `Volumes`, `Networks`, `Containers`
    3. États du `Pod` : `pending` -> `running` / `failed` -> `succeeded` (terminé)
    4. Remonte l'information à l'`APIServer`

---

# Gestion du cluster

* Fichiers de configuration `yml` (à privilégier autant que possible !)
* Interface en ligne de commande `kubectl` (surtout pour lancer les fichiers de config)
* Interface web (peu utilisée)

---
layout: section
---

# Ressources du cluster

---

## Labels

- attributs clé=valeur des objets du cluster
- utilisé par kubernetes
- `NodeSelector` : lance un pod sur un `Node` ayant ce label
- `NodeAffinity` : décrit des affinités entre un `Pod` et un `Node`
- `podAffinity`, `podAntiAffinity` : (anti)affinité entre `Pod`
- il existe aussi des `annotations` : idem mais NON utilisé par k8s ensuite

---

## Gestion des applications

- `Deployment` : gère le déploiement d'un `ReplicaSet`
  - et la mise à jour des applications (rolling update, rollback, scaling)
- `ReplicaSet` : crée et gère le suivi (réplicas) d'un pod
  - ne pas utiliser de `ReplicaSet` directement mais passer par un `Deployment` (plus puissant)
- `Pod` : gère un ensemble de conteneurs partageant la même isolation : stack réseau, stockage, …
  - démarré directement ou (mieux) par un `deployment` créant un `ReplicaSet`
  - éphémère : pas de données critiques dans le pod
  - 1 IP par pod partagée entre tous les conteneurs (mais l'IP peut changer)
    - accès par `localhost` aux autres conteneurs et **partage des ports ouverts**

---

## Service

- Service DNS permettant d'accéder à 1 (ou plusieurs) Pods
  - Nom DNS court (dans le namespace) : `<service_name>.<namespace>` (ou `<service_name>` si `namespace==default`)
  - Nom DNS complet : `<service_name>.<namespace>.svc.<cluster-domain>`
  - exemple : `mon_service.mon_namespace.svc.mon_cluster`
- Association `Service` <-> `Pod`(s) grâce aux _labels_
- Au moins 2 CIDR (plages réseau) : CIDR Pod et CIDR Services

---

### Service: ClusterIP

- Expose à l'intérieur du cluster uniquement
- Accès via le nom du service

---

### Service: NodePort

- Expose à l'extérieur du cluster
- Accès via des ports sur les Nodes du cluster

---

### Service: LoadBalancer

- LoadBalancer pour l'accès au Pod depuis l'extérieur
- Permet d'avoir un accès unique à plusieurs conteneurs d'un Pod tournant sur plusieurs Nodes.

---

## Ingress

- Point d'accès publique unique pour l'accès aux différentes Pods (différent d'un Service)
- Recquiert un reverse-proxy et/ou un load balancer : `Nginx`, `Haproxy`, `Traefik`, `Consul`, `Istio`.
- Add-on réseau à installer (pas de gestion réseau native par k8s)

---

## Service Mesh

- Ajoute les services d'infrastructure communs
  - authentification
  - sécurité
  - logs
- Gère la communication sécurisée entre conteneurs sur des architectures micro-services
- À installer : `Istio`, `linkerd`, `consul`, …

---

## Configuration des applications

* `ConfigMap` pour modifier la configuration des applications
  - décorélé du code de l'application
* `Secret` (mots de passe)

---

## Stockage

- `Volume` : points de montages dans les conteneurs du pod
  - dans `Pod` => non persistant
  - extérieur au Pod => persistant
- `PersistentVolume` (`PV`) : stockage extérieur au pod (donc au conteneur)
  - provisionné à l'extérieur du pod (statique ou dynamique)
  - durée de vie indépendante du pod
- `Volume claim` : création d'un `PV`

---

### Types de volumes

- `emptyDir` : volume vide, supprimé avec le Pod (mais partage entre conteneurs du pod) 
- `hostPath` : monte un répertoire du Host vers le Pod
- `configMap` : monte des fichiers de configuration
- `PersistentVolume` : `iscsi`, `nfs`, `cephfs`

---

## StatefulSet

- Permet de déployer des applications avec état : BDD, …
- Ressources **ordonnées** (ordre de lancement)
- Un même volume monté dans un pod le reste pour toujours (même après recréation)
- Un DNS dédié (`service headless`) :
  - load-balancing sur tous les pods du set
  - sélection d'un pod en particulier

---

## Configuration du cluster

* Metadata
* `Namespace` : espaces de noms isolant des ressources
  - cloisonne une partie du cluster
  - idem namespace Linux
* Rôles

---

## Role-Based Access Control (RBAC)

- `ClusterRole` : profil permettant des accès / actions / ressources
- `ServiceAccount` : user applicatif
  - génère des token (secrets) : à monter par exemple dans un `Pod` pour permettre l'accès
- `Cluster Role Binding` : association `ServiceAccount` <-> `ClusterRole`

---
layout: section
---

# Configuration avancée des Pods

---

## Healthcheck

- `Readiness`
  - démarrage du Pod
  - remplacement si défectueux
- `Liveness`
  - monitoring du Pod
  - redémarrage automatique si problème
- 3 modes : `exec` (commande), `httpGet`, `tcpSocket`

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

- autres stratégies en ajoutant d'autres outils :
  - **blue/green** : coexistance des 2 versions (dont la nouvelle pour test)
  - **canary deployment** : coexistance avec migration progressive des requêtes vers v2

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

---

# Commandes de base de Kubernetes® 

Voir la [cheatsheet sur Kubernetes®](https://www.avenel.pro/cours/docker/kubernetes-cheatsheet)

---
layout: section
---

# Outils externes

---

# Helm

- Gestionnaire de "paquets" k8s
  - en fait des fichiers Yaml
  - ajout du versionning
- `chart` : ensemble de fichiers manifests
- `hub` <https://hub.helm.sh/>

---

# FluxCD

- Outil Gitops pour k8s
    - scrute un dépôt Git distant
    - mise à jour automatique des ressources k8s
    - plus de CLI `kubectl`
    - Utilise des `Kustomizations` de `Kustomize` (outil intégré à k8s)
- intégrations Helm et Terraform
- CLI `fluxctl` (pas de GUI)
    - outils plus avancés : `argoscd`, `jenkins X`

---

![](https://raw.githubusercontent.com/fluxcd/flux2/main/docs/diagrams/fluxcd-controllers.png)
<!-- _class: legende -->
_Architecture de FluxCD (source: documentation FluxCD)_

---

# Kyverno

- Moteur de politiques pour k8s
- Gère des règles de sécurité, de conformité et de gestion (fichiers Yaml)
- DevSecOps

---
layout: two-cols
---

<!-- class: liens -->

# Liens

- [Site web Kubernetes](https://kubernetes.io/)
- Bacs à sable pour tester k8s : [killercoda](https://killercoda.com/playgrounds/scenario/kubernetes) et <https://labs.play-with-k8s.com/>
- Mini-distributions : <https://blog.palark.com/small-local-kubernetes-comparison/>
- [Introduction à k8s](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/introduction/)
- Cours sur kubernetes :
  - [uptime-formation](https://supports.uptime-formation.fr/05-kubernetes/01_cours_presentation_k8s/)
  - [stephane-robert](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/introduction/)
  - [vidéos xavki](https://www.youtube.com/watch?v=37VLg7mlHu8&list=PLn6POgpklwWqfzaosSgX2XEKpse5VY2v5)

::right::

- [Introduction à kubectl](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/kubectl/)
- <https://roadmap.sh/kubernetes>
- [Helm: package manager pour déployer dans k8s](https://helm.sh/)
    - [Introduction à Helm](https://www.aukfood.fr/helm-le-meilleur-ami-de-votre-kubernetes/)
- [Livre : Bootstrapping Microservices with Docker, Kubernetes, and Terraform](https://www.manning.com/books/bootstrapping-microservices-with-docker-kubernetes-and-terraform)
- <https://www.cortex.io/post/understanding-kubernetes-services-ingress-networking>

---
layout: two-cols
---

- Autoscaling : [doc](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) et [pratique](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
- [HPA Autoscaling depuis des métriques custom dans Prometheus](https://blog.zwindler.fr/2024/10/11/optimisation-ressources-kubernetes-autoscaling-horizontal-custom-metrics-prometheus-adapter/)
- [Werf: lier CI/CD et k8s](https://werf.io/)
- [Blue-Green deployment in k8s](https://developer.harness.io/docs/continuous-delivery/deploy-srv-diff-platforms/kubernetes/kubernetes-executions/create-a-kubernetes-blue-green-deployment/)
- [Canary deployment in k8s](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/canary-demo?view=azure-devops&tabs=yaml)
- <https://blog.wescale.fr/comment-rendre-une-application-haute-disponibilit%C3%A9-avec-kubernetes>
- <https://github.com/QJoly/kubernetes-coffee-image> : applications de test pour k8s (kustomize, helm, yaml, …)

::right::

- Tutoriels sur la communication entre pods :
  - [Utiliser un service](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)
  - [Tutoriel complet](https://medium.com/@extio/mastering-kubernetes-pod-to-pod-communication-a-comprehensive-guide-46832b30556b)
- [Exemple de monitoring Prometheus - Grafana dans un cluster Kubernetes](https://blog.octo.com/exemple-dutilisation-de-prometheus-et-grafana-pour-le-monitoring-dun-cluster-kubernetes)
- [Article très complet sur le service mesh Istio](https://une-tasse-de.cafe/blog/istio/)
- <https://spacelift.io/blog/kubernetes-secrets>
- [Learning Kubernetes, Pods & Deployments with Doom](https://www.youtube.com/watch?v=j9DOWkw9-pc)

---

<!-- class: legal -->

# Legal

- Docker®, Docker Swarm and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
[docker-cheatsheet]: https://www.avenel.pro/cours/docker/docker-cheatsheets.html
