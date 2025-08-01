---
title: Analyses de code en Python et utilisation du debugger
date: 2024 / 2025
---

## Récupération des exemples de code

Les exemples de code pour chaque partie sont à récupérer dans un dépôt git :

```
git clone https://git.sr.ht/~toma/python-unit
```

## Les outils d'analyse statique de code (Pylint)

_Les langages typés (et, dans une moindre mesure, les langages non typés) permettent de vérifier la cohérence du modèle créé depuis le code source afin de détecter des erreurs directement à la compilation et non à l'exécution (espaces mémoire non alloués, variables non instanciées, …)_

Python étant un langage fortement dynamique, les erreurs trouvées par le compilateur lui-même sont assez limitées, il est donc utile d'utiliser des outils annexes capables de trouver des patterns connus amenant à des erreurs à l'exécution. Attention : la nature dynamique du langage peut également retourner des faux négatifs durant l'analyse.

`Pylint` est un outil d'analyse statique du code source pour Python permettant de détecter des erreurs normalement détectées par les compilateurs de langages statiques (C, C++, …). Il vérifie également la bonne conformité du code source aux normes standardisées de développement en Python.

`Pylint` peut être installé depuis `pip` :

```sh
$ pip install pylint
```

`Pylint` peut ensuite être exécuté directement sur un fichier de code source :

```sh
$ pylint monFichier.py
```

### Intégration dans l'IDE

Utiliser `pylint` en ligne de commandes est très utile dans des environnements communs (intégration continue, ...). Mais pour un développeur, il est fastidieux de devoir naviguer entre la ligne de commandes et son IDE.

On préfère donc utiliser directement `pylint` via un plugin de son IDE.

### Personnalisation du linter

#### Fichier de configuration

`pylint` utilise un fichier de configuration standard pour respecter les normes universelles de Python - ce ne sont pas forcément les normes que l'on désire suivre dans son équipe. Il est donc possible de changer la configuration de `pylint` en créant un fichier de configuration :

