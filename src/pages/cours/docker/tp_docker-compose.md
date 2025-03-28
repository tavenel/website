---
title: Gestion de services avec docker compose
date: 2024 / 2025
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

:::tip
La CLI `docker compose` est basée sur la CLI `docker` pour être au maximum compatible avec elle : `docker compose ps`, `docker compose logs`, …
:::

:::exo
1. Démarrer la stack `docker compose`.
2. En utilisant `docker compose` et simplement `docker`, afficher les conteneurs, les volumes et le réseau créés.
:::

## Réseau docker-compose

:::tip
- Tout comme _Docker_ crée un enregistrement _DNS_ par nom de conteneur, _Docker compose_ crée un enregistrement _DNS_ par nom de _Service_ : ainsi dans l'exemple précédent, le _Service_ `wordpress` peut joindre le _Service_ `db`, même si les conteneurs n'ont pas le même nom.
- Par défaut, un fichier `compose.yml` crée automatiquement un réseau de type `bridge` pour l'ensemble des services dans ce fichier.
:::

Cette configuration n'est souvent pas suffisante, et l'on préfère définir explicitement les réseaux à utiliser.

Par exemple, dans la stack ci-dessous le `proxy` est uniquement dans un réseau `frontend`, l'`app` est dans 2 réseaux `frontend` et `backend` et `db` uniquement dans un réseau `backend`. Ainsi, `proxy` et `db` ne peuvent pas communiquer. Les conteneurs créés par cette stack sont tous sur des réseaux isolés, mais l'on veut pouvoir communiquer avec `proxy` directement depuis la machine hôte : il faut donc ajouter un _binding_ de port pour accéder depuis le port `8080` de l'hôte au port `80` du conteneur du service `proxy`. On peut donc maintenant accéder à l'application dans un navigateur depuis l'URL : <http://localhost:8080>.

```yaml
services:
  proxy:
    build: ./proxy
    networks:
      - frontend
    ports:
      - "8080:80"
  app:
    build: ./app
    networks:
      - frontend
      - backend
  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
    # Specify driver options
    driver: bridge
    driver_opts:
      com.docker.network.bridge.host_binding_ipv4: "127.0.0.1"
  backend:
    # Use a custom driver
    driver: custom-driver
```

## Dépendances

Le paramètre `depends_on:` est utilisée pour spécifier les dépendances (et donc l'ordre d'exécution) des services dans un fichier `compose.yml` afin de s'assurer que certains services ne commencent qu'une fois leurs dépendances sont prêtes. Cette dépendance est d'autant plus intéressante lorsqu'elle est connectée au `HEALTHCHECK` de _Docker_ : `depends_on: condition: service_healthy`. Ainsi on ne démarre le _Service_ qu'une fois que la dépendance est entièrement opérationnelle (par exemple, la base de données est démarrée et accessible).

## Scaling de services

Récupérer l'excellent support de formation de _Jérôme Petazzoni_ : 

```sh
git clone https://github.com/jpetazzo/container.training.git
```

Dans ce dépôt git se trouve le programme `dockercoins` : ce programme simule un miner de _docker coins_ qui est proportionnel au nombre de _workers_ déployés.

:::exo
1. Utiliser la commande `docker compose up` pour démarrer la stack applicative. Inspecter le fichier `docker-compose.yml` pour trouver comment accéder à l'interface Web du projet sur votre machine.
2. En utilisant une commande `docker compose`, réaliser un _scaling_ des `workers`. Observer dans la différence dans l'interface Web.
:::

## Dockeriser une application

> Jean, un de vos amis, est développeur dans une école d'informatique. Il vient tout juste de finaliser son premier projet en Python. Il s’agit d’une API qui va permettre d’enregistrer des élèves dans une base de données Redis.
> Avant d’avancer plus loin dans son code, il vous demande s'il est possible d’utiliser Docker pour pouvoir présenter son application à ses collègues depuis n’importe quel poste informatique. En effet, ces derniers ne travaillent pas tous sous le même système d’exploitation.

Suivre [cet exercice OpenClassrooms](https://openclassrooms.com/fr/courses/2035766-optimisez-votre-deploiement-en-creant-des-conteneurs-avec-docker/7540111-entrainez-vous-en-orchestrant-vos-images-docker-avec-docker-compose) pour vous entraîner à dockeriser une application.

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Oracle and MySQL are registered trademarks of Oracle and/or its affiliates.
- WordPress is a registered trademark of the WordPress Foundation in the United States and other countries.
