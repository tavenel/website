---
title: Projet Bomberman - tests unitaires
date: 2024 / 2025
correction: false
---

# Projet Python Bomberman - ajout de tests unitaires

## Présentation

Le but de ce projet est de retravailler le projet Bomberman du module Python pour y ajouter des tests unitaires, et d'adapter le code du projet en conséquence.

### Objectifs pédagogiques

Ce projet vous permettra de :

- Mettre en place un framework de tests unitaires en Python
- Identifier les cas de tests à mettre en place
- Écrire des tests unitaires en Python
- (Ré)Architecturer son code pour le rendre testable

## Tests unitaires

Il est très compliqué de définir une couverture de test nécessaire et suffisante, car cela dépend énormément du code à tester : on privilégiera donc toujours la qualité du test sur les statistiques de sa couverture de code.

_On appelle code métier du code lié directement aux exigences fonctionnelles (et donc compréhensible par un expert du domaine - par exemple, la gestion des conditions de vol dans un programme d'aviation) et non un code ajouté simplement à cause de contraintes techniques (par exemple, comment interagir avec la base de données)._

Les parties de code _métier_ d'une application sont les plus critiques et celles à tester le plus en profondeur dans les tests unitaires. Au contraire, les classes ayant des dépendances externes sont en général difficiles à tester et sensibles aux changements d'implémentation : il est normal que leur couverture de tests unitaires soit moins importante.

- On activera la couverture de test dans l’IDE afin de vérifier que les classes sont bien testées.
- On ajoutera les tests unitaires nécessaires.
- On pensera à utiliser des substituts (`Mock`, `Stub`) lorsque c'est nécessaire pour s'abstraire des dépendances.
- On modifiera le code source de l’application pour corriger les bugs trouvés au fur et à mesure du développement (Test-Driven Development).

## Notation

Le barème est le suivant :

- 3 points sur un court rapport sur la réalisation des tests unitaires : expliquer pourquoi vous avez choisi de tester plus fortement certaines parties du code que d'autres, les changements à opérer dans le code pour le tester, etc… ;
- 7 points pour la couverture de tests (nombre de tests, choix des scénarios, ...)
  + il est attendu une bonne couverture par lignes de code pour les tests unitaires sur les classes métier du backend et du frontend (environ 80%) ;
- 7 points pour la qualité des tests (design patterns utilisés, lisibilité du code de test, ...)
- 3 points pour le (re)développement de l'application (aboutissement du projet, qualité du code, ...) suite à l'écriture de tests

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- "Python" is a registered trademark of the PSF.

