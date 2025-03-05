---
title: TP - Les fichiers
date: 2024 / 2025
correction: false
---

:::tip
Voir cours LPIC-1 section _Manipulating Files_, 103.3 Lesson 1 p.227
:::

## Types de fichiers

La commande `ls -l` affiche le type d'un fichier :

```console
$ ls -l
drwxr-xr-x - root 30 Aug 14:30 /etc/
```

Le premier symbole indique la nature du fichier :

- `-` : fichier classique
- `d` : dossier
- `l` : lien **symbolique**
- `c` : périphérique de type caractère
- `b` : périphérique de type bloc
- `p` : pipe (tube, tuyau ou file d'attente)
- `s` : socket

## Commandes utiles

- `cp` (copy) : Cette commande est utilisée pour copier des fichiers ou des répertoires d'un emplacement à un autre.
- `find` : La commande find est utilisée pour rechercher des fichiers et des répertoires dans une hiérarchie de répertoires en fonction de différents critères tels que le nom, la taille, la date de modification, etc.
- `mkdir` (make directory) : Cette commande permet de créer un nouveau répertoire (dossier) dans le système de fichiers.
- `mv` (move) : La commande mv est utilisée pour déplacer ou renommer des fichiers et des répertoires.
- `ls` (list) : Cette commande est utilisée pour afficher la liste des fichiers et répertoires dans un répertoire donné.
- `rm` (remove) : La commande rm est utilisée pour supprimer des fichiers et des répertoires du système de fichiers. Elle peut être utilisée avec des options pour supprimer de manière récursive (`-r`) et interactive (`-i` pour une confirmation).
- `rmdir` (remove directory) : Cette commande permet de supprimer des répertoires vides du système de fichiers.
- `touch` : La commande touch est utilisée pour créer un nouveau fichier vide ou mettre à jour la date de modification d'un fichier existant.
- `tar` : Cette commande est utilisée pour créer, afficher ou extraire des archives `tar`, qui sont des regroupements de fichiers et de répertoires compressés.
- `cpio` : La commande cpio est utilisée pour copier des fichiers dans ou depuis une archive `cpio`, un format d'archivage couramment utilisé sur les systèmes Unix.
- `dd` : La commande dd est utilisée pour copier et convertir des fichiers et des données en utilisant des blocs de taille fixe. Elle est souvent utilisée pour la création de copies exactes de disques.
- `file` : Cette commande permet de déterminer le type de fichier en se basant sur son contenu, en identifiant son format et ses caractéristiques.
- `gzip`, `gunzip`, `bzip`, `bzip2` : Les commande `gzip`, `gunzip`, `bzip2`, `bunzip2` sont utilisées pour (dé)compresser des fichiers en utilisant l'algorithme de compression gzip/bzip2.

## Travaux pratiques sur les fichiers

### Commande cp

Objectif : Copier un fichier dans un répertoire spécifique.

1. Créez un fichier vide nommé `fichier_source.txt` dans votre répertoire personnel.
1. Créez un répertoire nommé `nouveau_repertoire` dans votre répertoire personnel.
1. Utilisez la commande `cp` pour copier `fichier_source.txt` dans le répertoire `nouveau_repertoire`.
1. Vérifiez que le fichier a été copié avec succès dans le répertoire en utilisant la commande `ls`.
1. Supprimez le fichier copié du répertoire `nouveau_repertoire` en utilisant la commande `rm`.

### Commande mkdir

Objectif : Créer une structure de répertoires.

1. Créez un répertoire principal nommé `Dossier_Principal` dans votre répertoire personnel.
1. À l'intérieur de `Dossier_Principal`, créez trois sous-répertoires nommés `Repertoire_A`, `Repertoire_B` et `Repertoire_C`.
1. Utilisez la commande `ls` pour vérifier que les répertoires ont été créés avec succès.
1. Supprimez le répertoire `Repertoire_C` en utilisant la commande `rmdir`.
1. Utilisez `ls` à nouveau pour vérifier que le répertoire `Repertoire_C` a été supprimé.

### Commande mv

Objectif : Déplacer et renommer des fichiers.

1. Créez un fichier nommé `fichier_original.txt` dans votre répertoire personnel.
1. Utilisez la commande `mv` pour le renommer en `fichier_renomme.txt`.
1. Vérifiez que le fichier a été renommé avec succès en utilisant la commande `ls`.
1. Créez un répertoire nommé `Repertoire_Mouvement` dans votre répertoire personnel.
1. Utilisez la commande `mv` pour déplacer `fichier_renomme.txt` dans `Repertoire_Mouvement`.
1. Vérifiez que le fichier a été déplacé dans le répertoire en utilisant la commande `ls`.

### Commande find

Objectif : Rechercher tous les fichiers avec une extension spécifique dans un répertoire.

1. Créez plusieurs fichiers dans votre répertoire personnel avec différentes extensions (par exemple, `.txt`, `.jpg`, `.log`, `.csv`, etc.).
1. Utilisez la commande `find` pour rechercher tous les fichiers avec l'extension `.txt` dans votre répertoire personnel.

### Commande file

Objectif : Identifier le type de fichier.

1. Identifier le type du fichier `/etc/passwd`.
1. Identifier le type du fichier `/dev/sda1`.
1. Identifier le type du fichier `/proc/1/fd/1`.
1. Identifier le type du fichier `/tmp/`.
1. Retrouver les mêmes résultats avec la commande `ls`.

:::correction
```console
$ file /etc/passwd
/etc/passwd: ASCII text

$ ls -l /etc/passwd
-rw-r--r--    1 root     root          1752 Aug 29 11:53 /etc/passwd

# Le 1er caractère `-` indique un fichier texte standard.

---------------------------------------------------------

$ file /dev/sda1
/dev/sda1: block special (8/1)

$ ls -l /dev/sda1  
brw-rw----    1 root     disk        8,   1 Sep 18 17:29 /dev/sda1

# Le 1er caractère `b` indique un fichier de type block.

---------------------------------------------------------

$ file /proc/1/fd/1
/proc/1/fd/1: symbolic link to /dev/console (deleted)

$ ls -l /proc/1/fd/1
lrwx------    1 root     root            64 Sep 19 23:34 /proc/1/fd/1 -> /dev/console (deleted)

# Le 1er caractère `l` indique un lien symbolique. La cible est /dev/console.

---------------------------------------------------------

$ file /tmp
/tmp: sticky, directory

$ ls -ld /tmp
drwxrwxrwt   11 root     root          1700 Sep 19 23:58 /tmp

# Le 1er caractère `d` indique un dossier.
```
:::

### Compression et décompression

#### Commandes gzip et bzip2

Objectif : Compresser et décompresser des fichiers avec `gzip` et `bzip2`.

1. Créez un fichier texte nommé `fichier_texte.txt` contenant du texte.
1. Utilisez la commande `gzip` pour compresser `fichier_texte.txt` en un fichier `gzip` nommé `fichier_texte.gz`.
1. Vérifiez que `fichier_texte.gz` a été créé.
1. Utilisez la commande `gunzip` pour décompresser `fichier_texte.gz` en un fichier texte nommé `fichier_texte_decompresse.txt`.
1. Vérifiez que le fichier décompressé contient le même contenu que l'original en utilisant la commande `diff`.
1. Mêmes questions pour les commandes `bzip2` et `bunzip2`.

#### Commande tar

Objectif : Créer une archive `tar`.

1. Créez trois fichiers vides nommés `fichier1.txt`, `fichier2.txt` et `fichier3.txt` dans votre répertoire personnel.
1. Utilisez la commande `tar` pour créer une archive `tar` nommée `archive.tar` contenant ces trois fichiers.
1. Vérifiez que l'archive a été créée avec succès en utilisant la commande `tar -tf archive.tar` pour lister son contenu.
1. Ajoutez un fichier supplémentaire nommé `fichier4.txt` à l'archive en utilisant la commande `tar -rf archive.tar fichier4.txt`.
1. Affichez à nouveau le contenu de l'archive pour vérifier que `fichier4.txt` a été ajouté.

#### Commande cpio

Objectif : Créer une archive `cpio`.

1. Créez deux fichiers vides nommés `document1.txt` et `document2.txt` dans votre répertoire personnel.
1. Utilisez la commande `find` pour rechercher ces deux fichiers et _pipez_ le résultat vers la commande `cpio` pour créer une archive cpio nommée `archive.cpio`.
1. Vérifiez que l'archive a été créée avec succès en utilisant la commande `cpio -t < archive.cpio` pour lister son contenu.
1. Créez un répertoire vide nommé `repertoire_cible` dans votre répertoire personnel.
1. Utilisez la commande `cpio` pour extraire le contenu de `archive.cpio` dans le répertoire `repertoire_cible`.

#### Commande dd

Objectif : Copier des données d'un fichier source vers un fichier de destination.

**Attention : la commande `dd` est très puissante mais permet d'écrire de n'importe quel fichier source vers n'importe quel fichier de destination, y compris le fichier représentant la partition racine ! `dd` peut d'ailleurs être utilisé pour faire des copies simples d'un disque.**

Instructions :

1. Créez un fichier texte de plusieurs lignes et nommez-le `source.txt`.
1. Utilisez la commande `dd` pour copier le contenu de `source.txt` vers un nouveau fichier nommé `destination.txt`.
1. Vérifiez que `destination.txt` contient le même contenu que `source.txt` en utilisant la commande `diff` pour comparer les fichiers.

:::correction

```sh
# Commandes gzip et bzip2

gzip fichier_texte.txt

gunzip fichier_texte.gz

bzip2 texte_a_compresser.txt

bunzip2 texte_compresse.bz2

---------------------------------------------------------

# Commande tar

tar -cf archive.tar fichier_source.txt nouveau_repertoire

tar -tf archive.tar

tar -rf archive.tar fichier4.txt

tar -tf archive.tar

---------------------------------------------------------

# Commande cpio

find . -name "document*.txt" | cpio -o > archive.cpio

cpio -t < archive.cpio

cpio -i < archive.cpio -d -v

---------------------------------------------------------

# Commande dd

dd if=source.txt of=destination.txt
```
:::
