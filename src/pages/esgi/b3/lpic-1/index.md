---
title: 🐧 LPIC-1
layout: '@layouts/BaseLayout.astro'
---

# 🐧 Linux LPIC-1

_Préparation à la certification LPIC-1 v5.0_

## Présentation de la certification

- 2 examens : LPIC-101 **puis** LPIC-102 pour obtenir le LPIC-1
- 2 modules : LPIC-101 (1er semestre) et LPIC-102 (2nd semestre)
- Examens en anglais
- 1H30
- 60 questions découpées proportionnellement au poids des chapitres : 8 pour chapitre 1, ... (voir plan)
- Score > 500/800 pour passer (12.5/20)

### Exam101

- Compétences de base: matériel, installation de Linux, gestion des packages, commandes Unix et GNU, système de fichiers , X Window.
- Connaissance globale du système Linux ;
- Options les plus utilisées des commandes.

### Exam102

- Noyau, initialisation du système, impression, documentation, scripts shell, tâches administratives, gestion du réseau et sécurité.
- Administration de système Linux ;
- Gérer efficacement les tâches d'un système.

### Comment préparer la certification ?

1. Les concepts principaux sont dans ces slides
2. Le support détaillé reprend et complète les explications données en cours
3. Pendant le cours :
  - prendre des notes, notamment sur les options
  - reproduire les exercices pendant le cours
4. En autonomie :
  - reproduire les exercices
  - s'exercer aux examens blancs

La certification LPIC est conséquente et les questions très précises, il faut donc :

- bien apprendre **par coeur les commandes et les options à utiliser**
- **apprendre et pratiquer le vocabulaire (conséquent)**
- **s'entraîner régulièrement**

### Quelle distribution ?

- LPIC vise des concepts généraux, pas vraiment de distribution de choix...
- ...mais vise principalement les dérivés Debian (Ubuntu, ...) et RedHat (RHEL, CentOS, ...)

### Niveau requis

