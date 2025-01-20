---
title: Figures colorées
author: Tom Avenel
date: 2023 / 2024
correction: false
---

# Figures géométriques

## Classe Rectangle

- Écrire une classe `Rectangle` permettant de construire un rectangle dotée d'attributs `longueur` et `largeur`.
- Créer une méthode `perimetre()` permettant de calculer le périmètre du rectangle et une méthode `surface()` permettant de calculer la surface du rectangle
- Créer 2 instances de `Rectangle` et calculer leurs `perimetre()` et `surface()`.

## Héritage : classe Carre

- Créer une classe `Carre` héritant de `Rectangle` et permettant de créer un carré.
- Créer une instance de `Carre` et calculer son `perimetre()` et `surface()`.

## Classe Cercle

- Créer une classe `Cercle` pour construire un cercle ayant un `rayon`.
- Ajouter des méthodes `perimetre()` et `surface()`. Utiliser `math.pi` (`import math`).
  + On rappelle que le périmètre d'un cercle se calcule par la formule : $2\Pi.r$
  + On rappelle que la surface d'un cercle se calcule par la formule : $\Pi.r^2$
- Que remarque-t-on quand aux méthodes de ces différentes classes ?
  + Quel type d'architecture permet de gérer proprement cette similarité ?
  + Implémenter cette architecture

# Couleurs

## RGB

- Créer une classe `CouleurRGB` permettant de stocker une couleur au format Rouge, Vert, Bleu. Cette classe possède donc 3 attributs (entiers) : `rouge`, `vert`, `bleu`.
- Ajouter une méthode `couleur_rgb()` affichant la couleur RGB sous forme d'un triplet : `(rouge,vert,bleu)`. Par exemple : `(10,20,100)`.
- Ajouter une méthode `couleur_hexa()` permettant de retourner la couleur au format hexadécimal correspondant : on utilisera le code `f"#{r:02x}{g:02x}{b:02x}"` pour convertir 3 variables `r`, `g` et `b`.

## Hexadécimal

- Créer une classe `CouleurHexa` permettant de stocker une couleur au format hexadécimal. Cette classe possède un attribut unique (chaîne de caractères de type : `#aabbcc`) : `hexa`.
- Ajouter une méthode `couleur_hexa()` permettant de retourner la couleur au format hexadécimal.
- Ajouter une méthode `couleur_rgb()` permettant de retourner la couleur RGB correspondante. On utilisera le code : `(int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16))` pour convertir une chaîne de caractères hexadécimale `hx` (de type `#aabbcc`) en triple `R,G,B` correspondant.

# Délégation : figure avec couleur

En utilisant 2 fois un pattern de délégation pour les figures géométriques et pour les couleurs, créer une classe : `FigureColoree` représentant une figure géométrique ayant une couleur.

Les instances de cette classe doivent posséder les méthodes suivantes : `perimetre()`, `surface()`, `couleur_rgb()`, `couleur_hexa()`.

