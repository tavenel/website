---
title: 󱃾 Tom Avenel - M1 Devops
layout: ../../../layouts/BaseLayout.astro
---

# 󱃾  Conteneurs et Devops

## Présentation du module

### 🎯 Objectifs du cours

- Découvrir les principes DevOps
- Utiliser l'Infrastructure-as-Code avec Ansible® et Terraform®
- Créer des conteneurs avec la solution Docker®
- Gérer les images et les instances 
- Comprendre et mettre en place les mécanismes de stockage des conteneurs
- Comprendre les orchestrateurs de conteneurs : docker-compose et Kubernetes®

### 📅 Déroulé des séances

Module de 21H

Évaluation :

- 2 CC : QCM et Document de synthèse
- Évaluation finale : Projet et soutenance

## Rappels

- Gestionnaire de versions : voir le [cours Git](/cours/git)
- Intégration continue et déploiement continu : voir le [cours CI/CD](/cours/ci)

## Documents

- [🤓 Cours d'introduction au Devops](/cours/devops/devops-cours)

###   Docker®

- [🤓 Cours - introduction à Docker](/cours/docker/docker-cours)
- [🤓 Cheatsheet commandes Docker®, Dockerfile & Docker Compose](/cours/docker/docker-cheatsheet)
- [  TP Introduction à l'usage de conteneurs Docker®](/cours/docker/tp_docker) : l'objectif de ce TP est de se familiariser avec les concepts de base de Docker® - installation du Docker® Engine, création d'images, récupération d'images existantes depuis le Docker® Hub, création de conteneur depuis une image.
- [  TP Gestion de services applicatifs avec docker-compose](/cours/docker/tp_docker-compose) : l'objectif de ce TP est d'utiliser une technologie de conteneurs pour isoler une application en plusieurs composants. L'application sera déployée automatiquement dans un environnement docker-compose.

### 󱃾 Kubernetes® 

- [🤓 Cours - introduction à Kubernetes](/cours/docker/kubernetes-cours)
- [🤓 Cheatsheet Kubernetes®](/cours/docker/kubernetes-cheatsheet)
- [󱃾  TP : Premiers pas avec Kubernetes](/cours/docker/tp_k8s) : l'objectif de ce TP est de découvrir Kubernetes® à travers Minikube, une installation (très) simplifiée pour tester Kubernetes sur un seul serveur.
- 󱃾  Learn Kubernetes Basics: Tutoriels officiels pour débuter avec Kubernetes : <https://kubernetes.io/docs/tutorials/kubernetes-basics/>
- [󱃾  TP : Monitoring de Kubernetes avec Prometheus et Grafana](/cours/docker/tp_prometheus_grafana_k8s) : un exemple pour mettre en place une infrastructure standard de monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation.
- [󱃾  TP : Logging centralisé d'un cluster Kubernetes](/cours/docker/tp_k8s_elk) : le logging centralisé est essentiel dans un environnement `Kubernetes` pour surveiller les applications et diagnostiquer les problèmes. Nous allons voir différentes solutions de logging centralisé : stack ELK, `Fluent`, `Loki`.

### Infrastructure-as-Code

- [🤓 Cours d'introduction à Ansible : gérer des machines simplement par Infrastructure-as-Code](/cours/devops/ansible-cours)
- [🤓 Cours d'introduction à Terraform : gérer des ressources dans un cluster Cloud avec une notion d'état](/cours/devops/terraform-cours)
- [💻 Configuration des clés SSH pour un accès sécurisé](/cours/devops/tp_ssh)
- [💻 TP utiliser Ansible et Git pour réaliser de l'Infrastructure-as-Code.](/cours/git/git-tp-ansible)

### 📌 Projet Devops - Conteneurisation et déploiement continu d'une application en suivant un modèle DevOps

Dans le but d'accélérer le _time-to-market_ d'une application et d'augmenter la qualité de celle-ci, il est décidé de réaliser un déploiement continu de l'application par l'utilisation de conteneurs.

- [html](/cours/devops/projet-devops.html)
- [pdf](/cours/devops/projet-devops.pdf)
- [markdown](/cours/devops/projet-devops.md)

## Pour aller plus loin

- Voir les autres ressources du [cours sur le devops](/cours/devops).
