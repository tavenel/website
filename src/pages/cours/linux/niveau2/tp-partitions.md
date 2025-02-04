---
title: TP - Gestion des partitions et des systèmes de fichiers
date: 2024 / 2025
correction: false
---

## Schéma de partitionnement

Ce TP a pour but de déterminer le meilleur schéma de partitionnement possible, ce qui représente la plus grande difficulté pour un débutant. Le TP convient pour toutes les distributions.

Vous disposez sur votre PC personnel d’un disque de 160 Go dont 40 sont déjà occupés par un autre système. Votre machine dispose de 2 Go de mémoire vive. Il vous reste 120 Go d’espace disque.

_Comment pouvez-vous les répartir, sachant que vous voulez séparer vos données du système ?_

1. Quelle doit être la taille de la partition d’échange SWAP ?

:::correction
La partition d’échange est utilisée lorsque Linux ne dispose plus d’assez de place en mémoire vive pour traiter toutes ses données. Les données sont déplacées en mémoire virtuelle sur cette partition d’échange pour libérer plus ou moins temporairement de la mémoire pour d’autres données. Votre système disposant de 2 Go de mémoire, vous pouvez ne prévoir que 2 Go de swap. Il reste alors 118 Go d’espace disque pour la suite.
:::

2. Quelle place réserver au système `/` ?

:::correction
Même si vous deviez installer tous les produits présents sur un DVD d’installation, le total n’atteindrait pas 10 Go. Mais deux choses doivent attirer votre attention : vous pouvez rajouter des produits issus d’autres sources (nouveaux dépôts, installation manuelle, etc.) par la suite, et les répertoires `/var` et `/tmp` peuvent être amenés à grossir.Disposant d’assez de place, pourquoi ne pas réserver 20 ou 30 Go à la racine ? Partez par exemple sur 20 Go. Il reste 98 Go.
:::

3. Quelle place réserver au `/home` ?

:::correction
La partition qui contient `/home` est celle qui contient vos données, ou celle des autres utilisateurs. C’est elle qui occupe le plus de place, entre les photos, la musique, les films, les documents de travail, etc. Réservez les 98 Go restants. Le disque est entièrement partitionné.
:::

4. Est-il utile de créer une partition étendue ?

:::correction
Vous avez trois partitions à créer sur le disque, en plus de celle qui existe déjà soit en tout quatre partitions. C’est le nombre exact pour prévoir quatre partitions primaires. Mais pensez que vous pouvez avoir besoin de réduire, supprimer ou recréer des partitions. Dans ce cas, la limite est déjà atteinte. Soyez prévoyant et créez une partition étendue où créer des partitions logiques.
:::

5. Quel est le schéma final du disque ?

:::correction
- Partition primaire 1 : l'OS déjà présent, 40 Go.
- Partition étendue :
  - Partition logique 1 : `/`, 20 Go.
  - Partition logique 2 : `/home`, 98 Go.
  - Partition logique 3 : swap, 2 Go.
  - Les 160 Go sont tous occupés.
:::


## Les disques et partitions

But : créer une partition et la faire reconnaître par le système. Attention l’opération peut être destructive !

