---
pagetitle:   Tom Avenel - Versioning Git administrateur
updated: 2024-10-02
---

#  Versioning Git pour l'administrateur

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

### 🤓 Cours

- [html](/cours/git/git-cours.html)
- [pdf](/cours/git/git-cours.pdf)
- [markdown](/cours/git/git-cours.md)

### 💻 TP - Premiers pas

L'objectif de ce TP est d'installer et de configurer git, puis de se familiariser avec ses concepts de base.

- [html](/cours/git/git-tp-commit.html)
- [pdf](/cours/git/git-tp-commit.pdf)
- [markdown](/cours/git/git-tp-commit.md)

### 💻 TP - Le gitignore

L'objectif de ce TP est d'utiliser le fichier spécial `.gitignore` pour masquer des fichiers à Git.

- [html](/cours/git/git-tp-gitignore.html)
- [pdf](/cours/git/git-tp-gitignore.pdf)
- [markdown](/cours/git/git-tp-gitignore.md)

### 💻 TP - Utiliser l'historique de Git™

L'objectif de ce TP est d'utiliser les fonctions d'historique de git.

- [html](/cours/git/git-tp-historique.html)
- [pdf](/cours/git/git-tp-historique.pdf)
- [markdown](/cours/git/git-tp-historique.md)

### 💻 TP - Git™ Bisect

 L'objectif de ce TP est d'utiliser la commande Git Bisect pour trouver un commit par dichotomie.

- [html](/cours/git/git-tp-bisect.html)
- [pdf](/cours/git/git-tp-bisect.pdf)
- [markdown](/cours/git/git-tp-bisect.md)

### 💻 TP - Github® et dépôts distants

 L'objectif de ce TP est de créer, configurer et utiliser un dépôt git distant sur la plateforme Github®.

- [html](/cours/git/git-tp-github.html)
- [pdf](/cours/git/git-tp-github.pdf)
- [markdown](/cours/git/git-tp-github.md)

### 💻 TP Github - Utiliser les Gist

Petit TP dont l'objectif est de découvrir les Gist de GitHub.

- [html](/cours/git/git-tp-github-gist.html)
- [pdf](/cours/git/git-tp-github-gist.pdf)
- [markdown](/cours/git/git-tp-github-gist.md)

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

### 💻 TP Github - Les actions (introduction à la CI)

Les _Actions_ GitHub permettent très facilement une initiation à un worflow d'intégration continue très limité.

- [html](/cours/git/git-tp-github-actions.html)
- [pdf](/cours/git/git-tp-github-actions.pdf)
- [markdown](/cours/git/git-tp-github-actions.md)

### 💻 TP Neovim - gérer ses configurations avec Git

L'objectif de ce TP est d'utiliser Git pour gérer les fichiers de configuration d'un programme (ici `Neovim`).

- [html](/cours/git/git-tp-iac-nvim.html)
- [pdf](/cours/git/git-tp-iac-nvim.pdf)
- [markdown](/cours/git/git-tp-iac-nvim.md)

### 💻 TP utiliser Ansible avec Git

L'objectif de ce TP est d'utiliser Ansible et Git pour réaliser de l'Infrastructure-as-Code.

- [html](/cours/git/git-tp-ansible.html)
- [pdf](/cours/git/git-tp-ansible.pdf)
- [markdown](/cours/git/git-tp-ansible.md)

### 💻 TP - Intégrer Git dans un IDE

L'objectif de ce TP est d'utiliser Git directement dans l'IDE et d'y afficher les derniers changements dans le code.

- [html](/cours/git/git-tp-ide.html)
- [pdf](/cours/git/git-tp-ide.pdf)
- [markdown](/cours/git/git-tp-ide.md)

### 💻 TP - Manipulations avancées de la HEAD

Dans ce TP, nous allons voir des commandes avancées pour déplacer le pointeur vers le commit courant (`HEAD`) de Git.

- [html](/cours/git/git-tp-deplacer-head-avance.html)
- [pdf](/cours/git/git-tp-deplacer-head-avance.pdf)
- [markdown](/cours/git/git-tp-deplacer-head-avance.md)

