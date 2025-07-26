---
title: TP - Gestion avancée de fichiers - permissions, liens, recherche
date: 2024 / 2025
---

## Gestion des permissions

### Permissions standard

1. Créez un fichier `/tmp/test_permissions_file` et changez ses droits pour que le propriétaire ait tous les droits, et seuls les membres du même groupe peuvent lire le contenu du fichier.
2. Créez un dossier `/tmp/test_permissions_dir` et modifiez le propriétaire en `tom` et le groupe de ce dossier en `users` (ou un autre utilisateur et un autre groupe).
3. Tout le monde doit pouvoir **lister** les fichiers dans ce dossier, mais sans créer ou supprimer les fichiers. Changez les droits existants pour que tous les fichiers déjà créés dans ce répertoire appartiennent au groupe `users`. Placez les bons droits.
4. Créez un répertoire test dans `/tmp` avec les droits `rwxrwxrwx`. Créez-y un fichier et modifiez les droits de ce fichier en retirant le droit `w` au groupe et aux autres. Qui peut le supprimer ?

:::correction
```sh
# #1.
touch /tmp/test_permissions_file
chmod 750 /tmp/test_permissions_file

# #2.
mkdir /tmp/test_permissions_dir
chown tom:users /tmp/test_permissions_dir 

---------------------------------------------------------

# #3.
chmod 755 /tmp/test_permissions_dir
chmown -R :users /tmp/test_permissions_dir # -R : récursif

---------------------------------------------------------

# #4.
mkdir /tmp/test 
chmod 777 /tmp/test 
touch /tmp/test/toto 
chmod g-w,o-w /tmp/test/toto 
```

Tout le monde peut supprimer ce fichier : ses droits n’ont pas d’importance. Ce sont les droits du répertoire, notamment le droit d’écriture sur le répertoire, qui déterminent qui peut supprimer les fichiers dedans. 
:::

### `umask` - Restreindre des droits automatiquement 

Lors de la création d’un fichier ou d’un répertoire, des droits leur sont automatiquement assignés. Généralement, c’est `rw-r--r--` (644) pour un fichier et `rwxr-xr-x` (755) pour un répertoire.

Ces valeurs sont contrôlées par un masque, lui-même modifiable par la commande `umask`. La commande `umask` prend comme paramètre une valeur octale dont chaque droit individuel sera supprimé des droits d’accès maximum du fichier ou du répertoire. 

- Par défaut, tous les fichiers sont créés avec les droits 666 (`rw-rw-rw-`). 
- Par défaut tous les répertoires sont créés avec les droits 777 (`rwxrwxrwx`). 
- Puis le masque est appliqué. 
- Le masque est le même pour l’ensemble des fichiers. 
- Un masque ne modifie pas les droits des fichiers existants, mais seulement ceux des nouveaux fichiers. 

:::tip
Les droits par défaut (maximum) des fichiers et des répertoires ne sont pas identiques.

C’est logique : `w` comme le droit `x` permet de rentrer dans un répertoire, il est normal que celui-ci en dispose par défaut. Ce même droit est inutile par défaut sur les fichiers : seule une très petite minorité des fichiers sont des scripts et des programmes binaires. 
:::

:::tip
Le masque par défaut est 022, soit `----w--w-`. Pour obtenir cette valeur, tapez `umask` sans paramètre. 
:::


#### Calcul de masque 

Pour un fichier :

```
Défaut  rw-rw-rw- (666) 
Retirer ----w--w- (022) 
Reste   rw-r--r-- (644) 
```

Pour un répertoire :

```
Défaut  rwxrwxrwx (777) 
Retirer ----w--w- (022) 
Reste   rwxr-xr-x (755)
```

#### TP

Créez un masque restrictif : vous pouvez faire ce que vous voulez, le groupe a seulement accès aux répertoires et peut lire les fichiers, mais les autres ne peuvent rien faire. 

