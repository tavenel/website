---
title: Présentation du projet
description: Présentation du projet
type: projet
sidebar:
  order: 10
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
---
## 🎯 Objectif général

Déployer une **application multi-composants** (par exemple une application web avec front, back et base de données) dans un **environnement de type production**, en suivant les **bonnes pratiques DevOps**: conteneurisation, Infrastructure-as-Code, intégration et déploiement continus, observabilité et gestion des logs.

## Contexte

Dans le but de remporter un appel d’offres pour la réalisation d’un projet décrit ci-dessous, plusieurs équipes DevOps décident de réaliser un prototype répondant aux spécifications demandées.

Ces projets nécessitant un déploiement dans une infrastructure de Cloud, plusieurs équipes SysOps proposent le déploiement et la gestion de cette infrastructure complexe.

Dans le but d'accélérer le _time-to-market_ d'une application et d'augmenter la qualité de celle-ci, il est décidé de réaliser un déploiement continu de l'application par l'utilisation de conteneurs et de CI/CD, en utilisant un pattern d'Infrastructure-as-Code.

Le projet à utiliser est une application multi-composants (typiquement, une application Web). Ce projet devra être productivisé dans un cadre Devops (voir contraintes ci-dessous).

Le formateur jouera l'ensemble des rôles externes à l'équipe projet (et donc principalement celui de client pour l'application finale).

## Interactions Devops/Sysops

- La mission des équipes SysOps est la mise à disposition et la maintenance d’infrastructures de Cloud (une infrastructure différente par équipe) permettant le déploiement de conteneurs applicatifs Docker.
- Ces conteneurs applicatifs seront fournis par les équipes DevOps et contiendront le code métier du projet.
- Attention : tout conteneur applicatif de n’importe qu’elle équipe DevOps devra pouvoir être déployé sur n’importe quelle plateforme Cloud des équipes SysOps !
- Il pourra donc être nécessaire de définir un ensemble de spécifications communes, en accord avec l’ensemble des équipes projets.

## Résultat attendu

- Un document décrivant les différents éléments à mettre en place et résumant l'ensemble des principes Devops/Sysops suivis dans le projet et comment ceux-ci seront implémentés. Ce document sera remis en cours de réalisation
- Le ou les dépôts de code source utilisés, que ce soit pour la gestion du code source des applications métier, ou pour la gestion des configurations des infrastructures.
- Le rapport et les détails d'implémentation seront présentés lors d'une soutenance de projet faisant la démonstration de l'exécution et de l'intégration de votre partie du projet.

Si nécessaire, certains dépôts de code peuvent être partagés entre les équipes.

## Soutenance finale

La soutenance devra permettre de vérifier :

- Le fonctionnement de l'application.
- La capacité à reconstruire l'infrastructure à partir des fichiers IaC.
- Le fonctionnement du pipeline CI/CD.
- La portabilité de l'application entre plusieurs infrastructures SysOps.
- Le déploiement et la mise à jour de l'application en production.
- La prise en compte du zéro-downtime et de l'auto-scaling.
- La supervision de l'application et de l'infrastructure.

**La démonstration de l'intégration entre une équipe DevOps et une équipe SysOps constitue un élément central de la validation du projet.**
