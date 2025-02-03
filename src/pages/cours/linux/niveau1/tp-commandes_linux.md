---
title: Utilisation des commandes Linux
date: 2024 / 2025
---

# Prérequis

_L’ensemble de ce TP sera réalisé avec le compte utilisateur créé à l'installation de la machine virtuelle (ne pas se connecter avec le compte du super-utilisateur `root` )._

## Réinitialisation du mot de passe administrateur (root)

Si vous avez oublié votre mot de passe utilisateur, vous pouvez utiliser la méthode suivante :

- Connectez-vous avec l’utilisateur `root` (mot de passe : osboxes.org)
- Tapez la commande :

```sh
# passwd NOM_DE_VOTRE_UTILISATEUR
```

Cette commande permet de changer le mot de passe de votre utilisateur.

Tapez la commande exit pour revenir à l’écran de connexion et utilisez votre utilisateur avec son nouveau mot de passe.

# Gestion des fichiers

## Rappel : répertoire utilisateur

*Remarque : par défaut, après la connexion d’un utilisateur le système vous place dans votre répertoire de travail : `/home/NOM_DE_VOTRE_UTILISATEUR`*

*A tout moment, on pourra revenir facilement dans ce répertoire de travail grâce à la commande cd, utilisée sans paramètre :*

```sh
$ cd
```

## Manipulation de fichiers

- Créez un nouveau répertoire `tp2` dans votre répertoire utilisateur.
- Déplacez-vous dans ce nouveau répertoire.
- Créez un nouveau fichier `fichier1`.
- Listez le nouveau fichier pour vérifier sa création.
- Changez le nom de ce fichier en `fichier2`.
- Créez un nouveau répertoire `sousRepertoire` dans le répertoire courant (`tp2`).
- Déplacez le fichier `fichier2` dans le répertoire `sousRepertoire`.
- Supprimez le fichier `fichier2`.
- Supprimez le répertoire `sousRepertoire`.

## Affichage du contenu d’un fichier

- Afficher le contenu du fichier `/etc/passwd`.

## Utilisations avancées

- Créer un nouveau fichier `fichierAvance1` dans le répertoire `/root`.
- *Comme toutes les commandes du shell, la commande `ls` utilisée pour afficher des informations sur un fichier est en fait un programme dédié, installé sur le système* :
  + Rechercher le chemin du fichier `ls` installé sur le système (on pourra utiliser la commande `find`).

# Hacker le shell

## Utilisation des filtres

- Créez un nouveau répertoire `hack` dans votre répertoire utilisateur.
- Déplacez-vous dans le répertoire `hack`.
- Créez des nouveaux fichiers :
   - un nouveau fichier `fichier1.txt`
   - un nouveau fichier `fichier2.txt`
   - un nouveau fichier `fichier3.bin`
- En utilisant des filtres du shell :
   - Listez les fichiers `fichier1.txt` et `fichier2.txt`
   - Listez les fichiers `fichier1.txt` et `fichier2.txt` et `fichier3.bin`
- Utilisation avancée :
   - Listez l'ensemble des chemins des fichiers dont l'extension est `.bin` sur le système.

## Redirections

- Créer un nouveau fichier `redirect`.
- Redirigez la sortie standard de la commande `$ ls –l redirect` (permettant de lister toutes les informations sur le fichier `redirect`) dans un fichier `redirect.out`
- Affichez le contenu du fichier `redirect.out`
- Redirigez la sortie standard de la commande `$ ls –l fichierNonExistant` dans un fichier `fichierNonExistant.out`
- Quel est le contenu du fichier `fichierNonExistant.out` ? Pourquoi ?
- Redirigez la sortie d'erreur de la commande `$ ls –l fichierNonExistant` dans un fichier `fichierNonExistant.err`
- Vérifiez que l'erreur n’est plus affichée sur la console, mais stockée dans le fichier `fichierNonExistant.err`

# Les processus

## Les basiques

- Listez les processus de l'utilisateur courant.
- Listez l'arbre des processus de l'utilisateur courant.
- Listez les utilisateurs connectés sur le système.

## Utilisation avancée

- Lister l'ensemble des processus de tous les utilisateurs.
- Lister l'ensemble des processus de tous les utilisateurs avec la commande ayant lancé le processus.
- Tuer un processus :
  + Lancez la commande : `$ sleep 600 &`
  + Cette commande permet d’exécuter une boucle d’attente pendant 600s en arrière-plan.
  + Attention à bien ajouter le caractère `&` en fin de commande : c’est ce caractère qui transforme la commande d’avant plan (comportement standard) en processus d’arrière-plan.
- En listant les processus de l’utilisateur courant, récupérez l'identifiant de processus (`pid`) de cette commande.
- Tuez la commande `sleep` en arrière-plan, en utilisant son identifiant de processus.
- Listez les processus de l'utilisateur courant pour vérifier que la commande n’est plus présente.

# Chemins absolus et relatifs

## Rappels de cours

Il existe 2 façons d'accéder à un fichier dans un environnement Linux :

- En utilisant un chemin de fichier absolu, commençant par un `/` (le chemin du fichier depuis la racine, par exemple : `/etc/passwd`).
- En utilisant un chemin de fichier relatif (le chemin d’accès au fichier depuis le répertoire courant, par exemple : `monSousRepertoire/monAutreRepertoire/monFichier`).

À tout moment, on pourra afficher le répertoire de travail courant grâce à la commande :

```sh
$ pwd
```

## Chemins relatifs

Placez-vous dans votre répertoire utilisateur. Ensuite, en utilisant uniquement des chemins de fichier relatifs, et sans se déplacer :

- Créer un nouveau répertoire `repertoireRelatif` dans le répertoire courant.
- Créer un nouveau fichier `monFichier` dans le répertoire `repertoireRelatif`.
- Lister les informations du fichier `monFichier`.

## Chemins absolus

Toujours sans vous déplacer de votre répertoire utilisateur, et en utilisant uniquement des chemins de fichier absolus :

- Créer un nouveau répertoire `repertoireAbsolu` dans le répertoire `/tmp`.
- Créer un nouveau fichier `monFichier` dans le répertoire `repertoireAbsolu`.
- Lister les informations du fichier `monFichier`.

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Linux is a registered trademark of The Linux Foundation in the United States and/or other countries.
