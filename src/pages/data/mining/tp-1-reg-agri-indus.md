---
title: Data mining - TP 1 - Régression linéaire
date: 2023 / 2024
---

L'exercice utilise des indices annuels de production agricole (2e ligne) et de production industrielle (3e ligne) relevés entre les années 1944 et 1961.

Nous allons rechercher une éventuelle relation linéaire entre ces deux indices par la méthode des moindres carrés.

|1944|1945|1946|1947|1948|1949|1950|1951|1952|1953|1954|
|----|----|----|----|----|----|----|----|----|----|----|
|100 |60  |76  |74  |90  |93  |102 |98  |103 |110 |117 |
|100 |50  |84  |99  |113 |122 |128 |143 |145 |146 |159 |

|1955|1956|1957|1958|1959|1960|1961|
|----|----|----|----|----|----|----|
|118 |112 |115 |116 |121 |134 |130 |
|172 |188 |204 |213 |220 |242 |254 |

## Saisie des données et tracé des courbes

1. Saisir ces deux suites d'indices sous la forme de deux listes à 18 composantes en tapant les instructions :

```python
agri=[100,60, ...., 134,130]
indu=[100,50, ....,242,254]
```

Vérifier votre saisie en tapant par exemple `agri[7]` ou `indu[14]`.

2. Tracer les courbes des indices annuels de production agricole et de production industrielle en fonction des années.

On utilisera la fonction `plot` de la librairies `matplotlib` :

```python
# Prépare 4 figures ax[0],..,ax[3] pour la suite
fig, ax = plt.subplots(4, 1, figsize=(8, 10)) 
fig.tight_layout()

# Crée un dessin
ax[0].plot(x, y, label='...', color='blue')
ax[0].set(title='...')
ax[0].legend() # Trace les légendes - attention à réaliser cet appel à la fin

plt.show() # Affiche les dessins
```

Il est également possible d'utiliser les instructions `plt.XXX()` directement sans passer par un `subplot` : `plt.plot(x,y)`, ... si l'on travaille sur un seul dessin.

:::correction
```python
import numpy as np
import matplotlib.pyplot as plt

agri = [100, 60, 76, 74, 90, 93, 102, 98, 103, 110, 117, 118, 112, 115, 116, 121, 134, 130]
indus = [100, 50, 84, 99, 113, 122, 128, 143, 145, 146, 159, 172, 188, 204, 213, 220, 242, 254]
n = len(agri)
x = np.arange(start=1944, stop=1962, step=1)

fig, ax = plt.subplots(2, 1, figsize=(8, 10))
fig.tight_layout()

ax[0].plot(x, agri, label='production agricole', color='orange')
ax[0].plot(x, indus, label='production industrielle', color='blue')
ax[0].set(title='Production agricole et production industrielle de 1945 à 1961')
ax[0].legend()
```
:::

## Nuage de points son centre de gravité

3. Calculer les coordonnées du centre de gravité du nuage de points ${x=agri, y=indus}$.
4. Tracer le nuage de points dans un nouveau graphique `ax[1]` :
  - Utiliser l'instruction `plt.scatter()` similaire à `plt.plot()`
  - Tracer le centre de gravité dans le nuage de points.
  - Quelle position occupe le centre de gravité par rapport au nuage ?
  - Si l'on ajoutait le centre de gravité (x, y) comme un 19e point au nuage, quel serait le centre de gravité du nouveau nuage ? Pourquoi ?
5. Quel a priori le nuage de points donne-t-il sur l'existence d'une relation linéaire entre les deux variables ?

:::correction
```python
centre = {'x': sum(agri)/n, 'y': sum(indus)/n}
# ou : 
centre2 = {'x': np.average(agri), 'y': np.average(indus)}
print(f'Centre de gravité : {centre} ou {centre2}')

ax[1].scatter(agri, indus)
ax[1].scatter(centre['x'], centre['y'], color='red', label='Centre de gravité')
ax[1].set(title='Nuage de points : production agricole en fonction de la production industrielle')
ax[1].legend()

plt.show()
```
:::

