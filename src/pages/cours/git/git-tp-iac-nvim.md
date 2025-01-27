---
title: Git pour gérer ses configurations - IaC
author: Tom Avenel
date: 2023 / 2024
---

# Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

# Infrastructure-as-Code (IaC)

L'Infrastructure-as-Code consiste à utiliser des fichiers de configuration et des scripts pour coder le déploiement et la configuration d'une architecture.

Dans ce TP, nous allons voir comment `Git` peut grandement nous aider à versionner et déployer ces fichiers d'IaC, tant pour un point de vue de développeur que d'administrateur système.

Voir aussi le TP sur `Ansible`.

## Gérer la configuration de ses outils : l'IDE (Neo)Vim

Dans cet exercice nous allons utiliser l'éditeur de texte `Vim` (plus spécifiquement, un fork de `Vim` nommé `Neovim` qui reste très proche de `Vim` : <https://neovim.io/doc/user/nvim.html>).

`Vim` est un éditeur de texte avancé permettant de manipuler du texte par des opérateurs, dans plusieurs modes différents. Pour une découverte de `Neovim`,taper la commande `:Tutor<Enter>` à l'intérieur de l'éditeur lancé par la commande `nvim` (pour `Vim`, taper `:vimtutor` à l'intérieur de l'éditeur lancé par la commande `vim`).

:::tip
`vim` et `nvim` utilisent des commandes pour modifier le texte et interagir avec l'éditeur, ce qui peut désorienter au début. Si vous avez besoin de quitter `vim` ou `nvim` :

1. Appuyer sur `<Echap>` pour être sûr d'être en mode `Normal`.
2. Taper la commande `:quit<Enter>` pour quitter l'éditeur.
:::

### `Neovim`

1. Installer `nvim` sur votre machine : <https://github.com/neovim/neovim/blob/master/INSTALL.md>
2. Ouvrir un fichier de code (`Python`, ...) dans `Neovim` : `nvim mon_fichier.py`. Vous pouvez modifier ce fichier dans `nvim` mais pour l'instant l'interface est assez limitée...

:::tip
Une particularité de `Vim` (et `NeoVim`) est d'être entièrement configurable via des fichiers de configuration permettant de changer entièrement le comportement de l'éditeur ou de lui ajouter des fonctionnalités. Ces configurations sont stockées :

- Sur `Linux` ou `MacOS` dans `$XDG_CONFIG_HOME/nvim` (en principe : `~/.config/nvim`)
- Sur `Windows` (`cmd`) : `%userprofile%\AppData\Local\nvim\`
- Sur `Windows` (`powershell`) : `$env:USERPROFILE\AppData\Local\nvim\`

Nous allons utiliser deux "distributions" permettant de récupérer des configurations toutes faites pour `Neovim` depuis des dépôts `Git` afin d'améliorer notre éditeur.
:::

### `LazyVim`

`LazyVim` : <https://www.lazyvim.org/> est une distribution de `Neovim` ajoutant le gestionnaire de package `lazy.nvim` et de nombreuses configurations et plugins pour faciliter le développement et transformer l'éditeur de texte en réel IDE.

1. Installer les configurations de `LazyVim` en clonant le dépôt `Git` : suivre <https://www.lazyvim.org/installation>.

_Dans ce tutoriel, il est conseillé à la fin de supprimer le dossier `.git` afin de pouvoir créer votre propre dépôt `Git` avec vos configurations. Que pensez-vous de cette affirmation ? Existe-t-il un pattern permettant de gérer cette double dépendance : avoir un lien sur le dépôt `Git` officiel de `LazyVim` et un autre lien vers votre dépôt personnel ?_

2. Lancer `nvim` une fois la configuration clonée : `Neovim` installe automatiquement les dépendances spécifiées dans les configurations.
3. Ouvrir un fichier de code (`Python`, ...) et vérifier que `Neovim` a bien ajouté la coloration syntaxique, la complétion automatique, la détection d'erreurs, ...
3. Les configurations de `Neovim` sont stockées dans un répertoire `.config/nvim` : voir <https://www.lazyvim.org/configuration>. Créer un dépôt `git` dans ce répertoire pour y gérer vos configurations. Faire un `push` de ces configurations dans un dépôt distant.
4. Modifier une configuration - par exemple, changer le thème en utilisant `gruvbox` (en créant le fichier `lua/plugins/colorscheme.lua` dans le répertoire des configurations) : <https://www.lazyvim.org/plugins/colorscheme> . Redémarrer `nvim`, réouvrir le fichier de code et vérifier que la coloration syntaxique a bien changé.
5. Partager le changement de configuration avec un autre apprenant en utilisant votre dépôt distant.

:::tip
En pratique, on utilise souvent ce principe d'échange de fichiers de configuration pour avoir facilement la même configuration sur l'ensemble de ses postes de travail. Particulièrement utile lorsque l'on démarre / détruit beaucoup de machines virtuelles !
:::

### `kickstart`

Nous allons utiliser un autre dépôt de configuration pour voir à quel point il est facile de changer le comportement du programme :

1. Supprimer les fichiers de configuration récupérés par `LazyVim`.
2. Refaire le même exercice avec : <https://github.com/nvim-lua/kickstart.nvim>

:::tip
Il existe d'autres distributions de `Neovim` : <https://github.com/LunarVim/LunarVim>, <https://github.com/NvChad/NvChad>, ...
Il s'agit à chaque fois de configurations spécifiques pour `Neovim`, il est donc toujours possible de changer ce que l'on désire pour créer son propre IDE. Les utilisateurs avancés créent en général des configurations sur mesure en partant de zéro.
:::

:::tip
On peut bien sûr réitérer le même exercice avec tout programme configurable par des fichiers de configuration : `vsCode`, ...

On peut aussi aller jusqu'à stocker le déploiement des infrastructures et des outils (par exemple par des fichiers `Ansible` - voir le TP dédié).
:::

# Legal

- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- Ansible® is a registered trademark of RED HAT, INC.

