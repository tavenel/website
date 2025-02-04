---
title: TP - Traitement de flux de type texte
date: 2024 / 2025
correction: false
---

## Commandes utiles

:::tip
Pour une liste des commandes, voir _Summary_, 103.2 Lesson 1 p.212
:::

### Formattage de fichiers

- `cut` : permet d'extraire des colonnes spécifiques de fichiers texte en utilisant un délimiteur (généralement le caractère de tabulation ou un autre caractère spécifié). Il est couramment utilisé pour manipuler des fichiers `CSV` et d'autres données tabulaires. Par exemple, pour extraire la 2e colonne d'un fichier `donnees.csv` séparé par des virgules : `cut -d ',' -f 2 donnees.csv`
- `grep` : utilisée pour rechercher des motifs (expressions régulières) dans un ou plusieurs fichiers texte et afficher les lignes qui correspondent à ces motifs (voir section dédiée).
- `nl` : utilisé pour numéroter les lignes d'un fichier texte. Il est souvent utilisé pour ajouter des numéros de ligne à des fichiers lors de la création de rapports ou de documents.
- `od` : od affiche le contenu d'un fichier en format octal ou d'autres formats spécifiés. Il est principalement utilisé pour visualiser des fichiers binaires ou pour des besoins de débogage.
- `paste` : utilisé pour fusionner le contenu de plusieurs fichiers ligne par ligne en utilisant un délimiteur (généralement une tabulation). Cela permet de combiner des données provenant de différentes sources, souvent utilisé pour fusionner des colonnes de plusieurs documents.
- `sed` : éditeur de flux utilisé pour manipuler et transformer le texte en fonction de règles spécifiées, généralement à l'aide d'expressions régulières. Usage classique : `sed 's/ancien/nouveau/g' mon_fichier.txt`
- `split` : divise un fichier en plusieurs parties plus petites en fonction d'une taille spécifiée. Il est couramment utilisé pour diviser de gros fichiers en plusieurs fichiers plus faciles à gérer (nommés par défaut `x...`).
- `tr` : utilisé pour effectuer des transformations de texte simples, telles que la conversion de la casse, la substitution de caractères, ou la suppression de caractères spécifiques.
- `uniq` : permet de supprimer les lignes en double d'un fichier texte. Il est souvent utilisé en combinaison avec la commande `sort` pour éliminer les doublons d'un fichier trié : `sort mon_fichier | uniq`
- `wc` : utilisé pour compter les mots, les caractères et les lignes dans un fichier ou dans une entrée standard.

### Fichiers compressés et hash de fichiers

- `bzcat`, `xzcat` et `zcat` : Ces commandes permettent d'afficher le contenu de fichiers compressés au format `Bzip2`, `XZ` et `Gzip`, respectivement, sans les décompresser. Elles sont utiles pour lire le contenu de fichiers compressés rapidement.
- `md5sum`, `sha256sum`, `sha512sum` : Ces commandes calculent les sommes de contrôle (`hash`) de fichiers en utilisant respectivement les algorithmes `MD5`, `SHA-256` et `SHA-512`. Elles sont utilisées pour vérifier l'intégrité des fichiers en générant une signature numérique unique.

## Afficher un fichier texte et limiter son affichage.

Afficher du texte à l'écran est primordial mais faire défiler de longues lignes de texte peut être coûteux en performances pour de gros fichiers. Il est donc utile de pouvoir restreindre cet affichage.

1. Afficher l'intégralité du fichier `/etc/passwd`.
2. Afficher le contenu du fichier `/etc/passwd` en ajoutant des numéros de ligne.
3. Afficher les 10 premières lignes du fichier `/etc/passwd`.
4. Afficher les 10 dernières lignes du fichier `/etc/passwd`.
5. Afficher le contenu du fichier `/etc/passwd` en hexadécimal.
6. Écrire en continu dans un fichier avec la commande suivante : `for i in $(seq 1 4 20000); do echo "Ligne $((i % 5000))" >> /tmp/mon_fichier.txt; done`. Dans un autre terminal, afficher en temps réel le contenu en cours d'écriture dans ce fichier.
7. Utiliser deux commandes différentes de pagination pour parcourir le fichier `/tmp/mon_fichier.txt`.
8. Afficher le contenu du fichier `/tmp/mon_fichier.txt` en enlevant les doublons de lignes.
9. Diviser le fichier `/tmp/mon_fichier.txt` en segments de 100 lignes nommés `/tmp/extrait-...`
10. Calculer le `hash` du fichier `/tmp/mon_fichier.txt`.

