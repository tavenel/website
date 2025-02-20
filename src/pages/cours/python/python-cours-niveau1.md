---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Cours sur le langage Python
tags:
- python
---

# Installation de l'environnement de développement

---

# Installer Python et gérer les dépendances

- Suivre les sections "Installer Python" et "Installation de Visual Studio Code" de la [documentation Microsoft][doc-install-microsoft].
- Pour une procédure plus détaillée, voir la [documentation officielle][doc-install-win].
- Pour une installation dans un environnement virtuel `virtualenv`, voir la [documentation sur les venv][doc-venv].
- Pour gérer l'installation de modules, voir la [documentation sur l'installation de modules Python][doc-python-modules].
- Pour utiliser Python directement dans le navigateur : <https://trinket.io/>

---

# Erreurs courantes

- Installations parallèles de Python : la commande `py` ou `python` n'exécute pas le bon programme python avec la bonne version :
  - Gérer la variable d'environnement `$PATH` : voir [ce tutoriel sous Windows](https://www.malekal.com/comment-modifier-la-variable-path-sous-windows-10-11/)
  - Si `virtualenv`, vérifier que sa configuration a été chargée dans le terminal courant

---

- `pip install ...` a bien installé la dépendance mais `python` ne trouve pas la dépendance :
  - `pip` vient du `$PATH` : il peut référencer un module pip d'une autre version de python que la version actuelle
  - préférer `python -m pip` qui force à utiliser le module pip de la version courante.
- `pip not found` :
  - dernières versions de Python => exécuter dans un terminal administrateur : `python -m ensurepip --upgrade`
  - anciennes versions : désinstaller et réinstaller Python

---
layout: section
---

# Présentation du langage

---

# Présentation du langage Python

Python est un langage **interprété** utilisant un **typage dynamique**.

---

Le langage Python est utilisé principalement pour le développement :

- de scripts ;
- de tests ;
- de calculs scientifiques : big data, machine learning ;
- d'applications de bureau complètes ;
- d'applications web.

---

# Les versions de Python

Python 3 a été une réécriture importante du langage et de ses paradigmes, avec des changements incompatibles avec la version 2.
Il est donc courant de déployer à la fois un interpréteur Python 2 et Python 3 sur sa machine personnelle, voir sur un serveur.
Ce cours se concentre sur la dernière version de **Python 3**.

---
layout: section
---

# Eléments principaux de syntaxe

---

# Affichage

```python
print(3)

print('Ma valeur suivante est :', 5)
```

---

# Variable

## Variable simple

```python
ma_variable = 42

print('ma_variable :', ma_variable)
```

---

## Typage dynamique

```python
ma_variable = 42

print( type(ma_variable) )
```
---

## Documentation de types

```python
ma_variable_entier: int = 42

print(ma_variable_entier)
print( type(ma_variable_entier) ) # int
```

---

**Attention : le type n'est que de la documentation !!**

```python
ma_variable_entier: int = 'Hello'

print(ma_variable_entier)
print( type(ma_variable_entier) ) # str
```
---

## Double assignation

```python
ma_variable1, ma_variable2 = 4, 8

print('ma_variable1 :', ma_variable1, ' et ma_variable2 : ', ma_variable2)
```

---

# Commentaires

```python
# Une ligne de commentaires
```

---

```python
ma_variable = 42  # Un commentaire en bout de ligne

print('ma_variable :', ma_variable)
```

---

# Chaînes de caractères (type : str)

## Ligne simple

```python
mon_texte1 = "Hello, World !"
mon_texte2 = 'Hello, World !' # Totalement équivalent à la ligne précédente
mon_texte3 :str = 'Hello, World !' # Totalement équivalent à la ligne précédente

print(mon_texte1)
print(mon_texte2)
print(mon_texte3)
print( type(mon_texte1) ) # str
print( type(mon_texte2) ) # str
print( type(mon_texte3) ) # str
```

---

## Multi-ligne

```python
mon_texte4 = """Hello
World !"""
mon_texte5 = '''Hello
World !'''

print(mon_texte4)
print(mon_texte5)
print( type(mon_texte4) ) # str
print( type(mon_texte5) ) # str
```

---

# f-string : chaîne de caractères avec variables

```python
ma_var = 42
mon_texte6 = f'La variable ma_var vaut : {ma_var}'

print(mon_texte6)
print( type(mon_texte6) ) # str
```

---

# Arithmétique

## Support des opérations artihmétiques standard (type: int)

```python
ma_var = 42
resultat = 2 * ma_var / 5

print(resultat)
print( type(resultat) ) # float
```

---

## Précision des float

Que retourne le code suivant ?

```python
0.1 + 0.2
```

---

# Exercice : multiplication

Dans le shell Python, définir et initialiser deux variables numériques x et y (on choisira la valeur de x et de y). Calculer et afficher : "Le résultat de la multiplication de x par y est : z" en remplaçant z par sa valeur.

---

# Opérations logiques (type: bool)

## and

```python
x1 = True
x2 = False
y1 = True
y2 = False

print( x1 and y1 ) # True
print( x2 and y1 ) # False
print( x1 and y2 ) # False
print( x2 and y2 ) # False
```

---

## or

```python
x1 = True
x2 = False
y1 = True
y2 = False

print( x1 or y1 ) # True
print( x2 or y1 ) # True
print( x1 or y2 ) # True
print( x2 or y2 ) # False
```

---

## not

```python
x1 = True
x2 = False

print( not x1 )
print( not x2 )
```

---

# Tests

```python
print( 1 < 2 )

print( 1 > 2 )

print( 3 <= 4 )

print( 3 >= 4 )
```

---

# Tests - suite

```python
print( [1, 2] == [3, 4] )

print( [1, 2] != [3, 4] )

print( [1, 2] == [1, 2] ) # True
```

---

# Ensemble

```python
mon_ensemble = { 'Cat', 'Dog' } # Pas d'élément dupliqué

print( mon_ensemble )
print( type(mon_ensemble) ) # set
```

---

# **Séquence**

---

## Liste

```python
ma_liste = [ 1, 2, 4, 8, 16 ]

print( ma_liste )
print( type(ma_liste) ) # list
print( ma_liste[0] )
print( type(ma_liste[0]) ) # int
```

---

### Assignation

```python
ma_liste :list = [ 1, 2, 4, 8, 16 ]

ma_liste[1] = 3
print( ma_liste ) #  [1, 3, 4, 8, 16]
```

---

### Extraction - slices

```python
ma_liste :list = [ 1, 2, 4, 8, 16 ]

# Extrai et copie de liste
print( ma_liste[1:3] ) # [2, 4]
print( ma_liste[:-1] ) # [1, 2, 4, 8]
print( ma_liste[2:] )  # [4, 8, 16]
```

Pour plus d'information sur les slices, voir [ce cours][zds-slices].

---

## Construction de liste par expression

Une liste peut se construire avec l'expression `[ expression for element in ... ]`
```python
liste1 = [ 1, 2, 4 ]
liste2 = [ 2 * x for x in liste1 ]

print( liste1 ) # [1, 2, 4]
print( liste2 ) # [2, 4, 8]
```

---

## Range

```python
my_range = range(5)

print( my_range )
print( type(my_range) ) # range
```

---

## Tuple (n-uplet)

```python
mon_tuple = 1, 'Hello' # Tuple (1, 'Hello')

print( mon_tuple )
print( mon_tuple[0] ) # 1
print( mon_tuple[1] ) # 'Hello'
print( type(mon_tuple) ) # tuple
```

[Documentation sur les séquences][doc-seq]

---

# Dictionnaires

```python
mon_tel = {'jack': 4098, 'sape': 4139}

print( mon_tel )
print( mon_tel['jack'] ) # 4098
print( mon_tel['sape'] ) # 4139
print( type(mon_tel) ) # dict
```

---

## Addition / Concatenation 

```python
print( 2 + 5 )

print( [1, 2] + [3, 4] )

print( 'Hello, ' + "World !" )
```

---

# **Boucles**

---

# If

---

```python
x = -1
if x < 0:
    print('Nombre negatif')
elif x == 0:
    print('Zero')
else:
    print('Nombre positif')
```

---

```python
x = 0
if x < 0:
    print('Nombre negatif')
elif x == 0:
    print('Zero')
else:
    print('Nombre positif')
```

---

```python
x = 2
if x < 0:
    print('Nombre negatif')
elif x == 0:
    print('Zero')
else:
    print('Nombre positif')
```

---

# Exercice : Test de résultat

Reprendre l'exercice de la multiplication de deux variables numériques x et y. Si le résultat est supérieur à 50, afficher : 'Le résultat de la multiplication z est supérieur à 50' en remplaçant z par sa valeur. Sinon, afficher 'le résultat z est inférieur à 50.'

---

# For : itérations sur une séquence

## Liste

```python
ma_sequence = ['Cat', 'Dog', 'Bird']
for w in ma_sequence:
    print(w)
```

---

## Set