:::correction
- Le masque doit laisser passer tous les droits de l’utilisateur : `0`. 
- Le masque doit laisser passer les droits `r` et `x` pour les groupes. Seul `w` est masqué : `2`. 
- Le masque supprime tous les droits aux autres : `7`. 
- Résultat : `# umask 027`
:::

## Liens réels et symboliques

### Liens réels

1. Créer un fichier `target` et un lien réel `hardlink` vers ce fichier.
2. Afficher les attributs et l'inode de ces deux fichiers.
  - Que remarque-t-on ?
  - Comment savoir si le fichier `target` a des liens ?
3. Supprimer le fichier d'origine `target`.
  - Que remarque-t-on ?
4. Afficher le nombre de liens réels de votre répertoire utilisateur.
  - Que remarque-t-on ?


:::correction
```sh
# 1.
$ echo "Une ligne de contenu" > target
$ ln target hardlink

---------------------------------------------------------

# 2.
$ ls -l target hardlink

 274106 -rw-r--r--    2 tom      tom              0 Aug 28 10:35 hardlink
 274106 -rw-r--r--    2 tom      tom              0 Aug 28 10:35 target

# Les deux fichiers ont le même inode 274106, ce qui est normal.
# Attention, les inodes ne sont uniques que par partition !!
# Le numéro `2` avant les permissions indique le nombre de
# références au fichier (normalement `1` pour un fichier normal et 
# `2` pour un répertoire). Ici il y a donc bien 2 références au même fichier.

---------------------------------------------------------

# 3.
$ rm target
$ ls -li hardlink

 274106 -rw-r--r--    1 tom      tom              0 Aug 28 10:35 hardlink

# Le fichier `hardlink` n'a pas été supprimé !
# Seul le nombre de références à l'inode a été décrémenté.
# Le fichier ne sera supprimé que lorsque ce nombre atteint 0.

$ cat hardlink
Une ligne de contenu
```
:::

:::correction
```sh
# 4.
$ ls -lid ~
     33 drwxr-xr-x   16 tom      tom       600 Aug 28 09:33 /home/tom

# Le répertoire a 16 références (alors qu'aucun lien n'a été créé) !!!
# En réalité, ces liens existent bien - il s'agit des références spéciales
# créées avec le répertoire : `.` (et `..`).
# Ansi, `.` pour le répertoire courant et `..` pour chaque sous-répertoire
# sont des références à ce répertoire...
# Vérifions que ces références pointent bien sur l'inode `33` :

$ ls -lia /home/tom
total 1132504
     33 drwxr-xr-x   16 tom      tom            600 Aug 28 09:33 .
[...]

$ ls -lia /home/tom/.config 
total 12
    175 drwxr-xr-x   29 tom      tom            640 Aug 24 16:23 .
     33 drwxr-xr-x   16 tom      tom            600 Aug 28 09:33 ..
[...]

# Attention, ce comportement n'est pas vrai sur un système de fichiers de type `btrfs`.
# Les références spéciales existent bien mais
# le système de fichiers renvoie une unique référence par répertoire.

$ mount | grep btrfs
/dev/sda6 on /mnt/data type btrfs (rw,relatime,ssd,space_cache=v2,subvolid=5,subvol=/)

$ ls -lid /mnt/data/Documents
    256 drwxr-xr-x    1 tom   tom        96 Aug 26 14:00 /mnt/data/Documents
```
:::

### Liens symboliques

1. Créer un lien symbolique `symlink-erreur` vers `target-fausse`.
  - Que remarque-t-on ?
2. Créer un fichier `target` et un lien symbolique `symlink`. Vérifier le lien créé.
3. Supprimer le fichier `target`. Que se passe-t-il ? Pourquoi ?

