---
title: TD traitement des données - régression linéaire
date: 2023 / 2024
---

# Nombre d'espèces par surface

## Introduction

L'une des rares lois que l'on a pu mettre en évidence en Écologie est la relation existant entre le nombre $N$ d'espèces présentes dans un habitat donné (bien délimité) et la surface $S$ de cet habitat.

On considère généralement que cette relation est de la forme :

$$N = A.S^B$$

Où $A$ et $B$ sont deux constantes.

Afin de vérifier cette relation pour les plantes présentes dans une prairie (pissenlit, paquerettes, orties, boutons d'or, ...), on a effectué les mesures indiquées dans le premier tableau ci-dessous. On a représenté sur la première figure ci-dessous les valeurs de $N$ en fonction de celles de $S$ et sur la deuxième les valeurs de $\tilde{N} = ln(N)$ en fonction de celles de $\tilde{S} = ln(S)$.

On voit que la régression linéaire de $\tilde{N}$ sur $\tilde{S}$ a donné l'équation $\tilde{N} = 0,2199 \tilde{S} + 1,7432$ avec $R^2 = 0,9684$.

![Régression linéaire nombre d'espèces par surface](@assets/data/reg-ecologie.png)

<div class="caption">Régression linéaire nombre d'espèces par surface</div>

## Questions

1. Pourquoi n'a-t-on pas effectué directement une régression linéaire de $N$ sur $S$ et a-t-on préféré transformer $N$ en $\tilde{N}$ et $S$ en $\tilde{S}$ ?
2. À partir de la régression linéaire effectuée, calculer les constantes $A$ et $B$ de la relation $N=A.S^B$.
3. Quelle valeur $\tilde{N}$ ce modèle linéaire prédit-il pour $\tilde{S} = ln(64)$ ? En comparant avec la valeur de $\tilde{S}$ observée, calculer le résidu $\epsilon$ en ce point.
4. Quelle valeur $\tilde{N}$ ce modèle linéaire prédit-il pour $\tilde{S} = ln(100)$ ? En déduire le nombre d'espèces pouvant coexister dans un habitat de surface $S = 100$, selon ce modèle.

# Végétation au sol en fonction de la chimie

## Présentation

On s'intéresse à la répartition de la végétation dans un site aride du
sud de la France, la plaine de la Crau (13).

On effectue 9 prélèvements de sol $(S1, ..., S9)$ pour lesquels on retient, après analyse, 6 mesures (pH, C/N, Ca, Mg, K, P) et dans le même temps on évalue dans chaque cas le pourcentage de recouvrement au sol par la végétation (%V).

Les données brutes sont regroupées dans le tableau suivant :

|    |  pH  |  C/N  |  Ca  |  Mg  |  K   |  P   | %V |
|----|------|-------|------|------|------|------|----|
| S1 | 5.5  | 30.75 | 0.55 | 0.01 | 0.42 | 0.01 | 15 | 
| S2 |  7   | 19.29 | 1.02 | 0.07 | 0.43 | 0.02 | 42 |
| S3 | 6.8  | 31.47 | 1.02 | 0.05 | 0.45 | 0.01 | 26 |
| S4 | 7.3  | 2.93  | 1.82 | 0.09 | 0.44 | 0.02 | 50 |
| S5 | 5.62 | 32.45 | 0.42 | 0    | 0.41 | 0.01 | 25 |
| S6 | 6.6  | 20.05 | 0.75 | 0.01 | 0.44 | 0.01 | 30 |
| S7 |  7   | 3.35  | 1.33 | 0.07 | 0.46 | 0.02 | 50 |
| S8 | 5.8  | 33.18 | 0.48 | 0.02 | 0.43 | 0.01 | 18 |
| S9 |  7   | 5.32  | 1.35 | 0.07 | 0.48 | 0.005| 38 |

On veut étudier de quelle façon les variables pH, C/N et P influent sur le pourcentage de recouvrement au sol par la végétation et on va pour cela chercher à expliquer par une régression linéaire la quantité
%V en fonction de chacune de ces 3 variables explicatives.

## Questions

1. Exprimer, par une régression linéaire, %V en fonction de pH et donner l'équation de la droite des moindres carrés ainsi que la valeur du coefficient de détermination $R^2$ (on pourra utiliser le fait que la variance de pH vaut 0.417, que la variance de %V vaut 150.44 et que leur covariance vaut 6.92).
2. On a aussi cherché à expliquer de la même façon %V à l'aide de deux autres variables, C/N et P. On a obtenu les dessins des nuages et des droites de régression suivants :

![Regression C/N et P](@assets/data/reg-c-n-p.png)

<div class="caption">Regression C/N et P</div>

Malheureusement, on a mélangé les résultats ; les équations $y = 1617,4x + 12$ et $y = -0,904x + 50,691$ et les coefficients $R^2 = 0,8178$ et $R^2 = 0,4937$. Sans faire de nouveaux calculs, indiquer quelle équation et quel coefficient correspond à quel dessin en justifiant vos réponses.

3. Parmi ces trois régressions, y en a-t-il à votre avis qui soient acceptables ? Justifier votre réponse.
4. Finalement, compte tenu de ces résultats, peut-on conclure que la chimie du sol peut expliquer le pourcentage de végétation ? On pourra se servir de la part de dispersion de %V expliquée par les régressions.
