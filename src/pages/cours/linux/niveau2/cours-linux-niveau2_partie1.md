---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Cours Linux avancé - partie 1
tags:
- linux
---

## Chapitres

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

- [Support de cours](https://learning.lpi.org/fr/learning-materials/101-500/)
- [Support de cours (PDF)](https://learning.lpi.org/pdfstore/LPI-Learning-Material-101-500-en.pdf)
- [Objectifs détaillés de la certification LPIC-101](https://www.lpi.org/fr/our-certifications/exam-102-objectives)
- [Livre Bash beginner's guide](https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/)
- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)

---

## Conventions de notation

- Les commandes et noms de fichiers apparaissent dans le texte avec `cette syntaxe`.
- Les descriptions de commandes suivent le formalisme des _man pages_ :
  - Les symboles `<>` indiquent un argument obligatoire.
  - Les symboles `[]` indiquent un argument optionnel.  

---

# Plan de cours

## 1.1 - Sujet 101 : Architecture système [8]

- 101.1 Détermination et configuration des paramètres du matériel [2]
  - TP : affichage de la configuration du système et des périphériques
  - TP : gestion des modules noyau
- 101.2 Démarrage du système [3]
  - TP : Grub
  - TP : SysV init et systemd init
- 101.3 Changement de niveaux d'exécution / des cibles de démarrage de systemd et arrêt ou redémarrage du système. [3]

---

## 1.2 - Sujet 102 : Installation de Linux et gestion de paquetages [12]

- 102.1 Conception du schéma de partitionnement [2]
- 102.2 Installation d'un gestionnaire d'amorçage [2]
- 102.3 Gestion des bibliothèques partagées [1]
  - TP : librairies partagées
- 102.4 Utilisation du gestionnaire de paquetage Debian [3]
- 102.5 Utilisation des gestionnaires de paquetage RPM et YUM [3]
  - TP : Gestion de paquetages : rpm, yum et dnf vs dpkg et apt
- 102.6 Linux en tant que système virtuel hébergé [1]

---

## 1.3 - Sujet 103 : Commandes GNU et Unix [26]

- 103.1 Travail en ligne de commande [4]
  - TP : Utilisation de la ligne de commande
- 103.2 Traitement de flux de type texte avec des filtres [2]
  - TP : Traitement de flux de type texte avec filtres et expressions rationnelles
- 103.3 Gestion élémentaire des fichiers [4]
  - TP : Gestion des fichiers
- 103.4 Utilisation des flux, des pipes et des redirections [4]
  - TP : Utilisation des flux, des pipes et des redirections 

---

- 103.5 Création, contrôle et interruption des processus [4]
- 103.6 Modification des priorités des processus [2]
  - TP : Gestion des processus et de leur priorité
- 103.7 Recherche dans des fichiers texte avec les expressions rationnelles [3]
- 103.8 Édition de fichier simple [3]
  - TP : Introduction à vi

---

## 1.4 - Sujet 104 : Disques, systèmes de fichiers Linux, arborescence de fichiers standard (FHS) [14]

- 104.1 Création des partitions et des systèmes de fichiers [2]
- 104.2 Maintenance de l'intégrité des systèmes de fichiers [2]
- 104.3 Montage et démontage des systèmes de fichiers [3]
  - TP : Gestion des partitions et des systèmes de fichiers
- 104.4 Supprimé
- 104.5 Gestion des permissions et de la propriété sur les fichiers [3]
- 104.6 Création et modification des liens physiques et symboliques sur les fichiers [2]
- 104.7 Recherche de fichiers et placement des fichiers aux endroits adéquats [2]
  - TP : Gestion avancée de fichiers - permissions, liens, recherche

---
layout: section
---

# Chapitre 1. Architecture matérielle et gestion des périphériques

TODO

---
layout: section
---

# Chapitre 2. Installation de Linux et gestion de paquetages


TODO

---
layout: section
---

# Chapitre 3. Commandes GNU et Unix

TODO


---
layout: section
---

# Chapitre 4. Disques, systèmes de fichiers Linux, arborescence de fichiers standard (FHS)

[TODO]

# 104.4 Supprimé

TODO droits

---

- Voir le TP dédié [tp-fichiers-avance][tp-fichiers-avance].

---

# 104.6 Création et modification des liens physiques et symboliques sur les fichiers 


# 104.7 Recherche de fichiers et placement des fichiers aux endroits adéquats

---

## find

- Recherche récursive dans un répertoire des **chemins** de fichiers
- critères de recherche nom, type, date, taille utilisateur, ...
- pas de cache

---

## locate

- Interroge une BD des noms de fichiers (cache)
- `updatedb` met à jour le cache

---

## which

- Inverse du `$PATH` : retourne le chemin vers la commande
- `which <commande>` ou `which -a <commande>`

---

## type

- Similaire à `which`
- Ajoute le type de fichier
- `type [-a] [-t] <commande>`

---

## whereis

- Similaire à `which` mais ajoute les _man page_ et le code source
- `whereis [-b|m|s] <commande>` pour limiter la sortie au binaire / man page / source code

---

## Fichiers temporaires (FHS v3)

- `/tmp` : volatile
  + peut être effacé à l'arrêt du programme
  + (normalement) nettoyé au redémarrage
- `/var/tmp` : persistant
  + (normalement) conservé au redémarrage
- `/run` : données runtime (`pid`, ...)
  + précédemment `/var/run`

---

- Pour un rappel de la hierarchie standard des fichiers (FHS), voir le cours _104.7 Find system files and place files in the correct location_, p.524
- Voir le TP dédié [tp-fichiers-avance][tp-fichiers-avance].

---

![Les différents répertoires de la Filesystem Hierarchy Standard](@assets/linux/fhs.png)

<div class="caption">Les différents répertoires de la Filesystem Hierarchy Standard (FHS)</div>

<!-- Annexe : liste des TPs -->

[tp-ligne-commande]: tp-ligne-commande.md
[tp-systeme]: tp-systeme.md
[tp-grub]: tp-grub.md
[tp-shared-lib]: tp-shared-lib.md
[tp-sysv-systemd]: tp-sysv-systemd.md
[tp-rpm-apt]: tp-rpm-apt.md
[tp-texte]: tp-texte.md
[tp-fichiers]: tp-fichiers.md
[tp-redirections]: tp-redirections.md
[tp-process]: tp-process.md
[tp-fichiers-avance]: tp-fichiers-avance.md
[tp-partitions]: tp-partitions.md

<!-- Annexe: liste des liens utiles -->
[wiki-shared-lib]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/Installation_de_Linux_et_gestion_des_packages/G%C3%A9rer_les_biblioth%C3%A8ques_partag%C3%A9es
[wiki-partitions]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/P%C3%A9riph%C3%A9riques_et_syst%C3%A8mes_de_fichiers_Linux/Cr%C3%A9er_des_partitions_et_des_syst%C3%A8mes_de_fichiers
[wiki-filtres]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Ex%C3%A9cution_de_flux_de_textes_en_utilisant_des_filtres
[wiki-fichiers]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Gestion_de_base_des_fichiers
[wiki-redirections]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Utiliser_les_streams,_pipes,_et_redirections
[wiki-regex]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Expressions_r%C3%A9guli%C3%A8res

