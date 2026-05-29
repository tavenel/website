---
title: 🐧 Linux
layout: '@layouts/BaseLayout.astro'
---

# 🐧 Linux

## Conventions de notation

- Les commandes et noms de fichiers apparaissent dans le texte avec `cette syntaxe`.
- Les descriptions de commandes suivent le formalisme des _man pages_ :
  - Les symboles `<>` indiquent un argument obligatoire.
  - Les symboles `[]` indiquent un argument optionnel.  
  - Le symbole `|` indique un choix (exclusif) entre 2 arguments.
  - Le symbole `…` indique un argument pouvant être répété.

## Rappels

### Architecture d'un système Linux

- Kernel, Shell, FHS
- Services système (systemd)
- Structure des répertoires : `/etc`, `/var`, `/usr`, `/home`, `/opt`

### Commandes essentielles

- Navigation : `ls`, `cd`, `pwd`
- Fichiers : `cp`, `mv`, `rm`, `cat`, `nano`, `vim`
- Droits : `chmod`, `chown`, `umask`
- Processus : `ps`, `htop`
- Services : `systemctl`, `journalctl`

### Comptes utilisateurs sous Linux

- Commandes : `useradd`, `passwd`, `usermod`, `groupadd`
- Fichiers : `/etc/passwd`, `/etc/shadow`, `/etc/group`
- Gestion des sudoers

## Installation

