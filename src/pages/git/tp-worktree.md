---
title: TP Git Worktree
date: 2025 / 2026
---

## Présentation

`git worktree` est une fonctionnalité qui permet de créer plusieurs répertoires de travail (working directories) associés à un même dépôt Git. Cela vous permet de travailler **simultanément sur plusieurs branches** sans avoir à cloner le dépôt plusieurs fois ni à stash/changer de branche en permanence.

Chaque worktree est **indépendant** : vous pouvez y faire des commits sans impacter les autres répertoires de travail.

:::tip
Les worktrees sont particulièrement utiles quand vous travaillez sur une fonctionnalité et devez basculer rapidement sur une correction de bug urgente, ou pour relire une PR tout en continuant à coder.
:::

## Objectifs

1. Comprendre le concept de worktree et son utilité
2. Créer, lister et supprimer des worktrees
3. Travailler simultanément sur plusieurs branches
4. Utiliser un dépôt bare comme hub central de worktrees
5. Connaître les bonnes pratiques et limitations

## Prérequis

- Git installé (v2.5+ — `git worktree` est disponible depuis cette version)
- Un dépôt Git existant avec au moins une branche secondaire

## Lister les worktrees existants

Avant toute manipulation, observons la configuration actuelle :

```sh
git worktree list
```

Vous devriez voir une seule entrée : votre répertoire courant, avec la branche active.

:::exo
Exécutez `git worktree list` et notez le chemin absolu, le commit pointé et la branche active.
:::

## Créer un worktree

La commande de base pour ajouter un worktree :

```sh
git worktree add <chemin> <branche>
```

**Exemple** : travailler sur `feature-A` dans un dossier séparé :

```sh
git worktree add ../tp-worktree-feature-A feature-A
```

:::exo

1. Créez un worktree pour la branche `feature-A` dans `../tp-worktree-feature-A`.
2. Déplacez-vous dans ce nouveau répertoire : `$ cd ../tp-worktree-feature-A`
3. Vérifiez que vous êtes bien sur la branche `feature-A` avec `$ git status`.
4. Créez un fichier `feature.txt` et commitez-le : `$ echo "A" > feature.txt && git add feature.txt && git commit -m "Ajout feature A"`

:::

:::tip
Le chemin du worktree peut être absolu ou relatif. Le worktree **crée automatiquement la branche** si elle n'existe pas. Utilisez `git worktree add -b <nouvelle-branche> <chemin>` pour créer un worktree sur une **nouvelle** branche.
:::

## Worktree sur une nouvelle branche

```sh
git worktree add -b feature-C ../tp-worktree-feature-C
```

:::exo
Créez un worktree sur une **nouvelle** branche `feature-C`, positionné dans `../tp-worktree-feature-C`. Vérifiez avec `git worktree list` que les deux worktrees apparaissent.
:::

:::correction

```sh
git worktree add -b feature-C ../tp-worktree-feature-C
git worktree list
```

Vous devriez voir trois entrées : le dépôt d'origine, `tp-worktree-feature-A` et `tp-worktree-feature-C`.
:::

## Indépendance des worktrees

L'intérêt principal des worktrees est leur indépendance.

:::exo

1. Restez dans `tp-worktree-feature-C` et modifiez `feature.txt` en y ajoutant une ligne "C".
2. Commitez : `$ git add feature.txt && git commit -m "Ajout feature C"`
3. Revenez dans le dépôt initial : `$ cd ../tp-worktree`
4. Allez dans `tp-worktree-feature-A` : `$ cd ../tp-worktree-feature-A`
5. Vérifiez que le `feature.txt` n'a **pas** été modifié (il contient toujours "A").

:::

:::warn
**Contrainte importante** : Git ne permet pas de checkout de la **même branche** dans deux worktrees différents, sauf si l'un des deux est en mode détaché (detached HEAD). Vous obtiendrez une erreur du type : `fatal: 'feature-A' is already checked out at '...'`.
:::

## Déplacer un worktree

Vous pouvez déplacer un worktree vers un autre emplacement :

