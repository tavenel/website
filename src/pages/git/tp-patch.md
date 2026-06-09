---
title: TP Patching
date: 2025 / 2026
tags:
- git
---

## Ajout partiel de modifications

Git supporte l'ajout de fichiers par morceaux (_hunks_) en utilisant la commande `git add --patch`. Cela permet de ne pas intégrer tous les changements d'un fichier d'un coup, par exemple si vous avez travaillé sur 2 fonctionnalités en même temps dans le même fichier de code.

## Mode interactif

Git fournit un mode interactif permettant d'ajouter ou non les `hunk` (morceaux de modifications) détectées automatiquement grâce à la commande `git add --patch`.

Le mode patch permet principalement les opérations suivantes :

- `y` : ajouter les modifications présentées
- `n` : ne pas ajouter les modifications présentées
- `q` : quitter et annuler
- `a` : ajouter les modifications présentées et toutes les suivantes
- `d` : ne PAS ajouter les modifications présentées NI toutes les suivantes
- `s` : séparer le bloc de modifications affichées en sous-blocs à traiter individuellement

1. Créer un nouveau fichier et taper 2 paragraphes de texte.
2. Ajouter ce nouveau fichier (entièrement).
3. Créer un commit contenant une première version du fichier.
4. Modifier les 2 paragraphes de texte.
5. Utiliser la commande `git add --patch mon_fichier` pour passer en mode interactif et ajouter seulement les modifications du premier paragraphe. On pourra séparer le bloc de modifications si besoin. Créer un commit.
6. Vérifier l'état actuel des changements avec les commandes `git status` et `git diff`.
7. Utiliser de nouveau l'option `patch` pour ajouter le 2e paragraphe et créer un nouveau commit.

## Mode édition

Git fournit un mode édition permettant de modifier le _diff_ à intégrer : `git add --edit mon_fichier`. Cela ne modifie pas le contenu actuel du fichier, seulement les changements dans git. La commande `--edit` ouvre le diff total dans un éditeur de texte et permet ainsi à l'utilisateur de modifier le diff à intégrer.

Le _diff_ se compose :

- de lignes `+` représentant les lignes ajoutées (ou les nouvelles versions des modifications). Pour ne pas les intégrer, il suffit de les supprimer.
- de lignes `-` représentant les lignes supprimées (ou les anciennes lignes modifiées). Pour annuler leur suppression ou laisser l'ancienne version, il suffit de remplacer le `-` par un espace.

1. Reprendre le fichier précédent et modifier les 2 paragraphes de texte.
2. Avec la commande `git add -e` ajouter uniquement les changements du 1er paragraphe. Réaliser un deuxième commit.
3. Ajouter les changements du 2e paragraphe dans un troisième commit.
