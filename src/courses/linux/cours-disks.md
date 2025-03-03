---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Disques, systèmes de fichiers Linux, arborescence de fichiers standard (FHS)
layout: '@layouts/CoursePartLayout.astro'
---

# 104.1 Création des partitions et des systèmes de fichiers

- Partition : morceau de disque physique
  - vu comme "disque" virtuel dans un OS.
  - Windows : `C:`, `D:`, ...
  - Linux : `/dev/hda1`, `/dev/sdb2`, ...
- Table de partition : stocke le schéma de partitionnement du disque

---

## Commandes

- `fdisk`, `gdisk` : gère le partitionnement
- `mkfs` : crée un filesystem (formatte une partition)
- Voir cours 104.1 _Create partitions and filesystems_ section _mkfs_ p.414
- Voir cours 104.1 _Create partitions and filesystems_ section _fdisk_ p.407 et _gdisk_ p.411
- Voir aussi la [wikiversité][wiki-partitions].
- Voir le TP dédié [tp-partitions][tp-partitions].

---

## MBR vs GPT

- `MBR` (_Master Boot Record_, _DOS_) : table de partition au début du disque.
  - disque < 2TB
  - <= 4 partitions primaires
- `GPT` (_GUID Partition Table_) : nouveau standard
  - en principe couplé à `UEFI`
  - beaucoup plus puissant : pas de limite de taille, de nombre de partitions, backups, ...

---

## ext2, ext3, ext4

- `ext2` est le système de fichiers historique sous Linux
  - `/boot` utilise encore souvent `ext2`
- amélioré avec `ext3` par la **journalisation**
- amélioré avec `ext4` (performance, ...)
- `ext3` et `ext4` sont aussi des filesystem `ext2` (mêmes commandes)

---

## btrfs

- ButterFS (`btrfs`) : alternative à `ext4` (Fedora, ...)
- supporte de nombreuses options similaires à `ZFS` (Oracle Solaris) :
  - `btrfs snapshot`
  - `btrfs subvolumes`
  - ...

---

## XFS

- Filesystem très performant optimisé gros fichiers, grandes partitions et CPU puissants (RedHat, ...)
- `xfs_repair`

---

## FAT / vFAT / exFAT

- `FAT` : Filesystem historique MS-DOS puis Windows
- extension `vFAT` : `FAT32`, ...
  - FAT32 : fichier <= 4GB
- `exFAT`
  - supporté dans presque tout OS.
  - très utilisé dans les supports externes (clé USB, ...)
  - grande taille de fichier possible

---

## swap

- Type de partition spéciale
- Déplace temporairement de la RAM sur disque pour augmenter virtuellement la RAM.

---

# 104.2 Maintenance de l'intégrité des systèmes de fichiers

- Voir cours _104.2 Maintain the integrity of filesystems_ p.439
- `du` : taille de fichiers
- `df` : espace libre partitions
- `fsck` : vérification de filesystem
- `tune2fs` : tuning d'un filesystem ext2
- Voir le TP dédié [tp-partitions][tp-partitions].

---

# 104.3 Montage et démontage des systèmes de fichiers

- Windows : disques `C:`, `D:`, ...
- Unix : une partition se **monte** dans un **répertoire** (vide) quelconque
- `mount` (lit le contenu de `/proc/mounts`), `umount`
- `lsof <point montage ou device>` : programmes ayant des I/O ouverts sur le filesystem
- `/etc/fstab` : filesystem à monter (avec les options)
  + préférer identifier les disques par `UUID`

---

- Voir cours _104.3 Control mounting and unmounting of filesystems_ p.461
- Voir le TP dédié [tp-partitions][tp-partitions].

---

## Monter les disques avec `systemd`

- `systemd` peut gérer les points de montage à l'init
- fichiers `*.mount` dans `/etc/systemd/system/` :
  - `mnt-donnees.mount` pour `/mnt/donnees`
- Voir cours _104.3 Control mounting and unmounting of filesystems_ section _systemd_ p.470

---

