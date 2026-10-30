---
title: CI/CD - Intégration et Déploiement continus dans Kubernetes
description: CI/CD - Intégration et Déploiement continus dans Kubernetes
type: cours
sidebar:
  order: 6
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
date: 2024 / 2025
---
L'adoption de pratiques CI/CD est cruciale pour assurer une livraison rapide, fiable et efficace des nouvelles fonctionnalités et corrections, tout en minimisant les risques d'erreurs humaines. Dans cette section, vous allez mettre en place les différentes étapes du pipeline depuis l'intégration du code source jusqu'au déploiement en production en passant par les tests automatisés et la gestion des artefacts.

### 🦊 Installation de Gitlab

Nous allons utiliser Gitlab comme serveur d'intégration continue, registry Docker et serveur de déploiement continu. Déployer Gitlab dans Kubernetes via Helm.

```sh
helm repo add gitlab https://charts.gitlab.io/
helm show values gitlab/gitlab > values.yaml
# Modifier le fichier `values.yaml` avec les valeurs souhaitées
helm upgrade --install gitlab gitlab/gitlab -f values.yaml
```

:::caution
La helm chart Gitlab est très gourmande en ressources. Pour un serveur d'intégration continue alternatif, on pourra déployer <https://gittea.dev/> qui est compatible avec la CI/CD de Github : <https://docs.gitea.com/installation/install-on-kubernetes>
:::

### Pipeline simple CI/CD

:::exo
Créer une **premier pipeline** GitLab CI pour :

- Créer les composants de votre application : images Docker du backend & frontend
- Publier ces images dans la registry Gitlab
- Déployer votre application sur Kubernetes via Helm.

:::

:::note

- Pour apprendre à utiliser Gitlab pour stocker ses images docker, voir : <https://blog.stephane-robert.info/post/gitlab-container-docker-registry/>

:::
