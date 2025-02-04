---
title: Data mining - Mise en place de l'environnement
date: 2023 / 2024
---

# Création de l'environnement

## Pré-requis : Python

Nous allons utiliser le langage et des bibliothèques Python, il faut donc [commencer par installer][doc-install-win], si ce n'est déjà fait, Python sur le système.

Une version récente de Python est nécessaire.

## Virtualenv Python

Pour ne pas impacter le reste du système, il est recommandé d'installer les librairies de data mining dans un environnement indépendant du reste du système : c'est le principe des _virtual environments_.

Nous utiliserons donc un [venv](https://docs.python.org/fr/3/library/venv.html) dans ce TP.

```sh
$ python -m venv /path/to/new/virtual/environment
```

ou

```cmd
C:\>python -m venv C:\path\to\myenv
```

Cette commande crée une installation locale de Python dans le répertoire spécifié.

:::tip
Il faut ensuite, **dans chaque terminal ouvert par la suite**, activer cet environnement en sourçant la configuration (voir le [tableau ici](https://docs.python.org/fr/3/library/venv.html#how-venvs-work)).

Par exemple :

```bash
$ source /path/to/new/virtual/environment/bin/activate
```

ou

```cmd
C:\> C:\path\to\myenv\Scripts\activate.bat
```
:::

## Empaquetage et installation d'une bibliothèque Python

`pip` est un programme permettant d'installer une bibliothèque Python depuis le [Python Package Index][site-pypi] - nous utiliserons ce programme pour ajouter les librairies nécessaires à l'environnement de travail.

```sh
$ python -m pip install <librairie>
```

## Numpy

_Numpy_ est (de très loin) la librairie la plus utilisée pour manipuler des données (tableaux, matrices, ...) beaucoup plus facilement qu'en utilisant la librairie standard Python `stdlib`.

Ajouter dans l'environnement la librairie [numpy][numpy-official] :

```sh
$ python -m pip install numpy
```

:::tip
Par convention, on importe cette librairie en utilisant le nom `np` :

```python
import numpy as np
```

Dans la suite du cours, toute expression commençant par `np.` est un appel utilisant la librairie _numpy_.
:::

## Pandas

_Pandas_ est une librairie permettant de gérer des données à destination d'algorithmes de data mining :

```sh
$ python -m pip install pandas
```

:::tip
Par convention, on importe cette librairie en utilisant le nom `pd` :

```python
import pandas as pd
```

Dans la suite du cours, toute expression commençant par `pd.` est un appel utilisant la librairie _pandas_.
:::

## Matplotlib

_Matplotlib_ est une librairie permettant de tracer des courbes (et d'autres types de diagrammes statistiques) en _Python_.

Ajouter dans l'environnement la librairie [matplotlib][matplotlib-official] :

```sh
$ pip install matplotlib
```

:::tip
Par convention, on importe cette librairie (en réalité, l'objet `pyplot` de cette librairie qui nous intéresse pour tracer des courbes) sous le nom `plt` :

```python
import matplotlib.pyplot as plt
```

Dans la suite du cours, toute expression commençant par `plt.` est un appel à l'objet `pyplot` de la librairie _matplotlib_.
:::

## Scipy

_Scipy_ est la librairie de référence pour le traitement scientifique des données en Python.

Pour faire un raccourci :

- _Numpy_ contient la gestion du modèle de données (la classe `array`) ;
- _Scipy_ contient les algorithmes de _data science_ utilisant ce modèle de données.

Voir : [le site de Scipy][scipy-site] et la [documentation de référence][scipy-doc].

:::tip
Par convention, on importe cette librairie avec le nom `sp` :

```python
import scipy as sp
```

## Statsmodels

_Statsmodels_ est une librairie permettant de faire du calcul statistique (et de la régression linéaire) :

```sh
python -m pip install statsmodels
```

:::tip
Par convention, on importe cette librairie avec le nom `sm` :

```python
import statsmodels.api as sm
```
:::

## Scikit-learn

_Scikit-learn_ est une librairie très utilisée en machine learning.

```sh
python -m pip install scikit-learn
```

:::tip
Par convention, on importe cette librairie avec le nom `sklearn` :

```python
import scikit-learn as sklearn
```
:::

## IDE

Python est un langage interprété qui peut être exécuté directement dans le shell `python`. Si cette solution n'est pas optimale en programmation informatique, elle peut être très utile en _data science_ pour tester rapidement l'exécution d'un algorithme.

Pour une utilisation plus poussée, il est recommandé d'utiliser un environnement de développement :

- Directement dans un IDE : [Visual Studio Code][vscode-python], [PyCharm][pycharm-python], ...
- En utilisant un système mélangeant exécution de code / gestion de rapports : [jupyter notebooks][jupyter-site].

---

# Liens

- [Développement Python sous Visual Studio Code][vscode-python]
- [Développement Python sous PyCharm][pycharm-python]
- [Les notebooks Jupyter][jupyter-site]
- [Documentation sur les venv][doc-venv].
- [Venv][doc-venv]
- [Le site Pypi][site-pypi]
- [Installer Python sous Windows][doc-install-win]
- [Bibliotheque standard][doc-stdlib]
- [Documentation complète][doc-full]
- [Reference du langage Python][doc-ref]
- [Les séquences][doc-seq]
- [Cours sur les slices][zds-slices]
- [Cours Python orienté data science][scipy]
- [La bibliothèque NumPy et création de graphiques Matplotlib][numpy-matplotlib]
- [Documentation Scikit-learn][sklearn-doc]

[doc-install-win]: https://docs.python.org/fr/3/using/windows.html
[doc-ref]: https://docs.python.org/fr/3/reference/index.html#reference-index
[doc-seq]: https://docs.python.org/fr/3/library/stdtypes.html#typesseq
[doc-stdlib]: https://docs.python.org/fr/3/tutorial/stdlib.html
[doc-full]: https://docs.python.org/fr/3/library/index.html#library-index
[doc-venv]: https://docs.python.org/3/tutorial/venv.html
[zds-slices]: https://zestedesavoir.com/tutoriels/582/les-slices-en-python/
[site-pypi]: https://pypi.org 
[scipy]: https://scipy-lectures.org/
[numpy-official]: https://numpy.org/
[matplotlib-official]: https://matplotlib.org/
[numpy-matplotlib]: https://zestedesavoir.com/tutoriels/4139/les-bases-de-numpy-et-matplotlib/
[vscode-python]: https://code.visualstudio.com/docs/languages/python
[pycharm-python]: https://www.jetbrains.com/pycharm
[jupyter-site]: https://docs.jupyter.org/en/latest/index.html
[scipy-site]: http://www.scipy.org/
[scipy-doc]: http://docs.scipy.org/doc/scipy/reference/
[sklearn-doc]: https://scikit-learn.org/stable/

---

# Legal

- "Python" is a registered trademark of the PSF. The Python logos (in several variants) are use trademarks of the PSF as well.
- PYPI is a trademark of Python Software Foundation.

<!-- vscode pycharm jupyter matplotlib numpy scikit sklearn -->
