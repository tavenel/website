---
title: TP - La ligne de commande
date: 2024 / 2025
---

## La ligne de commande

Une ligne de commande Linux comprend les éléments suivants :

- _Commande_ : C'est le nom de la commande que vous souhaitez exécuter. Par exemple, `ls`, `cd`, `mkdir`, `rm`, etc. Chaque commande effectue une action spécifique.
- _Options_ : Les options modifient le comportement de la commande. Elles sont précédées d'un tiret court `-` ou de deux tirets `--`. Par exemple, `ls -l` affiche une liste détaillée des fichiers.
- _Arguments_ : Les arguments sont des informations supplémentaires que la commande peut nécessiter pour fonctionner correctement. Par exemple, si vous utilisez `cp chemin_fichier1 chemin_fichier2`, `fichier1` et `fichier2` sont les arguments.
- _Redirections et Pipes_ : Vous pouvez rediriger la sortie d'une commande vers un fichier en utilisant >, ajouter la sortie à un fichier avec >>, ou rediriger l'entrée à partir d'un fichier avec <. Vous pouvez également utiliser des pipes (|) pour diriger la sortie d'une commande vers l'entrée d'une autre. _Voir le TP sur les redirections._
- _Wildcards_ : Les caractères génériques, comme `*`, `?`, `[`, `]`, `{`, `}`, sont utilisés pour effectuer des correspondances de motifs avec des noms de fichiers. Par exemple, `*.txt` correspondra à tous les fichiers avec l'extension `.txt`. _Voir le TP sur les flux de texte._

:::tip
L'argument `--` permet de séparer la commande et ses options des arguments. Ce paramètre spécial est très utile pour travailler sur des noms spéciaux de fichiers.

Par exemple : `rm -- -1` supprime le fichier `-1` (alors que `rm -1` fournit l'option `-1` à la commande `rm`).
:::

:::link
Voir aussi :

- <https://doc.ubuntu-fr.org/tutoriel/console_ligne_de_commande>
- <https://doc.ubuntu-fr.org/console>
- <https://doc.ubuntu-fr.org/terminal>
:::

## Variables shell

- `nom_de_variable=valeur` : déclare une variable et lui assigne une valeur : `nom="John"`, `age=30`, ... Pas de typage de Bash.
- `$nom_de_variable` : accède à la valeur de la variable : `echo "Age : $age"` affiche `Age : 30`.
- `unset nom_de_variable` : supprime la variable nommée `nom_de_variable` pour la session shell en cours. La modification n'est pas permanente et n'affecte pas les futures sessions.

### Variables d'environnement

- _Variables Locales et Globales_ : En Bash, les variables sont locales par défaut, ce qui signifie qu'elles ne sont visibles que dans le script ou le contexte où elles sont déclarées. Pour créer une variable globale (ou variable d'environnement), on utilise l'instruction `export`. Par exemple : `export MA_VARIABLE_GLOBALE="Voici une variable globale"`. _Attention : l'export n'est réalisé que sur les processus pour lesquels vous avez le droit d'impacter l'environnement ! En général, il s'agit donc des processus hérités du processus courant._
- `env` est une commande commande utilisée pour afficher les variables d'environnement et leurs valeurs actuelles.
- `set` affiche les variables d'environnement, les variables locales et les options du shell. 
- Quelques variables d'environnement courantes :
  - `USER` : Le nom de l'utilisateur actuellement connecté.
  - `HOME` : Le répertoire personnel de l'utilisateur.
  - `SHELL` : Le shell par défaut de l'utilisateur.
  - `PATH` : Les répertoires dans lesquels le système recherche les fichiers exécutables lorsque vous saisissez des commandes (voir ci-dessous).
  - `PWD` : Le répertoire de travail actuel.
  - `LANG` : La configuration de la langue par défaut du système.

Vous pouvez également utiliser la commande `env` pour exécuter un programme avec des variables d'environnement spécifiques. Par exemple, pour exécuter un programme `mon_programme` avec une variable d'environnement spécifique, vous pouvez saisir :

