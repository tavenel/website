---
title: Exercices Python
---

## Jeu du plus ou moins

Tirer un nombre au hasard entre 1 et 100. L'utilisateur doit trouver ce nombre et pour cela proposer des valeurs - le programme indique à chaque réponse de l'utilisateur si le nombre est supérieur ou inférieur à celui entré.
Au bout de 5 essais, si le nombre n'a pas été trouvé le programme indique entre quelles dizaines chercher (par exemple : entre 30 et 40 pour 42).

:::correction
```python
def input_int():
    while True:
        try:
            return int(input("Proposition:"))
        except ValueError:
            print("Invalid")

if __name__ == '__main__':

    import random
    result = random.randint(0, 100)
    tries = 0

    while True:
        choice = input_int()
        if choice == result:
            print("Bravo !")
            break
        elif choice < result:
            print("C'est plus")
        elif choice > result:
            print("C'est moins")

        tries += 1
        if tries == 5:
            print(f"Le résultat est entre {10 * int(result / 10)}  et {10 * (int(result / 10) +1)}")
```
:::

## (Dé)sérialisation simple d'objets Python

Soit une classe Point possédant 3 attributs `x`,`y`,`z`.

1. Écrire l'implémentation de cette classe en Python.
2. Définir une liste d'instances de points : `[(1,2,0);(2,4,8);(0,1,0)]`
3. Sérialiser et stocker cette liste dans un fichier `JSON`
4. Dans un shell Python, désérialiser ce fichier `JSON` dans une variable.
5. Afficher le résultat de l'addition des points en utilisant la variable précédente.

:::correction
```python
import json

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point[{self.x}, {self.y}, {self.z}]'

    def __str__(self):
        return f'[{self.x}, {self.y}, {self.z}]'

    @staticmethod
    def fromJSON(json_dict):
        #return Point(x=json_dict['x'])
        print('p : ', json.loads(json_dict))
        return json_dict

class CustomEncoder(json.JSONEncoder):
    ''' Encoder JSON : sérialisation en utilisant les données __dict__ '''
    def default(self, o):
            return o.__dict__

def point_from_dict(dct):
    ''' Désérialisation de dict en Point '''
    return Point(dct['x'], dct['y'], dct['z'])


class Point2(dict):
    ''' Hack : hériter de la classe dict pour hériter de
    toutes les fonctionnalités (repr, str, json) '''
    def __init__(self, fname):
        dict.__init__(self, fname=fname)

if __name__ == '__main__':

    # Solution naive
    l = [ Point(1,2,0), Point(2,4,8), Point(0,1,0) ]
    print("Origine:", l)
    # Sérialisation et stockage
    with open('out.json', 'w') as f:
        json.dump(l, f, cls=CustomEncoder)
    with open('out.json', 'r') as f:
        # Récupération
        l_get = json.load(f, object_hook=point_from_dict)
        print("Deserialize:", l_get)

    # Solution par héritage
    l2 = [
        Point2({'x':1,'y':2,'z':0}),
        Point2({'x':2,'y':4,'z':8}),
        Point2({'x':0,'y':1,'z':0})
        ]
    print("Origine:", l2)
    # Sérialisation et stockage
    with open('out2.json', 'w') as f:
        json.dump(l2, f)
    with open('out2.json', 'r') as f:
        # Récupération
        l2_get = json.load(f)
        print("Deserialize:", l2_get)
```
:::

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

:::correction
### Correction

