---
title: TP Manipulations avancées de la HEAD
author: Tom Avenel
date: 2023 / 2024
keywords:
- git
- ci
- devops
correction: false
---

# TP : Manipulations avancées de la HEAD

Dans ce TP, nous allons voir des commandes avancées pour déplacer le pointeur vers le commit courant (`HEAD`) de Git.

## Remonter l'historique : `~`, `^` et `@`.

Pour naviguer dans l'historique des commits en ligne de commande, on utilise des opérateurs spécifiques. 

Par exemple, on peut utiliser la commande suivante :

```bash
# Place la branche courante avant les deux derniers commit 
$ git reset HEAD~2
```

### Le symbole `~`

- Le symbole `~` permet de remonter linéairement dans l'historique des commits. Par exemple, la commande `HEAD~2` sélectionne le parent du parent du commit actuel (`HEAD`), remontant ainsi deux générations.
- Graphiquement, `~` représente une remontée verticale, suivant une ligne droite dans l’historique des commits.

### Le symbole `^`

- En cas de merge (fusion de branches), un commit peut avoir plusieurs parents, et c'est là que le symbole `^` intervient. Il permet de sélectionner le parent spécifique dans le cas d'un commit de merge. Par exemple, `HEAD^2` sélectionne le deuxième parent du commit de fusion.
- Graphiquement, `^` symbolise les bifurcations dans l'historique des commits, où plusieurs branches se rejoignent en un point.

### Exemple combiné

Il est possible de combiner ces opérateurs pour effectuer une navigation complexe, comme `HEAD~3^2~2^^`. Cependant, ces combinaisons peuvent rapidement devenir difficiles à lire et interpréter.

### `HEAD@{n}`

`HEAD@{}` permet d'accéder à l'historique des positions de `HEAD`, autrement dit, à toutes les positions précédentes où `HEAD` a pointé dans la branche courante ou lors des changements de branches. Cette syntaxe est couramment utilisée pour consulter l'historique des déplacements de `HEAD` et faciliter la navigation vers des états antérieurs dans le dépôt.

- La syntaxe générale `HEAD@{n}` désigne le n-ième état antérieur de `HEAD`. Par exemple, `HEAD@{1}` fait référence à l’état immédiatement précédent de `HEAD`, `HEAD@{2}` à l'état d'avant, et ainsi de suite.
- `HEAD@{}` sans un numéro affiche l’historique complet des changements de `HEAD` avec leurs dates, permettant de voir quand `HEAD` a changé de position.

#### Exemples 

##### Lister les changements de HEAD

```bash
git reflog
```

Cette commande affiche un journal de tous les changements de `HEAD` (par exemple, les déplacements de branches, les merges, les resets) : vous verrez une liste numérotée qui correspond à `HEAD@{n}` pour chaque changement.

##### Revenir à une position antérieure de HEAD

Si vous souhaitez revenir à un état précédent de HEAD, utilisez :

```bash
git checkout HEAD@{n}
```
où `n` est le nombre correspondant à l'état que vous voulez retrouver. Cela est utile pour revenir temporairement à un état spécifique sans créer un nouveau commit.

##### Utilisation avec `git reset`

Vous pouvez également utiliser cette syntaxe avec `git reset` pour remettre la branche courante à une position antérieure :

```bash
git reset --hard HEAD@{n}
```

Cela fait revenir votre branche (et l’index si vous utilisez `--hard`) à un point spécifique de l’historique.

### Liens

:::link
Voir aussi :

- <https://stackoverflow.com/questions/2221658/whats-the-difference-between-head-and-head-in-git>
- <https://dkhambu.medium.com/head-and-head-in-git-655681c3237e>
- <https://www.golinuxcloud.com/git-head-caret-vs-tilde-at-sign-examples/>
:::

### Exercice

Assurez-vous d'avoir un dépôt Git avec plusieurs commits, dont des commits de merge. Vous pouvez créer un nouveau dépôt ou utiliser un dépôt existant.

1. Commencez par afficher l'historique des commits de votre dépôt à l'aide de la commande `git log --oneline`.
2. Trouvez l'identifiant du commit correspondant à `HEAD~2`. Que représente ce commit par rapport à HEAD ?
3. Placez-vous sur un commit de merge. Trouvez son 1er parent et son 2e parent.
4. Affichez l'historique des positions de HEAD.
5. Choisir un commit, se déplacer sur ce commit, puis revenir à la position actuelle.
6. Choisissez un nombre à partir de votre reflog et remettez votre branche à cet état avec un hard reset.
7. Quelle est la différence entre `HEAD~1` et `HEAD^` ?
8. Que se passe-t-il lorsque vous utilisez `git reset --hard` ? Quelles sont les implications de cette commande ?

::: {.correction .if correction="true"}
```bash
# 1.
git log --oneline
# 2.
git show HEAD~2
# 3.
git show HEAD^
git show HEAD^2
# 4.
git reflog
# 5.
git checkout HEAD@{1}
git checkout -
# 6.
git reset --hard HEAD@{n}
```

Question 7 :

