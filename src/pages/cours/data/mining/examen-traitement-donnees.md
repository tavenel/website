---
title: B2 ESGI - Examen Mathématiques pour le traitement des données (3H)
date: 2023 / 2024
correction: false
---

# Exercice 1 - Questions de cours (3 pts)

1. Qu'est-ce qu'un algorithme d'apprentissage non supervisé ? Quel est l'intérêt d'un tel algorithme, et sa limitation ?
2. Définissez dans vos propres mots ce qu'est un "bon" modèle de data mining en utilisant les termes `prédiction` et `observation`.
3. L'existence d'un "bon" modèle de régression linéaire entre deux variables $X$ et $Y$ implique-t-il un relation de causalité entre $X$ et $Y$ ?

::: {.correction .if correction="true"}
1. Un algorithme d'apprentissage non supervisé est un algorithme qui n'a pas besoin de données d'apprentissage, c'est-à-dire qu'on ne connaît pas d'avance les valeurs possibles de la variable à prédire Y (et donc, à l'inverse d'un algorithme d'apprentissage supervisé, on ne dispose pas de données étiquetées contenant des valeurs de Y pour des valeurs de(s) variable(s) prédictive(s) X). L'intérêt d'un tel algorithme est de ne pas avoir besoin de connaissance du métier pour réaliser l'étiquettage (par exemple, pas besoin d'être médecin pour faire une étude sur une maladie). L'inconvénient est que les résultats peuvent êtres moins précis, et le sens des données de sortie pas toujours facile à expliquer (puisqu'il n'y a plus de sens du métier dans les données - par exemple, segmenter des patients malades en fonction de variables non observables dans la vraie vie).
2. Un bon modèle de data mining est un modèle dont les prédictions ($\hat{Y}$) sont assez proches des observations ($Y$) sans pour autant créer de surapprentissage, c'est-à-dire que les prédictions seront toujours valables pour de nouvelles observations sur la même étude.
3. Non, il peut y avoir corrélation sans causalité : voir [ce lien](https://www.tylervigen.com/spurious-correlations).
:::

# Exercice 2 - Relation prix d'un appartement / surface (5 pts + 1 bonus)

En principe, pour un quartier donné la surface d’un appartement détermine assez bien son prix.

Nous souhaitons donc expliquer le prix en kilo euros en fonction de la surface en $m^2$.

Nous disposons pour cela d'un échantillon $(x_1 , y_1 )$, $(x_2 , y_2 )$, ... , $(x_n , y_n )$ de taille $n = 10$ où $x_i$ représente la surface de l’appartement $i$ et $y_i$ son prix.

Appartement    | 1      | 2      | 3      | 4       | 5      | 6      | 7      | 8      | 9      | 10     |
---------------|--------|--------|--------|---------|--------|--------|--------|--------|--------|--------|
_Prix observé_ | 130.00 | 280.00 | 650.00 | 800.00  | 268.00 | 790.00 | 500.00 | 320.00 | 250.00 | 250.00 |

Pour modéliser la dépendance entre le prix d’un appartement et la surface, nous choisissons le modèle de la régression linéaire simple : pour tout $i = 1, ... , n$ :

$$y_i = b + a x_i + \epsilon_i$$ 

1. Que représentent respectivement les termes $b+ a x_i$ et $\epsilon_i$ dans l’équation ci-dessous ? (0.5pt)
2. Quelle est la méthode qui permet d’estimer les coefficients $a$ et $b$ ? Expliquer très brièvement le principe de cette méthode. (0.5pt)
3. Nous avons ajusté un modèle de régression linéaire simple pour expliquer le prix en fonction de la surface.

Coefficients | Estimation | Erreur 
-------------|------------|--------
a            | 5.353      | 0.414  
b            | -29.466    | 41.245 

R-carré ajusté: 0.8603
Statistique de test du Khi-2 : T=20

(a) Quelle est la variable à expliquer ? Quelle est la variable explicative ? (0.5 pt)
(b) Donner les estimations des coefficients de la régression et préciser leur interprétation. (1 pt)
(c) Donner l’équation de la droite ajustée. (0.5 pt)
(d) Tester la nullité de la pente de la droite de régression en précisant l'hypothèse nulle du test. Que conclure au seuil 5% ? (1.5 pt)
(e) Relever la valeur observée du coefficient de détermination $R^2$ et l’interpréter. (0.5 pt)

4. Expliquer comment on obtient les deux derniers lignes du tableau ci-dessous (_Prix prédit_ et _Résidus_). (1pt)

Appartement    | 1      | 2      | 3      | 4       | 5      | 6      | 7      | 8      | 9      | 10     |
---------------|--------|--------|--------|---------|--------|--------|--------|--------|--------|--------|
_Prix observé_ | 130.00 | 280.00 | 650.00 | 800.00  | 268.00 | 790.00 | 500.00 | 320.00 | 250.00 | 250.00 |
_Prix prédit_  | 120.42 | 238.19 | 537.97 | 1019.75 | 264.96 | 987.64 | 559.38 | 291.72 | 227.49 | 157.89 |
_Résidus_      | 9.58   | 41.81  | 112.03 | -219.75 | 3.04   | -197.64| -59.38 | 28.28  | 22.51  | 92.11  |

::: {.correction .if correction="true"}
1. $b+ a x_i$ est la prédiction de $y$ le prix de l'apartement étant donnée $x$ la surface. $\epsilon_i$ est le résidu, c'est-à-dire la différence entre $y$ observé et $\hat{y}$ prédit pour le prix.
2. On utilise la méthode des moindres carrés, qui permet de minimiser la moyenne des écarts au carré entre les prédictions et les observations.
3.
 a. variable à expliquer = prix du logement / variable explicative = surface du logement
 b. $\hat{a}$ est la pente de la droite de régression, $\hat{b}$ est l'ordonnée à l'origine de cette droite. Si la surface augmente de $1m^2$ alors le prix augmente de $\hat{a}$. Ici $\hat{b}$ correspond au prix d'un appartement de $0m^2$... ce qui n'a pas de sens concret (sert uniquement au calcul).
 c. On déduit de $\hat{a}$ et $\hat{b}$ que : $\hat{Y} = 5.353x -29.466$
 d. Au seuil $1-\alpha = 0.95$, pour une loi du Khi-2 à $n-1 = 9$ degrés de liberté, d'après [la table du Khi-2](https://fr.wikipedia.org/wiki/Loi_du_%CF%87%C2%B2#Table_de_valeurs_des_quantiles) : on rejette $H_0$ ssi $T > 16.92$. Comme $T=20$, on rejette $H_0$ : $a$ n'est pas nulle.
 e. $R^2 = 0.8603 \approx 1$ : il y a une forte corrélation linéaire (donc le modèle de régression linéaire est un bon modèle : le prix prédit depuis la surface de l'appartement explique bien le prix observé).
4. On prédit le prix $\hat{Y}$ depuis la surface en utilisant l'équation de la droite de régression linéaire. On calcule ensuite le résidu qui est la différence entre l'observation et la prédiction : $\epsilon_i = Y_i - \hat{Y}_i$

:::

# Exercice 3 : Régression linéaire sur fossiles de fémur et humérus (6 pts)

On dispose de 5 specimens fossiles d'un animal disparu pour lesquels on possède les mesures de la longueur de leur fémur ($x_i$) et de leur humérus ($y_i$).

1. Compléter le tableau suivant.

i | $x_i$ | $y_i$ | $x_i^2$ | $y_i^2$ | $x_iy_i$
--|-------|------|---------|---------|---------
1 |  38   |  41  |         |         |
2 |  56   |  61  |         |         |
3 |  59   |  70  |         |         |
4 |  64   |  72  |         |         |
5 |  75   |  84  |         |         |

2. Calculer la moyenne $\bar{x}$ et $\bar{y}$ de chaque type d'os.
3. Calculer la variance $Var(x)$ et l'écart-type $\sigma(x)$ des fémurs. Même question pour les humérus.
4. Calculer la covariance de $x$ et $y$.
5. Déterminer, par la méthode des moindres carrés ordinaires, l'équation de la droite de régression de $y$ sur $x$.
6. Cette droite passe-t-elle par le centre de gravité ? Faites les calculs et expliquez pourquoi on obtient ce résultat.
7. Calculer le coefficient de corrélation linéaire. Commenter.
8. Calculer la longueur prédite par ce modèle pour l'humérus d'un spécimen dont le fémur mesurerait 50cm.

::: {.correction .if correction="true"}
4. $cov(x,y) = 171.36$
5. $\hat{y} = 1.175x - 3.019$
6. Oui : le centre de gravité est le point central du nuage - c'est l'individu qui représente le mieux la population. La droite passe donc par ce point car elle minimise les écarts à la moyenne.
7. $R^2 = 0.99 \approx 1$ : la corrélation linéaire est très forte donc la taille d'un humérus est presque entièrement corrélée (et donc décrite) depuis la taille d'un fémur par régression linéaire.
8. 55.73cm
:::

# Exercice 4 : Couleur d'un fruit : proches voisins (3 pts)

On cherche à prédire la couleur d’un fruit en fonction de sa largeur (L) et de sa hauteur (H).

On dispose des données d’apprentissage suivantes :

largeur | hauteur | couleur
--------|---------|--------
2       | 6       | red
5       | 6       | yellow
2       | 5       | orange
6       | 5       | purple
1       | 2       | red
4       | 2       | blue
2       | 1       | violet
6       | 1       | green

L’objectif est d'étudier l'influence des voisins sur la propriété de couleur d'un fruit.

Soit $U$ le nouveau fruit de largeur $L = 1$, et de hauteur $H = 4$.

1. Quelle est sa couleur si l'on considère 1 voisin ?
2. Quelle est sa couleur si l'on considère 3 voisins ?
3. Plutôt que le vote majoritaire pour déterminer la classe d'arrivée, on voudrait considérer le vote des voisins pondérés par la distance.
   Chaque voisin vote selon un poids $w$ inversement proportionnel au carré de sa distance : $w = 1/d^2$.
   On prend 3 voisins, quelle est la couleur de $U$ ? Comparez vos résultats à ceux de la question 2.

::: {.correction .if correction="true"}
1. et 2. Voir cours - application directe de k-NN
3. Plutôt qu'un vote majoritaire (chaque élément a un poids = 1), on utilise le poids dans le vote de la classe finale. Ainsi pour $k = 3$ proches voisins, si l'on a 2 éléments dans la classe rouge $x_1$ et $x_2$ et un élément dans la classe orange $x_3$ le vote de la classe orange vaudra $vote_{orange}=w_{x_3}=\frac{1}{d_{x_3}^2}$ et $vote_{rouge}=w_{x_1} + w_{x_2}=\frac{1}{d_{x_1}^2} + \frac{1}{d_{x_2}^2}$. Il est alors possible que $vote_{orange} > vote_{rouge}$ même si il y a plus d'éléments rouges proches voisins que d'éléments oranges : la distance permet de pondérer le nombre d'individus (on préfère donc être très proche de quelques individus d'une classe plutôt que d'être un peu proche mais plus éloigné quand même de pleins d'individus d'une autre classe).
:::

# Exercice 5 : centres mobiles (3 pts)

Dans une étude industrielle, on a étudié 2 caractères : $X_1$ et $X_2$, sur 6 individus $w_1$, ... , $w_6$.

Les données recueillies sont :

Individu | $X_1$ | $X_2$
---------|-------|------
$w_1$    |   -2  | 2
$w_2$    |   -2  | -1
$w_3$    |   0   | -1
$w_4$    |   2   | 2
$w_5$    |   -2  | 3
$w_6$    |   3   | 0

Faire une classification par la méthode des centres mobiles en utilisant un algorithme des k-moyennes avec pour centres initiaux : $c_0^1$ de coordonnées $(-1; -1)$ et $c_0^2$ de coordonnées $(2;3)$.

On arrêtera l'algorithme lorsque cela sera jugé nécessaire (en justifiant).

::: {.correction .if correction="true"}
Voir cours - application directe de k-means
:::
