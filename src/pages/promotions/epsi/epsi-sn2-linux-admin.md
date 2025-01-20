---
pagetitle: 🐧 Tom Avenel - SN2 Linux Admin
---

# 🐧 Adminisitration Linux (Shell)

_Modifié le: 2024-10-23_

![](/resources/images/cover/linux-admin.jpg)

## Présentation du module

### 🎯 Objectifs

- Mise en place de la gestion des accès aux fichiers avec ACL
- Utilisation des expressions régulières
- Développement de scripts bash

### Contenu du cours

- Les droits
  - Rappels sur les droits classiques 
  - Les droits spéciaux : suid, sgid, sticky bit
  - Les ACL
  - Gestion du masque
- Expressions Régulières
  - Filtres 
  - Les Glob 
  - Les regex
- Bash avancé
  - Vim 
  - Script bash
    - exécution, jobs, shebang, source, variables, arguments
    - tests et conditions
    - boucles
    - fonctions
    - tableaux
- Administration réseau
  - Netfilter
  - Netstat
  - Netcat
  - Nmap
  - Tcpdump

### 📅 Déroulé du cours

- Module de 10H
- Évaluation : TP noté

## 💻 Environnement de travail : Machine virtuelle Ubuntu

Installation d'une machine virtuelle Ubuntu de type Desktop dans VirtualBox.

- [html](/cours/linux/installation/tp-installation-vbox-ubuntu-workstation.html)
- [pdf](/cours/linux/installation/tp-installation-vbox-ubuntu-workstation.pdf)
- [markdown](/cours/linux/installation/tp-installation-vbox-ubuntu-workstation.md)

## Documents

### Partie 1 : Les droits

#### 🤓 Cours Linux sur les permissions et les droits

- [html](/cours/linux/niveau2/cours-linux-droits.html)
- [pdf](/cours/linux/niveau2/cours-linux-droits.pdf)
- [markdown](/cours/linux/niveau2/cours-linux-droits.md)

#### 📁 TP : Gestion avancée de fichiers - permissions, liens, recherche

L'objectif de ce TP est la gestion avancée de fichiers - gestion des permissions, liens standards et symboliques, recherche de chemins de fichiers et de contenus.

- [html](/cours/linux/niveau2/tp-fichiers-avance.html)
- [pdf](/cours/linux/niveau2/tp-fichiers-avance.pdf)
- [markdown](/cours/linux/niveau2/tp-fichiers-avance.md)

#### 🔐 TP : Gestion des permissions avancées avec SUID, SGID et ACL

Ce TP a pour objectif d'apprendre l'utilisation des permissions avancées sous Linux, à savoir le SUID, le SGID et les listes de contrôle d'accès (ACL).

- [html](/cours/linux/niveau2/tp-droits-avance.html)
- [pdf](/cours/linux/niveau2/tp-droits-avance.pdf)
- [markdown](/cours/linux/niveau2/tp-droits-avance.md)

### Partie 2 - Regexp 

#### 📃 TP : Traitement de flux de type texte

Dans un système Linux, l'échange d'information passe principalement par des fichiers texte - il existe donc de très nombreuses commandes optimisées à cette fin avec lesquelles il faut être à l'aise. Il y aura également souvent plusieurs possiblités pour arriver au même résultat.

- [html](/cours/linux/niveau2/tp-texte.html)
- [pdf](/cours/linux/niveau2/tp-texte.pdf)
- [markdown](/cours/linux/niveau2/tp-texte.md)

### Partie 3 - Vim

#### ✍️ TP : Introduction à vi

Exécuter la commande `vimtutor`.

#### Liens VIM

- <https://vim-adventures.com>
- <https://thevaluable.dev/vim-commands-beginner/>
- <https://thevaluable.dev/vim-intermediate/>
- <https://thevaluable.dev/vim-advanced/>
- <https://thevaluable.dev/vim-adept/>
- <https://thevaluable.dev/vim-veteran/>
- <https://thevaluable.dev/vim-expert/>

### Partie 4 - Script Bash

#### 🤓 TP : Le shell

L'objectif de ce TP est de se familiariser avec l'utilisation du shell Bash : fonctions, boucles, tests, …

- [html](/cours/linux/niveau2/cours-shell.html)
- [pdf](/cours/linux/niveau2/cours-shell.pdf)
- [markdown](/cours/linux/niveau2/cours-shell.md)

#### 📜 TP Bash - Gestion des fichiers et des utilisateurs

Dans ce TP, nous allons :

- Apprendre à manipuler des fichiers et des répertoires avec Bash.
- Utiliser des boucles et des conditions.
- Créer des scripts interactifs.
- Gérer les utilisateurs et permissions basiques dans un environnement Linux.

- [html](/cours/linux/niveau2/tp-script.html)
- [pdf](/cours/linux/niveau2/tp-script.pdf)
- [markdown](/cours/linux/niveau2/tp-script.md)

### Partie 5 - Administration réseau

#### 🤓 Cours Linux d'introduction à l'administration réseau

- [html](/cours/linux/niveau2/cours-linux-network.html)
- [pdf](/cours/linux/niveau2/cours-linux-network.pdf)
- [markdown](/cours/linux/niveau2/cours-linux-network.md)

#### 🔐 TP : Notions de sécurité d'un système Linux

L'objectif de ce TP est d'aborder des notions de sécurité sur un système Linux : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …

- [html](/cours/linux/niveau2/tp-security.html)
- [pdf](/cours/linux/niveau2/tp-security.pdf)
- [markdown](/cours/linux/niveau2/tp-security.md)

### 📌 Projet : Mise en place de règles de filtrage sous Debian avec Netfilter

Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu.

- [html](/cours/linux/projet-netfilter.html)
- [pdf](/cours/linux/projet-netfilter.pdf)
- [markdown](/cours/linux/projet-netfilter.md)

