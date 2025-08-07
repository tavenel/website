---
title: TP - Rescue
date: 2024 / 2025
---

## 🎯 Objectif

Démarrer Linux depuis un Live CD / USB, puis utiliser le principe de _change root_ 

Apprendre à :
- Démarrer un système depuis un Live CD/USB
- Monter un système de fichiers existant
- Chrooter pour accéder à l'environnement endommagé 

## 📌 Scénario

Votre système Linux ne démarre plus correctement, par exemple :

- Le mot de passe root est inconnu
- Le chargeur de démarrage GRUB est corrompu
- Des fichiers critiques sont endommagés

Pour pouvoir accéder au système endommagé, nous utiliserons un _bind mount_ qui est une fonctionnalité du système de fichiers Linux qui permet de monter un répertoire existant à un autre endroit du système de fichiers (en le _liant_) tout en partageant exactement le même contenu, ainsi qu'un `chroot` (_change root_) qui est une commande Unix qui permet de changer le répertoire racine `/` pour un processus donné et ses processus enfants.

### Démarrage sur Live CD/USB

1. Insérez l'ISO de la distribution Live dans la VM (ou l'ordinateur physique).
2. Démarrez la machine et bootez depuis le Live CD (ou la clé USB).
3. Choisissez **"Try Ubuntu"** ou équivalent pour accéder à un terminal.

### Identifier les partitions du système endommagé

Dans le terminal Live :

```sh
lsblk
```

Repérez la partition principale (généralement /dev/sda1, /dev/vda1, etc.).

### Monter la partition racine

```sh
sudo mount /dev/sdXn /mnt

# Par exemple :
sudo mount /dev/sda1 /mnt
```

Puis montez les systèmes nécessaires pour le chroot :

```sh
sudo mount --bind /dev /mnt/dev
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
```

:::tip
Un _bind mount_ crée un alias d'un répertoire dans un autre chemin. Ce n'est pas une copie, mais une autre vue du même contenu.
:::

### Entrer dans l’environnement chrooté

```sh
sudo chroot /mnt
```

:::tip
`chroot` isole un processus dans un sous-ensemble du système de fichiers, comme s'il s’agissait de la racine `/`. Cela permet d'exécuter des commandes ou un environnement dans une "prison" système. C'est une des bases des technologies de conteneurs.
:::

:::tip
🔁 Vous êtes maintenant "dans" le système endommagé, mais via l'environnement Live (i.e. en utiliant le noyau démarré par le live CD / USB).

Exécuter les opérations de récupération nécessaires.
:::

### Quitter et démonter

```sh
exit
sudo umount /mnt/dev
sudo umount /mnt/proc
sudo umount /mnt/sys
sudo umount /mnt
```

Retirer l'ISO du lecteur virtuel ou physique et redémarrer la machine :

```sh
sudo reboot
```


