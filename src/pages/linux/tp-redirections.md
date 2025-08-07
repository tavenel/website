---
title: TP - Utilisation des flux, des pipes et des redirections 
date: 2024 / 2025
---

## Cours

:::tip
- Voir cours LPIC-1 section _A Quick Review on Redirections and Pipes_, 103.2 Lesson 1 p.194
- Voir cours LPIC-1 section _Redirects_, 103.4 Lesson 1 p.267
:::

## Travaux Pratiques

1. La commande `find /` retourne beaucoup d’erreurs si elle est utilisée par un simple utilisateur à cause d’un problème de droits. Évitez les messages d’erreurs en les redirigeant vers un _trou noir_
2. Dans le cas précédent et malgré les erreurs, vous avez encore accès à beaucoup d’emplacements et la liste qui s’affiche est très longue et donc inexploitable. Placez cette liste dans un fichier appelé `résultat`.
3. Maintenant, plus rien ne s’affiche. En fin de compte, pour savoir pourquoi vous ne pouvez pas accéder à certains répertoires vous voulez aussi obtenir les messages d’erreurs dans le fichier `résultat`, avec la liste des fichiers. Faites une redirection du canal d’erreur standard dans le canal de sortie standard.
4. Plus rien ne s’affiche. Vous voulez les deux : un fichier et l’affichage des résultats sur écran. La commande `tee` s’utilise avec un tube et permet de récupérer un flux sortant, de le placer dans un fichier et de ressortir ce flux comme si de rien n’était.
5. `xargs` est une commande UNIX puissante qui permet de récupérer les arguments en sortie de la commande précédente et de les traiter à travers un pipe. Utiliser `xargs` pour chercher le pattern `127.0.0.1` dans tout fichier de `/etc`.
6. Utiliser `xargs` pour compter le nombre de lignes de tous les fichiers `.md` présents récursivement dans un répertoire et trier ces fichiers par nombre de lignes croissant.

:::correction
1. La commande `find /` retourne beaucoup d’erreurs si elle est utilisée par un simple utilisateur à cause d’un problème de droits. Évitez les messages d’erreurs en les redirigeant vers un _trou noir_

```sh
find / 2>/dev/null
```

2. Dans le cas précédent et malgré les erreurs, vous avez encore accès à beaucoup d’emplacements et la liste qui s’affiche est très longue et donc inexploitable. Placez cette liste dans un fichier appelé `résultat`.

```sh
find / 1>resultat 2>/dev/null
```

3. Maintenant, plus rien ne s’affiche. En fin de compte, pour savoir pourquoi vous ne pouvez pas accéder à certains répertoires vous voulez aussi obtenir les messages d’erreurs dans le fichier `résultat`, avec la liste des fichiers. Faites une redirection du canal d’erreur standard dans le canal de sortie standard.

```sh
find / >resultat 2>&1
```

4. Plus rien ne s’affiche. Vous voulez les deux : un fichier et l’affichage des résultats sur écran. La commande `tee` s’utilise avec un tube et permet de récupérer un flux sortant, de le placer dans un fichier et de ressortir ce flux comme si de rien n’était.

```sh
find / 2>&1 | tee resultat.
```

Le fichier `résultat` contient la liste de tous les fichiers accessibles, les erreurs et le tout s’affiche aussi sur l’écran.

5. `xargs` est une commande UNIX puissante qui permet de récupérer les arguments en sortie de la commande précédente et de les traiter à travers un pipe. Utiliser `xargs` pour chercher le pattern `127.0.0.1` dans tout fichier de `/etc`.

```sh
find /etc -type f | xargs grep '127.0.0.1'
```

6. Utiliser `xargs` pour compter le nombre de lignes de tous les fichiers `.md` présents récursivement dans un répertoire et trier ces fichiers par nombre de lignes croissant.

```sh
find MON_REP -type f -name '*.md' | xargs wc -l | sort
```
:::
