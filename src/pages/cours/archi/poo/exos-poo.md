---
title: Exercices POO
date: 2023 / 2024
correction: false
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

