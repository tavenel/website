---
title: ☑️ Checklist Création de projet
---

# ☑️ Checklist Création de projet

_Modifié le: 2025-01-22_

## Gestion de projet

- Besoins, fonctionnalités, …
- Cycles de développement : itératif ? incrémental ? …
- Documentation : wiki, …
  - liens : graphe DAG (1 page principale)
	- Onboarding : Process de développement, Outils utiles, Liens dépôts, …

## Développement :

  - Choix d'architecture : REST API, Event-driven, Data-driven, synchrone vs asynchrone, …
  - Choix des technologies : maturité ? communauté ? licenses ?
	- Environnement de dev : plugins IDE, outils à installer, …

## Environnements : minimum dev + staging + production

- IaC dès le début, rester agnostique
- Monitoring
- Observabilité

## CI/CD :

- Dépôt(s) Git (monorepo vs multirepo). Modèle de branches ?
- Décrire le processus de pipeline => pull-request ?
	- Rafiner à chaque itération
- Étapes minimales : Build, Analyses de code, Tests unitaires, Tests end-to-end

## Sécurité :

- Modèle : STRIDE, PASTA, …
- Disaster Recovery => à tester !
  - (Chaos Computing)
 CVEs

## Data :

- Stockage(s)
- Flux
- Backups, restauration, …

