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
