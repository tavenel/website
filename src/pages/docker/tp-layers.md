---
title: Optimisation des layers d'une image Docker
date: 2025 / 2026
---

Vous travaillez dans une équipe DevOps. Une application Node.js doit être conteneurisée, mais le Dockerfile fourni est mal optimisé. Votre mission : **analyser, comprendre et améliorer cette image**.

## 🎯 Objectifs pédagogiques

À l'issue de ce TP, vous serez capable de :

- Comprendre le fonctionnement interne des **layers Docker**
- Analyser la structure et la taille d'une image
- Identifier les mauvaises pratiques dans un Dockerfile
- Optimiser une image en :
  - réduisant le nombre de layers
  - exploitant efficacement le cache Docker
  - diminuant la taille finale
- Mettre en œuvre des techniques avancées :
  - organisation des instructions
  - nettoyage des dépendances
  - multi-stage build

## Analyse d'une image non optimisée

Voici un Dockerfile non optimisé :

```dockerfile
FROM node:18

WORKDIR /app

COPY . .

RUN npm install

RUN apt-get update
RUN apt-get install -y curl

EXPOSE 3000

CMD ["node", "app.js"]
````

Builder l'image et analyser les layers :

```bash
docker build -t app:bad .
docker history app:bad
```

:::tip

### 🔍 Comprendre les layers

Chaque instruction du Dockerfile crée un **layer immuable** :

- `FROM` → base de l'image
- `COPY` → ajoute des fichiers
- `RUN` → exécute une commande et crée un nouveau layer

Docker empile ces layers comme un système de fichiers en couches.
:::

### Exercice

:::exo

Répondez aux questions suivantes :

1. Combien de layers sont générés ?
2. Quelles instructions sont les plus coûteuses ?
3. Pourquoi le cache Docker est mal utilisé ?
4. Que se passe-t-il si un seul fichier change ?

:::

:::correction

### Correction

- Focus sur :

```dockerfile
COPY . .
RUN npm install
```

- Docker invalide le cache dès que le contenu copié change
- Donc `npm install` est relancé inutilement
- Autres problèmes :
  - Trop de `RUN`
  - Pas de nettoyage système
  - Mauvais ordre des instructions
  - Image de base lourde

:::

## Optimisation du Dockerfile

### Objectif

Réécrire un Dockerfile plus efficace en :

- réduisant les layers
- améliorant le cache
- diminuant la taille finale

### 🔧 Principe 1 - Optimisation du cache Docker

❌ Mauvaise pratique : le cache est invalidé à chaque modification du code

```dockerfile
COPY . .
RUN npm install
```

:::tip
Bonne pratique :

- `package.json` change rarement
- Docker peut réutiliser le cache pour `npm install`
- Gain de temps énorme en build

:::

```dockerfile
COPY package*.json ./
RUN npm install
COPY . .
```

### 🔧 Principe 2 - Réduction du nombre de layers

❌ Mauvaise pratique : 2 layers inutiles

```dockerfile
RUN apt-get update
RUN apt-get install -y curl
```

:::tip
Bonne pratique :

- Une seule instruction = un seul layer
- Nettoyage pour réduire la taille

:::

```dockerfile
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### 🔧 Principe 3 - Choix d'une image légère

❌Mauvaise pratique : l'image standard inclut un OS entier conséquent

```dockerfile
FROM node:18
```

:::tip
Bonne pratique :

- Alpine = distribution minimaliste
- Image beaucoup plus légère
- Moins de surface d'attaque

:::

```dockerfile
FROM node:18-alpine
```

## Écriture du Dockerfile optimisé

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN apk add --no-cache curl

EXPOSE 3000

CMD ["node", "app.js"]
```

### Comparaison et analyse comparative

```bash
docker build -t app:optimized .
docker images
docker history app:bad
docker history app:optimized
```

:::exo

- Combien de layers avez-vous gagné ?
- Quelle est la différence de taille ?
- Pourquoi l'image optimisée est plus performante ?

:::

## Multi-stage build

- Objectif : séparer l'environnement de **build** de l'environnement de **runtime**.
- Un multi-stage build permet :
  - de compiler dans une première image
  - de ne garder que le nécessaire dans la finale
- Avantages :
  - Les dépendances de build ne sont pas conservées
  - Les fichiers sources inutiles sont supprimés
  - Seuls les artefacts nécessaires sont copiés

```dockerfile
# Stage 1: build
FROM node:18 AS builder

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Stage 2: runtime
FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app/dist ./dist
COPY package*.json ./

RUN npm install --only=production

CMD ["node", "dist/app.js"]
```

:::exo

- Quelle différence de taille observez-vous ?
- Quels fichiers ont disparu ?
- Pourquoi c'est essentiel en production ?

:::

## Analyse avancée

:::tip
👉 Docker cache les layers **instruction par instruction** :

- ordre du Dockerfile = performance
- granularité des instructions = impact direct

:::

Commandes utiles :

```bash
docker history <image>
docker inspect <image>
```

:::tip
L'outil <https://trivy.dev/> permet d'optenir des informations avancées sur les layers.
:::

:::exo

- Quel layer est le plus volumineux ?
- Que contient chaque layer ?
- Que se passe-t-il si vous modifiez :
  - un fichier source ?
  - `package.json` ?

:::