```sh
env NOM_DE_VARIABLE=VALEUR mon_programme
```

:::exo
1. Créer une variable `ma_variable` ayant comme valeur `42`. Afficher la valeur de cette variable.
1. Taper la commande `bash` : ceci va créer un nouveau shell (dans un nouveau processus) fils du shell courant.
1. Vérifier que la variable `ma_variable` n'est pas instanciée. Finir l'exécution de ce processus par la commande `exit`.
1. Exporter la variable `ma_variable`.
1. Taper de nouveau la commande `bash` pour créer un nouveau shell (dans un nouveau processus) fils du shell courant.
1. Vérifier que la variable `ma_variable` est maintenant présente dans le nouveau processus. Finir l'exécution de ce processus par la commande `exit`.
1. Supprimer la variable `ma_variable`.
:::

### Le PATH

`PATH` est une variable d'environnement essentielle dans tous les systèmes d'exploitation standard (Windows, Unix, Linux et macOS). Elle définit les répertoires dans lesquels le système d'exploitation recherche les fichiers exécutables (les programmes ou les scripts) lorsque vous saisissez une commande dans un terminal.

- Lorsque vous saisissez une commande dans un terminal, le système d'exploitation tente de localiser le fichier exécutable correspondant à cette commande. Par exemple, si vous tapez `ls`, le système recherche le fichier exécutable de la commande `ls`.
- Les répertoires sont séparés par des deux-points (`:`) sous Unix et Linux, ou par des points-virgules (`;`) sous Windows.
- Le système recherche dans les répertoires du `PATH` de gauche à droite : si plusieurs répertoires contiennent des fichiers exécutables portant le même nom, le premier fichier trouvé dans la liste des répertoires du `PATH` est utilisé.
- Si la commande spécifiée ne se trouve pas dans les répertoires du `PATH`, le système vérifie également le répertoire courant.
- La variable `PATH` peut être modifiée par l'utilisateur.

:::exo
Modifier le `PATH` pour ajouter un répertoire de votre choix contenant un binaire. Vérifier que le binaire peut être exécuté en tapant uniquement son nom (et non le chemin complet vers le fichier de programme).
:::

## Aide et documentation sur les commandes

1. La commande `man` est utilisée pour afficher le manuel (la documentation) des commandes, des fichiers ou des concepts sous Linux. Elle fournit des informations détaillées sur la manière d'utiliser une commande et ses options.
2. La commande `apropos` est utilisée pour rechercher des commandes en fonction de mots-clés ou de descriptions. Elle parcourt la base de données des pages de manuel et renvoie une liste de commandes et de concepts associés aux mots-clés spécifiés.
3. La commande `which` est utilisée pour déterminer l'emplacement du fichier exécutable d'une commande. Lorsque vous saisissez `which` suivi du nom d'une commande, elle affiche le chemin absolu du fichier exécutable correspondant. Cela peut être utile pour savoir quelle version d'une commande est exécutée si plusieurs versions sont installées sur votre système.
4. La commande `type` est utilisée pour déterminer le type d'une commande. Elle indique si une commande est une commande interne du shell, une commande externe ou un alias.

:::exo
1. Afficher la page de manuel de la commande `ls`.
1. Trouver des commandes liées à la copie de fichiers.
1. Chercher le chemin vers l'exécutable de la commande `python`.
1. Chercher le type de la commande `ls`.
1. Chercher le type de la commande `cd`.
:::

## Historique des commandes

- La commande `history` permet d'afficher l'historique des commandes entrées.
- La variable `!` contient le `PID` de la dernière commande lancée en arrière-plan : `echo $!`
- `! <cmd>` : inverse le code d'erreur de la commande. Attention : si le flag `set -e` a été activé (arrêter le script à la 1e erreur), une erreur dans une commande commençant par `!` est ignorée !
- `!!` : réexécute la dernière commande
  - `!124` : réexécute la 124e commande de l'historique
  - `!-3` exécute la 3e dernière commande
  - `!ls` : réexécute la dernière commande commençant par `ls`
