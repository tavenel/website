---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: 📋 Stratégies de tests
tags:
- tests
---

## Stratégie de test

- 📄 Description **générale** du processus de test :
  - 📦 Au niveau produit ;
  - 🏢 Au niveau de l'organisation.

---

## 🔍 Stratégie Analytique

- 📈 Basée sur l'analyse d'**un facteur** : _exigences, risques, ..._
  - 📌 Ex : _risques_ => tests conçus et priorisés en fonction du niveau de risque.

---

## 📊 Stratégie Basée sur des modèles (MBT)

Tests conçus (manuellement ou automatiquement) à partir d'un **modèle abstrait et haut niveau du SUT** :
- 📌 Ex : fonction, processus métier, structure interne, caractéristique non-fonctionnelle : fiabilité, ...
- 🤖 Les outils MBT peuvent automatiser le design des tests fonctionnels (boîte noire) : _MaTeLo, PragmaDev Studio, Time Partition Testing_.

---

⚠️ **Attention** : **MBT == modélisation du SUT** (et non modélisation des tests)

---

### 👍 Avantages

- 📊 Tests proches du SUT grâce au modèle :
  - ✅ Tests **robustes et bien conçus** ;
  - 🎯 Bonne couverture ;
  - 💰 Réduit le coût des tests (modélisation, maintenance).
- 📄 Améliore la **qualité de la documentation** des exigences
  - 🤝 Plateforme commune designers / testeurs
- 📈 Améliore la **qualité du processus** de test.

---

### 👎 Inconvénients

- 🔗 Adhérence forte au modèle :
  - ✅ Nécessite un modèle bien fait
- 🔄 Nécessite une adaptation modèle <-> implémentation par le testeur (_concrétisation_) :
  - ⏳ Prend du temps ;
  - 📚 Nécessite compétences : connaissance métier, _UML_

---

## 📝 Stratégie Méthodique

Utilisation systématique d'un **ensemble prédéfini** de tests ou conditions de test :
- 🔧 Défaillances les plus probables ;
- 🏆 Caractéristiques de qualité importantes ;
- 📜 Normes internes à l'entreprise.

---

## 📏 Stratégie Conforme à une norme (ou processus)

Analyse, conception et implémentation de tests basés sur des **règles et normes externes** :
- 📜 Normes spécifiques à l'industrie ;
- 📜 Normes imposées par ou à l'entreprise.

---

## 👥 Stratégie Dirigée (ou consultative)

- Test dicté par les **recommandations** des parties prenantes, des **experts** techniques ou du domaine métier.

:::tip
👨‍💼 Les experts peuvent être extérieurs
:::

---

## 🔄 Stratégie Anti-régressions

Objectif : **éviter les régressions** :
- 🔄 Réutilisation des tests existants ;
- 🤖 Automatisation des tests de régression ;
- 🤖 Automatisation des cas nominaux.

---

### 👍 Avantages

- ✅ Si produit en production mais aucune stratégie existante ;
- 💰 Effort limité ;
- 📈 Pas de détérioration de la qualité.

---

### 👎 Inconvénients

- ❓ Qualité des intégrations ?
- 🚫 Pas d'amélioration de la qualité.

---

## 🔄 Stratégie Réactive

Tests conçus, implémentés et exécutés immédiatement **à partir des résultats de tests antérieurs** :
- 🚫 Pas de pré-planification ;
- 📌 Ex : tests exploratoires.

---

### 👍 Avantages

- 🔄 Tests adaptables si spécifications floues ou changeantes ;
- 💰 Coût de spécification de test faible.

---

### 👎 Inconvénients

- 📜 Peu de processus :
  - ⚠️ Fort risque d'oublier des tests ;
  - 🎯 Tests adaptés uniquement au SUT (pas au besoin)
- 🚫 Non automatisable.

---

# 📊 Métriques de tests

À recueillir pendant et après les activités de test :
- 📅 Avancement par rapport au **calendrier** et au **budget** prévus ;
- 🏆 **Qualité actuelle** de l'objet de test ;
- 🎯 **Pertinence** de l'approche de test ;
- 📈 **Efficacité** des activités de test par rapport aux objectifs.

---

## 📊 Métriques courantes

- 📊 _% temps de travail_ ou _% nombre_ de cas de tests implémentés.
- 🛠️ _% préparation de l'environnement_ de test.
- 🏃 _Exécution des cas de test_ : exécutés/non exécutés, réussis/échoués, conditions réussies/échouées.
- 🐛 _Informations sur les défauts_ : densité, corrigés, taux de défaillance, tests de confirmation.
- 🎯 _Couverture_ : exigences, User Stories, critères d'acceptation, risques, lignes de code.
- 📅 _Degré d'achèvement des tâches_, affectation et utilisation des ressources, et temps passé.
- 💰 _Rapport Bénéfice / Coût_ de la découverte d'autres défauts ou de l'exécution de tests supplémentaires.

---

## 👥 Indépendance des testeurs

Principe : avoir une équipe **dédiée** au test **indépendante** des autres équipes (notamment des développeurs).

---

### 👍 Avantages

- 🐛 Détecter des erreurs différentes par rapport aux développeurs ;
- ✅ Vérifier et contester les spécifications et l'implémentation du système.

---

### 👎 Inconvénients

- 🚫 Manque de collaboration :
  - 📜 Manque d'information pour le testeur ;
  - ⏳ Retards dans les retours d'information et relation conflictuelle avec l'équipe de développement ;
- ⚠️ Problème de gouvernance : _la qualité ne regarde que les testeurs_ ;
- ⏳ Testeurs vus comme un goulot d'étranglement responsable des retards ;

---

### 🛠️ En pratique

- 🏢 Petites structures (startups) et/ou projet peu critiques : cercles de travail pluridisciplinaires ;
- 🏭 Projet critique et/ou organisation très formelle et/ou beaucoup de ressources : équipe(s) dédiée(s) au test.

---

# 📚 Liens

- 📖 Model-based testing : _Kramer, A., Legeard, B. (2016): "Model-Based Testing Essentials - Guide to the ISTQB(R) Certified Model-Based Tester - Foundation Level". John Wiley & Sons, 2016, (ISBN 978-1119130017)_
- 🌐 [Lien vers le blog Octo](https://blog.octo.com/la-pyramide-des-tests-par-la-pratique-1-5)

