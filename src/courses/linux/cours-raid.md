---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: RAID logiciel
layout: '@layouts/CoursePartLayout.astro'
---

## 🚀 RAID

**RAID** (Redundant Array of Independent Disks) : technique de combinaison de plusieurs disques pour améliorer la **performance**, la **tolérance aux pannes** ou les deux.


| Type   | Description                                            | Nombre min. de disques |
| ------ | ------------------------------------------------------ | ---------------------- |
| RAID 0 | Répartition (striping) : rapide mais pas de redondance | 2                      |
| RAID 1 | Miroir (mirroring) : redondance complète               | 2                      |
| RAID 5 | Parité répartie : bon compromis performance/sécurité   | 3                      |


| Outil/Fichier         | Rôle                                   |
| --------------------- | -------------------------------------- |
| `mdadm`               | Création et gestion des ensembles RAID |
| `/etc/mdadm.conf`     | Configuration persistante              |
| `/proc/mdstat`        | Surveillance de l'état du RAID         |
| `partition type 0xFD` | Type pour RAID autodétecté             |

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

