---
title: Partie pratique 3 - Utiliser un dépôt distant - Github®
date: 2023 / 2024
---

# Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

# Création d'un dépôt distant

Pour ce TP, nous allons utiliser la plateforme `Github` pour y héberger notre dépôt `git`.

Remarque : `git` est un gestionnaire de version entièrement décentralisé : il est même possible de cloner un dépôt sur un périphérique local (clé USB) ou à travers `SSH` (`NAS`, échanges directs entre deux développeurs), l'utilisation d'un serveur `git` n'est donc pas obligatoire.

Suivre la page de tutoriel à [cette adresse](https://openclassrooms.com/fr/courses/7162856-gerez-du-code-avec-git-et-github/7165712-demarrez-votre-projet-avec-github) pour créer un compte GitHub et un premier dépôt distant.

# Connexion depuis la machine locale

On utilise en général un accès à un serveur git distant :

- soit depuis un accès `HTTP(S)` : cette méthode est notamment utile pour un accès publique en lecture seule (sans contrôle d'accès, récupération des sources uniquement)
- soit depuis un accès `SSH` : cette méthode permet, une fois configurée, de simplifier l'administration de nombreux dépôts distants en utilisant la même clé `SSH` pour un même utilisateur.

Pour ce TP, nous allons négliger la sécurité et utiliser un accès public (depuis `HTTPS`) : quiconque ayant le lien du dépôt de code pourra donc y accéder et effectuer des changements.

# Synchronisation dépôt local / dépôt distant

`Git` étant décentralisé, le dépôt distant ne sert qu'à synchroniser des changements lorsque nécessaire.

La première étape consiste donc à "cloner" ce dépôt localement.

Note : une fois de plus, `git` est décentralisé : on utilise souvent un modèle "1 dépôt local <-> 1 dépôt distant" mais il est tout à fait possible de gérer plusieurs dépôts distants, ou de ne pas synchroniser entièrement les dépôts (différentes branches, etc...).

## Clone

L'opération de `clone` permet de créer une copie locale d'un dépôt distant.

```bash
$ git clone url-distante
# Crée un dossier du nom du projet contenant un clone local du dépôt.
```

Effectuer un clone du dépôt créé précédemment, par exemple :

```bash
$ git clone https://github.com/mon_utilisateur/mon_depot_distant.git
```

Note : Par défaut, le dépôt distant récupéré après une opération de `clone` a pour alias `origin` et est automatiquement lié au dépôt local.

## Gestion des dépôts distants

Pour afficher les dépôts distants, utiliser la commande `remote` :

```bash
$ git remote -v
```

Il est possible d'ajouter ou de supprimer des dépôts distants avec les commandes `$ git remote add` et `$ git remote remove`. Cette utilisation avancée permet de gérer des cas complexes hors du programme de ce cours, par exemple un dépôt A possédant le code de base d'un programme que l'on veut patcher, et un dépôt B possédant la sauvegarde du patch mais ne pouvant pas être lié à A. 

# Synchronisation avec les changements distants

## Récupération des changements distants

La récupération de changements distants se fait par l'opération `fetch`. Cette opération met à jour dans le dépôt local les changements réalisés à distance (techniquement, les branches `refs/remotes/<branche_remote>/` sont mises à jour localement).
Une opération `fetch` n'opère donc aucun changement sur les commit locaux, elle rapatrie juste des changements.

## Opération de merge

Une fois les changements dans les commit distants récupérés (par exemple une modification effectuée par un autre développeur), il va falloir les fusionner avec nos changements locaux.
Pour cela, l'opération `merge` permet de fusionner les changements récupérés avec les changements locaux.

L'exécution de cette commande conduit à deux états possibles :

- Les changements sont intégrables sans problème de concurrence. Par exemple, un développeur a créé un premier fichier et un autre développeur a modifié un autre fichier : les deux changements peuvent être intégrés sans problème.
- Les changements sont concurrents et créent un conflit. Par exemple, deux développeurs ont modifié la même ligne d'un fichier différemment. Dans ce cas, `git` appelle un autre programme pour demander à l'utilisateur de résoudre les conflits.

Les problèmes de concurrence sont donc gérés **localement** par le développeur qui récupère les changements distants et sont sous sa responsabilité.

L'algorithme de merge de `git` est l'un des plus puissants parmi les gestionnaires de versions, c'est aussi l'une des forces de `git` : il n'est souvent pas nécessaire d'intervenir, même si l'on a modifié le même fichier en parallèle.

## La commande pull

En pratique, on utilise souvent la commande `pull` directement pour réaliser à la fois une opération `fetch` suivie d'une opération `merge`.

### Pull sans conflit

1. En utilisant l'interface graphique de `GitHub`, réaliser un changement dans le fichier `index.html`.
2. Utiliser la commande `$ git pull` pour récupérer ce changement localement.
3. Vérifier que le fichier local a bien été synchronisé.

### Pull avec conflit

Avant d'effectuer un conflit, configurer l'outil de résolution que vous souhaitez utiliser avec git, par exemple `vscode` (attention à bien ajouter les guillemets simples `'` pour les commandes) :

```bash
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait --merge $REMOTE $LOCAL $BASE $MERGED'
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
```

Si vous préférez ne pas utiliser VSCode, vous pouvez installer et utiliser `Meld` qui est l'outil phare de la résolution de conflits (et permet aussi de visualiser les diffs plus élégamment) :

```bash
git config --global diff.tool meld
git config --global difftool.meld.path "C:/Program\ Files\ (x86)/Meld/Meld.exe"
git config --global merge.tool meld
git config --global mergetool.meld.path "C:/Program\ Files\ (x86)/Meld/Meld.exe"
```

1. En utilisant l'interface graphique de `GitHub`, réaliser un changement dans le fichier `index.html`.
2. Effectuer un autre changement à la même ligne dans le même fichier.
3. Utiliser la commande `$ git pull` pour récupérer ce changement localement.
4. En utilisant l'outil que vous avez configuré, résoudre le conflit : on pourra utiliser la commande `$ git mergetool`.
5. Vérifier que le fichier local contient bien le résultat attendu.

# Envoi des changements locaux sur le dépôt distant

Une fois les changements locaux effectués, nous voulons également les synchroniser sur le dépôt distant.
Pour cela, la commande `push` permet d'envoyer les commit à distance :

```bash
$ git push 
```

Vérifier sur l'interface de `GitHub` que le résultat du merge a bien été envoyé à distance.

La commande complète est en réalité `$ git push <remote> <branche>` ce qui permet de gérer des cas complexes de synchronisation. Sauf indication, on se limitera dans ce cours à cette simple commande sans arguments : `$ git push`.

# Travail collaboratif

Réalisons maintenant un vrai cas de développement collaboratif :

1. Configurer le dépôt `GitHub` d'un autre apprenant pour pouvoir y effectuer des opérations.
2. Cloner ce dépôt.
3. Effectuer chacun une modification dans votre dépôt local.
4. Synchroniser ces changements à travers le dépôt distant.

_L'ordre d'exécution des opérations (pull / push apprenant 1 vs apprenant 2) a-t-il un impact ? Pourquoi ?_

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.

