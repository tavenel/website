---
title:   Tom Avenel - Versioning Git administrateur
layout: ../../../layouts/BaseLayout.astro
---

#  Versioning Git pour l'administrateur

## Présentation du module

### 🎯 Objectifs du cours

- Installer et configurer l'outil Git
- Créer et configurer un dépôt avec Git
- Maîtriser les bases de l’outil Git (Clone, Checkout, Add, Commit, Push, Branch, Merge, ...).
- Comprendre la différence entre Git et GitHub et comment ils fonctionnent ensemble.
- Travailler avec une plateforme distante comme GitHub.
- Savoir utiliser la puissance des branches.
- Résoudre les conflits de commit
- Utiliser Git pour gérer des configurations et scripts d'infrastructure
- Introduction à l'Intégration Continue (CI) avec les actions GitHub.
- Introduction à l'Infrastructure-as-Code (IaC) avec Git et Ansible

### 📅 Déroulé du cours

Module de 12H

Évaluation : QCM et TP machine

#### Plan détaillé

- Introduction au versioning de code (cours)
- Partie pratique 1 : Premiers pas avec git
  + Rappels sur la ligne de commandes
  + Installation et configuration de Git
  + Création d'un premier dépôt : `git init`
  + Création d'un premier commit : `git add`, `git commit`
- Le modèle de branches (cours)
- Partie pratique 2 : Voyager et manipuler dans l'historique Git
  + Annuler un changement avant commit : `git reset`
  + Réécrire un commit : `git commit --amend`
  + Annuler un commit par ajout inverse : `git revert`
  + Se déplacer dans l'historique : `git checkout`
  + Modifier les index : `git reset --mixed` et `git reset --hard`
  + Supprimer des fichiers : `git rm`
- Partie pratique 3 : Utiliser un dépôt distant - Github
  + Création et configuration d'un compte GitHub
  + Création d'un dépôt distant
  + Récupération du dépôt distant : `git clone`
  + Gestion ds dépôts distants : `git remote`
  + Fusion de commits : `git merge`
  + Récupération de changements sans conflits : `git pull`
  + Envoi de changements locaux au dépôt distant : `git push`
  + Cas concret de travail collaboratif avec dépôt distant
- Introduction aux workflows collaboratifs (cours)
- Partie pratique 4 : Le systeme de branches
  + Afficher les branches : `git branch`
  + Supprimer une branche
  + Intégrer des commits dans une branche
  + Envoyer la branche vers un dépôt distant
- Examen : QCM et questions de cours notées
- Partie pratique 5 : Workflows Git
  + Intégration par branche de fonctionnalité
  + Intégrations avec partage de code
  + La pull-request
  + Workflow Gitflow
- Interfaces graphiques pour Git et intégration dans un IDE (cours)
- Partiel : Travail collaboratif avec Git

## Documents

- [🤓 Cours](/cours/git/git-cours)
- [💻 TP - Premiers pas : installer & configurer git et les concepts de base](/cours/git/git-tp-commit)
- [💻 TP - gitignore : utiliser le fichier spécial `.gitignore` pour masquer des fichiers à Git](/cours/git/git-tp-gitignore)
- [💻 TP - Utiliser l'historique de Git™](/cours/git/git-tp-historique)
- [💻 TP - Github® et dépôts distants](/cours/git/git-tp-github)
- [💻 TP - Les branches Git™](/cours/git/git-tp-branches)
- [💻 TP Github - Utiliser les Gist](/cours/git/git-tp-github-gist)
- [💻 TP - Les tags](/cours/git/git-tp-tags)
- [💻 TP - Git pour un Projet XAMPP](/cours/git/git-tp-xampp) : Configurer un environnement de développement local avec XAMPP et utiliser Git pour versionner une application web stockée dans le dossier `htdocs`.
- [💻 TP - Manipulations avancées de la HEAD](/cours/git/git-tp-deplacer-head-avance)
- [💻 TP Neovim - gérer ses configurations avec Git](/cours/git/git-tp-iac-nvim)
- [💻 TP utiliser Ansible et Git pour réaliser de l'Infrastructure-as-Code](/cours/git/git-tp-ansible)

## Pour aller plus loin

- Voir les autres ressources du [cours sur Git](/cours/git).

