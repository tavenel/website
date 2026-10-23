---
title: Disques, systèmes de fichiers Linux, arborescence de fichiers standard (FHS)
description: Disques, systèmes de fichiers Linux, arborescence de fichiers standard (FHS)
type: cours
sidebar:
  order: 6
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
---
## Création des partitions et des systèmes de fichiers

- Partition : morceau de disque physique
  - vu comme "disque" virtuel dans un OS.
  - Windows : `C:`, `D:`, ...
  - Linux : `/dev/hda1`, `/dev/sdb2`, ...
- Table de partition : stocke le schéma de partitionnement du disque

---

## Commandes

- `fdisk`, `gdisk` : gère le partitionnement
- `mkfs` : crée un filesystem (formatte une partition)
- Voir cours LPIC-1 section 104.1 _Create partitions and filesystems_ section _mkfs_ p.414
- Voir cours LPIC-1 section 104.1 _Create partitions and filesystems_ section _fdisk_ p.407 et _gdisk_ p.411
- Voir aussi la [wikiversité sur les partitions](https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/P%C3%A9riph%C3%A9riques_et_syst%C3%A8mes_de_fichiers_Linux/Cr%C3%A9er_des_partitions_et_des_syst%C3%A8mes_de_fichiers)
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

## Types de périphériques supportés

| Type      | Exemple de périphérique | Chemin dans `/dev`        |
| --------- | ----------------------- | ------------------------- |
| IDE       | Disques anciens         | `/dev/hdX`                |
| SATA/SCSI | HDD ou SSD modernes     | `/dev/sdX`                |
| NVMe      | SSD M.2/PCIe            | `/dev/nvmeXnY`            |
| iSCSI     | Stockage réseau         | `/dev/sdX` (via iscsiadm) |
| SAN       | FibreChannel, AoE, FCoE | dépend du protocole       |

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

## Maintenance de l'intégrité des systèmes de fichiers

- Voir cours LPIC-1 section _104.2 Maintain the integrity of filesystems_ p.439
- `du` : taille de fichiers
- `df` : espace libre partitions
- `fsck` : vérification de filesystem
- `tune2fs` : tuning d'un filesystem ext2
- Voir le TP dédié [tp-partitions][tp-partitions].

---

## Montage et démontage des systèmes de fichiers

- Windows : disques `C:`, `D:`, ...
- Unix : une partition se **monte** dans un **répertoire** (vide) quelconque
- `mount` (lit le contenu de `/proc/mounts`), `umount`
- `lsof <point montage ou device>` : programmes ayant des I/O ouverts sur le filesystem
- `/etc/fstab` : filesystem à monter (avec les options)
  + préférer identifier les disques par `UUID`

---

- Voir cours LPIC-1 section _104.3 Control mounting and unmounting of filesystems_ p.461
- Voir le TP dédié [tp-partitions][tp-partitions].

---

## Monter les disques avec `systemd`

- `systemd` peut gérer les points de montage à l'init
- fichiers `*.mount` dans `/etc/systemd/system/` :
  - `mnt-donnees.mount` pour `/mnt/donnees`
- Voir cours LPIC-1 section _104.3 Control mounting and unmounting of filesystems_ section _systemd_ p.470

---

## 🗂️ AutoFS - Montage automatique à la demande

- `/etc/auto.master` : fichier principal déclarant les points de montage.
- `/etc/auto.misc`, `/etc/auto.nfs`, etc. : fichiers secondaires avec les règles de montage.
- `systemctl status autofs` & `automount -v`

### 📌 Exemple : montage automatique d'un partage NFS

```
# /etc/auto.master

/mnt/nfs  /etc/auto.nfs
```

```
# /etc/auto.nfs
partage1  -fstype=nfs4  nfsserver:/srv/partage1
```

:::tip
Le partage sera monté automatiquement au moment de l'accès à `/mnt/nfs/partage1`.
:::

---

## 💿 ISO pour CD-ROM

- Types de filesystem :
  - _ISO9660_ : Format standard de CD-ROM
  - _UDF_ : Format pour les DVD
  - _HFS_ : Ancien format Mac
- Extensions utiles :
  - `-J` : _Joliet_ : compatibilité avec Windows (longs noms de fichiers).
  - `-R` : _Rock Ridge_ : ajoute les permissions UNIX.
  - `-b` : _El Torito_ : rend l'ISO amorçable (bootable).

### 🛠️ Création d'un ISO bootable avec `mkisofs`

```sh
mkisofs -o image.iso -b isolinux/isolinux.bin -c boot.cat -no-emul-boot -boot-load-size 4 \
  -boot-info-table -R -J -v -T ./dossier_source
```

---

## 🔐 dm-crypt & LUKS : Systèmes de fichiers chiffrés

