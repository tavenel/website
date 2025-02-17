---
title: Installation de Linux Debian Serveur dans une machine virtuelle
---

# Partie I : Création d’une machine virtuelle Linux

## Installation de VirtualBox

- Télécharger VirtualBox depuis le site officiel : <https://www.virtualbox.org/>
- Installer VirtualBox depuis l’installeur téléchargé

## Installation du pack d’extension VirtualBox pour utiliser des fonctionnalités avancées

- Télécharger le pack d’extension depuis le site de Virtual Box : <https://download.virtualbox.org/virtualbox/7.0.6/Oracle_VM_VirtualBox_Extension_Pack-7.0.6a-155176.vbox-extpack>
- Ouvrir `VirtualBox` et ajouter le pack d’extension : Dans le menu Fichier, sélectionner **Paramètres.** Dans la fenêtre qui s’affiche, ouvrir la catégorie **Extensions**, cliquer sur le bouton “+” et ajouter l’extension téléchargée

## Récupération d’une image préinstallée d’un système Linux

- Télécharger une image préinstallée du **serveur** debian (version **64 bits**) : <https://sourceforge.net/projects/osboxes/files/v/vb/14-D-b/11/Server/64bit.7z/download>
- Extraire l’image téléchargée (on pourra utiliser l’outil 7zip : <https://www.7-zip.org/download.html> )

## Créer une machine virtuelle à l’aide de l’image de disque virtuel (VDI) extrait à l’étape précédente

- Dans l’interface principale de VirtualBox, cliquer sur l’icône « _Nouvelle_ »
- 1er écran :
  - Dans le champ _Nom_: choisir le nom que vous souhaitez pour votre machine virtuelle
  - Dans le champ _Type_, choisir "_Linux_" et dans le champ version: « _Debian (64 bits)_ »
  - Cliquer sur Suivant

![Création d'une machine virtuelle](@assets/virtualbox/creer-vm.png)

- 2e écran : Mémoire virtuelle
  - Choisir de réserver `1024Mo` pour la mémoire
  - Cliquer sur Suivant
- 3e écran : Disque dur
  - Sélectionner « _Utiliser un fichier de disque dur virtuel existant_ »
  - Cliquer sur l’icône du dossier pour importer un nouveau disque dans VirtualBox
  - Cliquer sur le bouton _Ajouter_ et choisir l’image de disque dur Debian qui a été extraite à l’étape 3 (fichier de type VDI)
  - Sélectionner le disque dur ajouté, cliquer sur _Choisir_

![Sélection du disque dur](@assets/virtualbox/select-hdd.png)

- Cliquer sur Créer pour créer la machine virtuelle

## Configurer un pont (bridge) entre l’interface réseau de votre ordinateur personnel et la machine virtuelle Linux

- Sélectionner la machine virtuelle créée et cliquer sur l’icône « _Configuration_ »
- Ouvrir l’onglet « _Réseau_ »
- Changer le _Mode d’accès réseau_ en « _Accès par pont_ » et sélectionner l’interface utilisée dans Windows pour se connecter à Internet.

![Configuration du bridge](@assets/virtualbox/bridge.png)

- Valider la configuration en cliquant sur _Ok_.

## Démarrer la machine virtuelle

- Lancer la machine virtuelle (sélectionner la machine virtuelle et cliquer sur le bouton _Démarrer_ de l’interface principale de VirtualBox)
- Nous allons nous connecter en tant que super-utilisateur sur le système (utilisateur `root`) pour disposer des droits d’administration
  - Attendre le lancement du système jusqu’à l’écran demandant les identifiants de connexion

![](@assets/virtualbox/login.png)

- - Entrer le nom de l’utilisateur racine : `root` et valider (touche <kbd>Entrée</kbd>)
    - Entrer le mot de passe : `osboxes.org` et valider (touche <kbd>Entrée</kbd>)

:::warn
### ATTENTION

1. Sur un interpréteur de commandes Linux, rien n’apparaît sur le terminal lorsque vous tapez votre mot de passe. C’est normal ! Cela permet de ne pas afficher d'information sur les mots de passe en cas de copie. Entrer le mot de passe sans changement à l’écran puis valider : vous devriez ensuite voir un message de bienvenue si vous êtes correctement connecté au système. En cas d’erreur, le mot de passe sera demandé de nouveau.

2. Le système est configuré par défaut pour un clavier en langue anglaise (_qwerty_) : sur un clavier en langue française (_azerty_), le mot de passe à taper correspond à : `osboxes:org`
:::

# Partie II : Configurer la machine virtuelle

## Configuration du clavier en français

Nous allons commencer par reconfigurer le clavier pour utiliser un clavier _AZERTY_.

- Depuis la machine virtuelle, une fois connecté, taper la commande suivante dans le terminal pour reconfigurer le clavier :
  ```sh
  dpkg-reconfigure keyboard-configuration
  ```
- Garder le clavier standard (_Generic 105-key PC (intl.)_) : appuyer sur <kbd>Entrée</kbd>
- Dans l’écran suivant, sélectionner "_Other_" puis sélectionner le clavier "_French_", puis de nouveau "_French_". Valider.

![](@assets/virtualbox/french.png)

- Dans l’écran suivant, sélectionner "_The default for the keyboard layout_" puis "_No compose key_"
    - Valider, vérifier que la configuration est terminée et que le système est revenu en mode ligne de commande (curseur clignotant en bas de l’écran).

![](@assets/virtualbox/no-compose.png)

Pour que les changements soient pris en compte, nous allons redémarrer le système.

- Taper la commande suivante :

```sh
reboot
```

Vous pouvez maintenant vous connecter de nouveau au système, cette fois avec un clavier _azerty_ (le mot de passe à taper cette fois est donc bien `osboxes.org` )

## Configuration de l’interface réseau dans la machine virtuelle

- Depuis la machine virtuelle, une fois connecté comme utilisateur root, taper la commande suivante dans le terminal pour trouver l'interface réseau du système (valider par la touche <kbd>Entrée</kbd>):

```sh
ip link
```

Cette commande va afficher dans la console les deux interfaces configurées sur le système : une interface identifiée "_loopback_" (interface interne), et une seconde interface réseau (qui correspond au _bridge_ que nous avons créé, par exemple, `enp0s3`)

![](@assets/virtualbox/ip-link.png)

- Une fois le nom de l’interface récupéré, nous allons modifier le fichier `/etc/réseau/interfaces` avec l’éditeur de texte nano pour y inscrire la configuration de cette interface. Pour cela, exécuter la commande :
  ```sh
  nano /etc/network/interfaces
  ```
- Ajoutez les lignes suivantes au fichier **(remplacez `enp0s3` par le nom de votre interface réseau)** :
  ```
  auto enp0s3
  iface enp0s3 inet dhcp
  ```
- Taper <kbd>Ctrl</kbd> + <kbd>X</kbd> pour quitter l'éditeur
  - L'éditeur demande si l’on veut enregistrer les changements avant de quitter : taper <kbd>Y</kbd> pour _Yes_
  - L'éditeur demande ensuite quel nom de fichier utiliser : garder le nom du fichier (`/etc/network/interfaces`) et appuyer sur <kbd>Entrée</kbd>

![](@assets/virtualbox/interfaces.png)

- Nous allons maintenant redémarrer le service réseau pour prendre en compte ces changements :
  - Assurez-vous de bien avoir quitté l’éditeur nano et d’être retourné dans l’invité de commandes (curseur clignotant en bas de l’écran)
  - Pour redémarrer le service réseau, entrer la commande suivante :
  ```sh
  systemctl restart networking
  ```
- Vérifiez l’état du service réseau :
  ```sh
  systemctl status networking
  ```

![](@assets/virtualbox/status-networking.png)

- Vérifiez que vous avez maintenant une adresse IP dans la machine virtuelle et que vous pouvez atteindre le réseau :
  ```sh
  ip addr show
  ```
- La commande doit afficher une adresse IP, similaire à : `192.168.0.1` (même format `w.x.y.z` mais l’adresse peut être différente)
    - Testons ensuite le réseau en essayant d’atteindre `www.google.fr`. La commande `ping` permet d’envoyer des paquets en permanence vers un système distant. Taper la commande suivante, attendre que quelques paquets soient envoyés puis mettre fin à la commande en appuyant sur <kbd>CTRL</kbd> + <kbd>C</kbd> (il s’agit du raccourci standard pour arrêter une commande sous Linux) :

```sh
ping www.google.fr
```

![](@assets/virtualbox/ping.png)

- Vérifier dans le retour affiché à l’écran que la commande ping ne retourne pas d’erreur et que tous les paquets ont bien été transmis

Remarque : si vous ne pouvez pas réaliser de ping sur un site web externe, c’est peut-être parce qu'_IPv6_ est activé (VirtualBox ne gère pas bien IPv6 sur les interfaces de type `bridge`).

Pour corriger ce problème, désactiver IPv6 en ajoutant dans le fichier `/etc/sysctl.conf` les lignes suivantes :

```ini
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.all.autoconf = 0
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.default.autoconf = 0
```

Appliquer ensuite les modifications :

```sh
sysctl -p
```

puis redémarrer le service réseau :

```sh
systemctl restart networking
```

## Mise à jour du système d’exploitation de la machine virtuelle

- L'image préinstallée que nous avons téléchargée est configurée pour utiliser le cdrom d’installation. Nous allons la modifier pour installer des programmes depuis le réseau :
  - Modifier le fichier `/etc/apt/sources.list`

```sh
nano /etc/apt/sources.list
```

- et remplacer la ligne :

```
deb cdrom:[Debian GNU ........ ] / buster contrib main
```

- Par la ligne suivante :

```
deb http://deb.debian.org/debian/ buster contrib main
```

- Sauver les changements et quitter l'éditeur `nano` (<kbd>Ctrl</kbd> + <kbd>X</kbd>, <kbd>Y</kbd> pour les modifications et <kbd>Entrée</kbd> pour garder le même nom de fichier).

![](@assets/virtualbox/apt-sources.png)

- Une fois le fichier modifié, nous allons mettre à niveau le système :

```sh
apt-get update && apt-get upgrade
```

A la question :

```
Do you want to continue ? [Y/n]
```

Taper <kbd>Y</kbd> et appuyer sur <kbd>Entrée</kbd>

## Installation du paquet sudo

Le programme `sudo` permet à un utilisateur d’utiliser des commandes d’administration.

- Installez le paquet `sudo` (c’est-à-dire le programme `sudo`, assemblé pour notre système d'exploitation). L'installation d'un programme est très simple sur Linux car elle utilise généralement le gestionnaire de paquets du système. Sur une distribution Debian / Ubuntu, on utilise `apt` :

```sh
apt install sudo
```

## Création d’un compte utilisateur

- Ajouter un nouvel utilisateur (remplacer `MY_USER` par votre utilisateur, attention ce nom doit être en minuscule et sans espace) :

```sh
adduser MY_USER
```

- Laissez ce nouvel utilisateur exécuter les commandes administratives. Pour cela, nous allons ajouter notre utilisateur au groupe d’utilisateurs `sudo`. Ce groupe a automatiquement le droit d’exécuter la commande `sudo` que nous venons d’installer, afin de réaliser des commandes d’administration :

```sh
usermod -a -G sudo MY_USER  
```

## Utilisez votre nouvel utilisateur

- Redémarrer la machine virtuelle depuis la ligne de commandes :

```sh
reboot
```

- Connectez-vous avec votre nouveau compte utilisateur

## Créez une sauvegarde de votre machine

- Dans le menu _Machine_, sélectionner _Prendre un instantané_. Cela permettra de revenir à cette sauvegarde en cas de mauvaise manipulation sur le système.


