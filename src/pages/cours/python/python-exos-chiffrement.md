---
title: Exercices Python - chiffrement
---

## Code de César

Le code de César est un algorithme de chiffrement utilisé par Jules César dans ses correspondances secrètes : <https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage>.

Il s'agit d'appliquer un décalage prédéfini à l'alphabet utilisé normalement : par exemple, on décale toutes les lettres de 3 (`a` devient `d`, `b` devient `e`, `c` devient `f`, etc...)

En utilisant les fonctions : `ord(chr) -> int` pour récupérer l'ordinal d'un caractère (le numéro correspondant à son code) et `chr(int) -> chr` pour transformer un code de caractère en type caractère, écrire les fonctions suivantes :

1. `chiffre_cesar(texte, decalage)` qui chiffre une chaîne de caractères en lui appliquant le décalage souhaité
2. `dechiffre_cesar(code, decalage)` qui déchiffre une code ayant été chiffré avec le décalage fourni en paramètre.

On pourra utiliser les fonctions : `isalpha()`, `isupper()`, `islower()` de la classe `Character`.

## Chiffre de Vernam

Le code de César n'est pas très robuste à une analyse statistique du texte, et il est assez facile de casser ce code manuellement. Le chiffrement de Vernam améliore cette méthode en appliquant une permutation différente (prédéfinie) pour chaque caractère du texte : par exemple, on choisit de décaler le 1er caractère de 3, le 2e caractère de 7, le 3e de 1, etc...

1. Écrire une fonction `chiffre_vernam(texte, permutations)` qui prend en paramètre une chaîne de caractères à chiffrer et une liste de décalages à appliquer. Si la liste des décalages est plus petite que le texte, on recommence au début de cette liste.
2. Écrire une fonction `dechiffre_vernam(code, permutations)` qui réalise l'opération inverse.

## Fonction de hachage

Une fonction de hachage est une fonction qui permet de projeter un ensemble complexe et/ou de grande taille vers un ensemble simple et limité (entiers, chaînes de caractères à taille fixe, ...). Ces fonctions sont très utilisées en cryptographie, pour vérifier l'intégrité de données mais aussi en programmation pour optimiser l'indexation d'entrées.

1. Écrire une classe `MaClasse` dont le constructeur initialise trois attributs fournis en paramètres : `identifiant (entier), index (flottant entre 0 et 9), donnees (chaîne de caractères)`.
2. Écrire une fonction `hash()` sans paramètre qui calcule un hachage de la classe de la façon suivante : `10*identifiant + index`. Le résultat est un entier.
3. Calculer le `hash` des instances : `A(1, 0.1, 'hello')`, `B(2, 0.8, 'world')`, `C(2, 0.9, 'here')`. Que remarquez-vous ? (Écrire la réponse en commentaire dans le code de l'exercice).