- [󰣛 Machine virtuelle Fedora Desktop dans VirtualBox](/linux/tp-installation-vbox-fedora-workstation)
- [󰕈 Machine virtuelle Ubuntu Desktop dans VirtualBox](/linux/tp-installation-vbox-ubuntu-workstation)
- [󰣚  Machine virtuelle Debian serveur dans VirtualBox](/linux/tp-installation-vbox-debian-server)
- [Installer un serveur Ubuntu sous Virtualbox](https://www.eugenetoons.fr/installer-un-serveur-ubuntu-sous-virtualbox/)

- [✨ Configuration d'un poste de travail Linux](/linux/tp-env-dev) : Installation de programmes libres alternatifs pour améliorer l'ergonomie de sa station de travail.

## Découverte de Linux

- [🤓 Cours découverte de Linux](/linux/cours-1)
- [  TP - Utilisation des commandes Linux](/linux/tp-commandes_linux)
- [  TP - Utilisation des commandes avancées](/linux/tp-commandes_avancees)
- [📜 TP - Création de scripts Bash](/linux/tp-scripts_bash)
- [📜 TP Bash - Gestion des fichiers et des utilisateurs](/linux/tp-script) : apprendre à manipuler des fichiers et des répertoires avec Bash, utiliser des boucles et des conditions, créer des scripts interactifs, gérer les utilisateurs et permissions basiques.
- [🚮 TP - Commande trash simulant l'utilisation d'une poubelle](/linux/tp-trash)
- [🔦 Installation d'un serveur LAMP (Linux Apache MySQL PHP) permettant d'héberger un site Web](/linux/projet_lamp)

## Niveau 2

- [🤓 Cours Linux intégral](/linux/cours)
- [🤓 Cours complet sur le shell Bash : fonctions, boucles, tests, …](/linux/cours-shell)
- [⌨️ TP : affichage de la configuration du système et des périphériques, gestion des modules noyau](/linux/tp-systeme)
- [📀 TP : utiliser GRUB pour une restauration système](/linux/tp-grub)
- [📀 TP : utiliser un Live CD/USB pour une restauration système](/linux/tp-rescue)
- [▶️ TP : SysV init](/linux/tp-sysv) : administrer les services et changer de runlevel dans un système SysV.
- [▶️ TP : Systemd init](/linux/tp-systemd) : administrer les services et changer de runlevel dans un système systemd.
- [🗃️ TP : librairies partagées](/linux/tp-shared-lib)
- [📦 TP : Gestion de paquetages](/linux/tp-rpm-apt) : gérer (installer, mettre à jour, désinstaller) des programmes depuis des packets RedHat via rpm, yum et dnf et des packets Debian via dpkg et apt.
- [  TP : Utilisation efficace de la ligne de commande](/linux/tp-ligne-commande)
- [📃 TP : Traitement de flux de type texte](/linux/tp-texte)
- [📂 TP : Gestion basique des fichiers - déplacement, copie, liste et types de fichiers](/linux/tp-fichiers)
- [↔️ TP : Utilisation des flux, des pipes et des redirections](/linux/tp-redirections)
- [⚙️ TP : Gestion des processus et de leurs priorités](/linux/tp-process)
- [💽 TP : Gestion des partitions et des systèmes de fichiers](/linux/tp-partitions)
- [💽 TP : Utiliser LVM pour créer, gérer et étendre des volumes logiques](/linux/tp-lvm)
- [💽 TP : Mise en place d'un partage NFS (Network File System) sous Debian](/linux/tp-nfs)
- [💽 TP : Utiliser iSCSI pour gérer des disques réseau](/linux/tp-iscsi)
- [💽 TP : Utiliser ZFS pour gérer des volumes logiques et des partitions](/linux/tp-zfs)
- [📁 TP : Gestion avancée des fichiers - permissions, liens, recherche](/linux/tp-fichiers-avance)
- [🔐 TP : Gestion des permissions avancées avec SUID, SGID et ACL](/linux/tp-droits-avance)
- [👥 TP : Gestion des utilisateurs et de la sécurité](/linux/tp-utilisateurs)
- [🕗 TP : Planification de tâches avec `at`, `cron` et `systemd`](/linux/tp-cron)
- [📨 TP : Langue et encodage](/linux/tp-lang) : gérer l'utilisation d'encodages différents (`ASCII`, `UTF-8`, …), de formats de fichiers différents (`Unix`/Linux vs `Dos`/Windows) et de langues différentes par l'utilisation de _locales_.
- [📜 TP : Journalisation avec Syslog](/linux/tp-syslog) : gérer les journaux (logs) système et utilisateur, en local ou vers un serveur centralisé, notamment par le biais de `syslog` et ses différentes implémentations : `syslog`, `rsyslog` et `syslog-ng`.
- [📡 TP : Configuration réseau](/linux/tp-network) : gérer la configuration réseau d'un système Linux en utilisant les outils historiques `net-tools`, les outils modernes `iproute2`, ou les implémentations `systemd`. L'utilisation de `Network Manager` est aussi abordée.
- [🔒 TP : Notions de sécurité : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …](/linux/tp-security)
- [🔐 TP : Sécurité des échanges avec SSH et GPG](/linux/tp-ssh-gpg)
- [🌐 TP : Installation d'un service VPN](/linux/tp-vpn)
- [💾 TP Sauvegarde et Restauration sous Linux](/linux/tp-backup)
- [🛠️ TP : Administration d'un système Linux](/linux/tp-admin-technova) : Cas fictif pour mettre en pratique les commandes shell sous Linux, en se concentrant sur la gestion des droits des utilisateurs et des groupes et la configuration de l'élévation de privilèges.
- [🔐 TP : Mise en place de règles de filtrage sous Debian avec Netfilter iptables](/linux/projet-netfilter-iptables) : Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu.
- [🔐 TP : Mise en place de règles de filtrage sous Debian avec Netfilter nftables](/linux/projet-netfilter-nftables) : Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu.
- [📦 TP : Compilation, personnalisation et installation d'un noyau Linux](/linux/tp-build-kernel) : Votre mission est de compiler et installer un noyau Linux personnalisé ainsi que de rebuilder automatiquement un module externe avec DKMS.
- [🔐 TP : Investigation post-compromission sous Linux : détection et analyse](/linux/tp-forensics) : Identifier les traces d'une compromission (analyse de logs, rootkits, persistence) et utiliser des outils d'investigation (chkrootkit, rkhunter, auditd, osquery).
- [🔐 Projet : Infrastructure Linux sécurisée pour un centre de données confidentiel](/linux/projet-cyber) : L'objectif est de concevoir, déployer et sécuriser une infrastructure Linux complète répondant à des exigences fortes de disponibilité, confidentialité et intégrité des données.

## 🔗 LPIC-1

Voir le [cours dédié](/esgi/b3/lpic-1)

## 🔗 LPIC-2

Voir le [cours dédié](/esgi/m1/lpic-2)

## 🤯 Concepts avancés

- [📦 TP : Découverte des Cgroups](/linux/tp-cgroup) : une introduction aux cgroups, permettant de limiter les ressources utilisées par des processus.
- [💾 TP Clusters de haute disponibilité (HA) et Corosync](/linux/tp-ha)
- [🤯 Création de conteneur en utilisant les namespace natifs Linux](/docker/container-from-namespace) : cet exercice montre comment créer des conteneurs sans Docker en utilisant directement les fonctionnalités des namespace du noyau Linux.

## Ressources

### Exercices, Gamification, Challenges

- [Une VM Linux dans le navigateur](https://webvm.io/)
- Un jeu de piste Linux utilisant le terminal : <https://github.com/phyver/GameShell>
- Un jeu de piste à réaliser sur sa machine virtuelle en utilisant les commandes Linux: <https://github.com/veltman/clmystery>
- Un "wargame" (orienté cyber-sécurité) en ligne permettant d'apprendre Linux par le jeu : <https://overthewire.org/wargames/bandit/>
- VMs d'entraînement avec des problèmes à résoudre: <https://sadservers.com/>
- Formations et challenges : <https://labs.iximiuz.com/>

### Liens

- [Livre Bash beginner's guide](https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/)
- <https://github.com/bobbyiliev/introduction-to-bash-scripting> : livre gratuit
- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- <https://roadmap.sh/linux>
- Formation détaillée sur les bases de Linux : <https://formations.microlinux.fr/linux-rhel9/a-propos/>
  - Du même auteur, histoire d'Unix, Linux et de l'Open-Source : <https://formations.microlinux.fr/introduction/a-propos/>
- [Une formation gratuite de la Linux Foundation (LFS101)](https://training.linuxfoundation.org/training/introduction-to-linux/)
- [Vidéo : 100+ Linux things in 10 mins](https://youtube.com/watch?v=LKCVKw9CzFo)
- [Structure du système de fichiers](https://www.zdnet.fr/pratique/linux-la-structure-du-systeme-de-fichiers-expliquee-397880.htm)
- [Commandes Linux](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes/) et [Commandes avancées](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes-avancees/)
- [Scripts Shell](https://linux.goffinet.org/administration/scripts-shell/) et [TP pas à pas](https://systemes.gricad-pages.univ-grenoble-alpes.fr/www-unix/avance/seance1-2-script-sh-pas-a-pas/tp-pas-a-pas.pdf)
- [Variables d'environnement : TP pas à pas](https://systemes.gricad-pages.univ-grenoble-alpes.fr/www-unix/avance/seance4-varenv-pas-a-pas/tp-pas-a-pas-varenv.pdf)
- [Mind map SSH](https://www.formation-lpi.com/Mind-Map-SSH.html) et [Mind map GPG](https://www.formation-lpi.com/Mind-Map-gpg.html)
- [Migrer une installation Linux](https://www.antoinefi.net/index.php/2025/01/29/migrer-une-installation-linux/)
- Livre : Unix and Linux system administration handbook, 5th edition. Evi Nemeth, Garth Snyder, Trent R.Hein, Ben Whaley, Dan Mackin
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)
- [20 years of Linux on the Desktop](https://ploum.net/2024-10-20-20years-linux-desktop-part1.html)
- [Montez un serveur de fichiers sous Linux (OpenClassRoom)](https://openclassrooms.com/fr/courses/2356316-montez-un-serveur-linux-et-ses-services)
- [Gérez votre serveur Linux et ses services (OpenClassRoom)](https://openclassrooms.com/fr/courses/1733551-gerez-votre-serveur-linux-et-ses-services)

### Liens VIM

- Un jeu graphique en ligne pour découvrir VIM (3 premiers niveaux gratuits) : <https://vim-adventures.com>
- <https://thevaluable.dev/vim-commands-beginner/>
- <https://thevaluable.dev/vim-intermediate/>
- <https://thevaluable.dev/vim-advanced/>
- <https://thevaluable.dev/vim-adept/>
- <https://thevaluable.dev/vim-veteran/>
- <https://thevaluable.dev/vim-expert/>

## 🚀 Autres ressources

- Voir la page sur [⚒️ les outils](/tools)
