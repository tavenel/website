---
title: TP - Gestion des utilisateurs
date: 2024 / 2025
---

1. Créez un utilisateur `tom` ayant comme `UID 1200`, comme groupe `users`, comme commentaire "_Chasseur de Jerry_" et comme shell `/bin/bash`. Créez bien entendu l'utilisateur avec son répertoire personnel.
2. Donnez le mot de passe `tomcat` à `tom`. Vous pouvez créer un mot de passe sans saisie par la commande `passwd` avec le paramètre `--stdin` si ce paramètre est disponible, sinon on pourra utiliser la commande `chpasswd` (sur systèmes Ubuntu par exemple).
3. Rajoutez un groupe `cat` avec le `GID 530`.
4. Ajoutez `tom` dans le groupe `cat` en éditant le fichier `/etc/group`. Pour cela rajoutez le nom `tom` à la fin de la ligne correspondante. 
5. Modifiez les informations de changement de mot de passe de `tom` avec la commande `chage`. Le mot de passe ne peut pas être changé avant 10 jours et il est obligatoire de le changer tous les 50 jours. 
6. Supprimez manuellement l’utilisateur `tom` du fichier `/etc/passwd` pour le retirer du système. Lancez ensuite la commande `pwck`. Rectifiez le problème. 

::: {.correction .if correction="true"}
1. Créez un utilisateur `tom` ayant comme `UID 1200`, comme groupe `users`, comme commentaire `Chasseur de Jerry` et comme shell `/bin/bash`. Créez bien entendu l'utilisateur avec son répertoire personnel.

```
# useradd -m -u 1200 -g users -c "Chasseur de Jerry" tom 
```

2. Donnez le mot de passe `tomcat` à `tom`. Vous pouvez créer un mot de passe sans saisie par la commande `passwd` avec le paramètre `--stdin`.

```
# echo tomcat | passwd -stdin tom 
```

3. Rajoutez un groupe `cat` avec le `GID 530`.

```
# groupadd -g 530 cat 
```

4. Ajoutez `tom` dans le groupe `cat` en éditant le fichier `/etc/group`. Pour cela rajoutez le nom `tom` à la fin de la ligne correspondante. 

```
cat:x:530:tom 
```

5. Modifiez les informations de changement de mot de passe de `tom` avec la commande `chage`. Le mot de passe ne peut pas être changé avant 10 jours et il est obligatoire de le changer tous les 50 jours. 

```
# chage tom 
Changing agin information for tom 
Minimum Password Age [7] : 10 
Maximum Password Age [40] : 50 
... 
```

6. Supprimez manuellement l’utilisateur `tom` du fichier `/etc/passwd` pour le retirer du système. Lancez ensuite la commande `pwck`. Rectifiez le problème. 

La commande vous informe que le groupe `cat` contient un utilisateur `tom` qui n’existe plus. 

Vous devez donc retirer `tom` du groupe `cat` pour conserver la cohérence du système. 
:::
