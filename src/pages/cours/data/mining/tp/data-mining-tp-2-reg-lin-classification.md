---
title: Data mining - TP 2 - Classification par régression linéaire
author: Tom Avenel
date: 2023 / 2024
---

1. Charger les données de test en utilisant la librairie `pandas` :

```python
students = pd.read_csv('students-breakfast.csv')
```

Cet appel charge les différentes colonnes du fichier `csv` dans un objet `students` : par exemple, `students.score` est un objet `Pandas.Series` correspondant à la colonne des scores (cet objet s'utilise de façon similaire à une liste).

2. Afficher le nuage de points : `score` en fonction de `breakfast`.
  - Que remarquez-vous ?

3. Calculer et afficher la moyenne des scores pour les individus :
  a. Ayant consommé un petit déjeuner ;
  b. N'ayant pas consommé de petit déjeuner ;
  c. Que remarquez-vous ?

On pourra utiliser les méthodes `groupby()` et `mean()` de la librairie `pandas` (automatiquement ajoutés à l'objet `students`).

4. Tracer la droite passant par les deux moyennes précédentes.
  - Quelle est votre remarque ?

5. Utiliser la librairie `statsmodels` pour calculer la régression de `score ~ breakfast`
  - Afficher les paramètres du modèle.
  - Quelle est votre conclusion ?

6. Calculer la différence entre les deux moyennes calculées question 3. Que remarquez-vous ?

7. Conclusion : y a-t-il un lien entre la prise d'un petit déjeuner et le score ? Si oui, quelle prédiction nous apporte ce modèle ?
