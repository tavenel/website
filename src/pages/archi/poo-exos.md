---
title: Exercices POO
date: 2023 / 2024
---

## Création d'une classe

Créez une classe nommée `Personne` avec les attributs suivants : `nom`, `prenom`, `age` et `adresse`. Ajoutez également une méthode nommée "parler" qui affiche un message de salutation.

## Composition - Bibliothèque

1. Créez une classe `Livre` qui a des attributs `titre` et `auteur`. Ajoutez une méthode `afficher` qui affiche le titre et l'auteur du livre.
2. Créez une classe `Bibliotheque` qui a un attribut `livres` (une liste d'objets `Livre`). Ajoutez des méthodes `ajouter_livre` et `supprimer_livre` pour ajouter et supprimer des livres de la bibliothèque.

## Héritage et polymorphisme

### Héritage - Personne et Employé

Créez une classe nommée `Employe` qui hérite de la classe `Personne`. Ajoutez un nouvel attribut à la classe `Employe` nommé `salaire` et une méthode nommée `travailler` qui affiche un message disant que l'employé est en train de travailler.

Pour utiliser une méthode de la classe parente, on utilise la fonction `super()`, par exemple : `super().__init__(...` appelle le constructeur du parent.

### Polymorphisme - animaux

Créez une classe nommée `Animal` avec une méthode `regime_alimentaire`. Ensuite, créez deux sous-classes `Lapin` et `Chat` qui héritent de la classe `Animal` et qui affichent chacune à l'écran le `regime_alimentaire` de l'animal : `"végétarien"` pour `Lapin` et `"carnivore"` pour `Chat`.

### Polymorphisme - Véhicule et Bus

Créer une classe `Bus` héritant de la classe `Vehicle` ayant une capacité par défaut de `50` :
`Bus.seating_capaticy()` retourne `The seating capacity of a bus is 50 passengers`

:::correction
## Correction

```python
class Personne:
    
    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
    
    def parler(self):
        print("Bonjour, je m'appelle", self.prenom, self.nom,  \
        "et j'ai", self.age,  \
        "ans. J'habite à", self.adresse)

class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
    def afficher(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")

class Bibliothèque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"{livre.titre} a été ajouté à la bibliothèque.")

    def supprimer_livre(self, livre):
        if livre in self.livres:
            self.livres.remove(livre)
            print(f"{livre.titre} a été supprimé de la bibliothèque.")
        else:
            print(f"{livre.titre} n'est pas dans la bibliothèque.")

    def afficher_livres(self):
        if len(self.livres) == 0:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque:")
            for livre in self.livres:
                print(f"- {livre.titre} par {livre.auteur}")

class Employe(Personne):
    
    def __init__(self, nom, prenom, age, adresse, salaire):
        super().__init__(nom, prenom, age, adresse)
        self.salaire = salaire
    
    def travailler(self):
        print(self.prenom, self.nom, "est en train de travailler.")

class Animal:
    
    def regime_alimentaire(self):
        pass

class Lapin(Animal):
    
    def regime_alimentaire(self):
        print("végétarien")

class Chat(Animal):
    
    def regime_alimentaire(self):
        print("carnivore")

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__('bus', max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

if __name__ == '__main__':
    b = Bus(max_speed=90, mileage=100)
    print(b.seating_capacity())
    print(b.seating_capacity(65))
```

:::

## Gestion d'étudiants

Dans cet exercice, vous allez créer un programme qui permet de stocker et de gérer une liste d'étudiants.

1. Créez une classe `Etudiant` avec les attributs suivants :
  - nom
  - prénom
  - date de naissance (au format "jj/mm/aaaa")
  - liste de notes (sous forme de liste de nombres)
2. Ajoutez une méthode `moyenne` qui calcule la moyenne des notes de l'étudiant.
3. Créez une classe `GestionEtudiants` avec :
  - un attribut liste d'étudiants (sous forme de liste d'objets `Etudiant`)
  - les méthodes suivantes :
    + ajouter un étudiant à la liste ;
    + supprimer un étudiant de la liste ;
    + afficher la liste des étudiants (avec leur nom, prénom, date de naissance et moyenne).
