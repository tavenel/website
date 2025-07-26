---
title: TP Git Grep
date: 2024 / 2025
---

# TP Git : Recherches dans un dépôt Git

## Introduction

Ce TP a pour objectif de vous apprendre à effectuer des recherches dans un dépôt Git en utilisant différentes commandes telles que `git grep`, `git log --grep`, et `git log -S`. Ces outils sont essentiels pour naviguer efficacement dans l'historique de votre projet et trouver des informations spécifiques.

## Recherche dans un dépôt Git

Pour rechercher le contenu d'un commit (c'est-à-dire les lignes de code source, par opposition aux messages de commit et autres), exécutez :

```sh
git grep "<regexp>" $(git rev-list --all)
```

Pour limiter la recherche récursivement à un sous-répertoire (par exemple, `lib/util`) :

```sh
git grep "<regexp>" $(git rev-list --all -- lib/util) -- lib/util
```

Autres méthodes de recherche utiles :

1. Rechercher dans une branche :
	```sh
	git grep "<regexp> origin/main"
	```
2. Rechercher depuis le répertoire courant le texte correspondant à l'expression régulière regexp :
	```sh
	git grep "<regexp>"
	```
3. Afficher uniquement les chemins d'accès aux fichiers :
	```sh
	git grep -l "<regexp>"
	```
4. Rechercher les commits contenant à la fois `regexp1` et `regexp2` :
	```sh
	git grep --all-match -e <regexp1> -e <regexp2>
	```
5. Rechercher les lignes de texte modifiées correspondant au motif :
	```sh
	git diff --unified=0 | grep <pattern>
	```
6. Rechercher du texte correspondant à l'expression régulière regexp dans tous les commits entre `rev1` et `rev2` :
	```sh
	git grep <regexp> $(git rev-list "<rev1>..<rev2>")
	```
7. Recherche _pickaxe_ : rechercher les changements ayant ajouté ou supprimé une chaîne de caractères (`-p` affiche l'auteur, la date et le diff):
	```sh
	git log -S "FIXME" -p
	```
8. Chercher dans les messages de commits :
	```sh
	git log --grep "TODO"
	```

## Recherche dans le contenu des fichiers avec `git grep`

1. Utilisez la commande suivante pour rechercher une chaîne de caractères dans tous les fichiers trackés :
     ```sh
     git grep "search_string"
     ```
   - Remplacez `"search_string"` par le texte que vous souhaitez rechercher.
2. Pour afficher les numéros de ligne où les correspondances sont trouvées :
     ```sh
     git grep -n "search_string"
     ```
3. Pour effectuer une recherche insensible à la casse :
     ```sh
     git grep -i "search_string"
     ```

## Recherche dans les messages de commit avec `git log --grep`

1. Utilisez la commande suivante pour rechercher un mot ou une phrase dans les messages de commit :
     ```sh
     git log --grep="search_string"
     ```
   - Remplacez `"search_string"` par le texte que vous souhaitez rechercher.
2. Pour effectuer une recherche insensible à la casse :
     ```sh
     git log --grep="search_string" -i
     ```
3. Pour limiter les résultats aux commits qui correspondent à tous les motifs donnés :
     ```sh
     git log --grep="pattern1" --grep="pattern2" --all-match
     ```

## Partie 3 : Recherche des modifications de texte avec `git log -S`

1. Utilisez la commande suivante pour trouver les commits où une chaîne de caractères a été modifiée :
     ```sh
     git log -S "search_string"
     ```
   - Remplacez `"search_string"` par le texte que vous souhaitez rechercher.
2. Pour effectuer une recherche insensible à la casse :
     ```sh
     git log -S "search_string" -i
     ```
3. Pour afficher les différences introduites par chaque commit :
     ```sh
     git log -S"search_string" -p
     ```

## Exercices Pratiques

1. **Recherche de TODOs** :
   - Utilisez `git grep` pour trouver tous les commentaires TODO dans votre codebase.
   - Utilisez `git log --grep` pour trouver les commits mentionnant "TODO" dans leurs messages.
2. **Suivi d'une fonction** :
   - Utilisez `git log -S` pour trouver les commits où une fonction spécifique a été modifiée.
   - Comparez les résultats avec ceux obtenus en utilisant `git grep` pour rechercher la même fonction dans les fichiers.
3. **Recherche de bugs** :
   - Utilisez `git log --grep` pour trouver les commits mentionnant "bug" ou "fix" dans leurs messages.
   - Analysez les résultats pour comprendre l'historique des corrections de bugs dans votre projet.

