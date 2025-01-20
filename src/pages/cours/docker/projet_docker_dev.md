---
title: Projet Dockerisation d'un Projet Multi-Composants
author: Tom Avenel
date: 2023 / 2024
---

# Dockerisation d'un Projet Multi-Composants

## Objectif

Le but de ce projet est de dockeriser un projet personnel existant qui se compose de plusieurs composants (par exemple, une application web front-end, une API back-end, une base de données, etc.). Vous devrez créer des images Docker pour chaque composant, en utilisant des Dockerfile _multi-stage_ pour optimiser la taille des images et améliorer les performances.

## Contexte

De nombreux projets modernes sont constitués de plusieurs services interconnectés, chacun ayant ses propres dépendances et configurations. La dockerisation de ces projets permet de s'assurer qu'ils s'exécutent de manière cohérente sur différents environnements (local, test, production) et facilite le déploiement.

## Tâches à Réaliser

- Identifiez les composants de votre projet existant.
- Évaluez les dépendances nécessaires pour chaque composant.
- Créez les Dockerfile pour chaque composant en utilisant des builds multi-stage lorsque cela est nécessaire.
- Créez un fichier `docker-compose.yml` pour orchestrer vos différents conteneurs
- Testez chaque composant en s'assurant qu'ils fonctionnent comme prévu et vérifiez la communication entre les services.
- Créez des fichiers de ressources `k8s` / `podman` pour un déploiement en production.
- (Optionel) créez une chart `Helm` pour gérer de manière unifiée toute votre stack applicative dans k8s.

\newpage{}

## Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- K8s® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Podman® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Helm® is a registered trademark of The Linux Foundation in the United States and/or other countries.

