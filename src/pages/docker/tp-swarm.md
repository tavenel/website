---
title: Déploiement Multi-Host avec Docker Swarm
date: 2025 / 2026
---

## Objectifs pédagogiques

À l'issue de ce TP, vous serez capable de :

* Comprendre les limites du mode single-host Docker
* Mettre en place un cluster Docker Swarm
* Déployer une application multi-conteneurs sur plusieurs hôtes
* Utiliser les concepts de services, overlay network et scaling
* Comprendre la répartition de charge (load balancing)

## Contexte

* Votre entreprise souhaite rendre son application hautement disponible et scalable.
* Jusqu'à présent, l'application était déployée sur une seule machine via Docker. Cette approche présente des limites :
  * Point de défaillance unique
  * Scalabilité limitée
* Vous devez désormais déployer cette application sur **plusieurs machines (multi-host)**.

## Problématique technique

:::tip
**On ne peut pas utiliser un réseau `overlay` multi-host sans activer un orchestrateur comme Docker Swarm**.
:::

Le driver réseau `overlay` de Docker repose sur :

* un **store distribué (KV store)** pour partager l'état du réseau
* un mécanisme de **découverte des pairs**
* une **gestion des endpoints multi-host**

:::warn
Historiquement, un réseau Overlay en Docker nécessitait Consul + Etcd + ZooKeeper. Cette approche est aujourd'hui abandonnée en faveur **exclusivement** de **Docker Swarm** pour fournir :

* la gestion du cluster
* la distribution des métadonnées réseau
* la création des réseaux overlay multi-host

:::

## Architecture cible

```
[ User ]
    |
    v
[ Load Balancer Swarm ]
    |
    v
[ Frontend (replicas) ]
    |
    v
[ Backend (replicas) ]
    |
    v
[ Database ]
```

## Prérequis

* 2 à 3 machines Linux (VM ou cloud)
* Docker installé sur chaque machine
* Connectivité réseau entre les machines

## Initialisation du cluster Swarm

### Initialiser le manager

Sur la machine principale :

```bash
docker swarm init
```

Récupérer le token d'ajout des workers.

### Ajouter des workers

Sur les autres machines :

```bash
docker swarm join --token <TOKEN> <IP_MANAGER>:2377
```

### Vérification

Sur le manager :

```bash
docker node ls
```

## Réseau overlay

Créer un réseau multi-host :

```bash
docker network create \
  --driver overlay \
  app-overlay
```

## Déploiement des services

### Base de données

```bash
docker service create \
  --name mongo \
  --network app-overlay \
  --mount type=volume,source=mongo-data,target=/data/db \
  mongo:latest
```

### Backend

```bash
docker service create \
  --name backend \
  --network app-overlay \
  --replicas 2 \
  -e MONGO_URL=mongodb://mongo:27017/appdb \
  backend-app
```

### Frontend

```bash
docker service create \
  --name frontend \
  --network app-overlay \
  --replicas 2 \
  -p 8080:80 \
  nginx:latest
```

## Vérifications

Lister les services :

```bash
docker service ls
```

Observer les conteneurs :

```bash
docker service ps frontend
```

Tester l'accès via : <http://\<IP_NODE\>:8080>

## Scaling

Augmenter le nombre de réplicas :

```bash
docker service scale frontend=4
```

Observer la répartition des conteneurs sur les nœuds.

## Analyse technique

:::exo

1. Quelle est la différence entre un conteneur et un service dans Swarm ?
2. Qu'est-ce qu'un réseau overlay ?
3. Comment Swarm répartit-il les conteneurs ?
4. Que se passe-t-il si un nœud tombe ?
5. Pourquoi la base de données est-elle plus complexe à scaler ?

:::

## Bonus (niveau avancé)

* Déployer via un stack (`docker stack deploy`)
* Ajouter Traefik comme reverse proxy
* Mettre en place TLS entre les nœuds
* Tester une panne de nœud
