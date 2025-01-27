---
title: Monitoring Kubernetes avec Prometheus et Grafana
author: Tom Avenel
date: 2024 / 2025
correction: false
---

# Monitoring Kubernetes avec Prometheus et Grafana

## Introduction

Le monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation est une solution courante pour collecter, stocker et visualiser les métriques du cluster, des pods et des applications. Voici un exemple pour mettre en place cette infrastructure de monitoring.

## Installer Prometheus et Grafana avec Helm

`Helm` est un gestionnaire de packages pour `Kubernetes` qui facilite l'installation de chartes (charts) comme celles de `Prometheus` et `Grafana`. Si vous n'avez pas encore `Helm`, installez-le d'abord.

### Ajouter les dépôts Helm pour Prometheus et Grafana

``` bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

### Installer Prometheus

Vous pouvez installer Prometheus à l'aide de la charte `Helm` `kube-prometheus-stack` (qui inclut à la fois Prometheus et les alertes associées) :

```bash
helm upgrade --install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

Cela installera `Prometheus`, `Alertmanager`, les `Node Exporters` (pour les métriques des nœuds), ainsi que `Grafana` dans le namespace monitoring.

### Vérifier l'installation de Prometheus

Pour vérifier que tout est correctement installé, vous pouvez utiliser la commande suivante :

```bash
kubectl get pods -n monitoring
```

Vous devriez voir plusieurs pods liés à `Prometheus`, `Alertmanager`, et `Grafana`.

## Exposer Prometheus et Grafana

### Exposer Grafana

Utilisez la commande suivante pour exposer l'interface web de Grafana en tant que service de type `NodePort` ou `LoadBalancer` :

```bash
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
```

Accédez à `Grafana` en ouvrant un navigateur et en entrant l'URL suivante : <http://localhost:3000>.

Le username par défaut est `admin`.
Le mot de passe est récupérable avec la commande suivante :

```bash
kubectl get secret --namespace monitoring prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

### Exposer Prometheus

Vous pouvez également exposer l'interface `Prometheus` :

```bash
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090 -n monitoring
```

Accédez à Prometheus via l'URL : <http://localhost:9090>.

## Configurer Prometheus pour Monitorer Kubernetes

Les composants `Prometheus` déployés via `Helm` viennent déjà configurés pour scraper les métriques du cluster `Kubernetes`. Vous pouvez cependant ajuster la configuration si nécessaire. Voici où trouver la configuration :

```bash
kubectl edit configmap prometheus-kube-prometheus-prometheus -n monitoring
```

Prometheus collecte les métriques des `Kubelets`, des `Node Exporters`, des `APIServers`, et des `Services` exposant des métriques via des annotations comme :

```yaml
annotations:
  prometheus.io/scrape: "true"
  prometheus.io/port: "8080"
```

## Configurer des Dashboards dans Grafana

`Grafana` est livré avec plusieurs tableaux de bord prédéfinis, mais vous pouvez en ajouter de nouveaux pour `Kubernetes`. Une fois connecté à `Grafana` :

- Allez dans `Connections` > `Data Sources`.
- Ajoutez une nouvelle source de données `Prometheus` avec l'URL : <http://prometheus-kube-prometheus-prometheus.monitoring.svc:9090>.
- Importez des Dashboards préconfigurés pour `Kubernetes`.

Par exemple, utilisez l'ID `3119` pour importer un tableau de bord `Kubernetes` ou l'ID `6417` pour les métriques de pods.

Vous pouvez aussi personnaliser les graphiques pour visualiser les métriques de vos pods, nœuds, et autres composants du cluster.

## Exemples de métriques utiles

Voici quelques exemples de métriques que vous pouvez surveiller avec `Prometheus` et visualiser avec `Grafana` :

- Métriques des pods : Utilisation CPU, utilisation de la mémoire, redémarrages, statut de readiness.
- Métriques des nœuds : Utilisation des ressources (CPU, mémoire, stockage), saturation des nœuds, nombre de pods par nœud.
- API Server : Latence des requêtes, nombre de requêtes par seconde.
- Métriques d'application : Exposez des métriques personnalisées via le client `Prometheus` (`Go`, `Python`, `Java`) dans votre application.

## Configurer des Alertes

L'installation de `Prometheus` via `kube-prometheus-stack` comprend également `Alertmanager`. Vous pouvez définir des règles d'alerte pour surveiller des événements importants comme :

- Utilisation CPU ou mémoire élevée.
- Pods en état d'échec ou en attente depuis trop longtemps.
- Nœuds indisponibles.

Vous pouvez configurer des alertes dans les fichiers de configuration de `Prometheus` ou via des `CRD` (_Custom Resource Definitions_) associées aux règles d'alerte.


# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Prometheus® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Helm® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Grafana® is a registered trademark of Raintank, Inc. dba Grafana Labs (“Grafana Labs”).

