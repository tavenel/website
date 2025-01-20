---
title: Migration et reprise des données
author: Tom Avenel
date: 2023 / 2024
---

# Cas pratique 2 : Migration et reprise des données

Dans les cas pratique 1, les données à intégrer sont un ensemble conséquent d'informations sur des employés.

Ces données sont aujourd'hui stockées en production au format `XML`.
Ce format pose cependant des soucis de maintenabilité et de performance pour un volume élevé de données.

Il a donc été décidé de transformer ces données pour les intégrer dans un base de données relationnelle : il s'agit des données à intégrer dans le cas pratique 1, fournies sous forme d'un dump d'une base de donnée de développement.

Le but de ce cas pratique est de valider la migration et la reprise de ces données, depuis le format précédent `XML` vers le nouveau format `SQL`.

## Récupération des données de production

Commencer par récupérer les données de production au format `XML` du cas pratique 1.

## Description des données migrées

Les données sont disponibles dans un dump d'une base de données `MySQL`, simulant 300,000 enregistrements d'employés et 2,8 million d'entrées de salaires.
Il s'agit de l'entièreté des données des employés de l'entreprise.

Les données sont disponibles dans une archive : <https://github.com/datacharmer/test_db/releases/download/v1.0.7/test_db-1.0.7.tar.gz>

_Schéma relationnel réalisé par Giuseppe Maxia et export de données par Patrick Crews._

## Environnement d'intégration pour la migration des données

L'environnement d'intégration est un conteneur `MySQL` simple.

Celui-ci utilise l'image ayant le tag `latest`, et les accès à la base de données sont réalisées par le super-utilisateur.

Pour déployer l'application dans l'environnement d'intégration :

1. Extraire l'archive sur la machine hôte
2. Démarrer un conteneur `MySQL` et provisionner la base avec les employés
```sh
$ docker run --name integration -e MYSQL_ROOT_PASSWORD=test mysql:latest
$ docker cp test_db/ integration:/tmp/
$ docker exec -it integration /bin/bash
$ cd /tmp/test_db
$ mysql -p -t < employees.sql
$ rm -r /tmp/test_db
```

## Environnement de production

L'environnement de (pré-)production est également un conteneur MySQL mais avec quelques changements :

- Le conteneur s'appelle `production`
- L'image utilisée est la version 5.5 de `MySQL`
- Le mot de passe de l'administrateur `MySQL` est temporaire
- Les accès à la base de données sont réalisés par l'utilisateur `prod` (mot de passe : `prod`)
- Les mots de passe sont fournis par des fichiers de mots de passe dans le répertoire `/opt/data/secrets` dans l'hôte et le conteneur (ou autre au besoin)
- Les données d'insertion et les sauvegardes sont stockées dans le répertoire `/opt/data` dans l'hôte et le conteneur (ou autre au besoin)

Le démarrage du système de production est prévu par la commande suivante :

```sh
$ docker run --name production \
-v /opt/data:/opt/data \
-e MYSQL_ONETIME_PASSWORD=yes \
-e MYSQL_ROOT_PASSWORD_FILE=/opt/data/secrets/mysql-root.secret \
-e MYSQL_USER=prod \
-e MYSQL_PASSWORD=/opt/data/secrets/mysql-user.secret \
mysql:5.5
```

Le reste du déploiement de l'application est prévu de manière similaire à l'environnement d'intégration.

## Travail attendu

- Définir le niveau de qualité requis et évaluer les risques de la migration et de la reprise de données

### Partie migration des données

- Concevoir le tableau de mapping source et données : Lister les données sources et champs de destination pour stocker les données  
- Déterminer le type de migration : migration d’initialisation – migration quotidienne  
- Expliquer la stratégie de tests : identification des techniques de tests et des critères retenus pour choisir les scénarios de tests.
- Concevoir un plan de tests permettant de valider la migration des données du format `XML` à une base de données relationnelle.
- Définir les scénarios et les cas de tests 
- Pour chaque type de test :  
  - Décrire le test, expliquer son implémentation et son exécution 
  - Si non implémenté ou exécuté, expliquer les raisons 
  - Données utilisées (connues ? contrôlées ? ...) 
- Suite à la réalisation de ce plan de tests, le choix de migration des données vous paraît-il pertinent ? Pourquoi ?

### Partie reprise des données

- Présenter un nouveau cahier de recette permettant de valider la reprise des données
- Exécuter la recette sur la pré-production
- Consigner les résultats d'exécution de la recette (statut du test, éléments vérifiés, logs, ...)
- Expliquer les défaillances et anomalies éventuellement relevées ainsi que les solutions apportées
- Suite à la réalisation de ces tests, avez-vous des recommandations à apporter sur la future production ? sur l'environnement d'intégration ?

## Documentation 

- Conteneur MySQL utilisé : [lien](https://hub.docker.com/_/mysql?tab=description)