3. Créez une fonction `menu` qui affiche un menu sur la console permettant à l'utilisateur de choisir entre les actions suivantes :
  - ajouter un étudiant ;
  - supprimer un étudiant ;
  - afficher la liste des étudiants ;
  - quitter le programme.
4. Dans une boucle principale, appelez la fonction `menu` pour afficher le menu et traiter l'action choisie par l'utilisateur.

:::correction
### Correction

```python
class Etudiant:
    def __init__(self, nom, prenom, date_naissance, notes):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.notes = notes

    def moyenne(self):
        if len(self.notes) == 0:
            return 0
        else:
            return sum(self.notes) / len(self.notes)

class GestionEtudiants:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def supprimer_etudiant(self, nom, prenom):
        for etudiant in self.etudiants:
            if etudiant.nom == nom and etudiant.prenom == prenom:
                self.etudiants.remove(etudiant)

    def afficher_liste_etudiants(self):
        for etudiant in self.etudiants:
            print(f"Nom : {etudiant.nom} | Prénom : {etudiant.prenom} | Date de naissance : {etudiant.date_naissance} | Moyenne : {etudiant.moyenne()}")

def menu():
    print("1. Ajouter un étudiant")
    print("2. Supprimer un étudiant")
    print("3. Afficher la liste des étudiants")
    print("4. Quitter le programme")
    choix = input("Entrez votre choix : ")
    return choix

if __name__ == "__main__":
    gestion_etudiants = GestionEtudiants()

    while True:
        choix = menu()

        if choix == "1":
            nom = input("Nom de l'étudiant : ")
            prenom = input("Prénom de l'étudiant : ")
            date_naissance = input("Date de naissance de l'étudiant (jj/mm/aaaa) : ")
            notes = []
            while True:
                note = input("Note de l'étudiant (ou 'q' pour arrêter) : ")
                if note == "q":
                    break
                else:
                    notes.append(float(note))
            etudiant = Etudiant(nom, prenom, date_naissance, notes)
            gestion_etudiants.ajouter_etudiant(etudiant)
            print("Etudiant ajouté avec succès !\n")

        elif choix == "2":
            nom = input("Nom de l'étudiant à supprimer : ")
            prenom = input("Prénom de l'étudiant à supprimer : ")
            gestion_etudiants.supprimer_etudiant(nom, prenom)
            print("Etudiant supprimé avec succès !\n")

        elif choix == "3":
            gestion_etudiants.afficher_liste_etudiants()
            print()

        elif choix == "4":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.\n")
```

:::

## Figures Colorées

### Figures géométriques

#### Classe Rectangle

- Écrire une classe `Rectangle` permettant de construire un rectangle dotée d'attributs `longueur` et `largeur`.
- Créer une méthode `perimetre()` permettant de calculer le périmètre du rectangle et une méthode `surface()` permettant de calculer la surface du rectangle
- Créer 2 instances de `Rectangle` et calculer leurs `perimetre()` et `surface()`.

#### Héritage : classe Carré

- Créer une classe `Carre` héritant de `Rectangle` et permettant de créer un carré.
- Créer une instance de `Carre` et calculer son `perimetre()` et `surface()`.

#### Classe Cercle

- Créer une classe `Cercle` pour construire un cercle ayant un `rayon`.
- Ajouter des méthodes `perimetre()` et `surface()`. Utiliser `math.pi` (`import math`).
  + On rappelle que le périmètre d'un cercle se calcule par la formule : $2\Pi.r$
  + On rappelle que la surface d'un cercle se calcule par la formule : $\Pi.r^2$
- Que remarque-t-on quand aux méthodes de ces différentes classes ?
  + Quel type d'architecture permet de gérer proprement cette similarité ?
  + Implémenter cette architecture

### Couleurs

#### RGB

