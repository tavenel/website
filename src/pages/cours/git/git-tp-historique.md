---
title: TP Voyager et manipuler l'historique Git™
date: 2023 / 2024
tags:
- git
- ci
- devops
---

## Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

## Initialisation du projet

1. Créer un nouveau dépôt git
2. Créer un nouveau fichier `index.html`
3. Créer un premier commit avec le contenu du fichier `index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph</p>
</body>
</html>
```

## Annuler un changement avant commit

1. Ajouter un fichier `README` avec le contenu suivant : "Ceci est un TP git".
2. Modifier le contenu de la balise `title` dans le fichier `index.html`.
3. Ajouter ces modifications au `staging` : `git add README index.html`

_Pensez-vous qu'il est judicieux de créer un même commit pour les deux changements précédents ? Pourquoi ?_

Il est possible d'annuler des changements dans le `staging` grâce à la commande `reset` :

```bash
$ git reset
```

Créer un commit unique pour le changement du fichier `index.html` et un autre pour l'ajout du `README`.

_L'ordre des commit a-t-il un impact ? Pourquoi ?_

Attention : la commande `reset` est très puissante et dangereuse (voir section "Expert"). Cet exemple n'est à utiliser qu'avant d'avoir intégré les changements dans un commit !

## Réécrire l'histoire d'un commit

En cas d'erreur, il est possible de réécrire un commit grâce à l'option `--amend`.

1. Modifier le fichier `README` en ajoutant le contenu : "Pour installer le programme, voir le fichier INSTALL".
2. Créer un fichier `INSTALL`
3. Utiliser la commande `$ git commit -a` : cette commande va créer un commit en utilisant les changements connus par git.

_Le fichier `INSTALL` a-t-il été intégré au commit ? Pourquoi ?_

Pour corriger cette erreur :

1. Ajouter le fichier `INSTALL` au staging
2. Réécrire le commit précédent : `git commit --amend`

**Attention : ne jamais réécrire l'histoire d'un commit qui aurait été publié dans un dépôt distant (commande push). À réserver aux commits d'un dépôt local !**

## La méthode sûre : annuler un commit par ajout inverse (revert)

La commande `git revert` permet de créer un nouveau commit "inverse" du commit spécifié pour l'annuler. Aucun commit n'est donc détruit, ce qui limite grandement les risques de perte d'information mais peut polluer l'historique.

1. Créer un nouveau fichier `inutile.txt`, l'ajouter au staging, puis créer un nouveau commit contenant ce fichier.
2. Créer un nouveau commit annulant celui-ci grâce à la commande revert : `$ git revert HEAD`
3. Vérifier que le fichier a bien été supprimé du working directory et du staging.

Attention : contrairement à `git reset` qui annule toute une ligne d'historique jusqu'au commit spécifié, `git revert` annule uniquement un seul et unique commit en créant un nouveau commit inverse.

`Git revert` permet donc d'annuler n'importe quel ancien commit de l'historique, même s'il est très antérieur au commit actuel.

## Niveau expert : modifier les pointeurs (checkout / reset)

### Se déplacer dans l'historique : checkout

La commande `git checkout` permet de déplacer la référence courante (`HEAD`) vers un commit spécifié. Au lieu de suivre un historique cohérent dans une branche (voir TP suivant), la référence est directement liée à un commit, comme si celui-ci n'avait pas d'historique.

Cette commande est utile pour inspecter un changement stocké dans l'historique.

1. Noter la branche de travail actuelle avec la commande `$ git status` (en principe `master` ou `main`).
2. Récupérer l'identifiant d'un commit précédent avec la commande `$ git log`
3. Se déplacer dans le commit précédent avec la commande `$ git checkout identifiant_du_commit`
4. Inspecter la version récupérée : les fichiers ont été modifiés dans le working directory
5. Revenir à un état attaché dans la branche de travail : `$ git checkout nom_de_la_branche`

