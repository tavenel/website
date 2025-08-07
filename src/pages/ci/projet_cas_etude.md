---
title: Étude de cas CI/CD - de la théorie à la démonstration
date: 2025 / 2026
---

### 📝 Contexte

Vous faites partie de l'équipe DevOps d'une entreprise fictive nommée **DevFlow Corp**. Votre équipe est chargée de définir et démontrer une **stratégie CI/CD complète** pour un projet applicatif donné.

L'objectif est de simuler une situation réelle dans laquelle vous devez :

- Identifier les enjeux CI/CD du projet.
- Concevoir une solution technique adaptée.
- Mettre en œuvre un pipeline CI/CD fonctionnel.
- Présenter une démonstration et une documentation associée.

### 📦 Livrables attendus

1. **Étude de cas CI/CD** (document de 2 à 3 pages) :

   - Description du projet choisi (voir liste de suggestions).
   - Objectifs de la chaîne CI/CD.
   - Choix des outils CI/CD (ex: GitLab CI, GitHub Actions, Jenkins, etc.).
   - Description des étapes du pipeline.
   - Justification des choix techniques.

2. **Pipeline CI/CD opérationnel** :

   - Dépôt Git contenant le code source + fichier de pipeline.
   - Exécution automatisée avec logs visibles.

3. **Démonstration** :

   - Présentation du projet, du pipeline et de son fonctionnement.
   - Déclenchement d'une modification (commit/push) pour montrer l'exécution du pipeline.

4. **Documentation technique** :

   - README.md expliquant comment cloner, tester et utiliser le pipeline.
   - Schéma de l'architecture CI/CD

### 🔍 Contraintes techniques

- Le pipeline doit inclure **au moins 4 étapes** :
  1. **Build** de l'application (ou linting).
  2. **Tests automatisés**.
  3. **Analyse de code ou vérification de sécurité**.
  4. **Déploiement automatique ou en staging**.
- L'environnement peut être un conteneur Docker, une VM ou un service cloud gratuit (Vercel, Netlify, Heroku, Railway…).
- L'usage d'un fichier `.gitlab-ci.yml`, `.github/workflows/`, ou `Jenkinsfile` est recommandé.

### 🧠 Suggestions de cas d'étude possibles

Choisir **une seule** de ces proposition ou proposer un autre cas d'étude à faire valider :

| Cas d'étude                           | Description                                                                            |
| ------------------------------------- | -------------------------------------------------------------------------------------- |
| **Blog statique avec Jekyll ou Hugo** | Génération statique, tests de lien, publication automatique.                           |
| **API REST en Node.js / Python / Go** | Tests unitaires, linter, analyse SonarQube, déploiement sur Render ou Railway.         |
| **App front-end React/Vue**           | Build Webpack/Vite, tests avec Jest, publication sur Netlify ou Vercel.                |
| **Microservice Dockerisé**            | Build image Docker, tests, push sur Docker Hub, déploiement local avec Docker Compose. |
| **Application avec base de données**  | CI avec tests, déploiement de l'application et de la DB via Docker Compose.            |
| **Projet full DevSecOps**             | Pipeline avec scan de vulnérabilités, secret detection, policy gates, déploiement.     |


### 🧮 Grille d'évaluation

| Critère                                       | Points |
| --------------------------------------------- | ------ |
| Étude de cas claire, contextualisée, réaliste | 4 pts  |
| Pipeline CI/CD fonctionnel et reproductible   | 6 pts  |
| Qualité de la documentation technique         | 3 pts  |
| Justification des outils et étapes            | 3 pts  |
| Démonstration orale claire et bien menée      | 2 pts  |
| Pertinence des tests / déploiement            | 2 pts  |