:::correction
```sh
# 1.
$ ln -s target-fausse symlink-erreur
$ ls -l symlink-erreur

lrwxrwxrwx    1 tom   tom     6 Aug 28 10:56 symlink-erreur -> target-fausse

# Le lien est créé, même si la target n'existe pas.

---------------------------------------------------------

# 2.
$ ln -s target symlink
$ ls -l symlink target

lrwxrwxrwx    1 tom      tom              6 Aug 28 10:58 symlink -> target

# symlink pointe bien vers target.

---------------------------------------------------------

# 3.
$ ls -li symlink target
 274652 lrwxrwxrwx    1 tom      tom      6 Aug 28 10:58 symlink -> target
 274649 -rw-r--r--    1 tom      tom      6 Aug 28 10:58 target

# Il y a bien une seule référence à `target`
# (seules les liens réels comptent)
# et les fichiers symlink et target n'ont pas le même inode
# (fichiers différents).
# On peut donc supprimer le contenu de l'inode de target.

$ rm target
$ ls -li symlink target

ls: target: No such file or directory
 274652 lrwxrwxrwx    1 tom   tom        6 Aug 28 10:58 symlink -> target

$ cat symlink

cat: can't open 'symlink': No such file or directory

# Le lien symbolique existe encore mais est cassé.
```
:::


## Recherche de chemins de fichiers et de contenus

### La commande find

```sh
find [chemin...] [expression]
```

La commande `find` permet de rechercher de façon récursive dans un répertoire des fichiers selon certains critères de recherche commande le nom, le type, la date, la taille ou l'utilisateur.

Vous pouvez également agir sur la liste des fichiers trouvés.

:::tip
Options les plus courantes (voir le cours de la certification LPIC-1 p.530 pour plus d'options) :

- `-name` : filtre sur le nom (sensible à la casse, sinon `-iname`). **Attention à bien échapper les caractères spéciaux : `'*.pdf'` et non `*.pdf` !**
- `-type` : filtre sur le type **interne** de fichier (pas son extension) :
  + `-type f` : fichiers standards uniquement
  + `-type d` : répertoires uniquement
- `-maxdepth N` et `-mindepth N` : limiter la profondeur à N (maximum ou minimum). Par exemple : `-maxdepth 1` limite au répertoire courant.
- `-readable`, `-writable`, `-executable`, `-perm NNNN` : chercher par droits pour l'utilisateur courant
- `-empty`, `-size +5M`, `-size -100k`
- `-amin M`, `-cmin M`, `-mmin M`, `-atime J`, `-ctime J`, `-mtime J` : accès, modification d'un attribut de fichier, modification du contenu pour une période de `M` minutes ou `J` jours (supporte `+` et `-`).
:::

:::tip
Pour enchaîner une autre commande avec les résultats de chemins de fichiers récupérés par la commande `find`, on pourra utiliser l'option `-exec`. Cette option utilise un argument `{}` qui sera remplacé par le chemin du fichier trouvé, et doit finir par `\;` :

```sh
# Trouver les fichiers TXT dans le répertoire utilisateur et afficher leur contenu avec la commande CAT :
find ~ -type f -name '*.txt' -exec cat {} \;
```
:::

:::tip
Exemple : Compresser tous les fichiers textes de plus de 24 h :

```sh
find . -name "*.txt" -mtime 1 -type f -print0 | xargs -0 gzip
```
:::

:::tip
Quelques erreurs courantes :

- Attention à échapper tous les caractères spéciaux : `\*`, `'*.pdf'`, `\?`, `'f?.pdf`, `\(`, `\)`, `\;`.
	- Sans échapper le caractère `*`, celle-ci est évaluée par le _shell_ **avant** d'exécuter la commande `find` (or, on veut passer le caractère `*` en argument, sans l'évaluer). Par exemple, `find /home/tom -name *.c` ne va **~pas chercher les fichiers terminant par `.c` dans mon répertoire utilisateur~**. Les jokers (`*`, …) sont évalués **dans le répertoire courant avant d'exécuter une commande** : la commande précédente correspond par exemple à la commande réelle : `find /home/tom -name frcode.c locate.c word_io.c` si les fichiers `frcode.c`, `locate.c` et `word_io.c` sont présents **dans le répertoire courant**. On devra donc échapper la commande : `find /home/tom -name '*.c'` ou `find /home/tom -name \*.c` pour que la commande réellement exécutée par le shell soit bien : `find /home/tom -name *.c`
  - Messages d'erreur liés :
		- `find: paths must precede expression`
		- `find: possible unquoted pattern after predicate -name?`