- `!:<i>` : réutilise le ième argument de la commande précédente : `echo one two three`
  - `echo !:2 #two`
  - `!:^` : 1er argument
  - `!:$` : dernier argument
  - `!:*` tous les arguments
- `!ma_var` crée une indirection : cela va évaluer le contenu référencé, lui-même, par le contenu de `ma_var` :
  - `toto=2; titi=toto; echo ${!titi} #2`

Exemple de réutilisation des arguments :

```sh
echo "f1" "f2" "f3"
echo !!:2 # :2 == f2, voir aussi :^, :$, :*
echo !!:2:a # /home/user/f2 => :a récupère le chemin, :A suit les liens (symlink), :h extrait seulement le répertoire, :h1 le 1er répertoire, :t seulement le nom de fichier, :r retire l'extension
echo !!:s/… # substitute, idem Vim
echo ${var/<pattern>/<replacement>} # remplace 1e occurence de `pattern` par `replacement`
echo ${var//<pattern>/<replacement>} # remplace toutes occurences de `pattern` par `replacement`
echo ${^array}.png # one.png two.png three.png
```

:::exo
1. Comment affichez-vous les 10 dernières commandes de l'historique ?
1. Utilisez la commande `!n` (où `n` est un numéro de commande) pour réexécuter une commande spécifique à partir de l'historique.
1. Utilisez la commande `!!` pour réexécuter la dernière commande de votre historique.
1. Utilisez la commande `!commande` (où `commande` est une partie d'une commande précédente) pour réexécuter la dernière commande qui contient la chaîne spécifiée.
1. Quel est le rôle du fichier `.bash_history` ?
1. Comment effacez-vous l'historique des commandes ?
:::

:::tip
- Pour éviter d'ajouter une commande dans l'historique, par exemple pour des raisons de sécurité, il suffit d'ajouter un espace avant la commande.
- La commande `history -c` efface l’historique de la session courante.
:::

## Complétion et navigation : Tabulation, touches directionnelles, raccourcis

- Selon la distribution la touche de tabulation offre des possibilités d'auto-complétion.
  - L'auto-complétion de certains binaires non natifs demandent l'installation et la configuration de scripts ou paquets supplémentaires.
- Les touches directionnelles permettent de naviguer dans l'historique des commandes
- La plupart des shells utilisent par défaut les mêmes raccourcis (basés sur `emacs`):
  - `[Ctrl] + [a]` : aller au début de la ligne
  - `[Ctrl] + [e]` : aller à la fin de la ligne
  - `[Ctrl] + [w]` : supprimer un mot en arrière (et le mets dans le presse-papier)
  - `[Alt] + [d]` : supprimer un mot en avant
  - `[Alt] + [b]` : revenir en arrière d'un mot
  - `[Alt] + [f]` : avancer d'un mot
  - `[Ctrl] + [u]` : supprimer le texte avant le curseur (et le mets dans le presse-papier)
  - `[Ctrl] + [k]` : supprimer le texte après le curseur (et le mets dans le presse-papier)
  - `[Ctrl] + [y]` : colle le contenu du presse-papier
  - `[Ctrl] + [c]` : tuer proprement le programme en cours d'exécution
  - `[Ctrl] + [z]` : suspendre le programme en cours d'exécution (`fg` pour ramener au 1er plan, `bg` pour continuer l'exécution en arrière-plan)
  - `[Ctrl] + [r]` : chercher dans l'historique (à l'envers)
  - `[Ctrl] + [l]` : nettoyer l'écrant (`clear`)
  - `[Ctrl] + [d]` : fermer le terminal (`exit`)
  - `[Ctrl] + [s]` : arrêter le défilement de l'écran
  - `[Ctrl] + [q]` : reprendre le défilement de l'écran
  - `[Ctrl] + [XX]` : naviguer entre 2 positions (par défaut : position courante du curseur et début de ligne)
  - `[Ctrl] + [T]` : inverse les 2 derniers caractères
  - `[Alt] + [T]` : inverse les 2 derniers mots
- Il est possible d'utiliser plutôt les raccourcis `vi` : `set -o vi`
