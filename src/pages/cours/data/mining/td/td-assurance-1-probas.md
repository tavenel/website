---
title: TD traitement des données - probabilités
author: Tom Avenel
date: 2023 / 2024
correction: false
---

# Introduction

Une banque souhaite vendre un produit d’assurance à ses clients. Pour mettre en place cette stratégie commerciale, le data miner envisage, à partir d’un échantillon représentatif de la base clients, de construire un modèle. Dans la première partie de ce TD, nous allons étudier un modèle probabiliste de profiling.

Le data miner dispose pour cet exercice de quatre variables explicatives :

- la variable binaire _Crédit_ traduisant le fait que le client possède ou non au sein de l’organisme un crédit en cours ;
- la variable binaire _Sexe_ représentant le sexe du client ;
- la variable qualitative _Revenus_ indiquant la classe des revenus du client ;
- la variable continue _Age_ indiquant l'âge du client.

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


# Partie A : Profiling

## Étude de la variable Crédit.

1. Compléter le tableau de contingence (en effectifs) suivant :

| Crédit    | Oui | Non | Total |
|-----------|-----|-----|-------|
| Assurance |     |     |       |
| Oui       |     |     |       |
| Non       |     |     |       |
| Total     |     |     |       |

2. Calculer la probabilité de « succès » au sein de la population des clients possédant un crédit :

$$\pi(Credit=Oui)=?$$

En déduire la valeur de l'_odds_ (chance) pour la variable _Assurance_ au sein de la population des clients possédant un crédit.

On définit l'odds par : 

$$Odds(Credit=Oui)=\frac{\pi(Credit=Oui)}{1-\pi(Credit=Oui)}$$

3. Calculer l’odds pour la variable Assurance au sein de la population des clients ne possédant pas de crédit en cours. En déduire la valeur de l’_Odds Ratio_ OR(Oui|Non) de la variable Assurance par rapport à la variable Crédit avec la formule :

$$OR(Oui|Non) = \frac{Odds(Credit=Oui)}{Odds(Credit=Non}$$

4. Interpréter cette quantité, puis préciser si la variable Crédit possède un impact "significatif" sur la variable cible. Justifier votre réponse.

## Etude de la variable Sexe.

1. Réaliser le tableau de contingence de la variable.
2. Calculer la probabilité de succès au sein de la population des clients de sexe féminin. En déduire la valeur de l'odds pour l'Assurance au sein des clients de sexe féminin.
3. Calculer l'odds ratio de la variable Assurance par rapport à la variable Sexe.
4. Interpréter ce résultat.

## Etude de la variable Revenus

Mêmes questions pour la variable Revenus. On utilisera les 3 classes : $20-30$, $30-40$, $40-60$ et la classe $20-30$ comme modalité de référence.

## Etude de la variable Age

Calculer l'âge moyen pour les événements "succès" et "échec". Qu'en déduit-on ?

## Bilan

- Quelles variables sont pertinentes ou non pertinentes ?
- Quel est le type de clients qu'il conviendra de cibler afin d’améliorer la vente du produit ?

