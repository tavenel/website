---
title: Atelier DevOps-SysOps & Atelier Méthodes Agiles
date: 2022 / 2023
tags:
- devops
- agile
- docker
- ci
- jenkins
---

## Contexte de l'atelier

Dans le but de remporter un appel d’offres pour la réalisation d’un projet décrit ci-dessous, plusieurs équipes DevOps décident de réaliser un prototype répondant aux spécifications demandées.

Ces projets nécessitant un déploiement dans une infrastructure de Cloud, plusieurs équipes SysOps proposent le déploiement et la gestion de cette infrastructure complexe.

Afin de gérer efficacement le projet, celui-ci sera réalisé en suivant les principes des méthodes Agiles.

## Présentation du projet

### Contexte

Le projet à utiliser est une application multi-composants (typiquement, une application Web) - on pourra réutiliser une application déjà créée par le groupe (à préférer) ou l'application donnée en exemple. Ce projet devra être productivisé dans un cadre Devops (voir contraintes ci-dessous).

Le formateur jouera l'ensemble des rôles externes à l'équipe projet (et donc principalement celui de client pour l'application finale).

### Contraintes

Certaines contraintes ont déjà été identifiées sur le projet. Ces contraintes sont susceptibles d’évoluer en fonction des retours des utilisateurs, et de nouvelles contraintes pourront être ajoutées par le client si besoin.

- **Déploiement au plus tôt :** le projet est très prometteur et de nombreux concurrents se sont déjà positionnés sur le marché. Il est donc absolument primordial de disposer d’une première version en production de toute urgence afin de créer un marché captif au plut tôt. Cette version sera certainement très limitée dans un premier temps, et améliorée au fur et à mesure des mises à jour.
- **Auto-scaling** : il est difficile de prévoir le modèle d’adoption des applications proposées, cependant le service marketing prévoit déjà une montée en charge importante des utilisateurs dès les premières itérations. Il est donc nécessaire que l'infrastructure supporte un service de scaling **dès la 2e itération**
- **Zero-downtime** : ce projet est critique pour le business du client, celui-ci insiste sur le fait qu'il n’est pas envisageable d’avoir une interruption de service lors de la mise à jour des composants applicatifs ou lors de changements dans l'infrastructure.

## Partie Devops/Sysops

Le projet sera réalisé en suivant les préconisations des pratiques DevOps et SysOps.

L’ensemble des points ci-dessous sont des réflexions à avancer en parallèle pour permettre une compatibilité entre chaque point technique du projet.

### Environnements à déployer

La mission des équipes SysOps est la mise à disposition et la maintenance d’infrastructures de Cloud (une infrastructure différente par équipe) permettant le déploiement de conteneurs applicatifs Docker.

Ces conteneurs applicatifs seront fournis par les équipes DevOps et contiendront le code métier du projet.

**Attention : tout conteneur applicatif de n’importe qu’elle équipe DevOps devra pouvoir être déployé sur n’importe quelle plateforme Cloud des équipes SysOps !**

**Il pourra donc être nécessaire de définir un ensemble de spécifications communes, en accord avec l’ensemble des équipes projets.**

L’infrastructure physique utilisée comme support pourra être au choix :

- Une ou plusieurs VMs d'un serveur physique
- Une infrastructure d’IaaS (Amazon Web Services, ...)
- Des machines virtuelles locales (Oracle® VirtualBox, ...)

- Afin de pouvoir déployer des conteneurs, il faudra un environnement de production robuste : on déploira donc un cluster Kubernetes.
- Il n'est bien sûr pas envisageable de déployer directement une application non testée en production. On veillera donc à créer un 2e environnement qui servira de test et/ou staging. Les contraintes étant moindres sur cet environnement, on pourra au choix déployer un autre cluster Kubernetes (limité) ou se contenter d'un orchestrateur `docker-compose`.

### Isolation par conteneurs

Il est demandé d'isoler chaque composant métier dans des conteneurs applicatifs. On utilisera donc des conteneurs Docker, que l'on pourra stocker dans le répertoire d’images par défaut (_Docker Hub_) ou dans une registry privée de l’équipe déployée dans le datacenter de test/staging.

Dans un véritable environnement de production, la sécurisation de ce répertoire d’images est une contrainte importante et pouvant induire des choix d'architecture spécifique. Pour le prototype, on pourra exceptionnellement omettre ces questions de sécurité pour simplifier le déploiement.

### Infrastructure as Code (IaC)

Afin de suivre la recommandations DevOps d'IaC, il est demandé de rendre reproductible tous les déploiements sous forme de fichiers de code et/ou de fichiers de configuration (Yaml, …).

On utilisera `Ansible` pour automatiser l'installation et la configuration des environnements : `Docker` / `k8s`,  stack applicative . On ne demande cependant pas de provisionner les OS des serveurs des différents environnements depuis `Ansible` (on démarrera donc le projet avec un ou plusieurs OS déjà installés). On pourra également utiliser `Terraform` pour provisionner les ressources (optionnel).

L'ensemble du code nécessaire au déploiement et à la maintenance de l'infrastructure (scripts, fichiers de configuration, …) devront également être versionnés dans un ou plusieurs dépôt(s) de code partagés.

### Intégration continue (CI)

Afin de garantir l’intégrité des images déployées, on mettra en place un pipeline de CI/CD contenant à la fois des étapes de contrôle de la qualité (tests automatiques, analyse statique de code, …) et la génération et publication des artéfacts de production.

Ce pipeline devra donc en priorité générer une image Docker depuis un commit du code source provenant du dépôt de code.

Pour l'exécution du pipeline, on pourra au choix :

- Déployer un orchestrateur d'intégration continue : `Jenkins`, `Gitlab`, …
- Utiliser un orchestrateur SaaS : pipelines `Bitbucket`, `Gitlab` cloud, `Github`

Attention à bien respecter les contraintes d'IaC : la configuration du CI/CD devra ausssi être scripté (en général, fichiers `Yaml`) !

:::link
Pour utiliser Jenkins avec Docker en IaC, on pourra se référer à la documentation des pipelines : <https://www.jenkins.io/doc/book/pipeline/docker/>
:::

### Déploiement continu (CD)

Une fois les composants applicatifs générés, il faut pouvoir réaliser leur déploiement sur la plateforme. 

En bonus, on pourra réaliser également un _déploiement continu de l'infrastructure_ suivant un modèle _GitOps_, grâce à un outil comme `fluxCD` (ou `ArgoCD`, plus complet mais plus compliqué). Ces outils permettent de mettre à jour automatiquement l'infrastructure de production depuis le dépôt Git des fichiers de configuration de k8s !

En absence de déploiement continu de l'infrastructure, il est tout de même demandé une mise à jour automatique des composants métier en utilisant des scripts et/ou des exécutions Ansible / Terraform.

#### Zero-downtime

L'application devra être mise à jour en respectant des contraintes de zero downtime : les clients doivent pouvoir accéder en permanence à l'application. On réfléchira donc à l'adaptation du modèle de déploiement continu, et on pourra utiliser un outil comme `flagger` pour éviter une interruption de service.

On ne demande cependant pas de mettre en place un HA proxy (pas de "vrai" service de haute disponibilité).

### Observabilité

Un système de monitoring devra être mis en place, tant au niveau métier (crash de l'application, …) qu'au niveau de l'infrastructure technique (état des services `Docker` ou `k8s`, …)

L'utilisation du couple `Prometheus` / `Grafana` est la solution de monitoring par excellence dans les environnements Cloud. `Grafana` est un outil puissant d'affichage de tableaux de contrôles. `Prometheus` est un outil de monitoring disposant de multiples sondes permettant de surveiller presque tout type d'application (et d'afficher des tableaux de contrôle minimalistes). `Prometheus` s'intègre très bien avec `Grafana` et les 2 outils sont presque toujours utilisés ensemble.

Pour récupérer des sondes `Docker`, on pourra utiliser si besoin `cAdvisor` qui permet d'envoyer à `Prometheus` les informations des conteneurs.

:::link
- Pour apprendre à configurer simplement `Prometheus`, `Grafana` et `cAdvisor` en utilisant `docker compose`, on pourra par exemple utiliser [ce tutoriel](https://pramodshehan.medium.com/containers-metrics-in-prometheus-and-grafana-389555499eb8).
- On pourra, au choix, créer son propre dashboard dans `Grafana`, ou utiliser un modèle existant, par exemple : <https://grafana.com/grafana/dashboards/179-docker-prometheus-monitoring/>.
:::

### Logging centralisé

Un environnement de type Cloud peut contenir de nombreux éléments, générant chacun des logs. Or il est important en cas de problème d'être capable de corréler les différents éléments de l'architecture, et les différents composants applicatifs.

Pour faciliter ce travail, on mettra en place un système de logging centralisé : stack ELK, …

Si ce travail est nécessaire en 1e approche, ce n'est souvent pas suffisant dans un cas réel, car il devient vite compliqué de suivre la requête d'un client depuis le reverse proxy à l'entrée du datacenter, jusqu'aux différents services applicatifs et techniques. En pratique, on utilise donc également des outils de tracing qui permettent de suivre précisément une requête à travers tous les composants déployés : `zipkin`, `OpenTelemetry`, … On ne demande pas de mettre en place ce service de tracing dans ce projet.

## Partie Méthodes Agiles

Le projet sera réalisé en plusieurs itérations, en utilisant la méthodologie `Scrum`.

### Répartition des rôles Scrum

Assigner à chaque membre de l'équipe, un ou plusieurs rôles nécessaires à la conduite d'un projet suivant la méthode `Scrum`.

_Le formateur jouera l'ensemble des rôles externes à l'équipe projet (et donc principalement celui de coach agile et de client pour l'application finale)._

### Création du backlog

Réaliser un backlog initial du projet. On pourra s'aider d'un story mapping, mais cela n'est pas une obligation.

De même, l'utilisation d'Épics est possible mais n'est pas obligatoire.

### Réaliser les sprints

Les projets Scrum utilisent en général des sprints de 1 à 3 semaines. Pour s'entraîner à la gestion itérative d'un projet, ce projet sera réalisé en plusieurs sprints de durée arbitraire.

Attention : En Scrum, chaque User Story correspond à l’ajout d’une fonctionnalité **métier** dans le projet !

L'ensemble des cérémonies Scrum devra être respecté pendant l'itération, notamment :

- La réunion de planification du Sprint
- Les réunions de stand-up avant chaque nouvelle journée
- La revue puis la rétrospective en fin de Sprint

On prendra soin également de calculer la **vélocité** et le **burndown** après chaque Sprint.

### Outil utilisé

Le suivi du projet sera réalisé grâce à l'outil Jira d'Atlassian, disponible gratuitement en SaaS pour de petites équipes : https://www.atlassian.com/fr/software/jira

Pour réaliser le suivi du projet :

1. Créer un nouveau projet de type "Scrum" (ce choix est disponible à l'inscription)
1. Commencer par remplir l'onglet Backlog
   1. Entrer les User Stories du backlog
   1. Penser à remplir les Story Points lorsque nécessaire, pour permettre la génération des rapports
   1. Entrer les sous-tâches des stories lorsque nécessaire, depuis la vue d'une User Story
1. Dans l'onglet Backlog, il est possible de :
   1. Créer un (ou plusieurs) Sprint(s)
   1. Plannifier un (ou plusieurs) Sprint(s)
   1. Démarrer le prochain Sprint
1. Une fois démarré, le Sprint en cours est visible dans l'onglet "Sprints actifs"
   1. Déplacer les différentes Tâches (et/ou User Story directement) du tableau Kanban pendant l'exécution du Sprint, afin de refléter leur état à chaque instant. Penser à assigner les tâches !
   1. Une fois le Sprint réalisé, cliquer sur "Terminer le Sprint".
   1. Analyser les différents rapports générés. Depuis l'onglet "Rapport de Sprint", cliquer sur "Exécuter la rétrospective" pour démarrer une rétrospective en utilisant Confluence (l'outil de Wiki d'Atlassian).

On pourra également utiliser l'outil EasyRetro : <https://easyretro.io/>

## Résultat attendu 

Il est attendu pour chaque groupe un rendu pour la partie atelier Devops/Sysops et un rendu pour la partie atelier Agile. Chaque partie sera notée indépendamment.

### Partie Devops/Sysops

- Un court document décrivant l’ensemble des principes Devops/Sysops suivis dans le projet et comment ceux-ci ont été implémentés
- Le ou les dépôts de code source utilisés, que ce soit pour la gestion du code source des applications métier, ou pour la gestion des configurations des infrastructures.
- Le rapport et les détails d'implémentation seront présentés lors d'une soutenance de projet (dernier cours).

Si nécessaire, certains dépôts de code peuvent être partagés entre les équipes.

### Partie Méthodes Agiles

- Un projet Scrum configuré dans Jira, avec l'ensemble des User Story et Tâches enregistrées et à jour
  - Penser à donner les droits d'accès au formateur ! Une solution simple est d'inclure le formateur dans l'équipe projet.
  - Attention à ajouter les droits d'accès en cas d'utilisation d'autres outils !
- L'exécution de plusieurs sprints, avec pour chacun d'entre eux :
  - Un livrable, c'est-à-dire un produit prêt à être livré au client
  - Un calcul de la vélocité et du burndown
  - Une revue de Sprint, qui sera effectuée avec le client (*i.e. le formateur*). Cette revue comportera une démonstration du travail réalisé pendant le Sprint. Attention, il n'est pas demandé de détailler l'ensemble du produit, mais bien de proposer au client une démonstration de ce qui l'intéresse.
  - Une rétrospective du Sprint.
    - La page Confluence générée par Jira pour la rétrospective devra être utilisée comme la page d'accueil du rapport, même s'il est possible d'utiliser un autre outil, par exemple <https://easyretro.io/> et d'ajouter un lien dans Confluence vers la rétrospective générée dans cet autre outil.
    - On intègrera également le résultat de la revue (livrable et commentaires éventuels) sur cette page, directement ou via un lien vers ce livrable

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker, Docker Swarm and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Prometheus®, Kubernetes® and K8s® are registered trademarks of The Linux Foundation in the United States and/or other countries.
- Oracle and Oracle® VirtualBox are registered trademarks of Oracle and/or its affiliates.
- Amazon Web Services are trademarks of Amazon.com, Inc. or its affiliates in the United States and/or other countries
- Jenkins® is a registered trademark of LF Charities Inc.
- Bitbucket and Jira are registered trademarks of Atlassian Pty Ltd.
- GitLab is a registered trademark of GitLab Inc.
- GITHUB is a trademark of GitHub, Inc., registered in the United States and other countries.
- Grafana® is a registered trademark of Raintank, Inc. dba Grafana Labs (“Grafana Labs”).
