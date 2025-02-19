---
title: Data mining - TP 4 - Algorithme k-means des k moyennes
date: 2023 / 2024
---

# Algorithme k-means

## Générer les données d'entrée

Nous allons utiliser des données générées aléatoirement pour cet exercice.

Pour cela :

- Importer les librairies nécessaires (`numpy` pour générer des données aléatoires, et pandas pour écrire le fichier `CSV`).
- Générer des données aléatoires à l'aide de `numpy`.
- Créer un `DataFrame` pandas à partir de ces données aléatoires.
- Utiliser la fonction `to_csv` de pandas pour écrire le `DataFrame` dans un fichier `CSV`.

:::exo
Créer un fichier `CSV` nommé `kmeans.csv` contenant 1000 lignes et 2 colonnes de données aléatoires comprises entre 0 et 100.
:::

:::correction

### Correction

```python
import numpy as np
import pandas as pd

# Générer des données aléatoires
data = np.random.randint(0, 100, size=(1000, 2))

# Créer un DataFrame pandas à partir de ces données
df = pd.DataFrame(data, columns=['colonne1', 'colonne2'])

# Écrire le DataFrame dans un fichier CSV
df.to_csv("kmeans.csv", index=False)
```
:::

## Clustering des données

Nous allons maintenant classer ces données en utilisant un algorithme des K-moyennes :

- Importer les librairies nécessaires (`pandas` pour lire le fichier `CSV`, et `scikit-learn` pour l'algorithme de clustering).
- Lire le fichier `CSV` en utilisant `pandas` et stocker les données dans une variable.
- Sélectionner les colonnes à utiliser pour le clustering.

- Initialiser l'algorithme de clustering de `scikit-learn` (`from sklearn.cluster import KMeans`) et entraîner le modèle sur les données en utilisant la fonction `fit`.
- Prédire les cluster des données en utilisant la fonction `predict`.
- Afficher les résultats en utilisant une boucle pour parcourir chaque ligne de données et afficher le cluster prédit.

:::exo
Créez un programme qui lit un fichier `CSV` et effectue un clustering des données à l'aide de la librairie `scikit-learn` en utilisant un algorithme des k-moyennes..
:::

:::correction
### Correction

```python
from sklearn.cluster import KMeans
import pandas as pd

# Lire le fichier CSV
data = pd.read_csv("kmeans.csv")

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
```
:::

## Représentation graphique

- Importer la librairie `matplotlib`
- Utiliser la fonction `scatter` de `matplotlib` pour tracer un `scatter plot` des données en utilisant les colonnes sélectionnées pour le clustering comme abscisses et ordonnées.
- Utiliser la fonction `scatter` de `matplotlib` à nouveau pour tracer un `scatter plot` des centres de chaque cluster obtenus avec l'algorithme de clustering. Vous pouvez récupérer ces centres en utilisant la propriété `cluster_centers_` de l'objet `kmeans`.
- Afficher le graphique en utilisant la fonction `show` de `matplotlib`.

:::exo
Afficher un `scatter plot` des données en utilisant la colonne 1 comme abscisses et la colonne 2 comme ordonnées.
Les points seront colorés en fonction du cluster prédit par l'algorithme de clustering.
Les centres de chaque cluster seront également affichés en utilisant des marqueurs en forme de croix rouges.
:::

:::exo
- Faire varier le nombre de classes.
- Commenter les résultats obtenus : crédibilité, précision, ...
- Quel semble être le meilleur nombre de classes ?
:::

:::correction
### Correction

```python
import matplotlib.pyplot as plt

# Tracer un scatter plot des données
plt.scatter(X['colonne1'], X['colonne2'], c=predictions)

# Tracer un scatter plot des centres de chaque cluster
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')

# Afficher le graphique
plt.show()
```
:::

