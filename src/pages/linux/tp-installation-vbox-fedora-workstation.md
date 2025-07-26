---
title: Installation de Fedora
date: 2023 / 2024
---

# Installation de Fedora en machine virtuelle VirtualBox

Nous allons installer une version Workstation (c'est-à-dire une version optimisée pour un usage personnel avec un environnement graphique, par opposition à une version serveur).

## Création de la machine virtuelle

1. Télécharger un média d'installation de Fedora (choisir `ISO For Intel and AMD x86_64 systems`) : <https://fedoraproject.org/workstation/download/>
2. Télécharger et installer VirtualBox **pour votre OS actuel** (en principe Windows ou MacOS) : <https://www.virtualbox.org/wiki/Downloads>
3. Lancer VirtualBox, cliquer sur _Nouvelle_ pour créer une nouvelle machine virtuelle
  + Choisir un nom pour la machine virtuelle
  + Allouer au moins 2048MB de mémoire
  + Choisir _Créer un disque_, choisir le type `VDI`, taille dynamique, et une taille d'au moins 10Gio. **Attention à bien placer ce fichier de disque virtuel à un endroit où vous ne le supprimerez pas !!!**.
4. La machine virtuelle est créée, mais avant de la lancer nous allons y ajouter le média d'installation :
  + Sélectionner la machine virtuelle
  + Cliquer sur _Configuration_ / _Stockage_
  + Cliquer sur l'image de CD-Rom : le panel _Lecteur optique_ devrait s'afficher dans la fenêtre.
  + Cliquer sur la nouvelle image de CD-Rom dans le panel _Lecteur optique_ intitulé _Choisissez un lecteur optique..._
  + Choisir _Choose a disk file_
  + Sélectionner le média et valider, quitter le menu de configuration

## Installation de la machine virtuelle

1. Sélectionner et Démarrer la machine virtuelle
2. Cliquer sur _Install Fedora_
3. Cliquer sur l'icône de disque dur, garder le partitionnement automatique, valider.
4. Lancer l'installation
5. À la fin de l'installation, cliquer en haut à droite pour faire apparaître le menu et étendre la machine.
6. Une fois la machine virtuelle éteinte, retirer le média d'installation (panel _Stockage_ de _Configuration_ utilisé à l'étape précédente).
  + Attention à ne pas retirer le disque dur mais bien le média d'installation (fichier `.iso` !)

## Premier démarrage

1. Démarrer la machine virtuelle, suivre l'assistant de configuration (activer les dépôts de logiciels tiers).
  + Fedora s'installe par défaut avec le gestionnaire de fenêtres `Gnome` (l'interface graphique la plus courante sous Linux).
2. Cliquez sur _Activité_ et cherchez et lancez l'application _Logiciels_. Mettre à jour le système.
  + Attention, la mise à jour peut être longue. Redémarrer le système si demandé.
3. Cliquez sur _Activité_ et cherchez _Terminal_ : ce sera (de loin) le programme le plus utilisé dans ce module.
4. Cliquer sur le menu _Machine_ de VirtualBox puis _Prendre un instantané_ : cela permet de faire une sauvegarde de cet état de la machine en cas d'erreur par la suite.

Votre machine virtuelle Fedora est prête à être utilisée !

## Additions invité

Les _additions invité_ permettent d'améliorer l'ergonomie de votre VM. VirtualBox va patcher le noyau Linux pour y installer ses drivers et permettre le copier-coller, une résolution adaptée à votre écran, …

Suivre le tutoriel : <https://lecrabeinfo.net/virtualbox-installer-les-additions-invite-guest-additions.html>

**Attention, les additions invité ont besoin des packages `bzip2` et `tar` qu'il faut installer avant**

```sh
sudo dnf install bzip2 tar
```

