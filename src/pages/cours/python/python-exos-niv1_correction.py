## Entrée utilisateur

# Demande de saisie du nom de l'utilisateur
nom = input("Entrez votre nom : ")

# Affichage du message de bienvenue
print("Bienvenue ", nom , " !")

## -------------------------------------------------------------------------
## Tables de multiplication

# Demande de saisie du nombre et du nombre de termes
nombre = int(input("Entrez un nombre : "))
termes = int(input("Entrez le nombre de termes de la table de multiplication : "))

# Boucle pour afficher les termes de la table de multiplication
for i in range(1, termes + 1):
    resultat = nombre * i
    print(nombre, "x", i, "=", resultat)

## -------------------------------------------------------------------------
### Diviseurs d'un nombre
def diviseurs(nb):
    compteur = nb
    diviseurs = 0
    while compteur != 2:
        compteur -= 1
        if nb % compteur == 0:
            print(compteur, ' est un diviseur de ', nb)
            diviseurs += 1
            #premier = False

    return diviseurs
    
if __name__ == '__main__':

    nb = int(input("Nombre :"))
    nb_diviseurs = diviseurs(nb)
    if nb_diviseurs: # diviseurs != 0
        print(nb, ' a ', nb_diviseurs, ' diviseurs')
    else:
        print(nb, ' est un nombre premier')

    # Ou beaucoup plus directement :
    nb_diviseurs2 = [x for x in range(2, nb) if nb % x == 0]



    ### Nombres premiers
    premiers = []
    nb_premiers = 0
    i = 2
    while nb_premiers < 100:
        if not diviseurs(i):
            premiers.append(i)
            nb_premiers += 1
        i += 1
    print(premiers)

## -------------------------------------------------------------------------
## Suite de Fibonacci

# Demande de saisie du nombre maximum
nombre_max = int(input("Entrez le nombre maximum : "))

# Initialisation des variables
n1 = 0
n2 = 1

# Boucle pour afficher les termes de la suite de Fibonacci
while n1 <= nombre_max:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth


## -------------------------------------------------------------------------
## Gardien de phare

def marches_parcourues(nombre_de_marches, hauteur_de_marche):
	distance_parcourue_aller_retour = nombre_de_marches * hauteur_de_marche * 2
	distance_parcourue_par_jour = distance_parcourue_aller_retour * 5
	distance_parcourue_par_semaine = distance_parcourue_par_jour * 7
	distance_en_km = distance_parcourue_par_semaine / 100 / 1000
	print( "Pour {} marches de {} cm, il parcourt {:.2f} km par semaine."
	.format(nombre_de_marches, hauteur_de_marche, distance_en_km) )

marches_parcourues(100, 20)
# Pour 100 marches de 20 cm, il parcourt 1.40 km par semaine.

## -------------------------------------------------------------------------
## Chaîne d'ADN

def valide(chaine):
    """Retourne vrai si la chaîne est composée de a,t,g,c"""
    if len(chaine) < 1:
        return False
    
    for car in chaine:
        if car not in 'atcg':
            return False

    # Cas general
    return True 

def saisie(user_text):
    s = input(user_text)
    while not valide(s) :
        print(s, "ne peut contenir que les chaînons 'a', 't', 'g' et 'c' et ne doit pas être vide")
        s = input(user_text)
    return s

def proportion(chaine, sequence):
    """Retourne la proportion de la séquence <s> dans la chaîne <a>."""
    return 100* chaine.count(sequence) / len(chaine)

if __name__ == '__main__':
    chaine = saisie("Chaine : ")
    sequence = saisie("Sequence à chercher : ")
    print(" Il y a {:.2f} % de {:s} dans la chaine".format(proportion(chaine, sequence), sequence))
