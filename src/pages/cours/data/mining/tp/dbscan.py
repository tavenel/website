from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Génération de données de test
# `make_moons` est une fonction de génération de données fournie par scikit-learn, elle génère des données bidimensionnelles qui ressemblent à des lunes ou des demi-cercles.
# Elle prend en entrée deux paramètres principaux :
#- n_samples: le nombre de points à générer
#- noise : le taux de bruit à ajouter aux données générées, cela permet d'ajouter une certaine incertitude aux données de sorte que les points ne soient pas parfaitement alignés sur les demi-cercles.
# Ces données sont généralement utilisées pour tester les algorithmes de clustering, car elles ont une structure de données complexe qui nécessite un regroupement efficace pour être correctement reconnue.
X, y = make_moons(n_samples=200, noise=0.05)

# Initialisation et entraînement du modèle DBSCAN
#Vous pouvez jouer avec les paramètres eps et min_samples pour voir comment ils affectent les résultats de regroupement.
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan.fit(X)

# Prédiction des clusters
labels = dbscan.labels_

# Visualisation des résultats
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()

