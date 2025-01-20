---
title: Installation d'Ubuntu
author: Tom Avenel
date: 2023 / 2024
---

# Installation d'Ubuntu en machine virtuelle VirtualBox

Nous allons installer une version Desktop (c'est-à-dire une version optimisée pour un usage personnel avec un environnement graphique, par opposition à une version serveur).

## Création de la machine virtuelle

1. Télécharger un média d'installation de Ubuntu (choisir la version `LTS`) : <https://ubuntu.com/download/desktop>
2. Télécharger et installer VirtualBox **pour votre OS actuel** (en principe Windows ou MacOS) : <https://www.virtualbox.org/wiki/Downloads>
3. Lancer VirtualBox, cliquer sur _Nouvelle_ pour créer une nouvelle machine virtuelle
  + Choisir un nom pour la machine virtuelle
  + Allouer au moins 2048MB de mémoire
  + Choisir _Créer un disque_, choisir le type `VDI`, taille dynamique, et une taille d'au moins 20Gio. **Attention à bien placer ce fichier de disque virtuel à un endroit où vous ne le supprimerez pas !!!**.
4. La machine virtuelle est créée, mais avant de la lancer nous allons y ajouter le média d'installation :
  + Sélectionner la machine virtuelle
  + Cliquer sur _Configuration_ / _Stockage_
  + Cliquer sur l'image de CD-Rom : le panel _Lecteur optique_ devrait s'afficher dans la fenêtre.
  + Cliquer sur la nouvelle image de CD-Rom dans le panel _Lecteur optique_ intitulé _Choisissez un lecteur optique..._
  + Choisir _Choose a disk file_
  + Sélectionner le média et valider, quitter le menu de configuration

## Installation de la machine virtuelle

1. Sélectionner et Démarrer la machine virtuelle
2. Cliquer sur _Installer Ubuntu_
3. Choisir _Installation minimale_
  + Cocher _Télécharger les mises à jour_
  + Cocher _Installer un logiciel tiers ..._
4. Choisir _Effacer le disque et installer Ubuntu_
5. Lancer l'installation
6. Configurer le système pendant l'installation
  + Ne pas cocher _Active Directory_
7. À la fin de l'installation, cliquer sur _Redémarrer_.

## Premier démarrage

1. Démarrer la machine virtuelle, suivre l'assistant de configuration.
  + Ubuntu s'installe par défaut avec le gestionnaire de fenêtres `Gnome` (l'interface graphique la plus courante sous Linux).
2. Cliquez sur _Activité_ et cherchez et lancez l'application _Ubuntu Software_. Mettre à jour le système.
  + Attention, la mise à jour peut être longue. Redémarrer le système si demandé.
3. Cliquez sur _Activité_ et cherchez _Terminal_ : ce sera (de loin) le programme le plus utilisé dans ce module.
4. Cliquer sur le menu _Machine_ de VirtualBox puis _Prendre un instantané_ : cela permet de faire une sauvegarde de cet état de la machine en cas d'erreur par la suite.

Votre machine virtuelle Ubuntu est prête à être utilisée !

## Additions invité

Les _additions invité_ permettent d'améliorer l'ergonomie de votre VM. VirtualBox va patcher le noyau Linux pour y installer ses drivers et permettre le copier-coller, une résolution adaptée à votre écran, …

Suivre le tutoriel : <https://lecrabeinfo.net/virtualbox-installer-les-additions-invite-guest-additions.html>

**Attention, les additions invité ont besoin des packages `bzip2` et `tar` qu'il faut installer avant**

```sh
sudo apt update && sudo apt install bzip2 tar
```

