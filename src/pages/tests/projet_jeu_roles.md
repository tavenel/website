---
title: Jeu de rôle
date: 2023 / 2024
---

# Présentation du projet 

Le projet consiste à développer une application Web permettant à un joueur de jouer à un jeu de rôle contre l'ordinateur.

Le détail du cahier des charges est le suivant - en cas de question sur les spécifications, le formateur jouera le rôle du client final pour préciser celles-ci.

## Fonctionnalités

- Le joueur possède un `personnage` ayant des `caractéristiques` et des `objets` 
  + les différentes caractéristiques seront à choisir par les développeurs ;
  + les valeurs des caractéristiques du personnage doivent **évoluer** en fonction des événements de jeu.
  + la liste des objets est choisie par les développeurs ;
  + le personnage doit **acquérir et perdre des objets** en fonction des événements de jeu.
- Le joueur doit pouvoir **personnaliser** son personnage au démarrage de la partie. Cette personnalisation a un impact sur les caractéristiques du personnage.
- Le jeu se déroule en une suite d'`événements`.
  + certains événements ont un impact **positif** pour le joueur, d'autres ont un impact **négatif** ;
  + le jeu doit proposer des `actions` à réaliser à chaque événement, ces actions ont un impact sur le déroulement des événements et le choix des événements suivants ;
  + certains événements font interagir d'**autres personnages non jouables** (ex : combat contre des ennemis, ...)
- Le jeu doit contenir une part d'**aléatoire** (par exemple, la valeur exacte de certaines caractéristiques des ennemis ou l'enchaînement des événements).
- Le jeu possède des conditions de **victoire** et des conditions de **défaite** (événement et/ou conditions sur les objets acquis ou les caractéristiques du personnage).

# Réalisation des tests

## Tests unitaires

Il est très compliqué de définir une couverture de test nécessaire et suffisante, car cela dépend énormément du code à tester : on privilégiera donc toujours la qualité du test sur les statistiques de sa couverture de code.

_On appelle code métier du code lié directement aux exigences fonctionnelles (et donc compréhensible par un expert du domaine - par exemple, la gestion des conditions de vol dans un programme d'aviation) et non un code ajouté simplement à cause de contraintes techniques (par exemple, comment interagir avec la base de données)._

Les parties de code _métier_ d'une application sont les plus critiques et celles à tester le plus en profondeur dans les tests unitaires. Au contraire, les classes ayant des dépendances externes sont en général difficiles à tester et sensibles aux changements d'implémentation : il est normal que leur couverture de tests unitaires soit moins importante.

- On activera la couverture de test dans l'IDE afin de vérifier que les classes sont bien testées.
- On ajoutera les tests unitaires nécessaires.
- On pensera à utiliser des substituts (`Mock`, `Stub`) lorsque c'est nécessaire pour s'abstraire des dépendances.
- On modifiera le code source de l'application pour corriger les bugs trouvés au fur et à mesure du développement (Test-Driven Development).

## Tests end-to-end

- En utilisant le framework d'automatisation de navigateurs `Selenium`, ajouter des tests de fonctionnalité depuis l'interface Web.
  + On utilisera un design pattern de `PageObject`, c'est-à-dire que les pages et les éléments de l'interface graphique seront décrits dans des classes de tests dédiées (voir cours).
- On pourra également lancer l'application et réaliser des tests de fonctionnalité à la main - ceux-ci seront à documenter dans le rapport.

# Travail demandé 

Dans le respect du cahier des charges, il est attendu :

- Le développement de l'application en suivant un processus de **test-driven development** :
  + L'application sera une **application Web** ;
  + L'application devra utiliser un système de persistance (base de données `SQL`, ...);
  + L'application devra posséder un **backend** et un **frontend** réalisés chacuns par l'équipe du projet ;
  + Le choix des technologies (frameworks backend et frontend) sont laissés libres ;
  + L'application devra posséder des tests unitaires dans le backend **et** dans le frontend ;
- L'application sera testée fonctionnellement dans plusieurs environnements en utilisant le framework `Selenium`, par exemple : `Firefox` et `Google Chrome`.

## Rendus attendus 

Le barème est le suivant :

- 1 note sur la partie tests unitaires (/20) ;
- 1 note sur la partie tests end-to-end (/20) ;
- Chaque partie a le même barème :
  + 3 points pour la partie tests unitaires (ou tests end-to-end) du rapport ;
  + 6 points pour la couverture de tests (nombre de tests, choix des scénarios, ...)
    * il est attendu une bonne couverture par lignes de code pour les tests unitaires sur les classes métier du backend et du frontend (environ 80%) ;
	* il est attendu au moins 5 tests `Selenium`.
    * attention à prioriser les tests
  + 6 points pour la qualité des tests (design patterns utilisés, lisibilité du code de test, tests indépendants, ...)
    * On utilisera un design pattern de `PageObject`, c'est-à-dire que les pages et les éléments de l'interface graphique seront décrits dans des classes de tests dédiées (voir cours).
  + 5 points pour le développement de l'application (aboutissement du projet, qualité du code, ...)
- Le rapport sur la réalisation de l'étude de cas devra contenir :
  + Une description rapide de l'application (et ses limitations) ;
  + Le code source de l'application, le code des tests unitaires et le code des tests `Selenium` ;
  + Les choix technologiques (si nécessaires) ;
  + Une documentation courte expliquant comment installer un environnement de développement sur l'installation (installation des dépendances, lancement de l'application, exécution des tests, ...) ;
  + Les choix de réalisations de tests, par exemple : donner un exemple expliquant pourquoi vous avez choisi de tester plus fortement certaines parties du code que d'autres ;
  + Processus de tests : donner un exemple expliquant en quoi l'écriture et l'exécution des tests en parallèle de la réalisation de l'application a impacté l'écriture de votre code de production.

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- SELENIUM is a trademark of Software Freedom Conservancy, Inc.
- "Python" is a registered trademark of the PSF.
- Java is a registered trademark of Oracle and/or its affiliates.
- Firefox® is a registered trademark of the Mozilla Foundation.
- Chrome™ is a trademark of Google LLC.
