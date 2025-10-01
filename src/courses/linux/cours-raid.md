---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: RAID logiciel
layout: '@layouts/CoursePartLayout.astro'
---

## 🚀 RAID

**RAID** (Redundant Array of Independent Disks) : technique de combinaison de plusieurs disques pour améliorer la **performance**, la **tolérance aux pannes** ou les deux.


| Type   | Description                                            | Nombre de disques | Nombre max de disques en erreur supportés |
| ------ | ------------------------------------------------------ | ---------------------- | ----------------------------------------- |
| RAID 0 | Répartition (striping) : rapide mais pas de redondance | 2                  | 0 |
| RAID 1 | Miroir (mirroring) : redondance complète               | 2                  | 1 |
| RAID 5 | Parité répartie : plus d'espace de stockage, moins de redondance | 3 ou plus          | 1 |


![RAID 1](@assets/linux/RAID_1.svg)

<div class="caption">RAID1. Source : https://commons.wikimedia.org/wiki/File:RAID_1.svg (CC-BY-SA).</div>

![RAID 5](@assets/linux/RAID_5.svg)

<div class="caption">RAID5. Source : https://en.wikipedia.org/wiki/File:RAID_5.svg (GFDL).</div>


| Outil/Fichier         | Rôle                                   |
| --------------------- | -------------------------------------- |
| `mdadm`               | Création et gestion des ensembles RAID |
| `/etc/mdadm.conf`     | Configuration persistante              |
| `/proc/mdstat`        | Surveillance de l'état du RAID         |
| `partition type 0xFD` | Type pour RAID autodétecté             |

:::link
Pour plus d'information, voir le document de la formation LPIC-2 :

- [Configuring RAID](https://lpic2book.github.io/src/lpic2.204.1/)
:::

---

## 🔧 Création d'un RAID logiciel

- Type de partition : `fd` (Linux RAID autodetect)
- Outil `mdadm` (option `--level` : type de RAID)
- Mettre à jour l'initramdisk
- Partition RAID (`/dev/md0`) utilisée avec un filesystem standard (_ext4_, …)

```sh
# Création du RAID
mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1

# Surveillance
mdadm --detail /dev/md0
mdadm --detail --scan >> /etc/mdadm/mdadm.conf
```

### Modifications

```sh
# Ajouter un disque
mdadm --add /dev/md0 /dev/sdd1

# Retirer un disque

mdadm --fail /dev/md0 /dev/sdc1
mdadm --remove /dev/md0 /dev/sdc1
```

### 🛑 Arrêt du RAID

```sh
umount /mnt/raid
mdadm --stop /dev/md0
mdadm --remove /dev/md0
```

---

