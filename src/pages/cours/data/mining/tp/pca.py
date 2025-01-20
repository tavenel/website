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

