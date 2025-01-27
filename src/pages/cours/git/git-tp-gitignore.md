---
title: Gitignore
author: Tom Avenel
date: 2023 / 2024
keywords:
- git
- ci
- devops
---

## Le fichier spécial .gitignore

Le fichier spécial `.gitignore` (à placer directement dans le répertoire de travail de Git, sans sous-dossier) permet de lister des chemins de fichiers à ignorer lors d'un `git checkout ` : ces fichiers deviennent invisibles pour git.

Ce fichier contient un ensemble de patterns (répertoires, noms de fichiers, ...) à ignorer par Git. Par exemple, les fichiers compilés :

```gitignore
bin/
classes/
build/
*.out
*.pyc
*.javac
```

## Exemple

Sans `.gitignore`, Git détecte le répertoire `bin/` :

```
$ git checkout

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    bin/
```

Après ajout dans le `.gitignore` ce dossier disparaît :

Fichier `.gitignore` :

```gitignore
bin/
```

```
$ git checkout

Untracked files:
  (use "git add <file>..." to include in what will be committed)
```

## Exercice

- Créer un nouveau fichier `a.out` dans votre répertoire de travail. Vérifier que git détecte ce nouveau fichier en affichant le statut.
- Ajouter le `.gitignore` correspondant pour ignorer tous les fichiers ayant comme extension `.out` (fichiers compilés générés depuis du langage `C`).
- Vérifier que le fichier `a.out` n'est plus visible.
- En pratique, on utilise le `.gitignore` pour partager avec le reste de l'équipe les fichiers à ignorer de son répertoire de travail. Ajouter ce fichier dans un commit.
- Ajouter le fichier `a.out` quand même à un commit (il faudra peut-être forcer l'ajout).
- Modifier le contenu du fichier `a.out`. Afficher le statut : que peut-on en déduire ?

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
