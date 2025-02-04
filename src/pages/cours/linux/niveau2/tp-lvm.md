---
title: TP LVM
date: 2024 / 2025
correction: false
---

## Contexte

Vous êtes administrateur système d'une entreprise. Un serveur Linux contient plusieurs disques non alloués, et vous devez configurer le stockage pour répondre aux besoins suivants :

1. Créer une partition pour les données des utilisateurs.
2. Mettre en place un système évolutif grâce à LVM.
3. Ajouter de l'espace disque lorsque les besoins augmentent.

### Matériel nécessaire

- Une machine virtuelle ou un serveur physique avec au moins 2 disques additionnels non alloués.
- Un accès root ou un utilisateur avec des droits sudo.
- Distribution Linux (Debian, Ubuntu, CentOS ou autre compatible avec LVM).

## Préparation de l'environnement

Connectez-vous au serveur Linux avec un utilisateur ayant les droits administrateurs.

Listez les disques disponibles pour vérifier l'espace libre :

```sh
lsblk
fdisk -l
```

Identifiez deux disques vides, par exemple `/dev/sdb` et `/dev/sdc`.

## Initialisation des disques pour LVM

1. Créez une table de partition GPT sur chaque disque.
2. Créez une partition unique sur chaque disque.
3. Marquez les partitions comme utilisables par LVM grâce à `pvcreate`.

```sh
# En utilisant fdisk :
fdisk /dev/sdb
# Tapez `n` pour créer une nouvelle partition.
# Choisissez `p` pour une partition primaire.
# Acceptez les valeurs par défaut pour le numéro de partition, le premier secteur, et le dernier secteur (pleine capacité).
# Tapez `t` pour définir le type de partition. Entrez le code `8e` (type `LVM`).
# Tapez `w` pour enregistrer les modifications sur le disque

# En utilisant parted :
parted /dev/sdb -- mklabel gpt
parted /dev/sdb -- mkpart primary 0% 100%

# Utilisation de LVM
pvcreate /dev/sdb1
pvcreate /dev/sdc1
```

## Création d’un groupe de volumes

1. Créez un groupe de volumes nommé `vg_data` à partir des partitions initialisées.
2. Vérifiez le groupe de volumes créé en l'affichant.
 
```sh
vgcreate vg_data /dev/sdb1 /dev/sdc1
vgdisplay
```

## Création de volumes logiques

1. Créez un volume logique nommé `lv_users` de 10 Go à partir de `vg_data`
2. Formatez le volume avec un système de fichiers `ext4`
3. Montez le volume dans `/mnt/users`
4. Ajoutez une entrée dans `/etc/fstab` pour un montage automatique au démarrage.

```sh
lvcreate -L 10G -n lv_users vg_data

mkfs.ext4 /dev/vg_data/lv_users

mkdir -p /mnt/users
mount /dev/vg_data/lv_users /mnt/users

echo '/dev/vg_data/lv_users /mnt/users ext4 defaults 0 2' >> /etc/fstab
```

## Extension d’un volume logique

1. Simulez une augmentation des besoins en espace disque en ajoutant un nouveau disque `/dev/sdd`.
2. Initialisez le disque pour LVM.
3. Ajoutez le nouveau disque au groupe de volumes `vg_data`
4. Augmentez la taille du volume logique `lv_users` de 5 Go.
5. Redimensionnez le système de fichiers sans démonter le volume.
6. Vérifiez la taille du volume logique et du système de fichiers :

```sh
# Voir partie 1 pour fdisk ou parted

pvcreate /dev/sdd1

vgextend vg_data /dev/sdd1

lvextend -L +5G /dev/vg_data/lv_users

resize2fs /dev/vg_data/lv_users

lvdisplay /dev/vg_data/lv_users
df -h /mnt/users
```


:::correction
# Correction

## Initialisation des disques pour LVM

```sh
# En utilisant fdisk :
fdisk /dev/sdb
# Tapez `n` pour créer une nouvelle partition.
# Choisissez `p` pour une partition primaire.
# Acceptez les valeurs par défaut pour le numéro de partition, le premier secteur, et le dernier secteur (pleine capacité).
# Tapez `t` pour définir le type de partition. Entrez le code `8e` (type `LVM`).
# Tapez `w` pour enregistrer les modifications sur le disque

# En utilisant parted :
parted /dev/sdb -- mklabel gpt
parted /dev/sdb -- mkpart primary 0% 100%

# Utilisation de LVM
pvcreate /dev/sdb1
pvcreate /dev/sdc1
```

## Création d’un groupe de volumes

```sh
vgcreate vg_data /dev/sdb1 /dev/sdc1
vgdisplay
```

## Création de volumes logiques

```sh
lvcreate -L 10G -n lv_users vg_data

mkfs.ext4 /dev/vg_data/lv_users

mkdir -p /mnt/users
mount /dev/vg_data/lv_users /mnt/users

echo '/dev/vg_data/lv_users /mnt/users ext4 defaults 0 2' >> /etc/fstab
```

## Extension d’un volume logique

```sh
# Voir partie 1 pour fdisk ou parted

pvcreate /dev/sdd1

vgextend vg_data /dev/sdd1

lvextend -L +5G /dev/vg_data/lv_users

resize2fs /dev/vg_data/lv_users

lvdisplay /dev/vg_data/lv_users
df -h /mnt/users
```
:::
