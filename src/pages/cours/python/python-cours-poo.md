---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Le langage Python
keywords:
- python
---

<!-- _backgroundColor: "#000" -->
<!-- _color: "red" -->

![bg left:40% 80%][python-logo]

# Le langage Python®

_Tom Avenel_

<https://www.avenel.pro/>

---

<!-- Section -->
<style scoped>
section { background: darkmagenta; }
h1 { color: white; }
</style>
# <!-- fit --> Programmation orientée objet

---

# Classes

Une déclaration de classe est un morceau de code standard et est **exécutée**.
- La déclaration de classe peut être faite n'importe où
- Le code dans la classe peut être n'importe quoi (fonctions, code exécuté, ...)

Un _objet classe_ est créé lors de la lecture de la déclaration de classe.

---

# Exemple de classe simple

```python
class MaClasse:
    # code local à la classe (et à toutes ses instances)

    # Attribut 'données' de la classe partagé avec toutes ses instances
    mon_identifiant_commun = 12

    # Attribut 'Méthode' de la classe
    def ma_methode(self): # Une fonction dans une classe reçoit l'instance de la classe en 1er paramètre
        print('Utilisation de la classe :', self)
```

---

# Instanciation de classe sans constructeur

```python
class MaClasse:
    pass

mon_instance1 = MaClasse()
mon_instance2 = MaClasse()

print( type(mon_instance1) )
print( mon_instance1 == mon_instance2 )
```

---

```python
class MaClasse:
    # Attribut 'données' de la classe partagé avec toutes ses instances
    mon_identifiant_commun = 12

mon_instance1 = MaClasse()
mon_instance2 = MaClasse()

print( MaClasse.mon_identifiant_commun ) #12
print( mon_instance1.mon_identifiant_commun ) #12
print( mon_instance2.mon_identifiant_commun ) #12
```

---

```python
class MaClasse:

    # Attribut 'Méthode' de la classe
    def ma_methode(self): # Une fonction dans une classe reçoit l'instance de la classe en 1er paramètre
        print('Utilisation de la classe :', self)

mon_instance1 = MaClasse()
mon_instance2 = MaClasse()

mon_instance1.ma_methode()
mon_instance2.ma_methode()
```

---

# Utilisation de constructeur

```python
class MaClasseAvecConstructeur:
    # Le constructeur est une méthode spéciale nommée __init__()
    def __init__(self, valeur_initiale):
        """
        Valeur stockée dans self : propre à chaque instance.
        mon_attribut_de_classe est différent pour chaque instance
        """
        self.mon_attribut_de_classe = valeur_initiale 
    
    def afficher(self):
        print('Valeur stockee : ', self.mon_attribut_de_classe)

mon_instance = MaClasseAvecConstructeur(2)
mon_instance.afficher()

print( mon_instance.mon_attribut_de_classe )
```

---

# Instanciation de classe avec constructeur

```python
class MaClasseAvecConstructeur:
    def __init__(self, valeur_initiale):
        self.mon_attribut_de_classe = valeur_initiale 
    
    def afficher(self):
        print('Valeur stockee : ', self.mon_attribut_de_classe)

mon_instance1 = MaClasseAvecConstructeur(21)
mon_instance2 = MaClasseAvecConstructeur(22)
mon_instance1.afficher() # 21
mon_instance2.afficher() # 22
MaClasseAvecConstructeur.afficher(mon_instance1) # 21
print( mon_instance1.__class__ ) # MaClasseAvecConstructeur
```

---

<!-- _class: small -->

# Héritage de classe

```python
class MaClasseParente:
    pass

class MaClasseDerivee(MaClasseParente):
    """
    MaClasseDerivee est utilisée en priorité,
    si l'attribut n'existe pas il sera recherché dans
    MaClasseParente
    """
    def verif_heritage(self):
        print('Instance de MaClasseDerivee ?', isinstance(self, MaClasseDerivee))
        print('Instance de MaClasseParente ?', isinstance(self, MaClasseParente)) # True !!
        # self est une instance de MaClasseDerivee mais aussi de toutes ses classes parentes
        print('Hérite de MaClasseParente ?', issubclass(MaClasseDerivee, MaClasseParente))

mon_instance = MaClasseDerivee()
mon_instance.verif_heritage() # True True True
```

