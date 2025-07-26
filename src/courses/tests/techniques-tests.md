---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Techniques de tests
tags:
- tests
---

## 🧩 Techniques de test boîte-noire

---

### 📊 Partitions d'équivalence

- 📂 Données **divisées en partitions** supposées être traitées de la même manière (_Kaner 2013_ et _Jorgensen 2014_) ;
- 📌 1 donnée ne peut être dans 2 partitions ;
- 📌 Partition valide vs invalide ;
- 📌 **Partitions invalides à tester séparément** (sinon mélange des erreurs).

---

### 📈 Analyse des valeurs limites

- 📊 Partitions d'équivalence avec **données numériques ou ordonnées**
- 📌 On teste seulement les **valeurs limites des partitions** (_Beizer 1990_) ou (variante) les 3 valeurs juste en dessous, sur et au-dessus (_Jorgensen 2014_)
- 🎯 Idée : plus de risque d'erreur aux limites (normalement, même algorithme dans la classe).

---

#### 📌 Exemple

Soit `1<=n<=5` avec `n` un entier positif :
- 3 partitions _invalide A={6..9} (trop grand), valide B={1..5}, invalide C={0} (trop petit)_
- Beizer : `{5,6}` et `{0,1}`
- Jorgensen : `{4,5,6}` et `{0,1,2}`

---

### 📋 Test de tables de décision

- 📌 Chaque ligne identifie des **conditions** (entrées) (en haut dans le tableau) ou des **sorties** (en bas dans le tableau) du système ;
- 📌 Chaque colonne : **combinaison de conditions** ;
- 🎯 Permet d'identifier les **combinaisons importantes**.
- 📌 _Couverture minimale courante : couvrir toutes les combinaisons_

---

### 🔄 Test des transitions d'état

- 📌 Basés sur les événements (ou séquences d'événements) créant un **changement d'état** dans le système ;
- 🌐 Voir [un exemple de la taverne du testeur](https://latavernedutesteur.fr/2018/10/02/techniques-basees-sur-les-specifications-4-7-les-tests-de-transition-detat/)

---

- 📌 Si **tableau** : montre toutes les **transitions valides** et les **transitions potentiellement invalides** entre les états d'un système (et les événements, les conditions de garde et les actions résultantes pour les transitions valides).
- 📌 Si **diagramme** de transition d'états : montre **uniquement les transitions valides**.

---

- 📌 Usage :
  - 📌 _Applications basées sur des menus_ ;
  - 📌 _Logiciel embarqué_ ;
  - 📌 _Métier modélisable par états (aviation, ...)_.

---

### 👥 Test des cas d'utilisation

- 📌 Tests utilisant des _cas d'utilisation_ : spécifient un **comportement** qu'un système peut accomplir **en collaboration** avec un ou plusieurs acteurs (humains, dépendance externe, autres composants, ...) (_UML 2.5.1 2017_)
- 📌 _Les interactions peuvent être représentées graphiquement par des flux de travail, des diagrammes d'activités ou des modèles de processus métier._

---

## 🛠️ Techniques de test boîte-blanche

---

### 📋 Test et couverture des instructions

- 📌 Exerce les **instructions exécutables** dans le code (lignes de code).
- 📌 _Couverture de test : lignes de code exécutées par le test / lignes de code total_.
- 🎯 Aide à **détecter des zones non testées** par d'autres types de tests.

---

### 📋 Test et couverture des décisions

- 📌 Exerce les **décisions possibles** dans le code.
  - 📌 Ex : `if` et `else`
- 📌 _Couverture de test : décisions testées / décisions totales_.
- 🎯 Aide à trouver des **conditions pas totalement testées**.

---

## 🧪 Techniques de test basées sur l'expérience

---

### 📌 Estimation d'erreur

- 📌 _Comment l'application a-t-elle fonctionné avant ?_
- 📌 _Quels types d'erreurs les développeurs ont-ils tendance à faire ?_
- 📌 _Quelles défaillances se sont produites dans d'autres applications ?_

---

- 📌 Tests écrits depuis une **liste estimant les erreurs** ;
- 📌 Utilise l'**expérience** et les **données recueillies**.

---

### 🧪 Tests exploratoires

- 📌 Tests **informels** réalisés "**en live**" ;
- 🎯 Utiles si spécifications peu adaptées au test ;
- 🏃 Rapides à mettre en œuvre.
  - 📌 Ex : _test de session (temps fixe, objectifs définis, réalisation libre)_.
- 🔄 Souvent **combinés à d'autres types** de tests.

---

### 📋 Tests basés sur des checklists

- 📌 Liste d'**éléments à vérifier** ou ensemble de critères pour valider le produit ;
- 📌 Souvent **modifiée pendant l'analyse** mais parfois checklist _classique_ réutilisable ;
- 📌 _Utile si base de test existante peu formelle_.

---

## 🎯 Choix des techniques de test

---

### 📌 Exemples de facteurs

- 📌 Type de composant ou de système ;
- 📌 Complexité du composant ou des systèmes ;
- 📜 Normes réglementaires ;
- 📌 Exigences client ou contractuelles ;
- 📌 Niveaux de risque ;
- 📌 Types de risques ;
- 🎯 Objectifs du test ;
- 📜 Documentation disponible ;
- 📚 Connaissances et compétences des testeurs ;
- 🛠️ Outils disponibles ;
- ⏳ Temps et budget ;
- 🔄 Modèle de cycle de vie du développement logiciel ;
- 📌 Utilisation prévue du logiciel ;
- 📌 Expérience des techniques sur le composant ou le système à tester ;
- 🐛 Types de défauts attendus dans le composant ou le système.

---

