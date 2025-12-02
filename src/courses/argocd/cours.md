---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Introduction au GitOps et à Argo CD
layout: '@layouts/CoursePartLayout.astro'
tags:
- kubernetes
- devops
- argocd
---

## Présentation d'Argo CD

- Argo CD est un contrôleur Kubernetes de déploiement continu basé sur le principe GitOps.
- Il permet :

  - Le déploiement automatique depuis Git
  - La visualisation de l'état des applications
  - La gestion multi-environnements
  - Le rollback automatique

---

![Architecture d'ArgoCD](https://argo-cd.readthedocs.io/en/stable/assets/argocd_architecture.png)
<div class="caption">Architecture d'ArgoCD (source: documentation ArgoCD)</div>

---

## Architecture

### Composants principaux

- **API Server** : Interface REST/CLI/UI
- **Application Controller** : Compare l'état désiré et l'état réel
- **Repo Server** : Récupère et génère les manifests
- **Dex (optionnel)** : Gestion de l'authentification

### Workflow général

1. L'application est décrite dans Git
2. Argo CD lit les configurations
3. Le contrôleur compare l'état souhaité et l'état courant
4. Argo CD synchronise Kubernetes si nécessaire

---

## Installation

### Installation via kubectl

```bash
git clone https://github.com/argoproj/argo-cd.git
kubectl apply -n argocd -f argo-cd/manifests/install.yaml
```

### Accès à l'interface Web

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

- Accès : <https://localhost:8080>
- Récupération du mot de passe admin :

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

---

## Concepts clés

### Application

- L'entité principale dans Argo CD
- Décrit :

  - Source : repo Git, chemin, révisions
  - Destination : cluster, namespace
  - Stratégie de synchronisation

### Mode de synchronisation

- **Manuel** : nécessite action utilisateur
- **Automatique** : Argo CD synchronise dès qu'un changement Git est détecté
- Options :

  - Prune : supprime automatiquement les ressources Kubernetes qui ne sont plus présentes dans le dépôt Git.
  - SelfHeal : corrige automatiquement toute dérive entre l'état Git et l'état réel du cluster.
  - Sync waves : modifie l'ordre de déploiement des ressources
    - Chaque ressource peut recevoir une annotation : `argocd.argoproj.io/sync-wave: "0"`
    - Déploiement du plus petit `sync-wave` au plus grand

---

## Déployer une application

### Exemple de déploiement Nginx

Créer une application YAML :

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: nginx-app
  namespace: argocd
spec:
  destination:
    namespace: default
    server: https://kubernetes.default.svc
  project: default
  source:
    repoURL: https://github.com/example/nginx-demo
    path: manifests
    targetRevision: HEAD
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

Appliquer :

```bash
kubectl apply -f nginx-app.yaml
```

---

## Gestion multi-environnements

### Approches possibles

- **Branches Git** : dev, staging, prod
  - souvent déconseillé car demande des intégrations multiples de commits
- **Répertoires** : /dev, /staging, /prod
- **Kustomize** : _overlays_ par environnement
- **Helm** : valeurs différentes

### Exemple structure Kustomize

```
├── base
│   ├── deployment.yaml
│   └── service.yaml
└── overlays
    ├── dev
    │   └── kustomization.yaml
    └── prod
        └── kustomization.yaml
```

---

## Hooks, Waves, Health checks

### Sync Hooks

Permettent d'exécuter des actions avant/après déploiement.

- `PreSync`, `Sync`, `PostSync`, `SyncFail`

### Sync Waves

Permettent d'**orchestrer le déploiement par étapes**.

### Health checks personnalisés

- Possibilité de définir des _healthchecks_ personnalisés.

---

## RBAC et gestion de sécurité

### Authentification

- **Native**
- **Dex** (_OIDC_)

### Autorisations

- Gestion par rôles (`read-only`, `operator`, `admin`)

---

## Monitoring et observabilité

- Export des métriques Argo CD dans _Prometheus_
- Argo CD expose les logs des pod
