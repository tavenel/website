---
title: Exercices avancés Python
date: 2023 / 2024
---

# Commande de robot

Un robot est disposé sur une grille de taille supposée infinie dont les cases sont repérées par ses coordonnées (x, y).
Initialement, il est situé à l'origine (0, 0) et tourné vers le nord (vers les y croissant).

Les commandes de déplacement du robot sont :

- 'g' : rotation de 90° à gauche (si le robot est initialement orienté vers le nord, il sera orienté vers l'ouest) ;
- 'd' : rotation de 90° à droite (si le robot est initialement orienté vers le nord, il sera orienté vers l'est) ;
- entier de 1 à 9 : l'avancée du robot en nombre de cases selon sa direction en cours.


Les commandes seront passées dans une liste, par exemple :

```python
commandes = [4, 'd', 3]
```

Le robot avance de 4 cases vers le nord, tourne de 90° vers la droite, puis avance à nouveau de 3 cases vers l'est.

Pour compliquer l'exercice, des obstacles peuvent être disposés sur la grille. Les coordonnées des obstacles seront passées dans une liste, par exemple :

```python
obstacles = [(3, 2), (5, 1)]
```

Ici, deux obstacles sont placés aux coordonnées (3, 2) et (5, 1).

Si un obstacle se trouve sur la trajectoire du robot, ce dernier ne peut évidemment pas le traverser.
Le robot devra être bloqué sur la case qui précède l'obstacle, et passer à l'exécution de la commande suivante.

Écrire une fonction `robot_simulation(commandes, obstacles)` qui prend en paramètres une liste des commandes à exécuter et une liste de coordonnées d'obstacles (liste vide si pas d'obstacles). Pendant tout son parcours, le robot va plus ou moins s'éloigner de sa position de départ (0, 0). La fonction devra renvoyer la distance maximale élevée au carré (distance euclidienne) de la case la plus éloignée du point de départ atteinte par le robot.


```python
>>> robot_simulation(commandes = [7, 'd', 'd', 4], obstacles = [(0, 5)]) 
>>> 16
```

Car le robot ne se déplace que de 4 cases vers le nord avant d'être bloqué par un obstacle, puis de 4 cases après avoir fait demi-tour.
Le robot est donc revenu à sa position initiale, mais au cours de son trajet il a atteint la case (0, 4) juste avant de faire demi-tour et qui se trouve être la case la plus éloignée de l'origine (0,0), soit le carré de la distance égal à 16 (02 + 42).

Autres exemples :

```python
>>> robot_simulation(commandes = [4, 'd', 4, 'g', 1, 'd', 2, 'd', 3, 'd', 1], obstacles = [(0, 4), (3, 3)]) 
>>> 32 
  
>>> robot_simulation(commandes = ['g', 4, 'd', 3, 'g', 1, 'd', 'd', 5], obstacles = [(-4, 2)]) 
>>> 26
```

Source et crédit : <https://python.developpez.com/exercices/?page=Problemes-complexes#Commande-de-robot>

# Plus petit, plus grand - et détection de triche 

Le jeu "plus petit/plus grand" est un des classiques dans l'apprentissage de la programmation. L'ordinateur génère un nombre aléatoire et le joueur essaye de le retrouver. À chaque étape, l'ordinateur indique si le nombre proposé est plus petit ou plus grand que le nombre à trouver.
Ici, l'exercice proposé est de programmer la position inverse : le joueur choisit un nombre et l'ordinateur essaye de le retrouver selon la même approche.

La vraie difficulté de l'exercice sera que le programme doit détecter la tricherie (celle du joueur, car le programme, lui, ne triche jamais). Ce cas se produit quand l'ordinateur propose (par exemple) 50 et que le joueur répond "+". Puis plus tard, il propose 51 et le joueur répond "-". Et bien entendu, une situation symétrique si l'ordinateur propose (toujours) 50 et que le joueur répond "-". Puis plus tard, il propose 49 et le joueur répond "+".

## Exemple de résultat honnête

```python
Mémorisez un nombre entre 1 et 100, je vais essayer de le retrouver
Appuyez sur <enter> quand vous serez prêt. Et ne trichez pas ensuite...
Je propose 57... +, - ou G ?-
Je propose 37... +, - ou G ?-
Je propose 19... +, - ou G ?+
Je propose 25... +, - ou G ?G
J'ai trouvé 25 en 4 coups !!!
```

## Exemple de tricherie

```python
Mémorisez un nombre entre 1 et 100, je vais essayer de le retrouver
Appuyez sur <enter> quand vous serez prêt. Et ne trichez pas ensuite...
Je propose 44... +, - ou G ?-
Je propose 29... +, - ou G ?-
Je propose 17... +, - ou G ?+
Je propose 25... +, - ou G ?+
Je propose 27... +, - ou G ?-
Je propose 26... +, - ou G ?-
Tricheur !!! A la réponse 4 il avait été proposé 25 et répondu "+" - En proposant 26 la réponse ne peut pas être "-" !!!
J'ai gagné par forfait en 6 coups !!!
```

Source et crédit : <https://python.developpez.com/exercices/?page=Problemes-complexes#Plus-petit-Plus-grand>

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- "Python" is a registered trademark of the PSF. The Python logos (in several variants) are use trademarks of the PSF as well.
