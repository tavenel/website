---
title: Tests automatisés et analyses de code en Python
date: 2024 / 2025
---

## Récupération des exemples de code

Les exemples de code sont à récupérer dans un dépôt git :

```
git clone https://git.sr.ht/~toma/python-unit
```

## Les modules de tests unitaires Python (Unittest, ...)

_Les tests unitaires permettent de vérifier le bon fonctionnement de parties isolées du code, au plus proche de l'implémentation. Ceux-ci peuvent être réalisés manuellement (au débugger) mais leur facilité d'écriture permet de souvent les automatiser._

Dans sa forme la plus simple, un test unitaire peut être une simple assertion du bon fonctionnement ajoutée au sein même du programme, afin d'arrêter son exécution si la cohérence du code est remise en cause :

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

Si elles sont très pratiques, ces assertions nécessitent l'exécution du code de production et peuvent être difficiles à exploiter : on leur préfère donc l'usage d'un framework de test dédié (pour exécuter du code de test en dehors du code de production).

On utilisera dans ce cas pratique Unittest, un framework de test unitaire populaire pour Python et très similaires aux frameworks classiques de tests unitaires (`Junit` et tous les `*unit`) :

- Chaque test se focalise sur une vérification dédiée, isole une partie très limitée du code (fonction seule ou classe), et est **indépendant**
- Utilisation de méthodes `setUp()` et `tearDown()` dans les tests pour :
	+ Mettre en place l'environnement avant le test : `setUp()`
	+ Nettoyer l'environnement après le test : `tearDown()`
- Un test est une classe qui hérite de `unittest.TestCase(https://docs.python.org/3/library/unittest.html#unittest.TestCase)`
- La classe `TestCase` fournit des méthodes `assert` permettant d'exécuter les vérifications nécessaires et de générer les rapports de test

Des exemples de tests sont fournis dans le répertoire unittest.

Pour exécuter les tests unitaires, on pourra :

- Exécuter la classe / méthode de test directement en utilisant unittest :

```sh
$ python -m unittest exemple1.MyTest.test
```

- Exécuter tous les tests du fichier de test fourni :

```sh
$ python -m unittest exemple1.py
```

- Ajouter l'exécution des tests directement dans le main du fichier de tests :

```sh
$ python exemple2.py
```

- Utiliser le mode de découverte pour scanner et exécuter automatiquement les tests :

```sh
$ python -m unittest discover répertoire_projet “exemple*.py”
```


:::exo
- Exécuter les tests fournis en exemple (répertoire `unittest`) et vérifier leur bonne exécution
- En s'inspirant des exemples fournis, ajouter un ensemble de tests unitaires permettant de vérifier le bon fonctionnement des classes et fonctions du programme.

On essaiera de suivre un patron _Arrange Act Assert_ (voir cours) pour l'écriture du code de test.
:::

## La couverture de code des tests

_Les tests unitaires sont un garde-fou très utile pour vérifier le bon fonctionnement des implémentations. Leur facilité d'écriture implique rapidement l'existence d'une grande batterie de tests. Comment avoir alors une vision globale de la qualité sur le produit, et comment trouver les portions non testées du code ?_

On utilise pour cela un outil de couverture de tests : cet outil va scanner les lignes de code de production exécutées lorsque les tests tournent, pour détecter quelles classes / fonctions ont été testées, et lesquelles n'ont pas été testées.

On utilisera pour cela l'outil `coverage`. Son usage est très simple :

- Exécution des tests sous surveillance : remplacer l'exécution des tests depuis la commande `python` par la commande `coverage run`. Par exemple :

```sh
$ python -m unittest exemple1.py
```

Devient

```sh
$ coverage run -m unittest exemple1.py
```

- Génération des rapports : une fois les tests exécutés sous surveillance, on génère les rapports d'exécution :

```sh
$ coverage report
```

Note : La commande suivante permet de générer un rapport HTML, bien plus utile puisqu'il permet de lire facilement les lignes de code non couvertes :

```sh
$ coverage html
```

:::exo
Tester la couverture des tests réalisés à l'étape précédente. Améliorer cette couverture en ajoutant des tests vérifiant les parties importantes de l'application n'ayant pas encore de test.
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- "Python" is a registered trademark of the PSF. The Python logos (in several variants) are use trademarks of the PSF as well. ®
- Oracle and Java are registered trademarks of Oracle and/or its affiliates.
