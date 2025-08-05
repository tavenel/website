---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Architecture matérielle et gestion des périphériques
layout: '@layouts/CoursePartLayout.astro'
---

## Détermination et configuration des paramètres du matériel

---

### Architecture PC de base

_Quels sont les composants principaux d'une architecture PC ?_

- Central Processing Unit (CPU)
- Random Access Memory (RAM) and Read-Only Memory (ROM)
- Basic Input/Output System (BIOS), ou UEFI (chap.2)
- Les bus
- Les disques

---

![Diagramme d'architecture du kernel](https://upload.wikimedia.org/wikipedia/commons/c/cf/Linux_kernel_diagram.svg)

<div class="caption">Diagramme d'architecture du kernel</div>

[Linux kernel diagram : architecture haut niveau](https://commons.wikimedia.org/wiki/File:Linux_kernel_diagram.svg)

<div class="caption">Linux kernel diagram : architecture haut niveau</div>

---

![Linux kernel map](https://upload.wikimedia.org/wikipedia/commons/5/5b/Linux_kernel_map.png)

[_Linux kernel map (pour info)_](https://commons.wikimedia.org/wiki/File:Linux_kernel_map.png)

<div class="caption">Linux kernel map</div>

---

### Gestion des périphériques

---

#### Les bus

- [ISA (obsolète)](https://www.materiel-informatique.be/isa.php)
- [PIC (obsolète)](https://www.materiel-informatique.be/pci.php)
- [AGP (carte graphique)](https://www.materiel-informatique.be/agp.php)
- [PCI Express](https://www.materiel-informatique.be/pci-express.php)

---

#### Allocation de ressources

- Communication par CPU : _Interrupt Request Number (IRQ 0-15)_ `/proc/interrupts`
- Transfert direct de données par RAM : _Direct Memory Access (DMA)_ `/proc/dma`
- Adresses Entrées/Sorties (I/O ports) pour lecture / écriture `/proc/ioports`

---

### /proc et /sysfs

- `/proc` : système de fichiers virtuel en mémoire, gère l'état du système et les processus
  + `/proc/cpuinfo`, `/proc/<PID>/status`, ...
- `/sys` (ou `sysfs`) : gestion des périphériques & config du noyau

---

### Userspace Dev (udev)

- Gère les fichiers de `/dev` pouvant être gérés sans droits d'administration (clé USB, ...)
- Gère les événements _userspace_ en cas d'ajout/suppression d'un périphérique matériel (clé USB, ...)
- `udevd`, `D-Bus`

:::tip
_udev_ est le gestionnaire de périphériques dans les distributions modernes.
:::

- **Outils** :

```sh
udevinfo -p /sys/class/net/eth0/ -a
udevadm info -q all -n /dev/sda
udevadm monitor
```

- **Règles udev personnalisées** :
  - `/etc/udev/rules.d/`
  - `/lib/udev/rules.d/`

Exemple de règle udev :

```
ACTION=="add", KERNEL=="sdb", RUN+="/usr/local/bin/myscript.sh"
```

- Recharger udev :

```sh
udevadm control --reload-rules
```

---

### Commandes utiles

- `dmesg` : kernel ring buffer (messages du noyau)
- `lspci` (fichier `/proc/bus/pci`)
- `lsusb`
- `uname -a` : informations sur le système
- fichiers de logs : `/var/log/`
- Voir le TP dédié [tp-systeme][tp-systeme].

---

## Modules Noyau (Kernel Modules)

Composants logiciels chargés et déchargés dynamiquement dans le noyau Linux

---

### 🌟 Avantages

- Flexibilité : Possibilité d'ajouter/supprimer des fonctionnalités au noyau sans redémarrage.
- Sécurité : Permet de maintenir la taille du noyau initial plus petite.
- Maintenance : Facilite les mises à jour et la maintenance du noyau en isolant les changements.
- Gestion de dépendances

---

### Commandes utiles

- Chargement d'un module : `modprobe <nom_du_module>`
- Déchargement d'un module : `modprobe -r <nom_du_module>`
- Liste des modules chargés : `lsmod`
- Informations sur un module : `modinfo <nom_du_module>`
- Chargement au démarrage : `modprobe.conf` (ou `/etc/modprobe.d/`)
- Voir la partie sur les modules du TP [tp-systeme][tp-systeme].

---

## `/dev`

- Fichiers spéciaux (_fichiers de périphérique_) représentant les périphériques matériels et les ressources système.
- Facilite la communication avec les périphériques matériels et virtuels.
- Les programmes accèdent aux périphériques en lisant/écrivant dans les fichiers correspondants dans `/dev` :
  - **Périphériques de Caractères** : claviers, souris, terminaux
  - **Périphériques de Blocs** : disques durs, partitions

---

### Nomenclature

- Périphériques numérotés et nommés conventionnellement :
  - Disques IDE : `/dev/hda`, `/dev/hdb`, ...
  - SCSI et récents : `/dev/sda`, `/dev/sdb`, ...
  - `/dev/hda`, `/dev/hdb` : 1er disque dur, 2e disque dur.
  - `/dev/sdb1`, `/dev/hda3` : 1e partition du 2e disque, 3e partition du 1er disque.

---

## Démarrage du système

---

### `BIOS` (Basic Input/Output System) vs `UEFI` (Unified Extensible Firmware Interface)

Différents types de _firmwares_ (dans mémoire de la carte mère).

---

#### BIOS (ancien)

1. `POST` (Power-on Self Test)
2. Le BIOS charge les composants principaux : clavier, disques, écran, ...
3. Le BIOS charge le `bootloader` (first stage) depuis le `Master Boot Record (MBR)` (partitionnement `DOS`)
4. Le `bootloader` charge le reste du programme (second stage)
5. Le `bootloader` charge le noyau (`kernel`)

---

#### UEFI (récent)

1. `POST` (Power-on Self Test)
2. L'UEFI charge les composants principaux : clavier, disques, écran, ...
3. L'UEFI charge applications `EFI` (`bootloaders`, programmes de sélection d'OS, outils de diagnostic) depuis une partition `ESP` (EFI System Partition) dédiée (format `FAT12`, `FAT16`, `FAT32` ou `ISO-9660`).
  - UEFI comprend le partitionnement `GPT` (GUID Partition Table) (et `MBR` mais découragé)
4. Le `bootloader` charge le noyau (`kernel`)

---

#### Secure Boot

`UEFI` supporte le `Secure Boot` pour charger uniquement des applications `EFI` autorisées par le constructeur.

---

#### GRUB

- Grand Unified Bootloader (`GRUB`) est (de loin) le bootloader principal pour un PC Linux.
- Un bootloader charge le noyau en lui fournissant des paramètres : _init_, _runlevel_, partition _root_, ...
- Le noyau prend la main
- `/proc/cmdline` : paramètres fournis au noyau
- Voir le TP dédié [tp-grub][tp-grub].

---

#### Démarrage

- Beaucoup de possibilités différentes : scripts, ...
- En principe :
  - `initramfs` : partition `root` temporaire en RAM
  - Montage des partitions décrites dans `/etc/fstab`
  - Démarrage du programme `init`
  - Démontage de l'`initramfs`

---

### Init

- Différents programmes `init` : `/bin/bash`, script dédié, ...
  + Presque toujours `SysV`, `systemd` (très majoritaire) ou `upstart`
  + D'autres existent : `OpenRC`, ...
- Une des différences majeures entre distributions !

---

#### SysV

- Service init historique et très majoritaire avant `systemd`
- Démarre des daemons par `runlevel`

---

#### systemd

- Manager de services modernes (2010) : parallélisme, démarrage par dépendances, ...
- Compatible `SysV` et `runlevels`
- Ultra majoritaire dans les serveurs
- Commandes dédiées : `systemctl`, `journalctl`
- Voir le TP dédié [tp-systemd][tp-systemd].

---

#### Upstart (obsolète)

- Autre modernisation de `SysV` pour accélérer le démarrage (parallélisme).
- Popularisé par `Ubuntu` avant son abandon pour `systemd`.
- Voir le cours "101.3 Lesson 1" p.43 de la certification LPIC-1 pour plus de détails, `Upstart` ne sera pas abordé en TP.

---

### Changement de runlevels, arrêt et redémarrage.

---

#### Runlevel (SysV init)

- Runlevel **0** : System shutdown.
- Runlevel **1**, **s** ou **single** : Single user mode, without network and other non-essential capabilities (maintenance mode).
- Runlevel (2), **3** or (4) : Multi-user mode (console).
- Runlevel **5** : Multi-user mode (graphique mais sinon idem 3).
- Runlevel **6** : System restart.
- Seuls **0, 1 et 6** sont communs à toute distribution.

- Voir le TP dédié [tp-sysv][tp-sysv].

---

#### init

Le programme `/sbin/init` gère le `runlevel` :

- depuis les paramètres passés au noyau ;
- ou depuis le fichier `/etc/inittab`.

- `/etc/init.d` contient les scripts qui gèrent les runlevels
- `/etc/rc0.d`, `/etc/rc1.d`, … contiennent les scripts des runlevels correspondants

Voir le cours de la certification LPIC-1 pour le format du fichier `/etc/inittab`, 101.3 Lesson 1 p.37

---

### Résumé du boot - traditionnel vs moderne

- POST -> BIOS -> MBR (DOS) -> Grub -> Kernel -> Init -> Runlevel (SysV)
- POST -> UEFI -> EFI (GPT) -> direct ou Grub -> Kernel -> Init -> Runlevel (systemd) 


---

## Commandes utiles pour le matériel

- `lshw`, `lsusb`, `lspci`, `lscpu`, `lsblk`, `lsscsi` : informations générales hardware, usb, PCI port, CPU, block devices (partitions disques durs), disques physiques
- `lsmod` : liste les modules noyau chargés
- ` dmidecode -t …` : informations sur le matériel physique (nombre de slots RAM, …)
- `inxi`, `neofetch`, `fastfetch` (non-POSIX) : résumés d'informations sur le système

<!-- Annexe : liste des TPs -->
[tp-systeme]: /linux/tp-systeme
[tp-grub]: /linux/tp-grub
[tp-sysv]: /linux/tp-sysv
[tp-systemd]: /linux/tp-systemd

---

