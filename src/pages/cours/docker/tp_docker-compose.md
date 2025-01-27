---
title: Gestion de services avec docker compose
date: 2023 / 2024
---

Nous allons maintenant utiliser l’outil `docker compose` pour créer, configurer et démarrer une stack `WordPress®` complète contenant un conteneur applicatif `WordPress®` et un conteneur `MySQL®`.

Pour cela, nous allons définir 2 services :

- un conteneur `mysql:5.7`

- un conteneur `wordpress:latest`

## Création du fichier de configuration compose.yaml

Créer un fichier de configuration `compose.yaml` permettant de configurer les 2 services `MySQL®` et `WordPress®` avec les contraintes suivantes :

Le conteneur `MySQL®` :

- utilise un volume externe pour persister des données (rappel : un conteneur doit être **stateless** au maximum, on persiste donc les données sur un volume externe au conteneur)

- définit les variables d’environnement suivantes : `MYSQL_ROOT_PASSWORD`, `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`

Le conteneur `Wordpress®` :

- dépend du conteneur `MySQL®` (on utilisera l’attribut `depends_on`)
- expose son port 80 sur un port du système hôte
- définit les variables d’environnement suivants :
   - `WORDPRESS_DB_HOST: db:3306`
   - `WORDPRESS_DB_USER`, `WORDPRESS_DB_PASSWORD`, `WORDPRESS_DB_NAME` cohérentes avec les variables d’environnement du conteneur `MySQL®`

Nous ajouterons la configuration `restart: always` à tous les services pour redémarrer automatiquement les conteneurs en cas d’arrêt ou de crash.

Exemple de fichier `compose.yaml` final pour une stack `MySQL®` + `WordPress®`.

Attention, un fichier `YAML` est sensible à l'indentation !

\pagebreak

```yaml
services:

  db:

    image: mysql:5.7

    volumes:
    - db_data:/var/lib/mysql

    restart: always

    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress:

   depends_on:
   - db

   image: wordpress:latest

   ports:
   - "8000:80"

   restart: always

   environment:
     WORDPRESS_DB_HOST: db:3306
     WORDPRESS_DB_USER: wordpress
     WORDPRESS_DB_PASSWORD: wordpress
     WORDPRESS_DB_NAME: wordpress

volumes:
  db_data: {}
```

## Démarrage de la stack

Utiliser la CLI `docker compose` pour démarrer la stack que nous venons de définir (voir la Cheatsheet en fin de document).

La CLI `docker compose` est basée sur la CLI `docker` pour être au maximum compatible avec elle.

## Dockeriser une application

> Jean, un de vos amis, est développeur dans une école d'informatique. Il vient tout juste de finaliser son premier projet en Python. Il s’agit d’une API qui va permettre d’enregistrer des élèves dans une base de données Redis.
> Avant d’avancer plus loin dans son code, il vous demande s'il est possible d’utiliser Docker pour pouvoir présenter son application à ses collègues depuis n’importe quel poste informatique. En effet, ces derniers ne travaillent pas tous sous le même système d’exploitation.

Suivre [cet exercice OpenClassrooms](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/7540111-entrainez-vous-en-orchestrant-vos-images-docker-avec-docker-compose) pour vous entraîner à dockeriser une application.

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Oracle and MySQL are registered trademarks of Oracle and/or its affiliates.
- WordPress is a registered trademark of the WordPress Foundation in the United States and other countries.
