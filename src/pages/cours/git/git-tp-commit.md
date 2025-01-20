---
title: TP Premiers pas avec Git™
author: Tom Avenel
date: 2023 / 2024
---

## Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

## Installation et configuration

Pour installer et configurer `git`, suivre les instructions du tutoriel OpenClassrooms : [lien](https://openclassrooms.com/fr/courses/7162856-gerez-du-code-avec-git-et-github/7165721-installez-git-sur-votre-ordinateur)

**Si vous n'êtes pas familier avec `vi`, attention à bien configurer un autre éditeur de votre choix** : `git config --global core.editor ...` . Cet éditeur servira uniquement pour les messages à ajouter aux commit : un simple `notepad` suffit.

Attention, sous Windows il faut remplacer `C:\...\mon_programme.exe` par des slash `/` en pensant à ajouter devant les caractères spéciaux (par exemple les espaces) un backslash : `\` : `C:\Program Files\mon_programme.exe` devient donc `C:/Program\ Files/mon_programme.exe`.

Par exemple, pour utiliser `vsCode` sous Windows avec le chemin par défaut : `git config --global core.editor "C:/Program\ Files/Microsoft\ VS\ Code/Code.exe --wait"`

::: tip
Si vous souhaitez utiliser `vsCode` comme éditeur, attention à bien ajouter l'option `--wait` à la commande : `git config --global core.editor "C:/.../code.exe --wait`. 
:::

Attention, il est possible d'entrer plusieurs configurations `core.editor`. En cas d'erreur, il faut donc commencer par supprimer toutes les références précédentes à `core.editor` avant d'en déclarer un nouveau : `git config --global --unset-all core.editor`

## Création d'un nouveau dépôt de code

Avant toute opération sur les fichiers, il nous faut créer un dépôt de code.
Ce dépôt nous servira à stocker les différentes versions de nos fichiers. 

Pour créer un dépôt, ouvrir un terminal dans le répertoire à utiliser et taper la commande :

```bash
$ git init
```

Cette commande crée un nouveau répertoire caché `.git` dans le répertoire courant : c'est une astuce simple pour vérifier que l'on travaille bien dans un dépôt git.

Attention, tous les fichiers utilisés par la suite devront être dans ce répertoire ou dans un sous-répertoire : c'est le `working directory` de `git`. `Git` ne peut pas voir les fichiers d'un autre répertoire ailleurs sur le système !

Pour visualiser simplement l'état du dépôt (modifications à intégrer, etc...) on pourra utiliser la commande :

```bash
$ git status
```

## Ajout d'un premier fichier au dépôt

### Créer un  nouveau fichier

Créer un nouveau fichier _index.html_ dans le répertoire de travail avec le contenu suivant :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph</p>
</body>
</html>
```

Consulter l'état du dépôt : le nouveau fichier est détecté mais est pour l'instant ignoré : status `untracked`.

```bash
$ git status

On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        index.html

nothing added to commit but untracked files present (use "git add" to track)
```

_Dans quel zone (working directory, staging, repository) le fichier index.html est-il actuellement ?_

Ce comportement par défaut est très pratique. Il est possible de "polluer" son répertoire de travail avec des fichiers qui ne seront jamais ajoutés au dépôt de code : fichiers binaires de compilation, fichiers temporaires, etc...

### Ajout du fichier à l'index git

Utiliser la commande `git add` pour ajouter ce nouveau fichier à l'index du dépôt git :

```bash
$ git add
```

_Dans quel zone (working directory, staging, repository) le fichier index.html est-il actuellement ?_

_A-t-on créé un nouvel historique du fichier dans git à cette étape ?_

La commande `git add` permet d'ajouter directement tout le contenu d'un nouveau répertoire. L'option `--all` permet d'ajouter à l'index tous les fichiers `untracked` : cette pratique est déconseillée car elle risque d'ajouter des fichiers non voulus.

La commande `git rm --cached` permet l'opération inverse (on utilise plus souvent le `reset` : voir TP suivant).

La commande `git add -p` permet interactivement d'ajouter ou non des morceaux de changements (chunks) pour chaque fichier.

### Création d'un premier commit

`Git` utilise une notion unique pour identifier tout changement dans les fichiers du dépôt : le _commit_. **Un commit est identifié par un _hash_ (identifiant unique) qui est immuable** : cet identifiant restera le même quelque soit la vie du commit. Cette propriété sera très utile lors de l'utilisation des branches.

**Attention : un commit correspond à un ensemble de modifications sur un ensemble de fichiers, il n'est pas possible de "mélanger" des commit proposant des modifications différentes directement (voir système de "merge" dans le prochain tp). Il est donc préconisé de créer des commit identifiant de petites modifications logiques plutôt qu'un système de "backup" à la fin de la journée.**

La commande `git log` permet d'afficher l'historique des commit sur le dépôt courant :

```bash
$ git log
```

_A-t-on déjà créé un commit dans le dépôt courant ? Pourquoi ?_

Créer un nouveau commit en utilisant la commande `git commit` :

```bash
$ git commit
```

Vérifier :
- que le nouveau commit a bien été créé (voir les logs de commit)
- qu'un changement n'est plus détecté dans notre fichier

_Dans quel zone (working directory, staging, repository) le fichier index.html est-il actuellement ?_

## Intégration de modifications

Dans l'étape précédente, nous avons créé un premier commit comportant une version initiale d'un document.

Nous allons voir maintenant comment intégrer des changements de ce document dans notre dépôt.

1. Changer le titre dans la balise title pour y ajouter votre nom (par exemple : `Welcome Tom`)
2. _Vérifier que `git` détecte bien un changement dans notre fichier : quelle commande utiliser ?_
3. Afficher les différences entre la working directory et le staging avec la commande : `$ git diff`
4. _Dans quel zone (working directory, staging, repository) le fichier index.html est-il actuellement ?_
5. Intégrer les changements dans un nouveau commit
6. Vérifier la bonne intégration de ces changements

\newpage{}

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
