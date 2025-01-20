# ~~ Générer les données d'entrée ~~

import numpy as np
import pandas as pd

# Générer des données aléatoires
data = np.random.randint(0, 100, size=(1000, 2))

# Créer un DataFrame pandas à partir de ces données
df = pd.DataFrame(data, columns=['colonne1', 'colonne2'])

# Écrire le DataFrame dans un fichier CSV
df.to_csv("fichier.csv", index=False)


# ~~ Clustering des données ~~

from sklearn.cluster import KMeans
import pandas as pd

# Lire le fichier CSV
data = pd.read_csv("fichier.csv")

# Sélectionner les colonnes à utiliser pour le clustering
X = data[['colonne1', 'colonne2']]

# Initialiser l'algorithme de clustering
kmeans = KMeans(n_clusters=5)

# Entraîner le modèle sur les données
kmeans.fit(X)

# Prédire les clusters des données
predictions = kmeans.predict(X)

# Afficher les résultats
#for i, prediction in enumerate(predictions):
  #print(f"Ligne {i}: cluster {prediction}")


# ~~ Représentation graphique ~~

import matplotlib.pyplot as plt

# Tracer un scatter plot des données
plt.scatter(X['colonne1'], X['colonne2'], c=predictions)

# Tracer un scatter plot des centres de chaque cluster
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')

# Afficher le graphique
plt.show()

