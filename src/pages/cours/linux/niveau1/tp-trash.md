---
title: Poubelle - commande trash
date: 2024 / 2025
correction: false
---

## Objectif

_L'objectif de cet exercice est de créer une commande `trash` qui déplacera les fichiers dans un répertoire poubelle au lieu de les effacer._

## Étapes

1. Créez un répertoire `~/Poubelle`.
2. Créez un fichier `trash` dans le répertoire `~/bin` ayant pour première ligne `#!/usr/bin/env bash` contenant la suite de commandes nécessaire pour déplacer tous les fichiers passés en argument sur la ligne de commande dans le répertoire `~/Poubelle`.
   On utilisera une boucle `for` et `$*`. On tapera par exemple : `trash *.txt` pour effacer tous les fichiers se terminant par `txt`.
3. Rendre le fichier `trash` exécutable : on utilisera la commande `chmod`.
4. Testez la commande `trash`. Remarque : taper uniquement `trash` ne fonctionnera pas car cette commande n'est pas connue du système, il faudra utiliser le chemin vers le fichier `trash` comme commande (par exemple : `~/bin/trash`).
5. Ajoutez le répertoire `~/bin` dans votre `$PATH` avec la commande suivante : `PATH=~/bin:$PATH && export PATH`. Pourquoi fait-on cela ?
6. Ajouter une option `-c` à la commande telle que `trash -c` affiche la taille du contenu du répertoire poubelle. On utilisera la commande `du -sk` (cf. `man`).
7. Ajouter une option `-e` permettant de vider le contenu de la poubelle.
8. Ajouter une option `-h` affichant une aide analogue à celle de `cp -h`.
9. En utilisant un `alias`, utiliser la commande `trash` plutôt que la commande `rm` pour déplacer un fichier vers la poubelle plutôt que de le supprimer.

::: {.correction .if correction="true"}
## Correction

```bash
#!/usr/bin/env bash

usage()
{
    echo 'Usage : $0 [-h|-e|-c] [fichier1 ... fichiern]'
}

if [ -z $1 ]; then
    usage > /dev/stderr && exit 1
fi

if [[ $1 == '-h' ]]; then
    usage > /dev/stderr && exit 0
elif [[ $1 == '-c' ]]; then
    du -sk ~/Poubelle
    exit 0
elif [[ $1 == '-e' ]]; then
    rm -rf ~/Poubelle/*
    exit 0
fi

for i in $*; do
    mv $i ~/Poubelle
done
```
:::
