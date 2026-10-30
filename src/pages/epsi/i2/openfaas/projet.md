---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: λ TP Noté - Déploiement d'une application serverless complète avec OpenFaaS
date: 2025 / 2026
---

## 🎯 Objectifs pédagogiques

**Assembler plusieurs fonctions en une application cohérente illustrant un workflow serverless**.

À l'issue de ce TP, vous serez capable de :

* Concevoir une application découpée en plusieurs **fonctions serverless** autonomes et interconnectées.
* Déployer ces fonctions avec OpenFaaS et orchestrer leur exécution en un **workflow logique**.
* Gérer la configuration, les données sensibles, et la communication entre fonctions.
* Utiliser les **bons patterns serverless** (fan-out, pipelines, pub/sub, enrichment, etc.).

## 📦 Contexte

Vous êtes développeur cloud dans une startup qui souhaite adopter une architecture **serverless** pour lancer un **MVP** rapide.

Votre mission est de concevoir et déployer une application composée **d'au moins 3 fonctions** autonomes, capables d'interagir entre elles pour former un workflow cohérent.

## 🗂 Sujet

Le **choix du cas d'usage est libre**, mais vous devez respecter les contraintes suivantes :

1. **Minimum 3 fonctions distinctes**, chacune avec une responsabilité claire.
2. Les fonctions doivent **communiquer entre elles** :
   * via HTTP (REST API)
   * et/ou via un **système de messagerie** (ex: NATS, Kafka, RabbitMQ).
3. Une **API externe** doit être utilisée dans au moins une fonction.
4. Une fonction doit **interagir avec une base de données** (PostgreSQL, MongoDB, etc.).
5. Utilisation rigoureuse de :
   * `secrets` pour les informations sensibles
   * `configmaps` ou `environment` pour les configurations
6. Fournir une documentation claire et un script ou collection Postman pour tests.
7. **Monitoring obligatoire** :
   * La fonction doit exposer des métriques Prometheus
   * Présenter comment suivre l'usage, les erreurs, ou la latence via OpenFaaS UI ou Prometheus.
8. Au moins une fonction doit être configurée pour utiliser l'**auto-scaling**.

## 💡 Exemples de projets possibles

| Idée d'application                | Fonctions possibles                                     |
| --------------------------------- | ------------------------------------------------------- |
| Générateur de rapport météo PDF   | `fetch-city`, `weather-enrich`, `pdf-generate`          |
| Analyse de tweets                 | `scraper`, `analyzer`, `store-results`                  |
| Formulaire d'inscription sécurisé | `validate`, `store-user`, `notify-email`                |
| Traitement d'image                | `upload`, `resize`, `watermark`                         |
| Agrégation de données publiques   | `fetch-source-a`, `fetch-source-b`, `aggregate-results` |
| Bot Discord de résumé d'un lien | `receive-message` (Webhook), `fetch-content`, `summarize-text`, `send-discord-reply` |


## 📁 Livrables attendus

1. **Une archive du code source** : code commenté et structuré pour chaque fonction, …
2. **README.md** détaillant :
   * Objectif de l'application
   * Description de chaque fonction
   * Dépendances (DB, broker, APIs)
   * Étapes de déploiement (`faas-cli deploy`)
   * Étapes de test
3. **Scripts de test** reproductibles

## 📝 Barème


| Critère                                                 | Points | Commentaire |
| ------------------------------------------------------- | ------ | -------------------------------------------------------------------------------------------- |
| Respect des contraintes techniques générales            | 4 pts  | 3 fonctions minimum, API externe, base de données, secrets/env vars utilisés correctement    |
| Architecture cohérente du workflow                      | 2 pts  | Fonctionnalités correctement réparties entre les fonctions, pas de logique dupliquée         |
| Interfonctionnalité / Appel croisé HTTP ou via broker   | 3 pts  | Testable et stable                                                                           |
| Monitoring Prometheus configuré et démontré             | 2 pts  | Affichage via UI ou requête directe Prometheus                                               |
| Scaling automatique opérationnel                        | 3 pts  | Test de montée en charge possible (ex : `hey`, `ab`, ou boucles `curl`)                    |
| Qualité du code et organisation du dépôt                | 2 pts  | Séparation logique, documentation inline, scripts propres                                  |
| Tests reproductibles (curl, Postman, script bash, etc.) | 2 pts  | Inclure `curl-test.sh`, `postman_collection.json`, etc.                                    |
| README clair et complet                                 | 2 pts  | Déploiement, tests, explication de l'architecture                                            |
| Bonus | -      | Orchestration (faas-flow), stockage d'état, front léger, logs avancés, circuit breaker, etc. |