:::correction
```
#1.
$ cat /etc/passwd

---------------------------------------------------------

#2.
$ nl /etc/passwd

---------------------------------------------------------

#3.
$ head -n 10 /etc/passwd

---------------------------------------------------------

#4.
$ tail -n 10 /etc/passwd

---------------------------------------------------------

#5.
$ od --format=x /etc/passwd

---------------------------------------------------------

#6.
$ tail -f /tmp/mon_fichier.txt

---------------------------------------------------------

#7.
## simpliste : more
$ more /tmp/mon_fichier.txt

## un peu plus puissant : less
$ less /tmp/mon_fichier.txt

---------------------------------------------------------

#8.
## Attention à bien trier le fichier avant !
$ sort /tmp/mon_fichier.txt | uniq

$ wc -l /tmp/mon_fichier.txt # 6000 lignes
$ sort /tmp/mon_fichier.txt | uniq |wc -l # 1250 lignes

---------------------------------------------------------

#9.
$ split -l 100 /tmp/mon_fichier.txt /tmp/extrait-

---------------------------------------------------------

#10.
$ md5sum /tmp/mon_fichier.txt
```
:::


## Les filtres

Les filtres permettent d'aller un peu plus loin en sélectionnant plus finement les données à afficher ou en les modifiant.

### Quelques caractères spéciaux