- `HEAD~1` se réfère au premier parent du commit actuel (c'est-à-dire le commit juste avant HEAD) de manière linéaire dans l'historique. Il est utilisé pour naviguer dans une seule ligne de commits, ce qui est particulièrement utile lorsque l'historique est linéaire.
- `HEAD^` est utilisé principalement dans le contexte de commits de fusion (merge commits), où un commit peut avoir plusieurs parents. `HEAD^` se réfère au premier parent d'un commit de fusion, tandis que `HEAD^2` désignerait le deuxième parent.
- Dans un scénario sans fusion, `HEAD~1` et `HEAD^` pointeront vers le même commit.
- Dans un scénario de fusion, `HEAD^` et `HEAD~1` peuvent pointer vers des commits différents si le commit actuel est un commit de fusion.

Question 8 :

`git reset --hard` réinitialise l'état de la branche courante à un commit spécifique, en changeant également l'index et le répertoire de travail pour correspondre à ce commit.
Toutes les modifications non enregistrées (c'est-à-dire les changements dans le répertoire de travail qui n'ont pas été ajoutés à l'index) seront perdues. Cela signifie que toutes les modifications en cours sont effacées et que l'état du projet est ramené exactement à l'état du commit spécifié.
:::

## Revert après un merge

Lors du `revert` d'un merge, un problème similaire apparaît : il faut choisir sur quel parent remonter. De manière similaire à l'instruction `^`, on utilise l'option `-m` (`--mainline`) de la commande `revert` pour choisir sur quelle branche remonter.

Par défaut, Git refuse de revenir en arrière sur un commit de fusion (`merge`), car l'action attendue est ambiguë.

Si vous souhaitez annuler un commit de fusion, il est nécessaire d'indiquer à Git quel parent du commit de fusion doit être considéré comme la branche principale, c'est-à-dire celle vers laquelle vous voulez revenir.

Souvent, ce sera le premier parent. Par exemple, si vous étiez sur `main` et que vous avez fait un `git merge mauvaise_branche` (pour fusionner la branche `mauvaise_branche`), puis décidé d'annuler cette fusion, le premier parent correspondrait à la branche `main` d'avant la fusion, tandis que le second parent correspondrait à la tête de `mauvaise_branche`.

Dans ce cas, on exécute :

```bash
git revert -m 1 HEAD
```

La commande suivante permet d'afficher les branches parentes dans l'ordre. Le premier parent listé correspond à `-m 1`, et le second à `-m 2` :

```bash
git cat-file -p [ID_DU_COMMIT_DE_FUSION]
```

:::link
Voir aussi : <https://stackoverflow.com/questions/5970889/why-does-git-revert-complain-about-a-missing-m-option>
:::

### Exercice

Assurez-vous d'avoir un dépôt Git avec plusieurs commits, y compris au moins un commit de fusion (`merge`). Vous pouvez créer un nouveau dépôt ou utiliser un dépôt existant.

#### Créer une situation de fusion

1. Créez une nouvelle branche à partir de `main` et effectuez quelques commits sur `nouvelle_branche`.
2. Revenez à main et effectuez quelques commits supplémentaires.
3. Fusionnez `nouvelle_branche` dans `main`.
4. Affichez l'historique des commits pour identifier l'ID du commit de fusion. Notez l'ID du commit de fusion que vous venez de créer.
5. Afficher les parents du commit de fusion. Identifiez les parents et notez quel parent correspond à `-m 1` et `-m 2`.

#### Revert du commit de fusion

1. Décidez quel parent vous souhaitez utiliser comme branche principale pour le revert. Généralement, ce sera le premier parent.
2. Exécutez le revert. Résolvez les conflits éventuels qui pourraient survenir pendant le revert.
3. Affichez à nouveau l'historique des commits. Vérifiez que le revert a été effectué correctement et examinez l'impact sur votre historique.
4. Quelles sont les raisons pour lesquelles Git refuse par défaut de revert un commit de fusion ?
5. Pourquoi est-il important de spécifier quel parent utiliser lors du revert d'un commit de fusion ?


::: {.correction .if correction="true"}
```bash
git checkout -b nouvelle_branche
git checkout main
git merge nouvelle_branche
git log --oneline
git cat-file -p [ID_DU_COMMIT_DE_FUSION]
git revert -m 1 [ID_DU_COMMIT_DE_FUSION]
git log --oneline
```

Question 4 :

Lorsqu'un commit de fusion est créé, il a (au moins) deux parents. Cela signifie que revenir en arrière sur ce type de commit n'est pas aussi simple que de supprimer un commit linéaire, car il faut décider quelle branche doit être considérée comme la principale. Git refuse de le faire par défaut pour éviter toute ambiguïté sur l'état du dépôt après le revert. En d'autres termes, Git ne sait pas automatiquement quel état doit être restauré, d'où la nécessité d'utiliser l'option `-m` pour spécifier explicitement le parent à utiliser.

Question 5 :

En spécifiant le parent avec l'option -m, git restaure un état précis du dépôt, en conservant les modifications de la branche principale (généralement le premier parent) tout en annulant les modifications apportées par la branche fusionnée (le deuxième parent). Cela réduit également les risques de conflits lors du revert.
Enfin, cela permet aux collaborateurs de mieux suivre l'évolution du projet et de comprendre les décisions prises lors des revert grâce à un historique bien documenté et linéaire qui facilite la gestion du code.
:::

## `git rev-parse`

La commande `git rev-parse` est un outil polyvalent de Git utilisé principalement pour traduire et interpréter des références de commit, telles que des noms de branches, des tags, des références relatives (`HEAD~2`, `HEAD^`), et d'autres identifiants Git, en leurs valeurs SHA-1. Elle est souvent utilisée dans des scripts pour obtenir des identifiants précis ou extraire des informations spécifiques du dépôt Git.

Options utiles :

`--show-toplevel` : Affiche le chemin absolu de la racine du dépôt Git.
`--show-prefix` : Affiche le chemin relatif entre le répertoire actuel et la racine du dépôt.
`--git-dir` : Indique l'emplacement du dossier .git.

Exemples :

```bash
git rev-parse HEAD~2
git rev-parse main # branche
git rev-parse v1.0 # tag

COMMIT_SHA=$(git rev-parse main)
echo $COMMIT_SHA

git show $(git rev-parse HEAD~2)
```

:::link
Documentation de référence : <https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-rev-parse.html>
:::

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries

