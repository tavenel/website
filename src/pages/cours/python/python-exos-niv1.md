---
title: Exercices Python niveau 1
author: Tom Avenel
correction: false
---

## Entrée utilisateur

Écrire un programme qui demande à l'utilisateur de saisir son nom et affiche un message de bienvenue avec son nom.

## Tables de multiplication

Écrire un programme qui affiche les `n` premiers termes de la table de multiplication d'un nombre donné.

L'utilisateur doit saisir la valeur de `n` et le nombre pour lequel la table de multiplication doit être affichée.

## Diviseurs

### Diviseurs d'un nombre

L'utilisateur donne un entier supérieur à 1 et le programme affiche, s'il y en a, tous ses diviseurs propres sans répétition ainsi que leur nombre. S'il n'y en a pas, il indique qu'il est premier.
Pour rappel, `a` est un diviseur de `b` si, et seulement si, `a % b = 0`.
Par exemple :

```
Entrez un entier strictement positif : 12
Diviseurs propres sans répétition de 12 : 2 3 4 6 (soit 4 diviseurs propres)
Entrez un entier strictement positif : 13
Diviseurs propres sans répétition de 13 : aucun ! Il est premier
```

### Nombres premiers

Écrire un programme affichant la liste des 100 plus petits nombres premiers.

## Suite de Fibonacci

Écrire un programme qui calcule la suite de _Fibonacci_ jusqu'à un nombre donné. La suite de _Fibonacci_ est définie de la manière suivante : la première valeur est $0$, la deuxième valeur est $1$, et chaque valeur suivante est la somme des deux valeurs précédentes.

## Gardien de phare

Un gardien de phare descend de son phare 5 fois par jour.

Écrire une procédure (donc sans `return`) `hauteurParcourue()` qui reçoit deux paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
 
> Pour x marches de y cm, il parcourt z.zz m par semaine.

On n'oubliera pas :

- qu'une semaine comporte 7 jours ;
- qu'une fois en bas, le gardien doit remonter ;
- que le résultat est à exprimer en m.

Pour afficher le résultat, on pourra utiliser le formatage de chaîne de caractères Python suivant : `{:.2f}` permettant de formater l'affichage en un flottant à 2 chiffres après la virgule, par exemple le code suivant affichera : `La valeur de x est 3.14` :

```python
x = 3.14159265
print("La valeur de x est {:.2f}".format(x))
```

## Chaîne d'ADN

Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide (valide signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison arbitraire de "a", "t", "g" ou "c").

- Écrire une fonction `valide()` qui renvoie vrai si la saisie est valide, faux sinon.
- Écrire une fonction `saisie()` qui effectue une saisie valide et renvoie la valeur saisie sous forme d'une chaîne de caractères. On utilisera la fonction `input()`.
- Écrire une fonction `proportion()` qui reçoit deux arguments, la chaîne et la séquence et qui retourne la proportion de séquence dans la chaîne (c'est-à-dire son nombre d'occurrences).

On pourra utiliser la fonction `len()` qui calcule la longueur d'une chaîne de caractères `mon_texte` : `len(mon_texte)`.

Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence et affiche le résultat.

Exemple d'affichage :

```
chaîne : attgcaatggtggtacatg
séquence : ca
Il y a 10.53 % de "ca" dans votre chaîne.
```