- `.` : n'importe quel caractère
- `^` : début de ligne
- `$` : fin de ligne
- `[ati]` : un caractère `a` ou `t` ou `i` 
- `[^ati]` : un caractère **sauf** `a`, `t`, `i`
- `[0-9]`, `[a-z]` : un chiffre entre `0` et `9`, un caractère entre `a` et `z`
- `?`, `*`, `+` : un caractère, 0 ou plusieurs caractères, au moins un caractère
- `\` : caractère d'échappement pour `.^$*[](){}|\` (ex: `\*` : caractère `*`)

1. Le fichier `/etc/passwd` est un grand classique sous Unix. Il se compose de sept champs séparés par des `:` : `login:passwd:UID:GID:Commentaire:homedir:shell` . Récupérez la ligne de l'utilisateur `root` dans `/etc/passwd`.
2. De cette ligne, récupérez l'`UID` de `root`.
3. Comptez le nombre d'utilisateurs contenus dans ce fichier à l'aide d'une redirection en entrée.
4. Un peu plus compliqué : récupérez la liste des `GID`, triez-les par ordre croissant et supprimez les doublons.
5. De là, extrapolez le nombre de groupes différents utilisés.
6. Convertissez tous les login en majuscules.
7. Isolez maintenant la huitième ligne de `/etc/passwd`.

:::correction
1. Le fichier `/etc/passwd` est un grand classique sous Unix. Il se compose de sept champs séparés par des `:` : `login:passwd:UID:GID:Commentaire:homedir:shell` . Récupérez la ligne de l'utilisateur `root` dans `/etc/passwd`.

```
$ grep ^root: /etc/passwd
```

2. De cette ligne, récupérez l'`UID` de `root`.

```
$ grep ^root: /etc/passwd | cut -d: -f3
```

3. Comptez le nombre d'utilisateurs contenus dans ce fichier à l'aide d'une redirection en entrée.

```
$ wc -l < /etc/passwd
```

4. Un peu plus compliqué : récupérez la liste des `GID`, triez-les par ordre croissant et supprimez les doublons.

```
$ cut -d: -f4 /etc/passwd | sort -n | uniq
```

5. De là, extrapolez le nombre de groupes différents utilisés.

```
$ cut -d: -f4 /etc/passwd | sort -n | uniq | wc -l
```

6. Convertissez tous les login en majuscules.

```
$ cut -d: -f1 /etc/passwd | tr "[a-z]" "[A-Z]"
```

7. Isolez maintenant la huitième ligne de `/etc/passwd`.

Il y a plusieurs solutions, en voici deux :

```
$ head -8 /etc/passwd | tail -1
$ grep -n "" /etc/passwd | grep ^8: | cut -d: -f2-
```
:::

## Utilisation de jokers (wildcards) et des caractères d'échappement

Les jokers sont des caractères spéciaux utilisés dans les commandes du shell pour effectuer des correspondances de motifs avec des noms de fichiers et de répertoires. Ils permettent d'effectuer des opérations sur un ensemble de fichiers en utilisant des modèles ou des motifs au lieu de spécifier des noms de fichiers exacts.

- `*` (astérisque) : Correspond à n'importe quel nombre de caractères, y compris zéro caractère. Par exemple, `*.txt` correspond à tous les fichiers ayant une extension `.txt` dans le répertoire courant.
- `?` (point d'interrogation) : Correspond à un seul caractère quelconque. Par exemple, `image?.jpg` correspond à des fichiers tels que `image1.jpg`, `imageA.jpg`, etc.
- `[ ]` (crochets) : Permet de spécifier un ensemble de caractères possibles pour un seul caractère à cet emplacement. Par exemple, `[aeiou]` correspond à n'importe quelle voyelle, et `[0-9]` correspond à n'importe quel chiffre.
- `[! ]` (point d'exclamation suivi de crochets) ou `[^ ]` (circonflexe suivi de crochets) : Correspond à un caractère qui n'est pas dans l'ensemble spécifié. Par exemple, `[!aeiou]` correspond à n'importe quel caractère qui n'est pas une voyelle.
- `{ }` (accolades) : Permet de spécifier plusieurs options pour une partie d'un motif. Par exemple, `*.{jpg,png}` correspond à tous les fichiers avec l'extension `.jpg` ou `.png`.
- `**` : Utilisé pour effectuer une recherche récursive dans des sous-répertoires. Par exemple, `**/*.txt` correspondra à tous les fichiers `.txt` dans tous les sous-répertoires à partir du répertoire courant. Attention, `**` n'est pas standard et n'est pas toujours supporté : sur `bash`, activer `globstar` : `shopt -s globstar`. Supporté par défaut sur `zsh`.

Les jokers sont extrêmement utiles pour effectuer des opérations en masse sur des fichiers, pour les scripts shell et pour simplifier la gestion des fichiers et des répertoires.

### Travaux Pratiques

1. Affichera tous les fichiers ayant l'extension `.txt` dans le répertoire courant.
2. Supprimera tous les fichiers qui commencent par "backup" dans le répertoire courant.
3. Copiera les fichiers `image1.jpg`, `image2.jpg` et `image3.jpg` dans le répertoire courant.
4. Affichera tous les fichiers avec les extensions `.jpg` ou `.png` dans le répertoire courant.
5. Utilisez les caractères jokers pour lister tous les fichiers dont le nom contient `x` suivit de `in` dans le dossier `/etc`.
6. Utilisez les caractères jokers pour lister tous les fichiers dont le nom commence par n'importe quel caractère entre `a` et `e`, suivi d'au moins deux caractères et qui ne fini pas par un nombre.
7. Utilisez les caractères jokers pour lister tous les fichiers dont le nom contient exactement quatre caractères ainsi que les fichiers dont le nom commence par une majuscule. N'explorez par les sous-dossiers.
8. Utilisez les caractères jokers pour lister tous les fichiers qui contiennent `sh` dans le dossier `/bin`.
9. Affichez votre variable d'environnement `HOME` précédée par la chaîne `la valeur de $HOME est : `.
10. Affichez votre variable d'environnement `SHELL` encadrée par deux astérisques de chaque coté.
11. Comment afficheriez-vous la chaîne de caractères suivantes telle quelle avec la commande `echo`, en vous servant de double guillemets `"` et d'anti-slash `\` ?
    `@ # $ % ^ & * ( ) ' " \`
12. Utilisez la commande `echo` pour afficher les deux chaînes suivantes :
    ```
    C'est ce qu'il a dit !
    'Plus jamais ça !' a-t-il répondu.
    ```

:::correction
1. `ls *.txt` : Affichera tous les fichiers ayant l'extension `.txt` dans le répertoire courant.
2. `rm backup*` : Supprimera tous les fichiers qui commencent par "backup" dans le répertoire courant.
3. `cp image[1-3].jpg` : Copiera les fichiers `image1.jpg`, `image2.jpg` et `image3.jpg` dans le répertoire courant.
4. `ls {*.jpg,*.png}` : Affichera tous les fichiers avec les extensions `.jpg` ou `.png` dans le répertoire courant.
5. `ls -d /etc/{**/,}*x*in*`
6. `ls -d {**/,}[a-e]?*[^0-9]`
7. `ls -d ???? [A-Z]*`
8. `ls -d /bin/{**/,}*sh*`
9. `echo "la valeur de \$HOME est : $HOME"`
10. `echo "**$SHELL**"`
11. `echo "* @ # \$ % ^ & * ( ) ' \" \\"`
12. `echo -e "C'est ce qu'il a dit "'!'"\n'Plus jamais ça "'!'"' a-t-il répondu."`
:::

## Les expressions régulières

Les expressions régulières permettent d'aller beaucoup plus loin dans la sélection de données d'un fichier texte. Elles peuvent être très complexes afin de réaliser très efficacement des traitements lourds sur de gros fichiers - on se limitera ici à des exemples facilement compréhensibles.

:::tip
- Voir cours 103.7 Lesson 1 sur les expressions régulières, p.361
- Voir cours 103.7 Lesson 2 sur `grep` et `sed` p.372
- Voir aussi la section sur les filtres dans le TP sur la gestion des flux textes.
:::

:::link
Pour une introduction aux regex, voir les tutoriels <https://thevaluable.dev/regular-expression-basics-vim-grep/> et <https://thevaluable.dev/vim-regular-expressions-in-depth/>
:::

### grep

`grep` est l'une des commandes les plus pratiques dans un environnement de terminaux Linux. L'acronyme `grep` signifie « global regular expression print » (rechercher globalement les correspondances avec l'expression régulière). Cela signifie que vous pouvez utiliser `grep` pour voir si l'entrée qu'il reçoit correspond à un modèle spécifié. Apparemment trivial, ce programme est extrêmement puissant. Sa capacité à trier les entrées en fonction de règles complexes fait qu'il est couramment utilisé dans de nombreuses chaînes de commande.

#### Options courantes

- `-i` : Ignore la casse.
- `-r` : Recherche récursive dans les répertoires.
- `-v` : Inverse la recherche (affiche les lignes qui ne contiennent pas le motif).
- `-l` : Affiche seulement les noms des fichiers contenant le motif.
- `-n` : Affiche le numéro de ligne avec chaque correspondance.

### Travaux pratiques : la commande grep

1. Récupérer le fichier de la licence GPL v3 pour la suite des questions : `curl -o GPL-3 https://www.gnu.org/licenses/gpl-3.0.txt`
2. Utiliser `grep` et trouver toutes les lignes qui contiennent le mot `GNU`.
3. Recherchez chaque instance du mot `license` (en majuscule, minuscule ou les deux).
4. Recherchez chaque ligne qui ne contient pas le mot `the`.
5. Même question en ajoutant le numéro de ligne.
6. Trouver les lignes où `GNU` se trouve au tout début d'une ligne (utiliser une expression régulière).
7. Trouver les lignes où `and` se trouve en fin de ligne (utiliser une expression régulière).
8. Trouver les lignes qui en contiennent `too` ou `two`.
9. Trouver toutes les lignes qui commencent par une lettre majuscule.

