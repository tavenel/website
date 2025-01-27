---
title: Estimateur de Kaplan-Meier
---

## Récupérer les données statistiques

Le but de cet exercice est de réaliser une simulation d'un estimateur de Kaplan-Meier <https://fr.wikipedia.org/wiki/Estimateur_de_Kaplan-Meier>.

1. Télécharger le fichier `kaplan-meier.csv` contenant des entrées statistiques au format `CSV` (lignes séparées par des sauts de ligne et colonnes séparées par des virgules `,`) et le placer dans votre répertoire de travail.
  Ces données correspondent à des individus d'une population statistique et contiennent les informations suivantes : `initial` (champ 1), `final` (champ 2), `identifiant` (champ 3).
2. Écrire une fonction qui lit le contenu de ce fichier et retourne une liste d'individus créées depuis ces données.
  Chaque individu sera représenté par un dictionnaire au format ci-dessous (tous les champs sont des entiers). On pourra utiliser la fonction `split` pour séparer les colonnes d'une ligne.

  ```
  { 'initial': 1e colonne, 'final': 2e colonne, 'identifiant': 3e colonne } 
  ```

## Calcul de la durée

Les données `initial` et `final` correspondent aux jours d'études sur l'individu (par exemple, le 1er individu a été étudié du jour 49 au jour 79).

3. Écrire une fonction qui modifie chacun des individus pour ajouter un champ `duree` dans leur dictionnaire. La durée correspond au résultat de `final - initial`.

## Indicateur de temps

4. Écrire une fonction `nombre_individus_dans_etude(t)` qui calcule le nombre d'individus étudiés pendant au moins `t` jours.
5. Écrire une fonction `nombre_individus_identifies_a(t, i)` qui calcule le nombre d'individus dont l'identifiant vaut `i` et dont la durée d'étude est égale à `t`.

## Estimateur de Kaplan-Meier

Les données fournies sont en réalité des données issues des hôpitaux relatives à une épidémie.

Pour chaque personne, on connaît donc :

- Sa date d'entrée (jour de l'année) : champ `initial`
- Sa date de sortie si la personne est guérie : champ `final`
- L'issue : décès (0) ou guérison (1) : champ `identifiant`

L'estimateur de _Kaplain-Meier_ est une fonction statistique `S(t)` permettant de calculer la probabilité de survie des malades encore dans l'hôpital `t` jours après leur arrivée.

On note `n(t)` le nombre de personnes entrées à l'hôpital et qui y sont encore après `t` jours, et `d(t)` le nombre de personnes qui sont décédées au jour `t` à partir de leur entrée à l'hôpital.

L'estimateur de _Kaplan-Meier_ pour un `t` donné vaut alors : 

$$\hat{S}(t) = \prod_{i:t{i}\leq t}\left(1 - \frac{d_i}{n_i}\right)$$

C'est-à-dire : $(1 - d(t)/n(t))$ multiplié par toutes les valeurs précédemment calculées de $S(i)$ pour $i < t$.

6. Calculer tous les $S(t)$ pour $t$ allant de 1 à 100.


## Représentation graphique

7. Installer la librairie `matplotlib`. Par exemple :

```sh
pip install matplotlib
```

8. A l'aide de l'exemple de code ci-dessous, tracer la courbe de _Kaplan-Meier_ pour les $S(t)$ calculés précédemment.

```python
import matplotlib.pyplot as plt

x = [1, 3, 4, 6]
y = [2, 3, 5, 1]
plt.plot(x, y)
plt.show()
```

