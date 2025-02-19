---
title: Examen Data mining
date: 2023 / 2024
---

# Présentation des données

Un dataset nommé `exam-browsers.csv` contient les observations d'un échantillon de visiteurs sur un site Web : temps passé en secondes sur le site web (`time_seconds`), âge (`age`), information sur le navigateur : `Chrome` ou `Safari` (`browser`).

`time_seconds`|`age`|`browser`
--------------|-----|--------
486.0|47.1|Safari
645.7|64.6|Chrome
345.0|45.4|Safari
413.4|34.4|Chrome
426.4|31.3|Safari
242.1|37.5|Safari
439.5|28.8|Chrome
365.9|35.2|Safari
276.5|43.4|Safari
548.9|64.2|Chrome
537.9|41.6|Chrome
379.4|38.9|Safari
384.7|45.8|Chrome
612.5|62.4|Chrome
268.7|25.3|Safari
251.5|41.2|Safari
448.0|34.5|Chrome
414.7|39.5|Chrome
538.2|43.5|Chrome
371.9|39.6|Safari
253.7|31.9|Safari
208.8|28.7|Safari
303.6|43.0|Safari
559.6|52.7|Chrome
435.4|54.8|Safari
523.4|44.8|Chrome
479.2|50.2|Safari
445.5|49.5|Chrome
397.6|34.3|Chrome
456.7|49.9|Safari
389.7|32.6|Safari
361.4|40.9|Chrome
277.1|20.5|Safari
384.6|36.1|Safari
474.8|61.3|Chrome
468.7|41.4|Chrome
509.3|39.8|Chrome
452.4|43.3|Chrome
557.4|49.4|Safari
388.1|57.4|Safari
535.7|54.3|Chrome
454.5|43.5|Safari
489.9|46.2|Safari
292.7|26.2|Safari
561.7|40.7|Chrome
536.1|47.6|Chrome
321.3|48.2|Chrome
271.9|28.2|Safari
571.1|47.4|Chrome
349.3|42.2|Safari
508.4|46.6|Chrome
630.1|67.2|Chrome
535.2|57.8|Safari
386.2|26.6|Safari
456.3|45.9|Safari
565.0|60.5|Safari
429.8|56.6|Safari
575.4|50.1|Chrome
578.1|66.5|Safari
374.5|42.8|Chrome
637.0|56.8|Chrome
619.7|53.8|Chrome
585.6|34.5|Chrome
575.4|48.9|Safari
259.9|17.5|Safari
553.4|60.5|Safari
476.7|50.0|Chrome
412.1|51.2|Safari
477.6|51.1|Chrome
440.8|40.7|Safari
386.5|29.2|Safari
418.7|42.2|Chrome
501.1|53.2|Safari
542.0|46.2|Safari
505.9|55.9|Safari
267.9|30.7|Safari
492.8|48.2|Chrome
385.1|43.5|Safari
421.1|57.8|Safari
486.2|55.7|Chrome
284.4|41.6|Safari
390.6|44.7|Safari
498.2|56.0|Chrome
332.9|36.5|Chrome
358.4|34.8|Safari
247.4|32.1|Chrome
414.4|45.6|Chrome
394.3|39.5|Safari
399.3|35.4|Safari
444.3|38.1|Chrome
451.9|54.5|Chrome
248.2|30.0|Safari
415.5|53.7|Chrome
437.3|44.9|Chrome
713.6|80.7|Chrome
456.7|43.5|Chrome
619.1|60.2|Chrome
364.3|45.1|Safari
385.3|23.4|Safari
271.7|38.6|Safari

# Exercice 1 : Régression linéaire (15 pts)

_Dans cet exercice, nous allons tenter de prédire le temps passé sur le site web en fonction de l'age de l'individu par une régression linéaire._

1. Charger les données `CSV` en utilisant la librairie `pandas`.
2. En utilisant la méthode `head()` du dataset `pandas` chargé, afficher les 5 premières lignes.
3. Afficher un nuage de points (`scatter plot`) de temps ~ age.
4. Graphiquement, peut-on s'attendre à une corrélation linéaire ? Pourquoi ?
5. Utiliser un modèle de régression linéaire pour prédire `time_seconds` depuis `age`.
6. Afficher les coefficients du modèle de régression linéaire.
7. Tracer sur le même graphique, le nuage de points temps ~ age et la droite de régression linéaire.
8. Graphiquement, la droite de régression semble-t-elle bien approcher le modèle ? Pourquoi ?
9. Calculer les prédictions du modèle pour toutes les valeurs de `age`.
10. Afficher sur le même graphe :
  - Le nuage de points temps ~ age
  - La droite de régression linéaire
  - Les prédictions du modèle pour toutes les valeurs de age
11. Calculer les résidus de la prédiction. On pourra utiliser le générateur Python suivant : `resid = [ f(y, y_) for (y, y_) in zip([x for x in website['time_seconds'] ], predict) ]` où `f(y, y_)` est une fonction permettant de calculer le résidu depuis `y` et `y_`.
12. Afficher les résidus en fonction de l'âge. Le résultat vous semble-t-il correct graphiquement ?
13. Afficher l'histogramme des résidus - que remarque-t-on ? Que peut-on en conclure quand au modèle ?
14. En utilisant la fonction `metrics.r2_score`, calculer le coefficient de corrélation linéaire. Que peut-on en déduire ? Voir : <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html>
15. Prédire le temps de visite moyen d'un utilisateur de 40 ans. Discuter le résultat. On pourra utiliser : `np.array([ma_valeur]).reshap(1, -1)` pour générer une matrice à 1 donnée `ma_valeur` en valeur prédictive.

# Exercice 2 : Classification k-NN (5 pts)

_Nous allons maintenant tenter de réaliser une classification k-NN en utilisant l'age et le navigateur (_browser_)._

0. Utiliser un encodeur (`from sklearn.preprocessing import LabelEncoder`) pour encoder les données `browser` en `browserN` (données numériques) :
   ```python
   enc = LabelEncoder()
   enc.fit(website['browser'])
   website['browserN'] = enc.transform(website['browser'])
   ```

1. Afficher un nuage de points : `browserN` ~ `age`
2. Quelle prédiction est-on en train de réaliser en utilisant un algorithme k-NN ?
3. En utilisant 25% de données de test, prédire la classification pour le jeu de test. On utilisera `k=3`.
4. Répéter le même algorithme plusieurs fois et calculer à chaque fois la précision du modèle. Qu'observe-t-on ? Pourquoi ? Conclure sur la précision du modèle.
5. Prédire le résultat pour `age=40`. Que veut dire ce résultat ?
6. Faire varier la valeur de paramètre `k` de 3 à 7. Que remarque-t-on ?
7. Bonus: quel est le temps moyen passé sur le site par les utilisateurs de Chrome et ceux de Safari ?

:::correction
# Correction

```python
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
```
:::

:::correction

# Correction - 2

```python
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
```
:::