:::link
Voir aussi les exercices : https://github.com/learnbyexample/TUI-apps
:::

:::correction

```
#2.
$ grep GNU GPL-3

---------------------------------------------------------

#3.
$ grep -i "license" GPL-3

---------------------------------------------------------

#4.
$ grep -v "the" GPL-3

---------------------------------------------------------

#5.
$ grep -vn "the" GPL-3

---------------------------------------------------------

#6.
$ grep "^GNU" GPL-3

---------------------------------------------------------

#7.
$ grep "and$" GPL-3

---------------------------------------------------------

#8.
$ grep "t[wo]o" GPL-3

---------------------------------------------------------

#9.
$ grep "^[A-Z]" GPL-3

# ou mieux :
$ grep "^[[:upper:]]" GPL-3
```
:::

### Autres commandes utilisant les expressions régulières

1. Affichez le nombre de mots dans tous les fichiers commençant par la lettre `h` dans le dossier `/etc`.

:::correction
```
$ wc -w /etc/{**/,}h*
```
:::

2. [Difficile] Quelle est la commande pour remplacer tous les séparateurs `:` dans le fichier `/etc/password` par le caractère `#` ?

:::correction
```
$ sed 's,^\([^:]*\):\([^:]*\):,\1#\2#,' -i /etc/password
```
:::
