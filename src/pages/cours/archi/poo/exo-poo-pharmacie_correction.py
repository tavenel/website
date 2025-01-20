'''
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
'''

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
