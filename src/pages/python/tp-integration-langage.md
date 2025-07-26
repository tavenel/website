---
title: Intégration et modification du langage Python
correction: false
---

## Présentation

En Python, tout est objet : écrire `x = 2` est un raccourci pour générer une instance d'un entier `x = int(2)`.

L'addition de 2 entiers est donc un appel de méthode entre deux instances de la classe `int`.

Pour réaliser une addition, Python utilise en fait la méthode `__add__()` de la classe `int`.

Lorsque l'on tape `2 + 3` dans le shell, quelle est réellement l'opération réalisée en utilisant les instances de la classe `int` ?

  + Vérifier que ces deux écritures font similaires en testant leur égalité.
  + Rappel : en Python, `mon_instance.ma_methode()` est un raccourci pour appeler `MaClasse.ma_methode(mon_instance)` si `mon_instance` est une instance de `MaClasse`.

:::correction
```python
# 2 + 3 réalise une opération `__add__()`
# sur les instances `int(2)` et `int(3)` donc :
# print( 2+3 )
# print( int.__add__(2,3) )
# print( 2+3 == int.__add__(2,3) )
```
:::

## Utiliser le Python Object Model : addition de types personnalisés

Soit une classe `Point` modélisant un point à 3 dimensions :

```python
class Point:

    def __init__(self, x, y, z):
	
        self.x = x
        self.y = y
        self.z = z
```

- En reprenant l'exemple précédent, proposer une implémentation de la méthode `__add__(self, autre_instance)` pour la classe Point.
- Utiliser cette implémentation pour réaliser élégamment l'addition de deux instances `Point(1,2,3)` et `Point(-1,2,0)`.

### Égalité

- Tester l'égalité : `Point(1,2,3) == Point(1,2,3)`. Pourquoi ce résultat ?
- De manière similaire, implémenter la méthode `__eq__(self, autre_instance)` qui retourne `True` si et seulement si deux instances sont égales.
- Vérifier que `Point(1,2,3) == Point(1,2,3)`.

:::correction
```python
class Point:

    def __init__(self, x, y, z):
	
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):

        return f'Point[{self.x},{self.y},{self.z}]'

    def __str__(self):

        return f'[{self.x},{self.y},{self.z}]'

    def __add__(self, other):

        return Point(
                self.x + other.x,
                self.y + other.y,
                self.z + other.z,
                )

    def __eq__(self, other):

        return isinstance(other, Point) \
                and self.x == other.x \
                and self.y == other.y \
                and self.z == other.z

if __name__ == '__main__':

    # POINTS
    p1 = Point(1,2,3)
    p2 = Point(-1,2,0)

    # Test de __str__() et __repr__()
    print("Le point p1", p1)
    print("Le point p2", p2)

    print(f"Addition de P1: {p1} avec P2: {p2} = {p1 + p2}")

    # Point(1,2,3) != Point(1,2,3) sans __eq__()
    # car on teste les pointeurs des objets et pas les contenus.
    print("Test égalité : Point(1,2,3) =? Point(1,2,3)", \
      {Point(1,2,3) == Point(1,2,3)})

    # Le test `isinstance()` dans la méthode `__eq__()`
    # permet de vérifier l'égalité suivante :
    print( "Point(1,2,3) =? 4", \
      Point(1,2,3) == 4 )
```
:::

## Collection personnalisée

Python propose des méthodes permettant de gérer facilement des classes de collections d'éléments.

Soit la classe `CollectionDePoints` suivante :

```python
class CollectionDePoints:

	def __init__(self, collection):

        self.mes_points = list(collection)
```

Créer une instance `ma_collection` de cette classe stockant 10 instances de `Point`.

### Insérer / récupérer des éléments

Les méthodes `__getitem__(self, indice)` et `__setitem(self, indice, item)__` permettent de récupérer / insérer un élément à un indice donné dans la collection.

- Ajouter des implémentations pour la classe `CollectionDePoints`.
- Vérifier l'ajout des points en utilisant : `ma_collection[1] = ...`
- Récupérer une sous-collection de points des indices `2` (inclus) à `4` (exclus).

### Itérations

- Une classe est itérable si elle possède une fonction `__iter__()` qui renvoit un itérateur.
- Un itérateur est un objet qui possède :
  + une méthode `__next__(self)` qui renvoie l'élément suivant en cours d'itération.
  + une méthode `__iter__(self)` qui renvoie un objet itérateur avec lequel continuer l'itération (souvent un simple `return self`).
  + `raise` une exception `StopIteration` lorsqu'il n'y a plus d'élément à itérer.
- Rendre la classe `CollectionDePoints` itérable
- Itérer sur les 10 points de la classe en utilisant une boucle `for` et afficher chaque point atteint.
  + Pour afficher les instances de `Point`, on pourra utiliser `__repr__(self)` et `__str__(self)` qui retournent un objet `str` pour l'affichage (la 1ere méthode donne une représentation interne pour les logs, la seconde sert à un affichage "propre").

