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
