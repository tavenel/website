---
title: TP - Bibliothèques partagées
date: 2024 / 2025
---

:::tip
Voir aussi la [wikiversité][wiki-shared-lib]
:::

1. Afficher la liste des dépendances du programme `cp`.

:::correction

```console
$ ldd -d -v /bin/cp
  libc.so.6 => /lib/libc.so.6 (0x40027000)
  /lib/ld-linux.so.2 => /lib/ld-linux.so.2 (0x40000000)

  Version information:
  /bin/cp:
               libc.so.6 (GLIBC_2.1.3) => /lib/libc.so.6
               libc.so.6 (GLIBC_2.1) => /lib/libc.so.6
               libc.so.6 (GLIBC_2.2) => /lib/libc.so.6
               libc.so.6 (GLIBC_2.0) => /lib/libc.so.6
  /lib/libc.so.6:
               ld-linux.so.2 (GLIBC_2.1.1) => /lib/ldlinux.so.2
               ld-linux.so.2 (GLIBC_2.2.3) => /lib/ldlinux.so.2
               ld-linux.so.2 (GLIBC_2.1) => /lib/ldlinux.so.2
               ld-linux.so.2 (GLIBC_2.2) => /lib/ld-linux.so.2
               ld-linux.so.2 (GLIBC_2.0) => /lib/ld-linux.so.2
```

:::

2. En tant que `root` déplacez une des librairies requises par `cp` (par exemple `libacl.so.*`) dans `/tmp/lib/`. Exécutez de nouveau `ldd`. Pouvez-vous lancer la commande `cp` ? Expliquez.

Exécutez ensuite la commande `ldconfig`.

:::correction

```sh
mkdir /tmp/lib
mv /lib/x86_64-linux-gnu/libacl.so* /tmp/lib
```

Exécutez cp - le programme ne se lance pas car la librairie est introuvable.

La commande `ldd` vous informe de la disparition de la bibliothèque déplacée :

```
libacl.so.1 => not found
```

:::

3. Éditez le fichier de configuration `/etc/ld.so.conf` et rajoutez-y le chemin `/tmp/lib`. Exécutez à nouveau `ldconfig` puis relancez la commande `cp`. Que se passe-t-il ?

:::correction
En rajoutant le chemin `/tmp/lib` puis en mettant à jour le cache du chargeur dynamique avec `ldconfig`, la bibliothèque est de nouveau accessible.

```console
$ vi /etc/ld.so.conf
/tmp/lib/
---------------------------------------------------------

$ ldconfig

---------------------------------------------------------

$ ldd /bin/cp
libacl.so.1 => /tmp/lib/libacl.so.1
```

Le programme fonctionne à nouveau.
:::

4. Remettez tout dans l'état initial. Déplacez la bibliothèque vers sa position d'origine, supprimez `/tmp/lib` de `ld.so.conf` et relancez `ldconfig`. Supprimez `/tmp/lib`.

[wiki-shared-lib]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/Installation_de_Linux_et_gestion_des_packages/G%C3%A9rer_les_biblioth%C3%A8ques_partag%C3%A9es
