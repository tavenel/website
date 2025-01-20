---
title: Les workflows Git™ et la pull-request
author: Tom Avenel
date: 2023 / 2024
---

# Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

**L'intégralité de ce cas pratique est à réaliser en binôme.**

# Workflow branche de fonctionnalité

## Intégration simple de fonctionnalités concurrentes

Dans ce premier exemple, nous allons utiliser un workflow de fonctionnalité pour isoler un développement concurrent de deux nouvelles fonctions dans un produit.

1. Créer un nouveau dépôt git (pour pourra utiliser l'hébergement Github® pour le partage).
1. Le premier développeur crée une nouvelle branche de fonctionnalité et ajoute sa fonctionnalité A dans sa branche de fonctionnalité.
1. En parallèle, le deuxième développeur ajoute sa fonctionnalité B depuis une autre branche de fonctionnalité.
1. Vérifier le graphe des commit : les différentes fonctionnalités sont-elles bien identifiables dans leurs branches respectives ?

On pourra utiliser la commande suivante pour afficher un graphe des commit :

```bash
git log --oneline --decorate --graph
```

## Intégration concurrente avec partage de code

Nous allons maintenant utiliser le même exemple que précédemment mais cette fois-ci il n'est pas possible de finir complètement le développement de A ou de B sans intégrer les deux à la fois. Par exemple, A peut être le code du backend et B le code du frontend pour une nouvelle fonctionnalité, chacun réalisés par un développeur différent.

Une première solution (parfois utilisée) serait d'intégrer les changements de chaque développeur dans le tronc commun, et d'attendre l'ensemble des intégrations pour avoir une fonctionnalité complète.

Cependant, on préfère ici ne pas polluer le tronc commun avec d'intégrer une fonctionnalité complète.

_Comment adapter l'exemple précédent à ce nouveau besoin ? On pourra créer des branches supplémentaires si besoin._

# La pull-request et la revue de code

L'un des principaux intérêts d'un serveur de code hébergé comme `GitHub®` est la possibilité d'interagir avec les commit `Git` de manière assez poussée.

Par exemple, il est possible de réaliser des revues de code avant d'intégrer une fonctionnalité dans le tronc commun. Ce procédé consiste à faire relire le code à intégrer par un ou plusieurs autre(s) développeur(s) afin de minimiser les risques d'erreur.

Reprendre le premier exemple en utilisant `GitHub®` ou un autre service Cloud d'hébergement de code source. Au moment de fusionner la branche de fonctionnalités dans le tronc commun, créer une `pull-request` préparant cette opération de fusion. Le 2e développeur aura alors la responsabilité de relire le code modifié et de proposer des changements. Intégrer ensuite la branche de fonctionnalités en acceptant la pull-request.

Pour plus d'information sur la revue de code dans `GitHub®` : <https://github.com/features/code-review>.

_Les outils d'hébergement de dépôts Git comme GitHub permettent également de lier des pull-request à des "issues", ce qui permet d'identifier des commit, branches ou pull-request à un bug._


# Workflow Gitflow

Nous allons utiliser un workflow de type Gitflow pour maintenir à disposition de nos clients trois versions concurrents d'un produit : les versions `v1.0`, `v2.0` et `unstable`.

## Développement par versions

1. Créer un nouveau projet sur `Github®` et le partager avec les deux développeurs.
1. Créer une branche de développement qui servira à recevoir les fusions des fonctionnalités.
1. Ajouter une nouvelle fonctionnalité A à travers une branche dédiée.
1. Créer et livrer la première version `v1.0` du projet incluant la fonctionnalité A.
1. Ajouter une nouvelle fonctionnalité B au projet.
1. Créer et livrer la deuxième version `v2.0` du projet incluant les fonctionnalités A et B.

_Comment livrer la version `unstable` du projet ? Cette version doit inclure à tout instant les derniers développements stables du projet, même ceux qui ne font pas encore partie d'une version identifiée._

_Pour identifier les versions d'un projet : v1.0, v2.0 on pourra utiliser les [tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) de Git._

## Hotfix

_Un problème a été détecté sur la fonctionnalité A !_

Corriger une erreur dans la fonctionnalité A. Cette erreur devra être corrigée dans toutes les versions du produit.

\newpage{}

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.
