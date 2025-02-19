---
title: Data mining - TP 6 - Autres algorithmes
date: 2023 / 2024
---

# DBScan

```python
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
```

# CART

```python
from sklearn import datasets
from sklearn import tree

# Charger les données iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Créer et entraîner le modèle CART
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

# Faire une prédiction pour une fleur d'iris
prediction = clf.predict([[5.1, 3.5, 1.4, 0.2]])
print(prediction)


#Dans cet exemple, nous utilisons les données Iris fournies par scikit-learn pour entraîner un modèle CART, puis nous utilisons ce modèle pour prédire la classe d'une fleur d'iris particulière (en utilisant ses mesures de sépale et de pétale).
#Note: Il est important de noter que pour des raisons de simplicité, l'arbre de décision n'est pas limité en profondeur, il peut donc causer un surapprentissage. Il est recommandé de limiter la profondeur de l'arbre ou d'utiliser une technique de validation croisée pour éviter cela.
```

# PCA

```python
# Ce code charge les données Iris, une base de données populaire pour les exemples d'apprentissage automatique. Il utilise ensuite les données pour instancier un objet PCA, et ensuite il applique l'algorithme PCA aux données en utilisant les méthodes fit_transform. Il affiche ensuite les composantes principales obtenues, l'explication de la variance des composantes principales et les composantes principales.
#
# Il est important de noter que l'analyse en composantes principales est souvent utilisée pour la visualisation de données et la réduction de dimensions. Il est donc souvent utilisé en combinaison avec d'autres techniques d'apprentissage automatique ou de visualisation pour obtenir des résultats utiles.

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

# Chargement des données Iris
iris = load_iris()
iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

# Instanciation d'un objet PCA
pca = PCA(n_components=2)

# Appliquer l'algorithme PCA aux données
principal_components = pca.fit_transform(iris_df.drop("target", axis=1))

# Afficher les composantes principales obtenues
print(principal_components)

# Affichage de l'explication de la variance des composantes principales
print(pca.explained_variance_ratio_)

#Affichage des composantes principales
print(pca.components_)
```

# LabelEncoder

```python
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
enc.fit(data['Regime'])
data['RegimeN'] = enc.transform(data['Regime'])
```

