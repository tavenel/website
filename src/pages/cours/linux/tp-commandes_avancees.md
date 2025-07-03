---
title: Utilisation des commandes avancées Linux
date: 2024 / 2025
---

*L’ensemble de ce TP sera réalisé avec le compte utilisateur créé à l'installation de la machine virtuelle - voir le prérequis du TP précédent si celui-ci a été oublié.*

## Gestion des droits d’accès

- Créez un nouveau fichier `droitsParDefaut` dans votre répertoire utilisateur.
- En utilisant la commande `ls`, listez les droits par défaut à la création d’un nouveau fichier.
- Ajoutez le droit d’exécution pour l'utilisateur courant, retirez le droit de modification pour le reste du groupe et retirez le droit de lecture pour le reste du monde.
- Changez le propriétaire du fichier pour le faire appartenir à l'utilisateur `root`.
- Essayez de lire le contenu du fichier.
- Supprimez le fichier.

## Exécution de scripts

- Créez un répertoire `mesBinaires` dans votre répertoire utilisateur.
- Dans ce répertoire, créez un fichier de script nommé `mesProcessus` permettant d’afficher les processus de l’utilisateur courant.
- Ajoutez les droits d’exécution pour le propriétaire à votre fichier de scripts.
- Ajoutez le répertoire `mesBinaires` dans la variable `$PATH`.
- Exécutez votre script en exécutant directement votre commande : `$ mesProcessus`.

## Enchaînement de commandes

- En utilisant la commande `sort`, exécutez un enchaînement de commandes permettant de lister les utilisateurs du fichier `/etc/passwd` par ordre alphabétique.
- En utilisant un pipe de terminal (symbole `|` ), exécutez une commande permettant de rechercher dans les configurations du système tout fichier faisant référence à votre utilisateur. Ne pas utiliser l'argument récursif de `grep` (`grep -r`) car cet argument n'est pas POSIX : cet argument n'est donc pas disponible sur beaucoup de systèmes.
- Tester le résultat de la commande suivante : `sudo echo "salut" | id`. Que remarque-t-on ? Pourquoi ?

:::tip
Pour enchaîner des commandes, il peut être utile d'utiliser la commande `xargs`. Cette commande traite l'entrée standard `STDIN` ligne par ligne pour exécuter la commande suivante pour chacune des lignes rencontrées, en ajoutant à la fin de la commande le contenu de la ligne.

Cette commande est utile pour exécuter des commandes ayant besoin de noms de fichiers, par exemple :
```sh
find … | xargs grep <mon_pattern>
```

Cela va exécuter `grep <mon_pattern>` pour chacun des fichiers trouvés précédemment.
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Linux is a registered trademark of The Linux Foundation in the United States and/or other countries.
