---
marp: true
paginate: true
#footer: _© 2024 Tom Avenel under 󰵫  BY-SA 4.0_
title: Tkinter
keywords:
- python
---

<!-- _backgroundColor: "#000" -->
<!-- _color: "red" -->

# Programmation des interfaces graphiques : Tkinter

_Tom Avenel_

<https://www.avenel.pro/>

---

<!-- Section --> 
<style scoped>
section { background: teal; }
h1 { color: white; }
</style>
# <!-- fit --> Programmation des interfaces graphiques
# La bibliothèque Tkinter

---

# Tcl

`Tcl` est un langage de programmation interprété dynamiquement (comme `Python`).

Il est généralement utilisé comme langage de script pour `Tk` et embarqué dans des applications écrites en `C`.

---

# Tk

`Tk` est un package de `Tcl` écrit en `C` permettant de manipuler des widgets d'interface graphique (GUI).

Il utilise les librairies graphiques disponibles sur le système d'exploitation et permet de s'abstraire de celles-ci.

---

# Ttk

`Themed Tk` (`Ttk`) est très similaire à `Tk` mais propose des widgets plus 'modernes' et utilise le style global du système d'exploitation pour une expérience utilisateur cohérente.

Lorsqu'elle est disponible, on préfèrera utiliser `Ttk` plutôt que `Tk`.

---

# Tkinter

`Tkinter` est une abstraction de `Tcl/Tk` pour `Python`.

En utilisant des objets Python, `Tkinter` crée des commandes `Tcl/Tk` permettant de modifier l'interface graphique.

`Tkinter` permet également de lier les modèles de threading de `Tcl/Tk` et de `Python` (attention donc lors de l'utilisation de threads `Python`).

On veillera notamment à utiliser une instance unique de `Tk`.

---

# Principaux conteneurs

```python
class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
```

La classe `Tk` est instanciée sans argument.

Cela crée un widget de haut niveau de `Tk` qui est généralement la fenêtre principale d'une application.

Chaque instance a son propre interpréteur `Tcl` associé.

---

```python
from tkinter import Tk

root = Tk() # Initialise Tk et retourne l'interpréteur Tcl (ici stocké dans la variable 'root').
```

---

# Concepts de Tk

Une interface graphique `Tkinter` est composée de widgets indépendants représentés par des objets Python.

Ces widgets sont créés par des classes telles `ttk.Frame` `ttk.Label` et `ttk.Button`.

---

Les widgets possèdent une hiérarchie, par exemple les instances de widgets `Label` et `Button` sont des fils du widget `Frame`, lui-même fils du widget `root`.

Lors de la création d'un widget, le parent est passé comme 1er argument du constructeur.

---

Les widgets ne sont pas placés automatiquement dans l'interface utilisateur.
Le positionnement est délégué à des gestionnaires de géométrie tel l'objet `Grid`.

---

`Tkinter` peut modifier l'affichage dynamiquement et réagir aux interactions de l'utilisateur.
Pour cela, il est nécessaire d'utiliser des boucles d'événements (event loop), sinon l'affichage restera inchangé.

---

# Principaux widgets et composants

> Voir liens `Tkinter` dans la section Documentation

---

# Exemple : Hello World

---

# **Gestion des événements**

---

# Command binding

## Binding de fonction sans argument : référence de fonction

```python
def button_clicked():
    print('Button clicked')

ttk.Button(root, text='Click Me',command=button_clicked)
```

---

## Binding de fonction avec argument : utilisation de lambda

```python
def button_clicked(arg):
    print('Button clicked with param : ', arg)

ttk.Button(root, text='Pierre',command=lambda: button_clicked('Rock'))
```

---

# Event binding

Le binding de commande est simple mais très limité : on préfèrera la plupart du temps utiliser un binding d'événements :

```python
widget.bind(event, handler, add=None)
```

- `event` est l'événement auquel réagir dans le widget
- `handler` est la méthode à appeler lorsque l'événement est déclenché
- Si `add` vaut `+` il est possible d'ajouter plusieurs `handler` sur le même événement

---

Il est aussi possible de lier un événement à la fenêtre entière :

```python
root.bind(event, handler)
```

Un binding se défait par l'appel :

```python
widget.unbind(event)
```

Liste des events : [tkinter event binding][doc-tkinter-event-binding].

Pour plus d'informations, voir le [cours zestedesavoir.com sur la programmation par événements en Tkinter][zds-tkinter-events].

---

# Exemples

- binding simple
- binding avec paramètres
- binding multiple
- widgets basiques
- Ttk - utilisation de themes

---

# Applications multifenêtres
> Voir liens Tkinter dans la section Documentation

---

# Pattern MVC

Tkinter supporte le [pattern MVC][doc-tkinter-mvc]

Voir le [cours sur le pattern MVC][site-perso].

---

<!-- class: liens -->

# Liens utiles - Tkinter

- [Documentation et tutoriels Tkinter][doc-tkinter]
- [Documentation pattern MVC dans Tkinter][doc-tkinter-mvc]
- [Event binding dans Tkinter][doc-tkinter-event-binding]
- [Cours de programmation événementielle en Tkinter][zds-tkinter-events]
- [Tutoriel pas-à-pas pour apprendre Tkinter](https://www.tutorialspoint.com/python/python_gui_programming.htm)

[doc-tkinter]: https://www.pythontutorial.net/tkinter/
[doc-tkinter-mvc]: https://www.pythontutorial.net/tkinter/tkinter-mvc/
[doc-tkinter-event-binding]: https://www.pythontutorial.net/tkinter/tkinter-event-binding/
[zds-tkinter-events]: https://zestedesavoir.com/tutoriels/1729/programmation-avec-tkinter/
---

<!-- class: legal -->

# Legal

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
