---
title: Projet noté traitement des données
date: 2023 / 2024
correction: false
---

# Partie 1

## Exercice 1 : Classification par la méthode des centres mobiles

On considère les 6 points $M_1 = (-2, 3)$, $M_2 = (-2, 1)$, $M_3 = (-2, -1)$, $M_4 = (2, -1)$, $M_5 = (2, 1)$ et $M_6 = (1, 0)$.

1. En supposant que les deux premiers points $M_1$ et $M_2$ sont les centres initiaux, décrire par une succession de dessins, les étapes de l'algorithme des centres mobiles en représentant les centres et les classes (en entourant chacune d'un rond) à chaque itération.

2. Recommencer en choisissant $M_4$ et $M_6$ pour les centres initiaux. Obtient-on la même classification ?

## Exercice 2 : Classification hiérarchique ascendante

Classifier les points du nuage précédent par une classification hiérarchique ascendante et représenter le dendrogramme (à noter que lorsqu'on doit regrouper les deux points les plus proches et qu'il existe deux couples de points satisfaisant cette condition, on convient de choisir les deux points dont les numéros sont les plus petits).

En déduire une classification pour ce nuage de points.

# Partie 2 - Arbre de décision

## Introduction

Une banque souhaite vendre un produit d’assurance à ses clients. Pour mettre en place cette stratégie commerciale, le data miner envisage, à partir d’un échantillon représentatif de la base clients, de construire un modèle.

Dans cette seconde partie du TD, vous décidez de construire un arbre de décision afin de savoir si un client est intéressé ou non par le produit d’assurance.

Le data miner dispose pour cet exercice de quatre variables explicatives :

- la variable binaire _Crédit_ traduisant le fait que le client possède ou non au sein de l’organisme un crédit en cours ;
- la variable binaire _Sexe_ représentant le sexe du client ;
- la variable qualitative _Revenus_ indiquant la classe des revenus du client ;
- la variable continue _Age_ indiquant l’âge du client ;

Et d’une variable cible :

- la variable _Assurance_ traduisant le fait que le client a souscrit ou non le produit d’assurance.

Les données dont le data miner dispose sont contenues dans le tableau suivant :


| ID | Crédit | Sexe | Revenus | Age | Assurance |
|----|--------|------|---------|-----|-----------|
| 1  | Non    | H    | 40-50   | 45  | Non       |
| 2  | Oui    | F    | 30-40   | 40  | Non       |
| 3  | Non    | H    | 40-50   | 42  | Non       |
| 4  | Oui    | H    | 30-40   | 43  | Oui       |
| 5  | Non    | F    | 50-60   | 38  | Oui       |
| 6  | Non    | F    | 20-30   | 55  | Non       |
| 7  | Oui    | H    | 30-40   | 35  | Oui       |
| 8  | Non    | H    | 20-30   | 27  | Non       |
| 9  | Non    | H    | 30-40   | 43  | Non       |
| 10 | Non    | H    | 30-40   | 41  | Oui       |
| 11 | Oui    | F    | 40-50   | 43  | Oui       |
| 12 | Oui    | F    | 20-30   | 29  | Oui       |
| 13 | Non    | H    | 50-60   | 39  | Oui       |
| 14 | Non    | F    | 40-50   | 55  | Non       |
| 15 | Oui    | H    | 20-30   | 19  | Oui       |


## Division 1

1. Indiquer pour chacune des variables explicatives le nombre de division(s) admissible(s) que l’on peut former.  Justifier votre réponse.
2. On rappelle que l'_indice de Gini_ associé à un segment $t$ se calcule comme suit :

$$Gini(t) = 1 - p^2(0|t) - p^2(1|t)$$

Où les valeurs 0 et 1 désignent respectivement les modalités « échec » et « succès » associées à la variable cible.

Compléter alors le tableau suivant (justifier vos calculs) :

| Assurance | Racine |
|-----------|--------|
| Oui       |        |
| Non       |        |
| Gini      |        |

**Note** : ici et dans la suite, on arrondira à trois chiffres après la virgule.

3. Préciser de manière générale ce que mesure l’indice de Gini. Donner une interprétation de cet indice en terme de distribution de la variable cible.

4. Dans le but d'identifier la « meilleure » division globale, compléter les tableaux suivants :

+--------------------+-----+-----+
| Assurance \ Crédit | Oui | Non |
+:===================+:===:+:===:+
| Oui                |  ?  |  3  |
+--------------------+-----+-----+
| Non                |  1  |  ?  |
+--------------------+-----+-----+
| Gini               |  ?  |0.444|
+--------------------+-----+-----+
| Gini total         |    ?      |
+--------------------+-----+-----+


