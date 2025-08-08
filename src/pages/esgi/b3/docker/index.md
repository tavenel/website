---
title:   Tom Avenel - B3 Docker
layout: '@layouts/BaseLayout.astro'
---

#   Conteneurisation Docker

## Présentation du module

### 🎯 Objectifs du cours
 
- Créer des conteneurs avec la solution Docker®
- Comprendre les implications de la conteneurisation pour le développement logiciel : écriture de Dockerfile, …
- Gérer les images et les instances 
- Comprendre et mettre en place les mécanismes de stockage des conteneurs
- S'initier aux orchestrateurs de conteneurs : (docker-compose et Kubernetes®)
- Utiliser des conteneurs comme environnement de travail (VSCode DevContainers)

### 📅 Déroulé des séances

Module de 15H

Évaluation : QCM et Projet (soutenance)

## 📑 Documents

###   Docker®

- [🤓 Cours - introduction à Docker](/docker/cours)
- [🤓 Cheatsheet commandes Docker®, Dockerfile & Docker Compose](/docker/cheatsheet)
- [  TP Introduction à l'usage de conteneurs Docker®](/docker/tp) : l'objectif de ce TP est de se familiariser avec les concepts de base de Docker® - installation du Docker® Engine, création d'images, récupération d'images existantes depuis le Docker® Hub, création de conteneur depuis une image.
- [  TP Build avec buildx et BuildKit](/docker/tp-buildkit) : l'objectif de ce TP est de découvrir BuildKit, un builder moderne pour Docker.
- [  TP Gestion de services applicatifs avec docker-compose](/docker/tp-docker_compose) : l'objectif de ce TP est d'utiliser une technologie de conteneurs pour isoler une application en plusieurs composants. L'application sera déployée automatiquement dans un environnement docker-compose.
- [💻 TP : Environnement de Développement avec DevContainers](/docker/tp-devcontainer) : ce TP vise à configurer un environnement de développement portable et reproductible à l'aide de `Docker` et des `DevContainers`. L'objectif est de maîtriser la configuration d'un environnement `DevContainer` pour une application `Node.js` et de comprendre comment `Docker` peut être intégré dans le processus de développement.
- [🚢 TP Podman : Conteneurs et Pods sans serveur](/docker/tp-podman) : `Podman` est un moteur de conteneur compatible avec l'API Docker conçu pour créer, exécuter et gérer des conteneurs et des pods Kubernetes sans nécessiter de démon, ce qui le rend idéal pour le développement et pour tester des pods Kubernetes en local sans nécessiter de cluster Kubernetes complet.

### 󱃾 Kubernetes® 

- [🤓 Cours Kubernetes orienté Développeur](/k8s/cours-dev)
- [🤓 Cheatsheet Kubernetes®](/k8s/cheatsheet)
- [󱃾  TP : Premiers pas avec Kubernetes](/k8s/tp) : l'objectif de ce TP est de découvrir Kubernetes® à travers Minikube, une installation (très) simplifiée pour tester Kubernetes sur un seul serveur.
- 󱃾  Learn Kubernetes Basics: Tutoriels officiels pour débuter avec Kubernetes : <https://kubernetes.io/docs/tutorials/kubernetes-basics/>

### 🏆 Projet Dockerisation d'un Projet Multi-Composants

Le but de ce projet est de dockeriser un projet personnel existant qui se compose de plusieurs composants. 

- [📄 Sujet](/docker/projet-dev)

## 🚀 Pour aller plus loin

- Voir les autres ressources du [  cours sur Docker & Kubernetes](/docker).