```python
ma_sequence = {'Cat', 'Dog', 'Bird'}
for w in ma_sequence:
    print(w)
```

---

## Itération sur les éléments d'un dictionnaire

```python
mon_dict = {'firstname': 'John', 'lastname': 'Doe'}
for (k,v) in mon_dict.items():
    print(f"La clé {k} a pour valeur {v}")
```

---

## Itération sur les valeurs d'un dictionnaire

```python
mon_dict = {'firstname': 'John', 'lastname': 'Doe'}
for v in mon_dict.values():
    print(f"Les valeurs du dictionnaire sont : {v}")
```
---

## Itération sur les clés d'un dictionnaire

```python
mon_dict = {'firstname': 'John', 'lastname': 'Doe'}
for k in mon_dict.keys():
    print(f"Les clés du dictionnaire sont : {k}")
```

---

## Range

```python
for i in range(0,10,3):
    print(i, end=',')
```

---

## yield

- Générateurs : valeurs créées au fur et à mesure plutôt que tout d'un coup (lazy)
- utile pour grands ensembles ou séquences infinies
- écrire un générateur est difficile
- `yield` : générateur simple : suspends l'exécution d'une fonction, retourne une valeur, le prochain appel à la fonction reprend au même endroit

---

```python
def generateur_de_nombres():
    yield 1
    yield 2

mon_generateur = generateur_de_nombres()

print(next(mon_generateur))  # >>> 1
print(next(mon_generateur))  # >>> 2
print(next(mon_generateur))  # >>> Erreur: StopIteration

```

---

```python
def generateur_de_carres(n):
    for i in range(n):
        yield i ** 2

mon_generateur = generateur_de_carres(5)

# Utiliser une boucle for pour itérer à travers les valeurs générées
for carre in mon_generateur:
    print(carre)
```

Carrés générés au fur et à mesure : économise de la mémoire, temps d'exécution constant

---

# Exercice : somme

Calculer la somme : `1+3+5+...+99`

---

# Exercice : intersection d'ensembles

Renvoyer l'ensemble des éléments en commun dans les 2 ensembles suivants :

- `set1 = {10, 20, 30, 40, 50}`
- `set2 = {30, 40, 50, 60, 70}`
- 1ère méthode : utiliser une fonction de la classe `Set` permettant de calculer cette intersection.
- 2ème méthode : utiliser une boucle `for`.

---

# Case

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403: # Multi-matching using '|'
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

---

# Pattern matching utilisant une structure

```python
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

---

# Fonctions

```python
def ma_fonction_carre(n):
    """Affiche le carré du nombre
    fourni en paramètre
    """
    print(n**2)

ma_fonction_carre(3)
```

---

## `return`

```python
def ma_fonction_carre(n):
    """Affiche le carré du nombre
    fourni en paramètre
    """
    return n**2

resultat = ma_fonction_carre(3)
print( resultat )
print( type(resultat) )
```

---

## Avec documentation des types

```python
def ma_fonction_carre(n: int) -> int:
    """Affiche le carré du nombre
    fourni en paramètre
    """
    return n**2

resultat :int = ma_fonction_carre(3)
print( resultat )
print( type(resultat) ) # int
```

---

## Procédure

```python
def afficher_text(msg:str):
    print(msg)

resultat = afficher_text('hello')
print( resultat )
print( type(resultat) ) # NoneType
```

---

## Non modification des paramètres (passage par valeur)

```python
x = 2
def f(n):
    n += 1
    print(f'n vaut : {n}')

f(x)
print(f'Après appel, x vaut : {x}')
```

---

# Exercice : multiplication avec fonction

Reprendre l'exercice de multiplication de deux variables numériques x et y. Définir une fonction `multiplie` réalisant l'opération de multiplication et appeler cette fonction avant de réaliser le test sur l'affichage du résultat.

---

# Valeurs par défaut

Les fonctions Python permettent de ne pas passer de valeur à un paramètre afin d'utiliser une valeur par défaut :

```python
def ma_func(param='valeur_par_defaut'):
    print(param)

ma_func() # valeur_par_defaut
ma_func('valeur 2') # valeur 2
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

---

# `*args` et `**kwargs`

- Permet de fournir une liste ou un dict d'arguments d'un coup (_unpacking_)
- `*args` : ensemble des arguments non nommés (liste)
- `**kwargs` : ensemble des arguments nommés (dict)

---