## Régression linéaire de la production industrielle sur la production agricole

6. En utilisant la méthode des moindres carrés, calculer les coefficients de la droite de régression de la production industrielle sur la production agricole.
  - A quoi correspondent ces coefficients ?
7. Calculer le vecteur des valeurs estimées de la production industrielle pour l'ensemble des années de l'étude.
8. Tracer la droite de régression dans le graphique `ax[1]`.
  - Combien de points du nuage sont situés en dessous de cette droite ?
  - Quelles sont les coordonnées des deux points les plus éloignés en dessous et au dessus de la droite ?

:::correction
```python
a = Cov(X,Y)/Var(X)
b = mean(Y) - a * mean(X)
cov = {'cov_agri_indus': [], 'var_agri': [], 'var_indus': []}
for i in range(18):
    cov['cov_agri_indus'].append( (agri[i] - centre['x']) * (indus[i] - centre['y']) )
    cov['var_agri'].append( (agri[i] - centre['x']) ** 2 )
    cov['var_indus'].append( (indus[i] - centre['y']) ** 2 )

def b(a):
    return centre['y'] - a * centre['x']

a_hat_biais = sum(cov['cov_agri_indus']) / sum(cov['var_agri'])
b_hat_biais = b(a_hat_biais)
print(f'Estimation des paramètres de la régression linéaire (manuellement - avec biais) : a={a_hat_biais} et b={b_hat_biais}')

def reg_lin(a, b):
    return lambda x : a * x + b
reg_indus_agri = reg_lin(a_hat_biais, b_hat_biais)

ax[1].plot(
        agri,
        reg_indus_agri(np.array(agri)),
        color='blue', 
        label='Régression linéaire production industrielle sur production agricole (avec biais)'
        )
```
:::

## Utilisation de la librairie numpy

9. Utiliser la librairie `numpy` pour calculer matrice de covariance de la production industrielle et de la production agricole :

```python
cov_matrix = np.cov(agri, indus)
```

La matrice de covariance, en dimension 2, est une matrice représentant la variance et la covariance de deux variables :

```
( var(x)   |  cov(x,y) )
( cov(x,y) |  var(y)   )
```

10. En déduire les coefficients de la régression linéaire. A-t-on les mêmes valeurs que celles calculées précédemment ?

:::correction
```python
cov_matrix = np.cov(agri, indus)
#cov_matrix = np.cov(agri, indus, bias=True)
# matrice :
# ( var(x)   |  cov(x,y) )
# ( cov(x,y) |  var(y)   )
print('covar matrix :', cov_matrix)
print('var agri', cov_matrix[0][0])
print('covar agri,indus', cov_matrix[0][1])

a_hat2 = cov_matrix[0][1] / cov_matrix[0][0]
b_hat2 = b(a_hat2)
print(f'Estimation des paramètres de la régression linéaire (numpy) : a={a_hat2} et b={b_hat2}')
```
Les valeurs sont différentes - par défaut `numpy.cov()` utilise un estimateur sans biais.
Pour avoir les mêmes valeurs, on aurait pu utiliser : `np.cov(agri, indus, bias=True)`
Mais on préfère utiliser un estimateur non biaisé (ici : $E[X] = Sigma^2*(n-1)/n != Sigma^2$ )
Il faut donc rectifier cet estimateur par un facteur $n/(n-1)$
Voir : <https://en.wikipedia.org/wiki/Bias_of_an_estimator>
:::

## Correction de l'estimateur

