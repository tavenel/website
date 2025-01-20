---
title: Projet Selenium
author: Tom Avenel
date: 2023 / 2024
---

# Projet Automatisation de tests fonctionnels et de validation des interfaces utilisateur avec Selenium

Le but de ce projet est de coder des tests automatisés d'interface utilisateur pour un site web existant.

## Objectifs du projet

- Automatiser des scénarios de test pour un site Web de votre choix parmi ceux listés sur les sites suivants :
  - [Techlistic](https://www.techlistic.com/2020/07/automation-testing-demo-websites.html)
  - [TechBeamers](https://techbeamers.com/websites-to-practice-selenium-webdriver-online/)
- Développer une suite de tests en Selenium couvrant les principales fonctionnalités et interactions utilisateur (formulaires, boutons, navigation, etc.).
- Exécuter les tests de manière autonome et générer des rapports automatiques détaillés sur les résultats.

## Détails du projet

1. Sélectionnez un site parmi les options proposées et effectuez une analyse initiale pour identifier les fonctionnalités principales. Dressez une liste des scénarios utilisateur pertinents à tester (connexion, recherche, ajout au panier, etc.).
2. Rédigez des cas de test détaillés couvrant les principales interactions utilisateur. Chaque cas doit inclure :
  - Une description claire.
  - Les étapes pour reproduire le scénario.
  - Les données d’entrée requises.
  - Le résultat attendu.
3. En utilisant le framework d'automatisation de navigateurs `Selenium`, ajouter des tests de fonctionnalité depuis l'interface Web :
  - Créez des scripts Selenium pour automatiser chaque cas de test.
  - Utilisez des bonnes pratiques comme la séparation des éléments de l’interface utilisateur et l’implémentation de fonctions réutilisables.
  - On utilisera un design pattern de `PageObject`, c'est-à-dire que les pages et les éléments de l'interface graphique seront décrits dans des classes de tests dédiées (voir cours).
  - Organisez vos tests dans une suite structurée et assurez-vous qu'ils peuvent être exécutés indépendamment.
4. Exécution: l'application sera testée fonctionnellement dans plusieurs environnements, par exemple : `Firefox` et `Google Chrome`.
5. Rapports et journalisation des résultats :
  - Utilisez un outil de génération de rapports (comme Allure ou HTML reports) pour créer des rapports automatiques après l’exécution des tests.
  - Assurez-vous que chaque échec est accompagné d'une capture d'écran et d'un message d’erreur détaillé pour faciliter le débogage.

## Livrables attendus

- Un document décrivant les fonctionnalités choisies, les cas de test, et les résultats attendus.
- Les scripts pour chaque scénario de test, avec des commentaires clairs et une structure bien organisée.
- Un rapport final contenant les résultats des tests, les captures d’écran des erreurs, et une analyse des échecs.
- (Bonus) Configurer un pipeline CI/CD pour exécuter les tests automatiquement à chaque mise à jour du code (utilisez Jenkins, GitHub Actions, ou GitLab CI).

## Notation

Le barème est le suivant :

- 5 points pour le document décrivant les cas de tests
- 3 points pour le rapport d'exécution des tests
- 6 points pour la couverture de tests (nombre de tests, choix des scénarios, ...)
  - attention à prioriser les tests
  - il est attendu au moins 5 tests `Selenium`.
- 6 points pour la qualité des tests (design patterns utilisés, lisibilité du code de test, ...)

\newpage{}

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- SELENIUM is a trademark of Software Freedom Conservancy, Inc.
- Firefox® is a registered trademark of the Mozilla Foundation.
- Chrome™ is a trademark of Google LLC.

