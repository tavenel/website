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