+------------------+-----+-----+
| Assurance \ Sexe |  H  |  F  |
+:=================+:===:+:===:+
| Oui              |  ?  |  5  |
+------------------+-----+-----+
| Non              |  ?  |  2  |
+------------------+-----+-----+
| Gini             |0.469|  ?  |
+------------------+-----+-----+
| Gini total       |   0.441   |
+------------------+-----+-----+


+---------------------+-----+-----+-----+-----+-----+-----+
| Assurance \ Revenus |20-30|30-60|20-40|40-60|20-50|50-60|
+:====================+:===:+:===:+:===:+:===:+:===:+:===:+
| Oui                 |  ?  |  6  |  ?  |  3  |  6  |  2  |
+---------------------+-----+-----+-----+-----+-----+-----+
| Non                 |  ?  |  5  |  4  |  3  |  7  |  0  |
+---------------------+-----+-----+-----+-----+-----+-----+
| Gini                |  ?  |0.496|0.494|0.500|0.497|  ?  |
+---------------------+-----+-----+-----+-----+-----+-----+
| Gini total          |   0.497   |   0.496   |    ?      |
+---------------------+-----+-----+-----+-----+-----+-----+



+-----------------+---+------+---+------+---+------+-----+------+
| Assurance \ Age |   23     |   28     |   32     |   36.5     |
+-----------------+---+------+---+------+---+------+-----+------+
| Modalités       | < |$\geq$| < |$\geq$| < |$\geq$| <   |$\geq$|
+:================+:=:+:====:+:=:+:====:+:=:+:====:+:===:+:====:+
| Oui             | ? | ?    | 1 | 7    | 2 | 6    | 3   | 5    |
+-----------------+---+------+---+------+---+------+-----+------+
| Non             | ? | ?    | 1 | 6    | 1 | 6    | 1   | 6    |
+-----------------+---+------+---+------+---+------+-----+------+
| Gini            | 0 | 0.500| ? | 0.497| ? | ?    |0.375|0.496 |
+-----------------+---+------+---+------+---+------+-----+------+
| Gini total      |  0.467   |  0.497   |  0.489   |  ?         |
+-----------------+---+------+---+------+---+------+-----+------+

+-----------------+----+------+-----+------+-----+------+
| Assurance \ Age |   38.5    |   39.5     |   40.5     |
+-----------------+----+------+-----+------+-----+------+
| Modalités       | <  |$\geq$| <   |$\geq$| <   |$\geq$|
+:================+:==:+:====:+:===:+:====:+:===:+:====:+
| Oui             | ?  | ?    | 5   | 3    | 5   | 3    |
+-----------------+----+------+-----+------+-----+------+
| Non             | 1  | 6    | 1   | 6    | ?   | 5    |
+-----------------+----+------+-----+------+-----+------+
| Gini            |0.32|0.48  |0.278|0.444 |0.408|  ?   |
+-----------------+----+------+-----+------+-----+------+
| Gini total      |  0.427    |  0.378     |  0.441     |
+-----------------+----+------+-----+------+-----+------+

+-----------------+-----+------+-----+------+-----+------+
| Assurance \ Age |   41.5     |   42.5     |   44       |
+-----------------+-----+------+-----+------+-----+------+
| Modalités       | <   |$\geq$| <   |$\geq$| <   |$\geq$|
+:================+:===:+:====:+:===:+:====:+:===:+:====:+
| Oui             | 6   | 2    | 6   | 2    | 8   | 0    |
+-----------------+-----+------+-----+------+-----+------+
| Non             | 2   | 5    | 3   | 4    | 4   | 3    |
+-----------------+-----+------+-----+------+-----+------+
| Gini            |0.375|0.408 |0.444|0.444 |0.444|  0   |
+-----------------+-----+------+-----+------+-----+------+
| Gini total      |  0.390     |  0.444     |   ?        |
+-----------------+-----+------+-----+------+-----+------+

+-----------------+-----+------+
| Assurance \ Age |   50       |
+-----------------+-----+------+
| Modalités       | <   |$\geq$|
+:================+:===:+:====:+
| Oui             | 8   | 0    |
+-----------------+-----+------+
| Non             | 5   | 2    |
+-----------------+-----+------+
| Gini            |0.473| 0    |
+-----------------+-----+------+
| Gini total      |    ?       |
+-----------------+-----+------+


5. Déterminer la « meilleure » division globale, en précisant la variable ainsi que la condition associée. Justifier votre choix.

Note : en cas de choix multiple, on choisira par défaut la variable selon l'ordre dans lequel elles apparaissent dans le tableau de données.
6. Représenter graphiquement la première division en précisant la distribution (en effectifs) de la variable _Assurance_ à l'intérieur de chacun des segments, ainsi que l'effectif total en présence.

