---
title: Exercices Techniques de tests
correction: false
---

## Analyse partitionnelle

Soit le spécifications techniques suivantes pour l'exécution d'une fonction `Factoriel` :

- Si la valeur $n$ est négative : un message d'erreur est affichée.
- Si $n$ est dans $[1,20[$ on affiche la valeur exacte de `Factoriel(n)`.
- Si $n$ est dans $[20,200]$ on affiche une _approximation_ de `Factoriel(n)` en virgule flottante avec une précision de $0,1%$.
- Si $n>200$ un message d'erreur est affiché.

_Proposer des classes d'équivalence à tester._

::: {.correction .if correction="true"}
- $n < 0$ ou $n > 200$ : classe d'erreur 1 - message d'erreur à afficher ;
- $n \in [0,1]$ : classe d'erreur 2 - entrée non attendue ;
- $n \in [1,20[$ : classe valeur exacte `Factoriel(n)` ;
- $n \in [20,200]$ : classe approximation.
:::

## Test aux limites

Un programme de classification de triangles prend en entrée un triplet de réels $(a,b,c)$ correspondants aux longueurs des 3 côtés d'un triangle. Le programme doit préciser la nature du triangle (_équilatéral, isocèle, scalène, impossible_).

Donner des exemples de valeurs aux limites.

::: {.correction .if correction="true"}
- $(0,0,0)$ un point,
- $(0.1,0.1,0.1)$ un petit triangle,
- $(1,1,2)$ un segment,
- $(1,1,2.0000001)$ un triangle bien plat,
- $(4,0,3)$ une des longueurs est nulle
- $(4,4,4.000001)$ presque équilatéral
- etc.
:::

## Tables de décision

### Login

Soit une page Web permettant à un utilisateur de se connecter à un système.

Les conditions d'utilisation sont simples :

- Si le nom d'utilisateur et le mot de passe sont corrects, l'utilisateur est redirigé vers la page suivante ;
- Si le nom d'utilisateur ou le mot de passe sont incorrects, une page d'erreur est affichée.

1. Écrire les règles liées à cette fonctionnalité en utilisant une table de décision.
2. En déduire un jeu de tests appropriés permettant de couvrir toutes les règles.

| Conditions     | Cas 1 | Cas 2 | ...
|----------------|-------|-------|-----
| Username (T/F) |       |       |
| Password (T/F) |       |       |
| Output (E/N)   |       |       |

- T = True
- F = False
- E = Error
- N = Next

::: {.correction .if correction="true"}
- Case 1 – Username and password both were wrong. The user is shown an error message.
- Case 2 – Username was correct, but the password was wrong. The user is shown an error message.
- Case 3 – Username was wrong, but the password was correct. The user is shown an error message.
- Case 4 – Username and password both were correct, and the user navigated to the homepage

While converting this to a test case, we can create 2 scenarios :

- Enter the correct username and correct password and click on login, and the expected result will be the user should be navigated to the homepage

And one from the below scenario

- Enter wrong username and wrong password and click on login, and the expected result will be the user should get an error message ;
- Enter correct username and wrong password and click on login, and the expected result will be the user should get an error message ;
- Enter wrong username and correct password and click on login, and the expected result will be the user should get an error message.

As they essentially test the same rule.
:::

### Upload de photos

Soit une boîte de dialogue proposant à l'utilisateur l'upload d'une photo sous certaines conditions, par exemple :

- Le fichier est au format `.jpg` ;
- Le fichier fait moins de _32kb_ ;
- La résolution est de _137x177_.

Si l'une des conditions n'est pas satisfaite, le système retourne un message d'erreur dédié ; si toutes les conditions sont satisfaites, l'upload est validé.

Conditions | Case 1  | Case 2      | Case 3  | Case 4      | Case 5   | Case 6      | Case 7   | Case 8
-----------|---------|-------------|---------|-------------|----------|-------------|----------|------------
Format     | .jpg    | .jpg        | .jpg    | .jpg        | Not .jpg | Not .jpg    | Not .jpg | Not .jpg
Size (kb)  | < 32    | < 32        | >= 32   | >= 32       | < 32     | < 32        | >= 32    | >= 32
resolution | 137x177 | Not 137x177 | 137x177 | Not 137x177 | 137x177  | Not 137x177 | 137x177  | Not 137x177
Sortie     | Photo uploaded | Error message resolution mismatch | Error message size mismatch | Error message size and resolution mismatch | Error message for format mismatch | Error message format and resolution mismatch | Error message for format and size mismatch | Error message for format, size, and resolution mismatch

En utilisant cette table de décision, proposer un ensemble de cas de tests permettant une couverture complète de la fonctionnalité en testant toutes les sorties possibles.

::: {.correction .if correction="true"}
Nous pouvons créer 8 cas de tests permettant une couverture complète de la fonctionnalité :

- Upload a photo with format `.jpg`, size less than 32kb and resolution 137x177 and click on upload.
  Expected result is Photo should upload successfully ;
- Upload a photo with format `.jpg`, size less than 32kb and resolution not 137x177 and click on upload.
  Expected result is Error message resolution mismatch should be displayed ;
- Upload a photo with format `.jpg`, size more than 32kb and resolution 137x177 and click on upload.
  Expected result is Error message size mismatch should be displayed ;
- Upload a photo with format `.jpg`, size more than equal to 32kb and resolution not 137x177 and click on upload.
  Expected result is Error message size and resolution mismatch should be displayed ;
- Upload a photo with format other than `.jpg`, size less than 32kb and resolution 137x177 and click on upload.
  Expected result is Error message for format mismatch should be displayed ;
- Upload a photo with format other than `.jpg`, size less than 32kb and resolution not 137x177 and click on upload.
  Expected result is Error message format and resolution mismatch should be displayed ;
- Upload a photo with format other than `.jpg`, size more than 32kb and resolution 137x177 and click on upload.
  Expected result is Error message for format and size mismatch should be displayed ;
- Upload a photo with format other than `.jpg`, size more than 32kb and resolution not 137x177 and click on upload.
  Expected result is Error message for format, size and resolution mismatch should be displayed.
:::

## Approche par paires

La multiplicité des environnements d'intégration rend souvent impossible l'étude de tous les cas d'utilisation possibles.

Prenons par exemple la situation suivante :

|OS     |Réseau   |Imprimante|Application|
|-------|---------|----------|-----------|
|Linux  |IP       |HP35      |Word       |
|Windows|Wifi     |Canon900  |Excel      |
|Mac OS |Bluetooth|Canon-EX  |Powerpoint |

Créer un plan de tests pour l'ensemble de cette matrice de déploiement nécessite $3^4=81$ tests.

Pour limiter le nombre de tests, on procède à un plan de test par paires : on teste uniquement chaque combinaison de 2 variables. Cela permet tout de même de tester l'intégration 2 à 2 de chaque partie du système avec chacune des autres parties.

Proposer un plan de tests permettant de valider chaque paire d'interactions. 

::: {.correction .if correction="true"}
|OS     |Réseau   |
|-------|---------|
|Linux  |IP       |
|Windows|IP       |
|Mac OS |IP       |
|Linux  |Wifi     |
|Windows|Wifi     |
|Mac OS |Wifi     |
|Linux  |Bluetooth|
|Windows|Bluetooth|
|Mac OS |Bluetooth|


|OS     |Imprimante|
|-------|----------|
|Linux  |HP35      |
|Windows|Canon900  |
|Mac OS |Canon-EX  |
|Linux  |HP35      |
|Windows|Canon900  |
|Mac OS |Canon-EX  |
|Linux  |HP35      |
|Windows|Canon900  |
|Mac OS |Canon-EX  |


|OS     |Application|
|-------|-----------|
|Linux  |Word       |
|Windows|Excel      |
|Mac OS |Powerpoint |
|Linux  |Word       |
|Windows|Excel      |
|Mac OS |Powerpoint |
|Linux  |Word       |
|Windows|Excel      |
|Mac OS |Powerpoint |


|Réseau   |Imprimante|
|---------|----------|
|IP       |HP35      |
|IP       |Canon900  |
|IP       |Canon-EX  |
|Wifi     |HP35      |
|Wifi     |Canon900  |
|Wifi     |Canon-EX  |
|Bluetooth|HP35      |
|Bluetooth|Canon900  |
|Bluetooth|Canon-EX  |
:::

::: {.correction .if correction="true"}
|Réseau   |Application|
|---------|-----------|
|IP       |Word       |
|IP       |Excel      |
|IP       |Powerpoint |
|Wifi     |Word       |
|Wifi     |Excel      |
|Wifi     |Powerpoint |
|Bluetooth|Word       |
|Bluetooth|Excel      |
|Bluetooth|Powerpoint |


|Imprimante|Application|
|----------|-----------|
|HP35      |Word       |
|HP35      |Excel      |
|HP35      |Powerpoint |
|Canon900  |Word       |
|Canon900  |Excel      |
|Canon900  |Powerpoint |
|Canon-EX  |Word       |
|Canon-EX  |Excel      |
|Canon-EX  |Powerpoint |



On en déduit donc les paires suivantes en :

- recopiant les 1eres paires _OS_ et _Réseau_ ;
- puis en y ajoutant les paires manquantes pour _Réseau_ et _Imprimante_ ;
- puis en y ajoutant les paires manquantes pour _Imprimante_ et _Application_ .

|OS     |Réseau   |Imprimante|Application|
|-------|---------|----------|-----------|
|Linux  |IP       |HP35      |Word       |
|Windows|IP       |Canon900  |Word       |
|Mac OS |IP       |Canon-EX  |Word       |
|Linux  |Wifi     |HP35      |Excel      |
|Windows|Wifi     |Canon900  |Excel      |
|Mac OS |Wifi     |Canon-EX  |Excel      |
|Linux  |Bluetooth|HP35      |Powerpoint |
|Windows|Bluetooth|Canon900  |Powerpoint |
|Mac OS |Bluetooth|Canon-EX  |Powerpoint |


Voir aussi les [outils](https://www.pairwise.org/tools.html) disponibles pour réaliser une approche par paires (pariwise).
:::

## Tests boîte blanche

```
void foo ( bool a , bool b , bool c ) {
  if ( a or ( b and c )) then
    println("ok");
  else
    ();

  println("fin");
}
```

Proposer des jeux de tests permettant :

1. de couvrir les instructions ;
2. de couvrir les décisions.

Y a-t-il une différence ?

::: {.correction .if correction="true"}
1. Couverture des instructions :

- Cas de test $a$ vrai, $b$ faux, $c$ faux => test du `if` et du dernier `println()` ;
- Il manque un cas de test : $a$ faux, $b$ faux, $c$ faux => test du `else`.

2. Couverture des décisions :

- Cas de test $a$ vrai, $b$ faux, $c$ faux => test de la 1e condition du `if` ;
- Cas de test $a$ faux, $b$ vrai, $c$ vrai => test de la 2e condition du `if` ;
- Il manque un cas de test : $a$ faux, $b$ faux, $c$ faux => test du `else`.

La couverture par instructions est un sous-ensemble de la couverture par décisions.
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
