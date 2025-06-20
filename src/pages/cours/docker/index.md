---
title:   Docker® et 󱃾 Kubernetes® 
---

![](@assets/undraw/undraw_container-ship_t6yx.svg)

##   Docker®

- [🤓 Cours - introduction à Docker](/cours/docker/docker-cours)
- [🤓 Cheatsheet commandes Docker®, Dockerfile & Docker Compose](/cours/docker/docker-cheatsheet)
- [  TP Introduction à l'usage de conteneurs Docker®](/cours/docker/tp_docker) : l'objectif de ce TP est de se familiariser avec les concepts de base de Docker® - installation du Docker® Engine, création d'images, récupération d'images existantes depuis le Docker® Hub, création de conteneur depuis une image.
- [  TP Gestion de services applicatifs avec docker-compose](/cours/docker/tp_docker-compose) : l'objectif de ce TP est d'utiliser une technologie de conteneurs pour isoler une application en plusieurs composants. L'application sera déployée automatiquement dans un environnement docker-compose.
- [💻 TP : Environnement de Développement avec DevContainers](/cours/docker/tp_devcontainer) : ce TP vise à configurer un environnement de développement portable et reproductible à l'aide de `Docker` et des `DevContainers`. L’objectif est de maîtriser la configuration d'un environnement `DevContainer` pour une application `Node.js` et de comprendre comment `Docker` peut être intégré dans le processus de développement.
- [🚢 TP Podman : Conteneurs et Pods sans serveur](/cours/docker/tp_podman) : `Podman` est un moteur de conteneur compatible avec l'API Docker conçu pour créer, exécuter et gérer des conteneurs et des pods Kubernetes sans nécessiter de démon, ce qui le rend idéal pour le développement et pour tester des pods Kubernetes en local sans nécessiter de cluster Kubernetes complet.
- [🏆 Projet Docker et Docker compose : application de vote](/cours/docker/projet_note_docker) : le but de ce TP est d'isoler et de déployer une application dans une stack de conteneurs Docker Compose.
  -  Sources git : <https://git.sr.ht/~toma/docker-vote>
- [🏆 Projet Dockerisation d'un Projet Multi-Composants](/cours/docker/projet_docker_dev) : le but de ce projet est de dockeriser un projet personnel existant qui se compose de plusieurs composants. 
- [🤯 Création de conteneur en utilisant les namespace natifs Linux](/cours/docker/container-from-namespace) : cet exercice montre comment créer des conteneurs sans Docker en utilisant directement les fonctionalités des namespace du noyau Linux.

## 󱃾 Kubernetes® 

- [🤓 Cours Kubernetes : initiation basique](/cours/docker/kubernetes-cours-mini)
- [🤓 Cours Kubernetes : l'intégral](/cours/docker/kubernetes-cours-full)
- [🤓 Cours Kubernetes orienté Développeur](/cours/docker/kubernetes-cours-dev)
- [🤓 Cours Kubernetes orienté Administrateur Système](/cours/docker/kubernetes-cours-admin)
- [🤓 Cheatsheet Kubernetes®](/cours/docker/kubernetes-cheatsheet)
- [󱃾  TP : Premiers pas avec Kubernetes](/cours/docker/tp_k8s) : l'objectif de ce TP est de découvrir Kubernetes® à travers une installation (très) simplifiée pour tester Kubernetes sur un seul serveur.
- 󱃾  Learn Kubernetes Basics: Tutoriels officiels pour débuter avec Kubernetes : <https://kubernetes.io/docs/tutorials/kubernetes-basics/>
- [󱃾  TP : Déploiement applicatif avec Helm](/cours/docker/tp_helm) : un TP pour découvrir Helm, installer des _Chart_ existantes et apprendre à créer sa propre Chart.
- [󱃾  TP : Monitoring de Kubernetes avec Prometheus et Grafana](/cours/docker/tp_prometheus_grafana_k8s) : un exemple pour mettre en place une infrastructure standard de monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation.
- [󱃾  TP : Logging centralisé d'un cluster Kubernetes](/cours/docker/tp_k8s_elk) : le logging centralisé est essentiel dans un environnement `Kubernetes` pour surveiller les applications et diagnostiquer les problèmes. Nous allons voir différentes solutions de logging centralisé : stack ELK, `Fluent`, `Loki`.
- [🏆 Projet Docker et Kubernetes : application de vote](/cours/docker/projet_vote_k8s) : le but de ce TP est d'isoler et de déployer une application dans une stack de conteneurs Kubernetes
  -  Sources git : <https://git.sr.ht/~toma/docker-vote>
- [🏆 Projet Installation d'un Cluster Kubernetes et déploiement d'une application](/cours/docker/projet_install_kubernetes)
- [🏆 Projet Administration d'un Cluster Kubernetes](/cours/docker/tp_administration_kubernetes)
- [🏆 Projet Déploiement  applicatif dans Kubernetes](/cours/docker/projet_appli_kubernetes)

## λ OpenFaaS

- [λ TP serverless : Fonctions-as-a-Service dans Kubernetes avec OpenFaaS](/cours/docker/openfaas-tp)
- [🏆 Projet OpenFaaS dans Kubernetes](/cours/docker/openfaas-projet)

