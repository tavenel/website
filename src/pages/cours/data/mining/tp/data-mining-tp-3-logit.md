---
title: Data mining - TP 3 - Régression logistique
date: 2023 / 2024
---

# Modèle de régression linéaire

1. Utiliser la librairie `pandas` pour charger les données `students_hours_exam.csv`.
  - Que représentent ces données ?
  - On ne tiendra pas compte de la variable `practice_test` jusqu'à la partie III.

2. Tracer le nuage de points : `passed_exam ~ hours_studied`
  - On pourra utiliser l'instruction `plt.xlim(-1, 25)` pour rendre le graphique plus lisible

3. Réaliser un modèle de régression linéaire. On utilisera la librairie d'apprentissage automatique `sklearn` :

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(students[['variable prédictive']],students[['variable prédite']])
```

4. Tracer la droite de la régression linéaire en calculant les valeurs prédites par le modèle pour les points suivants (300 points de -16.65 à 33.35) :

```python
# reshape transforme la ligne en colonne
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
predictions = model.predict(sample_x)
```

5. En déduire graphiquement la probabilité de succès à l'examen dans les cas suivants :
  a. Aucune révision (heures : 0)
  b. Révision moyenne (heures : 10)
  c. Révision studieuse (heures : 30)

6. Quelle est votre conclusion quand à ce modèle ?

# Modèle de régression logistique simple

## Application du modèle

1. Utiliser un modèle de régression logistique sur les données :

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
```

2. Calculer un ensemble de prédictions en utilisant ce modèle et tracer la courbe associée :

```python
sample_x = np.linspace(-16.65, 33.35, 300).reshape(-1,1)
probability = model.predict_proba(sample_x)[:,1]
```

3. En déduire graphiquement la probabilité de réussite pour 5 heures de révision. Que pensez-vous de ce modèle ?

## Calcul du log-likelyhood

Rappel : le modèle de régression logistique suppose :

$$logit = ln\left(\frac{p}{1-p}\right) = \sum_{j=1}^{p} \beta_j\ X_{ij}$$

4. En utilisant les paramètres du modèle stockés dans `model.coef_` et `model.intercept_`, calculer le résultat de la fonction `logit` pour chacune des valeurs.
  - Attention à bien respecter les caractères `_`
  - En Python, il est possible de réaliser des opérations directement sur des vecteurs (sans passer par une boucle `for`) en utilisant des opérateurs standard : `*`, `+`, ...
  - On pourra utiliser la fonction `np.log()` pour calculer un logarithme.

5. En déduire la formule permettant de calculer la probabilité de succès en utilisant ce modèle.

6. Calculer le vecteur des probabilités pour toutes les données `hours_studied`.
  - On pourra utiliser la fonction `np.exp()` pour calculer un exponentiel.

7. En déduire la probabilité prédicte par le modèle de réussite après 5H de révision.

# Régression logistique généralisée

Nous allons maintenant utiliser toutes les données d'apprentissage afin de réaliser une régression généralisée en utilisant un ensemble de variables.

1. Séparer les données des variables prédictives `hours_studied` et `practice_test` des données de la variable labellisée (à prédire) `passed_exam` :

```python
X = students[['hours_studied', 'practice_test']]
y = students.passed_exam
```

2. Le modèle de régression logistique ne peut travailler que sur des données normalisées, i.e. $\mu = 0$ et $\sigma = 1$. Normaliser les données d'apprentissage avant de les utiliser (cela évite qu'une variable prenne trop de poids par rapport à une autre) :

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
```

3. Séparer les données d'entrée en données d'apprentissage et données de test :
  - Les données d'apprentissage sont fournies uniquement en entrée de l'algorithme et permettent à celui-ci de générer un modèle.
  - Les données de test permettent de valider la bonne exécution du modèle.

<!-- ![](https://cdn-coiao.nitrocdn.com/CYHudqJZsSxQpAPzLkHFOkuzFKDpEHGF/assets/static/optimized/rev-85bf93c/wp-content/uploads/2022/05/machine-learning-process_train-and-test.png) -->

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 27)
```

