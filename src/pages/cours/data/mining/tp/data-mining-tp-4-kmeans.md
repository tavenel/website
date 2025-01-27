---
title: Data mining - TP 4 - Algorithme k-means des k moyennes
date: 2023 / 2024
---

# Algorithme k-means

## Générer les données d'entrée

Nous allons utiliser des données générées aléatoirement pour cet exercice.

Pour cela :

- Importer les librairies nécessaires (`numpy` pour générer des données aléatoires, et pandas pour écrire le fichier `CSV`).
- Générer des données aléatoires à l'aide de `numpy`.
- Créer un `DataFrame` pandas à partir de ces données aléatoires.
- Utiliser la fonction `to_csv` de pandas pour écrire le `DataFrame` dans un fichier `CSV`.

:::exo
Créer un fichier `CSV` nommé `fichier.csv` contenant 1000 lignes et 2 colonnes de données aléatoires comprises entre 0 et 100.
:::

## Clustering des données

Nous allons maintenant classer ces données en utilisant un algorithme des K-moyennes :

- Importer les librairies nécessaires (`pandas` pour lire le fichier `CSV`, et `scikit-learn` pour l'algorithme de clustering).
- Lire le fichier `CSV` en utilisant `pandas` et stocker les données dans une variable.
- Sélectionner les colonnes à utiliser pour le clustering.

- Initialiser l'algorithme de clustering de `scikit-learn` (`from sklearn.cluster import KMeans`) et entraîner le modèle sur les données en utilisant la fonction `fit`.
- Prédire les cluster des données en utilisant la fonction `predict`.
- Afficher les résultats en utilisant une boucle pour parcourir chaque ligne de données et afficher le cluster prédit.

:::exo
Créez un programme qui lit un fichier `CSV` et effectue un clustering des données à l'aide de la librairie `scikit-learn` en utilisant un algorithme des k-moyennes..
:::

## Représentation graphique

- Importer la librairie `matplotlib`
- Utiliser la fonction `scatter` de `matplotlib` pour tracer un `scatter plot` des données en utilisant les colonnes sélectionnées pour le clustering comme abscisses et ordonnées.
- Utiliser la fonction `scatter` de `matplotlib` à nouveau pour tracer un `scatter plot` des centres de chaque cluster obtenus avec l'algorithme de clustering. Vous pouvez récupérer ces centres en utilisant la propriété `cluster_centers_` de l'objet `kmeans`.
- Afficher le graphique en utilisant la fonction `show` de `matplotlib`.

:::exo
Afficher un `scatter plot` des données en utilisant la colonne 1 comme abscisses et la colonne 2 comme ordonnées.
Les points seront colorés en fonction du cluster prédit par l'algorithme de clustering.
Les centres de chaque cluster seront également affichés en utilisant des marqueurs en forme de croix rouges.
:::

:::exo
- Faire varier le nombre de classes.
- Commenter les résultats obtenus : crédibilité, précision, ...
- Quel semble être le meilleur nombre de classes ?
:::

