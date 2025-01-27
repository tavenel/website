---
title: 🧪 Tom Avenel - B3 Tests unitaires et logiciels
---

# 🧪 Tests unitaires et logiciels

![](/resources/images/cover/tests.jpg)

## Présentation du module

### 🎯 Objectif
 
- Se familiariser avec le jargon des tests. 
- Comprendre les différents types de tests logiciels.
- Introduction à la validation par la recette fonctionnelle 
- Utiliser la méthode et les outils de test adaptés au contexte et à la situation 
- Définir un plan de test tout au long du développement de l’application 
- Concevoir et automatiser un processus de test dans le cadre du développement d’une application informatique. 
- Comprendre les enjeux des tests unitaires et développer des tests efficacement
- Tester une interface utilisateur automatiquement

### 📅 Déroulé des séances

Module de 24H

Évaluation : 2 CC + Projet

### Plan de cours

#### MÉTHODOLOGIE DES TESTS

##### INTRODUCTION AUX TESTS LOGICIELS 

- Qu'est-ce que le test ? Le bug et son coût. La testabilité. Les tests et le cycle de vie. Le concept de Vérification et Validation.
- Le métier de testeur logiciel.

##### LA DÉMARCHE DE TEST 

- Les cinq fondements. 
- Les processus projet et les tests. L'approche globale. 
- Le plan de test et ses déclinaisons. La stratégie de test. 
- L'approche par les risques. L'estimation. 
- Les plateformes. Tests et bases de données. 
- Préparer, exécuter et évaluer des tests. 
- La documentation de livraison. Le suivi. 

##### RAPPELS SUR LE PROCESSUS DE DÉVELOPPEMENT 

- Rôle du test dans le processus de développement. 
- Les tests : unitaires, fonctionnels, etc. 
- Les différentes méthodes de test. 
- Processus de test et stratégie de test. 
- Outils et méthodes intervenant à différentes étapes. 

##### LE PLAN DE TEST : ACQUERIR UNE METHODE D ELABORATION   

- Evaluer les risques  
- Définir le niveau de qualité requis selon le projet 
- Définir les objectifs, les thèmes, les scénarios et les cas de tests 
- Construire le plan de test 
- Bonnes pratiques : du cahier des charges à la recette 
 
##### LES MÉTHODES DE CONCEPTION DES SYSTÈMES INFORMATIQUE : 
- BDD : Behavior Driven Development 
- TDD : Tests Driven Design

##### TESTS DE VALIDATION : LA RECETTE FONCTIONNELLE  

- Introduction : 
- Finalité d’une recette 
- Place de la recette dans le cycle de vie 
- Périmètre d’une recette fonctionnelle : 
- Lien Qualité et test 
- Couverture des tests 
- Processus métier : scénario de tests  
- Bonnes Pratiques de la recette fonctionnelle
- Le cas de test : entrée, comportement, résultat attendu, résultat effectif 
- Le traitement des anomalies : classification, workflow 
- Plan d’une recette
- Démarche et acteurs 
- Coûts prévus 
- Risques 
- Organisation, cadrage, périmètres 
- Outils 
- Priorités 
- Environnement requis

#### AUTOMATISATION DES TESTS

##### INTRODUCTION À L’AUTOMATISATION DES TESTS 

- Quels tests et pour faire quoi ? 
- Les environnements de tests. 
- Gestion de la couverture des exigences par les tests. Notion de couverture et de granularité. 
- Démarche de mise au point : organisation des suites de tests et création des cas. 
- Faut-il automatiser un test ? Critères à prendre en compte ? 
- Préparation à l'automatisation. 
- Construction de la population de test. 
- Mise au point et vérification des tests (Revue) 
- Exécution, enregistrement des anomalies. Notion de rapport d'incident d'après l'IEEE. 
- Gestionnaires d'anomalies. Automatisation de la création des anomalies. 
- Analyse de résultats d'exécution de tests. Consolidation des tests. 

##### LES TESTS UNITAIRES

