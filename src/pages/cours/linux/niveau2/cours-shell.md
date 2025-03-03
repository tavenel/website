---
title: Le shell Bash
date: 2024 / 2025
correction: false
---

## Rappels

Voir le TP sur la ligne de commande pour les rappels : utilisation du prompt, variables d'environnement, `PATH`, …

## Types de shells

On obtient la liste des shells présents sur le système en affichant le fichier `/etc/shells` :

```sh
cat /etc/shells
```

- `sh` : Bourn Shell, historique, standard, "portable"
- `csh/tcsh` : C Shell
- `ksh` : Korn Shell
- `fish` : Friendly Interactive Shell
- `zsh` : Z Shell
- `bash` : Bourn Again Shell Linux, le plus utilisé

:::tip
La plupart des shells sont fortement compatibles car ils suivent des normes comme la [norme POSIX](https://fr.wikipedia.org/wiki/POSIX)
:::

## Bash

Le projet GNU offre des outils pour l'administration de système de type UNIX qui sont libres et qui respectent les standards UNIX.

`bash` est un Shell compatible avec `sh` qui offre des améliorations fonctionnelles pour la programmation et l’utilisation interactive.

## Fichiers utiles

- `/etc/profile` : fichier de configurations commun à tous les utilisateurs et tous les shells
- `/etc/bash/bashrc` ou `/etc/bash.bashrc` : fichier de configurations commun à tous les utilisateurs de `bash`
- `~/.profile` : fichier de configuration pour tous les shells de l'utilisateur courant
- `~/.bashrc` : fichier de configuration `bash` pour l'utilisateur courant (quelque soit le contexte)
- `~/.bash_profile` : en cas d'utilisation de shell interactif
- `~/.bash_login` : à la connexion de l'utilisateur (peu utilisé)
- `~/.bash_logout` : à la déconnexion de l'utilisateur (peu utilisé)


## Enchaînement de commandes

```sh
# Exécute commande1 puis commande2
commande1 ; commande2

# Exécute commande1 puis commande2 uniquement en cas de succès ($?==0)
commande1 && commande2

# Exécute commande1 puis commande2 uniquement en cas d'erreur ($?!=0)
commande1 || commande2
```

### Exemples

```sh
sudo apt-get update && sudo apt-get -y upgrade

sudo apt-get -y upgrade || echo "échec de la mise à jour !"
```

## Codes de retour

La variable spéciale `$?` contient le code de retour d'exécution de la commande précédente.

Une commande qui s'exécute avec succès renvoie (par convention) toujours `0`. Par exemple la commande `true` rend toujours ce code de retour :

```sh
true ; echo $?
```

Une commande qui échoue renvoie (par convention) autre chose que `0` (souvent, par défaut, `1`). Par exemple la commande `false` renvoie toujours `1` :

```sh
false ; echo $?
```

### Chaînage avec code de retour

Les fonctions `&&` et `||` sont équivalentes à :

```sh
# &&
commande1
if [ $? == 0 ]
then
    commande2
fi

# ||
commande1
if [ $? != 0 ]
then
    commande2
fi
```

### Séquences de commandes

Si les arguments diffèrent pour une même commande, on peut créer une boucle et profiter de variables :

```sh
for arg in /home /var /usr
do
  echo "visualisation : " $arg
  ls -a $arg
done
```

Ou encore en une seule ligne

```sh
for arg in /home /usr /var; do ls -la $arg; done
```

_Ou simplement `ls -la /home /usr /var` dans ce cas précis…_


## Substitution de commandes : \`\` ou `$()`

Il est possible d'exécuter une commande et de récupérer son résultat (la sortie standard). Cela peut servir à mettre le résultat dans une variable, ou à le passer à une autre commande.

### Exemple 1

La commande `uname` permet de connaître la version du noyau courant. Comment la substituer dans une variable ?

```console
$ uname -a

Linux c7li 3.10.0-327.4.5.el7.x86_64 #1 SMP Mon Jan 25 22:07:14 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

```sh
system=$(uname -a)
echo $system

# ou (mois robuste)

system=`uname -a`
echo $system
```

### Exemple 2

Comment effectuer une boucle `for` sur tous les résultats de `find` ?

```sh
for resultat in $(find $HOME -type f -mtime -1)
do
    echo "Ce fichier a été modifié il y a moins de 1 jour : $resultat"
done
```

## Alias

Un alias est une autre manière de substituer des commandes.

Pour obtenir la liste des alias :

```sh
alias
```

Pour créer un alias :

```sh
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
```

:::tip
On place en général les alias dans le fichier de configuration du shell : `~/.bashrc`
:::


# Fichiers de script

Un script est un fichier texte contenant une liste de commandes qui seront exécutées, comme si elles étaient tapées par l'utilisateur.
Chaque ligne représente une entrée de l'utilisateur.

Un fichier de script commence toujours par un _shebang_.

## Shebang

Le shebang, représenté par `#!`, est un en-tête d'un fichier texte qui indique au système d’exploitation que ce fichier n’est pas un fichier binaire mais un script (ensemble de commandes) ; sur la même ligne est précisé l’interpréteur permettant d’exécuter ce script. Pour indiquer au système qu’il s’agit d’un script qui sera interprété par `bash` on placera le shebang sur la première ligne :

```sh
#!/usr/bin/env bash
```

:::tip
- Pour obtenir un script plus portable, il est possible d'utiliser le shebang `#!/usr/bin/env sh` du Bourne Shell - on indique que l'interpréteur n'est pas `bash` mais `sh` (beaucoup plus limité)
- Un autre shebang classique est le shebang Python : `#!/usr/bin/env python3`
:::

## Droits d'exécution

Pour pouvoir être exécuté facilement, on ajoute les droits d'exécution à un fichier de script :

```
chmod +x mon_script.sh

# ou juste pour l'utilisateur courant :
chmod +ux mon_script.sh

# Exécution depuis le répertoire du script :
./mon_script.sh
```

## Variables prépositionnées

Certaines variables ont une signification spéciale réservée. Ces variables sont très utilisées lors la création de scripts :

- pour récupérer les paramètres transmis sur la ligne de commande,
- pour savoir si une commande a échoué ou réussi,
- pour automatiser le traitement de tous paramètres.

Liste de variables prépositionnées

- `$0` : nom du script. Plus précisément, il s’agit du paramètre 0 de la ligne de commande, équivalent de argv[0]
- `$1`, `$2`, …, `$9` : respectivement premier, deuxième, …, neuvième paramètre de la ligne de commande
- `$*` : tous les paramètres vus comme un seul mot
- `$@` : tous les paramètres vus comme des mots séparés : `$@` équivaut à `$1` `$2` …
- `$#` : nombre de paramètres sur la ligne de commande
- `$-` : options du shell
- `$?` : code de retour de la dernière commande
- `$$` : PID du shell
- `$!` : PID du dernier processus lancé en arrière-plan
- `$_` : dernier argument de la commande précédente

### Exemple

```sh
#!/usr/bin/env bash

echo "Nom du script $0"
echo "premier paramètre $1"
echo "second paramètre $2"
echo "PID du shell " $$
echo "code de retour $?"
exit
```

:::tip
Il existe aussi une commande `shift` permettant de décaler les arguments : `$1` est perdu, `$2` devient `$1`, … On utilise souvent cette commande dans une boucle pour consommer les arguments les uns après les autres.
:::

:::tip
On peut aussi utiliser la commande `getopts` plus puissante pour gérer des arguments : [voir ici](https://www.quennec.fr/book/export/html/341).
:::

## Interaction utilisateur

La commande `echo` pose une question à l’utilisateur.

La commande `read` lit les valeurs entrées au clavier et les stocke dans une variable à réutiliser.

```sh
echo "question"
read reponse
echo $response
```

On peut aller plus vite avec `read -p` qui sort du texte et attend une valeur en entrée :

```sh
read -p "question" reponse
echo $reponse
```

La fonction `readline` permet également de lire un input utilisateur. Très utilse, la commande `readline -e` permet d'utiliser le mode `readline` du terminal (auto-complétion des noms de fichiers, …)

## Fonctions

Une fonction est un bloc d’instructions que l’on peut appeller ailleurs dans le script. Pour déclarer une fonction, on utilise la syntaxe suivante :

```sh
maFonction()
{
  echo hello world
}

# Ou de manière plus ancienne :

function ma_fonction {
  echo hello world
}
```

La déclaration d’une fonction doit toujours se situer avant son appel. On mettra donc les fonctions en début de script.

### Exemple

```sh
#!/usr/bin/env bash

read -p "quel votre prénom ?" prenom
reponse() {
    echo $0
    echo "merci $prenom"
    exit 1
}
reponse
exit
```

### Variables locales

Le mot clé `local` permet de définir une variable dans un scope local à la fonction en cours d'exécution.

```sh
ma_fonction() {
    local ma_var_locale=2
    echo "Dans la fonction : $ma_var_locale"
}

ma_fonction
echo "Dans le scope global : $ma_var_locale"
```

On peut aussi utiliser le mot-clé `declare` qui permet en plus de typer la variable (`declare` implique `local`, sauf dans le scope global) :

```sh
declare -i num # `num` sera de type numérique
declare -i num=15 # `num` est de type numérique et vaut 15
# Déclaration de tableau
declare -a asdf   # indexed type
declare -A asdf   # associative type
```

## Déboggage de script

On peut débogguer l’exécution du script en le lançant avec `bash -x`. Par exemple :

```
$ bash -x mon_script.sh
```

# Structures conditionnelles

## `if` / `then` / `else`

```sh
if condition
then
    commande1
else
    commande2
fi

# ou

if condition ; then
    commande1
else
    commande2
fi
```

## Tests

La condition pourra contenir un _test_. Deux manières de réaliser un test (avec une préférence pour la première) :

```sh
[ expression ]

# ou

test expression
```

:::tip
`/user/bin/[` est renseigné comme un programme sur le système.
:::

On peut aussi utiliser la version étendue de la commande test :

```sh
[[ expression ]]
```

Il y a beaucoup d’opérateurs disponibles pour réaliser des tests sur les fichiers, sur du texte ou sur des valeurs arithmétiques. La commande `man test` donnera une documentation à lire avec attention : tout s’y trouve.

### Exemple

```sh
#!/usr/bin/env bash

passwdir=/etc/passwdd
checkdir() {
    if [ -e $passwdir ]; then
        echo "le fichier $passwdir existe"
    else
        echo "le fichier $passwdir n'existe pas"
    fi
}
checkdir
exit
```

### Variante

On reprend la fonction `checkdir` qui lit la valeur de la variable donnée par l’utilisateur :

```sh
#!/usr/bin/env bash

read -p "quel est le dossier à vérifier ?" passwdir
checkdir() {
    if [ -e $passwdir ]; then
        echo "le fichier $passwdir existe"
    else
        echo "le fichier $passwdir n'existe pas"
    fi
}
checkdir
exit
```

### Autres exemples

```sh
#! /bin/sh

execverif() {
    if [ -x $target ] ; then
        #('x' comme "e_x_ecutable")
        echo $target " est exécutable."
    else
        echo $target " n'est pas exécutable."
    fi
}
```

```sh
#! /bin/sh

dir="${HOME}/tmp/"
if [ -d ${dir} ] ; then
    rm -rf ${dir}
    echo "Le dossier de travail ${dir} existe et il est effacé"
fi
mkdir ${dir}
echo "Le dossier de travail ${dir} est créé"
```

## Résumé : Structure de base d’un script

Quel serait la structure de base d’un script Bash ?

1. Shebang
1. Commentaires
1. Fonction gestion de la syntaxe
1. Fonction(s) utile(s)
1. Corps principal
1. Fin

```sh
#!/usr/bin/env bash

target=$1

usage() {
    echo "Usage: $0 <fichier>"
    echo "Compte les lignes d'un fichier"
    exit
}

main() {
    ls -l $target
    echo "nombre de lignes : $(wc -l $target)"
    stat $target
}

if [ $# -lt 1 ]; then
    usage
elif [ $# -eq 1 ]; then
    main
else
    usage
fi
exit
```

# Boucles

## Boucle `for`

Dans la boucle `for-do-done`, la variable prendra successivement les valeurs dans la liste et les commandes à l’intérieur du `do-done` seront répétées pour chacune de ces valeurs.

```sh
for variable in liste_de_valeur ; do
    commande
    commande
done
```

:::tip
Par défaut, `for` utilise la liste `in $@` si on omet ce mot-clé.
:::

### Exemple - créer 10 fichiers

```sh
for num in 0 1 2 3 4 5 6 7 8 9 ; do touch fichier$num.tar.gz ; done

# ou (mieux) :

for num in {0..9} ; do touch fichier$num.tar.gz ; done
```

### Exemple - renommer des fichiers

Renomme tous les fichiers `*.tar.gz` en `*.tar.gz.old` :

```sh
#!/usr/bin/env bash

#x prend chacune des valeurs possibles correspondant au motif : *.tar.gz
for x in ./*.tar.gz ; do
    # tous les fichiers $x sont renommés $x.old
    echo "$x -> $x.old"
    mv "$x" "$x.old"
#on finit notre boucle
done
exit
```

## `while` et `until`

`while-do` répète les commandes tant que la condition est vérifiée.

```sh
while condition ; do
    commandes
done
```

`until-do` répète les commandes jusqu’à ce que la condition soit vraie (ou par équivalence tant qu'elle est fausse).

```sh
until condition ; do
    commandes
done
```

:::tip
Comment rompre ou reprendre une boucle ?

- Rupture avec `break`,
- Reprise avec `continue`.
:::

### Exemple

Supposons, par exemple que vous souhaitiez afficher les 100 premiers nombres :

```sh
#!/usr/bin/env bash

# boucle while
i=0
while [ $i -lt 100 ] ; do
    echo $i
    i=$[$i+1]
done
exit
```

De manière plus élégante avec l’instruction `for` :

```sh
#!/usr/bin/env bash

# for ((initial;condition;action))
for ((i=0;i<100;i=i+1)); do
    echo $i
done
exit
```

## Boucle `case-esac`

L’instruction `case-esac` permet de modifier le déroulement du script selon la valeur d’un paramètre ou d’une variable. On l’utilise le plus souvent quand les valeurs possibles sont en nombre restreint et peuvent être prévues. Les imprévus peuvent alors être représentés par le signe `*`.

Demandons par exemple à l’utilisateur s’il souhaite afficher ou non les fichiers cachés du répertoire en cours.

```sh
#!/bin/sh

#pose la question et récupère la réponse
echo "Le contenu du répertoire courant va être affiché."
read -p "Souhaitez-vous afficher aussi les fichiers cachés (oui/non) : " reponse

#agit selon la réponse
case $reponse in
    oui)
        clear
        ls -a ;;
    non)
        ls;;
    *) echo "Veuillez répondre par oui ou par non." ;;
esac
exit
```

## Trouver des erreurs dans ses scripts

Bash est un langage peu permissif sur la syntaxe et les erreurs sont fréquentes.

On pourra :

- utiliser un IDE avec un plugin de développement adapté
- utiliser l'outil en ligne <https://www.shellcheck.net/>

## Ajouter de la sécurité

Bash est un langage extrêmement permissif, ce qui peut poser de nombreux problèmes de sécurité.

On sera donc vigilant à :

- Utiliser des chemins absolus en production (et non pas le `$PATH` qui peut avoir été altéré) ;
- Éviter de mettre des secrets dans un script (utiliser une variable d'environnement, un fichier de secrets, ou un outil dédié tel `Vault`) ;
- Vérifier et nettoyer les entrées utilisateur (il est très facile de corrompre un script avec des catactères spéciaux).

### Vérifications automatiques

Il est possible de modifier le comportement par défaut de Bash en lui ajoutant des options spéciales. Il est recommandé d'ajouter ces options au début de chaque script :

```sh
set -e # quitter le script à la 1e erreur
set -u # quitter le script dès qu'une variable n'est pas définie
set -o pipefail # quitter le script si n'importe quelle commande d'un pipeline échoue (et pas seulement la dernière).
set -euo pipefail # options combinées
```

# Liens

- Comprendre l'héritage d'environnement dans les scripts, sous-process, pipes : [Bash and the process tree](https://flokoe.github.io/bash-hackers-wiki/scripting/processtree/)
- <https://tech.gamuza.fr/Recapitulatif-sur-les-array-en-bash.html>
- [TP Grenoble IP sur les script shell](https://systemes.gricad-pages.univ-grenoble-alpes.fr/www-unix/avance/seance1-2-script-sh-pas-a-pas/tp-pas-a-pas.pdf)
- <https://blog.stephane-robert.info/docs/admin-serveurs/linux/script-shell/>
- [Écrire des scripts sécurisés](https://blog.stephane-robert.info/docs/admin-serveurs/linux/scripts-shell-securises/)

