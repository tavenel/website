---
title: Projet Python Bomberman
author: Tom Avenel
date: 2024 / 2025
correction: false
---

# Projet Python - Bomberman

## Présentation

Bienvenue dans ce projet où vous allez coder votre propre jeu en Python ! Le but de ce projet est de vous initier à la programmation tout en développant un petit jeu. Vous allez créer un jeu inspiré de Bomberman : [Wikipedia](https://en.wikipedia.org/wiki/Bomberman) . Le jeu consiste en un plateau de jeu parsemé d'ennemis à éliminer en déposant des bombes stratégiquement.

### Objectifs pédagogiques

Ce projet vous permettra de :

- Manipuler les variables et les types de données en Python.
- Utiliser des structures de contrôle comme les conditions et les boucles.
- Générer des nombres aléatoires.
- Gérer les entrées utilisateur.
- Implémenter des fonctionnalités de base d'un jeu et introduire des éléments de gamification (niveaux, scores, etc.).

### Fonctionnalités du jeu

- Le plateau de jeu est un rectangle de `i` lignes et `j` colonnes formant `i*j` cases de jeu.
- Une case est soit :
  - vide
  - une brique incassable
  - une brique cassable
  - le personnage du/des joueur(s)
  - un ennemi
  - il ne peut pas y avoir plusieurs personnages sur une case : si un ennemi essaie de se déplacer sur la case d'un joueur (ou réciproquement), le joueur est éliminé
- Le personnage et les ennemis peuvent se déplacer horizontalement ou verticalement (pas en diagonale) sur une case adjacente **sauf si elle est occupée** (brique ou ennemi ou autre joueur).
- Le personnage peut déposer une bombe sur sa position en appuyant sur une touche du clavier.
  - la bombe explose après un certain délai (temps en secondes ou nombre de mouvements du joueur) sur une croix de 2 cases autour de la bombe (2 cases à droite, 2 cases à gauche, 2 cases en haut, 2 cases en bas).
  - une bombe qui explose élimine un joueur dans son rayon d'action
  - une bombe qui explose détruit un mur cassable ou un ennemi dans son rayon d'action
  - le nombre de bombes n'est pas limité (ce sera une amélioration du jeu)

### Conditions de victoire

Le jeu possède 2 modes : histoire ou compétition

#### Mode de jeu : histoire

- La partie s'arrête soit :
  - lorsque tous les ennemis sont éliminés : victoire
  - lorsque tous les joueurs sont éliminés : défaite
  - après un certain temps : défaite

#### Mode de jeu : compétition (bonus)

- La partie s'arrête soit :
  - lorsque tous les joueurs sont éliminés : défaite collective
  - lorsqu'un seul joueur n'est pas encore éliminé : victoire du dernier joueur
  - après un certain temps : match nul

## Implémentation

- Le plateau de jeu est à réaliser sur la console (plateau de jeu à 2 dimensions) ;
- Il doit contenir différents types de cases : ennemis, briques cassables, briques incassables ;
- La position de départ du (des) joueur(s) est laissée au choix des développeurs ;

### Itérations

Dans un premier temps, on implémentera le mode _histoire_

#### Version 1 - Un premier plateau

- Pour la première version, créer un petit plateau de jeu codé en dur dans le programme - ce sera donc toujours le même plateau qui sera utilisé.
- Afficher le plateau à l'écran

#### Version 2 - Un joueur se déplace

- Ajouter un personnage sur le plateau pouvant se déplacer horizontalement ou verticalement

#### Version 3 - Des ennemis

- Ajouter des ennemis (ne se déplaçant pas).
- Coder et vérifier que si le joueur rencontre un ennemi, la partie est perdu

#### Version 4 - Des briques

- Ajouter des briques dans le labyrinthe - le joueur ne peut pas les traverser.

#### Version 5 - Les bombes

- Coder la possibilité de déposer une bombe à la position actuelle du joueur.
- Après un certain temps, la bombe doit faire exploser les ennemis alentour et les briques cassables.

#### Version 6 - Score

On ajoutera une gestion du score : le joueur commence avec un certain nombre de points, chaque déplacement fait perdre des points. Le but est de finir la partie le plus rapidement possible afin de gagner le maximum de points.

#### Version 7 - Ennemis en mouvement

- Faire se déplacer les ennemis aléatoirement

### Bonus 1 : Score en base de données

On ajoutera un système de gestion des meilleurs scores qui seront enregistrés en base de données.

### Bonus 2 : Génération de cartes aléatoires

Le plateau doit pouvoir être généré aléatoirement à chaque partie. On choisira uniquement la taille du plateau.

### Bonus 3 : Ennemis intelligents

Dans cette dernière version (en bonus), les ennemis entendent l'arrivée du joueur et essaient de s'en approcher le plus possible. On pourra ensuite optimiser cette version pour ne se déplacer que lorsque le joueur est suffisamment proche pour être entendu (par exemple, à partir d'une distance euclidienne de 4 cases).

### Bonus 4 : Sauvegarde et restauration de partie

1. Ajouter une fonction dans l'interface permettant une sauvegarde de la partie courante en base de données.
2. Ajouter une fonction dans l'interface permettant une charger la partie sauvegardée et de continuer la partie.

### Bonus 5 : Mode multi-joueur

- Permettre à deux joueurs de jouer en même temps (en utilisant le même clavier)

### Bonus 6 : Modes _compétition_

- Implémenter le mode compétition (nécessite le mode multi-joueur).

## Évaluation

### Le rapport

Chaque groupe devra fournir un rapport résumant la réalisation de leur projet. Ce rapport est un rapport technique devant inclure :

- un court rappel du projet et des fonctionnalités attendues ;
- l'architecture de votre projet ;
- les choix techniques réalisés ;
- les spécificités de votre application ;
- les soucis rencontrés ;
- des axes d'amélioration pour le futur.

Le rendu devra également inclure le code source prêt pour la production (code nettoyé, commenté, ...).

### La soutenance

Chaque groupe devra présenter sa solution lors d'une soutenance.

Attention, il ne s'agit pas de lire le rapport ou de le recopier dans quelques slides, mais bien de présenter le projet à un jury qui ne connaîtrait pas votre réalisation. Il est fortement conseillé d'inclure une démonstration de votre rendu.

