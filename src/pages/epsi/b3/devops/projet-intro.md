---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Présentation du projet
layout: '@layouts/CoursePartLayout.astro'
---

## Contexte de l'atelier

Dans le but de remporter un appel d’offres pour la réalisation d’un projet décrit ci-dessous, plusieurs équipes DevOps décident de réaliser un prototype répondant aux spécifications demandées.

Ces projets nécessitant un déploiement dans une infrastructure de Cloud, plusieurs équipes SysOps proposent le déploiement et la gestion de cette infrastructure complexe.

Afin de gérer efficacement le projet, celui-ci sera réalisé en suivant les principes des méthodes Agiles.

## Résultats attendus

### Partie Devops/Sysops

- Un court document décrivant l’ensemble des principes Devops/Sysops suivis dans le projet et comment ceux-ci ont été implémentés
- Le ou les dépôts de code source utilisés, que ce soit pour la gestion du code source des applications métier, ou pour la gestion des configurations des infrastructures.
- Le rapport et les détails d'implémentation seront présentés lors d'une soutenance de projet (dernier cours).

Si nécessaire, certains dépôts de code peuvent être partagés entre les équipes.

### Partie agile

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

## Environnements à déployer

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

