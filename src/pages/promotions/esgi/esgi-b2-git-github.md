---
title: 󰊤  Tom Avenel - B2 GIT
---

# 󰊤  Versioning avec Git et Github

![](/resources/images/cover/git.jpg)

## Présentation du module

### 🎯 Objectifs du cours

- Installer et configurer l'outil Git
- Créer et configurer un dépôt avec Git
- Maîtriser les bases de l’outil Git (Clone, Checkout, Add, Commit, Push, Branch, Merge, ...).
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

## Documents

### 🤓 Cours

- [html](/cours/git/git-cours.html)
- [pdf](/cours/git/git-cours.pdf)
- [markdown](/cours/git/git-cours.md)

### 💻 TP - Premiers pas (le commit)

L'objectif de ce TP est d'installer et de configurer git, puis de se familiariser avec ses concepts de base.

- [html](/cours/git/git-tp-commit.html)
- [pdf](/cours/git/git-tp-commit.pdf)
- [markdown](/cours/git/git-tp-commit.md)

### 💻 TP - Le gitignore

L'objectif de ce TP est d'utiliser le fichier spécial `.gitignore` pour masquer des fichiers à Git.

- [html](/cours/git/git-tp-gitignore.html)
- [pdf](/cours/git/git-tp-gitignore.pdf)
- [markdown](/cours/git/git-tp-gitignore.md)

### 💻 TP - Intégrer Git dans un IDE

L'objectif de ce TP est d'utiliser Git directement dans l'IDE et d'y afficher les derniers changements dans le code.

- [html](/cours/git/git-tp-ide.html)
- [pdf](/cours/git/git-tp-ide.pdf)
- [markdown](/cours/git/git-tp-ide.md)

### 💻 TP - Utiliser l'historique de Git™

L'objectif de ce TP est d'utiliser les fonctions d'historique de git.

- [html](/cours/git/git-tp-historique.html)
- [pdf](/cours/git/git-tp-historique.pdf)
- [markdown](/cours/git/git-tp-historique.md)

### 💻 TP - Github® et dépôts distants

 L'objectif de ce TP est de créer, configurer et utiliser un dépôt git distant sur la plateforme Github®.

- [html](/cours/git/git-tp-github.html)
- [pdf](/cours/git/git-tp-github.pdf)
- [markdown](/cours/git/git-tp-github.md)

### 💻 TP - Les branches Git™

 L'objectif de ce TP est de manipuler un des concepts les plus puissants de Git™ - la notion de branches.

- [html](/cours/git/git-tp-branches.html)
- [pdf](/cours/git/git-tp-branches.pdf)
- [markdown](/cours/git/git-tp-branches.md)

### 💻 TP - Les tags

Petit TP permettant de découvrir les tags dans Git.

- [html](/cours/git/git-tp-tags.html)
- [pdf](/cours/git/git-tp-tags.pdf)
- [markdown](/cours/git/git-tp-tags.md)

### 💻 TP - Workflows Git™ et Pull Request

 L'objectif de ce TP est d'utiliser de travailler sur un projet en suivant des workflows Git et de s'initier au principe de la pull-request.
 **L'intégralité de ce cas pratique est à réaliser en binôme.**

- [html](/cours/git/git-tp-workflows-pr.html)
- [pdf](/cours/git/git-tp-workflows-pr.pdf)
- [markdown](/cours/git/git-tp-workflows-pr.md)

### 💻 TP - Workflow de Fork

 L'objectif de ce TP est de découvrir le principe du fork pour partager des changements sur un logiciel sans impacter le dépôt officiel.

- [html](/cours/git/git-tp-fork.html)
- [pdf](/cours/git/git-tp-fork.pdf)
- [markdown](/cours/git/git-tp-fork.md)

### 💻 TP - Git™ Bisect

 L'objectif de ce TP est d'utiliser la commande Git Bisect pour trouver un commit par dichotomie.

- [html](/cours/git/git-tp-bisect.html)
- [pdf](/cours/git/git-tp-bisect.pdf)
- [markdown](/cours/git/git-tp-bisect.md)

### 💻 TP - Git pour un Projet XAMPP

Configurer un environnement de développement local avec XAMPP et utiliser Git pour versionner une application web stockée dans le dossier `htdocs`.

- [html](/cours/git/git-tp-xampp.html)
- [pdf](/cours/git/git-tp-xampp.pdf)
- [markdown](/cours/git/git-tp-xampp.md)

### 💻 TP Neovim - gérer ses configurations avec Git

L'objectif de ce TP est d'utiliser Git pour gérer les fichiers de configuration d'un programme (ici `Neovim`).

- [html](/cours/git/git-tp-iac-nvim.html)
- [pdf](/cours/git/git-tp-iac-nvim.pdf)
- [markdown](/cours/git/git-tp-iac-nvim.md)

### 💻 TP - Manipulations avancées de la HEAD

Dans ce TP, nous allons voir des commandes avancées pour déplacer le pointeur vers le commit courant (`HEAD`) de Git.

- [html](/cours/git/git-tp-deplacer-head-avance.html)
- [pdf](/cours/git/git-tp-deplacer-head-avance.pdf)
- [markdown](/cours/git/git-tp-deplacer-head-avance.md)
