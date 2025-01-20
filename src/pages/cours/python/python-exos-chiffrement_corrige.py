## Code de César

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


## -------------------------------------------------------------------------------------------
## Chiffre de Vernam

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


## -------------------------------------------------------------------------------------------
## Fonction de hachage

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

