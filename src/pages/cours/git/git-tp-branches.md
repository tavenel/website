---
title: TP Le systeme de branches
author: Tom Avenel
date: 2023 / 2024
---

## Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

## Afficher la liste des branches

Pour afficher les branches de notre projet, on utilise la commande `$ git branch`. Une première branche a été créée avec notre dépôt : c'est cette branche que l'on a utilisé dans les autres TP.

```bash
$ git branch # liste des branches locales
```

`Git` étant décentralisé, la notion de branche est locale à un dépôt. Pour afficher les branches disponibles dans les dépôts distants (`upstream`), on peut utiliser la commande suivante :

```bash
$ git branch -a # liste des branches distantes
```

## Créer et se déplacer dans une nouvelle branche

Créer deux nouvelles branches et modifier la position de la `HEAD` pour utiliser une de ces nouvelles branches.

On utilisera les commandes suivantes :

```bash
$ git branch ma_nouvelle_branche # crée une nouvelle branche
```

```bash
$ git checkout ma_nouvelle_branche # se déplace vers la branche
```

```bash
$ git checkout -b une_branche # crée et se déplace sur la branche
```

Utiliser la commande `$ git status` pour vérifier le positionnement sur la nouvelle branche.

:::tip
`git switch` est une nouvelle commande git simplifiée et spécialisée pouvant remplacer `git checkout` pour la gestion des branches : `git switch <branche_existante>` pour changer de branche (existante) et `git switch -c <nouvelle_branche>` pour créer une nouvelle branche.
:::

## Supprimer une branche

Supprimer la nouvelle branche non utilisée :

```bash
$ git branch -d branche_a_supprimer
```

## Intégrer des commit dans la branche

Effectuer des changements dans le working directory puis intégrer ces changements dans un commit de la branche.

Vérifier la bonne intégration des changements.

**Rappel : `git` identifie tous les changements à travers les commit.** Aucun historique de fichier n'est donc stocké dans une branche : les branches ne sont que des pointeurs et des listes d'identifiants de commit. Ce modèle s'avère très puissant pour déplacer ou partager des commit entre branches : il suffit de modifier des pointeurs. A aucun moment un commit n'est modifié.

## Envoyer la branche vers un dépôt distant

Lors de la création d'une branche, celle-ci est liée au dépôt de code local.
Pour l'intégrer dans un dépôt distant, il faut la lier au dépôt distant (`upstream`) la première fois.

```bash
$ git push --set-upstream origin new-branch
```

Cette commande ne fonctionne que si vous souhaitez créer une branche avec le même nom que la branche locale. Dans le cas contraire, on utilisera la version complète de `$ git push` en spécifiant un upstream :

```bash
$ git push -u origin branche_locale:branche_distante
```

Les opérations suivantes d'envoi pourront se satisfaire d'un simple `$ git push`.

Note : si la branche a été récupérée depuis un dépôt distant, son `upstream` est déjà configuré.

## Fusionner la branche

Une fois satisfait des changements réalisés dans la branche, nous allons intégrer les intégrer à la branche principale par une opération de fusion.

### Opération de merge

Réaliser un merge de la nouvelle branche dans la branche principale :

1. Se déplacer dans la branche principale.
2. Créer une nouvelle branche `a-merger` depuis la branche principale et créer un nouveau commit avec un changement dans cette branche.
3. Se placer dans la branche principale.
4. Réaliser l'opération de merge : `$ git merge a-merger`
5. Vérifier l'historique des branches.

Note : si des changements on été réalisés dans la branche de destination, on préfèrera ajouter ces changements dans la branche source avant la fusion. Cela permet de réaliser une opération de merge dans la branche `new-branch` et non dans la branche `main` : le risque est ainsi contraint à la branche du développeur et non à la branche publique. On pourra tester localement la version fusionnée avant de la publier.

### Opération de rebase

A la place d'un merge, il est aussi possible d'effectuer un rebase de cette branche sur la branche principale :

1. Se déplacer dans la branche principale.
2. Créer une nouvelle branche `a-rebase` depuis la branche principale et créer un nouveau commit avec un changement dans cette branche.
3. Réaliser l'opération de rebase : `$ git rebase main`
4. Vérifier l'historique des branches.

- Pour plus d'informations sur le principe délicat du rebase, voir l'excellent guide : [merge vs rebase](https://www.atlassian.com/fr/git/tutorials/merging-vs-rebasing)
- Voir aussi le très complet tutoriel de SourceHut : <https://git-rebase.io/>

## [Bonus] Squash de commit

Une option intéressante au moment du d'une branche est la possibilité de réécrire la suite de commit à intégrer en un commit unique. Cela évite de polluer l'historique avec les commit utilisés pendant le développement.

```bash
$ git merge --squash ma_branche
```

Une opération de squash est également possible par rebase intéractif, par exemple, la commande suivante rassemble les 3 derniers commit en un seul :

```bash
$ git rebase -i HEAD~3
```

## [Bonus] Réordonner les commit

Il est possible de réordonner des commit pendant une opération de rebase interactif : il suffit de sélectionner (`pick`) les commit dans un ordre différent de l'ordre actuel.

```bash
$ git rebase -i HEAD~3
# pick ...
# pick ...
# pick ...
```

## [Bonus] La stash

Nous avons vu qu'il existe 3 espaces de travail dans `git` :

- le `working directory`
- le `staging`
- la zone de `commit`

En réalité, il existe virtuellement une 4e zone appelée la `stash` permettant de mettre temporairement de côté des modifications.

1. Modifier un fichier de l'espace de travail
2. Vérifier qu'il existe des changements à intégrer : `$ git status`
3. Mettre de côté ces changements : `$ git stash --all`
4. Vérifier que les changements ont disparu : `$ git status`
5. Se déplacer dans une autre branche : `$ git checkout .....`
6. Récupérer les modifications en cours : `$ git stash pop`

_La stash est très utile lorsque l'on s'est trompé de branche de travail._

## [Bonus] Cherry-picking

Il peut arriver d'avoir besoin d'intégrer les modifications apportées par un commit dans deux branches différentes à la fois (par exemple : correction isolée d'un bug critique sur différentes versions ayant divergé). Une opération de fusion n'est alors pas appropriée car elle obligerait à intégrer tous les changements d'une branche.

Dans ce cas, la commande `git cherry-pick` permet d'intégrer n'importe quel commit (situé dans n'importe quelle branche) dans la branche courante.

```bash
$ git checkout branche_contenant_le_commit
$ git cherry-pick identifiant_du_commit_à_intégrer
```

\newpage{}

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries

