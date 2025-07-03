---
title: 📄 De la culture DevSecOps à la mise en oeuvre CI/CD
date: 2025 / 2026
---

## 🎯 Objectif du Projet

L'objectif de ce projet est de réaliser un nouveau projet web ou de récupérer un projet existant et de mettre en œuvre une stratégie de migration de la gestion de projet vers une culture DevSecOps, et la mise en oeuvre d'un pipeline CI/CD.

### 🧩 Objectifs pédagogiques

* Comprendre les enjeux et les bénéfices d’une approche DevSecOps.
* Savoir concevoir une chaîne CI/CD outillée intégrant les aspects Sécurité, Qualité et Livraison.
* Appréhender les rôles et pratiques collaboratives Dev(Sec)Ops.
* Mettre en œuvre une chaîne de livraison continue automatisée.
* Identifier les bons indicateurs pour piloter une transition DevOps.

## 🗂️ **Structure du TP**

Le TP est découpé en **4 modules** pratiques, chacun avec des livrables, des travaux collaboratifs et un apport technique. Le tout est intégré dans un dépôt Git central et orchestré par un outil CI/CD au choix (Jenkins ou GitLab CI).

## 🧱 Module 1 - Schématisation d’un pipeline DevSecOps

### 🎯 Objectifs :

- Créer un schéma illustrant un processus DevSecOps complet.
- Modéliser le pipeline CI/CD intégrant les volets Sécurité, Qualité, Tests et Déploiement.

### 🛠️ Activités :

- **Recherche et sélection des outils DevSecOps** : Identifiez les outils nécessaires pour chaque étape du processus DevSecOps (par exemple, Jenkins/GitLab pour CI/CD, SonarQube pour l'analyse de code, Docker pour la conteneurisation, etc.).
* Identification des **étapes du pipeline CI/CD** (build, test, analyse, déploiement…).
* Choix et justification des **outils CI/CD** (SonarQube, Trivy, Snyk, Vault, etc.).
* Réalisation d’un **schéma du pipeline** (diagramme ou outil comme Lucidchart, draw.io…).

## 🤝 Module 2 - Mise en place et animation d’une équipe Dev(Sec)Ops

### 🎯 Objectif :

Structurer et documenter une organisation DevSecOps, en intégrant les différents rôles et en tenant compte du client.

### 🛠️ Activités :

- **Définition des rôles** : Identifiez les rôles clés au sein de l'équipe (par exemple, développeur, ingénieur DevOps, expert en sécurité, chef de projet, etc.).
- **Intégration du client** : Définissez comment le client sera intégré dans le processus (réunions régulières, feedback, etc.).
* Définition de la **méthode de travail** (Scrum, Kanban ?)
* Choix des **outils** de communication, gestion de tickets, documentation.
* Mise en place d'un outil de **suivi** (GitLab Issues, Jira, Trello, Mattermost…)

## 📈 Module 3 - Indicateurs et Roadmap de transition DevSecOps

### 🎯 Objectif :

Identifier les bons KPI pour piloter une transformation DevOps et esquisser une roadmap.

### 🛠️ Activités :

* Recherche sur les **KPI DevOps** (par exemple, temps de déploiement, nombre de vulnérabilités détectées, temps moyen de résolution des incidents, etc.)
* Choix de **4 à 6 indicateurs** pertinents pour le projet
* Création d’un **dashboard fictif** (tableau, visuel, prometheus/grafana simulé)
- **Planification** : Planifiez les différentes phases de la transition, en incluant les objectifs, les livrables et les échéances (3 à 6 mois, avec jalons)

## ⚙️ Module 4 - Mise en œuvre d'un pipeline CI/CD

### 🎯 Objectif :

Mettre en œuvre un pipeline CI/CD sur Jenkins ou GitLab, incluant build, tests, et déploiement simple.

### 🛠️ Activités :

* Choix du **projet à livrer** (application simple, microservice, script avec tests unitaires…)
- **Choix de l’outil CI/CD** : Décidez si vous allez utiliser Jenkins ou GitLab CI/CD.
- **Installation et configuration** : Installez et configurez l'outil choisi. Pour Jenkins, cela peut inclure l'installation des plugins nécessaires. Pour GitLab, cela peut inclure la configuration des runners.
- **Création d’un pipeline simple** : Créez un pipeline simple pour un projet exemple. Cela peut inclure des étapes de build, de test et de déploiement, par exemple : lint → tests → build → analyse SAST → déploiement
- Intégration de **tests de sécurité** de base (Trivy, snyk, ou scan dockerfile)
- **Reporting** de la CI/CD : intégration avec Slack / Discord, mail en cas d'erreur, …
- **Déploiement** sur un environnement cible : VM, Docker, Kubernetes

