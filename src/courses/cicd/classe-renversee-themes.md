---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: 📚 Thèmes à répartir entre les groupes
layout: '@layouts/CoursePartLayout.astro'
---

## 1. Fondamentaux de l’intégration continue

### Objectifs

- Comprendre le **problème initial** (intégration tardive, conflits…)
- Définir CI vs CD vs DevOps

### Travail à réaliser

- Définir :
  - intégration continue
  - livraison continue
  - déploiement continu
- Identifier les bénéfices et limites

### Livrables attendus

- Frise historique
- Schéma pipeline simplifié

---

## 2. Gestion de code source et workflow

### Objectifs

- Comprendre le rôle central de Git dans la CI

### Travail à réaliser

- Étudier :
  - stratégies de branches (GitFlow, trunk-based)
  - pull request / merge request
- Lien entre commits et pipeline

### TP proposé

- Simuler un workflow avec validation automatique

---

## 3. Pipeline CI : concepts et architecture

### Objectifs

- Comprendre ce qu’est un pipeline

### Travail à réaliser

- Décomposer :
  - stages
  - jobs
  - runners / agents
- Expliquer pipeline as code

### Livrables

- Diagramme pipeline détaillé

---

## 4. Automatisation du build

### Objectifs

- Comprendre le rôle du build dans la CI

### Travail à réaliser

- Outils à comparer : Maven / Gradle / npm / make
- Gestion des dépendances

### TP

- Créer un build automatisé

---

## 5. Tests automatisés

### Objectifs

- Comprendre la place des tests dans la CI

### Travail à réaliser

- Typologie :
  - unitaires
  - intégration
  - end-to-end
- Notion de pyramide des tests

### TP

- Ajouter des tests dans un pipeline

---

## 6. Qualité du code et analyse statique

### Objectifs

- Introduire la qualité continue

### Travail étudiants

- Outils :
  - SonarQube
  - linters
- Notions :
  - dette technique
  - coverage

### Livrables

- Démonstration d’analyse automatique

---

## 7. Gestion des artefacts

### Objectifs

- Comprendre ce que produit un pipeline

### Travail étudiants

- Définir :
  - artefact
  - repository (Nexus, Artifactory)
- Versioning

### TP

- Publier un artefact

---

## 8. Déploiement automatisé

### Objectifs

- Introduire CD

### Travail étudiants

- Stratégies :
  - blue/green
  - rolling
- Environnements :
  - dev / staging / prod

### TP

- Déploiement simple automatisé

---

## 9. Infrastructure et environnements

### Objectifs

- Comprendre où s’exécute la CI

### Travail étudiants

- Concepts :
  - conteneurs
  - VM
  - Kubernetes
- Isolation des environnements

---

## 10. Outils CI/CD (comparatif)

### Objectifs

- Vision marché

### Travail étudiants

- Comparer :
  - GitLab CI
  - GitHub Actions
  - Jenkins
- Critères :
  - simplicité
  - extensibilité
  - scalabilité

### Livrable

- Tableau comparatif critique

---

## 11. Sécurité dans la CI/CD (DevSecOps)

### Objectifs

- Introduire la sécurité dès le pipeline

### Travail étudiants

- Concepts :
  - SAST / DAST
  - scan de dépendances
- Intégration dans pipeline

---

## 12. Monitoring et feedback

### Objectifs

- Boucle de feedback rapide

### Travail étudiants

- Métriques :
  - taux de succès
  - durée pipeline
- Observabilité

---

## 13. Bonnes pratiques et anti-patterns

### Objectifs

- Prise de recul

### Travail étudiants

- Identifier :
  - pipelines trop longs
  - tests instables
  - dépendances externes

---
