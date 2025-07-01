---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Impact des tests sur l'intégration
keywords:
- integration
- tests
- ci
---

## 🛠️ Introduction

- 🔄 **Impact fort sur les processus d'intégration d'un système.**
- ⏳ Parfois vus comme un frein à la réactivité…
- 🕵️ …mais détectent des problèmes inhérents à la gestion du projet mis "sous le tapis"

---

⏰ Ce sont donc souvent des bombes à retardement lorsque la problématique apparaît en production et qu'aucun processus n'a été pensé en amont (récupération de données de test, réinitialisation d'un système, modification de données pendant l'exécution, gestion des logs, ...)

---

## 🔮 Anticiper

- 📅 Dédier des cycles du projet à des environnements et des outils d'intégration pour anticiper les problèmes en production :
  - 🧪 tests
  - 📊 monitoring
  - 📝 gestion des logs
  - 🔄 aide au redéploiement
  - …
- 💰 Généralement très rentable

---

🔧 Les réflexions et la mise en place des processus d'intégration (y compris les tests) se font dès le début du projet !

---

## ⚠️ Risques et coûts

Quelques exemples de risques :
- 😟 Altérer la confiance des utilisateurs : service non accessible, …
- 📜 Non-conformité aux réglementations : _RGPD_, …
- 🔒 Atteinte à la sécurité des données : perte de données, vol d'informations personnelles

---

💸 Toutes ces risques ont un coût important lorsqu'ils se produisent : on essaiera donc de faire correspondre le coût des tests au risque financier qu'ils protègent.

---

## 🏛️ Gouvernance

Les tests d'intégration constituent l'étape où l'on commence à assembler les briques applicatives unitaires pour construire un Système d'Information.
- 🤝 On passe du chacun pour soi à un système commun
- 🤹 Ne pas négliger les besoins des autres applications
  - d'un modèle producteur / consommateur à un modèle collaboratif
- ⚖️ Problèmes de gouvernance et d'arbitrage
  - À clarifier dès le début du projet
  - Décrire un processus clair

---

## 🤝 Entraide

- 🤗 Créer un climat de confiance et **d'aide aux investigations** :
  - entraide plutôt que compétition
  - transmission du savoir
- 👥 Ne pas séparer l'équipe d'intégration
  - une seule équipe porte l'ensemble de la responsabilité (Scrum, …)

---

## 🤔 Réflexions

- ⏳ Si trop de temps passé aux investigations :
  - soit l'équipe est en sous-effectif
  - soit les outils (monitoring, logs, …) ne sont pas adaptés
- 🛠️ Réfléchir constamment aux outils et processus permettant d'améliorer les investigations

---

## 🔧 Prioriser les corrections d'erreurs

- 📉 Dette technique : coût futur de tous les problèmes techniques (bugs, mauvaises pratiques, … )
- Sans correction, la dette technique augmente avec le projet et le temps
  - le même problème est de plus en plus difficile à corriger !
- ⏳ Ces erreurs vont aussi faire perdre du temps à tous les consommateurs du service ou de la fonctionnalité
  - l'impact d'une erreur sur l'avancée d'un projet est vite exponentielle.

---

- 🛠️ Solution : prioriser la correction des erreurs :
  - Gestion de processus d'exception ;
  - Arrêt du développement pour corrections critiques ;
  - Budgétisation des erreurs non corrigées et intégration dans les rapports projet.

---

## 🧪 Tests critiques

- 🔍 Ensemble de tests à tourner obligatoirement avant de continuer à une autre étape du processus
- 🛡️ Bonne pratique pour limiter les régressions.

---

Dans la pratique :
- 🔄 Ensemble de tests à valider avant d'intégrer en pré-production
  - Évite d'impacter les autres services lors de l'intégration
- ✅ Ensemble de tests manuels d'acceptation avant la mise en production.
  - Minimise les faux positifs à cause d'incohérences difficiles à automatiser (IHM, …)

---

## 🌐 Environnements dédiés

- 🧩 Intégration : interactions composants, difficile à tester, erreurs nombreuses
  - à anticiper
- 🛠️ Utiliser des environnements dédiés avant la mise en production : staging, pré-production, …
  - au moins 1 environnement d'intégration technique
  - parfois 1 environnement de recette (test du métier)

---