```sh
git worktree move <ancien-chemin> <nouveau-chemin>
```

:::exo
Déplacez le worktree `tp-worktree-feature-C` vers `../tp-feature-C-deplace` :

```sh
git worktree move ../tp-worktree-feature-C ../tp-feature-C-deplace
git worktree list
```

:::

## Verrouiller un worktree

Un worktree peut être **verrouillé** pour éviter qu'il ne soit supprimé accidentellement (par exemple si son disque est démonté).

```sh
git worktree lock <chemin>
git worktree unlock <chemin>
```

:::exo
Verrouillez `tp-worktree-feature-A`, puis observez l'état dans `git worktree list` (une mention `locked` apparaît). Déverrouillez-le ensuite.
:::

## Nettoyer et supprimer un worktree

Pour supprimer un worktree, deux options :

```sh
git worktree remove <chemin>
```

Si le worktree contient des modifications non commit :

```sh
git worktree remove --force <chemin>  # attention : supprime sans vérification
```

:::exo

1. Supprimez le worktree déplacé `../tp-feature-C-deplace` avec `git worktree remove`.
2. Vérifiez avec `git worktree list` qu'il a bien disparu.

:::

:::warn
Supprimez toujours un worktree via `git worktree remove` plutôt qu'avec `rm -rf`. La commande `remove` nettoie aussi les métadonnées internes de Git (fichiers dans `.git/worktrees/`).
:::

## Nettoyage des worktrees orphelins

Si un worktree a été supprimé avec `rm -rf` sans passer par `git worktree remove`, des fichiers résiduels traînent dans `.git/worktrees/`. Pour les nettoyer :

```sh
git worktree prune
```

:::exo

1. Supprimez « manuellement » le dossier `../tp-worktree-feature-A` : `$ rm -rf ../tp-worktree-feature-A`
2. Lancez `$ git worktree prune` puis `$ git worktree list` : l'entrée orpheline a disparu.

:::

## Worktree avec dépôt bare

Une utilisation avancée consiste à créer un dépôt **bare** puis à y attacher tous ses worktrees. C'est la configuration recommandée pour avoir un **répertoire central unique** pour un projet.

```sh
mkdir ~/mon-projet && cd ~/mon-projet
git init --bare
git worktree add ../main main     # dépôt bare, pas de checkout automatique
git worktree add ../feature-x feature-x
```

C'est notamment la configuration utilisée par des outils comme `jj` (Jujutsu) ou par des scripts d'automatisation.

## Worktree en mode detached HEAD

Vous pouvez attacher un worktree à un commit spécifique sans branche :

```sh
git worktree add --detach ../detache <sha-du-commit>
```

:::tip
Utile pour inspecter un état ancien du projet sans créer de branche.
:::

## Récapitulatif des commandes

| Commande | Description |
|---|---|
| `git worktree list` | Lister les worktrees |
| `git worktree add <path> <branch>` | Créer un worktree |
| `git worktree add -b <new-branch> <path>` | Créer un worktree avec une nouvelle branche |
| `git worktree add --detach <path> <commit>` | Worktree en detached HEAD |
| `git worktree move <old> <new>` | Déplacer un worktree |
| `git worktree remove <path>` | Supprimer un worktree |
| `git worktree lock <path>` | Verrouiller un worktree |
| `git worktree unlock <path>` | Déverrouiller un worktree |
| `git worktree prune` | Nettoyer les worktrees orphelins |

## Bonnes pratiques

- Utilisez des noms de dossiers explicites : `../mon-projet-hotfix`, `../mon-projet-feature-X`
- Préférez `git worktree remove` à `rm -rf` pour la suppression
- Les worktrees partagent le même répertoire `.git` : toute opération de garbage collection (`git gc`) impacte tous les worktrees
- Évitez de modifier les fichiers `.git/worktrees/` à la main
- Un worktree sur un disque externe ou réseau peut être verrouillé (`lock`) pour éviter des erreurs de prune

# Legal

- © 2026 Tom Avenel under CC BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
