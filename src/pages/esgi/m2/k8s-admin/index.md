---
title: 󱃾 Kubernetes
---

# 󱃾 Kubernetes

## 🎯 Objectifs du cours

- Connaître le fonctionnement de Kubernetes et ses différents composants
- Savoir installer, configurer et administrer Kubernetes dans un déploiement HA
- Être à même de placer automatiquement ses conteneurs sur un cluster ou dans le Cloud
- Savoir automatiser les déploiements d'applications conteneurisées
- Sécuriser le déploiement du cluster et des applications
- Superviser un cluster Kubernetes avec Prometheus et Grafana

## 📋 Prérequis

- Bonnes connaissances de Docker et des principes de conteneurisation
- Connaissances avancées en administration système Linux
- Les namespace et les cgroups Linux
- Bonnes notions de réseau, notamment routage et segmentation
- Connaissance des principes généraux d'un déploiement résilient H.A.

## 📅 Déroulé des séances

Module de 3*12H

Évaluation : CC et TP machine

## 📑 Documents

### Partie 1

- [🤓 Cours Kubernetes orienté Administrateur Système](/k8s/cours-admin)
- [🤓 Cheatsheet Kubernetes®](/k8s/cheatsheet)
- [󱃾 TP : Premiers pas avec Kubernetes](/k8s/tp-intro) : l'objectif de ce TP est de découvrir Kubernetes® à travers Minikube, une installation (très) simplifiée pour tester Kubernetes sur un seul serveur.
- [󱃾 TP Création de manifestes et déploiement d'une application containerisée avec kubectl](/k8s/tp-appli) : Exemple de création de manifestes et déploiement Kubernetes avec `kubectl` étape par étape, basé sur une mini-application à 2 services + 1 SGBDR containerisé.
- [🏆 Projet Installation d'un Cluster Kubernetes et déploiement d'une application](/k8s/projet-install)

### Partie 2

- [🏆 Projet Installation H/A d'un Cluster Kubernetes](/k8s/projet-install-ha)

### Partie 3

- [🏆 Projet Administration d'un Cluster Kubernetes](/k8s/tp-administration)
- [󱃾 TP : Monitoring de Kubernetes avec Prometheus et Grafana](/k8s/tp-prometheus-grafana) : un exemple pour mettre en place une infrastructure standard de monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation.
- [󱃾 TP : Logging centralisé d'un cluster Kubernetes](/k8s/tp-elk) : le logging centralisé est essentiel dans un environnement `Kubernetes` pour surveiller les applications et diagnostiquer les problèmes. Nous allons voir différentes solutions de logging centralisé : stack ELK, `Fluent`, `Loki`.

## 🚀 Pour aller plus loin

- Voir les autres ressources du [ cours sur Docker](/docker) et du [󱃾 cours sur Kubernetes](/k8s).