7. Dans toute la suite, on décidera qu'un segment est terminal si au moins l'une des conditions suivantes est satisfaite : le segment est pur, ou le segment contient un nombre d'unités inférieur ou égal à cinq.
Préciser pour chacun des segments résultant de la première division s'il s'agit d'un segment terminal ou d'un segment intermédiaire. Justifier votre réponse.

## Division 2

1. En se basant sur le travail précédent, compléter les tableaux suivants :

+--------------------+-----+-----+
| Assurance \ Crédit | Oui | Non |
+:===================+:===:+:===:+
| Oui                |  ?  |  3  |
+--------------------+-----+-----+
| Non                |  1  |  3  |
+--------------------+-----+-----+
| Gini               |0.278|     |
+--------------------+-----+-----+
| Gini total         |    0.389  |
+--------------------+-----+-----+


+------------------+-----+-----+
| Assurance \ Sexe |  H  |  F  |
+:=================+:===:+:===:+
| Oui              |  3  |  ?  |
+------------------+-----+-----+
| Non              |  3  |  ?  |
+------------------+-----+-----+
| Gini             |0.5  |  ?  |
+------------------+-----+-----+
| Gini total       |   ?       |
+------------------+-----+-----+


+---------------------+-----+-----+-----+-----+-----+-----+
| Assurance \ Revenus |20-30|30-60|20-40|40-60|20-50|50-60|
+:====================+:===:+:===:+:===:+:===:+:===:+:===:+
| Oui                 |  2  |  6  |  5  |  ?  |  6  |  2  |
+---------------------+-----+-----+-----+-----+-----+-----+
| Non                 |  1  |  3  |  3  |  ?  |  4  |  ?  |
+---------------------+-----+-----+-----+-----+-----+-----+
| Gini                |  ?  |0.444|0.469|0.375|0.48 |  ?  |
+---------------------+-----+-----+-----+-----+-----+-----+
| Gini total          |    ?      |   0.438   |    0.4    |
+---------------------+-----+-----+-----+-----+-----+-----+



+-----------------+---+------+---+------+-----+------+-----+------+
| Assurance \ Age |   23     |   28     |   32       |   36.5     |
+-----------------+---+------+---+------+-----+------+-----+------+
| Modalités       | < |$\geq$| < |$\geq$| <   |$\geq$| <   |$\geq$|
+:================+:=:+:====:+:=:+:====:+:===:+:====:+:===:+:====:+
| Oui             | 1 | 7    | 1 | 7    | 2   | 6    | 3   | 5    |
+-----------------+---+------+---+------+-----+------+-----+------+
| Non             | 0 | 4    | 1 | 3    | 1   | 3    | 1   | 3    |
+-----------------+---+------+---+------+-----+------+-----+------+
| Gini            | 0 | 0.463| ? | 0.42 |0.444|0.444 |0.375|0.469 |
+-----------------+---+------+---+------+-----+------+-----+------+
| Gini total      |  0.424   |  0.433   |  0.444     |  ?         |
+-----------------+---+------+---+------+-----+------+-----+------+

+-----------------+----+------+-----+------+-----+------+
| Assurance \ Age |   38.5    |   39.5     |   40.5     |
+-----------------+----+------+-----+------+-----+------+
| Modalités       | <  |$\geq$| <   |$\geq$| <   |$\geq$|
+:================+:==:+:====:+:===:+:====:+:===:+:====:+
| Oui             | ?  | 4    | 5   | ?    | 5   | 3    |
+-----------------+----+------+-----+------+-----+------+
| Non             | 1  | 3    | 1   | 3    | 2   | 2    |
+-----------------+----+------+-----+------+-----+------+
| Gini            |0.32|0.49  |0.278|0.5   |0.408|  0.48|
+-----------------+----+------+-----+------+-----+------+
| Gini total      |  0.419    |    ?       |  0.438     |
+-----------------+----+------+-----+------+-----+------+

+-----------------+-----+------+-----+------+
| Assurance \ Age |   41.5     |   42.5     |
+-----------------+-----+------+-----+------+
| Modalités       | <   |$\geq$| <   |$\geq$|
+:================+:===:+:====:+:===:+:====:+
| Oui             | ?   | 2    | 6   | 2    |
+-----------------+-----+------+-----+------+
| Non             | 2   | 2    | 3   | 1    |
+-----------------+-----+------+-----+------+
| Gini            |  ?  |0.5   |0.444|0.444 |
+-----------------+-----+------+-----+------+
| Gini total      |    ?       |  0.444     |
+-----------------+-----+------+-----+------+

2. Déterminer la « meilleure » division globale, en précisant la variable ainsi que la condition associée. Justifier votre choix.

