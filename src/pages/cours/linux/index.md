---
title: 🐧 Linux
---

## Conventions de notation

- Les commandes et noms de fichiers apparaissent dans le texte avec `cette syntaxe`.
- Les descriptions de commandes suivent le formalisme des _man pages_ :
  - Les symboles `<>` indiquent un argument obligatoire.
  - Les symboles `[]` indiquent un argument optionnel.  
  - Le symbole `|` indique un choix (exclusif) entre 2 arguments.
  - Le symbole `…` indique un argument pouvant être répété.

## Installation

- [󰣛 Machine virtuelle Fedora Desktop dans VirtualBox](/cours/linux/installation/tp-installation-vbox-fedora-workstation)
- [󰕈 Machine virtuelle Ubuntu Desktop dans VirtualBox](/cours/linux/installation/tp-installation-vbox-ubuntu-workstation)
- [󰣚  Machine virtuelle Debian serveur dans VirtualBox](/cours/linux/installation/tp-installation-vbox-debian-server)

- [✨ Configuration d'un poste de travail Linux](/cours/linux/installation/tp-env-dev) : Installation de programmes libres alternatifs pour améliorer l'ergonomie de sa station de travail.

## Découverte de Linux

- [🤓 Cours découverte de Linux](/cours/linux/niveau1/linux-cours-niveau1)
- [  TP - Utilisation des commandes Linux](/cours/linux/niveau1/tp-commandes_linux)
- [  TP - Utilisation des commandes avancées](/cours/linux/niveau1/tp-commandes_avancees)
- [📜 TP - Création de scripts Bash](/cours/linux/niveau1/tp-scripts_bash)
- [📜 TP Bash - Gestion des fichiers et des utilisateurs](/cours/linux/niveau2/tp-script) : apprendre à manipuler des fichiers et des répertoires avec Bash, utiliser des boucles et des conditions, créer des scripts interactifs, gérer les utilisateurs et permissions basiques.
- [🚮 TP - Commande trash simulant l'utilisation d'une poubelle](/cours/linux/niveau1/tp-trash)
- [🔦 Installation d'un serveur LAMP (Linux Apache MySQL PHP) permettant d’héberger un site Web](/cours/linux/niveau1/projet_lamp)

## Niveau 2

- [🤓 Cours Linux sur l'architecture matérielle et la gestion des périphériques](/cours/linux/niveau2/cours-linux-hardware)
- [🤓 Slides de cours sur l'installation de Linux et la gestion de paquetages](/cours/linux/niveau2/cours-linux-install)
- [🤓 Slides de cours sur les commandes GNU/Linux et Unix](/cours/linux/niveau2/cours-linux-commandes)
- [🤓 Slides de cours sur les disques et les partitions](/cours/linux/niveau2/cours-linux-disks)
- [🤓 Slides de cours Linux sur les permissions et les droits](/cours/linux/niveau2/cours-linux-droits)
- [🤓 Slides de cours Linux sur les liens](/cours/linux/niveau2/cours-linux-liens)
- [🤓 Slides de cours Linux sur la recherche de fichiers](/cours/linux/niveau2/cours-linux-find)
- [🤓 Slides de cours sur le Shell](/cours/linux/niveau2/cours-linux-shell)
- [🤓 Slides de cours sur les interfaces et bureaux utilisateur](/cours/linux/niveau2/cours-linux-desktop)
- [🤓 Slides de cours Linux sur l'administration système](/cours/linux/niveau2/cours-linux-admin)
- [🤓 Slides de cours Linux d'introduction à l'administration réseau](/cours/linux/niveau2/cours-linux-network)
- [🤓 Slides de cours Linux sur la sécurité](/cours/linux/niveau2/cours-linux-security)
- [🤓 Cours complet sur le shell Bash : fonctions, boucles, tests, …](/cours/linux/niveau2/cours-shell)
- [⌨️ TP : affichage de la configuration du système et des périphériques, gestion des modules noyau](/cours/linux/niveau2/tp-systeme)
- [📀 TP : utiliser GRUB pour une restauration système](/cours/linux/niveau2/tp-grub)
- [▶️ TP : SysV init et systemd init](/cours/linux/niveau2/tp-sysv-systemd) : administrer les services et changer de runlevel dans un système SysV ou systemd.
- [🗃️ TP : librairies partagées](/cours/linux/niveau2/tp-shared-lib)
- [📦 TP : Gestion de paquetages](/cours/linux/niveau2/tp-rpm-apt) : gérer (installer, mettre à jour, désinstaller) des programmes depuis des packets RedHat via rpm, yum et dnf et des packets Debian via dpkg et apt.
- [  TP : Utilisation efficace de la ligne de commande](/cours/linux/niveau2/tp-ligne-commande)
- [📃 TP : Traitement de flux de type texte](/cours/linux/niveau2/tp-texte)
- [📂 TP : Gestion basique des fichiers - déplacement, copie, liste, types de fichiers](/cours/linux/niveau2/tp-fichiers)
- [↔️ TP : Utilisation des flux, des pipes et des redirections ](/cours/linux/niveau2/tp-redirections)
- [⚙️ TP : Gestion des processus et de leur priorité](/cours/linux/niveau2/tp-process)
- [💽 TP : Gestion des partitions et des systèmes de fichiers](/cours/linux/niveau2/tp-partitions)
- [💽 TP : Utiliser LVM pour créer, gérer et étendre des volumes logiques](/cours/linux/niveau2/tp-lvm)
- [📁 TP : Gestion avancée de fichiers - permissions, liens, recherche](/cours/linux/niveau2/tp-fichiers-avance)
- [🔐 TP : Gestion des permissions avancées avec SUID, SGID et ACL](/cours/linux/niveau2/tp-droits-avance)
- [👥 TP : Gestion des utilisateurs et de la sécurité](/cours/linux/niveau2/tp-utilisateurs)
- [🕗 TP : Planification de tâches avec `at`, `cron` et `systemd`](/cours/linux/niveau2/tp-cron)
- [📨 TP : Langue et encodage](/cours/linux/niveau2/tp-lang) : gérer l'utilisation d'encodages différents (`ASCII`, `UTF-8`, …), de formats de fichiers différents (`Unix`/Linux vs `Dos`/Windows) et de langues différentes par l'utilisation de _locales_.
- [📜 TP : Journalisation avec Syslog](/cours/linux/niveau2/tp-syslog) : gérer les journaux (logs) système et utilisateur, en local ou vers un serveur centralisé, notamment par le biais de `syslog` et ses différentes implémentations : `syslog`, `rsyslog` et `syslog-ng` (l'accent est mis sur `rsyslog`). Les liens entre `syslog` et `systemd-journald` sont également abordés.
- [📡 TP : Configuration réseau](/cours/linux/niveau2/tp-network) : gérer la configuration réseau d'un système Linux en utilisant les outils historiques `net-tools`, les outils modernes `iproute2`, ou les implémentations `systemd`. L'utilisation de `Network Manager` est aussi abordée.
- [🔐 TP : Notions de sécurité : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …](/cours/linux/niveau2/tp-security)
- [🔐 TP : Sécurité des échanges avec SSH et GPG](/cours/linux/niveau2/tp-ssh-gpg)
- [🔐 TP : Administration d'un système Linux](/cours/linux/tp-admin-technova) : Cas fictif pour mettre en pratique les commandes shell sous Linux, en se concentrant sur la gestion des droits des utilisateurs et des groupes et la configuration de l'élévation de privilèges.
- [🔐 TP : Mise en place de règles de filtrage sous Debian avec Netfilter](/cours/linux/projet-netfilter) : Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu.

## 🔗 LPIC-1

Voir le [cours dédié](/promotions/esgi/esgi-b3-src-linux-lpic-1)

## Liens

- [Livre Bash beginner's guide](https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/)
- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- <https://roadmap.sh/linux>
- [Une VM Linux dans le navigateur](https://webvm.io/)
- [Une formation gratuite de la Linux Foundation (LFS101)](https://training.linuxfoundation.org/training/introduction-to-linux/)
- [Un "wargame" (orienté cyber-sécurité) en ligne permettant d'apprendre Linux par le jeu](https://overthewire.org/wargames/bandit/)
- [Un jeu de piste à réaliser sur sa machine virtuelle en utilisant les commandes Linux](https://github.com/veltman/clmystery)
- [Un autre jeu de piste](https://github.com/phyver/GameShell)
- [VMs d'entraînement avec des problèmes à résoudre](https://sadservers.com/)
- [Vidéo : 100+ Linux things in 10 mins](https://youtube.com/watch?v=LKCVKw9CzFo)
- [Structure du système de fichiers](https://www.zdnet.fr/pratique/linux-la-structure-du-systeme-de-fichiers-expliquee-397880.htm)
- [Commandes Linux](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes/) et [Commandes avancées](https://blog.stephane-robert.info/docs/admin-serveurs/linux/commandes-avancees/)
- [Scripts Shell](https://linux.goffinet.org/administration/scripts-shell/) et [TP pas à pas](https://systemes.gricad-pages.univ-grenoble-alpes.fr/www-unix/avance/seance1-2-script-sh-pas-a-pas/tp-pas-a-pas.pdf)
- [Variables d'environnement : TP pas à pas](https://systemes.gricad-pages.univ-grenoble-alpes.fr/www-unix/avance/seance4-varenv-pas-a-pas/tp-pas-a-pas-varenv.pdf)
- [Mind map SSH](https://www.formation-lpi.com/Mind-Map-SSH.html) et [Mind map GPG](https://www.formation-lpi.com/Mind-Map-gpg.html)
- [Migrer une installation Linux](https://www.antoinefi.net/index.php/2025/01/29/migrer-une-installation-linux/)
- Livre : Unix and Linux system administration handbook, 5th edition. Evi Nemeth, Garth Snyder, Trent R.Hein, Ben Whaley, Dan Mackin
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)

### Liens VIM

- <https://vim-adventures.com>
- <https://thevaluable.dev/vim-commands-beginner/>
- <https://thevaluable.dev/vim-intermediate/>
- <https://thevaluable.dev/vim-advanced/>
- <https://thevaluable.dev/vim-adept/>
- <https://thevaluable.dev/vim-veteran/>
- <https://thevaluable.dev/vim-expert/>