- globalement pour l'utilisateur : `~/.pylintrc` ;
- pour le projet courant (à partager avec le reste de l'équipe) : `<workspace_dir>/pylintrc`.

Il est aussi possible de générer le fichier utilisé par défaut pour l'éditer par la suite :

```
pylint --generate-rc
```

Par exemple, pour changer l'indentation en utilisant des tabulations :

```ini
[FORMAT]
indent-string=\t
```

:::tip
Si besoin, il est aussi possible d'ignorer un problème pour une ligne uniquement. Par exemple, utiliser le mot-clé `global` est déconseillé en Python (problème `W0603`). Si l'on veut autoriser cet usage uniquement sur une ligne, il suffit d'ajouter un commentaire :

```python
global ma_variable # pylint: disable=W0603
```
:::

:::exo
1. Intégrer `pylint` dans son IDE via un plugin dédié.
2. Exécuter `pylint` sur les exemples de code fournis (répertoire `pylint`). Analyser les comptes rendus d'analyse (erreurs critiques, avertissements, _coding-style_ sans impact fonctionnel, ...) et essayer de corriger les exemples.
3. Exécuter `pylint` sur les classes principales de votre application. Corriger les erreurs critiques reportées.
4. Si besoin, ajouter un fichier de configuration de `pylint` dans le projet pour définir sa propre configuration.
:::

## Le débugger de Python (exécution pas à pas et analyse post-mortem)

> Un débugger est un logiciel qui aide un développeur à analyser les bugs d'un programme. Pour cela, il permet d'exécuter le programme pas à pas - c'est-à-dire le plus souvent ligne par ligne -, d'afficher la valeur des variables à tout moment et de mettre en place des points d'arrêt sur des conditions ou sur des lignes du programme. (Wikipédia)

### Quand utiliser un débugger ?

Dans la pratique, on utilise souvent un débugger :

- Dans les étapes initiales du développement, ou lors de l'apprentissage d'un nouveau langage / framework pour analyser le comportement interne du programme
- Pour vérifier des zones du code difficiles à tester de manière automatique (souvent à cause de problèmes d'architecture)
- Pour analyser un bug dans un programme en cours d'exécution, lorsque cela est possible

### Comment débugger un programme ?

Pour débugger une application, on exécute les étapes suivantes :

1. Reproduire le bug : trouver un cas de test qui fait échouer le code à chaque fois.
2. Diviser et conquérir : une fois le cas de test échouant découvert, isoler le code coupable :
	- Quel module.
	- Quelle fonction.
	- Quelle ligne de code.
3. Changer une seule chose à chaque fois et réexécuter le cas de test reproduisant le bug.
4. Utiliser le débogueur pour comprendre ce qui ne va pas.
5. Prendre des notes, être rigoureux dans l'approche, ... : le débug d'une application est long et difficile.

Le débogueur python `pdb` permet d'inspecter le code de façon interactive pour :

- Voir le code source
- Monter et descendre la pile d'appel
- Inspecter les valeurs des variables
- Modifier les valeurs des variables
- Poser des points d'arrêt (breakpoints) pour mettre en pause l'exécution du programme et inspecter / agir sur son comportement

### Comment utiliser pdb ?

Il existe de nombreuses méthodes pour lancer le débugger `pdb`. On notera notamment :

* L'exécution d'un fichier sous débugger (équivalent à mettre un breakpoint sur la 1ère ligne)

```sh
$ python -m pdb monFichier.py
```

* L'ajout d'une instruction d'arrêt dans le code source (voir fichier `ex1.py`, le fichier s'exécute alors jusqu'au breakpoint) :

```sh
import pdb; pdb.set_trace()
$ python ex1.py
```

* En cas de crash durant l'exécution du code sous débugger, pdb permet une analyse post-mortem.

Pdb passe alors dans un mode interactif permettant d'entrer des commandes de débuggage.

### Principales commandes du débugger

- `continue` : Continue l'exécution du code jusqu'au prochain breakpoint
- `l(list)` : Liste le code à la position courante
- `p <expression>` : Affiche la valeur de l'expression, par exemple `p maVariable`
- `u(p)` : Monte à la pile d'appel
- `d(own)` : Descend à la pile d'appel
- `n(ext)` : Exécute la prochaine ligne (ne va pas à l'intérieur d'une nouvelle fonction)
- `s(tep)` : Exécute la prochaine déclaration (va à l'intérieur d'une nouvelle fonction)
- `bt` : Affiche la pile d'appel
- `a` : Affiche les variables locales
- `retval` : Affiche le retour de la fonction
- `!command` : Exécute la commande Python donnée (par opposition à une commande pdb)
- `Help [commande pdb]` 
  + Sans argument: lister les commandes `pdb`
  + Avec argument : Obtenir de l'aide sur la commande fournie en paramètre

Attention : En cas de `segmentation fault`, `pdb` n'est pas utile puisque l'interpréteur `Python` crash avant qu'il ne puisse passer dans le débugger (idem en cas de code `C` embarqué dans `Python`). Dans ce cas, on utilise un autre débugger capable d'intercepter ces erreurs : le `GNU Debugger` (`gdb`).

Attention pour le débug de variables privées en Python : les noms de variables privées sont changées par l'interpréteur Python : https://stackoverflow.com/questions/27463943/private-variables-during-debugging(https://stackoverflow.com/questions/27463943/private-variables-during-debugging)

:::exo
Utiliser `pdb` pour interagir avec les exemples (répertoire pdb) :

1. Modifier la valeur des variables `firstVar` et `secondVar` dans le fichier `ex1.py`
2. Modifier l'expression result pour afficher `firstVar – secondVar`
3. Débugger le fichier `index_error.py` pour le corriger
4. Débugger le fichier `to_debug.py` :
	+ Installer les dépendances du code : `python -m pip install numpy scipy`
	+ Débugger le programme - le résultat attendu est de la forme suivante. Pensez notamment à vérifier que l'on itère bien pour chaque `optimizer` !

```
Benching 1D root-finder optimizers from scipy.optimize:
                brenth:   604678 total function calls
                brentq:   594454 total function calls
                ridder:   778394 total function calls
                bisect:  2148380 total function calls
```

Utiliser le débugger pour vérifier le fonctionnement des fonctionnalités principales du programme Wikigame : on vérifiera notamment la bonne valeur des variables critiques dans le code, et leur modification suite aux interactions de l'utilisateur. On pourra également utiliser le débugger pour tester le comportement du code suite à des valeurs invalides (en entrée d'API ou directement dans les variables internes du code).
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- "Python" is a registered trademark of the PSF. The Python logos (in several variants) are use trademarks of the PSF as well. ®
- Oracle and Java are registered trademarks of Oracle and/or its affiliates.