---

# Héritage multiple

```python
class MonHeritageMultiple(ClasseParente1, ClasseParente2, ClasseParente3):
    # code de classe
```

---

# Variables privées
En Python, il est toujours possible d'accéder/modifier un attribut de l'héritage (pas de vérouillage ou de masquage d'attributs 'privés').

---

```python
class A:

    def _spam(self): # Par convention, cette classe est privée et ne **devrait** pas être appelée publiquement
        pass

    def __fonction_locale(self):
        """
        Préfixe double '__' :
        modifie self.__fonction_locale()
        en
        A.__fonction_locale(self)
        """

        self.i = 1

```

---

<!-- _class: small -->

```python
class A:
    def __fonction_locale(self): # Modifie self.__fonction_locale() en A.__fonction_locale(self)
        self.i = 1

    def fonction_publique(self):
        self.x = 1

    def affiche1(self):
        self.__fonction_locale()
        print(self.i)

    def affiche2(self):
        self.fonction_publique()
        print(self.x)

class B(A):
    def __fonction_locale(self):
        self.i = 2

    def fonction_publique(self):
        self.x = 2

o = B()
o.affiche1()
o.affiche2()
```

---

```python
>>> o.affiche1()
1
```

- `self.affiche1()` : (`self` <= `B`)
  - cherche `B.affiche1()` : X
  - cherche `A.affiche1()` : OK
    `self.__fonction_locale()` :
      - remplacé par `A.__fonction_locale()`
      - cherche `A.__fonction_locale()` : OK => i=1

---

```python
>>> o.affiche2()
2
```
- `self.affiche2()` : (`self` <= `B`)
  - cherche `B.affiche2()` : X
  - cherche `A.affiche2()` : OK
    `self.fonction_publique()` :
      - cherche `B.fonction_publique()` : OK => `x=2`

---

# Destructeurs

```python
del mon_objet
```

---

# Accès à la classe parente

```python
class A:
    def f(self):
        print('A')

class B(A):
    def f(self):
        print('B')
    def g(self):
        super().f()

a = A()
a.f() # A

b = B()
b.f() # B
b.g() # A
```

---

# Dataclasses

Permettent de créer rapidement une classe servant juste à transporter de la donnée :

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
print( john.dept ) # 'computer lab'
print( john.salary ) # 1000
```

---

# **Interfaces**

En Python, les interfaces ne sont pas directement implémentées par le langage.
Il est cependant possible d'utiliser les concepts d'une interface pour s'en approcher.

---

<!-- _class: small -->

# Interface informelle (Duck Typing)

Classe standard décrivant le contrat d'une interface (aucune vérification).

Toutes les implémentations sont vides (`pass`).

```python
class Animal:
    def espece(self) -> str:
        '''L'espèce de l'animal'''
        pass
    def cri(self) -> str:
        '''Le cri d'un animal'''
        pass

class Chien(Animal):
    def espece(self):
        return 'Canidées'

    def cri(self):
        return 'Wouah !'

c = Chien()
print( c.espece() )
print( c.cri() )
```

---

On peut également utiliser l'exception `NotImplementedError` plutôt que l'instruction `pass` : cela permet d'avoir une erreur si l'on a oublié de redéfinir la fonction.

Voir la suite du cours sur les exceptions.

```python
def ma_fonction_abstraite():
    raise NotImplementedError("Fonction à implémenter dans l'héritage !")
```

---

```python
class Animal:
    def cri(self) -> str:
        '''Le cri d'un animal'''
        raise NotImplementedError("Fonction à implémenter dans l'héritage !")

class Chien(Animal):
    pass

c = Chien()
print( c.cri() ) # NotImplementedError(...)
```

---

# Python ABC

Il existe d'autres méthodes plus complexes pour implémenter des interfaces plus formellement :
- l'utilisation de classes abstraites via la librairie _Abstract Base Class (ABC)_
- le module `zope.interface` de la librairie _Zope Component Architecture_ qui permet de marquer des implémentations héritant d'interfaces.

---

# Exercice : héritage multiple

- Écrire une classe `Mouette` héritant de deux classes parentes : une classe `Oiseau` et une classe `Vol`.
- La classe `Oiseau` possède une fonction booléenne `ovipare`. La classe `Vol` implémente la fonction `deplacement` d'une interface `Locomotion` en renvoyant : `deplacement() => "vol"`
- Instancier un objet `m` de type `Mouette`. Cette objet doit répondre au contrat suivant :
  + `m.deplacement() => "vol"`
  + `m.ovipare() => True`

---

# Attributs et méthodes statiques

- Le prototype d'une classe (`class MaClasse ...`) est un objet.
- Tout le code dans la classe est exécuté à la lecture du mot-clef `class`.
- Permet de gérer du code statique.
- Rappel : le 1er argument `self` est utilisé pour éviter ce comportement statique : `mon_instance.ma_methode()` appelle en réalité `MaClasse.ma_methode(on_instance)`.

---

## Exemple d'attribut statique

```python
class MaClasse:

    # nb_instances appartient à MaClasse et non à mon_instance
    nb_instances = 0

    def __init__(self, name):
        MaClasse.nb_instances += 1 # appartient à MaClasse
        self.name = name # appartient à mon_instance

mon_instance = MaClasse('un nom')
print( mon_instance.name )
print( MaClasse.nb_instances )
```

---

## Exemple de méthode statique

On pourra utiliser le décorateur `@staticmethod` :

```python
class MaClasse():

  nb_instances = 1

  @staticmethod
  def reset_instances():
      MaClasse.nb_instances = 0

mon_instance = MaClasse()
print(MaClasse.nb_instances) # 1
MaClasse.reset_instances()
print(MaClasse.nb_instances) # 0
```

---

# À retenir sur l'héritage

- `class MonImplem(MonParent)` fais hériter `MonImplem` de `MonParent`.
- Utiliser `self` dans toutes les méthodes (y compris le constructeur).
- Sans `self` les attributs / méthodes directement dans la classe sont statiques (partagés avec toutes les instances).
- `super().__init__(...)` permet d’appeler le constructeur de la classe parente.
- Les classes filles disposent des méthodes de la classe mère mais peuvent les _surcharger_ (redéfinir ces méthodes).
- `super().une_methode(...)` permet d’appeler `une_methode` telle que définie dans la classe mère.
- `dir(mon_instance)` ou `mon_instance.__dict__` : liste tous les attributs / methodes d’un objet (ou module).

---

# Exceptions

[Liste des exceptions natives][doc-exceptions]

## Lever une exception

```python
raise RuntimeError('Une erreur ici')
```
On préfèrera utiliser une classe spécifique d'exception : `ValueError`, `OSError`, … ou une classe d'exception créée dans l'application.

---

## Récupération d'exceptions

```python
try:
    x = int(input("Please enter a number: "))
    break
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
except (RuntimeError, TypeError, NameError) as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise # Propage l'exception pour ne pas la masquer à l'appelant
except Exception as exc:
    raise MonException('Mon exception imbriquée') from exc
```

---

<!-- _class: small -->

# try/finally

Un bloc `try/finally` permet d'exécuter un bloc de code `finally` dans tous les cas (exception ou comportement normal).

```python
try:
    # Cas 1
    i = 2 / 0
    # OU : Cas 2
    i = 2 / 2

    print('Resultat : ', i)
except ZeroDivisionError:
    print("Erreur !")
finally:
    print("Ce code est toujours appelé")
```

---

<!-- class: liens -->

# Liens utiles - notions avancées

- [Cours Python orienté data science][scipy]
- [La bibliothèque NumPy et création de graphiques Matplotlib][numpy-matplotlib]
- [Concurrence et asynchronisme en Python][async]
- [Les décorateurs][decorator]

---

# Liens utiles - exercices

- [Visualisation graphique d'exécution de code][python-tutor]
- [Python Challenges][python-challenge]

[python-logo]: https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg
[doc-install-win]: https://docs.python.org/fr/3/using/windows.html
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

<!-- class: legal -->

# Legal

- "Python" is a registered trademark of the PSF. The Python logos (in several variants) are use trademarks of the PSF as well.
- PYPI is a trademark of Python Software Foundation.
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
