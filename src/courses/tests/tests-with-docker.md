---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Tests dans des environnements conteneurisés avec Docker
tags:
- test
- docker
---

## Intérêt

- Docker permet de :
  - Créer des environnements **isolés** et **reproductibles**.
  - Réduire l'**écart** entre dev, test et prod.
  - Tester des **comportements réseau** ou **multi-services**.
- _Exemple : Tester une API Node.js avec une base PostgreSQL_

---

## Rappels sur Docker

- **Image** : modèle de conteneur (ex. : `python:3.11`, `nginx`, etc.).
- **Conteneur** : instance d’une image en exécution.
- **Dockerfile** : script de construction d’image.
- **docker-compose** : outil pour orchestrer plusieurs conteneurs.

---

## Exemples de types de tests en environnement conteneurisé

| Type de test         | Description | Exécution dans Docker |
|----------------------|-------------|------------------------|
| Tests unitaires      | Vérifient des unités de code isolées | Peu utile dans Docker sauf pour uniformiser l'environnement |
| Tests d'intégration  | Vérifient l'interaction entre composants | Conteneurs simulant les services externes (DB, API, MQ, etc.) |
| Tests end-to-end     | Vérifient le comportement global de l'application | Conteneur applicatif + réseau simulé |
| Tests de performance | Vérifient la tenue en charge | Conteneurs avec générateurs de charge |

---

## Cas d'usage : réseaux Docker pour simuler la production

- Simulation de **latence réseau** : `tc` dans un conteneur
- Tests avec des **microservices conteneurisés** : `docker-compose` avec plusieurs services
- Tests sur **différents systèmes** (OS, langages) : conteneurs multi-arch

---

## Intégration dans la CI/CD

Exemple avec _GitHub Actions_ :

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: testdb
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 20
      - run: npm install
      - run: npm test
```

---

## Bonnes pratiques

- **Isoler** les données de test (bases dédiées, volumes temporaires).
- *Nettoyer** après les tests (`--rm`, volumes temporaires).
- Utiliser des **images légères** (`alpine`).
- **Taguer** les images de test pour traçabilité.
- Intégrer dans le pipeline CI/CD avec les **mêmes images** que la prod.

---

## Liens

* [Testcontainers](https://www.testcontainers.org/): librairie Java pour créer des conteneurs de test à la volée.
* [Dockertest (Go)](https://github.com/ory/dockertest)

---


