---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Construire une Secure Delivery Platform
date: 2026 / 2027
---

## Objectifs pédagogiques

- **Concevoir et déployer une chaîne CI/CD sécurisée** pour une application conteneurisée, du commit jusqu'au déploiement Kubernetes.
- **Intégrer des contrôles de sécurité automatisés** (SAST, secrets, dépendances, images, IaC) et définir des règles de blocage (*security gates*).
- **Administrer et documenter une plateforme de delivery** en comprenant les interactions entre Git, CI/CD, registry, sécurité et Kubernetes.
- **Évaluer la robustesse de la plateforme face à des tentatives d'attaque**, en adoptant ponctuellement une posture Red Team.
- Comprendre que la sécurité d'une chaîne DevSecOps dépend autant des **outils de détection** que de la **configuration des règles, permissions et processus de traitement des alertes**.

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

Une attention particulière devra être portée à la **sécurité de la chaîne elle-même** : un pipeline peut disposer de nombreux scanners et rester vulnérable si ses règles Git, ses variables CI/CD, ses permissions ou ses mécanismes de validation sont mal configurés.

## Architecture cible

L'architecture cible est volontairement simple pour conserver un focus sur le DevSecOps :

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

Les outils proposés peuvent être remplacés par des solutions équivalentes, à condition de justifier ce choix.

## Scénario

Vous recevez un dépôt initial contenant une mini application Flask, un Dockerfile et des manifests Kubernetes.

L'application fonctionne déjà, en revanche, **la chaîne de delivery est volontairement incomplète**.

Votre mission consiste à transformer ce dépôt en une **Secure Delivery Platform** capable de détecter et de bloquer automatiquement les problèmes de sécurité pertinents.

## Prise en main

1. Analyser l'application et la cloner localement.
2. Déployer l'application dans un cluster Kubernetes local.
3. Créer un premier pipeline : lint, test.
4. Améliorer le pipeline : build image, push registry.
5. Ajouter progressivement la sécurité dans un but DevSecOps :

- Secret scanning avec Gitleaks. Fournir volontairement un secret fictif dans une branche, par exemple :
  `AWS_ACCESS_KEY_ID=...`
- SAST avec Semgrep.
- Dépendances avec Trivy pour découvrir les CVE présentes dans les dépendances.
- Scan d'image après le build avec Trivy.
- Docker hardening.
- Scan des manifests / configuration Kubernetes avec Trivy.
- Scanner le cluster Kubernetes avec Trivy afin de faire le lien entre DevSecOps et sécurité de l'infrastructure.

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

Afin que le projet devienne réellement une **Secure Delivery Platform**, définir une politique simple, par exemple :

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

## Challenge final

Analyser une nouvelle version de l'application contenant plusieurs problèmes.

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

## Challenge Red Team inter-groupes

### Principe

Chaque groupe devra, à tour de rôle, adopter une posture **Red Team** et tenter de faire passer une modification malveillante ou dangereuse dans le projet d'un autre groupe.

L'objectif n'est **pas** de prendre le contrôle du projet ni de causer des dégâts, mais de déterminer si la **Secure Delivery Platform détecte et traite correctement une tentative d'attaque sur la chaîne de développement et de livraison**.

Le groupe attaquant cherche donc volontairement à exploiter un défaut de configuration ou un contrôle de sécurité insuffisant.

### Conditions d'accès aux dépôts

Afin de rendre le challenge réellement possible, les projets devront être configurés pour permettre l'interaction entre groupes.

Pendant la période du challenge :

- chaque groupe doit rendre son projet **accessible aux autres groupes** ;
- chaque groupe concurrent doit disposer au minimum d'un rôle **Developer** sur le projet ciblé ;
- les groupes doivent donc pouvoir :
  - cloner le dépôt ;
  - créer une branche ;
  - pousser du code sur une branche non protégée ;
  - ouvrir une Merge Request ;
  - déclencher le pipeline CI ;
  - consulter les résultats du pipeline ;
- le dépôt doit rester accessible pendant toute la durée de la phase Red Team ;
- les règles de CI doivent s'appliquer également aux branches et Merge Requests créées par les autres groupes.
- Chaque groupe dispose de **2** tentatives contre les projets des autres groupes.
- Les attaques doivent être réalisées **uniquement dans le dépôt prévu pour le challenge** et doivent rester limitées au périmètre pédagogique défini : injection de secret, merge-request malveillante, ... **L'attaque ne doit provoquer aucune perte d'information définitive pour le groupe attaqué**

### Attribution du bonus

- Le challenge Red Team constitue un **bonus pouvant aller jusqu'à +2 points** à la note finale.
- Le bonus est attribué au **groupe attaquant** lorsque la plateforme du groupe cible ne détecte pas correctement l'attaque ou la traite de manière insuffisante.
- Le bonus récompense **la qualité de la tentative et la démonstration**, et non la simple production de code volontairement malveillant.
- Une même faiblesse exploitée plusieurs fois ne donne pas droit à plusieurs bonus.

| Résultat de l'attaque                                                |      Bonus |
| -------------------------------------------------------------------- | ---------: |
| Attaque correctement détectée et bloquée                             |          0 |
| Détection réalisée mais traitement insuffisant                       |       +0,5 |
| Attaque non détectée mais sans impact sur la livraison               |       +0,5 |
| Attaque non détectée et livraison autorisée                          |         +1 |
| Attaque permettant un véritable contournement de plusieurs contrôles | jusqu'à +2 |

## Grille d'évaluation du projet

| Critère                          |     Points |
| -------------------------------- | ---------: |
| Application conteneurisée        |          2 |
| Pipeline CI fonctionnel          |          3 |
| Tests automatisés                |          1 |
| Secret scanning                  |          1 |
| SAST / dependency scanning       |          1 |
| Image scanning                   |          1 |
| Security gate                    |          2 |
| Déploiement Kubernetes           |          2 |
| Documentation / architecture     |          2 |
| Complexité de la réalisation     |          5 |
| **Bonus Red Team inter-groupes** | **+2 max** |