- Expérience en architecture Intel x86 (plusieurs années, y compris composants matériels et leurs interactions avec l'OS)
- Bases de la ligne de commande GNU/Linux (> 3 mois)
- Connaissance de base des réseaux TCP/IP
- Connaissance des structures de systèmes de fichiers
- Pratique de l'anglais technique pour le passage de l'examen

### Ressources utiles

#### 📄 Supports de cours

- [LA référence - Support officiel : LPIC-1 Exam 101, PDF, English](https://www.lpi.org/fr/our-certifications/lpic-1-overview/)

#### 📝 Bibliographie

- [Bouziri, N. H. Andriambelo, A. Boyanov, N. Larrousse 2010. Préparation à l’examen 101 pour la certification de l’Institut professionnel de Linux, niveau junior LPIC-1. Agence universitaire de la Francophonie, Paris.](https://graal.ens-lyon.fr/~ycaniou/Teaching/CertificationLPI/Support_LPIC-101.pdf)
- [Livre Bash beginner's guide](https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/)

#### 📄 Examens blancs

- <https://www.penguintutor.com/quiz/index.php>
- <https://www.examtopics.com/exams/lpi/101-500/view/>
- <https://www.itexams.com/vendor/LPI>
- <https://www.certlibrary.com/vendor/LPI>

#### 🔗 Autres liens utiles

- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)
- <https://www.antoinefi.net/index.php/2024/12/19/linux-lpic-1-101-500-1/>
- <https://www.antoinefi.net/index.php/2024/12/30/linux-lpic-1-101-500-2/>
- <https://www.antoinefi.net/index.php/2025/01/13/linux-lpic-1-101-500-3/>
- [Présentation et comparaison des certifications Linux](https://blog.stephane-robert.info/docs/admin-serveurs/linux/certifications/)

## LPIC-101

### 🎯 Objectifs

- Reconnaître le matériel : ports PCI / USB, paramétrage du BIOS / UEFI
- Savoir installer et configurer un système GNU/Linux sur un poste de type PC
- Savoir utiliser les niveaux d’exécution et cibles systemd du système
- Savoir installer et désinstaller les programmes sur les distributions des familles RedHat ou Debian, et gérer les bibliothèques partagées.
- Connaître les spécificités de Linux en tant que système virtualisé.
- Bien utiliser la ligne de commande Linux (Bash, vi)
- Gérer les disques, partitions et systèmes de fichiers courants
- Gestion des fichiers : permissions et propriétés, recherche et liens

### 📅 Déroulé du cours

- Module de 18H
- Évaluation : QCM et Examen blanc

### 📑 Documents LPIC-101

- Les deux environnements suivants doivent être installés :
  - [󰣛 Machine virtuelle Fedora Desktop dans VirtualBox](/linux/tp-installation-vbox-fedora-workstation)
  - [󰕈 Machine virtuelle Ubuntu Desktop dans VirtualBox](/linux/tp-installation-vbox-ubuntu-workstation)
- 🤓 [Slides de cours LPIC-101](/linux/cours-lpic-101)
- [⌨️ TP : affichage de la configuration du système et des périphériques, gestion des modules noyau](/linux/tp-systeme)
- [📀 TP : utiliser GRUB pour une restauration système](/linux/tp-grub)
- [📀 TP : utiliser un live-CD pour une restauration système](/linux/tp-rescue)
- [▶️ TP : SysV init](/linux/tp-sysv) : administrer les services et changer de runlevel dans un système SysV.
- [▶️ TP : Systemd init](/linux/tp-systemd) : administrer les services et changer de runlevel dans un système systemd.
- [🗃️ TP : librairies partagées](/linux/tp-shared-lib)
- [📦 TP : Gestion de paquetages](/linux/tp-rpm-apt) : gérer (installer, mettre à jour, désinstaller) des programmes depuis des packets RedHat via rpm, yum et dnf et des packets Debian via dpkg et apt.
- [  TP : Utilisation efficace de la ligne de commande](/linux/tp-ligne-commande)
- [📃 TP : Traitement de flux de type texte](/linux/tp-texte)
- [📂 TP : Gestion basique des fichiers - déplacement, copie, liste, types de fichiers](/linux/tp-fichiers)
- [↔️ TP : Utilisation des flux, des pipes et des redirections ](/linux/tp-redirections)
- [⚙️ TP : Gestion des processus et de leur priorité](/linux/tp-process)
- [💽 TP : Gestion des partitions et des systèmes de fichiers](/linux/tp-partitions)
- [💽 TP : Utiliser LVM pour créer, gérer et étendre des volumes logiques](/linux/tp-lvm)
- [📁 TP : Gestion avancée de fichiers - permissions, liens, recherche](/linux/tp-fichiers-avance)
- [🔐 TP : Gestion des permissions avancées avec SUID, SGID et ACL](/linux/tp-droits-avance)
- ✍️ TP : Introduction à `vi` : exécuter la commande `vimtutor`.


## LPIC-102

### 💻 Objectifs

- Paramétrer le shell et écrire des scripts simples en `Bash`
- Installer et configurer l'interface graphique
- Connaître les outils d'accessibilité
- Effectuer les tâches d'administration de base : gérer les utilisateurs, utiliser les tâches automatiques, …
- Installer et paramétrer les services essentiels : messagerie, impression, horloge système, journaux système
- Avoir les notions de réseau essentielles à l’administration système : protocoles Internet, configuration réseau des postes, résolution `DNS` et dépannage
- Savoir mettre en place un niveau de sécurité sur les postes : services en écoute et ports ouverts, limitations d'accès, et chiffrement des données

### 📅 Déroulé du cours

- Module de 16.5H
- Évaluation : QCM et Examen blanc

### 📑 Documents LPIC-102

- 🤓 [Slides de cours LPIC-102](/linux/cours-lpic-102)
- [🤓 Cours complet sur le shell Bash : fonctions, boucles, tests, …](/linux/cours-shell)
- [📜 TP - Création de scripts Bash](/linux/tp-scripts_bash)
- [📜 TP Bash - Gestion des fichiers et des utilisateurs](/linux/tp-script) : apprendre à manipuler des fichiers et des répertoires avec Bash, utiliser des boucles et des conditions, créer des scripts interactifs, gérer les utilisateurs et permissions basiques.
- [🚮 TP - Commande trash simulant l'utilisation d'une poubelle](/linux/tp-trash)
- [👥 TP : Gestion des utilisateurs et de la sécurité](/linux/tp-utilisateurs)
- [🕗 TP : Planification de tâches avec `at`, `cron` et `systemd`](/linux/tp-cron)
- [📨 TP : Langue et encodage](/linux/tp-lang) : gérer l'utilisation d'encodages différents (`ASCII`, `UTF-8`, …), de formats de fichiers différents (`Unix`/Linux vs `Dos`/Windows) et de langues différentes par l'utilisation de _locales_.
- [📜 TP : Journalisation avec Syslog](/linux/tp-syslog) : gérer les journaux (logs) système et utilisateur, en local ou vers un serveur centralisé, notamment par le biais de `syslog` et ses différentes implémentations : `syslog`, `rsyslog` et `syslog-ng`.
  - Rappel - TP : [journaux de logs avec systemd-journald](/linux/tp-systemd)
- [📡 TP : Configuration réseau](/linux/tp-network) : gérer la configuration réseau d'un système Linux en utilisant les outils historiques `net-tools`, les outils modernes `iproute2`, ou les implémentations `systemd`. L'utilisation de `Network Manager` est aussi abordée.
- [🔐 TP : Notions de sécurité : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …](/linux/tp-security)
- [🔐 TP : Sécurité des échanges avec SSH et GPG](/linux/tp-ssh-gpg)

## 🚀 Pour aller plus loin

- Voir les autres ressources du [cours sur Linux](/linux).
