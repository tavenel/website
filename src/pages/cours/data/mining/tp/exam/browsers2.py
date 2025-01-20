import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

website = pd.read_csv('exam-browsers.csv')

# Utiliser un encodeur (`from sklearn.preprocessing import LabelEncoder`) pour encoder les données `browser` en `browserN` (données numériques) : # ```python
# enc = LabelEncoder()
# enc.fit(website['browser'])
# website['browserN'] = enc.transform(website['browser'])
# ```
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
enc.fit(website['browser'])
website['browserN'] = enc.transform(website['browser'])

# Afficher un nuage de points : `browserN` ~ `age`
plt.scatter(website[['age']], website[['browserN']])
#plt.show()

preds = []
accuracy = []
for i in range(20):
    # Séparer les données en données d'apprentissage (75%) et données de test (25%)
    X_train, X_test, y_train, y_test = train_test_split(website[['time_seconds']], website[['browser']], test_size=0.25) # 75% training and 25% test
    
    accu_i = []
    pred_i = []
    for j in range(3,8):
        # Utiliser un algorithme k-NN (k=3). Quelle classification est-on en train de réaliser ?
        # >On cherche la classe `browser` (`Chrome` ou `Safari`) des données
        knn = KNeighborsClassifier(n_neighbors=j)
        knn.fit(X_train, y_train)
        
        # Prédire la classification pour le jeu de test et calculer la précision du modèle. Que peut-on en déduire ?
        y_pred = knn.predict(X_test)
        accu_i.append( metrics.accuracy_score(y_test, y_pred) )
        # Prédire la classification pour age=40. Que veut dire ce résultat ?
        pred_i.append( knn.predict(np.array([40]).reshape(1, -1))[0] )
    accuracy.append(accu_i)
    preds.append(pred_i)

#print("Accuracy:", np.mean(accuracy), "from : ", accuracy)
#print("Pred 40:", preds)

# Faire varier la valeur du paramètre `k` de 3 à 7. Que remarque-t-on ?
# Répéter l'algorithme plusieurs fois - que remarque-t-on ?
#> La double boucle sert à calculer directement :
#> 20x le même algorithme `for i in range(20)`
#> Pour chaque essai, toutes les prédictions pour `k` allant de 3 à 7
#> Ici, quelque soit la valeur de k, on prédit toujours que le navigateur sera Safari.
#> Pour plusieurs essais avec `k` fixe, la précision varie : c'est normal, on choisit de garder aléatoirement 25% de données de test, mais pas toujours les mêmes !
#> Globalement, on a une précision d'environ 60% : On peut donc prédire qu'un utilisateur de 40 ans a environ 60% de chances d'utiliser Safari (d'après k-NN).


# Bonus : quel est le temps moyen passé sur le site pour chaque navigateur ?
np.mean([ t for (t,b) in zip(website['time_seconds'], website['browser']) if b == 'Safari' ])
# >391 : En moyenne, un utilisateur de Safari passe 391 secondes sur le site web
np.mean([ t for (t,b) in zip(website['time_seconds'], website['browser']) if b == 'Chrome' ])
# >490 : En moyenne, un utilisateur de Chrome passe 490 secondes sur le site web