```python
# Question 1
def lire_fichier_mots(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        mots = fichier.read().splitlines()
    return mots

# Question 2
def est_triee(liste_mots):
    return liste_mots == sorted(liste_mots)

# Question 3
def recherche_position_mot(liste_mots, mot):
    if mot in liste_mots:
        return liste_mots.index(mot)
    else:
        return -1

# Question 4
mots_liste = lire_fichier_mots('mots.txt')
position_un = recherche_position_mot(mots_liste, 'UN')
position_deux = recherche_position_mot(mots_liste, 'DEUX')
print(f"Position de 'UN' : {position_un}")
print(f"Position de 'DEUX' : {position_deux}")

# Méthode itérative
# Question 5
def recherche_dichotomique_iteratif(liste_mots, mot, debut=0, fin=None):
    # Même algorithme mais itératif (on n'appelle pas la fonction plusieurs fois)

    if fin is None:
        fin = len(liste_mots)

    while debut <= fin:

        # on divise la liste en 2 pour chercher dans l'une des 1/2 listes seulement
        milieu = (debut + fin) // 2 # division entière
        mot_milieu = liste_mots[milieu]

        # on utilise la notion d'ordre en Python : il est possible de comparer
        # directement des mots par ordre lexicographique (comme dans un dictionnaire).
        # MOT1 < MOT2 si MOT1 vient avant MOT2 dans l'ordre lexicographique
        if mot_milieu == mot:
            # trouvé
            return milieu
        elif mot_milieu < mot:
            debut = milieu + 1
            # Le mot n'a pas été trouvé mais on a mis à jour les index
            # on cherche dans la 1/2 liste du milieu à la fin
            # Python est un langage de passage d'arguments par valeur.
            # on a copié `debut`, on peut donc utiliser sa nouvelle valeur directement
        else:
            fin = milieu - 1
            # Le mot n'a pas été trouvé mais on a mis à jour les index
            # on cherche dans la 1/2 liste du début au milieu
            # Python est un langage de passage d'arguments par valeur
            # on a copié `fin`, on peut donc utiliser sa nouvelle valeur directement

    # Cas d'arrêt - le mot n'a pas été trouvé (debut > fin)
    return -1

# Question 6
len_liste = len(mots_liste)
sorted_liste = sorted(mots_liste)
position_un_dicho = recherche_dichotomique_iteratif(sorted_liste, 'UN')
position_deux_dicho = recherche_dichotomique_iteratif(sorted_liste, 'DEUX')
print(f"Position de 'UN' (dichotomique) : {position_un_dicho}")
print(f"Position de 'DEUX' (dichotomique) : {position_deux_dicho}")
assert position_un_dicho == position_un
assert position_deux_dicho == position_deux

## Par récursion
## Question 5
def recherche_dichotomique_recursif(liste_mots, mot, debut=0, fin=None):
    return dicho_rec( liste_mots, mot, debut, fin or len(liste_mots) )

def dicho_rec(liste_mots, mot, debut, fin):
    if debut > fin:
        # Cas d'arrêt - le mot n'a pas été trouvé
        return -1

    # on divise la liste en 2 pour chercher dans l'une des 1/2 listes seulement
    milieu = (debut + fin) // 2 # division entière
    mot_milieu = liste_mots[milieu]

    # on utilise la notion d'ordre en Python : il est possible de comparer
    # directement des mots par ordre lexicographique (comme dans un dictionnaire).
    # MOT1 < MOT2 si MOT1 vient avant MOT2 dans l'ordre lexicographique
    if mot_milieu == mot:
        # trouvé
        return milieu
    elif mot_milieu < mot:
        debut = milieu + 1
        # Le mot n'a pas été trouvé mais on a mis à jour les index
        # on cherche dans la 1/2 liste du milieu à la fin
        return dicho_rec(liste_mots, mot, debut, fin)
    else:
        fin = milieu - 1
        # Le mot n'a pas été trouvé mais on a mis à jour les index
        # on cherche dans la 1/2 liste du début au milieu
        return dicho_rec(liste_mots, mot, debut, fin)

# Question 6
position_un_dicho_rec = recherche_dichotomique_recursif(sorted_liste, 'UN')
position_deux_dicho_rec = recherche_dichotomique_recursif(sorted_liste, 'DEUX')
print(f"Position de 'UN' (dichotomique récursif) : {position_un_dicho_rec}")
print(f"Position de 'DEUX' (dichotomique récursif) : {position_deux_dicho_rec}")
assert position_un_dicho_rec == position_un
assert position_deux_dicho_rec == position_deux
```
:::

