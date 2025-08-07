---
title: TP Sauvegarde et Restauration sous Linux
date: 2025 / 2026
---

## 🎯 Objectifs

- Comprendre et mettre en oeuvre différentes méthodes de sauvegarde d'un système Linux
- Utiliser les outils classiques (`tar`, `rsync`, `dump/restore`)
- Découvrir des outils plus avancés (`partimage`, `mondorescue`, `BackupPC`)
- Tester la restauration de fichiers et de systèmes complets

## 📋 Prérequis

- Une machine virtuelle Linux (Debian ou Ubuntu)
- Un disque supplémentaire ou un répertoire de sauvegarde (`/mnt/backup`)
- Les paquets suivants installés : `rsync`, `partimage`, `dump`, `nfs-common`, `nfs-kernel-server`, `mondorestore`, `mondo`, `backuppc`

## 🗃️ Partie 1 — Sauvegardes classiques

### 🔹 1. Sauvegarde avec `tar`

1. Créer un dossier `/home/testuser` avec des fichiers à sauvegarder.
2. Archiver le dossier dans `/mnt/backup/testuser.tar.gz`

:::correction
```sh
sudo tar -czvf /mnt/backup/testuser.tar.gz /home/testuser
````
:::

3. Supprimer le dossier, puis le restaurer depuis l'archive.

:::correction
```sh
sudo rm -rf /home/testuser
sudo tar -xzvf /mnt/backup/testuser.tar.gz -C /
```
:::

### 🔹 2. Sauvegarde avec `rsync`

1. Lancer une sauvegarde incrémentale du dossier `/etc` vers `/mnt/backup/etc_bak`

:::correction
```sh
sudo rsync -av --delete /etc/ /mnt/backup/etc_bak/
```
:::

2. Modifier un fichier dans `/etc`, relancer `rsync` et observer les différences.

### 🔹 3. Sauvegarde de partition avec `dump/restore`

:::warn
Utilisable uniquement sur des partitions ext3/ext4
:::

1. Identifier la partition racine (ex: `/dev/sda1`) :

```sh
df -h /
```

2. Lancer une sauvegarde avec la commande `dump`.

:::correction
```sh
sudo dump -0u -f /mnt/backup/root.dump /
```
:::

3. Restaurer avec `restore` (⚠️ à faire sur un système de test ou partition montée)

:::correction
```sh
sudo restore -rf /mnt/backup/root.dump
```
:::

## 💾 Partie 2 — Sauvegardes d'images système

### 🔹 4. Sauvegarde avec `partimage`

1. Lister les partitions :

```sh
sudo fdisk -l
```

2. Lancer `partimage` en mode TUI :

```sh
sudo partimage
```

3. Sauvegarder la partition `/dev/sda1` dans `/mnt/backup/root_sda1.img`
4. Tester la restauration (⚠️ sur VM clone ou partition montée).

### 🔹 5. Sauvegarde avec `mondorescue`

1. Installer `mondo` :

```sh
sudo apt install mondo
```

2. Lancer l'outil graphique ou la commande :

```sh
sudo mondoarchive
```

3. Créer une image ISO du système dans `/mnt/backup`.
4. Simuler une restauration avec `mondorestore`.

## 🌐 Partie 3 — Sauvegarde centralisée avec BackupPC

### 🔹 6. Installation de BackupPC (sur une autre VM ou localhost)

1. Installation du paquet :

```sh
sudo apt install backuppc
```

2. Accès à l'interface web, par défaut sur <http://localhost/backuppc>
3. Configurer une machine cliente via SSH pour la sauvegarde.
4. Lancer une sauvegarde à distance d'un répertoire `/etc`.
5. Restaurer un fichier depuis l'interface.