- Organisation et bonnes pratiques pour les tests unitaires. 
- Critères d'automatisation. 
- Les tests aux limites, de robustesse, aléatoires. Analyse dynamique. 
- Mesure de la couverture de code : couverture des tests structurels, couverture d'instructions et 
branches. 
- Analyse statique de code : analyse outillée du code source hors exécution (règles de codage) : 
Checkstyle, Cobertura. 
- Automatisation avec un fichier de configuration. 
- Analyse dynamique de code : couverture des instructions, des branches, des prédicats… 
- Automatisation avec un outil d'analyse de couverture. 
- Organisation des tests unitaires, pair programming, pair testing. 
- Utilisation des frameworks : gestion des scripts de tests, gestion des données de tests, récupération

##### LES TESTS UNITAIRES AVEC LE LANGAGE PYTHON ET LES OUTILS QA  

- Mise en oeuvre des outils de test et d’évaluation de la qualité d’un programme Python 
- Les outils d’analyse statique de code (Pylint, Pychecker) 
- Analyse des comptes rendus d’analyse (types de message, avertissements, erreurs) 
- Le débogueur de Python (exécution pas à pas et analyse post-mortem) 
- Les modules de tests unitaires Python (Unittest…) 
- Les tests de couverture de code – profiling

##### AUTOMATISATION DE TESTS D'INTERFACE UTILISATEUR (SELENIUM)

- Automatisation des tests à l’aide de robot de tests : Utilisation de Selenium 
- Présentation des composants de Selenium 
- Sélénium IDE : Enregistrer, éditer et déboguer les tests 
- Sélénium Remote Control : écriture des tests d’automatisation – Framework de tests fonctionnels 
- Sélénium Grid : accélération des tests fonctionnels

##### AUTOMATISATION DES TESTS D’INTÉGRATION 

- Intégration ascendante versus descendante. Intégrations mixtes. 
- Objets simulacres : bouchons pour simuler les fonctions appelées, mocking pour remplacer un objet. 
Les frameworks. 

## Documents

### 🤓 Rappels de cours : Le langage Python

Voir la [page du cours Python](/cours/python/index.html)

### Introduction aux tests logiciels

#### 🤓 Cours d'introduction

- _Pourquoi le test logiciel ?_
- _Qu'est-ce qu'un testeur ?_

- [html](/cours/tests/methodo/cours-introduction-tests.html)
- [pdf](/cours/tests/methodo/cours-introduction-tests.pdf)
- [markdown](/cours/tests/methodo/cours-introduction-tests.md)

#### 🤓 Cours : les types de tests

- [pdf (2M)](/cours/tests/methodo/cours-tests.pdf)

#### 📝 Exercices sur la méthodologie des tests

- [html](/cours/tests/methodo/exercices_methodo_tests.html)
- [pdf](/cours/tests/methodo/exercices_methodo_tests.pdf)
- [markdown](/cours/tests/methodo/exercices_methodo_tests.md)

#### 🤓 Exemple de rapport de bug

- [html](/cours/tests/methodo/exemple-rapport-bug.html)
- [pdf](/cours/tests/methodo/exemple-rapport-bug.pdf)
- [markdown](/cours/tests/methodo/exemple-rapport-bug.md)

#### 🧪 Exemple de template de plan de tests

- [html](/cours/tests/methodo/exemple-template-plan-tests.html)
- [pdf](/cours/tests/methodo/exemple-template-plan-tests.pdf)
- [markdown](/cours/tests/methodo/exemple-template-plan-tests.md)

### Stratégies et techniques de tests

#### 🤓 Cours sur les tests statiques

- [html](/cours/tests/methodo/test-statique.html)
- [pdf](/cours/tests/methodo/test-statique.pdf)
- [markdown](/cours/tests/methodo/test-statique.md)

#### 🤓 Cours sur les techniques de tests

- [html](/cours/tests/methodo/techniques-tests.html)
- [pdf](/cours/tests/methodo/techniques-tests.pdf)
- [markdown](/cours/tests/methodo/techniques-tests.md)

#### 🤓 Cours sur les stratégies de tests

- [html](/cours/tests/methodo/cours-strategies-tests.html)
- [pdf](/cours/tests/methodo/cours-strategies-tests.pdf)
- [markdown](/cours/tests/methodo/cours-strategies-tests.md)

#### 📝 Exercices sur les techniques de tests

- [html](/cours/tests/methodo/techniques-tests-exercices.html)
- [pdf](/cours/tests/methodo/techniques-tests-exercices.pdf)
- [markdown](/cours/tests/methodo/techniques-tests-exercices.md)