- Créer une classe `CouleurRGB` permettant de stocker une couleur au format Rouge, Vert, Bleu. Cette classe possède donc 3 attributs (entiers) : `rouge`, `vert`, `bleu`.
- Ajouter une méthode `couleur_rgb()` affichant la couleur RGB sous forme d'un triplet : `(rouge,vert,bleu)`. Par exemple : `(10,20,100)`.
- Ajouter une méthode `couleur_hexa()` permettant de retourner la couleur au format hexadécimal correspondant : on utilisera le code `f"#{r:02x}{g:02x}{b:02x}"` pour convertir 3 variables `r`, `g` et `b`.

#### Hexadécimal

- Créer une classe `CouleurHexa` permettant de stocker une couleur au format hexadécimal. Cette classe possède un attribut unique (chaîne de caractères de type : `#aabbcc`) : `hexa`.
- Ajouter une méthode `couleur_hexa()` permettant de retourner la couleur au format hexadécimal.
- Ajouter une méthode `couleur_rgb()` permettant de retourner la couleur RGB correspondante. On utilisera le code : `(int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16))` pour convertir une chaîne de caractères hexadécimale `hx` (de type `#aabbcc`) en triple `R,G,B` correspondant.

### Délégation : figure avec couleur

En utilisant 2 fois un pattern de délégation pour les figures géométriques et pour les couleurs, créer une classe : `FigureColoree` représentant une figure géométrique ayant une couleur.

Les instances de cette classe doivent posséder les méthodes suivantes : `perimetre()`, `surface()`, `couleur_rgb()`, `couleur_hexa()`.

:::correction
### Correction

```python
import zope.interface
from zope.interface.verify import verifyObject, verifyClass

import math

###################################################
# Interfaces par contrat utilisant zope.interface #
###################################################

class FigureGeometrique(zope.interface.Interface):
    def perimetre():
        raise NotImplementedError("A spécialiser")
    def surface():
        raise NotImplementedError("A spécialiser")

@zope.interface.implementer(FigureGeometrique)
class Rectangle():
    def __init__(self, longueur, largeur):
        self.L = longueur
        self.l = largeur
        print(f'Nouvelle instance de rectangle : {self.L} et {self.l}')

    def perimetre(self):
        return 2*(self.l + self.L)

    def surface(self):
        return self.l * self.L

class Carre(Rectangle):
    def __init__(self, cote):
        super().__init__(cote, cote)

@zope.interface.implementer(FigureGeometrique)
class Cercle():
    def __init__(self, rayon):
        self.r = rayon
    
    def perimetre(self):
        return int( 2 * math.pi * self.r )
    
    def surface(self):
        return int( math.pi * (self.r ** 2) )

@zope.interface.implementer(FigureGeometrique)
class Ovale():
    def __init__(self, a, b):
        self.a = a
        self.b = b

verifyClass(FigureGeometrique, Rectangle)
verifyClass(FigureGeometrique, Carre)
verifyClass(FigureGeometrique, Cercle)
#Ovale ne vérifie pas l'interface => ERREUR
#verifyClass(FigureGeometrique, Ovale)

r1 = Rectangle(1,2)
r2 = Rectangle(3,4)

print(r1.perimetre())
print(r1.surface())

print(r2.perimetre())
print(r2.surface())

c = Carre(3)
print( c.perimetre() )
print( c.surface() )

cc = Cercle(5)
print( cc.perimetre() )
print( cc.surface() )

print("###BOUCLE###")
for f in [r1, r2, c, cc]:
    verifyObject(FigureGeometrique, f)
    print( f.perimetre() )
    print( f.surface() )

o = Ovale(2, 3)
#verifyObject(FigureGeometrique, o)



#####################################################
# Interfaces informelles (Duck Typing) - seules les #
# classes respectent le même contrat                #
#####################################################
class CouleurRGB:
    def __init__(self, rouge, vert, bleu):
        self.r = rouge
        self.g = vert
        self.b = bleu
    
    def couleur_rgb(self):
        return ( self.r, self.g, self.b )
    
    def couleur_hexa(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

class CouleurHexa:
    def __init__(self, code_hexa):
        self.hx = code_hexa
    
    def couleur_rgb(self):
        return (int(self.hx[1:3],16),int(self.hx[3:5],16),int(self.hx[5:7],16))
    
    def couleur_hexa(self):
        return self.hx

rgb = CouleurRGB(10, 20, 100)
print( rgb.couleur_rgb() )
print( rgb.couleur_hexa() )
hexa = CouleurHexa('#0a1464')
print( hexa.couleur_rgb() )
print( hexa.couleur_hexa() )

for c in [rgb, hexa]:
    print( c.couleur_rgb() )
    print( c.couleur_hexa() )


#####################################################
# Pattern Délégation - FigureGeométrique et Couleur #
#####################################################
@zope.interface.implementer(FigureGeometrique)
class FigureColoree:
    def __init__(self, forme:FigureGeometrique, couleur): # couleur: CouleurRGB ou CouleurHexa
        self.forme = forme
        self.couleur = couleur
    
    def perimetre(self):
        return self.forme.perimetre()
    
    def surface(self):
        return self.forme.surface()

    def couleur_de_figure(self):
        return self.couleur.couleur_hexa()
    
carre = Carre(4)
coul = CouleurRGB(10,2,1)

fc = FigureColoree( carre, coul )
fc2 = FigureColoree( Carre(3), CouleurHexa('#11aa22') )
fc3 = FigureColoree( Cercle(5), CouleurHexa('#11aa22') )
fc4 = FigureColoree( Ovale(2, 3), CouleurHexa('#11aa22') ) # Ne respecte pas le contrat (Ovale)
print( fc.perimetre() )
# print( fc4.perimetre() ) ## CRASH !!

print("###### Boucle de figures colorées #####")
for fig in [fc, fc2, fc3]:
    print( fig.perimetre() )
    print( fig.surface() )
    print( fig.couleur_de_figure() )
```
:::

