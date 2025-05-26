---
title: SysV
date: 2024 / 2025
correction: false
---

## SysV : init et runlevel

1. Si vous démarrez en mode graphique, modifiez `/etc/inittab` pour démarrer au niveau 3. 
2. Listez les services qui démarrent au niveau 3.
3. Passez à la console virtuelle 6 avec `[Alt][F6]` (ou `[Ctrl][Alt][F6]` sous environnement graphique X ou Wayland). Connectez-vous puis déconnectez-vous. Pourquoi le terminal revient-il au point de départ ?
4. La commande `runlevel` permet d'afficher le runlevel précédent (ou `N` s'il n'a pas changé) et le runlevel courant. Afficher ces runlevels.
5. La commande `telinit N` (avec `N` un runlevel) permet de changer de runlevel dynamiquement (sans redémarrer). Passer en mode single-user.
6. Avec la commande `shutdown`, éteignez l’ordinateur maintenant. Quel est le niveau d’exécution activé ? 

:::correction
1. Si vous démarrez en mode graphique, modifiez `/etc/inittab` pour démarrer au niveau 3. 

Changez la valeur de 5 à 3 sur la ligne `initdefault` et redémarrez. 

```
id:3:initdefault: 
```

2. Listez les services qui démarrent au niveau 3.

```sh
ls -l /etc/init.d/rc3.d/S* 
```

3. Passez à la console virtuelle 6 avec `[Alt][F6]` (ou `[Ctrl][Alt][F6]` sous environnement graphique X ou Wayland). Connectez-vous puis déconnectez-vous. Pourquoi le terminal revient-il au point de départ ?

Parce que `/etc/inittab` contient la commande `respawn` qui permet au processus de se relancer s’il est terminé. 

4. La commande `runlevel` permet d'afficher le runlevel précédent (ou `N` s'il n'a pas changé) et le runlevel courant. Afficher ces runlevels.

```console
$ runlevel  
3 1
```

5. La commande `telinit N` (avec `N` un runlevel) permet de changer de runlevel dynamiquement (sans redémarrer). Passer en mode single-user.

```sh
telinit 1
```

6. Avec la commande `shutdown`, éteignez l’ordinateur maintenant. Quel est le niveau d’exécution activé ? 

```sh
shutdown -r now 
```

C’est le niveau 0, d’arrêt, qui est activé.
:::

