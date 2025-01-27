---
title: Data mining - TP 5 - Algorithme k-NN des proches voisins
date: 2023 / 2024
---

# Classification k-NN de bouteilles de vin

## Exploration du dataset

1. Importer le dataset `wine` et explorer son contenu :

```python
from sklearn import datasets

# Chargement du dataset
wine = datasets.load_wine()

# Affichage des colonnes
print(wine.feature_names)

# Classes cibles de l'algo k-NN
print(wine.target_names) 

# Afficher les 5 premières données
print(wine.data[0:5])

# Clustering des données d'apprentissage (données labellisées)
print(wine.target)
```

2. Séparer les données d'apprentissage et de test : 70% d'apprentissage et 30% de test.

3. Initialiser l'algorithme k-NN pour k=5

```python
from sklearn.neighbors import KNeighborsClassifier
KNeighborsClassifier(n_neighbors=5)
```

4. Entraîner le modèle

5. Prédire les classifications des données de test en utilisant le modèle

6. Calculer la précision du modèle

7. Même question pour k=7. Que peut-on en déduire ?