### Création d'un volume chiffré avec LUKS


```sh
# 1. Initialiser le volume et le mapper :
cryptsetup luksFormat /dev/sdX
cryptsetup open /dev/sdX nom_volume

# 2. Système de fichiers :
mkfs.ext4 /dev/mapper/nom_volume
mount /dev/mapper/nom_volume /mnt/chiffre
```

```sh
# Fermeture du volume
umount /mnt/chiffre
cryptsetup close nom_volume
```

---

## LVM : Logical Volume Manager

- `Physical Volume PV` : disque physique (gère `RAID`, ...)
- `Volume Group VG` : pool de `PV`
- `Logical Volumes LVs` : découpage de `VG`
- Données gérées par unités (`extents`) : `PE` (`PV`) et `LE` (`LV`)
- les `LVs` peuvent être distribués sur plusieurs disques, gèrent chiffrement, ...
- `LV` accessible comme disque classique : `dev/VGNAME/LVNAME`

:::note
Pour des exemples d'utilisation, voir l'excellent wiki Archlinux : <https://wiki.archlinux.org/title/LVM>
:::

---

## Disques réseau : SAN

- Réseau dédié pour le stockage, haute performance.
- Protocoles :
  - **iSCSI** : basé IP, facile à déployer
  - **AoE (ATA over Ethernet)** : bas niveau, sans IP
  - **FCoE (Fibre Channel over Ethernet)** : haute vitesse, entreprise
- Identifiants de disque :
  - **WWN (World Wide Name)** : identifiant global
  - **WWID** : identifiant unique du disque
  - **LUN (Logical Unit Number)** : sous-unité dans un système SAN

---

### iSCSI (Internet SCSI)


| Commande      | Fonction                               |
| ------------- | -------------------------------------- |
| `iscsiadm`    | Gère les connexions iSCSI initiator    |
| `iscsid`      | Service iSCSI initiator                |
| `iscsid.conf` | Configuration (authentification, etc.) |
| `scsi_id`     | Identifie les disques via SCSI         |


```sh
iscsiadm -m discovery -t sendtargets -p 192.168.1.10
iscsiadm -m node --login
```

---

## 🔧 Utilitaires de réglage

### `hdparm`

Utilitaire pour configurer les disques IDE/SATA :

```sh
hdparm -I /dev/sda        # Affiche les infos du disque
hdparm -d1 /dev/sda       # Active le DMA
hdparm -tT /dev/sda       # Test de vitesse
```

:::caution
Les changements ne sont pas persistants. À automatiser via `/etc/hdparm.conf`.
:::

---

### `sdparm`

Utilitaire pour périphériques SCSI/SATA/SAS/USB :

```sh
sdparm --all /dev/sdX     # Affiche les paramètres
sdparm --set=WCE /dev/sdX # Active le cache d'écriture
```

---

### `nvme`

Pour les SSD NVMe :

```sh
nvme list                      # Affiche tous les périphériques NVMe
nvme id-ctrl /dev/nvme0        # Infos sur le contrôleur
nvme smart-log /dev/nvme0      # Affiche les données SMART
```

---

### `tune2fs`

Permet d'ajuster les paramètres des systèmes de fichiers ext4 :

```sh
tune2fs -l /dev/sdX1           # Affiche les réglages du FS
tune2fs -c 0 -i 0 /dev/sdX1    # Désactive les vérifications périodiques
```

---

### `fstrim`

Optimisation du TRIM pour SSD (libère les blocs inutilisés) :

```sh
fstrim -v /                   # TRIM manuel
```
---

## 📊 Analyse des ressources et IRQ (interruptions)

- Visualiser les interruptions :

```sh
cat /proc/interrupts
lspci -v
```

- Modifier un paramètre du noyau à chaud :

```sh
sysctl -w vm.dirty_ratio=20
```

Fichier de conf persistant : `/etc/sysctl.conf`

---

## 🔗 Liens

:::note
Pour plus d'information, voir le document de la formation LPIC-2 :

- [Operating The Linux Filesystem](https://lpic2book.github.io/src/lpic2.203.1/)
- [Maintaining a Linux Filesystem](https://lpic2book.github.io/src/lpic2.203.2/)
- [Creating And Configuring Filesystem Options](https://lpic2book.github.io/src/lpic2.203.3/)
- [Advanced Storage Device Administration](https://lpic2book.github.io/src/lpic2.204.0/)
- [Adjusting Storage Device Access](https://lpic2book.github.io/src/lpic2.204.2/)
- [Logical Volume Manager](https://lpic2book.github.io/src/lpic2.204.3/)
- [Configuring PCMCIA Devices](https://lpic2book.github.io/src/lpic2.204.4/)
:::

[tp-partitions]: /linux/tp-partitions

---

