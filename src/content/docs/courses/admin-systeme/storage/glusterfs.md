---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: GlusterFS - Système de fichiers distribué
type: cours
sidebar:
  order: 4
description: GlusterFS - Système de fichiers distribué
---
## GlusterFS

- Système de fichiers distribué open-source
- Permet d'agréger plusieurs serveurs de stockage en un volume unique
- Utilisé pour :
  - stockage distribué
  - haute disponibilité
  - scalabilité horizontale
  - infrastructures cloud / Kubernetes

### 🔑 Concepts clés

- **Scale-out** : Ajout de nœuds sans interruption
- **Volume** : Espace de stockage logique
- **Brick** : Répertoire exporté par un serveur
- **Trusted Storage Pool** : Ensemble des nœuds Gluster

---

### Fonctionnalités avancées

- 🔁 **Réplication** :
  - Synchronisation automatique entre bricks
  - Protection contre panne disque/nœud
- ⚖️ **Auto-healing** :
  - Reconstruction automatique des données
  - Déclenchée lors de reconnexion d'un nœud
- 📊 **Load balancing** :
  - Répartition dynamique des fichiers

---

### Cas d'usage

- Stockage partagé pour VM
- Backend pour conteneurs
- Serveurs web (shared content)
- Big Data (alternative légère)

---

### Limites

- Moins performant que Ceph
- Split-brain en réplication
- Complexité debug

---

## Architecture

GlusterFS fonctionne sans métadonnées centralisées (contrairement à Ceph ou HDFS).

### 🔧 Composants

- **Serveur (glusterd)** : gestion des volumes
- **Client** :
  - FUSE (montage classique)
  - NFS (optionnel)
- **Brick** : unité de stockage (dossier)

### 📐 Schéma logique

```
Client → Volume → Bricks → Serveurs
```

### Types de volumes

| Type                   | Description              | Cas d'usage           |
| ---------------------- | ------------------------ | --------------------- |
| Distributed            | Répartition des fichiers | Scalabilité           |
| Replicated             | Réplication des données  | HA                    |
| Distributed-Replicated | Mix des deux             | Prod                  |
| Dispersed              | Erasure coding           | Optimisation stockage |

---

## Mise en cluster

### 🔗 Ajouter des nœuds

Sur un nœud :

```bash
gluster peer probe node2
gluster peer probe node3
```

Vérification :

```bash
gluster peer status
```

---

## Création d'un volume

### 📁 Préparation des bricks

Sur chaque nœud :

```bash
mkdir -p /data/brick1
```

### 🔨 Création d'un volume répliqué

```bash
gluster volume create gv0 replica 3 \
node1:/data/brick1 \
node2:/data/brick1 \
node3:/data/brick1
```

Démarrage :

```bash
gluster volume start gv0
```

---

## Montage côté client

### 🔗 Montage FUSE

```bash
apt install glusterfs-client -y
mount -t glusterfs node1:/gv0 /mnt/gluster
```

### 📌 Montage persistant

```bash
node1:/gv0 /mnt/gluster glusterfs defaults,_netdev 0 0
```
