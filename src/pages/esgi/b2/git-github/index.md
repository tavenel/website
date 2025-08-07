---
title: 󰊤  Tom Avenel - B2 GIT
layout: '@layouts/BaseLayout.astro'
---

# 󰊤  Versioning avec Git et Github

## Présentation du module

### 🎯 Objectifs du cours

- Installer et configurer l'outil Git
- Créer et configurer un dépôt avec Git
- Maîtriser les bases de l'outil Git (Clone, Checkout, Add, Commit, Push, Branch, Merge, ...).
- Comprendre la différence entre Git et GitHub et comment ils fonctionnent ensemble.
- Travailler avec une plateforme distante comme GitHub.
- Savoir utiliser la puissance des branches.
- Résoudre les conflits de commit
- Travailler en petites et grandes équipes avec Git.

### 📅 Déroulé du cours

Module de 12H

Évaluation : QCM et TP machine

#### Séance 1

- Introduction au versioning de code (cours)
- Partie pratique 1 : Premiers pas avec git
  - Rappels sur la ligne de commandes
  - Installation et configuration de Git
  - Création d'un premier dépôt : `git init`
  - Création d'un premier commit : `git add`, `git commit`

#### Séance 2

- Le modèle de branches (cours)
- Partie pratique 2 : Voyager et manipuler dans l'historique Git
  - Annuler un changement avant commit : `git reset`
  - Réécrire un commit : `git commit --amend`
  - Annuler un commit par ajout inverse : `git revert`
  - Se déplacer dans l'historique : `git checkout`
  - Modifier les index : `git reset --mixed` et `git reset --hard`
  - Supprimer des fichiers : `git rm`
- Partie pratique 3 : Utiliser un dépôt distant - Github
  - Création et configuration d'un compte GitHub
  - Création d'un dépôt distant
  - Récupération du dépôt distant : `git clone`
  - Gestion ds dépôts distants : `git remote`
  - Fusion de commits : `git merge`
  - Récupération de changements sans conflits : `git pull`
  - Envoi de changements locaux au dépôt distant : `git push`
  - Cas concret de travail collaboratif avec dépôt distant

#### Séance 3

- Introduction aux workflows collaboratifs (cours)
- Partie pratique 4 : Le systeme de branches
  - Afficher les branches : `git branch`
  - Supprimer une branche
  - Intégrer des commits dans une branche
  - Envoyer la branche vers un dépôt distant
- Examen : QCM et questions de cours notées

#### Séance 4

- Partie pratique 5 : Workflows Git
  - Intégration par branche de fonctionnalité
  - Intégrations avec partage de code
  - La pull-request
  - Workflow Gitflow
- Interfaces graphiques pour Git et intégration dans un IDE (cours)
- Partiel : Travail collaboratif avec Git

## 📑 Documents

- [🤓 Cours](/git/cours)
- [💻 TP - Premiers pas : installer & configurer git et les concepts de base](/git/tp-commit)
- [💻 TP - gitignore : utiliser le fichier spécial `.gitignore` pour masquer des fichiers à Git](/git/tp-gitignore)
- [💻 TP - Intégrer Git dans un IDE](/git/tp-ide)
- [💻 TP - Utiliser l'historique de Git™](/git/tp-historique)
- [💻 TP - Github® et dépôts distants](/git/tp-github)
- [💻 TP - Les branches Git™](/git/tp-branches)
- [💻 TP - Recherche dans un dépôt Git™](/git/tp-grep)
- [💻 TP - Workflows Git™ et Pull Request](/git/tp-workflows-pr) : _à réaliser en binôme._
- [💻 TP - Fork : découvrir le principe du fork pour partager des changements sur un logiciel sans impacter le dépôt officiel](/git/tp-fork)
## 🚀 Pour aller plus loin

- Voir les autres ressources du [cours sur Git](/git).