La commande `git checkout` est aussi très utile pour changer de branche (voir TP suivant).

### Mixed reset

Nous avons déjà vu la commande `reset` utilisée sans argument pour annuler les changements dans le staging.

Cette commande est beaucoup plus puissante (et donc dangereuse) et permet en réalité de travailler à la fois sur l'état du working directory, du staging et sur l'index de la branche courante (i.e. le dernier commit, nommé HEAD) :

- l'option `--soft` change uniquement la `HEAD`
- l'option `--mixed` (option par défaut) change le staging et la `HEAD`
- l'option `--hard` change le working directory, le staging et la `HEAD`

On peut utiliser cette commande pour "annuler" virtuellement un commit (en réalité, le détacher de l'historique) :

```bash
$ git reset HEAD~2 # place la HEAD (modifie la branche courante) avant les deux derniers commit 
```

Le symbole `~` permet de remonter (linéairement) l'historique des commit : `HEAD~2` est le parent du parent de la `HEAD` (verticalement). En cas de merge, il peut être utile de sélectionner sur quelle branche remonter avant le merge (donc sélectionner un parent horizontalement). Cette opération se fait avec l'opérateur `^` : `HEAD^2` sélectionne la 2e branche ayant créé le merge. Il est possible de cumuler ces opérateurs : `HEAD~3^2~2^^` mais cela devient vite illisible...

On peut aussi utiliser directement un identifiant de commit :

```bash
$ git reset d56af577052517886f29179409dddc1f65a956d8 # retourne au commit avec le hash : d56af577052517886f29179409dddc1f65a956d8
```
### Hard reset

`git reset --hard` est l'option la plus souvent utilisée mais attention : **cette option détruit tout changement dans le staging et le répertoire de travail**. Elle permet de repositionner le pointeur de la branche courante sur un nouvel index, par défaut : `HEAD` (commit courant).

**Cette option ne doit être utilisée sur des commit publiés en dehors du dépôt local (après push) au risque de corrompre l'historique du dépôt distant**

```bash
$ git reset --hard
# Détruit tout changement (working directory, staging) depuis le dernier commit.
```

### Supprimer des fichiers : git rm

Il est possible de supprimer des fichiers par la commande `$ git rm`.

```bash
$ git rm index.html
# Supprime un fichier index.html du working directory et du staging.
# Nécessite un nouveau commit pour intégrer le changement.
```

```bash
$ git rm --cached index.html
# Supprime le fichier index.html du staging uniquement.
# Le fichier reste dans le working directory.
```

## [Bonus] Retrouver un commit perdu

Le `reflog` (log des références) est un enregistrement local des références du projet. Il est local et n'est jamais pushé. Cet historique nous permet de voir les états successifs de toutes les références (les pointeurs) du dépôt. Tout est enregistré.

De son côté, `fsck`, qui signifie `file system check`, permet de vérifier l'intégrité du système de fichier de Git et d'identifier les commit n'ayant plus de parents.

Lorsqu'un commit est "effacé", il est simplement déréférencé car il n’est plus atteignable par les commit de l'historique. Le `reflog` comme `fsck` permettent donc de récupérer des commit perdus.

1. Modifier le fichier `index.html`, ajouter les changements dans le staging et créer un nouveau commit.
2. Noter l'identifiant du commit : `git log`
3. Détruire ce nouveau commit : `git reset --hard HEAD~1`
4. Vérifier les modifications de la `HEAD` dans le reflog : `git reflog`.
5. Lister les objets perdus en incluant le reflog : `git fsck --unreachable --no-reflogs`. Vérifier que l'on retrouve l'identifiant du commit éliminé.

Il est courant pour récupérer un commit perdu de :

- créer une nouvelle branche depuis ce commit (sans danger) : `git branch <commit-id>`
- ou ajouter le commit perdu au-dessus du commit actuel (dangereux) : `git cherry-pick <commit-id>`.

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries

