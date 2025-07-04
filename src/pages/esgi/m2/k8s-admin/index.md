---
title: 󱃾 Kubernetes
layout: '@layouts/BaseLayout.astro'
---

# 󱃾  Kubernetes

### 📅 Déroulé des séances

Module de 2x18H

Évaluation : CC et TP machine

## Partie 1

### 🎯 Objectifs du cours

- Connaître le fonctionnement de Kubernetes et ses différents composants
- Savoir installer, configurer et administrer Kubernetes dans un déploiement HA

### 📋 Prérequis

- Bonnes connaissances de Docker et des principes de conteneurisation
- Connaissances avancées en administration système Linux
- Les namespace et les cgroups Linux
- Bonnes notions de réseau, notamment routage et segmentation
- Connaissance des principes généraux d'un déploiement résilient H.A.

### 📑 Documents

- [🤓 Cours Kubernetes orienté Administrateur Système](/cours/k8s/cours-admin)
- [🤓 Cheatsheet Kubernetes®](/cours/k8s/cheatsheet)
- [󱃾  TP : Premiers pas avec Kubernetes](/cours/k8s/tp) : l'objectif de ce TP est de découvrir Kubernetes® à travers Minikube, une installation (très) simplifiée pour tester Kubernetes sur un seul serveur.
- [🏆 Projet Installation d'un Cluster Kubernetes et déploiement d'une application](/cours/k8s/projet-install)

## Partie 2

### 🎯 Objectifs du cours

- Être à même de placer automatiquement ses conteneurs sur un cluster ou dans le Cloud
- Savoir automatiser les déploiements d'applications conteneurisées
- Sécuriser le déploiement du cluster et des applications
- Superviser un cluster Kubernetes avec Prometheus et Grafana

### 📑 Documents

- [🏆 Projet Administration d'un Cluster Kubernetes](/cours/k8s/tp-administration)
- [󱃾  TP : Monitoring de Kubernetes avec Prometheus et Grafana](/cours/k8s/tp-prometheus-grafana) : un exemple pour mettre en place une infrastructure standard de monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation.
- [󱃾  TP : Logging centralisé d'un cluster Kubernetes](/cours/k8s/tp-elk) : le logging centralisé est essentiel dans un environnement `Kubernetes` pour surveiller les applications et diagnostiquer les problèmes. Nous allons voir différentes solutions de logging centralisé : stack ELK, `Fluent`, `Loki`.

## 🚀 Pour aller plus loin

- Voir les autres ressources du [  cours sur Docker & Kubernetes](/cours/docker).
