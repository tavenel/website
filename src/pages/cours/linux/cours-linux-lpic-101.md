---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Linux LPIC-101
keywords:
- linux
---

# Présentation LPIC-1

---

## En pratique

- 2 parties : LPIC-101 et LPIC-102 pour obtenir le LPIC-1
- Dans ce cours : LPIC-101 (LPIC-102 au 2nd semestre)
- Examens en anglais
- 1H30
- 60 questions découpées proportionnellement au poids des chapitres : 8 pour chapitre 1, ... (voir plan)
- Score > 500/800 pour passer (12.5/20)

---

## Exam101

- Compétences de base: matériel, installation de Linux, gestion des packages, commandes Unix et GNU, système de fichiers , X Window.
- Connaissance globale du système Linux ;
- Options les plus utilisées des commandes.

---

## Exam102

- Noyau, initialisation du système, impression, documentation, scripts shell, tâches administratives, gestion du réseau et sécurité.
- Administration de système Linux ;
- Gérer efficacement les tâches d'un système.

---

![](https://www.formation-lpi.com/IMG/png/01-programme-lpi101-v5.0.png)

---

![](https://www.formation-lpi.com/IMG/png/programme-lpi102-v5.0.png)

---

# Niveau requis

- Expérience en architecture Intel x86 (plusieurs années, y compris composants matériels et leurs interactions avec l'OS)
- Bases de la ligne de commande GNU/Linux (> 3 mois)
- Connaissance de base des réseaux TCP/IP
- Connaissance des structures de systèmes de fichiers
- Pratique de l'anglais technique pour le passage de l'examen

---

# Objectifs

- Reconnaître le matériel : ports PCI / USB, paramétrage du BIOS / UEFI
- Savoir installer et configurer un système GNU/Linux sur un poste de type PC
- Savoir utiliser les niveaux d’exécution et cibles systemd du système
- Savoir installer et désinstaller les programmes sur les distributions des familles RedHat ou Debian, et gérer les bibliothèques partagées.
- Connaître les spécificités de Linux en tant que système virtualisé.
- Bien utiliser la ligne de commande Linux (Bash, vi)
- Gérer les disques, partitions et systèmes de fichiers courants
- Gestion des fichiers : permissions et propriétés, recherche et liens

---

# Ressources utiles

---

## Supports de cours

- [LA référence - Support officiel : LPIC-1 Exam 101, PDF, English](https://learning.lpi.org/en/learning-materials/learning-materials/)
- [Support officiel FR en cours de rédaction](https://learning.lpi.org/fr/learning-materials/learning-materials/)
- [Programme du LPI 101](https://wiki.lpi.org/wiki/LPIC-1_Objectives_V5.0)
- [Les principaux mots-clés à connaître](https://www.linuxcertif.com/doc/keyword_category/)

---

## Bibliographie

- [Bouziri, N. H. Andriambelo, A. Boyanov, N. Larrousse 2010. Préparation à l’examen 101 pour la certification de l’Institut professionnel de Linux, niveau junior LPIC-1. Agence universitaire de la Francophonie, Paris.](https://graal.ens-lyon.fr/~ycaniou/Teaching/CertificationLPI/Support_LPIC-101.pdf)
- [Préparation à la certification LPIC-1 examens LPI 101 et LPI 102, Sébastien ROHAUT, éditions ENI](https://www.editions-eni.fr/livre/linux-preparation-a-la-certification-lpic-1-examens-lpi-101-et-lpi-102-6e-edition-9782409024962)
- [Livre Bash beginner's guide](https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/)

---

## Examens blancs

- <https://www.penguintutor.com/quiz/index.php>
- <https://www.examtopics.com/exams/lpi/101-500/view/>
- <https://www.itexams.com/vendor/LPI>
- <https://www.certlibrary.com/vendor/LPI>

---

## Autres liens utiles

- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)
- [Supports recommandés par le LPI](https://lpi-fr.net/ressources/supports-de-formation/)

---

# Comment préparer la certification ?

1. Les concepts principaux sont dans ces slides
2. Le support détaillé reprend et complète les explications données en cours
3. Pendant le cours :
  - prendre des notes, notamment sur les options
  - reproduire les exercices pendant le cours
4. En autonomie :
  - reproduire les exercices
  - s'exercer aux examens blancs

---

La certification LPIC est conséquente et les questions très précises, il faut donc :

- bien apprendre **par cœur les commandes et les options à utiliser**
- **apprendre et pratiquer le vocabulaire (conséquent)**
- **s'entraîner régulièrement**

---

# Quelle distribution ?

- LPIC-1 vise des concepts généraux, pas vraiment de distribution de choix...
- ...mais vise principalement les dérivés Debian (Ubuntu, ...) et RedHat (RHEL, CentOS, ...)

---

<!-- class: legal -->

# Legal

- Linux est une marque déposée par Linus Torvalds aux États Unis et dans d'autres pays.
- Red Hat Linux et Red Hat Enterprise Linux sont des marques déposées par RedHat Inc.
- Mandriva® Linux® est une marque déposée par Mandriva Inc.
- SUSE™ (SUSE est une marque de SUSE LINUX Products GmbH, une filiale de Novell)
- UNIX® est une marque déposée de The Open Group. 
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