La méthode de calcul précédente est biaisée : en utilisant la moyenne des individus de l'étude, nous avons utilisé une estimation de l'espérance de la variable prédite (moyenne statistique des individus de l'étude), et non la valeur exacte de l'espérance (moyenne théorique). On prouve alors que : $E[X] = \frac{n-1}{n}\sigma^2 \neq \sigma^2$ (voir cours).

11. Rectifier l'estimateur précédent en corrigeant le calcul de la covariance d'un facteur $\frac{n}{n-1}$. Le résultat est-il le même qu'en utilisant la librairie `numpy` ?
12. Calculer les nouveaux coefficients de la régression linéaire.

:::correction
```python
a_hat = a_hat_biais * n/(n-1)
b_hat = b(a_hat)
print(f'Estimation des paramètres de la régression linéaire (manuellement - sans biais) : a={a_hat} et b={b_hat}')

reg_indus_agri2 = reg_lin(a_hat, b_hat)

ax[1].plot(
        agri,
        reg_indus_agri2(np.array(agri)),
        color='cyan', 
        label='Régression linéaire idus ~ agri (sans biais)'
        )
```
:::

## Régression linéaire de la production agricole sur la production industrielle

13. Calculer puis tracer la droite de régression de agri sur indu (et non plus de indu sur agri) dans le graphique ax[1]. Utiliser un label et une couleur différente.
  - Les deux droites coincident-elles ? Pourquoi ?
  - Quel est leur point d'intersection ?

:::correction
```python
# Calcul et ajout de la régression agri sur indus :
a2_hat = cov_matrix[0][1] / cov_matrix[1][1] # Cov(indus,agri) / Var(indus)
b2_hat = centre['x'] - a2_hat * centre['y']
print(f'Estimation des paramètres de la régression linéaire (numpy) de agri sur indus : a={a2_hat} et b={b2_hat}')
reg_agri_indus = reg_lin(a2_hat, b2_hat)
ax[1].plot(
        reg_agri_indus(np.array(indus)),
        indus,
        color='orange',
        label='Régression linéaire agri ~ indus'
        )
ax[1].legend()
plt.show()
```
:::

## Étude des résidus

14. Définir un vecteur `res(i), i = 1, ... , 18` dont les composantes sont les résidus (écart entre les valeurs observées et les valeurs prédites).
15. Tracer les résidus dans un troisième graphique `ax[2]`. Ajouter à cette figure, l'axe horizontal (qu'on pourra voir comme le graphe d'une fonction nulle)
  - Que vaut la moyenne des résidus ? Expliquez pourquoi
16. Tracer un histogramme des résidus dans un quatrième graphique `ax[3]`, on pourra utiliser l'instruction `plt.hist()`
  - Cet histogramme valide-t-il le choix du modèle linéaire pour ces données ?

:::correction
```python
pred_indus = [ reg_indus_agri(agri[i]) for i in range(n) ]
pred_agri = [ reg_agri_indus(indus[i]) for i in range(n) ]
resid_indus = [ y - y_ for (y, y_) in zip(indus, pred_indus) ]
resid_agri = [ y - y_ for (y, y_) in zip(agri, pred_agri) ]

fig, ax = plt.subplots(2, 2, figsize=(8, 10))
fig.tight_layout()

ax[0][0].plot(pred_indus, [0 for _ in range(n)], label='y=0', color='green')
ax[0][0].scatter(pred_indus, resid_indus, label='Résidus de indus ~ agri', color='blue')
ax[0][0].set(title='Dispersion des résidus indus ~ agri')
ax[0][0].legend()

ax[0][1].hist(resid_indus, label='Résidus de indus ~ agri', color='blue')
ax[0][1].set(title='Histogrammes des résidus indus ~ agri')
ax[0][1].legend()

ax[1][0].plot(pred_agri, [0 for _ in range(n)], label='y=0', color='green')
ax[1][0].scatter(pred_agri, resid_agri, label='Résidus de agri ~ indus', color='orange')
ax[1][0].set(title='Dispersion des résidus agri ~ indus')
ax[1][0].legend()

ax[1][1].hist(resid_agri, label='Résidus de agri ~ indus', color='orange')
ax[1][1].set(title='Histogrammes des résidus agri ~ indus')
ax[1][1].legend()
plt.show()

print(np.mean(resid_indus)) # ~= 0
print(np.mean(resid_agri)) # ~= 0
```
:::

## Niveau de corrélation linéaire du nuage

17. Calculer le carré du coefficient de corrélation linéaire : $R^2 = \rho^2$.
  - Que peut-on en déduire ?
  - Ce coefficient permet-il de choisir parmi les deux droites de régression l'une plutôt que l'autre ?

:::correction
```python
rau = sum(cov['cov_agri_indus']) / ( (sum(cov['var_agri']) * sum(cov['var_indus'])) ** 0.5)
# ou :
#rau = cov_matrix[0][1] / ((cov_matrix[0][0] * cov_matrix[1][1]) ** 0.5)
print('Rau2', rau ** 2)
```
:::

## Etude de la dispersion du nuage

18. A l'aide des formules données en cours, calculer les dispersions _SST_, _SSR_, _SSE_.
19. Vérifier la formule : $R^2=\frac{SSE}{SST}$ pour ce jeu de données.

:::correction
```python
R2 = sum([ (reg_agri_indus(indus_i) - centre['x']) ** 2 for indus_i in indus ]) / sum([ (agri_i - centre['x']) **2 for agri_i in agri ])
print('R2', R2)
```
:::

## Valeurs observées/valeurs prédites

20. En ne retenant que le premier modèle (celui de la première droite), calculer pour les années 1947 et 1950, les indices de production industrielle prédits par le modèle et les comparer aux indices observées.
  - Commenter les résultats obtenus.
  - Pourrions nous, avec ce modèle prévoir un indice de production industrielle à venir, par exemple celui de 1962 ? Pourquoi ?

:::correction
```python
print('Production industrielle estimée en 1947 :', reg_indus_agri(agri[3]))
print('Production industrielle réelle en 1947 :', indus[3])
print('Rapport :', reg_indus_agri(agri[3]) / indus[3])

print('Production industrielle estimée en 1950 :', reg_indus_agri(agri[6]))
print('Production industrielle réelle en 1950 :', indus[6])
print('Rapport :', reg_indus_agri(agri[6]) / indus[6])
```
:::

## Sensibilité aux valeurs extrêmes

21. On dit que la position de la droite de régression est très sensible par rapport aux valeurs abérantes. Faites une expérience pour illustrer cette affirmation en changeant l'un des indices observés.

:::correction
Changer `indus[3]` à $999$ et observer la détérioration du modèle.
:::

## Utilisation d'un modèle d'apprentissage

Les librairies d'apprentissage automatique proposent un ensemble de modèles permettant d'appliquer automatiquement les algorithmes de data mining. Ces algorithmes sont en général très optimisés en terme de performances en approchant le résultat du théorème mathématique par une méthode analytique - le résultat obtenu peut donc être légèrement différent du résultat théorique.

22. Utiliser la librairie `statsmodels` pour réaliser la régression linéaire.
  - Comparer les résultats obtenus avec la méthode précédente

```python
# Import de la librairie
import statsmodels.api as sm

# Création du modèle : 'indus ~ agri' est une régression
model = sm.OLS.from_formula('indus ~ agri', data = {'agri': agri, 'indus': indus})

# Application du modèle
results = model.fit()

# Affichage des coefficients
print(results.params)
```

23. Utiliser le modèle pour prédire les valeurs de la production industrielle en 1947 et 1950.
  - Comparer les résultats obtenus avec la méthode précédente

```python
newdata = {'agri':[data_1,..,data_n]}
results.predict(newdata)
```

:::correction
```python
import statsmodels.api as sm

# Create the model here:
model = sm.OLS.from_formula('indus ~ agri', data = {'agri': agri, 'indus': indus})
# Fit the model here:
results = model.fit()
# Print the coefficients here:
print(results.params)

# Prédiction de la production industrielle en 1947 et 1950
newdata = {'agri':[74,102]}
pred_indus_1947, pred_indus_1950 = results.predict(newdata)
print(f'Productions industrielles estimées en 1947 : {pred_indus_1947} et 1950 : {pred_indus_1950}')
```
:::

