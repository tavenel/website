---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Stockage Distribué avec Ceph
layout: '@layouts/CoursePartLayout.astro'
---

## Ceph

Ceph est une solution de stockage distribuée puissante et mature, adaptée aux environnements modernes (Cloud, DevOps, Kubernetes). Sa maîtrise nécessite une bonne compréhension Linux, réseau et systèmes distribués, mais offre une grande valeur opérationnelle.

Ceph est une plateforme de stockage distribué open source, conçue pour fournir un stockage **hautement disponible**, **scalable horizontalement** et **tolérant aux pannes**, sans point unique de défaillance (SPOF).

Ceph repose sur un algorithme de placement distribué (CRUSH) et permet de fournir trois types de stockage :

- **Objet** (via RADOS Gateway - S3/Swift)
- **Bloc** (via RBD - RADOS Block Device)
- **Fichier** (via CephFS)

### Cas d'usage typiques

- Infrastructures Cloud (OpenStack, Kubernetes)
- Virtualisation (stockage pour VM)
- Stockage objet S3 on-premise
- Stockage massif de données (Big Data, sauvegardes)

### Avantages

- Scalabilité horizontale
- Haute disponibilité native
- Auto-rééquilibrage
- Open source

### Limites

- Courbe d'apprentissage élevée
- Exigeant en ressources (CPU, RAM, réseau)
- Complexité opérationnelle

---

## Architecture

### Vue d'ensemble

Un cluster Ceph est composé de plusieurs types de démons :

- **MON (Monitor)** : maintient l'état du cluster
- **OSD (Object Storage Daemon)** : stocke les données
- **MGR (Manager)** : collecte métriques et plugins
- **MDS (Metadata Server)** : métadonnées CephFS
- **RGW (RADOS Gateway)** : accès objet S3/Swift

### RADOS (Reliable Autonomic Distributed Object Store)

RADOS est le cœur de Ceph. Il gère :

- La réplication
- Le placement des objets
- La cohérence
- La récupération après panne

### Algorithme CRUSH

_CRUSH_ détermine où stocker les données **sans table centrale**.

Concepts clés :

- CRUSH Map
- Buckets (OSD, Host, Rack, DC)
- Rules

Avantage majeur : suppression des goulots d'étranglement et meilleure résilience.

---

## Déploiement d'un cluster Ceph

### Architecture type d'un cluster Ceph

**Cluster minimal de production** :

- 3 nœuds MON/MGR (quorum)
- ≥ 3 nœuds OSD
- Réseau public (clients)
- Réseau cluster (réplication interne)

Bonnes pratiques :

- Séparer rôles critiques si possible
- Réseau dédié pour la réplication
- Disques dédiés par OSD

---

### Checklist de déploiement

**Avant installation**

- Synchronisation NTP active
- Résolution DNS fonctionnelle
- Accès SSH sans mot de passe
- Disques vierges disponibles
- Pare-feu configuré ou désactivé

**Pendant le bootstrap**

- Vérification de la version Ceph
- Déploiement du premier MON/MGR
- Sauvegarde de la clé admin

**Après déploiement**

- Vérifier l'état du cluster (HEALTH_OK)
- Vérifier la distribution des PG
- Tester un pool et un accès client

---

### Étapes générales de déploiement

1. Installation de cephadm (recommandé vs autres méthodes)
2. Bootstrap du cluster
3. Ajout des nœuds
4. Déploiement des OSD

---

## Stockage Bloc : Ceph RBD

### Concepts

- Pool
- Image RBD
- Snapshot
- Clone

### Cas d'usage

- Stockage pour VM (KVM, OpenStack)
- Volumes persistants Kubernetes

### Fonctionnalités avancées

- Thin provisioning
- Snapshots instantanés
- Réplication

---

## Stockage Objet : RADOS Gateway (RGW)

RGW fournit une API compatible :

- Amazon S3
- OpenStack Swift

### Concepts clés

- User
- Bucket
- Object
- Policy

### Cas d'usage

- Applications cloud-native
- Sauvegardes
- Archivage

---

## Stockage Fichier : CephFS

### Architecture

- MDS actif / standby
- Pool data
- Pool metadata

### Accès client

- Montage noyau Linux
- FUSE

### Cas d'usage

- Répertoires partagés
- Workloads HPC

---

## Gestion des pools et de la réplication

### Pools

- Réplication (replicated pools)
- Erasure Coding

### Placement Groups (PG)

- Rôle des PG
- Impact sur les performances

### Facteur de réplication

- Taille (size)
- Min_size

---

## Supervision, santé et maintenance

### Ceph Health

États possibles :

- `HEALTH_OK`
- `HEALTH_WARN`
- `HEALTH_ERR`

### Supervision

- Dashboard Ceph
- Prometheus
- Alertmanager

### Maintenance

- Ajout / retrait d'OSD
- Rebalancing
- Mise à jour du cluster

---

## Sécurité

### Authentification

- CephX
- Keyrings

### Réseau

- Séparation réseau public / cluster
- Chiffrement (_msgr2_)

### Bonnes pratiques

- Principe du moindre privilège
- Sauvegarde des clés

---

## Performances et bonnes pratiques

### Facteurs influençant les performances

- Type de disque
- Réseau
- Nombre de PG

### Optimisations

- SSD pour journaux / WAL
- Erasure Coding pour le stockage froid

---

## Glossaire Ceph

- **Ceph** : Plateforme de stockage distribué open source.
- **RADOS** : Cœur du système Ceph, stockage objet distribué.
- **OSD (Object Storage Daemon)** : Démon chargé de stocker physiquement les données.
- **MON (Monitor)** : Maintient l'état du cluster (maps, quorum).
- **MGR (Manager)** : Fournit métriques, dashboard et modules de gestion.
- **MDS (Metadata Server)** : Gère les métadonnées pour CephFS.
- **RGW (RADOS Gateway)** : Passerelle objet compatible S3/Swift.
- **CRUSH** : Algorithme de placement des données sans table centrale.
- **Pool** : Espace logique de stockage.
- **PG (Placement Group)** : Unité logique de distribution des objets.
- **RBD** : RADOS Block Device, stockage bloc.
- **CephFS** : Système de fichiers distribué Ceph.
- **Erasure Coding** : Technique de protection des données par fragments.
- **CephX** : Mécanisme d'authentification et d'autorisation Ceph.

---

## Erreurs courantes et dépannage

- **HEALTH_WARN** : PG mal répartis, seuils dépassés
- **OSD down** : disque défaillant ou problème réseau
- **No quorum** : nombre insuffisant de MON actifs
- **Performances faibles** : PG mal dimensionnés, réseau saturé

Méthodologie de dépannage :

1. Analyser l'état global
2. Identifier le composant fautif
3. Vérifier logs et métriques
4. Corriger puis surveiller la récupération

---
