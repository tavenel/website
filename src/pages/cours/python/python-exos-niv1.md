---
title: Exercices Python niveau 1
---

## Entrée utilisateur

Écrire un programme qui demande à l'utilisateur de saisir son nom et affiche un message de bienvenue avec son nom.

:::correction
```python
# Demande de saisie du nom de l'utilisateur
nom = input("Entrez votre nom : ")

# Affichage du message de bienvenue
print("Bienvenue ", nom , " !")
```
:::

## Tables de multiplication

Écrire un programme qui affiche les `n` premiers termes de la table de multiplication d'un nombre donné.

L'utilisateur doit saisir la valeur de `n` et le nombre pour lequel la table de multiplication doit être affichée.

:::correction
```python
# Demande de saisie du nombre et du nombre de termes
nombre = int(input("Entrez un nombre : "))
termes = int(input("Entrez le nombre de termes de la table de multiplication : "))

# Boucle pour afficher les termes de la table de multiplication
for i in range(1, termes + 1):
    resultat = nombre * i
    print(nombre, "x", i, "=", resultat)
```
:::

## Diviseurs

### Diviseurs d'un nombre

L'utilisateur donne un entier supérieur à 1 et le programme affiche, s'il y en a, tous ses diviseurs propres sans répétition ainsi que leur nombre. S'il n'y en a pas, il indique qu'il est premier.
Pour rappel, `a` est un diviseur de `b` si, et seulement si, `a % b = 0`.
Par exemple :

```
Entrez un entier strictement positif : 12
Diviseurs propres sans répétition de 12 : 2 3 4 6 (soit 4 diviseurs propres)
Entrez un entier strictement positif : 13
Diviseurs propres sans répétition de 13 : aucun ! Il est premier
```

:::correction
```python
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
```
:::

### Nombres premiers

Écrire un programme affichant la liste des 100 plus petits nombres premiers.

:::correction
```python
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
```
:::

## Suite de Fibonacci

Écrire un programme qui calcule la suite de _Fibonacci_ jusqu'à un nombre donné. La suite de _Fibonacci_ est définie de la manière suivante : la première valeur est $0$, la deuxième valeur est $1$, et chaque valeur suivante est la somme des deux valeurs précédentes.

:::correction
```python
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
```
:::

## Gardien de phare

Un gardien de phare descend de son phare 5 fois par jour.

Écrire une procédure (donc sans `return`) `hauteurParcourue()` qui reçoit deux paramètres, le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
 
> Pour x marches de y cm, il parcourt z.zz m par semaine.

On n'oubliera pas :

- qu'une semaine comporte 7 jours ;
- qu'une fois en bas, le gardien doit remonter ;
- que le résultat est à exprimer en m.

Pour afficher le résultat, on pourra utiliser le formatage de chaîne de caractères Python suivant : `{:.2f}` permettant de formater l'affichage en un flottant à 2 chiffres après la virgule, par exemple le code suivant affichera : `La valeur de x est 3.14` :

```python
x = 3.14159265
print("La valeur de x est {:.2f}".format(x))
```

:::correction
```python
def marches_parcourues(nombre_de_marches, hauteur_de_marche):
	distance_parcourue_aller_retour = nombre_de_marches * hauteur_de_marche * 2
	distance_parcourue_par_jour = distance_parcourue_aller_retour * 5
	distance_parcourue_par_semaine = distance_parcourue_par_jour * 7
	distance_en_km = distance_parcourue_par_semaine / 100 / 1000
	print( "Pour {} marches de {} cm, il parcourt {:.2f} km par semaine."
	.format(nombre_de_marches, hauteur_de_marche, distance_en_km) )

marches_parcourues(100, 20)
# Pour 100 marches de 20 cm, il parcourt 1.40 km par semaine.
```
:::

## Chaîne d'ADN

Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide (valide signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison arbitraire de "a", "t", "g" ou "c").

- Écrire une fonction `valide()` qui renvoie vrai si la saisie est valide, faux sinon.
- Écrire une fonction `saisie()` qui effectue une saisie valide et renvoie la valeur saisie sous forme d'une chaîne de caractères. On utilisera la fonction `input()`.
- Écrire une fonction `proportion()` qui reçoit deux arguments, la chaîne et la séquence et qui retourne la proportion de séquence dans la chaîne (c'est-à-dire son nombre d'occurrences).

On pourra utiliser la fonction `len()` qui calcule la longueur d'une chaîne de caractères `mon_texte` : `len(mon_texte)`.

Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence et affiche le résultat.

Exemple d'affichage :

```
chaîne : attgcaatggtggtacatg
séquence : ca
Il y a 10.53 % de "ca" dans votre chaîne.
```

:::correction
```python
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
```
:::