4. Réaliser une régression logistique généralisée en utilisant la méthode `model.fit(features, labels)` de la classe `LogisticRegression`. Cette méthode prend en paramètres :
  a. Les données d'apprentissage des variables prédictives ;
  b. Les données d'apprentissage labellisées.

5. Afficher les paramètres du modèle : la valeur `result.intercept_` (constante de la régression) et le vecteur `result.coef_` (vecteur des coefficients.
  - Les coefficients sont-ils positifs ou négatifs ? Qu'en déduit-on ?
  - Que peut-on conclure de la valeur de ces coefficients ?
  - Quelle variable est la plus importante pour la réussite d'un examen ?

6. Utiliser la méthode `predict()` du modèle pour prédire le succès ou l'échec pour les données de test.

7. Utiliser la méthode `predict_proba()` du modèle pour prédire la probabilité de succès ou d'échec pour les données de test.
  - Le résultat est une matrice affichant la probabilité de succès dans la 1ere colonne et la probabilité d'échec dans la 2e colonne.

8. Comparer les données prédites aux données de test labellisées.
  - Y a-t-il des erreurs ?
  - Si oui, sont-elles graves ?
  - Conclure : le modèle est-il intéressant ?

## Changement de threshold

L'algorithme de prédiction logistique est un algorithme non paramétrique. Cependant, il est possible de simuler un paramètre en utilisant une valeur spéciale pour classer nos données de succès et d'échec.

Par défaut, `sklearn` utilise un _threshold_ de 0.5, c'est-à-dire que toute prédiction ayant une probabilité supérieure à 0.5 est considérée comme un succès.

![](https://content.codecademy.com/programs/data-science-path/logistic-regression/Threshold-01.svg)

_Un threshold de 0.5 (défaut)._

Or le besoin peut ne pas être symétrique - dans l'exemple précédent par exemple, on peut préférer augmenter les chances de détecter la maladie, quitte à augmenter les faux positifs (détection positive pour des personnes saines) :

![](https://content.codecademy.com/programs/data-science-path/logistic-regression/Threshold-02.svg)

_Un threshold de 0.4_


9. Modifier le threshold de succès pour les prédictions des valeurs de tests pour mieux coller aux données.

On utilisera l'instruction suivante :

```python
# [:,1] sélectionne uniquement la 2e colonne de la matrice
# astype(int) transforme les booléens en entiers
(model.predict_proba(donnees_test)[:,1]>=threshold).astype(int)) 
```

10. Quel threshold permet d'avoir un modèle correct pour toutes les données de test ?

## Précision de la prédiction

### Matrice de confusion

La matrice de confusion permet de représenter facilement la qualité de la régression.

Étant donné deux vecteurs de données prédites `y_pred` et de données mesurées `y_true` :

```python
y_true = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
y_pred = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
```

La matrice de confusion affiche : le nombre de vrai positifs, de faux positifs, de vrais négatifs et de faux négatifs.

Elle est facile à calculer à la main mais il est encore plus simple d'utiliser la fonction intégrée de `sklearn` :

```python
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_true, y_pred))
```

11. Quelle est la matrice de confusion de notre exemple (pour un threshold de 0.5) ?

### Statistiques

Pour chacune de ces métriques, une valeur proche de 1 correspond à un bon modèle de prédiction (et inversement si proche de 0).

Le calcul des métriques est détaillé ci-dessous (avec V = vrai, F = faux, P = positif, N = négatif) :

- Accuracy = (VP + VN)/(VP + FP + VN + FN)
- Precision = VP/(VP + FP)
- Recall = VP/(VP + FN)
- F1 score: moyenne pondérée de la précision et du recall

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
accuracy_score(y_true, y_pred)
precision_score(y_true, y_pred)
recall_score(y_true, y_pred)
f1_score(y_true, y_pred)
```

12. Calculer les statistiques _accuracy_ et _F1_ du modèle. Que peut-on en déduire sur la précision du modèle ?
