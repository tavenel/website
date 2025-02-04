---
title: Création de scripts Bash
date: 2024 / 2025
---

## Création de scripts Bash

Un script est un fichier listant une suite de commandes à exécuter sur un système.

Pour créer un script sous Linux, on effectue les opérations suivantes :

- On crée un nouveau fichier, par exemple : `monScript.sh`
- On ajoute au début de ce fichier un `shebang` : c’est une ligne spéciale qui décrit au système quel est le langage utilisé dans le fichier de script.

Dans notre cas, nous utilisons le shell `Bash`, le `shebang` associé sera donc :

```bash
#!/usr/bin/env bash
```

- On complète ensuite le script, en ajoutant une commande par ligne. Ces commandes seront exécutées l'une après l'autre.
- On ajoute les droits d’exécution au fichier.
- On exécute le script :

```bash
./monScript.sh
```

## Script 1

Créer un premier script ayant le comportement suivant :

- Créer une variable `monMessage` contenant un texte de votre choix.
- Afficher le contenu de la variable `monMessage` à l’écran.
- Stocker le contenu de la variable `monMessage` dans un fichier `/tmp/monScript.out`.

:::correction
```bash
#!/usr/bin/env bash

monMessage='Hello'
echo $monMessage
echo $monMessage > /tmp/monScript.out
```
:::

## Script 2

Modifier le script précédent pour demander à l'utilisateur le contenu du message à stocker dans le fichier à l'aide de la commande `read`.

On pourra utiliser la page de manuel de la commande `read` pour connaître la syntaxe de cette commande (ou `help read` si la page de manuel n'est pas installée).

:::correction
```bash
#!/usr/bin/env bash

read -p 'Quel est le message? : ' monMessage
echo $monMessage
echo $monMessage > /tmp/monScript.out
```
:::

## Script 3

Créer un nouveau script qui demande deux nombres à l'utilisateur, et affiche à l'écran le résultat de leur multiplication.

:::tip
Pour effectuer une opération arithmétique en Bash, on peut utiliser l'opérateur `$(())`, par exemple : `$((1+2))`.
:::

:::correction
```bash
#!/usr/bin/env bash

echo 'Ce script multiplie 2 nombres'
read -p 'Quel est le 1er nombre ? : ' nombre1
read -p 'Quel est le 2e nombre ? : ' nombre2
echo "Le résultat de la multiplication est : $((nombre1*nombre2))"
```
:::

## Script 4

`Bash` supporte le passage de paramètres directement à l'exécution du script, de façon similaire à toute autre commande : `./monScript.sh <param1> <param2> ...`

Pour cela, le script dispose de variable d’environnement prédéfinies :

- `$#` : contient le nombre de paramètres
- `$0` : contient le nom du script exécuté
- `$1` : contient le premier paramètre
- `$2` : contient le second paramètre
- …

Modifier le script précédent pour effectuer l’addition de 3 nombres passés en paramètres.

:::correction
```bash
#!/usr/bin/env bash

echo "Le résultat de la multiplication de $1 par $2 et $3 est : $(($1*$2*$3))"
exit
```
:::

## Script 5

La condition `if` permet d’effectuer un branchement conditionnel : si la condition à tester est vraie, on exécute la commande à la suite du `then`, sinon on exécute la commande à la suite du `else`.

La syntaxe est la suivante (attention aux espaces !) :

```bash
if [ $maVariable = "monTest1" ]
then
	echo "Mon test 1 réussi"
elif [ $maVariable = "monTest2" ]
then
	echo "Mon test 2 réussi"
else
	echo "Tests 1 et 2 échoués"
fi
```

En utilisant une condition `if`, demander à l'utilisateur d’entrer un mot et vérifier que le mot entré est bien celui attendu.

:::correction
```bash
#!/usr/bin/env bash

read -p 'Entrer le mot : "toto" : ' mot
if [[ "$mot" != "toto" ]]; then
    echo "Le mot $mot n'est pas celui attendu !" > /dev/stderr && exit 2
else
    echo "Le mot $mot est bien : 'toto'" && exit
fi
exit
```
:::

## Script 6

Utiliser une condition `if` pour tester le nombre de paramètres fournis dans le script 4.

Si le nombre de paramètres n’est pas correct, on pourra quitter le script avec la commande `exit`.

Rappel : la commande `exit` prend en paramètre le code de retour du script. Par convention, on renvoie 0 en cas de succès (c’est en fait ce que fait le shell `Bash` automatiquement pour nous), et une valeur différente de 0 en cas d’échec.

:::correction
```bash
#!/usr/bin/env bash

usage() {
    echo "$0 <nombre1> <nombre2> <nombre3>"
}

if [ $# != 3 ]; then
    echo "Attention : mauvais passage de paramètres !" > /dev/stderr
    usage > /dev/stderr
    exit 1
fi

# Ou directement :
# [ $# != 3 ] && echo "Attention : mauvais passage de paramètres !" > /dev/stderr && usage > /dev/stderr && exit 1

echo "Le résultat de la multiplication de $1 par $2 et $3 est : $(($1*$2*$3))"
exit
```
:::

## Script 7

Toute commande (qu'il s’agisse d’un programme du système ou d’un script utilisateur) finit son exécution par un code de retour (0 en cas de succès, valeur autre que 0 en cas d’échec).

Le code de retour de la commande précédente est stocké dans la variable point d’interrogation : `?`

- Lister les informations du fichier `/fichierNonExistant` en redirigeant la sortie standard et la sortie d’erreur vers la sortie nulle : `/dev/null`.
- Tester le code de retour de la commande utilisée pour lister le fichier. En cas d’erreur, afficher un message d’erreur à l'utilisateur.

:::correction
```bash
#!/usr/bin/env bash

ls /fichierNonExistant >/dev/null 2>/dev/null
# Ou en redirigeant la sortie d'erreur (2) vers la sortie standard (1) :
# ls /fichierNonExistant >/dev/null 2>&1 

[ $? != 0 ] && echo "Le fichier n'existe pas !" > /dev/stderr && exit 2
exit
```
:::

## Script 8 : Niveau avancé

Comment faire lorsque l'on ne connaît pas le nombre exact de paramètres fournis en entrée du script ?

Dans ce cas, la commande `shift` permet d’itérer sur chaque argument en les consommant : après chaque appel, la variable `$1` contiendra la valeur du 1er argument, puis du 2e, puis du 3e, ...

On utilise généralement cette commande avec la fonction `while` qui permet d’exécuter une boucle tant que la condition passée en paramètre est satisfaite.

En utilisant la fonction `while` et la commande `shift`, modifier le script 4 pour effectuer l'addition de tous les paramètres, quel que soit le nombre de paramètres fournis par l'utilisateur.

:::correction
```bash
#!/usr/bin/env bash

result=0
while [ $# != 0 ]; do
	result=$(($result+$1))
	shift
done

echo $result
exit
```
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Linux is a registered trademark of The Linux Foundation in the United States and/or other countries.
