---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: ZFS
layout: '@layouts/CoursePartLayout.astro'
---

## Présentation

ZFS (Zettabyte File System) a été développé par Sun Microsystems avec une approche radicalement différente des systèmes de fichiers traditionnels, à la fois **gestionnaire de volumes logiques** et **système de fichiers transactionnel**.

Objectifs principaux :

* intégrité des données de bout en bout
* simplicité d'administration
* scalabilité

Comparaison rapide :

* ext4 / XFS : FS uniquement, LVM séparé
* RAID matériel : opaque pour le FS
* ZFS : vision globale stockage + données

---

## Architecture

### zpool

Un **zpool** est l'unité de base de stockage ZFS.

* Agrégation de disques physiques ou virtuels
* Gestion de la redondance et des performances
* Un pool = un ou plusieurs _vdevs_

Types de _vdev_ :

* mirror
* raidz1 / raidz2 / raidz3

### Copy-on-Write (CoW)

ZFS n'écrase jamais les données en place :

* nouvelles données écrites ailleurs
* pointeurs mis à jour de manière atomique

Avantages :

* cohérence permanente
* snapshots instantanés

### Intégrité des données

* Checksum sur chaque bloc
* Détection automatique de corruption silencieuse
* Auto-réparation avec redondance

### ARC et L2ARC

* ARC : cache mémoire principal (RAM)
* L2ARC : cache secondaire (SSD)

---

## Objets

### Datasets

Un dataset est un système de fichiers ZFS :

* monté automatiquement
* propriétés configurables indépendamment : quota / reservation, compression, atime, …

### Zvols

Volumes blocs exposés comme des périphériques :

* machines virtuelles
* iSCSI

### Snapshots

* instantanés cohérents
* lecture seule
* consommation d'espace différentielle

### Clones

* snapshot rendu modifiable
* utilisé pour tests, environnements temporaires

---

## Réplication et sauvegarde

`zfs send` / `zfs receive` :

* réplication incrémentale
* sauvegarde distante efficace
* Cas d'usage :
  * PRA / PCA
  * sauvegarde hors site

---

## Scrub

* vérification proactive de l'intégrité
* planification recommandée

---

## Monitoring

* `zpool status`
* `zfs list`
* alertes SMART

---

## raid-z

* Implémentation de type RAID intégrée à ZFS, basée sur des **vdevs**.
* Remplace le RAID matériel et le couple RAID + LVM.

Principes clés :

* contrairement au RAID-5 classique, pas de risque de _write hole_ (écriture de données et de parité pas totalement terminée laissant le RAID dans un état incohérent sans moyen de le détecter),
* intégrité des données assurée par checksums,
* reconstruction fiable grâce au Copy-on-Write.
* Les données sont réparties en **stripes dynamiques**
* La parité n’est pas fixe (pas de disque dédié)
* ZFS sait **quels blocs sont valides** : reconstruction fiable
* Pas de lecture inutile lors du resilver

:::tip
Différence majeure avec RAID matériel : ZFS reconstruit uniquement les blocs réellement utilisés.
:::

:::warn
**RAID-Z n’est pas extensible disque par disque** : on ne peut pas ajouter un disque à un vdev RAID-Z existant.
:::

---

|                               | RAIDZ1           | RAIDZ2           | RAIDZ3           |
| ----------------------------- | ---------------- | ---------------- | ---------------- |
| **Parité**                    | 1                | 2                | 3                |
| **Pannes tolérées (disques)** | 1                | 2                | 3                |
| **Disques min.**              | 3                | 4                | 5                |
| **Capacité utile**            | `(N−1) * taille` | `(N−2) * taille` | `(N−3) * taille` |

---

* RAIDZ1 :
  * environnements non critiques
  * volumes de test ou pédagogiques
  * Déconseillé en production sur gros disques (>4 To)
* RAIDZ2 :
  * Équivalent RAID-6
  * serveurs de fichiers
  * sauvegardes
  * production standard
  * Recommandation actuelle par défaut.
* RAIDZ3 :
  * très gros pools
  * données critiques
  * reconstruction longue (gros disques)

---

### RAID-Z vs Mirror

| Critère              | RAIDZ         | Mirror              |
| -------------------- | ------------- | ------------------- |
| Tolérance de panne   | 1 à 3 disques | 1 disque par miroir |
| Performance lecture  | Bonne         | Excellente          |
| Performance écriture | Moyenne       | Excellente          |
| Resilver             | Lent          | Rapide              |
| Évolutivité          | Limitée       | Très bonne          |

:::tip
**Règle pratique** :

* **VM / bases de données** : mirror
* **stockage massif / sauvegarde** : raidz2

:::

---

:::link
Voir aussi : <https://forum.proxmox.com/threads/performance-comparison-between-zfs-and-lvm.124295/>
:::
