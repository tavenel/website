import random

class PlusMoinsJeu:
    def __init__(self, borne_inf, borne_sup):
        self.borne_inf = borne_inf
        self.borne_sup = borne_sup
        self.nombre_secret = random.randint(self.borne_inf, self.borne_sup)
        self.essais = []
        self.triche = False

    def est_tricheur(self, proposition):
        for (essai, instruction) in self.essais:
            if ( abs(essai - proposition) <= 1 ) :
                if ( ( essai >= proposition and instruction == '+' ) or (essai <= proposition and instruction == '-') ):
                    return (essai, instruction)
        # Pas de triche détectée
        return False

    def jouer(self):
        print("Mémorisez un nombre entre", self.borne_inf, "et", self.borne_sup, ", je vais essayer de le retrouver")
        print("Appuyez sur <enter> quand vous serez prêt. Et ne trichez pas ensuite...")
        input()

        essai = self.borne_inf + (self.borne_sup - self.borne_inf) // 2
        coup = 1

        while True:
            print("Je propose", essai, "...", end=" ")
            reponse = input("+, -, ou G ?")
            tricheur = self.est_tricheur(essai)
            
            if reponse.lower() == 'g':
                print("J'ai trouvé", essai, "en", coup, "coups !!!")
                return
            elif coup > 1 and tricheur:
                print("Tricheur !!! À la réponse", coup,
                      "il avait été proposé", tricheur[0], "et répondu", tricheur[1],
                      ". En proposant", essai, "la réponse ne peut pas être", reponse, "!!!")
                print("J'ai gagné par forfait en", coup-1, "coups !!!")
                return

            self.essais.append( (essai, reponse) )

            if reponse == '+':
                self.borne_inf = essai + 1
            elif reponse == '-':
                self.borne_sup = essai - 1

            essai = self.borne_inf + (self.borne_sup - self.borne_inf) // 2
            coup += 1

# Exemple d'utilisation
jeu = PlusMoinsJeu(1, 100)
jeu.jouer()

