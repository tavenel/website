---
title: Projet Data mining - fouille de données
date: 2023 / 2024
---

# Fouille de données inconnues

L'objectif de ce projet à réaliser en binôme est de réaliser une fouille sur des données inconnues pour en extraire de l'information.

En annexe de ce document est fourni un fichier `CSV` de données.

Aucune information n'est connue sur ces données. En binôme, votre travail consiste, par le biais d'algorithmes de data mining bien choisis, à essayer d'extraire de l'information de ces données.

Pour cela :

1. Commencer par analyser les données : analyse du contenu du fichier, représentation graphique, ... Que peut-on en déduire sur les données ? Quels choix d'algorithmes semblent justifiés pour la suite ? Lesquels sont à écarter ? Pourquoi ?
2. Réaliser une fouille de données en utilisant plusieurs algorithmes bien choisis vus en cours de data mining. On expliquera pourquoi ces algorithmes ont été choisis, on détaillera leur utilisation et les essais réalisés, qu'ils soient fructueux ou non. Pour chaque algorithme, on fera une conclusion de l'analyse.
3. Conclure la fouille de données : qu'avez-vous découvert comme information sur les données ?

:::correction
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data-to-find.csv')

X_known = [],[]
X_unknown = [],[]
Y = []
for i in range(len(data['col1'])):
    if not pd.isna(data['col2'][i]): # il y a une donnée
        X_known[0].append(data['col0'][i])
        X_known[1].append(data['col1'][i])
        Y.append(data['col2'][i])
    else:
        X_unknown[0].append(data['col0'][i])
        X_unknown[1].append(data['col1'][i])

#print(X_unknown[0])
#print(data)
#print(len(X_known[0]))

plt.scatter(X_known[0], X_known[1], c=Y)
plt.scatter(X_unknown[0], X_unknown[1], c='red')
plt.show()
plt.clf()


from sklearn.model_selection import train_test_split

## Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(np.asarray(X_known).T, Y, test_size=0.3) # 70% training and 30% test

from sklearn.neighbors import KNeighborsClassifier

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# On prédit maintenant les classes manquantes
y_pred2 = knn.predict(np.asarray(X_unknown).T)

plt.scatter(X_known[0], X_known[1], c=Y)
plt.scatter(X_unknown[0], X_unknown[1], c=y_pred2)
plt.show()
```
:::

