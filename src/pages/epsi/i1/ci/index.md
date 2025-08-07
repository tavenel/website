---
title:  Tom Avenel - I1 CD/CD
layout: '@layouts/BaseLayout.astro'
---

#  Serveurs d'intégration continue (CI/CD)

## Présentation du module

### 🎯 Objectif
 
- Comprendre les principes et les enjeux de l'intégration et du déploiement continus dans le cadre du développement d'une application informatique.

### Compétences à acquérir

- Connaître et utiliser les outils d'intégration continue : tests automatiques, analyse, reporting, ... ;
- Décrire, formaliser et implémenter des pipelines CI/CD ;
- Configurer un serveur d'intégration continue ;
- Choisir un modèle de déploiement continu adapté.

### 📅 Déroulé des séances

Module de 10H

Évaluation : Examen + Projet commun avec le module [tests automatiques](/epsi/i1/tests-auto)

### Séance 1

- Rappels de cours : l'intégration continue (cours)
- Le serveur d'intégration continue (cours)
- Présentation de Jenkins® (cours)
- TP Jenkins® (pratique)

### Séance 2

- Mini Quizz séance précédente (examen)
- Les outils de l'intégration continue (cours)
- Les processus d'intégration (cours)
- Les grands principes de l'intégration continue (cours)
- Fin du TP Jenkins® (pratique)

### Séance 3

- Mini Quizz séance précédente (examen)
- TD sur les workflow d'intégration continue
- Démarrage du projet noté (pratique)

### Séance 4

- Devoir surveillé sur l'intégration continue - 2H (examen)

## 📑 Documents

- [🤓 Cours sur l'intégration continue ](/ci/cours)
- [Exemple de pipeline Jenkinsfile](/jenkins/jenkinsfile)
- [Exemple de pipeline pour Github Actions](/ci/exemple-github-actions)
- [Exemple de pipeline pour Gitlab CI](/ci/exemple-gitlab-ci)

### Exercices

- [📝 TD Processus d'intégration continue](/ci/td_process_ci) : une étude de cas d'intégration continue.

### TPs

- [💻 TP - Workflows Git™ et Pull Request](/git/tp-workflows-pr) : L'objectif de ce TP est de travailler sur un projet en suivant des workflows Git et de s'initier au principe de la pull-request.
- [ TP Jenkins](/jenkins/tp-full)
  -  Sources pour le TP : <https://git.sr.ht/~toma/jenkins_exemples>
- [💻 TP Intégration continue avancée](/ci/tp_ci_avance) : des exercices pour pousser plus loin l'intégration continue.

### 🏆 Projet noté CI/CD et Automatisation des tests - un jeu de rôle

Le projet consiste à développer une application Web permettant à un joueur de jouer à un jeu de rôle contre l'ordinateur.

_Après étude des besoins du client, vous décidez de développer cette application suivant un processus d'intégration continue, afin d'accélérer le développement du projet et pour garantir la qualité des fonctionnalités implémentées._

- [📄 Lien vers le sujet](/tests/projet_jeu_roles_tests_et_ci)

## 🚀 Pour aller plus loin

- [💻 TP Workflow : support de versions concurrentes](/ci/td_workflow_versions_concurrentes) : Simulation d'un workflow Git permettant de maintenir en concurrence deux versions stables d'un produit et une version en cours de développement.
- Voir les autres ressources du [cours sur l'intégration continue](/ci).
