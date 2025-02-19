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

:::correction
```python
def chiffre_cesar(texte, decalage):
    texte_chiffre = ""
    for char in texte:
        if char.isalpha():
            # Vérifie si le caractère est une lettre
            if char.isupper():
                # Chiffre les lettres majuscules
                texte_chiffre += chr((ord(char) - ord('A' ) + decalage) % 26 + ord('A'))
            elif char.islower():
                # Chiffre les lettres minuscules
                texte_chiffre += chr((ord(char) - ord('a') + decalage) % 26 + ord('a'))
        else:
            # Conserve les caractères non alphabétiques tels quels
            texte_chiffre += char
    return texte_chiffre

def dechiffre_cesar(code, decalage):
    return chiffre_cesar(code, -decalage)

# Exemple d'utilisation
texte_original = "Hello, how are you ?"
decalage_utilise = 3

# Chiffrement du texte
texte_chiffre = chiffre_cesar(texte_original, decalage_utilise)
print("Texte chiffré:", texte_chiffre)

# Déchiffrement du texte
texte_dechiffre = dechiffre_cesar(texte_chiffre, decalage_utilise)
print("Texte déchiffré:", texte_dechiffre)
```
:::

## Chiffre de Vernam

Le code de César n'est pas très robuste à une analyse statistique du texte, et il est assez facile de casser ce code manuellement. Le chiffrement de Vernam améliore cette méthode en appliquant une permutation différente (prédéfinie) pour chaque caractère du texte : par exemple, on choisit de décaler le 1er caractère de 3, le 2e caractère de 7, le 3e de 1, etc...

1. Écrire une fonction `chiffre_vernam(texte, permutations)` qui prend en paramètre une chaîne de caractères à chiffrer et une liste de décalages à appliquer. Si la liste des décalages est plus petite que le texte, on recommence au début de cette liste.
2. Écrire une fonction `dechiffre_vernam(code, permutations)` qui réalise l'opération inverse.

:::correction
```python
def chiffre_vernam(texte, permutations):
    texte_chiffre = ""
    i = 0  # Indice pour parcourir la liste des permutations
    for char in texte:
        if char.isalpha():
            # Vérifie si le caractère est une lettre
            if char.isupper():
                # Chiffre les lettres majuscules
                texte_chiffre += chr((ord(char) - ord('A') + permutations[i]) % 26 + ord('A'))
            elif char.islower():
                # Chiffre les lettres minuscules
                texte_chiffre += chr((ord(char) - ord('a') + permutations[i]) % 26 + ord('a'))
            i = (i + 1) % len(permutations)  # Réinitialise à zéro si on atteint la fin de la liste
        else:
            # Conserve les caractères non alphabétiques tels quels
            texte_chiffre += char
    return texte_chiffre

def dechiffre_vernam(code, permutations):
    # Utilise la fonction de chiffrement avec les décalages inverses pour déchiffrer
    decalages_inverse = [-x for x in permutations]
    return chiffre_vernam(code, decalages_inverse)

# Exemple d'utilisation
texte_original_vernam = "Hello, how are you ?"
permutations_utilisees = [3, 7, 1]

# Chiffrement du texte
texte_chiffre_vernam = chiffre_vernam(texte_original_vernam, permutations_utilisees)
print("Texte chiffré (Vernam):", texte_chiffre_vernam)

# Déchiffrement du texte
texte_dechiffre_vernam = dechiffre_vernam(texte_chiffre_vernam, permutations_utilisees)
print("Texte déchiffré (Vernam):", texte_dechiffre_vernam)
```
:::

## Fonction de hachage

Une fonction de hachage est une fonction qui permet de projeter un ensemble complexe et/ou de grande taille vers un ensemble simple et limité (entiers, chaînes de caractères à taille fixe, ...). Ces fonctions sont très utilisées en cryptographie, pour vérifier l'intégrité de données mais aussi en programmation pour optimiser l'indexation d'entrées.

1. Écrire une classe `MaClasse` dont le constructeur initialise trois attributs fournis en paramètres : `identifiant (entier), index (flottant entre 0 et 9), donnees (chaîne de caractères)`.
2. Écrire une fonction `hash()` sans paramètre qui calcule un hachage de la classe de la façon suivante : `10*identifiant + index`. Le résultat est un entier.
3. Calculer le `hash` des instances : `A(1, 0.1, 'hello')`, `B(2, 0.8, 'world')`, `C(2, 0.9, 'here')`. Que remarquez-vous ? (Écrire la réponse en commentaire dans le code de l'exercice).

:::correction
```python
class MaClasse:
    def __init__(self, identifiant, index, donnees):
        self.identifiant = identifiant
        self.index = index
        self.donnees = donnees

    def hash(self):
        return int(10 * self.identifiant + self.index)

# Instances de la classe
A = MaClasse(1, 0.1, 'hello')
B = MaClasse(2, 0.8, 'world')
C = MaClasse(2, 0.9, 'here')

# Calcul des hashs
hash_A = A.hash()
hash_B = B.hash()
hash_C = C.hash()

# Imprimer les résultats
print("Hash de A:", hash_A)
print("Hash de B:", hash_B)
print("Hash de C:", hash_C)

# Remarques :
# Les instances B et C ont le même identifiant (2) mais des index différents.
# Cependant, la fonction de hashage ne prend en compte que l'identifiant et l'index,
# ce qui signifie que les instances B et C auront le même hash.
# Ceci peut causer des collisions dans un contexte où des valeurs distinctes ont le même hash.
```
:::

