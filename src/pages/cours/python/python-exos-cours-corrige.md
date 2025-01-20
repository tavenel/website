---
title: Correction des exercices de cours
---

# Exercice : Multiplication

Dans le shell Python, définir et initialiser deux variables numériques x et y (on choisira la valeur de x et de y). Calculer et afficher : "Le résultat de la multiplication de x par y est : z" en remplaçant z par sa valeur.

## Correction

```python
x = 4
y = 5
print("Le resultat de la multiplication de x par y est :", x * y)
```

---

# Exercice : Test de résultat

Reprendre l'exercice de la multiplication de deux variables numériques x et y. Si le résultat est supérieur à 50, afficher : 'Le résultat de la multiplication z est supérieur à 50' en remplaçant z par sa valeur. Sinon, afficher 'le résultat z est inférieur à 50.'

## Correction

```python
x = 4
y = 5
z = x * y

if z > 50:
	print("Le resultat de la multiplication :", z, "est supérieur à 50")
else:
	print("Le resultat de la multiplication :", z, "est inférieur à 50")
```

---

# Exercice : somme

Calculer la somme : `1+3+5+...+99`

## Correction

```python
s = 0
for i in range(1,100,2):
	s += i

# ou
s = sum( [ i for i in range(1,100,2) ] )

print(s) # 2500
```

---

# Exercice : intersection d'ensembles

Renvoyer l'ensemble des éléments en commun dans les 2 ensembles suivants :

- `set1 = {10, 20, 30, 40, 50}`
- `set2 = {30, 40, 50, 60, 70}`
- 1ère méthode : utiliser une fonction de la classe `Set` permettant de calculer cette intersection.
- 2ème méthode : utiliser une boucle `for`.

## Correction

```python
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

s = set()
for x in set1:
	if x in set2:
		s.add(x)

print(s)
```

---

# Exercice : multiplication avec fonction

Reprendre l'exercice de multiplication de deux variables numériques x et y. Définir une fonction `multiplie` réalisant l'opération de multiplication et appeler cette fonction avant de réaliser le test sur l'affichage du résultat.

## Correction

```python
def multiplie(x,y):
	return x * y

print(multiplie(2,3))
```

---

# Exercice: Visibilité des variables

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Quelle est la visibilité de chaque variable ?

## Correction

```
#global => pas de variable 'spam'

scope_test()

	spam = "test spam" # contexte de "spam_scope_test"

	do_local()
		spam = "local spam" # local "spamL" : différent de "spam_scope_test"
	#scope_test
	print(spam) # "spam_scope_test" => "test spam"

	do_nonlocal()
        nonlocal spam # "spam_non_local" => redéfinit "spam_scope_test"
        spam = "nonlocal spam" => "spam_scope_test" == "spam_non_local" = "nonlocal spam"
	#scope_test
	print(spam) # "spam_scope_test" => "nonlocal spam"

	do_global()
        global spam # "spam_global" => crée une variable globale "spam" (n'existe pas encore)
        spam = "global spam" => "spam_global" = "global spam"
	print(spam) # "spam_scope_test" => "nonlocal spam"

#global
print(spam) # "spam_global" => "global spam"
```

---

# Exercice : héritage multiplie

- Écrire une classe `Mouette` héritant de deux classes parentes : une classe `Oiseau` et une classe `Vol`.
- La classe `Oiseau` possède une fonction booléenne `ovipare`. La classe `Vol` implémente la fonction `deplacement` d'une interface `Locomotion` en renvoyant : `deplacement() => "vol"`
- Instancier un objet `m` de type `Mouette`. Cette objet doit répondre au contrat suivant :
  + `m.deplacement() => "vol"`
  + `m.ovipare() => True`

## Correction

```python
class Oiseau:

    def ovipare(self) -> bool:
        return True

class Locomotion:

    def deplacement(self) -> str:
        '''
        Un mode de déplacement
        '''
        pass

class Vol(Locomotion):

    def deplacement(self) -> str:
        return 'Vol'


class Mouette(Oiseau, Vol):
    pass

m = Mouette()
print(m.deplacement())
print(Mouette.deplacement(m))
print(m.ovipare())
```

---

# Exercice : récupération des arguments

Écrire un script Python affichant le résultat de la multiplication de tous les nombres passés en paramètres. On utilisera une boucle d'itération sur les arguments du script.

## Correction

```python
#!/usr/bin/env python3

import sys

res = 1
for arg in sys.argv[1::]:
	res *= arg

print(arg)
```
