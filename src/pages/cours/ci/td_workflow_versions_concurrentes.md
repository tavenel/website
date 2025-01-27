---
title: TD Intégration Continue
date: 2023-2024
correction: false
---

# Workflow support de versions concurrentes

Dans cet exercice, nous allons simuler un workflow Git permettant de maintenir en concurrence deux versions stables d'un produit (nommées `v1` et `v2`) et une version `v3` en cours de développement. Les versions `v1` et `v2` sont toutes les deux disponibles chez les clients qui n'ont pas tous migré à la dernière version stable `v2`. Les développeurs travaillent tous sur une future version `v3`, sauf bug critique rencontré dans les versions en production.

Dans la suite de l'exercice, un fichier unique `contenu.txt` simulera le contenu du produit dans l'ensemble du workflow - celui-ci pourra donc avoir des contenus différents coexistant en parallèle pour chaque version du produit.

## Définition du workflow

- Réfléchir à un workflow Git **simple** permettant de gérer en parallèle 2 versions stables du produit (versions `v1` et `v2` actuellement déployées en production) et une version future en cours de développement. Décrire les branches principales à utiliser (hors branches temporaires éventuelles) pour réaliser ce workflow.

::: {.correction .if correction="true"}

Le workflow utilise comme branches principales :

- Une branche `v1`, reliquat de la mise en production de la version 1 encore active pour les changements en production. Cette branche a été créée depuis la branche principale au moment de la création du dépôt.
- Une branche `v2` créée depuis la branche `v1` au moment de la mise en production de la `v1` afin de préparer le développement de la `v2`.
- Une branche `v3` pour la version en cours de développement au moment de la mise en production de la `v2`.

:::

## Création du dépot

- Créer un nouveau dépôt sur `Github`.
- Simuler ce workflow en créant 3 versions d'un fichier `contenu.txt` et en intégrant ces versions dans les branches correspondantes (une pour chaque version stable `v1` et `v2` et une pour la version de développement).
  + La version `v1` du fichier contiendra les lignes : `Versios` et `v1`.
  + La version `v2` du fichier contiendra : `Versios` et `v1` et `v2`.
  + La version de développement du fichier contiendra : `Versios` et `v1` et `v2` et `v3`.

_Attention à bien respecter la typo : `Versios` pour la suite de l'exercice !_

::: {.correction .if correction="true"}

1. Créer un dépôt sur `Github`.
2. `v1` du fichier (en cours de développement):
  - Création de la branche `v1` : `git checkout -b v1`.
  - Création du fichier `Versios` et `v1`.
  - Ajout du commit : `git add contenu.txt` et `git commit -am v1`.
3. Création de la `v2` : `git checkout -b v2`
4. Ajout des changements de la `v2` :
  - ajout `v2` dans le fichier
  - `git commit -am v2`
5. Création de la `v3` : `git checkout -b v3`
6. Ajout des changements de la `v3` : 
  - ajout `v3` dans le fichier
  - `git commit -am v3`

Note - la `v3` n'existe pas encore en production, mais ce n'est pas un problème car l'on prépare seulement le développement futur - il est courant d'identifier cette version en amont pour faciliter la gestion de projet.

:::

## Ajout de fonctionnalité

- Ajouter une nouvelle fonctionnalité `F1` au produit en cours de développement : pour cela, ajouter une ligne `F1` dans le fichier et intégrer ce changement dans la branche correspondante.

::: {.correction .if correction="true"}

- Déplacement dans la branche de développement : `git checkout v3`
- Ajout de la ligne au fichier
- Intégration dans la branche : `git commit -am F1`

Note - on pourrait également créer une branche de fonctionnalité dédiée avant intégration dans la branche `dev` :

- Déplacement dans la branche de développement : `git checkout v3`
- Branchement temporaire pour `F1` : `git checkout -b F1`
- Ajout de la ligne au fichier
- Intégration dans la branche `F1` : `git commit -am F1`
- Fusion dans la branche `dev` : `git checkout v3` et `git merge F1`.

:::

## Nouvelle version mineure

- La version de production `v2` va être modifiée pour livrer une nouvelle version `v2`.1 : modifier la ligne `v2` par `v2.1` dans le fichier **pour la version `v2` uniquement**.

_La version de développement contiendra donc toujours la ligne : `v2` et non `v2.1`_

::: {.correction .if correction="true"}

- Déplacement dans la branche `v2` : `git checkout v2`
- Changement de `v2` en `v2.1`
- Intégration dans la branche `v2` : `git commit -am v2.1`
- Vérification : `git checkout v3` => le fichier contient `v2`

:::

## Portage de correctif

_Un bug critique a été trouvé en production depuis la version 1 ! Dans le fichier, le mot `Versios` a été mal orthographié et devrait en réalité s'écrire `Versions`._

- Corriger ce problème dans la version `v1`. Attention - corriger un problème en production est critique, on utilisera donc une branche de fonctionnalité dédiée nommée `fix-typo` et une `Merge Request` dans `GitHub` avant d'intégrer le correctif à la version `v1`.
- Réaliser un _portage_ de la modification, c'est-à-dire intégrer ce changement également dans la version `v2.1` et la version de développement.

_Attention : pour réaliser le portage, on n'utilisera que des commandes `git`, c'est-à-dire que le changement de ligne dans le fichier ne devra être réalisé qu'une seule et unique fois depuis un éditeur de texte pour la version `v1`._

::: {.correction .if correction="true"}

- Correction dans la `v1` :
  - Déplacement dans la branche `v1` : `git checkout v1`
  - Branchement temporaire pour `fix-typo` : `git checkout -b fix-typo`
  - Correction du bug
  - Intégration dans la branche `fix-typo` : `git commit -am 'typo versios'`
  - Ouverture d'une merge-request ou pull-request sur GitHub.
  - Après accord : Fusion dans la branche `v1` : `git checkout v1` et `git merge fix-typo`.
- Portage `v2`.1
  - Déplacement dans la branche `v2` : `git checkout v2`
  - Récupération des changements : `git merge fix-typo`
- Portage `v3`
  - Déplacement dans la branche `v3` : `git checkout v3`
  - Récupération des changements : `git merge fix-typo`

Note - sans branche intermédiaire de fonctionnalité `fix-typo`, on aurait pu directement fusionner la branche `v1` car les branches n'ont pas divergé. Dans un exemple plus complexe où `v1` aurait d'autres changements non désirés, on utilisera la commande git `cherry-pick` pour intégrer uniquement un commit aux branches `v2` et `v3`.

:::

## Nouvelle version stable

- Adapter le workflow pour déployer en production une nouvelle version stable `v3` depuis la version en cours de développement. On gardera également toujours les versions `v1` et `v2.1`
- Préparer une nouvelle version de développement à la suite de la version `v3` et ajouter une ligne `v4` dans le fichier.
- Ne devrait-on pas attendre de déployer `v4` en production avant d'ajouter cette ligne dans le fichier ? Pourquoi ?

::: {.correction .if correction="true"}

Il suffit de préparer une nouvelle version `v4` pour la future production depuis `v3` :

- `git checkout v3`
- `git checkout -b v4`
- ajout de la version 4 au fichier
- `git commit -am v4`.

Voir la note dans la correction de la question Création du dépôt : il est normal d'avoir une version 4 dans le dépôt de code même si celle-ci n'est pas encore en production, afin de préparer la livraison future de la `v4`.
:::

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0

