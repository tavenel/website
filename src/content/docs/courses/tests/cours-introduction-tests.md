---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Introduction aux tests logiciels
tags:
- tests
type: cours
sidebar:
  order: 4
description: Introduction aux tests logiciels
---
## 🤔 Pourquoi tester le logiciel ?

- 🚀 Les sondes perdues (Mars Climate Orbiter, Mars Pathfinder)
- 🛡️ Les missiles Patriotes
- 🌌 1er vol d'Ariane 5
- ⚕️ Therac-25
- 🎮 Steam sur Linux
- 🔒 OpenSSL sur Debian (génération aléatoire suite warning Valgrind)
- 💸 Pensions alimentaires britanniques : 1 milliard dollars

:::note
Pour plus d'information : <https://read.thecoder.cafe/p/therac-25>
:::

---

> 💡 En essayant continuellement on finit par réussir. Donc : plus ça rate, plus on a de chance que ça marche. (Devise Shadok)

Voir aussi : [Fireship - The horrors of software bugs](https://www.youtube.com/watch?v=Iq_r7IcNmUk)

---

### 📦 Les projets logiciels :

- ⏳ Ne livrent pas le produit dans les temps ;
- 💰 Coûtent beaucoup plus chers que prévu ;
- 📉 Délivrent un produit de qualité très faible ;
- ❌ Échouent dans la majorité des cas !!!

---

> 💡 En Europe, grâce aux logiciels de tests nous pourrions économiser plus de 100 milliards d'euros par an. _Klaus Lambertz, Verifysoft Technology GmbH_

---

## 💻 Spécificités du logiciel

- ❌ Échecs très nombreux ;
- 💥 Crash système considéré comme habituel ;
- 🐛 Cause du bug pas directement identifiable ;
- 🔧 Dommages (souvent) mineurs ;

---

- 🔮 À part dans les systèmes critiques, on considère que le logiciel ne peut anticiper toutes les situations ;
- 🌐 Les systèmes informatiques se complexifient trop vite ;
- 🔄 Les logiciels passent par des états discrets, dont certains ne sont pas prévus ;
- 🔄 Ajouts, changements de fonctionnalités, de plateformes...

---

![Ce que voulait le client](@assets/projet/balancoire.jpg)

<div class="caption">Ce que voulait le client.</div>

---

## 📊 Software Testing Trends (2025-2026)

### Main improvement areas in software testing

- 🤖 AI-assisted testing and test automation
- 🔄 Continuous testing and CI/CD integration
- 📚 Quality Engineering practices and test processes
- 🗣️ Cross-functional collaboration between development, testing and business teams
- 🔐 Security, performance and reliability testing

### Key test design techniques

- 📝 Use case and scenario-based testing
- 🔍 Exploratory testing
- 📏 Boundary value analysis
- 📊 Equivalence partitioning
- 🔀 Decision table and state transition testing
- ✅ Checklist-based testing
- 🤔 Error guessing

### New technologies and subjects affecting software testing

- 🤖 Generative AI and AI-assisted testing
- 🧠 Autonomous and agentic AI
- 🔐 Cybersecurity and privacy
- 📊 Big data and data quality
- ☁️ Cloud-native architectures and microservices
- 🌐 IoT and connected systems

### Trending topics in software testing

- 🤖 AI-driven test automation
- 🏃 Agile and continuous testing
- 🔄 Shift-left and shift-right testing
- 🏗️ Quality Engineering
- 🔐 Security and performance testing
- 🧪 Testing AI-based systems

### Non-testing skills expected from a modern software tester

- 🗣️ Communication and collaboration skills
- 🧠 Critical thinking and analytical skills
- 📚 Business and domain knowledge
- 💻 Programming and scripting skills
- 🤖 AI literacy and prompt engineering
- 📊 Data literacy
- 📈 Adaptability and continuous learning

---

Le rapport [World Quality Report 2025-26 - Capgemini / Sogeti / OpenText](https://www.opentext.com/en/media/report/world-quality-report-17th-edition-2025-26-en.pdf) donne des indications chiffrées intéressantes sur les compétences attendues des Quality Engineers :

- Generative AI	63 %
- Core Quality Engineering skills	60 %
- Development / coding skills	58 %
- Domain knowledge	56 %
- Soft skills	51 %
- CI/CD orchestration	44 %
- Cloud	41 %

Voir aussi ces autres enquêtes :

- [Software Testing in Practice and Research 2024 – German Testing Board](https://www.asqf.de/en/a-look-back-and-then-forward-results-of-the-2011-2024-surveys-software-testing-in-practice-and-research/)
- [State of Software Quality 2024 – Katalon](https://www.katalon.com/reports/state-quality-2024)
- [State of Developer Ecosystem 2025 – JetBrains](https://www.jetbrains.com/fr-fr/developer-research/)

---

## 👥 Les métiers du test logiciel

---

### 👨‍💼 Test Manager

_Responsable du processus et de la bonne conduite des tests._

Des activités techniques de test :
- 📅 Planifier les activités de test : objectifs, risques, estimation temps/effort/coût, types et niveaux de tests, gestion des défauts, ...
- 📄 Rédiger les plans de test ;
- 🛠️ Concevoir, implémenter, exécuter les tests ;
- 📊 Suivre et publier les résultats des tests ;
- 📏 Contrôler le niveau de qualité du produit (+métriques) ;

Des activités opérationnelles et de gestion :
- 📜 Développer une politique et une stratégie de test, gérer les testeurs ;
- 🤝 Coordonner avec les parties prenantes (chef de projet, PO, ...) ;
- 🔄 Coordonner avec l'intégration ;
- 🛠️ Gérer les environnements de test et de gestion des défauts (+outils).

---

### 👨‍💻 Testeur logiciel

Exemples d'activités :
- 🔍 Analyser et challenger les User Stories, les spécifications, les modèles pour les rendre testables ;
- 📝 Documenter les conditions de test ;
- 🛠️ Concevoir les environnements de test ;

- 📄 Contribuer aux plans de test ;
- ✅ Implémenter les cas de test ;
- 📂 Préparer les données de test ;
- 📅 Créer le planning détaillé d'exécution des tests ;
- 🏃 Exécuter les tests et documenter les résultats ;
- 🤖 Automatiser des tests si nécessaire ;
- 📊 Évaluer les caractéristiques non-fonctionnelles : performance, sécurité, ...

---

## 📖 Un vocabulaire précis et spécifique

_Voir le glossaire en annexe_

---

