---
title: TP ZFS
date: 2024 / 2025
---

## Objectifs pédagogiques

* Expliquer l'architecture et les concepts fondamentaux de ZFS
* Concevoir un pool ZFS adapté à des besoins réels (performance, résilience, capacité)
* Administrer des systèmes de fichiers ZFS (datasets, snapshots, réplication)
* Mettre en œuvre des stratégies de sauvegarde et de restauration avec ZFS
* Diagnostiquer et corriger des incidents simples sur un pool ZFS

## Prise en main

:::exo

1. Installer les paquets ZFS
2. Lister les disques disponibles
3. Vérifier l'état du module ZFS

:::

:::tip
Les disques destinés à ZFS ne doivent contenir ni partition montée ni système de fichiers existant.
:::

:::correction

```bash
# Installation
apt update
apt install -y zfsutils-linux

# Identification des disques
lsblk
fdisk -l

# Vérification du module ZFS
lsmod | grep zfs
zfs version
```

:::

## Création d'un pool ZFS

Objectif : créer un pool résilient

:::exo

1. Créer un pool nommé `tank` en **raidz1**
2. Vérifier l'état du pool
3. Identifier le point de montage par défaut

:::

:::correction

### Création du pool `tank` en raidz1

```bash
zpool create tank raidz1 /dev/sdb /dev/sdc /dev/sdd /dev/sde
```

### Vérification de l'état du pool

```bash
zpool status

zpool list
```

### Point de montage

Par défaut, le pool est monté dans :

```bash
/tank
```

:::

## Gestion des datasets

Objectif : segmenter les usages

:::exo

1. Créer les datasets suivants :

   * tank/users
   * tank/backups
   * tank/vm
2. Activer la compression sur `tank/backups`
3. Définir un quota sur `tank/users`

:::

:::correction

### Création des datasets

```bash
zfs create tank/users
zfs create tank/backups
zfs create tank/vm
```

### Activation de la compression

```bash
zfs set compression=lz4 tank/backups
```

### Définition d'un quota

```bash
zfs set quota=100G tank/users
```

Vérification :

```bash
zfs list
zfs get compression,quota tank/users tank/backups
```

:::

## Snapshots et restauration

Objectif : protéger et restaurer des données

:::exo

1. Créer un snapshot de `tank/users`
2. Supprimer un fichier volontairement
3. Restaurer le fichier depuis le snapshot

:::

:::correction

### Création d'un snapshot

```bash
zfs snapshot tank/users@snap1
```

### Suppression volontaire

```bash
rm /tank/users/fichier_test
```

### Restauration du fichier

Méthode 1 => accès direct au snapshot :

```bash
cp /tank/users/.zfs/snapshot/snap1/fichier_test /tank/users/
```

Méthode 2 => rollback complet (destructif) :

```bash
zfs rollback tank/users@snap1
```

:::

## Scrub et supervision

Objectif : vérifier l'intégrité du stockage

:::exo

1. Lancer un scrub du pool
2. Interpréter la sortie de `zpool status`
3. Proposer une fréquence de scrub adaptée

:::

:::correction

### Lancement du scrub

```bash
zpool scrub tank
```

### Suivi du scrub

```bash
zpool status
```

### Fréquence recommandée

* Serveur critique : 1 fois par mois
* Serveur standard : tous les 2 à 3 mois
* Le scrub permet de détecter et corriger les corruptions silencieuses.

:::

## Sauvegarde distante

Objectif : mettre en œuvre une réplication

:::exo

1. Réaliser un snapshot
2. Transférer le dataset vers un second serveur
3. Vérifier la cohérence des données

:::

:::correction

### Snapshot pour réplication

```bash
zfs snapshot tank/users@backup1
```

### Envoi vers un serveur distant

```bash
zfs send tank/users@backup1 | ssh backup@serveur2 zfs receive backup_pool/users
```

### Vérification

Sur le serveur distant :

```bash
zfs list
zfs diff backup_pool/users@backup1
```

:::