## Gestion d'une pharmacie

On s'intéresse à la gestion d'une pharmacie qui gère des clients et des produits.

Une _pharmacie_ est caractérisée par son _nom_ (`str`), son _adresse_ (de type `str`), ses _clients_ (liste de `clients`) et ses _produits_ (liste de `produits`).
Un _client_ est caractérisé par son _nom_ (`str`), son _prénom_ (`str`), le _numéro de sa carte vitale_ (`int`).
Un _produit_ est caractérisé par sa _référence_ (`str`) et son _prix_ (`float`).
Les produits que vend cette pharmacie sont soit des _médicaments_, soit des produits de _parapharmacie_.
Les _médicaments_ sont caractérisés par le fait qu'ils peuvent être _génériques_ ou pas, et par le fait qu'ils peuvent être délivrés _sans ordonnance ou pas_.
Les produits de _parapharmacie_ sont quant à eux caractérisés par leur _type de produit_ : _produit de beauté_, _cosmétique_ ou _diététique_.

Le programme doit permettre les opérations de gestion de la pharmacie suivantes :

- L'opération d'_achat_ caractérisée par un produit, un client et une quantité.
- L'opération d'_approvisionnement_ du stock caractérisée par un produit et une quantité.
- L'affichage de la liste des clients de la pharmacie et la liste des produits qu'elle vend.
- L'affichage des informations concernant le client.
- L'affichage des informations concernant un produit.
- L'affichage des informations concernant un médicament.
- L'affichage des informations concernant un produit de parapharmacie.

### Modélisation