Note : en cas de choix multiple, on choisira par défaut la variable selon l'ordre dans lequel elles apparaissent dans le tableau de données.
3. Représenter graphiquement cette seconde division en précisant la distribution (en effectifs) de la variable _Assurance_ à l'intérieur de chacun des segments, ainsi que l'effectif total en présence.

4. Préciser pour chacun des segments résultant de la deuxième division s'il s'agit d'un segment terminal ou intermédiaire. Justifier votre réponse.

## Division 3

1. A la vue des tableaux suivants, préciser si l'on travaille sur le segment $Credit=Yes$ ou $Credit=No$.

2. Compléter les tableaux suivants :

+------------------+-----+-----+
| Assurance \ Sexe |  H  |  F  |
+:=================+:===:+:===:+
| Oui              |  3  |  ?  |
+------------------+-----+-----+
| Non              |  0  |  1  |
+------------------+-----+-----+
| Gini             |  0  |  ?  |
+------------------+-----+-----+
| Gini total       |   0.222   |
+------------------+-----+-----+


+---------------------+-----+-----+-----+-----+
| Assurance \ Revenus |20-30|30-50|20-40|40-50|
+:====================+:===:+:===:+:===:+:===:+
| Oui                 |  2  |  ?  |  4  |  1  |
+---------------------+-----+-----+-----+-----+
| Non                 |  0  |  1  |  1  |  0  |
+---------------------+-----+-----+-----+-----+
| Gini                |  ?  |  ?  |0.32 |  0  |
+---------------------+-----+-----+-----+-----+
| Gini total          |    0.25   |   0.267   |
+---------------------+-----+-----+-----+-----+



+-----------------+---+------+---+------+-----+------+-----+------+
| Assurance \ Age |   24     |   32     |   37.5     |   41.5     |
+-----------------+---+------+---+------+-----+------+-----+------+
| Modalités       | < |$\geq$| < |$\geq$| <   |$\geq$| <   |$\geq$|
+:================+:=:+:====:+:=:+:====:+:===:+:====:+:===:+:====:+
| Oui             | 1 | 4    | 2 | 3    | 3   | ?    | ?   | 2    |
+-----------------+---+------+---+------+-----+------+-----+------+
| Non             | 0 | 1    | 0 | 1    | 0   | 1    | 1   | 0    |
+-----------------+---+------+---+------+-----+------+-----+------+
| Gini            | 0 |   ?  | 0 | 0.375|  0  |0.444 |  ?  |  0   |
+-----------------+---+------+---+------+-----+------+-----+------+
| Gini total      |  ?       |  0.25    |  0.222     |  0.25      |
+-----------------+---+------+---+------+-----+------+-----+------+

3. Déterminer la « meilleure » division globale, en précisant la variable ainsi que la condition associée. Justifier votre choix.

Note : en cas de choix multiple, on choisira par défaut la variable selon l'ordre dans lequel elles apparaissent dans le tableau de données.
4. Représenter graphiquement cette seconde division en précisant la distribution (en effectifs) de la variable _Assurance_ à l'intérieur de chacun des segments, ainsi que l'effectif total en présence.

5. Préciser pour chacun des segments résultant de la deuxième division s'il s'agit d'un segment terminal ou intermédiaire. Justifier votre réponse.

## Division 4

1. Compléter le tableau suivant :

+------------------+-----+-----+
| Assurance \ Sexe |  H  |  F  |
+:=================+:===:+:===:+
| Oui              |  ?  |  ?  |
+------------------+-----+-----+
| Non              |  ?  |  ?  |
+------------------+-----+-----+
| Gini             |  ?  |  ?  |
+------------------+-----+-----+
| Gini total       |   ?       |
+------------------+-----+-----+

2. Pourquoi n’a-t-on pas besoin de continuer les calculs ? Justifier votre réponse.

3. Représenter graphiquement cette troisième division en précisant la distribution (en effectifs) de la variable _Assurance_ à l'intérieur de chacun des segments, ainsi que l'effectif total en présence.

4. Préciser pour chacun des segments résultant de cette division s'il s'agit d’un segment terminal ou intermédiaire. Justifier votre réponse.

## Prévisions

1. Pour chacun des segments terminaux, allouer une modalité à la variable _Assurance_. Justifier votre choix.

2. Déterminer pour chacun des nouveaux clients, la valeur prédite par votre modèle pour la variable _Assurance_ :

ID | Crédit | Sexe | Revenus | Age | Assurance |
---|--------|------|---------|-----|-----------|
 1 | Oui    |  H   |  50-60  | 46  |     ?     |
 2 | Non    |  F   |  20-30  | 18  |     ?     |
 3 | Non    |  H   |  40-50  | 42  |     ?     |
 4 | Oui    |  H   |  50-60  | 51  |     ?     |
 5 | Oui    |  F   |  50-60  | 43  |     ?     |
