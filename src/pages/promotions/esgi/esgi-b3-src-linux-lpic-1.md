---
title: 🐧 Tom Avenel - B3 LPIC-1
---

# 🐧 Linux administration avancée LPIC-1 v5.0

_Préparation à la certification LPIC-1 v5.0_

![](/resources/images/cover/linux.jpg)

## Environnements de travail

Les deux environnements suivants doivent être installés.

### 💻 Machine virtuelle Fedora

Installation d'une machine virtuelle Fedora de type Desktop dans VirtualBox.

- [html](/cours/linux/installation/tp-installation-vbox-fedora-workstation.html)
- [pdf](/cours/linux/installation/tp-installation-vbox-fedora-workstation.pdf)
- [markdown](/cours/linux/installation/tp-installation-vbox-fedora-workstation.md)

### 💻 Machine virtuelle Ubuntu

Installation d'une machine virtuelle Ubuntu de type Desktop dans VirtualBox.

- [html](/cours/linux/installation/tp-installation-vbox-ubuntu-workstation.html)
- [pdf](/cours/linux/installation/tp-installation-vbox-ubuntu-workstation.pdf)
- [markdown](/cours/linux/installation/tp-installation-vbox-ubuntu-workstation.md)

## Présentation de la certification LPIC-1 v5.0

- 2 parties : LPIC-101 et LPIC-102 pour obtenir le LPIC-1
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

- LPIC-1 vise des concepts généraux, pas vraiment de distribution de choix...
- ...mais vise principalement les dérivés Debian (Ubuntu, ...) et RedHat (RHEL, CentOS, ...)

### Niveau requis

