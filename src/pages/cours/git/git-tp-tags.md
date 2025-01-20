---
title: Les tags de Git
author: Tom Avenel
date: 2023 / 2024
---

# Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

# Les tags

Les tags servent à étiqueter des commits. Ils fonctionnent de la même manière que les branches mais ne bougent pas avec la `HEAD`.

Les tags sont très utilisés pour ajouter des indications de versions. Pour créer un tag `v1.0` sur le commit courant, on utilise : `git tag v1.0`

## Création d'un premier tag

1. Créer un nouveau dépôt en ligne et le cloner localement.
1. Créer un nouveau fichier `f1` et l'ajouter dans un premier commit.
1. Créer un tag `v1.0`
1. Modifier le fichier `f1` et créer un nouveau commit.
1. Vérifier avec `git log` que la `HEAD` et la branche ont bien avancé mais que le tag est toujours attaché au 1er commit.

## Annotation

1. Créer une nouvelle branche avec un nouveau commit.
1. Ajouter un nouveau tag `v1.1` en ajoutant une annotation (option `-a` ou `--annotate`) : cela permet d’associer au tag une date de création, l'identité du créateur, et éventuellement sa signature (clé GnuPG).
1. Afficher le tag avec son annotation : il faudra pour cela afficher plusieurs lignes du tag (par défaut, Git n'affiche que la 1ere ligne). On utilise souvent : `git tag -n99` pour afficher 99 lignes par tag (normalement plus que suffisant...)

## Publication et récupération

### Publication

Les 2 tags créés n'existent encore que localement. Pour publier un tag, on utilise aussi la commande `push` de la même manière que pour une branche :

```
git push origin v1.0
```

ou pour publier tous les tags :

```
git push --tags origin
```

1. Publier uniquement le tag `v1.0` sur le dépôt distant. Vérifier que le tag (et uniquement celui-ci) a été publié en utilisant l'interface web.
1. Publier tous les tags locaux.

### Récupération

1. Cloner le dépôt distant une nouvelle fois. _Les tags sont-ils récupérés ?_

:::tip
Les tags sont récupérés automatiquement lors d'un `git pull` **pour les commit présents localement uniquement**.
:::

### Navigation

Il est possible de se déplacer à n'importe quel moment vers un tag en utilisant une opération `checkout`.

1. Se déplacer vers le tag `v1.0`. _Quel est l'état de la `HEAD` ?_

\newpage{}

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries

