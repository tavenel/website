---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Construire une Secure Delivery Platform
date: 2026 / 2027
---

## Objectifs pédagogiques

- **Concevoir et déployer une chaîne CI/CD sécurisée** pour une application conteneurisée, du commit jusqu'au déploiement Kubernetes.
- **Intégrer des contrôles de sécurité automatisés** (SAST, secrets, dépendances, images, IaC) et définir des règles de blocage (*security gates*).
- **Administrer et documenter une plateforme de delivery** en comprenant les interactions entre Git, CI/CD, registry, sécurité et Kubernetes.

## Contexte

Une équipe de développement fournit une petite application web conteneurisée. L'équipe d'administration doit mettre en place une plateforme permettant de :

- récupérer le code depuis Git ;
- construire une image conteneurisée ;
- vérifier automatiquement la qualité et la sécurité du code ;
- analyser les dépendances et l'image ;
- publier l'image dans un registry ;
- déployer automatiquement l'application sur Kubernetes ;
- empêcher la livraison lorsqu'un contrôle de sécurité critique échoue ;
- conserver les traces des différentes étapes de la livraison.

L'objectif n'est **pas** de construire une plateforme Kubernetes complète. Kubernetes est utilisé comme environnement cible afin de reproduire une chaîne de livraison moderne (et est optionnel).

## Architecture cible

L'architecture cible est volontairement simple  pour un focus sur le DevSecOps :

```text
 ┌──────────────────┐
 │   Git repository │
 │                  │
 │ application      │
 │ Dockerfile       │
 │ Kubernetes       │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │    CI pipeline   │
 │                  │
 │ 1. lint          │
 │ 2. tests         │
 │ 3. SAST          │
 │ 4. dependencies  │
 │ 5. secrets       │
 │ 6. build image   │
 │ 7. image scan    │
 └────────┬─────────┘
          │
    security gate
          │
 ┌────────▼─────────┐
 │ Container        │
 │ Registry         │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │    Kubernetes    │
 │                  │
 │ Deployment       │
 │ Service          │
 │ Config/Secret    │
 └────────┬─────────┘
          │
          ▼
 ┌──────────────────┐
 │    Web app       │
 └──────────────────┘
```

Proposition de stack technique standard :

| Fonction       | Outil                      |
| -------------- | -------------------------- |
| Git            | GitLab                     |
| CI/CD          | GitLab CI                  |
| Container      | Docker / Podman            |
| Registry       | GitLab Container Registry  |
| SAST           | Semgrep                    |
| Dépendances    | Trivy                      |
| Secrets        | Gitleaks                   |
| Image scanning | Trivy                      |
| Kubernetes     | Kind ou K3d                |
| Déploiement    | `kubectl`                  |
| Manifests      | YAML Kubernetes            |
| Application    | petite application fournie |

## Scénario

Vous recevez un dépôt initial [TODO] :

```text
secure-delivery/
├── app/
│   ├── src/
│   ├── tests/
│   ├── requirements.txt
│   └── ...
│
├── Dockerfile
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── namespace.yaml
│
└── README.md
```

L'application fonctionne déjà, en revanche, **la chaîne de delivery est volontairement incomplète**.

Votre mission consiste à transformer ce dépôt en une plateforme de delivery sécurisée.

## Prise en main

1. Analyser l'application et la cloner localement
2. Déployer l'application dans un cluster Kubernetes local
3. Créer un premier pipeline : lint, test
4. Améliorer le pipeline : build image, push registry
5. Ajouter progressivement la sécurité dans un but DevSecOps :

- Secret scanning avec Gitleaks. Fournir volontairement un secret fictif dans une branche, par exemple `AWS_ACCESS_KEY_ID=...`
- SAST avec Semgrep.
- Dépendances avec Trivy pour découvrir les CVE présentes dans les dépendances.
- Scan d'image après le build avec Trivy (puis Docker hardening).
- Scanner le cluster Kubernetes avec Trivy pour faire le lien entre DevSecOps et sécurité de l'infrastructure.

Le pipeline devient :

```text
              ┌── SAST
              │
              ├── dependency scan
              │
lint → test ──┼── secret scan
              │
              └── IaC scan
                    │
                    ▼
                 build
                    │
                    ▼
               image scan
                    │
                    ▼
                  push
```

## Security Gate et déploiement

Afin que le projet devient réellement une **Secure Delivery Platform**, définir une politique simple, par exemple :

```text
CRITICAL → pipeline bloqué
HIGH     → pipeline bloqué
MEDIUM   → warning
LOW      → information
```

Le pipeline devient :

```text
                 ┌───────────────┐
                 │     Git       │
                 └───────┬───────┘
                         │
                         ▼
                ┌─────────────────┐
                │      Tests      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Security scans  │
                └────────┬────────┘
                         │
                    Security Gate
                    /           \
                  FAIL           PASS
                   │               │
                   X               ▼
                             Build image
                                  │
                                  ▼
                              Trivy scan
                                  │
                             Security Gate
                                  │
                                  ▼
                                Push
                                  │
                                  ▼
                              Deploy K8s
```

## Démonstration

Faire une démonstration de l'exécution du pipeline en créant un nouveau commit et expliquer le processus DevSecOps complet mis en place :

```text
commit
  ↓
pipeline
  ↓
security scan
  ↓
security gate
  ↓
image
  ↓
registry
  ↓
Kubernetes
  ↓
application
```

### Challenge final

Analyser une nouvelle version de l'application contenant plusieurs problèmes [TODO].

Par exemple :

```text
Challenge branch
├── secret exposé
├── dépendance vulnérable
├── mauvaise configuration Docker
├── mauvaise configuration Kubernetes
└── vulnérabilité applicative
```

Vous devez montrer que votre plateforme :

1. détecte les problèmes ;
2. produit des rapports ;
3. bloque les problèmes définis comme critiques ;
4. autorise une livraison lorsque les contrôles passent.

## Grille d'évaluation

| Critère                      | Points |
| ---------------------------- | -----: |
| Application conteneurisée    |      2 |
| Pipeline CI fonctionnel      |      3 |
| Tests automatisés            |      1 |
| Secret scanning              |      1 |
| SAST / dependency scanning   |      1 |
| Image scanning               |      1 |
| Security gate                |      2 |
| Déploiement Kubernetes       |      2 |
| Documentation / architecture |      2 |
| Complexité de la rélisation  |      5 |
