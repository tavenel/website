---
title: Helm
date: 2024 / 2025
---

# Déploiement applicatif avec Helm

## Introduction

`Helm` est un outil et une CLI de _gestion de paquets_ pour Kubernetes qui permet de déployer et de gérer des applications Kubernetes de manière _déclarative_.

- Les `charts` Helm sont des packages qui encapsulent des configurations Kubernetes, des `templates`, et d'autres ressources nécessaires pour déployer une application.
- Les `templates` sont des fichiers de ressources Kubernetes qui utilisent le système de _templates Go_.
- Le fichier `values.yaml` contient les valeurs par défaut (modifiables) pour les templates de la `chart`.
- Les `charts` sont distribuées en ligne dans des `repositories` (publics ou privés)
- Une instance de la `chart` déployée dans le cluster est appelée `release`. Une `release` est versionnée : (des)installation, upgrade, rollback
- Il est possible d'ajouter des `hooks` autour des `releases` : avant / après installation, upgrade, …

:::warn
Attention : tout comme les images Docker, une chart Helm permet de récupérer des configurations et un packaging distribués en ligne. Il faut donc toujours bien vérifier les charts que l'on utilise (`repository` officiel, …)
:::

:::link
- Voir la [cheatsheet Kubernetes](/cours/docker/kubernetes-cheatsheet) pour les commandes.
- Voir le [TP Prometheus & Grafana](/cours/docker/tp_prometheus_grafana_k8s) pour apprendre à déployer Prometheus et Grafana en utilisant Helm.
- Voir le lien suivant pour un tutoriel : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/helm/>
:::

## Exemples de charts Helm populaires

1. **MySQL** :
   - **Description** : Déploie une instance MySQL.
   - **Repository** : `bitnami/mysql`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-mysql bitnami/mysql
     ```

2. **WordPress** :
   - **Description** : Déploie une instance WordPress avec une base de données MySQL.
   - **Repository** : `bitnami/wordpress`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-wordpress bitnami/wordpress
     ```

3. **MongoDB** :
   - **Description** : Déploie une instance MongoDB.
   - **Repository** : `bitnami/mongodb`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-mongodb bitnami/mongodb
     ```

4. **Redis** :
   - **Description** : Déploie une instance Redis.
   - **Repository** : `bitnami/redis`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-redis bitnami/redis
     ```

5. **Nginx** :
   - **Description** : Déploie une instance Nginx.
   - **Repository** : `bitnami/nginx`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-nginx bitnami/nginx
     ```

6. **PostgreSQL** :
   - **Description** : Déploie une instance PostgreSQL.
   - **Repository** : `bitnami/postgresql`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-postgresql bitnami/postgresql
     ```

7. **Kubernetes Dashboard** :
   - **Description** : Déploie le Kubernetes Dashboard pour la gestion visuelle du cluster.
   - **Repository** : `kubernetes/dashboard`
   - **Exemple de commande** :
     ```sh
     helm repo add kubernetes https://kubernetes.github.io/dashboard
     helm install my-dashboard kubernetes/dashboard
     ```

8. **Prometheus & Grafana** :
   - **Description** : Déploie la stack Prometheus & Grafana pour la surveillance et la collecte de métriques.
   - **Repository** : `prometheus-community/prometheus`
   - **Exemple de commande** :
     ```sh
     helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
		 helm install my-prometheus prometheus-community/kube-prometheus-stack
		 # ou seulement Prometheus :
		 # helm install prometheus-community/prometheus
     ```

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Helm® is a registered trademark of The Linux Foundation in the United States and/or other countries.