1. Le premier disque a été entièrement partitionné par l'installation par défaut. Il est possible de modifier ce partitionnement mais l'opération est fastidieuse et risquée - nous allons donc travailler sur un 2e disque virtuel.
  - Éteindre la machine virtuelle.
  - Aller dans la configuration `VirtualBox`, onglet `Stockage`, sélectionner la ligne `Contrôleur SATA` et cliquer sur le bouton `Ajouter un disque dur` au bout de la ligne.
  - Créer un nouveau disque dur `VDI` (par exemple 20 Gio maximum - seule la taille réellement utilisée sera réquisitionnée, il n'est donc pas nécessaire d'avoir assez d'espace disque sur votre machine physique).
  - Valider et redémarrer la machine.
2. Notre système dispose désormais d'un nouveau disque dur disposant d’espace pour la création de nouvelles partitions.
  - Le 1er disque `SATA` (`/dev/sda`) dispose d'une table de partitions `GPT` (modèle par défaut des systèmes récents).
  - Créer une table de partitions au format historique `DOS` sur le 2e disque.
  - Créer 3 partitions primaires sur ce disque de 2 Gio.
  - Créer une partition étendue de 4 Gio. Pourquoi créer une partition étendue ?
  - Créer une nouvelle partition de 2 Gio : que remarque-t-on ? Pourquoi ?
  - Changer le type de cette partition en `vfat`.
  - Essayer de créer une nouvelle partition de 8 Gio : que remarque-t-on ? Pourquoi ?
  - Penser à écrire la table de partitions avant de quitter.
3. Forcez la mise à jour de la nouvelle table des partitions avec `partprobe`.
4. Vérifiez dans `/dev` la présence des fichiers de partitions du nouveau disque.

:::correction

Lancez `fdisk`. Le 2e disque `SATA` s'appelle `/dev/sdb` :

```
# fdisk /dev/sdb
```

- Listez les commandes de `fdisk` en appuyant sur `m`.
- Nouvelle table de partitions :
  - Créez une nouvelle table de partitions `DOS` en appuyant sur `o`.
- Partitions primaires (x3) :
  - Créez une nouvelle partition en appuyant sur `n`.
  - Créez une partition primaire en appuyant sur `p`.
  - Gardez le numéro de partition et le secteur de démarrage par défaut. Choisir une taille de `+2G`.
- Partition étendue :
  - Créez une nouvelle partition en appuyant sur `n`.
  - Créez une partition étendue en appuyant sur `e`.
  - Gardez le numéro de partition et le secteur de démarrage par défaut. Choisir une taille de `+4G`.
  - Il ne peut y avoir que 4 partitions "standard" dans une table de partitions DOS : si l'on ajoute une partition primaire, ce sera la dernière partition. Une partition étendue permet d'ajouter de nouvelles partitions dites _logiques_ à l'intérieur.
- Nouvelle partition de 2Gio :
  - Créer une partition comme précédemment - il n'est plus possible d'ajouter de partition primaire, le seul choix est donc d'ajouter une partition logique (sous-partition de la partition étendue).
 - Changer le type de cette partition en `FAT32 (LBA)` :
    * `t` pour changer le type (choisir la partition 5)
    * `L` affiche les codes des types de partitions
    * taper `0c`
    * Afficher la table de partitions : `p`
- Nouvelle partition de 8Gio :
  - Impossible : la partition logique est une sous-partition de la partition étendue de 4Gio, on ne peut donc pas y créer une partition logique de 8 Gio.
- Écriture sur disque :
  - Appuyer sur `w`.

3. Forcez la mise à jour de la nouvelle table des partitions avec `partprobe` :

```
# partprobe /dev/sdb
```

4. Vérifiez dans `/dev` la présence des fichiers de partitions du nouveau disque.

```
# ls -l /dev/sdb*
```
:::

## Création d’un système de fichiers Linux

But : créer et manipuler le système de fichiers dans `/dev/sdb1`. Attention cette opération est destructive.

1. Créez un système de fichiers de type `ext2` dans `/dev/sdb1`, sans options particulières.
2. En fin de compte, il fallait le créer en `ext3` pour profiter de la journalisation. Modifiez le système de fichiers pour qu’il soit maintenant en ext3.
3. La nouvelle partition va servir au stockage de diverses données. Attribuez-lui une étiquette (nom, label) : `BACKUP`.
4. Cherchez maintenant à connaître l’identifiant unique de système de fichiers, l'`UUID`, de votre nouveau système de fichiers. Utiliser deux méthodes :
  - Par `blkid`
  - Par `dumpe2fs`

:::correction
```
# #1.
# mkfs -t ext2 /dev/sdb1

---------------------------------------------------------

# #2.

# tune2fs -j /dev/sdb1

---------------------------------------------------------

# #3.
# e2label /dev/sdb1 BACKUP 

---------------------------------------------------------

# #4.
# blkid /dev/sdb1

527585d3-1e52-4aba-b7fc-70f18388458d

# dumpe2fs /dev/sdb1 | grep -i uuid

Filesystem UUID: 527585d3-1e52-4aba-b7fc-70f18388458d
```
:::

## Création d’un système de fichiers Windows

But : créer et manipuler le système de fichiers dans `/dev/sdb5`. Attention cette opération est destructive.

1. Créez un système de fichiers de type `vfat` dans `/dev/sdb5` :
  - fournir une option pour une taille `FAT` de 32
  - fournir une option pour un label `DONNEES`

:::correction
```
# mkfs -t vfat -F 32 -n DONNEES /dev/sdb5
## ou
# mkfs.vfat -F 32 -n DONNEES /dev/sdb5
```
:::

## Accès et montage des systèmes de fichiers

But : accéder aux nouveaux systèmes de fichiers créés.

1. Créez des répertoires qui serviront de points de montage aux nouveaux systèmes de fichiers.
2. Montez les système de fichiers, par leurs noms de périphériques, dans le répertoire de montage correspondant.
3. Déplacez-vous dans chaque point de montage et créez un fichier quelconque.
4. Sortez de ce répertoire (`cd`) et démontez le système de fichiers.
5. Rajoutez 2 lignes dans `/etc/fstab` pour pouvoir monter ces système de fichiers automatiquement, par leur label.
  - on choisira comme options : `defaults 0 0`.
  - exécuter la commande `systemctl daemon-reload` pour recharger `/etc/fstab`.
6. Montez le système de fichiers simplement depuis le nom de son point de montage.

:::correction
```
# #1.
# mkdir /mnt/backup /mnt/donnees

---------------------------------------------------------

# #2.
# mount -t ext3 /dev/sdb1 /mnt/backup
# mount -t vfat /dev/sdb5 /mnt/donnees

---------------------------------------------------------

# #3.
# cd /mnt/backup && touch toto
# cd /mnt/donnees && touch toto

---------------------------------------------------------

# #4.
# umount /mnt/backup /mnt/donnees

---------------------------------------------------------

# #5.
# #Les lignes sont :
# LABEL=BACKUP /mnt/backup ext3 defaults 0 0
# LABEL=DONNEES /mnt/donnees vfat defaults 0 0

---------------------------------------------------------

# #6.
# mount -L BACKUP
# mount -L DONNEES
```
:::

## Statistiques et entretien du système de fichiers 

But : obtenir des informations sur l’occupation du système de fichiers et le réparer si besoin. 

1. Regardez l’état d’occupation de vos systèmes de fichiers, de manière lisible pour un humain.
2. Le système de fichiers pointant sur `/home` semble bien occupé. Il s’agit de déterminer ce qui peut occuper autant de place. Déterminez l’occupation de chaque fichier et répertoire.
3. Le résultat est trop long. Triez la sortie de manière à obtenir les plus grosses occupations en dernier.
4. Un répertoire monté sur `/mnt/backup` (TP précédent) a des problèmes : il semble que le contenu d’un répertoire soit corrompu : noms de fichiers et tailles farfelues. Vérifiez et réparez ce système de fichiers.
5. Forcez une vérification de ce système de fichiers au prochain redémarrage.
  - L'astuce pour cela est de changer artificiellement le nombre de montages avec `tune2fs` (par exemple à `1000`).
6. Quelle est la commande permettant de mettre votre disque dur en mode lecture seule ?
  - Il vous faudra peut-être installer le package `hdparm` :
    - `sudo apt install hdparm`
    - `sudo dnf install hdparm`
7. Quelle est la commande permettant d'activer/désactiver le cache d’un disque dur ?

:::correction
1. Regardez l’état d’occupation de vos systèmes de fichiers, de manière lisible pour un humain.

```
# df -H
```

2. Le système de fichiers pointant sur `/home` semble bien occupé. Il s’agit de déterminer ce qui peut occuper autant de place. Déterminez l'occupation de chaque fichier et répertoire.

```
# du -m /home 
```

3. Le résultat est trop long. Triez la sortie de manière à obtenir les plus grosses occupations en dernier.

```
# du -m | sort -n 
```

4. Un répertoire monté sur `/mnt/backup` (TP précédent) a des problèmes : il semble que le contenu d’un répertoire soit corrompu : noms de fichiers et tailles farfelues. Vérifiez et réparez ce système de fichiers.

```
# cd 
# umount /mnt/backup 
# fsck /dev/sdb1
```

5. Forcez une vérification de ce système de fichiers au prochain redémarrage.

```
# tune2fs -C 1000 /dev/sdb1
```

6. Quelle est la commande permettant de mettre votre disque dur en mode lecture seule ?

```
# Lecture du paramètre
hdparm -r /dev/sdb

# Mise en lecture seule
hdparm -r 1 /dev/sdb
```

7. Quelle est la commande permettant d'activer/désactiver le cache d’un disque dur ?

```
# Lecture du paramètre
hdparm -W /dev/sdb

# Désactivation du cache
hdparm -W 0 /dev/sdb
```
:::

## Swap et mémoire 

But : gérer le swap et la mémoire. 

1. Sur une machine donnée, le bilan mémoire se présente ainsi, qu'en déduisez-vous ? 

    ```
    # free 
           total      used    free  shared   buffers   cached 
    Mem: 2060680   2011224   49456       0    170628   958508 
    -/+ buffers/cache:  882088  1178592
    Swap:      2104472    1296  2103176
    ```

2. Vérifiez le nom de la partition contenant le ou les espaces de swap.
3. Le swap sur cette machine, à ce niveau de charge, est probablement inutile. Désactivez- le. 
4. Quelques instants plus tard, vous devez charger une application lourde de traitement d'image qui va énormément consommer de mémoire. Rechargez l'intégralité des zones de swap.

:::correction
1. Sur une machine donnée, le bilan mémoire se présente ainsi, qu'en déduisez-vous ? 

```
# free 
       total      used    free  shared   buffers   cached 
Mem: 2060680   2011224   49456       0    170628   958508 
-/+ buffers/cache:  882088  1178592
Swap:      2104472    1296  2103176
```

La machine dispose de 2 Go de mémoire vive, et de 2 Go de swap.

Bien qu’indiquant environ 48 Mo de mémoire libre, il y a environ 950 Mo de mémoire cache et 160 Mo de tampon. Soit potentiellement environ 1 Go de mémoire à libérer. 

2. Vérifiez le nom de la partition contenant le ou les espaces de swap.

Un man de `swapon` indique que l’information peut être trouvée dans `/proc/swaps` : 

```
# cat /proc/swaps 
Filename    Type        Size     Used   Priority 
/dev/zram0   partition   2104472  1336   -1 
```

On remarque ici une partition étrange : `/dev/zram0`. Un swap "classique" s'effectue sur une partition standard de type `swap` (par exemple, `/dev/sda5`). Le type `zram` est en fait une compression de la mémoire RAM : si la RAM vient à manquer, alors une partie de celle-ci est compressée puis envoyée en swap… dans la RAM (et non sur disque).

3. Le swap sur cette machine, à ce niveau de charge, est probablement inutile. Désactivez- le. 

```
# swapoff /dev/zram0 
```

4. Quelques instants plus tard, vous devez charger une application lourde de traitement d'image qui va énormément consommer de mémoire. Rechargez l'intégralité des zones de swap.

```
# swapon -a 
```
:::


## Quotas

But : mettre en place des quotas. 

1. Modifiez avec `vi` la ligne rajoutée dans `/etc/fstab` pour le filesystem `BACKUP` au TP _Accès et montage du système de fichiers_ pour activer les quotas utilisateur et remontez le système de fichiers.
  - on pourra utiliser les quotas classiques : `usrquota`
  - ou (mieux) les quotas journalisés : `usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vsfv0`
2. Créez et activez les quotas. 
3. Placez une limite globale de 150 Mo à votre utilisateur (utiliser `edquota`). 

:::tip
Voir aussi :

- <https://doc.ubuntu-fr.org/quota>
- <https://www.linuxtricks.fr/wiki/gestion-des-quotas-sous-linux-ext4-xfs>
:::

:::correction
1. Modifiez avec `vi` la ligne rajoutée dans `/etc/fstab` au TP _Accès et montage du système de fichiers_ pour activer les quotas utilisateur et remontez le système de fichiers.

Dans `/etc/fstab` : 

```
LABEL=BACKUP /mnt/backup ext3 defaults,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vsfv0 0 0 
```

puis : 

```
# systemctl daemon-reload
# mount -o remount -L BACKUP
```

2. Créez et activez les quotas. 

```
# quotacheck /mnt/backup 
# quotaon /mnt/backup 
```

3. Placez une limite globale de 150 Mo à votre utilisateur : 

```
# edquota tom 
```

Puis inscrivez la valeur `153600` (en octets) en `hard` et `soft`, et sauvez.
:::

## Version graphique

Il existe de nombreux autres outils pour gérer les disques, les partitions et les systèmes de fichiers :

- `parted` en ligne de commandes
- `gparted` (Gnome) est l'un des outils graphiques les plus populaires
