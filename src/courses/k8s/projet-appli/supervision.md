---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Supervision
layout: '@layouts/CoursePartLayout.astro'
date: 2024 / 2025
---

Le monitoring d'un cluster `Kubernetes` avec `Prometheus` pour la collecte des métriques et `Grafana` pour leur visualisation est une solution courante pour collecter, stocker et visualiser les métriques du cluster, des pods et des applications. Nous allons mettre en place cette infrastructure de monitoring.

:::exo

1. Mettre en place la supervision du cluster via `kube-prometheus-stack` (_Prometheus_ + _Grafana_) déployé via _Helm_
2. Exposer l'accès à _Grafana_ à l'extérieur du cluster via un _ingress_ : `traefik`

:::

:::link
Se référer au TP sur Prometheus et Grafana : <https://www.avenel.pro/k8s/tp-prometheus-grafana>
:::
