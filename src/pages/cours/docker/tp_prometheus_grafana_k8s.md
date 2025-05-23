---
title: Monitoring Kubernetes avec Prometheus et Grafana
date: 2024 / 2025
---

# Monitoring Kubernetes avec Prometheus et Grafana

## Introduction

Le monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation est une solution courante pour collecter, stocker et visualiser les métriques du cluster, des pods et des applications. Voici un exemple pour mettre en place cette infrastructure de monitoring.

:::link
Une installation courante de _Prometheus_ et _Grafana_ est réalisée via le packager _Helm_ en utilisant la _chart_ `kube-prometheus-stack` : c'est celle que nous utiliserons. Pour plus d'information, voir [le README](https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/README.md)
:::

## Installer Prometheus et Grafana avec Helm

`Helm` est un gestionnaire de packages pour `Kubernetes` qui facilite l'installation de chartes (charts) comme celles de `Prometheus` et `Grafana`. Si vous n'avez pas encore `Helm`, installez-le d'abord.

### Ajouter les dépôts Helm pour Prometheus et Grafana

``` bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

### Installer Prometheus & Grafana

Vous pouvez installer Prometheus à l'aide de la charte `Helm` `kube-prometheus-stack` (qui inclut à la fois Prometheus et les alertes associées) :

```sh
helm upgrade --install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

Cela installera `Prometheus`, `Alertmanager`, les `Node Exporters` (pour les métriques des nœuds), ainsi que `Grafana` dans le namespace monitoring.

:::tip
Vous pouvez ajouter les options `--set grafana.service.type=NodePort --set prometheus.service.type=NodePort` pour déployer un service de type _NodePort_ pour Prometheus et Grafana pour pouvoir facilement accéder aux dashboards.
:::

En cas de déploiement manuel, voici la procédure à suivre :

- Exécuter le serveur Prometheus dans un `Pod` (en utilisant un `Deployment` pour assurer son bon fonctionnement continu)
- Exposer l'interface web de Prometheus (par exemple avec un `NodePort`)
- Exécuter le _Node Exporter_ sur chaque `Node` (via un `DaemonSet`)
- Configurer un `ServiceAccount` pour permettre à Prometheus d'interroger l'API Kubernetes
- Configurer le serveur Prometheus (en stockant la configuration dans un `ConfigMap` pour faciliter les mises à jour)

### Vérifier l'installation de Prometheus

Pour vérifier que tout est correctement installé, vous pouvez utiliser la commande suivante :

```sh
kubectl get pods -n monitoring
```

Vous devriez voir plusieurs pods liés à `Prometheus`, `Alertmanager`, et `Grafana`.

### Recommandations

Assurez-vous toujours d'exécuter _Prometheus_ conformément aux recommandations de l'équipe Prometheus :

- Placez _Prometheus_ dans le même domaine de défaillance, c'est-à-dire sur le même réseau et au même emplacement géographique que les services surveillés.
- Utilisez un disque persistant pour conserver les données après chaque redémarrage de _Prometheus_.
-Utilisez la _compaction locale_ pour des rétentions plus longues.
- Ne modifiez pas les durées minimales des blocs _TSDB_.
- Ne faites pas de scaling de _Prometheus_ sauf si nécessaire : une seule instance _Prometheus_ est déjà efficace.

:::tip
En cas de besoin de scaling de _Prometheus_, il est possible d'utiliser _Thanos_.
:::

## Exposer Prometheus et Grafana

### Exposer Grafana

Utilisez la commande suivante pour exposer l'interface web de Grafana (en créant un tunnel, test uniquement) :

```sh
kubectl port-forward svc/prometheus-grafana 3000:80 -n monitoring
```

Accédez à `Grafana` en ouvrant un navigateur et en entrant l'URL suivante : <http://localhost:3000>.

:::tip
Il existe d'autres façons d'exposer le service : en tant que service de type `NodePort` ou `LoadBalancer`, derrière un `Ingresse` ou une `GatewayAPI`, …
:::

Le username par défaut est `admin`.
Le mot de passe est récupérable avec la commande suivante :

```sh
kubectl --namespace monitoring get secrets prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 -d ; echo
```

### Exposer Prometheus

Vous pouvez également exposer l'interface `Prometheus` :

```sh
kubectl port-forward svc/prometheus-kube-prometheus-prometheus 9090 -n monitoring
```

Accédez à Prometheus via l'URL : <http://localhost:9090>.

## Configurer Prometheus pour Monitorer Kubernetes

Les composants `Prometheus` déployés via `Helm` viennent déjà configurés pour scraper les métriques du cluster `Kubernetes`. Vous pouvez cependant ajuster la configuration si nécessaire. Voici où trouver la configuration :

