---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Le DevOps
layout: '@layouts/CoursePartLayout.astro'
---

# Objectifs
 
- Gérer ses projets tant en développement qu'en infrastructure en adoptant une approche Devops / Sysops

---

# Problèmes courants

- Silos entre les équipes Dev et Ops
  - Manque de collaboration
  - Problèmes de gouvernance, frictions
  - Pas de visibilité sur les process

---

# Problèmes courants

- Absence d'automatisation
  - Tâches manuelles répétitives sur de gros systèmes
  - Délais de livraison importants
  - Problèmes lors de la mise en production (erreurs, pannes)
  - Tests au dernier moment
  - Interruptions de service

---

# Devops

> Le DevOps est un ensemble de pratiques, de philosophies et d'outils visant à combiner les pratiques de développement (Dev) et les pratiques opérationnelles (Ops).

- Objectif : développement et déploiement d'applications / services en un temps record.
- RH déploiement et maintenance réduites par la mutualisation des compétences.
- Réconcilier 2 mondes : ops = stabilité, dev = vitesse

---

# Les 5 piliers CALMS du DevOps

- **Culture** :
	- Équipes transverses orientées produit
	- Gérer le risque et les erreurs
- **Automatisation** :
  - Coder l'Infrastructure (**IaC**)
	- Intégration & Livraison Continus (**CI/CD**)
- **Lean**
  - Amélioration continue
	- Livraison au plutôt, **itérations**
- **Mesurer** :
  - Monitoring continu.
- **Share** :
  - Collaboration
	- _Feedback loop_

---

# Culture DevOps

- But commun : la réussite du projet
- Collaboration étroite entre les équipes : dev, ops, QA, marketing, …
- Gestion de projet itérative
- Livraisons fréquentes
- Focus sur la continuité du service et la résolution rapide des problèmes

---

# Infrastructure as Code (IaC)

> Coder (scripts, fichiers de configuration) une infrastructure informatique virtuelle.

---

- Automatise le déploiement intégral d'applications :
  + de la couche infrastructure (généralement un Cloud privé)
  + à la couche logicielle.

---

- Déploiement facile et rapide des environnements de test
  + Facilite CI/CD

---

- Exemples d'outils IaC : Ansible® / Terraform / Puppet
- Souvent : fichiers `Yaml`

---

# Gestion des versions

- Objectif : segmenter tout changement et gérer un historique :
  + Dans le code ;
  + Sur la plateforme.

Voir le [cours sur les gestionnaires de versions (Git)][site-perso].

---
layout: section
---

# Intégration continue

> Ensemble de pratiques permettant de réduire la feedback loop.

Voir le [cours d'introduction sur l'intégration continue][site-perso].

---

# Les outils de l'intégration continue

