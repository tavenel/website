---
title: TP Partager un script ou un morceau de code - Gist®
author: Tom Avenel
date: 2023 / 2024
---

## Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

## Github Gist

Gist est un service fourni par GitHub. C'est un moyen simple de partager en public ou en privé des extraits de code, de notes, de listes de tâches, ...

Un _Gist_ (public ou privé) peut se partager avec uniquement une URL "secrète", ce qui permet de faciliter l'automatisation.

### Comment utiliser _Gist_ ?

Pour utiliser _Gist_, il faut :

- Se rendre sur [GitHub](https://github.com)
- Se connecter avec son compter
- Cliquer sur le bouton `+` en haut à droite
- Cliquer sur `New gist` (redirige vers <https://gist.github.com>).

### Public / Privé

Lors de la création d'un _Gist_, il est possible de configurer celui-ci en public ou privé :

- _Secret gist_ : accessible uniquement aux utilisateurs ayant le lien vers le _Gist_;
- _Public gist_ : accessible à tous et indexé publiquement.

### Lien avec Git

Un _Gist_ est en réalité un dépôt _Git_ (avec quelques contraintes sur ce qu'il est possible de pusher).

Il est donc possible de _cloner_ le dépôt, effectuer des changements et _pusher_ ceux-ci sur _Github_.

Attention cependant, de nombreuses fonctions avancées de _Git_ (branches, ...) seront ignorées par _Gist_.

### Intégration dans un script

Les _Gist_ sont très facilement intégrables dans des scripts puisqu'il suffit d'avoir l'URL d'un Gist pour le récupérer.

Créer un script permettant de cloner le Gist précédent (par exemple en utilisant `curl`).

## Liens

- [Documentation Gist](https://docs.github.com/fr/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)
- Pour parcourir les Gist publiques : <https://gist.github.com>
\newpage{}

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.

