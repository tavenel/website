---
title: "TP : Gestion des permissions avancées avec SUID, SGID et ACL sous Linux"
---

## Objectif du TP

Ce TP a pour objectif d'apprendre l'utilisation des permissions avancées sous Linux, à savoir le SUID, le SGID et les listes de contrôle d'accès (ACL). À la fin de ce TP, vous serez capable de configurer des permissions avancées pour différents utilisateurs et groupes.

### 📋 Prérequis

- Avoir des connaissances de base sur les permissions standards (rwx).

## Partie 1 : Comprendre et manipuler le SUID

### Qu'est-ce que le SUID ?

Le `SUID` (Set User ID) est un mécanisme de permission qui permet à un utilisateur d'exécuter un fichier avec les privilèges de son propriétaire, plutôt qu'avec ses propres privilèges.

### Étape 1 : Création d'un fichier avec le SUID

1. Créez un script simple appartenant à root et affichant qui est l'utilisateur courant du script.
2. Rendre ce script exécutable et tester son exécution
3. Modifiez les permissions pour activer le SUID et tester l'exécution du script

:::warn
La plupart des distributions récentes ont un noyau qui refuse l'exécution de `SUID` pour les scripts shells par mesure de sécurité.

On pourra à la place utiliser un petit programme en C qui affiche l'utilisateur courant :

```
#include <stdio.h>
#include <unistd.h>

int main(int argc, char** argv) {
    printf("%d", geteuid());
    return 0;
}
```

Et le compiler en utilisant :

```bash
gcc -o setuid-test setuid-test.c
./setuid-test
```
:::

:::correction
```sh
#!/bin/bash
echo "Le fichier est exécuté avec les privilèges de $(whoami)"
```

```sh
chmod +x suid_script.sh
sudo chown root:root suid_script.sh
./suid_script.sh
# tom
```

```sh
sudo chmod u+s suid_script.sh
./suid_script.sh
# root
```
:::


## Partie 2 : Comprendre et manipuler le SGID

### Qu'est-ce que le SGID ?

Le SGID (Set Group ID) est similaire au SUID, mais il affecte le groupe propriétaire du fichier. Il permet à un utilisateur d'exécuter un fichier avec les privilèges du groupe propriétaire.

### Étape 1 : Création d'un fichier avec le SGID

1. Créez un répertoire de test :
    ```sh
    mkdir /tmp/sgid_test
    ```

2. Modifiez les permissions du répertoire pour activer le SGID :
    ```sh
    chmod g+s /tmp/sgid_test
    ```

3. Ajoutez un fichier dans le répertoire :
    ```sh
    touch /tmp/sgid_test/fichier_test.txt
    ```

4. Vérifiez les permissions du fichier et du répertoire :
    ```sh
    ls -l /tmp/sgid_test
    ```

### Question :

Expliquez ce que fait le SGID dans cet exemple. Que se passe-t-il lorsque vous ajoutez des fichiers dans ce répertoire ?

:::correction
Le SGID (Set Group ID) applique les privilèges du groupe propriétaire à tout fichier créé dans le répertoire. Dans l'exemple, lorsque le SGID est activé sur le répertoire `/tmp/sgid_test`, tout fichier créé dans ce répertoire hérite automatiquement du groupe du répertoire, plutôt que du groupe de l'utilisateur qui a créé le fichier. Cela permet d'assurer que tous les fichiers créés dans un répertoire partagé appartiennent à un même groupe, facilitant la collaboration entre les membres de ce groupe.
:::

## Partie 3 : Gestion des ACL

### Qu'est-ce que les ACL ?

Les ACL (Access Control List) permettent de définir des permissions supplémentaires plus fines que celles offertes par les permissions standards (rwx). Les ACL sont utiles lorsque plusieurs utilisateurs ou groupes nécessitent des permissions différentes sur un fichier ou un répertoire.

### Étape 1 : Activation des ACL

1. Assurez-vous que le système de fichiers supporte les ACL :
    ```sh
    sudo tune2fs -l /dev/root | grep "Default mount options:"
    ```

    Si ce n'est pas le cas, activez les `acl` pour votre système de fichiers : `sudo tune2fs -o acl /dev/root` et redémarrez la machine ou remontez le système de fichiers : `mount -o remount /`
    Si besoin, installez également le paquet `acl` (sous _Debian_ ou _Ubuntu_) afin d'avoir les commandes `getfacl` et `setfacl`.

### Étape 2 : Gestion des ACL avec `setfacl` et `getfacl`

1. Créez un fichier de test :
    ```sh
    touch fichier_acl.txt
    ```

2. Ajoutez une permission spécifique pour un utilisateur (par exemple `user1`) :
    ```sh
    setfacl -m u:user1:r fichier_acl.txt
    ```

3. Vérifiez les ACL du fichier :
    ```sh
    getfacl fichier_acl.txt
    ```

4. Ajoutez une permission pour un groupe (par exemple `group1`) :
    ```sh
    setfacl -m g:group1:rw fichier_acl.txt
    ```

5. Supprimez une ACL pour un utilisateur :
    ```sh
    setfacl -x u:user1 fichier_acl.txt
    ```

### Question :

Pourquoi utiliser des ACL plutôt que les permissions standard ? Donnez un exemple de cas où cela est utile.

:::correction
Les ACL permettent de définir des permissions plus fines que les permissions standard rwx. Les permissions standard ne permettent de définir des droits d'accès qu'à trois entités : le propriétaire, le groupe, et les autres utilisateurs. Avec les ACL, vous pouvez spécifier des permissions pour des utilisateurs et des groupes supplémentaires, sans changer la propriété ou les groupes principaux du fichier.

Exemple de cas utile : Supposons que vous ayez un fichier accessible par un groupe de collaborateurs, mais qu'un seul membre d'un autre groupe ait besoin d'y accéder en écriture. Au lieu de changer la propriété ou de créer un groupe spécifique, vous pouvez utiliser les ACL pour attribuer l'accès en écriture à cet utilisateur, tout en laissant les autres utilisateurs du groupe avec les permissions habituelles.
:::

