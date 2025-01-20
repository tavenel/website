def robot_simulation(commandes, obstacles):
    # Initialisation du robot
    x, y = 0, 0  # Position du robot
    direction = (0, 1)  # Direction initiale (vers le nord)
    distance_max_carre = 0  # Distance maximale au carré atteinte

    # Fonction pour calculer la distance euclidienne au carré
    def distance_carre(x1, y1, x2, y2):
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    # Exécution des commandes
    for commande in commandes:
        if isinstance(commande, int):
            # Avancer de n cases
            for _ in range(commande):
                x += direction[0]
                y += direction[1]
                # Vérifier la présence d'obstacles
                if (x, y) in obstacles:
                    # Revenir à la case précédente si un obstacle est rencontré
                    x -= direction[0]
                    y -= direction[1]
                    break
                # Mettre à jour la distance maximale au carré
                distance_max_carre = max(distance_max_carre, distance_carre(x, y, 0, 0))
        elif commande == 'g':
            # Rotation de 90° à gauche
            direction = (-direction[1], direction[0])
        elif commande == 'd':
            # Rotation de 90° à droite
            direction = (direction[1], -direction[0])

    return distance_max_carre

# Exemples d'utilisation
resultat1 = robot_simulation(commandes=[7, 'd', 'd', 4], obstacles=[(0, 5)])
print(resultat1)  # Résultat attendu: 16

resultat2 = robot_simulation(commandes=[4, 'd', 4, 'g', 1, 'd', 2, 'd', 3, 'd', 1], obstacles=[(0, 4), (3, 3)])
print(resultat2)  # Résultat attendu: 32

resultat3 = robot_simulation(commandes=['g', 4, 'd', 3, 'g', 1, 'd', 'd', 5], obstacles=[(-4, 2)])
print(resultat3)  # Résultat attendu: 26