Proposer une modélisation orientée objet permettant la gestion d'une pharmacie : donner les classes, leurs attributs et leurs méthodes sous forme d'un schéma, en précisant les relations entre les classes (en utilisant : `hérite de` et `utilise`).
Il n'est pas demandé de donner l'implémentation des méthodes (seulement leur prototype, c'est-à-dire leur nom, le type des arguments en entrée et le type de retour).
Il n'est pas non plus demandé de formalisme strict (type UML) mais plutôt un schéma clair du contenu des classes et de leurs interactions.

### Implémentation

Implémenter en Python la modélisation orientée objet proposée. Pour vérifier cette implémentation, créer une instance de la pharmacie et des instances de clients, de produits, ... Vérifier ensuite le bon déroulement des opérations de gestion de la pharmacie en utilisant ces instances.

:::correction
### Correction

```
Pharmacie
├── Attributs :
│   ├── nom: str
│   ├── adresse: str
│   ├── clients: List[Client]
│   └── produits: Dict{Produit, quantite:int}
│
├── Méthodes :
│   ├── achat(produit: Produit, client: Client, quantite: int) -> None
│   ├── approvisionnement(produit: Produit, quantite: int) -> None
│   ├── afficher_clients() -> None
│   └── afficher_produits() -> None
│
└── Hérite de : None

Client
├── Attributs :
│   ├── nom: str
│   ├── prenom: str
│   └── numero_carte_vitale: int
│
├── Méthodes :
│   └── afficher_informations() -> None
│
└── Hérite de : None

Produit
├── Attributs :
│   ├── reference: str
│   └── prix: float
│
├── Méthodes :
│   └── afficher_informations() -> None
│
└── Hérite de : None

Medicament
├── Attributs :
│   ├── generique: bool
│   └── ordonnance_obligatoire: bool
│
├── Méthodes :
│   └── afficher_informations() -> None
│
└── Hérite de : Produit

ProduitParapharmacie
├── Attributs :
│   └── type_produit: TypeProduit
│
├── Méthodes :
│   └── afficher_informations() -> None
│
└── Hérite de : Produit

enum TypeProduit (BEAUTE,COSMETIQUE,DIETETIQUE)
```

```python
class Pharmacie:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.clients = []
        self.produits = {}

    def achat(self, produit, client, quantite):
        if client not in self.clients:
            self.clients.append(client)
        if self._get_stock(produit) > quantite:
            self._retrait(produit, quantite)
            print(f"Le client {client} achète {quantite} {produit}")
        else:
            print(f"Le client {client} ne peut pas acheter {quantite} de {produit}")

    def _get_stock(self, produit):
        if produit not in self.produits:
            return 0
        else:
            for (produit_stock, stock) in self.produits.items():
                if produit_stock == produit:
                    return stock

    def approvisionnement(self, produit, quantite):
        self.produits[produit] = self._get_stock(produit) + quantite

    def _retrait(self, produit, quantite):
        self.approvisionnement(produit, -quantite)

    def afficher_clients(self):
        for client in clients:
            print(client)

    def afficher_produits(self):
        for produit in produits:
            print(produit)

    def __str__(self):
        return f"Pharmacie {self.nom} à {self.adresse}\nClients: {self.clients}\nListe de produits: {self.produits}"

class Client:
    def __init__(self, nom, prenom, numero_carte_vitale):
        self.nom = nom
        self.prenom = prenom
        self.numero_carte_vitale = numero_carte_vitale

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def afficher_informations(self):
        print(self)

class Produit:
    def __init__(self, reference, prix):
        self.reference = reference
        self.prix = prix

    def afficher_informations(self):
        print(self)

class Medicament(Produit):
    def __init__(self, reference, prix, ordonnance_obligatoire, generique=False):
        super().__init__(reference, prix)
        self.ordonnance_obligatoire = ordonnance_obligatoire
        self.generique = generique

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.reference}{' (générique)' if self.generique else ''} {self.prix}eu"

from enum import StrEnum, auto
class TypeProduit(StrEnum):
    BEAUTE = auto()
    COSMETIQUE = auto()
    DIETETIQUE = auto()

class ProduitParapharmacie(Produit):
    def __init__(self, reference, prix, type_produit):
        super().__init__(reference, prix)
        self.type_produit = type_produit

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.reference} ({self.type_produit}) {self.prix}eu"

pharma = Pharmacie("Ma pharmacie", "38000 Grenoble")

doliprane = Medicament("doliprane", prix=12, ordonnance_obligatoire=False)
doliprane = Medicament("antibiotique", prix=32, ordonnance_obligatoire=False)
complement = ProduitParapharmacie("complément alimentaire", 15, TypeProduit.DIETETIQUE)

pharma.approvisionnement(doliprane, 4)
pharma.approvisionnement(complement, 7)

client1 = Client("Doe", "John", "123456789")
pharma.achat(client=client1, produit=doliprane, quantite=3)
pharma.achat(client=client1, produit=doliprane, quantite=5)

print(pharma)
```
:::

