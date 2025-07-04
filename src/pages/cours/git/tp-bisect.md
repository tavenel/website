---
title: TP Git Bisect
date: 2024 / 2025
---

## Introduction

`Git Bisect` est une fonctionnalité puissante de Git qui permet de localiser rapidement la cause d'un problème en effectuant des tests binaires par dichotomie. On attribue un état `good` ou `bad` aux commits de début (1) et de fin (2), puis on regarde le commit au milieu de l'intervalle (3). On réitère alors le procédé dans le 1/2 intervalle (1-3) ou (3-2), et ainsi de suite jusqu'à avoir atteint le commit que l'on recherche.

## Objectifs

1. Comprendre le fonctionnement de Git Bisect
2. Apprendre à l'utiliser pour résoudre un problème spécifique
3. Analyser les résultats et identifier la commit coupable

## Étapes du TP

### 1. Préparation

1. Créez un nouveau dépôt Git ou utilisez un existant
2. Ajoutez quelques commits avec des modifications aléatoires
3. Introduisez un bug dans l'un des derniers commits

### 2. Lancement de Git Bisect

1. Dans votre terminal, naviguez vers le répertoire du projet
2. Lancez la commande suivante :
   ```
   git bisect start
   ```
3. Répondez aux questions de Git Bisect :
   - Quel est l'état actuel du projet ? (good/bad)
   - Quelle est le dernièr commit connu où le problème n'était pas présent ?

### 3. Test et analyse

1. Git Bisect va maintenant vous guider à travers les commits
2. Pour chaque commit testé, vérifiez si le problème est présent ou non
3. Si le problème est présent, tapez `git bisect bad`
4. Sinon, tapez `git bisect good`

### 4. Résolution

1. Une fois que Git Bisect a terminé, il affichera la commit coupable
2. Vérifiez manuellement ce commit pour confirmer qu'il contient bien le bug

### 5. Nettoyage

1. Pour terminer Git Bisect, utilisez la commande :
   ```
   git bisect reset
	 ```

