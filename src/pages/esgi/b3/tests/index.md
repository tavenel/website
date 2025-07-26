---
title: 🧪 Tom Avenel - B3 Tests unitaires et logiciels
layout: '@layouts/BaseLayout.astro'
---

# 🧪 Tests unitaires et logiciels

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

## 📑 Documents

### Méthodologie

- [🤓 Cours : méthodologie des tests](/tests/cours-methodo)
- [📖 Exemple de rapport de bug](/tests/methodo/exemple-rapport-bug)
- [📖 Exemple de template de plan de tests](/tests/methodo/exemple-template-plan-tests)
- [📝 Exercices sur la méthodologie de test](/tests/methodo/exercices_methodo_tests)
- [📝 Exercices sur les techniques de tests](/tests/methodo/techniques-tests-exercices)

### Industrialisation des tests

- [🤓 Cours sur l'industrialisation des tests](/tests/cours-indus)

### Tests unitaires

- [🤓 Cours : le framework Unittest en Python](/tests/unit/python/cours-python-unittest)
-  Dépôts d'exemples de tests unitaires :
  - 󰌠 Python : <https://git.sr.ht/~toma/python-unit>
  - ☕ Java : <https://git.sr.ht/~toma/java-unit>
  - 🇰 Kotlin : <https://git.sr.ht/~toma/kotlin-unit>
  - Jest : <https://git.sr.ht/~toma/unit-jest>
- [💻 TP : Analyses de code en Python et utilisation du debugger](/tests/unit/python/tp-python-lint-debug)
- [💻 TP : Tests automatisés en Python](/tests/unit/python/tp-python-tests)
- [💻 TP : Tests unitaires Frontend en Jest](/tests/unit/jest/tp-jest)

### ⚛️ Selenium - Automatisation de tests fonctionnels d'interface Web

- [🤓 Cours Selenium](/tests/selenium-cours)
- [💻 TP Selenium - industrialiser le test d’interface utilisateur](/tests/selenium-tp)
  -   Sources pour le TP : `git clone https://git.sr.ht/~toma/selenium`

### Projet noté

- [🏆 Projet jeu de rôle](/tests/projet_jeu_roles) : développer un jeu de rôle avec un focus important sur les tests unitaires et les tests d'interface utilisateur.

## 🚀 Pour aller plus loin

- Voir les autres ressources du [🧪 cours sur les tests](/tests) et du [cours sur l'intégration continue](/ci).
