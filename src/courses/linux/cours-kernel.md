---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Le noyau Linux
layout: '@layouts/CoursePartLayout.astro'
---

## Composants du noyau


### Structure du noyau

- **modulaire** : noyau monolithique mais permet le chargement à chaud de modules
- **Sources du noyau** : `/usr/src/linux/`
- **Documentation** : `/usr/src/linux/Documentation/`
- **Compression** : le noyau est généralement compressé : _gzip_, _bzip2_, _xz_ (différences minimes taille vs performance)
  - **zImage** : image compressée du noyau. Convient aux systèmes embarqués avec moins de mémoire.
  - **bzImage** : (Big zImage) version compressée du noyau pouvant dépasser la limite de 640 Ko de mémoire.

Exemple :

```sh
ls -lh /boot/vmlinuz-*
````

### Versions

- Les versions stables suivent la forme : `6.x.y`
- Versions LTS (long term support) maintenues longtemps.
- Correctifs disponibles sur <https://www.kernel.org> mais en général **privilégier le packager de la distribution**.

---

## Compilation du noyau

### Arborescence des sources

- Lien symbolique vers les sources du noyau : `/usr/src/linux/`
- Fichier de configuration principal : `/usr/src/linux/.config`

### Étapes de compilation

1. **Récupération des sources**

```sh
cd /usr/src/
wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.19.299.tar.xz
tar -xf linux-4.19.299.tar.xz
cd linux-4.19.299
```

2. **Configuration du noyau**

- `make menuconfig` : interface en ncurses
- `make xconfig`, `make gconfig` : interfaces graphiques
- `make oldconfig` : met à jour l’ancienne config
- `make defconfig` : configuration par défaut

:::link
Pour plus d'information, voir l'excellent guide de la distribution Gentoo : <https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide>.
Voir aussi le guide Arch Linux : <https://wiki.archlinux.org/title/Kernel/Traditional_compilation>.
:::

3. **Compilation**

```sh
make -j$(nproc)
make modules
```

:::tip
L'option `-j` permet de parralléliser le build (c'est une option héritée de `make`) :

- Sur anciens systèmes, on recommande `$(nproc -1)`` pour avoir 1 CPU libre (arrêt du build, tâches système, …)
- Sur serveurs, normalement `$(nproc)` est fiable (les _scheduler_ récents allouent des temps d'exécution aux tâches système, légère perte de réactivité).
- Sur système peu risqué ou VM, on peut monter jusqu'à : `$(nproc * 2)` (utiliser le maximum de temps CPU pour le build, quitte à _freezer_ le système).
:::

:::tip
Pour réduire le temps, on pourra utiliser un système de fichiers en mémoire RAM (`tmpfs`) plutôt que d'écrire les fichiers compilés sur disque.
:::

4. **Installation**

```sh
make modules_install
make install
```

Cela installe :

- Le noyau dans `/boot/`
- Les modules dans `/lib/modules/<version>/`

5. **Générer l’image initramfs**

* Pour Debian/Ubuntu :

```sh
mkinitramfs -o /boot/initrd.img-4.19.299 4.19.299
```

* Pour RedHat :

```sh
mkinitrd /boot/initrd-4.19.299.img 4.19.299
```

* Avec dracut :

```bash
dracut --force /boot/initramfs-4.19.299.img 4.19.299
```

6. **Mettre à jour le bootloader (GRUB)**

```sh
update-grub       # Debian
grub2-mkconfig -o /boot/grub2/grub.cfg   # RedHat
```

### Utilisation de DKMS

**DKMS** permet de recompiler automatiquement les modules lors des changements de noyau.

* Exemple :

```sh
dkms add -m mymodule -v 1.0
dkms build -m mymodule -v 1.0
dkms install -m mymodule -v 1.0
```

### Boot sur disque NVMe

- **NVMe (Non-Volatile Memory Express)** : protocole conçu pour exploiter la vitesse des SSD via le bus PCIe.
- Apparaît généralement sous `/dev/nvme0n1`, `/dev/nvme1n1`, …
- L'image initramfs doit inclure les **pilotes NVMe** (`nvme`, `nvme_core`, `nvme_common`).
- Sinon le noyau ne pourra pas monter `/` et échouera au boot (erreur `unable to mount root fs`).

Vérification dans `initramfs` :

```sh
lsinitramfs /boot/initrd.img-$(uname -r) | grep nvme
```

