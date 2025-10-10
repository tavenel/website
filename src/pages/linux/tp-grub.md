---
title: TP - Grub
date: 2024 / 2025
---

## Utiliser GRUB pour changer le mot de passe root

But : démarrer Linux dans un mode minimal en cas de perte de mot de passe.

1. Démarrez votre machine Fedora et arrêtez-vous au menu de GRUB. Si vous êtes en mode graphique appuyez sur [Echap]. Sur l'entrée par défaut, appuyez sur la touche `e` pour éditer les informations de boot de ce menu. 
1. Au bout de la ligne commençant par `linux`, supprimer les instructions `rghb quiet` et ajoutez `init=/bin/sh` et appuyez sur `[Ctrl] + [X]`. Que fait cette modification ?
1. Au bout de quelques secondes, un prompt apparaît. Si besoin, passez en clavier français : `# loadkeys fr`
1. Remontez le système de fichiers racine en lecture seule : `# mount -o remount,rw /`
1. Tapez maintenant `passwd` et validez : vous pouvez changer le mot de passe de `root`. 
1. Redémarrer le système : puisque le "vrai" `init` n'a pas été chargé, le système ne sera pas capable de redémarrer proprement. Taper la commande `exit` puis fermer la machine virtuelle.

:::correction
La ligne `init=/bin/sh` change la commande d'`init` du noyau : au lieu de lancer `/sbin/init`, on lance un simple script shell (`/bin/sh` est le Bourne Shell, le shell script le plus minimal normalement disponible sur tout système de type Linux/Unix/POSIX/...)
:::

## Réparer Grub2

### Casser Grub pour le test

Dans un premier temps, nous allons détruire le bootloader pour nos tests. Redémarrer la machine virtuelle et ouvrir un terminal une fois connecté dans l'OS.

:::warn
**Avant toute action, faites un snapshot de votre machine virtuelle !!!**
:::

Sur un `UEFI` (changer `fedora` pour le nom du répertoire correspondant sur une autre distribution) :

```sh
# désinstallation
apt-get purge os-prober

# suppression de l'EFI
rm /boot/efi/EFI/fedora/grubx64.efi

# suppression du fichier de configuration
rm /boot/grub2/grub.cfg
# ou
rm /boot/grub/grub.cfg
```

Sur un `BIOS`:

```sh
# désinstallation
apt-get purge os-prober

# suppression du MBR
dd if=/dev/null of=/dev/sda bs=446 count=1
 
# suppression du fichier de configuration
rm /boot/grub/grub.cfg
```

### Réparer Grub2

1. Redémarrer la machine virtuelle et vérifier que le système ne démarre plus (erreur Grub).
2. Éteindre la machine virtuelle, et ajouter de nouveau le live-cd ubuntu (voir le TP d'installation) dans l'onglet Configuration / Stockage.
3. Démarrer la machine virtuelle sur le live-cd, choisir _Try ubuntu_.
4. Suivre le tutoriel suivant pour réparer le bootloader sur votre système : <https://debian-facile.org/doc:systeme:grub2:reparer>.
5. Redémarrer la machine (le DVD doit normalement s'enlever automatiquement de la configuration de virtualbox). Vérifier que le système démarre à nouveau correctement.

Quelques indications supplémentaires :

- Ne pas tenir compte des périphériques `/dev/loopXXX` présents sur la machine.
- On commence tout d'abord par récupérer sa partition système sur le disque dur et à la monter sur `/mnt/target`, sur le système en train de tourner par le live-cd.
- Dans le tutoriel, il est ensuite nécessaire de réaliser des _bind mount_ : `mount -o bind /dev /mnt/target/dev`. Cette commande permet de lier le répertoire `/dev` actuel au répertoire `/mnt/target/dev`. Ces opérations préparent le répertoire `/mnt/target` à être une "vrai" racine de partition Linux en ajoutant le contenu dynamique du système en train de tourner (`/dev`, `/sys`, ...) là où le noyau aurait dû les charger.
- **Attention : pour avoir du réseau par le suite il faut copier le fichier `/etc/resolv.conf` sur votre système : `cp /etc/resolv.conf /mnt/target/etc/`.**
- On effectue alors un _change root_ : `chroot /mnt/target`. Comme son nom l'indique, cela permet de changer l'emplacement de la partition `root` : pour le shell courant, le répertoire `/mnt/target` devient maintenant la racine `/` ! Il n'est donc plus possible de sortir de `/mnt/target` et le système se comporte comme si le noyau actuel (démarré depuis le live-cd) tournait le système Linux sur notre disque dur ! Cette fonctionnalité est à la base des technologies d'isolation et de conteneurisation sur Linux (`Docker`, ...)
