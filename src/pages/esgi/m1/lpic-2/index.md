---
title: 🐧 LPIC-2
layout: '@layouts/BaseLayout.astro'
---

# 🐧 Linux LPIC-2

_Préparation à la certification LPIC-2 v4.5_

## Présentation de la certification

- 2 examens : LPIC-201 **puis** LPIC-202 pour obtenir le LPIC-2
- 1H30
- 60 questions découpées proportionnellement au poids des chapitres : 8 pour chapitre 1, ... (voir plan)
- Score > 500/800 pour passer (12.5/20)

:::link
Plus d'informations : <https://www.lpi.org/our-certifications/lpic-2-overview/>
:::

La certification LPIC est conséquente et les questions très précises, il faut donc :

- bien apprendre **par coeur les commandes et les options à utiliser**
- **apprendre et pratiquer le vocabulaire**
- **s'entraîner régulièrement**

### 🎯 Objectif global

Pour obtenir la certification LPIC-2, un candidat doit être en mesure :

- d'administrer un site de petite ou de moyenne taille.
- d'élaborer, de mettre en œuvre, d'entretenir, de conserver dans un état cohérent et de sécuriser, ainsi que de résoudre les problèmes dans un petit réseau hétérogène (Linux, MS) avec :
  - serveurs LAN (Samba, NFS, DNS, DHCP, gestion des clients).
  - passerelle Internet (pare-feu, VPN, SSH, serveur mandataire (proxy) / cache web, messagerie).
  - serveur Internet (serveur web, proxy inverse reverse, serveur FTP.
- d'encadrer des techniciens.
- de conseiller la direction sur les achats et l'automatisation.

Source : <https://wiki.lpi.org/wiki/LPIC-2_Objectives_V4.5(FR)>

### Quelle distribution ?

- LPIC vise des concepts généraux, pas vraiment de distribution de choix...
- ...mais vise principalement les dérivés Debian (Ubuntu, ...) et RedHat (RHEL, CentOS, ...)
- Installer par exemple les deux environnements suivants :
  - [󰣛 Machine virtuelle Fedora Desktop dans VirtualBox](/linux/tp-installation-vbox-fedora-workstation)
  - [󰕈 Machine virtuelle Ubuntu Desktop dans VirtualBox](/linux/tp-installation-vbox-ubuntu-workstation)

### Niveau requis

- La certification LPIC-1 doit être maîtrisée : [Cours LPIC-1](/esgi/b3/lpic-1)

### 🎯 Exam 201-450 : Administration système avancée

- Sujet 200 : **Planification des ressources**
  - 200.1 Mesure de l'utilisation des ressources et résolution de problèmes (valeur : 6)
  - 200.2 Prévision des besoins en ressources (valeur : 2)
- Sujet 201 : **le noyau Linux**
  - 201.1 Composants du noyau (valeur : 2)
  - 201.2 Compilation du noyau (valeur : 3)
    - [📦 TP : Compilation, Personnalisation et Installation d'un Noyau Linux](/linux/tp-build-kernel)
  - 201.3 Gestion du noyau à chaud et résolution de problèmes (valeur : 4)
    - [⌨️ TP de rappel : affichage de la configuration du système et des périphériques, gestion des modules noyau](/linux/tp-systeme)
- Sujet 202 : **Démarrage du système**
  - 202.1 Personnalisation du démarrage système (valeur :3)
    - [▶️ TP de rappel : SysV init](/linux/tp-sysv) : administrer les services et changer de runlevel dans un système SysV.
    - [▶️ TP de rappel : Systemd init](/linux/tp-systemd) : administrer les services et changer de runlevel dans un système systemd.
  - 202.2 Récupération du système (valeur : 4)
    - [📀 TP de rappel : utiliser GRUB pour une restauration système](/linux/tp-grub)
    - [📀 TP de rappel : utiliser un Live CD/USB pour une restauration système](/linux/tp-rescue)
  - 202.3 Chargeurs d'amorçage alternatifs (valeur : 2)
- Sujet 203 : **Systèmes de fichiers et périphériques**
  - 203.1 Intervention sur le système de fichiers Linux (valeur : 4)
  - 203.2 Maintenance des systèmes de fichiers Linux (valeur : 3)
    - [💽 TP : Gestion des partitions et des systèmes de fichiers](/linux/tp-partitions)
  - 203.3 Options de création et de configuration des systèmes de fichiers (valeur : 2)
- Sujet 204 : **Administration avancée des périphériques de stockage**
  - 204.1 Configuration du RAID logiciel (valeur : 3)
  - 204.2 Ajustement des accès aux périphériques de stockage (valeur : 2)
  - 204.3 Gestionnaire de volumes logiques (valeur : 3)
    - [💽 TP : Utiliser LVM pour créer, gérer et étendre des volumes logiques](/linux/tp-lvm)
- Sujet 205 : **Configuration réseau**
  - 205.1 Configuration réseau de base (valeur : 3)
  - 205.2 Configuration réseau avancée (valeur : 4)
  - 205.3 Résolution des problèmes réseau (valeur : 4)
    - [📡 TP : Configuration réseau](/linux/tp-network) : gérer la configuration réseau d'un système Linux en utilisant les outils historiques `net-tools`, les outils modernes `iproute2`, ou les implémentations `systemd`. L'utilisation de `Network Manager` est aussi abordée.
- Sujet 206 : **Maintenance système**
  - 206.1 Compilation et installation de programmes à partir des sources (valeur : 2)
  - 206.2 Opérations de sauvegarde (valeur : 3)
    - [💾 TP Sauvegarde et Restauration sous Linux](/linux/tp-backup)
  - 206.3 Information des utilisateurs (valeur : 1)

### 🎯 Exam 202-450 : Réseau et Services

- Sujet 207 : **Serveur de nom de domaine**
  - 207.1 Configuration de base d'un serveur DNS (valeur : 3)
  - 207.2 Création et mise à jour des zones DNS (valeur : 3)
  - 207.3 Sécurisation d'un serveur DNS (valeur : 2)
- Sujet 208: **HTTP Services**
  - 208.1 Configuration élémentaire d'Apache (valeur : 4)
  - 208.2 Configuration d'Apache pour HTTPS (valeur : 3)
  - 208.3 Mise en place du serveur mandataire squid (valeur : 2)
  - 208.4 Mise en place de Nginx en tant que serveur Web et proxy inverse (valeur : 2)
- Sujet 209 : **Partage de fichiers**
  - 209.1 Configuration d'un serveur SAMBA (valeur : 5)
  - 209.2 Configuration d'un serveur NFS (valeur : 3)
- Sujet 210 : **Gestion des clients réseau**
  - 210.1 Configuration DHCP (valeur : 2)
  - 210.2 Authentification PAM (valeur : 3)
  - 210.3 Clients LDAP (valeur : 2)
  - 210.4 Configuration d'un serveur OpenLDAP (valeur : 4)
- Sujet 211 : **Services de courrier électronique**
  - 211.1 Utilisation des serveurs de messagerie (valeur : 4)
  - 211.2 Gestion de la distribution des courriels (valeur : 2)
  - 211.3 Gestion des accès aux boîtes aux lettres (valeur: 2)
- Sujet 212 : **Sécurité du système**
  - 212.1 Configuration d'un routeur (valeur : 3)
    - [🔐 TP : Mise en place de règles de filtrage sous Debian avec Netfilter](/linux/projet-netfilter) : Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu.
  - 212.2 Gestion des serveurs FTP (valeur : 2)
  - 212.3 Shell sécurisé (SSH) (valeur : 4)
    - [🔐 TP : Sécurité des échanges avec SSH et GPG](/linux/tp-ssh-gpg)
  - 212.4 Tâches de sécurité (valeur : 3)
    - [💻 TP : Utilisation du protocole HTTP avec Telnet](/web/exo-telnet_http)
    - [🔒 TP Optionnel : Notions de sécurité : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …](/linux/tp-security)
  - 212.5 OpenVPN (valeur : 2)
    - [🌐 TP : Installation d'un service VPN](/linux/tp-vpn)

### 📝 Ressources utiles

- Livre de la formation LPIC-2 : <https://lpic2book.github.io/src>
- Examens blancs :
  - <https://www.penguintutor.com/quiz/index.php>
  - <https://www.examtopics.com/exams/lpi/201-450/>
  - <https://www.examtopics.com/exams/lpi/202-450/>
  - <https://www.itexams.com/vendor/LPI>
  - <https://www.certlibrary.com/vendor/LPI>

#### 🔗 Autres liens utiles

- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)
- [Présentation et comparaison des certifications Linux](https://blog.stephane-robert.info/docs/admin-serveurs/linux/certifications/)

## 📅 Déroulé du cours

- 3 Modules de 12H
- Évaluation : QCM et Projets

## 📑 Documents

- [📝 Syllabus du contenu de la certification LPIC-2](/linux/lpic-2/contenu)
<!-- - [🤓 Cours Linux pour la certification LPIC-2](/linux/lpic-2/cours) -->
<!-- - [🏆 Projet LPIC-2 : Mise en place d'une infrastructure système complète sécurisée et supervisée](/linux/lpic-2/projet) -->

## 🚀 Pour aller plus loin

- Voir les autres ressources du [cours sur Linux](/linux).
