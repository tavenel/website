---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Déploiement continu GitOps avec Argo CD
layout: '@layouts/CoursePartLayout.astro'
date: 2025 / 2026
---

## Installation

1. Créer un namespace `argocd`
2. Installer ArgoCD dans le namespace `argocd`
3. Accéder à l'application web d'ArgoCD

## Dépôt Git

```
/overlays
  /dev
  /prod
/base
  deployment.yaml
  service.yaml
  […]
```

- Le répertoire `base/` contient les ressources Kubernetes pour déployer l'application
- Les répertoires `dev/` et `prod/` utilisent _Kustomize_ pour modifier des valeurs (variable `path:` de ArgoCD).

## Déploiement

1. Créer une ressource custom `Application` respectant la CRD d'ArgoCD pour un déploiement de dev.
2. Appliquer la ressource dans Kubernetes.

## Drift

Réaliser un test de dérive (_drift_) :

1. Modifier manuellement le nombre de pods via kubectl
2. Observer le comportement d'Argo CD. Comment réaliser une réconciliation automatique ?

## Production

1. Créer une ressource custom `Application` respectant la CRD d'ArgoCD pour un déploiement de production.
2. Appliquer la ressource dans Kubernetes.

## Stratégies de synchronisation

Modifier l'application dev pour tester :

1. Mode manuel
2. Mode automatique
3. Activation/désactivation de prune
4. Activation/désactivation du self-heal

## Ajouter un hook de synchronisation

Créer un job Kubernetes dans `overlays/dev` avec :

```yaml
metadata:
  annotations:
    argocd.argoproj.io/hook: PreSync
```

## Déploiement via Helm (optionnel)

1. Ajouter une _chart Helm_ à votre dépôt.
2. Créer une `Application` Argo CD qui utilise Helm comme source.

## Exercice : Pipeline GitOps

:::exo
Créer un workflow Git complet :

1. Commit → validation automatique
2. Merge en `main` → déclenchement du déploiement via Argo CD
3. Mise en place d'environnements dev et prod

### Livrables attendus

- Captures d'écran de l'interface Argo CD
- Manifests YAML
- Explication des choix d'architecture GitOps
- Analyse des dérives et correctifs apportés

:::

---

### Chart Helm

Afin de **déployer l'ensemble de votre application de manière automatisée et reproductible**, le déploiement final passera par une _Helm Chart_. Cette chart doit encapsuler tous les composants nécessaires à votre stack : services backend, frontend, base de données, services de cache ou de messagerie, configuration réseau, volumes persistants, etc.

Helm vous permet de **gérer l'ensemble des manifestes Kubernetes** (Deployment, Service, Ingress, Secret, ConfigMap…) via un système de templates et de valeurs paramétrables. Cela facilite non seulement le déploiement initial, mais aussi les mises à jour, les rollbacks et l'intégration avec des pipelines CI/CD ou GitOps.

Votre chart doit être **modulaire et configurable**, avec un fichier `values.yaml` bien documenté. Elle doit permettre de déployer votre stack dans différents environnements (dev, staging, prod) en changeant simplement les valeurs. Pensez également à inclure des `readinessProbe`/`livenessProbe`, des ressources (`limits`/`requests`), et à suivre les bonnes pratiques de sécurité (non-root, accès aux secrets, etc.).

### Ingress

Un Ingress agit comme un point d'entrée unique pour accéder à différents services au sein du cluster, permettant de diriger le trafic vers différentes versions d'une application en fonction de règles définies. La mise en place d'un Ingress pour un test A/B dans un environnement Kubernetes offre plusieurs avantages significatifs.

Pour un test A/B, cela signifie que vous pouvez facilement répartir le trafic entre deux versions d'une application (version A et version B) sans modifier l'infrastructure sous-jacente. Cela permet de comparer les performances et l'expérience utilisateur des deux versions en temps réel. L'Ingress facilite la gestion du trafic, permettant une répartition précise et contrôlée, et offre la flexibilité de modifier rapidement les règles de routage en fonction des résultats des tests. De plus, cela simplifie la collecte de données et l'analyse des résultats, car le trafic est géré de manière centralisée et cohérente.

:::exo
Configurer l'`Ingress` pour permettre un modèle de déploiement de type _A/B testing_.
:::