```python
# Unpacking explicite avec une liste, puis un dictionnaire
def aire_rectangle(a, b):
    return a*b

def aire_rectangle(cote1=0, cote2=0):
    return cote1*cote2

if __name__ == '__main__':
    rec1 = [3, 8]
    rec2 = {'cote1':4, 'cote2':8}
    # La liste rec1 va etre depaquetee en arguments unitaires
    print aire_rectangle(*rec1)
    # Le dictionnaire rec2 va etre depaquete en arguments unitaires
    print aire_rectangle(**rec2)
```

---

```python
# packing explicite
def aire_rectangle(*args):  # les arguments passes en parametre sont paquetes dans args qui se comporte comme un tuple
    if len(args) == 2:
        return args[0]*args[1]
    else:
        print('Merci de stipuler deux parametres')

def aire_rectangle2(**kwargs):  # les arguments passes en parametre sont paquetes dans kwargs qui se comporte comme un dictionnaire
    if len(kwargs) == 2:
        result = 1
        for key, value in kwargs.items():
            result *=value
        return result
    else:
        print('Merci de stipuler deux parametres')

if __name__ == '__main__':
    # Une liste va etre creee a partir des arguments fournis
    print aire_rectangle(3,8)
    # Un dictionnaire va etre cree a partir des arguments nommes
    print aire_rectangle2(cote1=4, cote2=8)
```

---

```python
# En cumulant les deux et d'autres arguments
def print_my_list(title_list, title_dict, *my_list, **my_dict):
    # Dans ce namespace, my_dict est un dictionnaire et my_list une liste
    
    print('ici les elements de la liste %s' % (title_list))
    for idx,value in enumerate(my_list):
        print('Index %02d: %s' % (idx, value))

    print('voici les elements du dictionnaire %s' % (title_dict))
    for key,value in my_dict.items():
        print('Element %s: %s' % (key, value))

if __name__ == '__main__':
    # En appel direct
    print_my_list('liste 0', 'dict 0', 0, 1, 2, zero=0, un=1, deux=2)

    # En passant une liste et un dict
    l1=[ 0, 1, 2 ]
    d1={ 'zero': 0, 'un': 1, 'deux': 2 }
    print_my_list('liste 0', 'dict 0', *l1, **d1)
```

---

<!-- class: liens -->

# Liens utiles - généralités

- [Installer Python sous Windows][doc-install-win]
- [Installation de modules Python][doc-python-modules]
- [Tutoriel officiel - Installing Packages (EN)][doc-python-install-en]
- [Bibliotheque standard][doc-stdlib]
- [Documentation complète][doc-full]
- [Reference du langage Python][doc-ref]
- [Les séquences][doc-seq]
- [Les exceptions][doc-exceptions]
- [Annotations de types][zds-annotations]
- [Cours sur les slices][zds-slices]
- [Venv][doc-venv]
- [Le site Pypi][site-pypi]

---

# Liens utiles - exercices

- [Visualisation graphique d'exécution de code][python-tutor]
- [Python Challenges][python-challenge]

[python-logo]: https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg
[doc-install-win]: https://docs.python.org/fr/3/using/windows.html
[doc-install-microsoft]: https://learn.microsoft.com/fr-fr/windows/python/beginners
[doc-python-modules]: https://docs.python.org/fr/3/installing/index.html
[doc-python-install-en]: https://packaging.python.org/en/latest/tutorials/installing-packages/
[doc-ref]: https://docs.python.org/fr/3/reference/index.html#reference-index
[doc-seq]: https://docs.python.org/fr/3/library/stdtypes.html#typesseq
[doc-exceptions]: https://docs.python.org/fr/3/library/exceptions.html#bltin-exceptions
[doc-stdlib]: https://docs.python.org/fr/3/tutorial/stdlib.html
[doc-full]: https://docs.python.org/fr/3/library/index.html#library-index
[doc-venv]: https://docs.python.org/3/tutorial/venv.html
[zds-annotations]: https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/2-functions/2-annotations-signatures/
[zds-slices]: https://zestedesavoir.com/tutoriels/582/les-slices-en-python/
[site-pypi]: https://pypi.org 
[scipy]: https://scipy-lectures.org/
[numpy-matplotlib]: https://zestedesavoir.com/tutoriels/4139/les-bases-de-numpy-et-matplotlib/
[async]: https://www.integralist.co.uk/posts/python-asyncio/
[decorator]: https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/2-functions/3-decorators/
[python-tutor]: https://pythontutor.com/
[python-challenge]: http://www.pythonchallenge.com/

---

# Legal

- "Python" is a registered trademark of the PSF. The Python logos (in several variants) are use trademarks of the PSF as well.
- PYPI is a trademark of Python Software Foundation.
- Other names may be trademarks of their respective owners

