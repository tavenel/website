---
title: 󱃾 Kubernetes
---

# 󱃾 Kubernetes

## 📅 Déroulé des séances

2 Modules : 14H de TP et 4H de cours (après e-learning)

Évaluation : Projet et QCM théorique

## 🎯 Objectifs du cours

- Être capable de mettre en place un cluster Kubernetes, soit dans le cloud (AKS,GKE, etc), soit "baremetal" (k3s, k0s, Talos Linux, etc)
- Administrer un cluster Kubernetes
- Comprendre les différents types de ressources d'un cluster Kubernetes (pods, ReplicaSets, déploiements, statefulsets, services, etc)
- Créer, modifier, supprimer des ressources Kubernetes
- Déployer des applicatifs simples (`Wordpress`, `Gitea`) de façon sécurisée dans un cluster Kubernetes
- Monter des Volumes Persistants, Secrets et ConfigMaps dans un Pod
- Être capable d'exposer des services Kubernetes à l'intérieur et à l'extérieur du cluster
- Découvrir Helm et être capable de l'utiliser pour déployer des applicatifs (Prometheus stack, etc)
- Être capable de déployer une classe de stockage
- Être capable de déployer un LoadBalancer
- Être capable de déployer un Ingress
- Être capable de créer un conteneur à partir d'un applicatif développé en cours et de l'envoyer sur un dépôt (public ou privé suivant moyens)
- Être capable de déployer ce conteneur dans un espace de noms dédié et de l'exposer à l'extérieur soit via un Service de type Load-Balancer soit via un Ingress
- Découvrir les opérateurs et déployer une base de données via l'opérateur Postgresql (Zalando ou Crunchy data) ou l'opérateur mariadb-galera

## 📋 Prérequis

- Bonnes connaissances de Docker et des principes de conteneurisation
- Connaissances avancées en administration système Linux
- Les namespace et les cgroups Linux
- Notions de réseau

## 📑 Documents

- [🔀 Module en classe renversée](/epsi/i2/k8s/classe-renversee)
- [🤓 Cours Kubernetes orienté Développeur](/k8s/cours-dev)
- [🤓 Cheatsheet Kubernetes®](/k8s/cheatsheet)
- [󱃾 TP : Premiers pas avec Kubernetes](/k8s/tp-intro) : l'objectif de ce TP est de découvrir Kubernetes® à travers une installation (très) simplifiée pour tester Kubernetes sur un seul serveur.
- [󱃾 TP Création de manifestes et déploiement d'une application containerisée avec kubectl](/k8s/tp-appli) : Exemple de création de manifestes et déploiement Kubernetes avec `kubectl` étape par étape, basé sur une mini-application à 2 services + 1 SGBDR containerisé.
- [󱃾 TP : Déploiement applicatif avec Helm](/k8s/tp-helm) : un TP pour découvrir Helm, installer des _Chart_ existantes et apprendre à créer sa propre Chart.
- [󱃾 TP : Monitoring de Kubernetes avec Prometheus et Grafana](/k8s/tp-prometheus-grafana) : un exemple pour mettre en place une infrastructure standard de monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation.
- [🏆 Projet Déploiement applicatif dans Kubernetes](/epsi/i2/k8s/projet)

## 🚀 Pour aller plus loin

- Voir les autres ressources du [ cours sur Docker](/docker) et du [󱃾 cours sur Kubernetes](/k8s).
