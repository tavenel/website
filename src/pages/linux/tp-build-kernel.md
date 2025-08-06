---
title: TP Compilation, Personnalisation et Installation d'un Noyau Linux
date: 2025 / 2026
---

### 🎯 Objectif

- Récupérer les sources du noyau Linux.
- Configurer le noyau via des interfaces texte.
- Compiler un noyau personnalisé.
- Créer une image initramfs.
- Installer et rendre le noyau bootable via le gestionnaire de démarrage.
- Gérer les modules avec DKMS.
- Comprendre la structure d'un noyau compilé.

### 📝 Énoncé

Vous êtes administrateur système sur un serveur Debian-like (Debian, Ubuntu). Votre mission est de **compiler et installer un noyau Linux personnalisé**, en suivant les bonnes pratiques.

Le noyau source choisi sera par exemple la version **LTS** (par exemple 6.12). Vous devez également configurer un module externe pour qu'il se reconstruise automatiquement avec DKMS.

:::link
Pour apprendre à compiler un noyaux Linux sous Debian, suivre la [documentation officielle](https://kernel-team.pages.debian.net/kernel-handbook/ch-common-tasks.html#s-common-official).
:::

### Préparation de l'environnement

1. Ajouter un lien vers le code source des paquets (`deb-src`) dans le gestionnaire de paquets (`apt`) :

   ```
	 # /etc/apt/sources.list


   deb http://archive.ubuntu.com/ubuntu plucky main restricted universe multiverse
   deb-src http://archive.ubuntu.com/ubuntu plucky main restricted universe multiverse
	 ```

2. Installer les paquets nécessaires à la compilation d'un noyau :

   ```sh
   apt-get install build-essential libncurses-dev
   apt-get build-dep linux
   ```

3. Créer un répertoire de travail et se positionner dans `/usr/src` :

   ```sh
   cd /usr/src
   ```

4. Télécharger et décompresser les sources du noyau :

   - depuis kernel.org
	 - ou en utilisant les packages Debian, par exemple pour le noyau courant : `apt install linux-source` ou `apt-get source linux`

### Configuration du noyau

1. Copier le fichier `.config` actuel depuis `/boot` (ex: `config-$(uname -r)`) vers le répertoire source ou utilisez `make localmodconfig` (ou pour repartir d'une configuration standard : `make defconfig`)

2. Pour modifier la configuration du noyau, on utilise généralement l'interface texte depuis `make menuconfig` (il existe également une interface _ncurses_ : `make nconfig`). Effectuer les changements :

   - Activer le support de Btrfs en dur (`[*]`).
   - Désactiver le support des systèmes de fichiers FAT et NTFS.

3. Désactiver la signature : sur les systèmes dérivés de Debian, les modules noyau sont signés par un certificat qui est n'est pas présent par défaut sur le système. Pour cette 1e compilation, nous allons désactiver cette signature :

   ```sh
   ./scripts/config --file .config --disable MODULE_SIG
	 ```

3. Sauvegarder et quitter.

### Compilation

```sh
# Compilation du noyau
make -j$(nproc)
# ou
make modules # pour builder uniquement les modules

# Installation des modules dans /lib/modules/…
make modules_install

# Installation du noyau dans /boot, génération de l'initram et mise à jour du bootloader
make install
```

:::tip
Voir [le cours pour la valeur à fournir à `-j`](/linux/lpic-2/cours#%C3%A9tapes-de-compilation)
:::

### Image initramfs et boot

1. Si ce n'est pas déjà fait, générer une image initramfs avec `mkinitramfs` ou `dracut`.
2. Vérifier que la nouvelle entrée de noyau a bien été ajoutée à GRUB.
3. Redémarrer la machine sur le nouveau noyau.
4. Vérifier avec `uname -r` que le noyau actif est le bon.

### Intégration de module DKMS

1. Créer un module simple en C (par exemple un module hello world).
2. Créer la structure DKMS nécessaire (`/usr/src/<modulename>-<version>` avec fichier `dkms.conf`).
3. Enregistrer le module auprès de DKMS.
4. Compiler et installer le module avec DKMS.
5. Vérifier que le module est bien compilé pour le nouveau noyau.

## 🧩 Exemple du module DKMS

```sh
/usr/src/hello-dkms-1.0/
├── hello.c
├── Makefile
└── dkms.conf
```

```c
// hello.c

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("TP LPIC-2");
MODULE_DESCRIPTION("Module DKMS Hello World");
MODULE_VERSION("1.0");

static int __init hello_init(void) {
    printk(KERN_INFO "Hello DKMS: module loaded.\n");
    return 0;
}

static void __exit hello_exit(void) {
    printk(KERN_INFO "Hello DKMS: module unloaded.\n");
}

module_init(hello_init);
module_exit(hello_exit);
```

```make
# Makefile

obj-m := hello.o
KVERSION := $(shell uname -r)

all:
	        $(MAKE) -C /lib/modules/$(KVERSION)/build M=$(PWD) modules

clean:
	        $(MAKE) -C /lib/modules/$(KVERSION)/build M=$(PWD) clean
```

:::tip
Le `Makefile` utilise la variable d'environnement `KERNEL_VERSION` qui sera injectée automatiquement par DKMS.
:::

```sh
# dkms.conf

PACKAGE_NAME="hello"
PACKAGE_VERSION="0.1"
CLEAN="make clean"
MAKE[0]="make all KVERSION=$kernelver"
BUILT_MODULE_NAME[0]="hello"
DEST_MODULE_LOCATION[0]="/updates"
AUTOINSTALL="yes"
```

### 🚀 Commandes

Une fois les fichiers placés dans `/usr/src/hello-dkms-1.0`, en tant que root :

```sh
# 1. Enregistrement du module
dkms add -m hello-dkms -v 1.0

# 2. Compilation pour le noyau actuel
dkms build -m hello-dkms -v 1.0

# 3. Installation du module compilé
dkms install -m hello-dkms -v 1.0
```

### ✅ Vérification

```sh
# Charger le module
modprobe hello

# Vérifier les logs du noyau
dmesg | grep "Hello DKMS"

# Lister les modules DKMS
dkms status

# Décharger le module
modprobe -r hello
```

:::link
Ce module DKMS est inspiré de : <https://wiki.ubuntu.com/Kernel/Dev/DKMSPackaging>
:::