Voir le [cours sur les outils de l'intégration continue][site-perso].

---

# Isolation par conteneurs

- Base de la culture DevOps
  + Docker

---

## Avantages

- \+ Immutabilité image de production :
  * Instances des applications générées depuis une image figée ;
  * Un seul livrable de production ;
  * Changements d'état sont minimaux et non critiques ;
- \+ Une instance applicative doit donc pouvoir être détruite et recréée à n'importe quel moment !

---

- \+ Environnement applicatif invariant :
  * Abstraction plateforme d'exécution ;
  * Dev, CI/CD, production => même image, OS, dépendances, ...
  * Tests dans même environnement que la production.

---

# Pet vs Cattle

- _Pet_ : approche traditionnelle : quelques grosses VM
  - backup de la VM
  - opérations manuelles dans la VM
  - modification de la VM au cours du temps
- _Cattle_ : approche DevOps : des 100aines de conteneurs
  - conteneurs anonymes, immuables, jetables
  - fichiers de config (templates)
  - changement de besoin => destruction, reconstruction

---

# Orchestration CI/CD

- Infrastructures dev et prod DevOps complexes => Serveurs CI
  + `Jenkins`, `Gitlab`
  + Code source -> image Docker -> pipeline CI : analyse statique, tests unitaires / intégration, livraison **images** Docker

---

# Orchestration production (technique)

- Orchestrateur `Docker` (`Kubernetes`, `Swarm`, ...)
  + Création automatique des instances des applications ;
  + Redondance, résilience, équilibre de charge, routage, ...

---

# Orchestration production (métier)

`Kubernetes` => orchestration technique != orchestration liée au code métier (microservices, ...).
  + Souvent orchestrateur _business_ supplémentaire : _registry_ `Spring Cloud`, _load balancer_ `NginX`, ...

---

# Observabilité

- Déploiements complexes => suivi **minutieux** et **automatisé** :
  + Observabilité plateforme Cloud et conteneurs : `Prometheus®` / `Grafana®` ;
  + Observabilité du métier applicatif : corrélation logs, …

---

## Types d'observabilité

- **logs** : messages des applications, à centraliser : `Loki`, `ELK`, `fluentd`, …
- **métriques** (sondes) : indicateurs sur la santé des composants : CPU, latence réseau, mémoire, … : `prometheus`
- **traces** : suivi d'un utilisateur / une requête à travers tout le système : `zipkin`, `OpenTelemetry`, …

Cette observabilité doit se coupler à des **alertes** en cas de souci !

---

# Chaos Engineering

- Idée : "casser" les systèmes volontairement pour tester l'observabilité et la reprise sur erreur
  - ex: scripts faisant tomber un service, …
- Populaire en sécurité : DevSecOps et SRE

---

# Liens avec l'agilité

- Nombreux outils provenant des pratiques des méthodes agiles :
  + Automatisation des compilations et des tests ;
  + Intégration continue ;
  + Déploiement continu ;
  + Gestion de projet agile particulièrement indiquée.

---

_L'association des pratiques DevOps et Agiles est si courante que ces deux concepts sont parfois confondus, mais leur but est différent : les méthodes agiles visent à **rapprocher l'équipe de développement du client final**, là où les pratiques DevOps tentent de **réconcilier les équipes de développement et les équipes opérationnelles**._

---

# Lien avec les micro-services

- Devops très adapté micro-services
  + Facilite CI/CD d'une partie métier de l'application.

---

## 12 factor apps

- Micro-services ~= SaaS
  + <https://12factor.net/fr/>

---

# Inconvénients du DevOps

- Infrastructure plus complexe
  - Outils supplémentaires : CI/CD, orchestration, monitoring, …
  - Attention à la sécurité
  - Attention à l'automatisation excessive
- Coûts initiaux élevés
  - Mise en place d'une nouvelle infrastructure et d'outils d'automatisation.
  - Formation aux outils et process
- Résistance au changement (culture organisationnelle différente)

---

# Du Devops au Devops/Sysops

- Objectif DevOps == une équipe Dev et Ops mais :
  + Architectures SaaS très complexes ;
  + Besoin de compétences variées ;
  + Métier spécialisé dans **la gestion de l'infrastructure SaaS** : _SysOps_.

---

> Le _SysOps_ gère l'ensemble de l'infrastructure physique et logicielle permettant le déploiement de conteneurs applicatifs (stack réseau, gestion des données, kubernetes, ...).
> Le métier de _DevOps_ consiste alors à développer et déployer des applications métier dans des conteneurs applicatifs sur cette plateforme.

---

# Variations du Devops

- Nombreuses variations adaptées à des contextes particuliers :
  + `DataOps` : adaptation au contexte très spécifique du Big Data (variation la plus courante) ;
  + `ArchOps` : réflexions d'architecture dans la boucle DevOps ;
  + `TestOps` : focus tests ;
  + `DevSecOps` : focus sécurité, ...
  + `GitOps` : Automatisation et Gestion des Infrastructures par Git

---

# GitOps

- `Git` == source de vérité pour code et déploiement applications et infrastructure
- Tous les changements (infrastructure et configurations) sont gérés et versionnés dans un dépôt Git (IaC).
- Un outil GitOps (`FluxCD`, `ArgoCD`, `Jenkins X`) surveille les changements dans Git et applique automatiquement les mises à jour au cluster (ex. `Kubernetes`).
- Traçabilité, Reproductibilité, Sécurité, Fiabilité, Rollbacks

---

# Métiers

- Même si l'on trouve de nombreux postes estampillés _devops_, ce n'est pas un métier mais une philosophie !
- Quelques métiers où l'on pratique quotidiennement le DevOps : _SRE_ (_Site Reliability Engineer_), _Platform engineer_

---

# Glossaire

- _DevOps_ : ensemble de pratiques, de philosophies et d'outils visant à combiner les pratiques de développement (Dev) et les pratiques opérationnelles (Ops).
- _SysOps_ : gère l'ensemble de l'infrastructure physique et logicielle permettant le déploiement de conteneurs applicatifs (stack réseau, gestion des données, kubernetes, ...).

---

- _IaC_ : Infrastructure-as-Code : Coder (scripts, fichiers de configuration) une infrastructure informatique virtuelle.
- _CI_ : Continuous Integration (Intégration Continu). Ensemble de pratiques permettant de réduire la feedback loop.
- _CD_ : Continuous Delivery/Deployment (Déploiement Continu). Mise en production automatique des artéfacts générés par la CI.
- _SaaS_ : Software-as-a-Service. Application hébergée sur le cloud et accessible directement à l'utilisateur final.

Voir aussi : <https://blog.stephane-robert.info/docs/glossaire/>

---

<!-- class: liens -->
# Liens

- Voir une sélection d'outils DevOps sur le [site web][site-perso]
- <https://roadmap.sh/devops>
- <https://www.damyr.fr/glossaire/>
- [Exemple de pipeline Jenkins YAML en Infrastructure-as-Code][gist-jenkins-pipeline-yaml]
- [Tutoriel OpenClassrooms sur le monitoring applicatif en Devops][tuto-openclassrooms-monitoring]
- [Exemple de monitoring Prometheus - Grafana dans un cluster Kubernetes](https://blog.octo.com/exemple-dutilisation-de-prometheus-et-grafana-pour-le-monitoring-dun-cluster-kubernetes)
- [Jeu Metrics, logs, traces, and mayhem pour s'entraîner à Grafana](https://grafana.com/blog/2024/11/20/metrics-logs-traces-and-mayhem-introducing-an-observability-adventure-game-powered-by-grafana-alloy-and-otel/)
- <https://github.com/bregman-arie/devops-exercises> : questions d'entretien
- [Le métier SRE](https://blog.zwindler.fr/talks/2022-sre-sre-partout/index.html)
- [Livres SRE (google)](https://sre.google/books/)
- [Schéma des outils Devops](https://platformengineering.org/platform-tooling)
- <https://github.com/stephrobert/awesome-french-devops>
- [Topologie d'équipes DevOps](https://blog.stephane-robert.info/docs/devops/team-toplogies-devops/)
- [Recueil de liens et mindmap des outils DevSecOps](https://blog.stephane-robert.info/docs/)
- [xavki - Vidéos sur le Devops](https://www.youtube.com/playlist?list=PLn6POgpklwWrBPMKFniOiMyLMdxlgFhrG)
- [xavki - roadmap DevOps](https://www.youtube.com/watch?v=1W0oUxaJz_8)
- [Playlist 90 days of DevOps](https://yewtu.be/playlist?list=PLsKoqAvws1psCnkDaTPRHaqcTLSTPDFBR)
- [OpenClassrooms : Découvrez la méthodologie DevOps](https://openclassrooms.com/fr/courses/6093671-decouvrez-la-methodologie-devops)

[gist-jenkins-pipeline-yaml]: https://gist.github.com/jonico/e205b16cf07451b2f475543cf1541e70
[tuto-openclassrooms-monitoring]: https://openclassrooms.com/fr/courses/2035736-mettez-en-place-lintegration-et-la-livraison-continues-avec-la-demarche-devops/6183162-monitorez-votre-application

