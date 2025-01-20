---
title: Exercices Python
author: Tom Avenel
depends: test/data/mots.txt
correction: false
---

## Jeu du plus ou moins

Tirer un nombre au hasard entre 1 et 100. L'utilisateur doit trouver ce nombre et pour cela proposer des valeurs - le programme indique à chaque réponse de l'utilisateur si le nombre est supérieur ou inférieur à celui entré.
Au bout de 5 essais, si le nombre n'a pas été trouvé le programme indique entre quelles dizaines chercher (par exemple : entre 30 et 40 pour 42).

## (Dé)sérialisation simple d'objets Python

Soit une classe Point possédant 3 attributs `x`,`y`,`z`.

1. Écrire l'implémentation de cette classe en Python.
2. Définir une liste d'instances de points : `[(1,2,0);(2,4,8);(0,1,0)]`
3. Sérialiser et stocker cette liste dans un fichier `JSON`
4. Dans un shell Python, désérialiser ce fichier `JSON` dans une variable.
5. Afficher le résultat de l'addition des points en utilisant la variable précédente.

## Exercice : Recherche dans une liste

### Lecture de fichier

Télécharger le fichier `mots.txt` qui contient un mot par ligne.

1. Lire ce fichier et construire une liste avec tous les mots du fichier
2. Écrire une fonction qui vérifie que la liste de mots est triée par ordre alphabétique
3. Écrire une fonction qui recherche un mot dans la liste et donne sa position (index dans la liste ou -1 s'il n'y est pas). Cette fonction prend en paramètre une liste et un mot et retourne un entier.
4. Quelle est la position des mots "UN" et "DEUX" ?

### Recherche dichotomique

Lorsqu'une liste est triée, rechercher un élément est beaucoup plus rapide. Si on cherche le mot X dans la liste, il suffit de le comparer au mot du milieu pour savoir si ce mot est situé dans la partie inférieur ou la partie supérieure. S'il est égal, le mot a été trouvé. Si le mot n'a pas été trouvé, on recommence avec la sous-liste inférieure ou supérieure selon les cas jusqu'à ce qu'on ait trouvé le mot ou qu'on soit sûr que le mot cherché n'y est pas. Le résultat de la recherche est la position du mot dans la liste ou -1 si ce mot n'a pas été trouvé. Cette recherche s'appelle une recherche dichotomique.

5. Écrire la fonction qui effectue la recherche dichotomique d'un mot dans une liste triée de mots. Cette fonction peut être récursive ou non. Elle prend au moins les deux mêmes paramètres que ceux de la question 3, si elle en a d'autres, il faudra leur donner une valeur par défaut. On précise que les comparaisons entre chaînes de caractères utilisent aussi les opérateurs `<, ==, >`
6. Vérifier que les deux fonctions retournent bien les mêmes résultats.

