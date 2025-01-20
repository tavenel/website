# Jeu du plus ou moins

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
            print(f"Le résultat est entre {10 * int(result / 10)} \
et {10 * (int(result / 10) +1)}")

# (Dé)sérialisation simple d'objets Python

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

