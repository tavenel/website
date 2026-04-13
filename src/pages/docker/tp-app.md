---
title: Conteneurisation d'une application multi-composants
date: 2025 / 2026
---

## Objectifs pédagogiques

À l'issue de ce TP, vous serez capable de :

- Conteneuriser une application composée de plusieurs services
- Utiliser des réseaux Docker dédiés
- Gérer des volumes persistants
- Configurer des variables d'environnement
- Orchestrer une application avec Docker Compose

## Contexte

Vous travaillez pour une startup qui développe une application web simple composée de :

- Un frontend (serveur web Nginx)
- Un backend (API Node.js)
- Une base de données (MongoDB)

L'objectif est de conteneuriser l'ensemble de cette application afin de faciliter son déploiement.

## Architecture cible

```
[ Navigateur ]
       |
       v
[ Nginx (frontend) ] ---> [ API Node.js ] ---> [ MongoDB ]
```

Contraintes :

- Le frontend doit être accessible depuis l'extérieur
- Le backend ne doit pas être exposé directement
- La base de données doit être persistante
- Les services doivent communiquer via un réseau Docker dédié

## Préparation de l'environnement

### Structure du projet

Créer l'arborescence suivante :

```
app/
 ├── frontend/
 │    └── index.html
 ├── backend/
 │    ├── app.js
 │    └── package.json
 └── docker-compose.yml
```

## Conteneurisation du backend

### Exemple de code backend (Node.js)

Créer un fichier `app.js` :

```js
const express = require('express');
const mongoose = require('mongoose');

const app = express();

mongoose.connect(process.env.MONGO_URL)
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error(err));

app.get('/', (req, res) => {
  res.send('API OK');
});

app.listen(3000, () => console.log('Server running'));
```

### Dockerfile backend

Créer un `Dockerfile` dans `backend/` :

```
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["node", "app.js"]
```

## Conteneurisation du frontend

### Exemple de page HTML

Créer `index.html` :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Frontend</title>
</head>
<body>
    <h1>Frontend OK</h1>
</body>
</html>
```

### Utilisation de Nginx

Aucun Dockerfile nécessaire, on utilisera l'image officielle.

## Déploiement de l'application

### Déploiement manuel avec les commandes Docker

1. Créer un réseau dédié pour permettre la communication entre les conteneurs :

    ```bash
    docker network create app-network
    ```

1. Créer un volume pour la persistance des données :

    ```bash
    docker volume create mongo-data
    ```

1. Lancer le conteneur MongoDB :

    ```bash
    docker run -d \
     --name mongo \
     --network app-network \
     -v mongo-data:/data/db \
     mongo:latest
    ```

1. Construire l'image du backend :

    ```bash
    docker build -t backend-app ./backend
    ```

1. Lancer le conteneur backend :

    ```bash
    docker run -d \
      --name backend \
      --network app-network \
      -e MONGO_URL=mongodb://mongo:27017/appdb \
      backend-app
    ```

1. Lancer le conteneur frontend avec montage du code HTML :

    ```bash
    docker run -d \
      --name frontend \
      --network app-network \
      -p 8080:80 \
      -v $(pwd)/frontend:/usr/share/nginx/html:ro \
      nginx:latest
    ```

1. Tester l'accès au frontend : [http://localhost:8080](http://localhost:8080)

### Fichier docker-compose.yml

1. Docker compose permet d'automatiser et de rendre reproductible le déploiement précédent.

    ```yaml
    version: '3.8'
    
    services:
      frontend:
        image: nginx:latest
        ports:
          - "8080:80"
        volumes:
          - ./frontend:/usr/share/nginx/html:ro
        networks:
          - app-network
    
      backend:
        build: ./backend
        environment:
          - MONGO_URL=mongodb://mongo:27017/appdb
        depends_on:
          - mongo
        networks:
          - app-network
    
      mongo:
        image: mongo:latest
        volumes:
          - mongo-data:/data/db
        networks:
          - app-network
    
    networks:
      app-network:
        driver: bridge
    
    volumes:
      mongo-data:
    ```

1. Lancer l'application :

    ```sh
    docker-compose up -d --build
    ```

1. Vérification :
   - Accéder au frontend : [http://localhost:8080](http://localhost:8080)
   - Vérifier les logs :

    ```sh
    docker-compose logs -f
    ```

## Analyse technique

:::exo

1. Pourquoi utilise-t-on un réseau Docker dédié ?
2. Pourquoi le backend n'expose-t-il pas de port ?
3. Quel est le rôle du volume `mongo-data` ?
4. Que se passe-t-il si le conteneur MongoDB est supprimé ?
5. Où sont stockées les variables d'environnement ?

:::

:::correction

1. Pourquoi utilise-t-on un réseau Docker dédié ?
   - Un réseau Docker dédié (`app-network`) crée un bridge qui permet :
   - **Isolation logique** : les conteneurs de l'application communiquent entre eux sans être exposés aux autres conteneurs du host.
   - **Résolution DNS interne** : Docker fournit un DNS embarqué → les services peuvent se joindre via leur nom (`mongo`, `backend`).
   - **Sécurité** : seuls les services connectés au réseau peuvent communiquer entre eux.
   - **Contrôle des flux** : on évite d'exposer inutilement des ports vers l'extérieur.
2. Pourquoi le backend n'expose-t-il pas de port ?
   - Le backend n'expose pas de port (`ports:` absent) car :
   - Il est **consommé uniquement en interne** par le frontend ou d'autres services
   - Il est accessible via le réseau Docker (`http://backend:3000`)
   - Cela **réduit la surface d'attaque** (principe du moindre privilège)
   - Seul le frontend joue le rôle de **point d'entrée (entrypoint)**.
3. Quel est le rôle du volume `mongo-data` ?
   - Le volume `mongo-data` permet de :
   - **Persister les données** de MongoDB en dehors du conteneur
   - Éviter la perte de données lors d'un redémarrage ou d'une suppression du conteneur
   - Sans volume, les données seraient stockées dans le filesystem éphémère du conteneur.
4. Que se passe-t-il si le conteneur MongoDB est supprimé ?
   - **Avec volume (`mongo-data`)** :
     - Les données sont conservées
     - Un nouveau conteneur retrouve l'état précédent
   - **Sans volume** :
     - Toutes les données sont perdues définitivement
     - Séparation **conteneur (stateless)** vs **données (stateful)**.
5. Où sont stockées les variables d'environnement ?
   - Injectées **au runtime** dans le conteneur :

    ```yaml
    environment:
      - MONGO_URL=mongodb://mongo:27017/appdb
     ```

   - Accessibles via `process.env` dans Node.js
   - En pratique, on ajoute outils sécurisés (Vault, secrets Docker)
   - **Ne jamais hardcoder les configurations sensibles**.

:::

## Améliorations

:::exo

- Ajouter un fichier `.env` pour externaliser la configuration
- Sécuriser MongoDB (authentification)
- Ajouter un reverse proxy avec configuration personnalisée
- Mettre en place des healthchecks

:::
