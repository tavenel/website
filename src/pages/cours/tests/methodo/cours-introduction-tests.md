---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Introduction aux tests logiciels
tags:
- tests
---

# Introduction aux tests logiciels

_Tom Avenel_

<https://avenel.pro>

---

# Pourquoi tester le logiciel ?

- Les sondes perdues (Mars Climate Orbiter, Mars Pathfinder)
- Les missiles Patriotes
- 1er vol d’Ariane 5
- Therac-25
- Steam sur Linux
- OpenSSL sur Debian (génération aléatoire suite warning Valgrind)
- Pensions alimentaires britanniques : 1 milliard dollars

---

> En essayant continuellement on finit par réussir. Donc : plus ça rate, plus on a de chance que ça marche. (Devise Shadok)

Voir aussi : [Fireship - The horrors of software bugs](https://www.youtube.com/watch?v=Iq_r7IcNmUk)

---

# Pourquoi tester le logiciel ?

## Les projets logiciels :

- Ne livrent pas le produit dans les temps ;
- Coûtent beaucoup plus chers que prévu ;
- Délivrent un produit de qualité très faible ;
- Échouent dans la majorité des cas !!!

---

> En Europe, grâce aux logiciels de tests nous pourrions économiser plus de 100 milliards d'euros par an. _Klaus Lambertz, Verifysoft Technology GmbH_

---

# Spécificités du logiciel

- Échecs très nombreux ;
- Crash système considéré comme habituel ;
- Cause du bug pas directement identifiable ;
- Dommages (souvent) mineurs ;

---

- A part dans les systèmes critiques, on considère que le logiciel ne peut anticiper toutes les situations ;
- Les systèmes informatiques se complexifient trop vite ;
- Les logiciels passent par des états discrets, dont certains ne sont pas prévus ;
- Ajouts, changements de fonctionnalités, de plate- formes...

---

![](/cours/gestion-projet/gestion_projet_balancoire.jpg)

---

<!-- _class: titre -->
# Enquête 2017-2018 ISTQB (International Software Testing Qualifications Board)

---

Main improvement areas in software testing are :

- Test automation
- Knowledge about test processes
- Communication between development and testing

---

Top five test design techniques utilized by software testing teams are :

- Use case testing
- Exploratory testing
- Boundary value analysis
- Checklist based
- Error guessing

---

New technologies or subjects that are expected to affect software testing in near future are :

- Security
- Artificial intelligence
- Big data

---

Trending topics for software testing profession in near future will be :

- Test automation
- Agile testing
- Security testing

---

Non-testing skills expected from a typical tester are :

- Soft skills
- Business/domain knowledge
- Business analysis skills

---

<!-- _class: titre lead -->
# Les métiers du test logiciel

---

# Test Manager

_Responsable du processus et de la bonne conduite des tests._

---

Des activités techniques de test :

- Planifier les activités de test : objectifs, risques, estimation temps/effort/coût, types et niveaux de tests, gestion des défauts, ...
- Rédiger les plans de test ;
- Concevoir, implémenter, exécuter les tests ;
- Suivre et publier les résultats des tests ;
- Contrôler le niveau de qualité du produit (+métriques) ;

---

Des activités opérationnelles et de gestion :

- Développer une politique et une stratégie de test, gérer les testeurs ;
- Coordonner avec les parties prenantes (chef de projet, PO, ...) ;
- Coordonner avec l'intégration ;
- Gérer les environnements de test et de gestion des défauts (+outils).

---

# Testeur logiciel

Exemples d'activités :

- Analyser et challenger les User Stories ,les spécifications, les modèles pour les rendre testables ;
- Documenter les conditions de test ;
- Concevoir les environnements de test ;

---

- Contribuer aux plans de test ;
- Implémenter les cas de test ;
- Préparer les données de test ;
- Créer le planning détaillé d'exécution des tests ;
- Exécuter les tests et documenter les résultats ;
- Automatiser des tests si nécessaire ;
- Évaluer les caractéristiques non-fonctionnelles : performance, sécurité, ...

---

# Un vocabulaire précis et spécifique

_Voir le glossaire en annexe_

