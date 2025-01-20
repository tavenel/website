# Import des librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Charger les données CSV
website = pd.read_csv('exam-browsers.csv')

# En utilisant la méthode `head()` du dataset `pandas` chargé, afficher les 5 premières lignes
print(website.head())

# Afficher un nuage de points (_scatter plot_) de temps ~ age
plt.scatter(x = 'age', y = 'time_seconds', data = website, color='black')

# Graphiquement, peut-on s'attendre à une corrélation linéaire ? Pourquoi ?
# >Oui car les données semblent s'aglomérer autour d'une droite - cependant le nuage de points est assez éparpillé (mauvaise corrélation linéaire ?)

# Afficher le graphique
#plt.show()
# Effacer le graphique (utiliser `plt.clf()`)
plt.clf()

# Utiliser un modèle de régression linéaire pour prédire `time_seconds` depuis `age`
model = LinearRegression()
model.fit(website[['age']],website[['time_seconds']])
# Afficher les coefficients du modèle de régression linéaire
print('a:',model.coef_)
print('b:',model.intercept_)

# Tracer sur le même graphique, le nuage de points temps ~ age et la droite de régression linéaire
plt.scatter(x = 'age', y = 'time_seconds', data = website, color='black')
plt.plot(website[['age']], model.intercept_ + model.coef_*website[['age']], color='blue')

# Graphiquement, la droite de régression semble-t-elle bien approcher le modèle ? Pourquoi ?
# >Oui car elle traverse le nuage et semble séparer équitablement les données

#plt.show()
plt.clf()

# Calculer les prédictions du modèle pour toutes les valeurs de `age`
#predict = [ model.intercept_[0] + model.coef_[0][0] * x for x in website['age'] ]
# ou simplement :
predict = model.predict(website[['age']])

# Afficher sur le même graphe :
# - Le nuage de points temps ~ age
# - La droite de régression linéaire
# - Les prédictions du modèle pour toutes les valeurs de age
plt.scatter(x = 'age', y = 'time_seconds', data = website, color='black')
plt.plot(website[['age']], model.intercept_ + model.coef_*website[['age']], color='blue')
plt.scatter(website[['age']], predict, color='red')

#plt.show()
plt.clf()

# Calculer les résidus de la prédiction. On pourra utiliser le générateur Python suivant : `resid = [ f(y, y_) for (y, y_) in zip([x for x in website['time_seconds'] ], predict) ]` où `f(y, y_)` est une fonction permettant de calculer le résidu depuis `y` et `y_`
resid = [ y - y_ for (y, y_) in zip([x for x in website['time_seconds'] ], predict) ]

# Afficher les résidus en fonction de l'âge. Le résultat vous semble-t-il correct graphiquement ?
plt.scatter(website[['age']], resid)
# >Graphiquement, le nuage de points semble bien dispersé => on veut un résidu aléatoire sans corrélation, cela semble possible

#plt.show()
plt.clf()

# Afficher l'histogramme des résidus - que remarque-t-on ? Que peut-on en conclure quand au modèle ?
plt.hist(resid)
# >Les résidus suivent une distribution normale : c'est attendu pour un bruit aléatoire. On en déduit que le modèle de régression linéaire peut effectivement être utilisé

#plt.show()
plt.clf()

# En utilisant la fonction `metrics.r2_score`, calculer le coefficient de corrélation linéaire. Que peut-on en déduire ? https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html
print(metrics.r2_score(website['time_seconds'], predict))
# >r2 = 0.51 << 1 : la corrélation linéaire n'est pas très bonne (le modèle ne prévoit pas le temps de manière très précise).

# Prédire le temps de visite moyen d'un utilisateur de 40 ans. Discuter le résultat. On pourra utiliser : `np.array([ma_valeur]).reshap(1, -1)` pour générer une matrice à 1 donnée `ma_valeur` en valeur prédictive.
pred_40 = model.predict(np.array([40]).reshape(1, -1))
print(pred_40)
# >pred_40 = 406s = 6min46s => On peut supposer qu'une personne de 40 ans passera environ 7 minutes sur le site Web (vue la précision toute relative du modèle : R2 pas énorme, il faut s'attendre à un écart potentiellement assez important).

