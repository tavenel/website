---
title: Gestion d'une pharmacie
date: 2023 / 2024
correction: false
---

## Gestion d’une pharmacie

On s'intéresse à la gestion d'une pharmacie qui gère des clients et des produits.

Une _pharmacie_ est caractérisée par son _nom_ (`str`), son _adresse_ (de type `str`), ses _clients_ (liste de `clients`) et ses _produits_ (liste de `produits`).
Un _client_ est caractérisé par son _nom_ (`str`), son _prénom_ (`str`), le _numéro de sa carte vitale_ (`int`).
Un _produit_ est caractérisé par sa _référence_ (`str`) et son _prix_ (`float`).
Les produits que vend cette pharmacie sont soit des _médicaments_, soit des produits de _parapharmacie_.
Les _médicaments_ sont caractérisés par le fait qu’ils peuvent être _génériques_ ou pas, et par le fait qu’ils peuvent être délivrés _sans ordonnance ou pas_.
Les produits de _parapharmacie_ sont quant à eux caractérisés par leur _type de produit_ : _produit de beauté_, _cosmétique_ ou _diététique_.

Le programme doit permettre les opérations de gestion de la pharmacie suivantes :

- L'opération d'_achat_ caractérisée par un produit, un client et une quantité.
- L'opération d'_approvisionnement_ du stock caractérisée par un produit et une quantité.
- L'affichage de la liste des clients de la pharmacie et la liste des produits qu’elle vend.
- L'affichage des informations concernant le client.
- L'affichage des informations concernant un produit.
- L'affichage des informations concernant un médicament.
- L'affichage des informations concernant un produit de parapharmacie.

## Modélisation

Proposer une modélisation orientée objet permettant la gestion d'une pharmacie : donner les classes, leurs attributs et leurs méthodes sous forme d'un schéma, en précisant les relations entre les classes (en utilisant : `hérite de` et `utilise`).
Il n’est pas demandé de donner l'implémentation des méthodes (seulement leur prototype, c'est-à-dire leur nom, le type des arguments en entrée et le type de retour).
Il n'est pas non plus demandé de formalisme strict (type UML) mais plutôt un schéma clair du contenu des classes et de leurs interactions.

## Implémentation

Implémenter en Python la modélisation orientée objet proposée. Pour vérifier cette implémentation, créer une instance de la pharmacie et des instances de clients, de produits, ... Vérifier ensuite le bon déroulement des opérations de gestion de la pharmacie en utilisant ces instances.

:::correction
## Correction

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

