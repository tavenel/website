---
title: Exercices POO
author: Tom Avenel
date: 2023 / 2024
correction: false
---

## Création d'une classe

Créez une classe nommée `Personne` avec les attributs suivants : `nom`, `prenom`, `age` et `adresse`. Ajoutez également une méthode nommée "parler" qui affiche un message de salutation.

## Composition - Bibliothèque

1. Créez une classe `Livre` qui a des attributs `titre` et `auteur`. Ajoutez une méthode `afficher` qui affiche le titre et l'auteur du livre.
2. Créez une classe `Bibliotheque` qui a un attribut `livres` (une liste d'objets `Livre`). Ajoutez des méthodes `ajouter_livre` et `supprimer_livre` pour ajouter et supprimer des livres de la bibliothèque.

## Héritage et polymorphisme

### Héritage - Personne et Employé

Créez une classe nommée `Employe` qui hérite de la classe `Personne`. Ajoutez un nouvel attribut à la classe `Employe` nommé `salaire` et une méthode nommée `travailler` qui affiche un message disant que l'employé est en train de travailler.

Pour utiliser une méthode de la classe parente, on utilise la fonction `super()`, par exemple : `super().__init__(...` appelle le constructeur du parent.

### Polymorphisme - animaux

Créez une classe nommée `Animal` avec une méthode `regime_alimentaire`. Ensuite, créez deux sous-classes `Lapin` et `Chat` qui héritent de la classe `Animal` et qui affichent chacune à l'écran le `regime_alimentaire` de l'animal : `"végétarien"` pour `Lapin` et `"carnivore"` pour `Chat`.

### Polymorphisme - Véhicule et Bus

Créer une classe `Bus` héritant de la classe `Vehicle` ayant une capacité par défaut de `50` :
`Bus.seating_capaticy()` retourne `The seating capacity of a bus is 50 passengers`