- Expérience en architecture Intel x86 (plusieurs années, y compris composants matériels et leurs interactions avec l'OS)
- Bases de la ligne de commande GNU/Linux (> 3 mois)
- Connaissance de base des réseaux TCP/IP
- Connaissance des structures de systèmes de fichiers
- Pratique de l'anglais technique pour le passage de l'examen

### Ressources utiles

#### 📄 Supports de cours

- [Les principaux mots-clés à connaître](https://www.linuxcertif.com/doc/keyword_category/)
- [LA référence - Support officiel : LPIC-1 Exam 101, PDF, English](https://learning.lpi.org/en/learning-materials/learning-materials/)
- [Support officiel FR en cours de rédaction](https://learning.lpi.org/fr/learning-materials/learning-materials/)
- [Programme du LPI 101](https://wiki.lpi.org/wiki/LPIC-1_Objectives_V5.0)
- [Objectifs détaillés de la certification LPIC-102](https://www.lpi.org/fr/our-certifications/exam-102-objectives)
- [Support de cours LPIC-102](https://learning.lpi.org/en/learning-materials/102-500/)

#### 📝 Bibliographie

- [Bouziri, N. H. Andriambelo, A. Boyanov, N. Larrousse 2010. Préparation à l’examen 101 pour la certification de l’Institut professionnel de Linux, niveau junior LPIC-1. Agence universitaire de la Francophonie, Paris.](https://graal.ens-lyon.fr/~ycaniou/Teaching/CertificationLPI/Support_LPIC-101.pdf)
- [Préparation à la certification LPIC-1 examens LPI 101 et LPI 102, Sébastien ROHAUT, éditions ENI](https://www.editions-eni.fr/livre/linux-preparation-a-la-certification-lpic-1-examens-lpi-101-et-lpi-102-6e-edition-9782409024962)
- [Supports recommandés par le LPI](https://lpi-fr.net/ressources/supports-de-formation/)
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
- [Supports recommandés par le LPI](https://lpi-fr.net/ressources/supports-de-formation/)
- <https://www.antoinefi.net/index.php/2024/12/19/linux-lpic-1-101-500-1/>
- <https://www.antoinefi.net/index.php/2024/12/30/linux-lpic-1-101-500-2/>
- <https://www.antoinefi.net/index.php/2025/01/13/linux-lpic-1-101-500-3/>

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

### Plan de cours

#### Rappels de cours

- Rôle d'un système d'exploitation
- Le noyau Linux, Noyau Linux vs Distribution GNU/Linux
- La ligne de commandes
- Les processus
- Les utilisateurs
- Le système de fichiers
- Les chemins de fichiers
- Les permissions sur les fichiers

#### 1.1 - Sujet 101 : Architecture système [8]

- 101.1 Détermination et configuration des paramètres du matériel [2]
  - TP : affichage de la configuration du système et des périphériques, gestion des modules noyau
- 101.2 Démarrage du système [3]
  - TP : Grub
  - TP : SysV init et systemd init
- 101.3 Changement de niveaux d'exécution / des cibles de démarrage de systemd et arrêt ou redémarrage du système. [3]

#### 1.2 - Sujet 102 : Installation de Linux et gestion de paquetages [12]

- 102.1 Conception du schéma de partitionnement [2]
- 102.2 Installation d'un gestionnaire d'amorçage [2]
- 102.3 Gestion des bibliothèques partagées [1]
  - TP : librairies partagées
- 102.4 Utilisation du gestionnaire de paquetage Debian [3]
- 102.5 Utilisation des gestionnaires de paquetage RPM et YUM [3]
  - TP : Gestion de paquetages : rpm, yum et dnf vs dpkg et apt
- 102.6 Linux en tant que système virtuel hébergé [1]

#### 1.3 - Sujet 103 : Commandes GNU et Unix [26]

- 103.1 Travail en ligne de commande [4]
  - TP : Utilisation de la ligne de commande
- 103.2 Traitement de flux de type texte avec des filtres [2]
  - TP : Traitement de flux de type texte avec filtres et expressions rationnelles
- 103.3 Gestion élémentaire des fichiers [4]
  - TP : Gestion des fichiers
- 103.4 Utilisation des flux, des pipes et des redirections [4]
  - TP : Utilisation des flux, des pipes et des redirections 
- 103.5 Création, contrôle et interruption des processus [4]
- 103.6 Modification des priorités des processus [2]
  - TP : Gestion des processus et de leur priorité
- 103.7 Recherche dans des fichiers texte avec les expressions rationnelles [3]
- 103.8 Édition de fichier simple [3]
  - TP : Introduction à vi

#### 1.4 - Sujet 104 : Disques, systèmes de fichiers Linux, arborescence de fichiers standard (FHS) [14]

- 104.1 Création des partitions et des systèmes de fichiers [2]
- 104.2 Maintenance de l'intégrité des systèmes de fichiers [2]
- 104.3 Montage et démontage des systèmes de fichiers [3]
  - TP : Gestion des partitions et des systèmes de fichiers
- 104.4 Supprimé
- 104.5 Gestion des permissions et de la propriété sur les fichiers [3]
- 104.6 Création et modification des liens physiques et symboliques sur les fichiers [2]
- 104.7 Recherche de fichiers et placement des fichiers aux endroits adéquats [2]
  - TP : Gestion avancée de fichiers - permissions, liens, recherche

### 📅 Déroulé du cours

- Module de 18H
- Évaluation : QCM et Examen blanc
- Comment préparer la certification ?
  * Les concepts principaux sont dans ces slides
  * Le support détaillé reprend et complète les explications données en cours
  * Pendant le cours :
    * prendre des notes, notamment sur les options
    * reproduire les exercices pendant le cours
  * En autonomie :
    * reproduire les exercices
    * s'exercer aux examens blancs
- La certification LPIC est conséquente et les questions très précises, il faut donc :
  * bien apprendre **par coeur les commandes et les options à utiliser**
  * **apprendre et pratiquer le vocabulaire (conséquent)**
  * **s'entraîner régulièrement**
- Quelle distribution ?
  * LPIC-1 vise des concepts généraux, pas vraiment de distribution de choix...
  * ...mais vise principalement les dérivés Debian (Ubuntu, ...) et RedHat (RHEL, CentOS, ...)

### 🤓 Cours Linux LPIC-101

- [html](/cours/linux/niveau2/cours-linux-niveau2_partie1.html)
- [pdf](/cours/linux/niveau2/cours-linux-niveau2_partie1.pdf)
- [markdown](/cours/linux/niveau2/cours-linux-niveau2_partie1.md)

### ⌨️ TP : affichage de la configuration du système et des périphériques, gestion des modules noyau

L'objectif de ce TP est la récupération d'informations sur le système et sur les périphériques de la machine.

- [html](/cours/linux/niveau2/tp-systeme.html)
- [pdf](/cours/linux/niveau2/tp-systeme.pdf)
- [markdown](/cours/linux/niveau2/tp-systeme.md)

### 📀 TP : Grub

L'objectif de ce TP est d'utiliser GRUB pour une restauration système.

- [html](/cours/linux/niveau2/tp-grub.html)
- [pdf](/cours/linux/niveau2/tp-grub.pdf)
- [markdown](/cours/linux/niveau2/tp-grub.md)

### ▶️ TP : SysV init et systemd init

Dans ce TP, nous allons découvrir comment administrer les services d'un système Linux et comment changer de runlevel, dans un système SysV ou systemd.

- [html](/cours/linux/niveau2/tp-sysv-systemd.html)
- [pdf](/cours/linux/niveau2/tp-sysv-systemd.pdf)
- [markdown](/cours/linux/niveau2/tp-sysv-systemd.md)

### 🗃️ TP : librairies partagées

L'objectif de ce TP est de comprendre la notion de bibliothèque partagée dans un environnement Linux.

- [html](/cours/linux/niveau2/tp-shared-lib.html)
- [pdf](/cours/linux/niveau2/tp-shared-lib.pdf)
- [markdown](/cours/linux/niveau2/tp-shared-lib.md)

### 📦 TP : Gestion de paquetages : rpm, yum et dnf vs dpkg et apt

L'objectif de ce TP est d'apprendre à gérer (installer, mettre à jour, désinstaller) des programmes depuis des packets RedHat via rpm, yum et dnf et des packets Debian via dpkg et apt.

- [html](/cours/linux/niveau2/tp-rpm-apt.html)
- [pdf](/cours/linux/niveau2/tp-rpm-apt.pdf)
- [markdown](/cours/linux/niveau2/tp-rpm-apt.md)

###   TP : Utilisation de la ligne de commande

L'objectif de ce TP est d'utiliser efficacement la ligne de commande.

- [html](/cours/linux/niveau2/tp-ligne-commande.html)
- [pdf](/cours/linux/niveau2/tp-ligne-commande.pdf)
- [markdown](/cours/linux/niveau2/tp-ligne-commande.md)

### 📃 TP : Traitement de flux de type texte

Dans un système Linux, l'échange d'information passe principalement par des fichiers texte - il existe donc de très nombreuses commandes optimisées à cette fin avec lesquelles il faut être à l'aise. Il y aura également souvent plusieurs possiblités pour arriver au même résultat.

- [html](/cours/linux/niveau2/tp-texte.html)
- [pdf](/cours/linux/niveau2/tp-texte.pdf)
- [markdown](/cours/linux/niveau2/tp-texte.md)

### 📂 TP : Gestion basique des fichiers - déplacement, copie, liste, types de fichiers

L'objectif de ce TP est d'apprendre la gestion basique des fichiers - déplacement, copie, liste, types de fichiers

- [html](/cours/linux/niveau2/tp-fichiers.html)
- [pdf](/cours/linux/niveau2/tp-fichiers.pdf)
- [markdown](/cours/linux/niveau2/tp-fichiers.md)

### ↔️ TP : Utilisation des flux, des pipes et des redirections 

L'objectif de ce TP est d'apprendre à utiliser les redirections de fichiers et les pipes.

- [html](/cours/linux/niveau2/tp-redirections.html)
- [pdf](/cours/linux/niveau2/tp-redirections.pdf)
- [markdown](/cours/linux/niveau2/tp-redirections.md)

### ⚙️ TP : Gestion des processus et de leur priorité

L'objectif de ce TP est d'apprendre à surveiller et gérer les processus sous Linux.

- [html](/cours/linux/niveau2/tp-process.html)
- [pdf](/cours/linux/niveau2/tp-process.pdf)
- [markdown](/cours/linux/niveau2/tp-process.md)

### 💽 TP : Gestion des partitions et des systèmes de fichiers

L'objectif de ce TP est d'apprendre à créer des partitions et administrer des systèmes de fichiers.

- [html](/cours/linux/niveau2/tp-partitions.html)
- [pdf](/cours/linux/niveau2/tp-partitions.pdf)
- [markdown](/cours/linux/niveau2/tp-partitions.md)

### 💽 TP : Gestion des disques et partitions avec LVM

L'objectif de ce TP est d'apprendre à utiliser LVM pour créer, gérer et étendre des volumes logiques.

- [html](/cours/linux/niveau2/tp-lvm.html)
- [pdf](/cours/linux/niveau2/tp-lvm.pdf)
- [markdown](/cours/linux/niveau2/tp-lvm.md)

### 📁 TP : Gestion avancée de fichiers - permissions, liens, recherche

L'objectif de ce TP est la gestion avancée de fichiers - gestion des permissions, liens standards et symboliques, recherche de chemins de fichiers et de contenus.

- [html](/cours/linux/niveau2/tp-fichiers-avance.html)
- [pdf](/cours/linux/niveau2/tp-fichiers-avance.pdf)
- [markdown](/cours/linux/niveau2/tp-fichiers-avance.md)

### 🔐 TP : Gestion des permissions avancées avec SUID, SGID et ACL

Ce TP a pour objectif d'apprendre l'utilisation des permissions avancées sous Linux, à savoir le SUID, le SGID et les listes de contrôle d'accès (ACL).

- [html](/cours/linux/niveau2/tp-droits-avance.html)
- [pdf](/cours/linux/niveau2/tp-droits-avance.pdf)
- [markdown](/cours/linux/niveau2/tp-droits-avance.md)

### ✍️ TP : Introduction à vi

Exécuter la commande `vimtutor`.

## LPIC-102

### 💻 Objectifs

- Paramétrer le shell et écrire des scripts simples en `Bash`
- Installer et configurer l'interface graphique
- Connaître les outils d'accessibilité
- Effectuer les tâches d'administration de base : gérer les utilisateurs, utiliser les tâches automatiques, …
- Installer et paramétrer les services essentiels : messagerie, impression, horloge système, journaux système
- Avoir les notions de réseau essentielles à l’administration système : protocoles Internet, configuration réseau des postes, résolution `DNS` et dépannage
- Savoir mettre en place un niveau de sécurité sur les postes : services en écoute et ports ouverts, limitations d'accès, et chiffrement des données

### Plan de cours

#### Sujet 105 : Shells et scripts Shell [8]

- 105.1 Personnalisation et utilisation de l’environnement du shell [4]
- 105.2 Personnalisation ou écriture de scripts simples [4]

#### Sujet 106 : Interfaces et bureaux utilisateur [4]

- 106.1 Installation et configuration de X11 [2]
- 106.2 Bureaux graphiques [1]
- 106.3 Accessibilité [1]

#### Sujet 107 : Tâches d’administration [12]

- 107.1 Gestion des comptes utilisateurs et des groupes ainsi que des fichiers systèmes concernés [5]
- 107.2 Automatisation des tâches d’administration par la planification des travaux [4]
- 107.3 Paramètres régionaux et langues [3]

#### Sujet 108 : Services systèmes essentiels [12]

- 108.1 Gestion de l’horloge système [3]
- 108.2 Journaux systèmes [4]
- 108.3 Bases sur l’agent de transfert de courrier (MTA) [3]
- 108.4 Gestion des imprimantes et de l’impression [2]

#### Sujet 109 : Notions élémentaires sur les réseaux [14]

- 109.1 Notions élémentaires sur les protocoles Internet [4]
- 109.2 Configuration réseau persistante [4]
- 109.3 Résolution de problèmes réseaux simples [4]
- 109.4 Configuration de la résolution de noms [2]

#### Sujet 110 : Securité [10]

- 110.1 Tâches d’administration de sécurité [3]
- 110.2 Configuration de la sécurité du système [3]
- 110.3 Sécurisation des données avec le chiffrement [4]

### 📅 Déroulé du cours

- Module de 16.5H
- Évaluation : QCM et Examen blanc

### 🤓 Cours Linux LPIC-102

- [html](/cours/linux/niveau2/cours-linux-niveau2_partie2.html)
- [pdf](/cours/linux/niveau2/cours-linux-niveau2_partie2.pdf)
- [markdown](/cours/linux/niveau2/cours-linux-niveau2_partie2.md)

### 🤓 Cours : Le shell

L'objectif de ce TP est de se familiariser avec l'utilisation du shell Bash : fonctions, boucles, tests, …

- [html](/cours/linux/niveau2/cours-shell.html)
- [pdf](/cours/linux/niveau2/cours-shell.pdf)
- [markdown](/cours/linux/niveau2/cours-shell.md)

#### 📜 TP - Création de scripts Bash

Dans ce TP, nous allons créer des scripts grâce au langage Bash.

- [html](/cours/linux/niveau1/tp-scripts_bash.html)
- [pdf](/cours/linux/niveau1/tp-scripts_bash.pdf)
- [markdown](/cours/linux/niveau1/tp-scripts_bash.md)

#### 📜 TP Bash - Gestion des fichiers et des utilisateurs

Dans ce TP, nous allons :

- Apprendre à manipuler des fichiers et des répertoires avec Bash.
- Utiliser des boucles et des conditions.
- Créer des scripts interactifs.
- Gérer les utilisateurs et permissions basiques dans un environnement Linux.

- [html](/cours/linux/niveau2/tp-script.html)
- [pdf](/cours/linux/niveau2/tp-script.pdf)
- [markdown](/cours/linux/niveau2/tp-script.md)

#### 🚮 TP - Commande trash

Dans ce TP, nous allons créer une commande simulant l'utilisation d'une poubelle.

- [html](/cours/linux/niveau1/tp-trash.html)
- [pdf](/cours/linux/niveau1/tp-trash.pdf)
- [markdown](/cours/linux/niveau1/tp-trash.md)

### 👥 TP : Gestion des utilisateurs et de la sécurité

L'objectif de ce TP est de créer un utilisateur et d'appliquer une politique de sécurité. 

- [html](/cours/linux/niveau2/tp-utilisateurs.html)
- [pdf](/cours/linux/niveau2/tp-utilisateurs.pdf)
- [markdown](/cours/linux/niveau2/tp-utilisateurs.md)

### 🕗 TP : Planification de tâches avec `at`, `cron` et `systemd`

L'objectif de ce TP est de plannifier l'exécution simple ou récurrente de tâches avec les programmes `at` et `cron`, ou en utilisant des timers `systemd`.

- [html](/cours/linux/niveau2/tp-cron.html)
- [pdf](/cours/linux/niveau2/tp-cron.pdf)
- [markdown](/cours/linux/niveau2/tp-cron.md)

### 📨 TP : Langue et encodage

L'objectif de ce TP est de gérer l'utilisation d'encodages différents (`ASCII`, `UTF-8`, …), de formats de fichiers différents (`Unix`/Linux vs `Dos`/Windows) et la gestion de langues différentes par l'utilisation de _locales_.

- [html](/cours/linux/niveau2/tp-lang.html)
- [pdf](/cours/linux/niveau2/tp-lang.pdf)
- [markdown](/cours/linux/niveau2/tp-lang.md)

### 📜 TP : Journalisation avec Syslog

L'objectif de ce TP est de gérer les journaux (logs) système et utilisateur, en local ou vers un serveur centralisé, notamment par le biais de `syslog` et ses différentes implémentations : `syslog`, `rsyslog` et `syslog-ng` (l'accent est mis sur `rsyslog`). Les liens entre `syslog` et `systemd-journald` sont également abordés.

#### Rappel - TP : journaux de logs avec systemd

Rappels du tp `sytemd` pour utiliser la journalisation `systemd-journald`.

- [html](/cours/linux/niveau2/tp-sysv-systemd.html)
- [pdf](/cours/linux/niveau2/tp-sysv-systemd.pdf)
- [markdown](/cours/linux/niveau2/tp-sysv-systemd.md)

#### TP sur la journalisation

Le TP de niveau LPIC-102 sur la journalisation.

- [html](/cours/linux/niveau2/tp-syslog.html)
- [pdf](/cours/linux/niveau2/tp-syslog.pdf)
- [markdown](/cours/linux/niveau2/tp-syslog.md)

### 📨 TP Bonus : Envoi de mail en utilisant le protocole SMTP

Dans ce TP, nous allons utiliser le protocole SMTP pour envoyer un mail depuis votre adresse de courrier électronique.

- [html](/cours/cloud/exo-smtp.html)
- [pdf](/cours/cloud/exo-smtp.pdf)
- [markdown](/cours/cloud/exo-smtp.md)

### 📡 TP : Configuration réseau

L'objectif de ce TP est de gérer la configuration réseau d'un système Linux en utilisant à la fois : les outils historiques `net-tools`, les outils modernes `iproute2`, ou les implémentations `systemd`. L'utilisation de `Network Manager` est aussi abordée.

- [html](/cours/linux/niveau2/tp-network.html)
- [pdf](/cours/linux/niveau2/tp-network.pdf)
- [markdown](/cours/linux/niveau2/tp-network.md)

### 🔐 TP : Notions de sécurité d'un système Linux

L'objectif de ce TP est d'aborder des notions de sécurité sur un système Linux : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …

- [html](/cours/linux/niveau2/tp-security.html)
- [pdf](/cours/linux/niveau2/tp-security.pdf)
- [markdown](/cours/linux/niveau2/tp-security.md)

### 🔐 TP : Sécurité des échanges avec SSH et GPG

- [html](/cours/linux/niveau2/tp-ssh-gpg.html)
- [pdf](/cours/linux/niveau2/tp-ssh-gpg.pdf)
- [markdown](/cours/linux/niveau2/tp-ssh-gpg.md)

