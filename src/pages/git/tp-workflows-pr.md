---
title: Les workflows Git™ et la pull-request
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

```sh
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

:::correction

## Correction

```sh
#!/bin/bash

echo '# Création du dépot'
git init exam-workflows-concurrents-correction
cd exam-workflows-concurrents-correction
git status

echo '## Création de la branche v1'
git checkout -b v1
git status
echo '## Création du commit dans v1'
echo -e "Versios\nv1" > contenu.txt
git status
git add contenu.txt
git diff --staged
git commit -m 'v1'
git status
git log --decorate --graph

echo '## Création de la branche v2'
git checkout -b v2
echo '## Ajout des changements et Création du commit dans v2'
echo "v2" >> contenu.txt
git add contenu.txt
git commit -m 'v2'

echo '## Création de la branche dev'
git checkout -b dev
echo '## Ajout des changements et Création du commit dans dev'
echo "v3" >> contenu.txt
git add contenu.txt
git commit -m 'v3'
git log --oneline --decorate --graph --all

echo '# Ajout de fonctionalité'
echo '#E Création de la branche f1 depuis dev'
git checkout dev
git checkout -b f1
echo '## Ajout des changements et Création du commit dans dev'
echo "F1" >> contenu.txt
git add contenu.txt
git commit -m 'F1'
git log --oneline --decorate --graph --all
echo '## Fusion de f1 dans dev'
git checkout dev
git merge f1

echo '# Nouvelle version mineure'
echo '## Ajout des changements et Création du commit dans v2'
git checkout v2
sed -i s/v2/v2.1/g contenu.txt # ou depuis un éditeur de texte
git status
git add contenu.txt
git commit -m 'v2.1'
git log --oneline --decorate --graph --all

echo '# Portage de correctif'
echo '## On se déplace sur la branche v1'
git checkout v1
echo '## On crée une nouvelle branche (depuis "v1")'
git checkout -b fix-typo
echo '## On corrige la typo et on crée un nouveau commit'
sed -i s/Versios/Versions/g contenu.txt # ou depuis un éditeur de texte
git commit -am 'typo versios'
echo '## On effectue une "Merge-Request" sur GitHub de fix-typo vers v1 et on la valide.'
echo '## On merge fix-typo dans v1 en se déplaçant dans "v1"'
git checkout v1
git merge fix-typo
echo '## Puis on merge fix-typo dans les autres branches...'
git checkout v2
git merge -m 'Merging branch fix-typo' fix-typo
git checkout dev
git merge -m 'Merging branch fix-typo' fix-typo
git log --decorate --graph --all

echo "## Autre solution plus propre : utiliser git cherry-pick pour récupérer uniquement le commit désiré (si la branche contenait d'autres changements indésirables)"
```

:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.
