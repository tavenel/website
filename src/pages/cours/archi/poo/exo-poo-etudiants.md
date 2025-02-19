---
title: Exercice - gestion d'étudiants
date: 2023 / 2024
correction: false
---

## Sujet

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
## Correction

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

