---
title: TP DevContainers
author: Tom Avenel
date: 2023 / 2024
correction: false
---

# TP Docker - Environnement de Développement avec DevContainers

## Objectif

Ce TP vise à configurer un environnement de développement portable et reproductible à l'aide de `Docker` et des `DevContainers`. L’objectif est de maîtriser la configuration d'un environnement `DevContainer` pour une application `Node.js` et de comprendre comment `Docker` peut être intégré dans le processus de développement.

## Contexte

L’un des défis rencontrés par les développeurs est de garantir la cohérence de l’environnement de développement entre différents membres d’une équipe. Grâce à `Docker` et aux `DevContainers`, il est possible de partager facilement des environnements de développement configurés de manière identique.

Un `DevContainer` est un environnement de développement personnalisé et isolé, configuré dans un conteneur `Docker`, utilisé principalement dans des éditeurs de code comme Visual Studio Code. Il permet aux développeurs de travailler dans un environnement reproductible et portable, peu importe la machine hôte.

## Étapes du TP

### Préparation du Projet

- **Clonez le dépôt frontend** : Récupérer un projet Frontend existant, on pourra par exemple récupérer une des implémentations frontend de l'application <https://github.com/gothinkster/realworld>

### Création du DevContainer

**Objectif** : Configurer un DevContainer dans Visual Studio Code qui utilise Docker pour exécuter l’application dans un environnement contrôlé.

- Créer le dossier `.devcontainer/` à la racine du projet.
- Créer un fichier `devcontainer.json` avec les éléments suivants :
   - L'image Docker à utiliser (par exemple, `node:16`).
   - Les options de montage de volume pour synchroniser le code source avec le conteneur.
   - Les configurations pour exécuter automatiquement l’installation des dépendances (`npm install`).
   - Les paramètres d’ouverture de port pour accéder à l’application via localhost.

Exemple de fichier `devcontainer.json` :
```json
{
  "name": "Node.js Dev Container",
  "image": "node:16",
  "postCreateCommand": "npm install",
  "mounts": [
    "source=${localWorkspaceFolder},target=/workspace,type=bind"
  ],
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "extensions": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode"
  ],
  "forwardPorts": [3000],
  "workspaceFolder": "/workspace"
}
```

### Configuration de Docker Compose (Optionnel)

**Objectif** : Combiner DevContainers et Docker Compose permet de créer un environnement de développement complexe et reproductible, idéal pour les projets nécessitant plusieurs services interconnectés.

- Créer un fichier `docker-compose.yml` pour ajoutez une implémentation du backend de l'application.
- Modifier le fichier `devcontainer.json` pour utiliser le fichier `docker-compose.yml`.

Exemple de fichier `docker-compose.yml` pour un service applicatif `app` et un service technique de BDD `mongo` :

```yaml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: .devcontainer/Dockerfile
    volumes:
      - .:/workspace
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
  
  mongo:
    image: mongo
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

Exemple de fichier `devcontainer.json` utilisant le service `app` et le `docker-compose.yaml` pour déployer une stack complète :

```json
{
  "name": "Node.js Dev Container",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/workspace",
  "extensions": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode"
  ],
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "postCreateCommand": "npm install"
}
```

### Tests et Debugging

- **Lancement de l’environnement** : Ouvrez le projet dans VS Code et démarrez le DevContainer.
- **Vérification du fonctionnement** : Testez que l’application se lance correctement avec `npm start` dans le DevContainer.
- **Debugging** : Ajoutez des configurations de debugging dans VS Code pour déboguer l’application Node.js dans le DevContainer.

### Environnement complet

- **Ajouter des extensions** : Ajoutez des extensions VS Code supplémentaires pour le linting et le formattage (`ESLint`, `Prettier`).
- **Scripts de tests** : Ajoutez un script de test (par exemple, `npm test`)
- **Environnement de développement avec Docker Compose** : Utilisez `docker-compose up` pour lancer l’environnement complet avec `MongoDB` et vérifiez la connexion entre l’application et la base de données.

\newpage{}

## Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.

