---
title: TP Partager un script ou un morceau de code - Gist®
date: 2025 / 2026
tags:
- git
- github
---

## Github Gist

Gist est un service fourni par GitHub. C'est un moyen simple de partager en public ou en privé des extraits de code, de notes, de listes de tâches, ...

Un _Gist_ (public ou privé) peut se partager avec uniquement une URL "secrète", ce qui permet de faciliter l'automatisation.

## Comment utiliser _Gist_ ?

Pour utiliser _Gist_, il faut :

- Se rendre sur [GitHub](https://github.com)
- Se connecter avec son compter
- Cliquer sur le bouton `+` en haut à droite
- Cliquer sur `New gist` (redirige vers <https://gist.github.com>).

## Public / Privé

Lors de la création d'un _Gist_, il est possible de configurer celui-ci en public ou privé :

- _Secret gist_ : accessible uniquement aux utilisateurs ayant le lien vers le _Gist_;
- _Public gist_ : accessible à tous et indexé publiquement.

## Lien avec Git

Un _Gist_ est en réalité un dépôt _Git_ (avec quelques contraintes sur ce qu'il est possible de pusher).

Il est donc possible de _cloner_ le dépôt, effectuer des changements et _pusher_ ceux-ci sur _Github_.

Attention cependant, de nombreuses fonctions avancées de _Git_ (branches, ...) seront ignorées par _Gist_.

## Intégration dans un script

Les _Gist_ sont très facilement intégrables dans des scripts puisqu'il suffit d'avoir l'URL d'un Gist pour le récupérer.

Créer un script permettant de cloner le Gist précédent (par exemple en utilisant `curl`).

## Ressources

- [Documentation Gist](https://docs.github.com/fr/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)
- Pour parcourir les Gist publiques : <https://gist.github.com>