:::correction
```
class CollectionDePoints:
    '''
    Implémentation directe de la solution.
    '''

    def __init__(self, collection):

        self.mes_points = list(collection)

    def __repr__(self):

        return f'CollectionDePoints({self.mes_points})'

    def __str__(self):

        return f'{self.mes_points}'

    def __getitem__(self, i):

        return self.mes_points[i]

    def __setitem__(self, i, value):

        self.mes_points[i] = value

    def __iter__(self):

        self.iter = 0
        return self

    def __next__(self):

        if self.iter == len(self.mes_points):
            raise StopIteration

        elt = self.mes_points[self.iter]
        self.iter += 1
        return elt
```
:::

:::correction
```python
class CollectionDePointsDelegate:
    '''
    Implémentation utilisant un pattern de délégation vers la liste
    '''

    def __init__(self, collection):

        self.mes_points = list(collection)

    def __repr__(self):
        return self.mes_points.__repr__()

    def __str__(self):
        return self.mes_points.__str__()

    def __getitem__(self, i):
        return self.mes_points.__getitem__(i)

    def __setitem__(self, i, value):
        return self.mes_points.__setitem__(i, value)

    def __iter__(self):
        return self.mes_points.__iter__()
```
:::

:::correction
```python
if __name__ == '__main__':
    # COLLECTIONS
    l = [ Point(i, 2*i, 3*i) for i in range(0,10) ]
    ma_collection = CollectionDePoints( l )
    print(ma_collection)

    ma_collection[1] = Point(1,2,3)
    print(f'ma_collection[1] : {ma_collection[1]}')
    print(f'ma_collection[2::4] : {ma_collection[2::4]}')

    print('Iteration')
    for p in ma_collection:
        print(p)

    m2 = CollectionDePointsDelegate(l)
    print(m2)
    m2[1] = Point(1,2,3)
    print(f'm2[1] : {m2[1]}')
    print(f'm2[2::4] : {m2[2::4]}')
    for p in m2:
        print(p)
```
:::

## Classe descripteur : getter et setter personnalisés

Python permet de redéfinir les concepts de `__getter__()` et `__setter__()`. Ce sont en fait ces méthodes qui sont appelées pour récupérer des attributs et leur assigner une valeur :

```python
print(instance.mon_attribut) # utilise __getter__()
instance.mon_attribut = 3 # utilise __setter__()
```

Cette redirection est très pratique pour écrire des classes descripteurs : ces classes permettent de sortir de la logique de code et de la donnée d'une classe conteneur mais de simuler un usage direct de cette classe conteneur.

Nous allons utiliser ce comportement pour sortir une opération de transformation de donnée `Fahrenheit` en `Celsius` d'une classe Température.

- Écrire une classe conteneur `Temperature`. Cette classe contiendra :
  + Un attribut `fahrenheit` initialisé dans le constructeur.
  + Une **variable statique de classe** `celsius = Celsius()` (pas de `self`). Une variable statique s'écrit directement dans le code de la classe et non dans le constructeur (une bonne pratique est de l'écrire juste après la ligne décrivant le nom de la classe). Cette variable sera associée au prototype de la classe elle-même et non aux instances de la classe.
- Écrire une classe descripteur vide `Celsius`.
- Ajouter à la classe `Celsius` une méthode `__get__(self, instance, owner)` :
  + `self` est la référence vers l'instance de `Celsius` : nous n'utiliserons pas cette classe directement.
  + `instance` est la référence vers l'instance du conteneur appelant (instance de `Temperature`) : c'est cette instance qui nous intéressera pour récupérer l'attribut `fahrenheit`.
  + `owner` est la référence vers la classe `Temperature` elle-même : nous ne l'utiliserons pas dans cet exemple.
  + Ajouter une trace à l'aide d'un `print` affichant les paramètres de cette méthode pour bien comprendre son appel.
  + Retourner la conversion en degrés Celsius depuis la formule : `5 * (fahrenheit - 32) / 9`.
- Ajouter à la classe `Celsius` une méthode `__set__(self, instance, value)` :
  + Même commentaire pour les paramètres `self` et `instance`.
  + `value` contient la valeur à assiger.
  + Ajouter une trace à l'aide d'un `print` affichant les paramètres de cette méthode pour bien comprendre son appel.
  + Implémenter cette méthode pour assigner à l'attribut `fahrenheit` de `Temperature` la bonne valeur depuis une `value` en Celsius.
- Testons notre classe descripteur avec le code suivant :

```python
t = Temperature(212)
print(t.celsius)
t.celsius = 0
print(t.fahrenheit)
```

:::correction
### Correction - Classe descripteur : getter et setter personnalisés

```python
class Celsius:

    def __get__(self, instance, owner):
        print(f"Getter de celsius pour l'instance: {instance} et owner: {owner}")
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        print(f"Setter de celsius pour l'instance: {instance}")
        instance.fahrenheit = 32 + 9 * value / 5


class Temperature:

    celsius = Celsius()

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

if __name__ == '__main__':

    t = Temperature(212)
    print(t.celsius)
    t.celsius = 0
    print(t.fahrenheit)
```
:::