- L'opérateur _et_ (`-a`) est implicite : `find -type f -name '*.pdf'` et `find -type f -a -name '*.pdf'` sont équivalents.
- L'opérateur _et_ (`-a`) est prioritaire sur l'opérateur _ou_ (`-o`) : la commande `find . -name afile -o -name bfile -print` va afficher (`print`) uniquement `bfile` car cette commande est équivalent à : `find . -name
       afile -o \( -name bfile -a -print \)`.
:::


### La commande locate

```sh
locate [option]... motif...
```

- Contrairement à `find` qui recherche en parcourant l'arborescence des fichiers, `locate` interroge une base de données des noms de fichiers du système alimentée par la commande `updatedb` (modifiable par `/etc/updatedb.conf`). Cela rend la recherche beaucoup plus rapide. 
- `locate` effectue une recherche par _pattern_ (et nom par chemin de fichier) : tout chemin contenant le pattern est retourné.
- Utiliser l'option `-i` pour une recherche insensible à la casse.


### TP


But : rechercher des fichiers avec `find`, `whereis` et `locate`.

1. Affichez tous les fichiers ayant une taille inférieure à 400 octets et ayant les droits 644. Utilisez les paramètres `-size` et `-perm` de la commande `find`.
2. Affichez tous les fichiers dans votre répertoire personnel ayant une taille inférieure à 400 blocs.
3. Listez en format long tous les fichiers du système vous appartenant modifiés il a plus de 7 jours. Utilisez les paramètres `-user` et `-mtime`.
4. Listez et affichez en format long les fichiers dans votre répertoire personnel qui ont comme propriétaire `guest` ou qui ont une taille entre 512 et 1024 octets, inclus.
5. Recherchez tous les fichiers vides du système n’appartenant pas à `root` et tentez de les supprimer. Utilisez les paramètres `-empty` et `-exec` pour exécuter un `rm` sur chaque fichier trouvé.
6. Indiquez où se situe la commande binaire `ls`. Utilisez la commande `whereis` pour cela.
7. Vous avez perdu le fichier `lettre_importante.odf`. Où est-il, sans utiliser `find` ?

:::correction
1. Affichez tous les fichiers ayant une taille inférieure à 400 octets et ayant les droits 644. Utilisez les paramètres `-size` et `-perm` de la commande `find`.

```sh
$ find / -size -400c -perm 644 -print
```

2. Affichez tous les fichiers dans votre répertoire personnel ayant une taille inférieure à 400 blocs.

```sh
$ find ~ -size -400 -print
```

3. Listez en format long tous les fichiers du système vous appartenant modifiés il a plus de 7 jours. Utilisez les paramètres `-user` et `-mtime`.

```sh
$ find / -user seb -mtime +7 -ls
```

4. Listez et affichez en format long les fichiers dans votre répertoire personnel qui ont comme propriétaire `guest` ou qui ont une taille entre 512 et 1024 octets, inclus.
 
Le petit piège réside ici dans le “inclus”. Si vous indiquez +512c, les fichiers de 512 octets sont exclus. Vous devez modifier les bornes en conséquence.

```sh
$ find ~ -user guest -size +511c -size -1025c -ls
```

5. Recherchez tous les fichiers vides du système n’appartenant pas à `root` et tentez de les supprimer. Utilisez les paramètres `-empty` et `-exec` pour exécuter un `rm` sur chaque fichier trouvé.

```sh
$ find / -type f -empty -exec rm -f {} \;
```

6. Indiquez où se situe la commande binaire `ls`. Utilisez la commande `whereis` pour cela.

```sh
$ whereis -b ls
```

7. Vous avez perdu le fichier `lettre_importante.odf`. Où est-il, sans utiliser `find` ?

Pour répondre il faut que la base locatedb soit déjà construite avec `updatedb`. Ensuite utilisez la commande `locate` :

```sh
$ locate lettre_importante.odf 
```
:::