```sh
kubectl edit configmap prometheus-kube-prometheus-prometheus -n monitoring
```

Prometheus collecte les métriques des `Kubelets`, des `Node Exporters`, des `APIServers`, et des `Services` exposant des métriques via des annotations comme :

```yaml
annotations:
  prometheus.io/scrape: "true" # pour activer la collecte
  prometheus.io/port: "9090" # pour indiquer le port utilisé
  prometheus.io/path: /metrics # pour préciser l'URI (`/metrics` par défaut)
```

## Exporters

### NodeExporter

Pour récupérer des sondes `Linux` automatiquement, on pourra utiliser le `NodeExporter` sur les _Node_, qui permet d'envoyer à `Prometheus` les informations liés à l'OS : <https://prometheus.io/docs/guides/node-exporter/>

### cAdvisor

Pour récupérer des sondes `Docker` automatiquement, on pourra utiliser `cAdvisor` sur les _Node_, qui permet d'envoyer à `Prometheus` les informations des conteneurs : <https://prometheus.io/docs/guides/cadvisor/>

## Configurer des Dashboards dans Grafana

`Grafana` est livré avec plusieurs tableaux de bord prédéfinis, mais vous pouvez en ajouter de nouveaux pour `Kubernetes`. Une fois connecté à `Grafana` :

- Allez dans `Connections` > `Data Sources`.
- Ajoutez une nouvelle source de données `Prometheus` avec l'URL : <http://prometheus-kube-prometheus-prometheus.monitoring.svc:9090>.
- Importez des Dashboards préconfigurés pour `Kubernetes`.

Par exemple, utilisez l'ID :

1. `2` pour importer un tableau de bord de monitoring de Prometheus.
2. `11074` pour une vue orientée Node Exporter (OS Linux "host").
3. `315` pour importer le tableau de bord classique de `Kubernetes` via Prometheus.
4. `15661` pour une vue orientée métriques des Nodes du cluster.
5. `11663` pour une les principales métriques des objets Kubernetes.
6. `22128` pour monitorer les `HorizontalPodAutoscaler`.
7. `11454` pour monitorer les `Volume`.
8. `14279` pour monitorer les `CronJob`.
9. `12006` pour monitorer l'_API Server_.
10. `20842` pour monitorer les certificats de _cert-manager_.
11. `15282` pour un cluster _k3s_.

:::link
Voir aussi les dashboards de la `kube-prometheus-stack` : <https://github.com/dotdc/grafana-dashboards-kubernetes>
:::

Vous pouvez aussi personnaliser les graphiques pour visualiser les métriques de vos pods, nœuds, et autres composants du cluster.

## Exemples de métriques utiles

Voici quelques exemples de métriques que vous pouvez surveiller avec `Prometheus` et visualiser avec `Grafana` :

### Métriques _Node_

- Utilisation du CPU, de la RAM et du disque sur l’ensemble du _Node_
- Nombre total de processus en cours d'exécution et leurs états
- Nombre de fichiers ouverts, sockets, et leurs états
- Activité d’I/O (disque, réseau), par opération ou volume
- Informations physiques/matérielles (si applicable) : température, vitesse des ventilateurs...
- API Server : Latence des requêtes, nombre de requêtes par seconde.

### Métriques _Conteneurs_

- Similaires aux métriques des _Node_
- Différences pour la RAM :
  - Distinction entre mémoire active et inactive
  - Une partie de la mémoire est partagée entre les conteneurs et gérée spécifiquement
- Suivi de l’activité d’I/O plus complexe :
  - Les écritures asynchrones peuvent entraîner des "charges" différées
  - Certains chargements en mémoire (page-ins) sont également partagés entre les conteneurs
- Voir : <http://jpetazzo.github.io/2013/10/08/docker-containers-metrics/>

### Métriques _applicatives_

- Métriques personnalisées liées à l’application et aux besoins métiers
- Performance système : latence des requêtes, taux d’erreur...
- Informations sur les volumes : nombre de lignes en base de données, taille des files de messages...
- Données métier : stock disponible, articles vendus, chiffre d’affaires...

## Configurer des Alertes

L'installation de `Prometheus` via `kube-prometheus-stack` comprend également `Alertmanager`. Vous pouvez définir des règles d'alerte pour surveiller des événements importants comme :

- Utilisation CPU ou mémoire élevée.
- Pods en état d'échec ou en attente depuis trop longtemps.
- Nœuds indisponibles.

Vous pouvez configurer des alertes dans les fichiers de configuration de `Prometheus` ou via des `CRD` (_Custom Resource Definitions_) associées aux règles d'alerte.


# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Prometheus® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Helm® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Grafana® is a registered trademark of Raintank, Inc. dba Grafana Labs (“Grafana Labs”).