#### 🤓 Cours : écrire du code testable

- [html](/cours/tests/methodo/ecrire-code-testable-cours.html)
- [pdf](/cours/tests/methodo/ecrire-code-testable-cours.pdf)
- [markdown](/cours/tests/methodo/ecrire-code-testable-cours.md)

#### 🤓 Cours sur les design patterns de test

- [html](/cours/tests/methodo/patterns-cours.html)
- [pdf](/cours/tests/methodo/patterns-cours.pdf)
- [markdown](/cours/tests/methodo/patterns-cours.md)

#### 🤓 Cours sur l'industrialisation des tests

_Pourquoi et comment automatiser les tests ?_

- [html](/cours/tests/methodo/indus-tests-cours.html)
- [pdf](/cours/tests/methodo/indus-tests-cours.pdf)
- [markdown](/cours/tests/methodo/indus-tests-cours.md)

### Les tests unitaires

#### 🤓 Cours : le framework Unittest en Python

- [TP html](/cours/tests/unit/python/cours-python-unittest.html)
- [TP pdf](/cours/tests/unit/python/cours-python-unittest.pdf)
- [TP markdown](/cours/tests/unit/python/cours-python-unittest.md)

#### 💻 TP : Tests automatisés et analyses de code en Python

Dans ce TP, nous allons voir comment automatiser des tests dans le langage Python.

- [TP html](/cours/tests/unit/python/tp-python-tests.html)
- [TP pdf](/cours/tests/unit/python/tp-python-tests.pdf)
- [TP markdown](/cours/tests/unit/python/tp-python-tests.md)
- Sources pour le TP : `git clone https://git.sr.ht/~toma/python-unit`

#### 💻 Tests unitaires Java - exemples de cours

- Sources pour le TP : `git clone https://git.sr.ht/~toma/java-unit`

#### 💻 Tests unitaires frontend Jest

- [TP html](/cours/tests/unit/jest/tp-jest.html)
- [TP pdf](/cours/tests/unit/jest/tp-jest.pdf)
- [TP markdown](/cours/tests/unit/jest/tp-jest.md)

### Selenium - Automatisation de tests fonctionnels d'interface Web

#### 🤓 Cours Sélénium - tests end to end

- [Cours html](/cours/tests/selenium/selenium-cours.html)
- [Cours pdf](/cours/tests/selenium/selenium-cours.pdf)
- [Cours markdown](/cours/tests/selenium/selenium-cours.md)

#### 💻 TP Sélénium

Dans ce cas pratique, nous allons automatiser et industrialiser le processus de test d’interface utilisateur d'un projet existant.

- [TP html](/cours/tests/selenium/tp-selenium.html)
- [TP pdf](/cours/tests/selenium/tp-selenium.pdf)
- [TP markdown](/cours/tests/selenium/tp-selenium.md)
- Sources pour le TP : `git clone https://git.sr.ht/~toma/selenium`

### 💻 TP d'entraînement : Facadia

Le but de ce projet est de récupérer un projet JS déjà développé (Facadia) pour écrire des tests unitaires, des tests d'intégration et des tests end-to-end.
- [html](/cours/tests/projet_facadia.html)
- [pdf](/cours/tests/projet_facadia.pdf)
- [markdown](/cours/tests/projet_facadia.md)

### 📌 Projet noté : jeu de rôle

Le but de ce projet est de développer un jeu de rôle avec un focus important sur les tests unitaires et les tests d'interface utilisateur.

- [html](/cours/tests/projet_jeu_roles.html)
- [pdf](/cours/tests/projet_jeu_roles.pdf)
- [markdown](/cours/tests/projet_jeu_roles.md)

### Pour aller plus loin

#### 🤓 Introduction à l'intégration continue 

- [html](/cours/ci/cours-intro-ci.html)
- [pdf](/cours/ci/cours-intro-ci.pdf)
- [markdown](/cours/ci/cours-intro-ci.md)

#### 📝 Travaux dirigés : écrire un plan de tests

Dans ce cas pratique, vous allez décrire un plan de test pour un projet existant.

- [html](/cours/tests/methodo/td_plan_tests.html)
- [pdf](/cours/tests/methodo/td_plan_tests.pdf)
- [markdown](/cours/tests/methodo/td_plan_tests.md)

