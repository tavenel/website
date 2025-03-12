---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Présentation du projet
layout: '@layouts/CoursePartLayout.astro'
---

## Contexte

Dans le but d'accélérer le _time-to-market_ d'une application et d'augmenter la qualité de celle-ci, il est décidé de réaliser un déploiement continu de l'application par l'utilisation de conteneurs et de CI/CD, en utilisant un pattern d'Infrastructure-as-Code.

Le projet à utiliser est une application multi-composants (typiquement, une application Web) - on pourra réutiliser une application déjà créée par le groupe (à préférer) ou l'application donnée en exemple. Ce projet devra être productivisé dans un cadre Devops (voir contraintes ci-dessous).

Le formateur jouera l'ensemble des rôles externes à l'équipe projet (et donc principalement celui de client pour l'application finale).

## Résultat attendu 

- Un document décrivant les différents éléments à mettre en place et résumant l'ensemble des principes Devops suivis dans le projet et comment ceux-ci seront implémentés. Ce document sera remis en cours de réalisation
- Le ou les dépôts de code source utilisés, que ce soit pour la gestion du code source des applications métier, ou pour la gestion des configurations des infrastructures.
- Le rapport et les détails d'implémentation seront présentés lors d'une soutenance de projet (dernier cours).

## Environnements à déployer

- Afin de pouvoir déployer des conteneurs, il faudra un environnement de production robuste : on déploira donc un cluster Kubernetes. Étant donné les ressources limitées sur ce projet, on pourra se limiter à une machine virtuelle tournant sur la machine d'un des apprenants afin de démarrer un noeud Kubernetes unique (par exemple, un déploiement Minikube).
- Il n'est bien sûr pas envisageable de déployer directement une application non testée en production. On veillera donc à créer un 2e environnement qui servira de test et/ou staging. Les contraintes étant moindres sur cet environnement, on pourra au choix déployer un autre cluster Kubernetes (limité) ou se contenter d'un orchestrateur `docker-compose`.

