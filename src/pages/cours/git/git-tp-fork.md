---
title: Workflow de Fork
author: Tom Avenel
date: 2023 / 2024
---

# Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

# Workflow de fork

:::tip
Par cohérence avec le reste des TP, nous utiliserons la notation `origin` pour le 1er dépôt distant lié après l'opération de clone, ici souvent le dépôt officiel.

Par convention, on nomme souvent le dépôt officiel `upstream` (et on n'utilise pas la notation `origin` qui peut porter à confusion). Il s'agit uniquement de conventions - git ne met aucun sens sur le nom des dépôts configurés dans les `remote`.
:::

## Préparation du dépôt "officiel"

Dans un premier temps, nous allons créer un dépôt de code contenant la version "officielle" du projet :

1. Créer un nouveau dépôt git (pour pourra utiliser l'hébergement Github® pour le partage).
1. Cloner ce dépôt localement sur votre machine.
1. Créer un nouveau fichier `f1` contenant quelques lignes de texte
1. Ajouter le fichier dans un commit dans le dépôt local et publier ce commit dans le dépôt distant.

:::tip
Consultez le lien vers le dépôt distant depuis votre dépôt local : l'opération `git clone` a créé automatiquement une référence vers un dépôt distant (`remote`) nommé (par convention) `origin` :

```
git remote -v
```
:::

## Fork avec Git

### Initialisation du fork

Pour pouvoir réaliser des modifications dans le dépôt sans impacter le dépôt officiel, nous allons utiliser un dépôt "fork" dédié :

1. Créer un nouveau dépôt vide sur GitHub. **Attention : ne PAS utiliser le bouton `fork` de GitHub !!**
1. Ajouter un nouveau `remote` pointant sur ce nouveau dépôt : on l'appellera par exemple `fork`.
1. Publier la branche courante dans le dépôt `fork` : `git push fork`.

### Modifications dans le fork

Vous souhaitez apporter des modifications au dépôt officiel mais sans impacter celui-ci :

1. Créer une nouvelle branche `modification` dans le dépôt local. Dans cette branche, modifier le fichier `f1` et créer un nouveau commit.
1. Publier la branche **dans le dépôt `fork` uniquement !!!**

### Récupération des changements officiels

Une nouvelle version est apparue dans le dépôt officiel : depuis l'interface de GitHub, changer une ligne du fichier `f1` dans le dépôt officiel et créer un nouveau commit.

Nous allons récupérer ces changements :

1. Dans le dépôt local, récupérer les changements de la branche `main` du dépôt officiel dans la branche `modification`.
1. Résoudre les conflits si besoin dans un nouveau commit.
1. Intégrer les nouveaux changements au dépôt `fork`.

### Up-port dans le dépôt officiel

Finalement, les changements réalisés dans le `fork` sont intéressants à intégrer directement dans le dépôt officiel.

1. Depuis le dépôt local, publier la branche `modification` dans le dépôt officiel.

## Utiliser l'option de Fork de GitHub

Dans l'exercice précédent, nous avons utilisé notre dépôt local pour faire le lien entre le dépôt officiel et le fork. Cette opération a l'inconvénient de faire disparaître le lien entre le dépôt officiel et le dépôt `fork` sur GitHub.

GitHub est capable de gérer directement un fork depuis son interface : cela revient donc à cloner un dépôt officiel pour créer un autre dépôt **distant** ce qui permet de créer un lien directement entre les 2 dépôts distants.

### Initialisation du fork

1. Cliquer sur le bouton `fork` en haut à droite du dépôt officiel et créer un fork distant nommé `fork2`. Ce dépôt est le nouveau fork distant.
1. Cloner `fork2` sur votre machine pour disposer d'un dépôt local **uniquement relié à `fork2`**.

### Modifications dans le fork

Ici, il n'y a plus qu'un `remote` - rien de différent avec un workflow centralisé :

1. Créer une nouvelle branche `modification` dans le dépôt local. Dans cette branche, modifier le fichier `f1` et créer un nouveau commit.
1. Publier la branche dans le dépôt `fork2`

### Récupération des changements officiels

Depuis l'interface de GitHub, changer une ligne du fichier `f1` dans le dépôt officiel et créer un nouveau commit.

Dans le dépôt `fork2`, cliquer sur `Sync fork` pour synchroniser le fork depuis l'interface graphique de GitHub. Voir la [documentation sur la synchronisation du fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork?platform=linux) pour les différents moyens de réaliser cette opération.

### Up-port dans le dépôt officiel

Publier la branche `modification` du fork vers le dépôt officiel en utilisant une [pull-request de fork (voir la documentation)](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/committing-changes-to-a-pull-request-branch-created-from-a-fork)

# Liens

Voir aussi le [tutoriel Atlassian sur le workflow de fork](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/forking-workflow)

\newpage{}

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.
