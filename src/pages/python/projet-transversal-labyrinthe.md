---
title: SN1 EPSI - Projet transversal - Labyrinthe
date: 2023 / 2024
---

# Projet transversal - le labyrinthe du Minotaure

## Présentation

> Dans la mythologie grecque, le Minotaure est un monstre fabuleux au corps d'un homme et à tête d'un taureau ou mi-homme et mi-taureau.
>
> Né des amours de Pasiphaé (épouse du roi Minos) et d'un taureau blanc envoyé par Poséidon, il est enfermé par Minos dans le labyrinthe. Situé au centre de la Crète, le labyrinthe est construit spécialement par Dédale afin que le Minotaure ne puisse s'en échapper et que nul ne découvre son existence. [...] Thésée, fils d'Égée, sera volontaire pour aller dans le labyrinthe et tuera le monstre. (source : Wikipedia)

L'objectif de ce projet est de recréer le labyrinthe et de permettre à Thésée d'atteindre le Minotaure puis de sortir du labyrinthe.

Les sections ci-dessous décrivent les différents éléments du programme et peuvent être réalisées pour la plupart en parallèle. Pour cette raison, celles-ci ont été découpées en plusieurs versions : on commencera donc par faire marche toutes les 1ères versions ensemble avant de passer aux versions suivantes.

## Le labyrinthe

- Le plateau de jeu est à réaliser sur la console ;
- Le labyrinthe est un plateau de jeu à 2 dimensions ;
- Il doit contenir au moins une entrée (pouvant servir de sortie) et éventuellement d'autres sorties ;
- Le labyrinthe contient des murs infranchissables ;
- Le labyrinthe contient des passages secrets : en les empruntant, Thésée se retrouve ailleurs dans le labyrinthe (n'importe où au choix du développeur). Les passages secrets marchent par paires et peuvent être bidirectionnels (ou non), au choix des développeurs.

### Version 1 - Un premier labyrinthe

Pour la première version, créer un petit labyrinthe codé en dur dans le programme - ce sera donc toujours le même plateau qui sera utilisé.

### Bonus : Version 2 - Génération de cartes aléatoires

Le labyrinthe doit pouvoir être généré aléatoirement à chaque partie. On choisira uniquement la taille du labyrinthe. _Attention, il doit y avoir un chemin permettant d'atteindre le Minotaure !_

## Thésée

- Le joueur joue Thésée, à la recherche du Minotaure.
- Le plateau de jeu doit représenter la position de Thésée sur une case du labyrinthe.
- Le joueur peut déplacer Thésée en appuyant sur les flèches du clavier.

### Le fil d'Ariane

Afin d'aider Thésée à retrouver son chemin dans le labyrinthe, Ariane lui fournit une pelote de fil.

Représenter sur le plateau le déplacement déjà réalisé par Thésée à chaque instant.

## Le Minotaure

### Version 1 - un Minotaure statique

Dans cette première version, le Minotaure est statique, c'est-à-dire qu'il représente uniquement une case du labyrinthe qu'il faut atteindre.

### Version 2 - le Minotaure se déplace

Dans cette 2ème version, le Minotaure se déplace aléatoirement dans le labyrinthe d'une case à chaque déplacement de Thésée (ils vont donc à la même vitesse).

### Bonus : Version 3 - un Minotaure intelligent

Dans cette dernière version (en bonus), le Minotaure entend l'arrivée de Thésée et essaie de s'en éloigner le plus possible. On pourra ensuite optimiser cette version pour ne fuir que lorsque Thésée est suffisamment proche pour être entendu (par exemple, à partir d'une distance euclidienne de 4 cases).

## Score

On ajoutera une gestion du score : le joueur commence avec un certain nombre de points, chaque déplacement fait perdre des points.

### Version 1

Le but est d'atteindre le Minotaure le plus rapidement possible afin de gagner le maximum de points.

### Version 2

On ajoutera un système de gestion des meilleurs scores qui seront enregistrés en base de données.

## Condition de victoire

Le joueur a gagné la partie lorsque :

- Le Minotaure a été atteint par Thésée...
- ...**et** Thésée est sorti du labyrinthe.

## Sauvegarde

1. Ajouter une fonction dans l'interface permettant une sauvegarde de la partie courante en base de données.
2. Ajouter une fonction dans l'interface permettant une charger la partie sauvegardée et de continuer la partie.

# Rendus attendus et évaluation

Le projet est à réaliser en binôme. Le projet sera noté, à part égales, par 3 types d'évaluations :

## Le rapport

Chaque binôme devra fournir un rapport résumant la réalisation de leur projet. Ce rapport est un rapport technique devant inclure :

- un court rappel du projet et des fonctionnalités attendues ;
- l'architecture de votre projet ;
- les choix techniques réalisés ;
- les spécificités de votre application ;
- les soucis rencontrés ;
- des axes d'amélioration pour le futur.

## La soutenance

Chaque binôme devra présenter sa solution lors d'une soutenance de **30 minutes** : **15 minutes** de présentation et **15 minutes** de questions.

Attention, il ne s'agit pas de lire le rapport ou de le recopier dans quelques slides, mais bien de présenter le projet à un jury qui ne connaîtrait pas votre réalisation. Il est fortement conseillé d'inclure une démonstration de votre rendu.

## Le produit

Le rendu devra également inclure le rendu du **produit**, c'est-à-dire un **livrable** à fournir aux utilisateurs :

- code source prêt pour la production (code nettoyé, commenté, ...) ;
- un document d'installation ;
- un manuel utilisateur.
- un programme exécutable (et non un simple fichier Python) : voir <https://www.pyinstaller.org/> par exemple.

