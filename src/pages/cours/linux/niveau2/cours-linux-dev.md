---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Linux
tags:
- linux
---

# Linux orienté développeurs

---

# Objectifs

- Avoir des connaissances de base des systèmes Linux : installation d'une distribution, gestion des packages, système de fichiers, environnement graphique
- Savoir utiliser les commandes courantes Unix et GNU : gestion des fichiers, traitement de flux de texte, gestion des processus
- Bien utiliser la ligne de commande Linux
- Écrire des scripts Bash

---

# Ressources utiles

- [Livre Bash beginner's guide](https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/)
- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)

---

# Conventions de notation

- Les commandes et noms de fichiers apparaissent dans le texte avec `cette syntaxe`.
- Les descriptions de commandes suivent le formalisme des _man pages_ :
  - Les symboles `<>` indiquent un argument obligatoire.
  - Les symboles `[]` indiquent un argument optionnel.  

---

# Interfaces et bureaux utilisateur

---

## Installation et configuration de X11

---

### X11

- Système graphique historique de Linux
- Modèle client / serveur
- Session X courante dans variable `DISPLAY` (en principe: `:0`)
- `/etc/X11/xorg.conf`
- `~/.xsession-errors`

---

![width:700px](https://learning.lpi.org/en/learning-materials/102-500/106/106.1/106.1_01/images/image_01.png)

<!-- _class: legende -->
Architecture de X11 (crédits: learning.lpi.org)

---

### Wayland

- Successeur de `X11` : adopté par défaut sur `Ubuntu`, `Fedora`, …
- Session courante : variable `WAYLAND_DISPLAY` : (`wayland-0`, …)

---

## Bureaux graphiques

---

### Desktop Environment

- Gestionnaire de fenêtres au-dessus du serveur graphique
- sur-couche à `X11` ou `Wayland`
- [Exemples](https://linux.goffinet.org/administration/introduction-a-linux/environnements-de-bureau/)

---

### Gnome : le bureau intégré

![](https://learning.lpi.org/en/learning-materials/102-500/106/106.2/106.2_01/images/gnome-debian-10.1.0.png)

---

### KDE : le bureau configurable

![](https://learning.lpi.org/en/learning-materials/102-500/106/106.2/106.2_01/images/kde-opensuse-15.1.png)

---

### XFCE : le bureau léger

![](https://learning.lpi.org/en/learning-materials/102-500/106/106.2/106.2_01/images/xfce-manjaro-18.1.0.png)

---

### Interopérabilité : normes freedesktop.org

- Variables à utiliser dans les applications (valeurs par défaut ci-dessous)
- `XDG_CURRENT_DESKTOP='Wayland'`
- `XDG_CONFIG_HOME=$HOME/.config`
- `XDG_CACHE_HOME=$HOME/.cache`
- `XDG_DATA_HOME=$HOME/.local/share`
- `XDG_RUNTIME_DIR=/run/user/$UID`

---

### VNC et RDP

- Protocoles de connexion à distance pour sessions graphiques

---

## Accessibilité

---

Les bureaux graphiques disposent de nombreux outils d'accessibilité :

- Thèmes du bureau à fort contraste ou grandes polices.
- Lecteur d'écran.
- Lecteur braille.
- Loupe d'écran.
- Clavier virtuel.
- Touches Difficiles/Répétition.
- Touches lentes/rebond/inverser.
- Émulation de la souris au clavier.
- Gestuelles.
- Reconnaissance vocale.

---

# Linux en tant que système virtuel hébergé

---

## Technologies de Virtualisation : Hyperviseurs

- Hyperviseur de Type 1 : Exécuté directement sur le matériel, ex. `Xen`, `KVM`
- Hyperviseur de Type 2 : Exécuté au-dessus d'un système d'exploitation, ex. `KVM`, `Oracle VirtualBox`.
- Conteneurs : Isole des ressources grâce aux `cgroups`, ex. `Docker`, `LXC`, ...

---

## Architecture d'une machine virtuelle (fully-virtualized)

```plantuml
@startditaa

+--------------+--------------+
| cGRE VM A    | cGRE VM B    |
| +----------+ | +----------+ |
| |   App1   | | |   App2   | |
| +----------+ | +----------+ |
| | bin/libs | | | bin/libs | |
| +----------+ | +----------+ |
| | cYEL     | | | cYEL     | |
| | Guest OS | | | Guest OS | |
| +----------+ | +----------+ |
+--------------+--------------+
| cRED    Hyperviseur         |
+-----------------------------+
|           OS hôte           |
+-----------------------------+
| cBLK   Infrastructure       |
+-----------------------------+

= Architecture de machine virtuelle : chaque VM virtualise un OS invité complet, ses librairies et ses applications. Les VMs tournent sur un hyperviseur, au-dessus d'un OS hôte

@endditaa
```

---

## Architecture d'un conteneur

```plantuml
@startditaa

+--------------+--------------+
| cPNK         | cPNK         |
| Conteneur A  | Conteneur B  |
| +----------+ | +----------+ |
| |   App1   | | |   App2   | |
| +----------+ | +----------+ |
| | bin/libs | | | bin/libs | |
| +----------+ | +----------+ |
+--------------+--------------+
| cBLU  OS hôte + Docker      |
+-----------------------------+
| cBLK   Infrastructure       |
+-----------------------------+

= Architecture de conteneur : chaque conteneur isole uniquement ses librairies et son application. Les conteneurs tournent sur un OS hôte commun tournant un engine Docker

@endditaa
```

---

## Principaux types de disques virtuels

- `RAW` : la taille totale du disque virtuel est réquisitionnée à la création
- `COW` : quota de taille maximale, espace réquisitionné à l'usage

---

## UUID

- Besoin d'identifiants uniques de machines virtuelles : _d-bus machine id_
- `dbus-uuidgen --ensure`, `dbus-uuidgen --get`
- stocké dans `/var/lib/dbus/machine-id` (symlink `/etc/machine-id`)

---

## Cloud-init

- Génère des machines virtuelles ou conteneurs dans un environnement de Cloud
- Fichier de configuration `YAML`

---

# Utilisation des gestionnaires de paquetage

---

## Gestionnaires de Paquets

Outils essentiels pour gérer l'installation, la mise à jour et la suppression de logiciels depuis une plateforme centrale vérifiée.

---

## Avantages

- Installation facile : Un simple commande installe le logiciel et ses dépendances.
- Mises à jour centralisées : Facilité de maintenir les logiciels à jour.
- Gestion des dépendances : Installation automatique des composants requis.
- Désinstallation propre : Suppression sans laisser de résidus.
- Sécurité :
  - Les paquets proviennent de sources fiables et vérifiées.
  - Mises à jour régulières pour corriger les vulnérabilités.

---

## Principaux gestionnaires de paquets

- APT (Advanced Package Tool) : Utilisé par Debian et dérivés (Ubuntu).
- RPM (Red Hat Package Manager) : Utilisé par Red Hat, Fedora, CentOS.
- Voir le TP dédié [tp-rpm-apt][tp-rpm-apt].

---

# Gestion des bibliothèques partagées

---

## Bibliothèque partagée

- `Shared Objects`
- _Ensemble de fonctions que les programmes peuvent réutiliser pour implémenter leurs fonctionnalités_.
- Liées au programme exécutable de manière :
  - **statique** : l'exécutable final contient les fonctions de la bibliothèque dans ses propres fichiers (`NOM_LIBRAIRIE.a` : `libpthread.a`)
  - **dynamique** (ou **partagée**) : bibliothèque chargée en mémoire RAM quand le programme aura besoin d'exécuter les fonctions qu'elle contient. (`NOM_LIBRAIRIE.so.VERSION` : `glibc.so.6`)
    + Windows : `DLL`

---

## Répertoires standards

- `/lib`
- `/lib32`
- `/lib64`
- `/usr/lib`
- `/usr/local/lib`

---

## Répertoires additionnels et cache

- `/etc/ld.so.conf` (ou `/etc/ld.so.conf.d/`) : indique les autres librairies à utiliser, puis...
- `ldconfig` : crée les liens symboliques vers les librairies et met à jour le cache...
- `/etc/ld.so.cache` : fichier de cache
- `LD_LIBRARY_PATH` : variable d'environnement supplémentaire pour scanner des répertoires de librairies (similaire à `$PATH`)

---

## Afficher les dépendances

- `ldd <executable>` : affiche les librairies dépendantes
- `ldd -u <executable>` : affiche les librairies dépendantes _unused_

---

- Voir aussi la [wikiversité][wiki-shared-lib]
- Voir le TP dédié [tp-shared-lib][tp-shared-lib].

---

# Partitionnement

---

## Partitions standard

- Bonne pratique : **séparer le système en plusieurs partitions**
- `/` : partition `root`, obligatoire, système principal
- `/boot` : contient les données de boot : `kernel`, `bootloader`, ...
- `/boot/efi` : montage de la partition `ESP`.
- `/home` : fichiers personnels et configurations des utilisateurs
- `/var` : données variables (`/var/logs`, `/var/tmp`, `/var/cache`) ou fichiers changeant pendant l'exécution (`/var/www/html`, `/var/lib/mysql`, `/var/lib/docker`)
- `swap` pour augmenter la RAM en utilisant un disque (non monté)

### Démo

---

# Travail en ligne de commande

- Échapper les caractères spéciaux avec `"` et `'`
- Wildcards `*`, `?`, `[a-zA-Z]`, `{toto,titi}`
- Voir la page (FR) [wikiversité][wiki-filtres] pour un rappel des filtres.
- Voir le TP dédié [tp-ligne-commande][tp-ligne-commande].

---

# Création, contrôle et interruption des processus

---

## Modification des priorités des processus

- priorité demandée par l'utilisateur : `nice` (-20 à 20)
  - champ `NI` de `ps`
- transformé par le scheduler en priorité effective (0 à 100)
  - champ `PRI` de `ps`

---

## Commandes utiles

- `ps` (`ps aux`), `top`, `pgrep`, `watch`
- `kill`, `pkill`, `killall`
- `nice`, `renice`
- fichiers `/proc/<PID>`

### Démo

---

## Jobs

- Processus démarré interactivement dont l'exécution continue en arrière-plan
- `jobs`, `fg`, `bg`, `&`, `nohup`

### Démo

---

Voir le TP dédié [tp-process][tp-process].

---

## Multiplexers de terminal

- `tmux` (le plus utilisé)
- `screen`  
- d'autres existent (bien moins utilisés)
- gèrent des _sessions_ de terminal en mode client/serveur :
  - écran découpé pour tourner des commandes en parallèle
  - déconnexion et reconnexion sans perdre l'exécution des commandes
  - très utiles pour gérer un serveur

---

# Gestion élémentaire des fichiers

---

- Voir la page (FR) [wikiversité][wiki-fichiers] pour un rappel sur la gestion des fichiers.

---

## Types de fichiers

- Fichier standard : majorité des fichiers : données, configurations, binaires, ...
- Répertoires : fichier spécial contenant d'autres fichiers
- Autres fichiers spéciaux (par exemple pour les entrées/sorties)

---

## Commandes utiles

- `touch`, `ls`
- `mkdir`, `rmdir`
- `cp`, `mv`, `rm`
- `find`, `file`
- `dd`, `tar`, `cpio`, `gzip`, `gunzip`, `bzip2`, `bunzip2`
- Voir le TP dédié [tp-fichiers][tp-fichiers].

### Démo

---

# Traitement de flux de type texte

Voir le TP dédié [tp-texte][tp-texte].

### Démo

---

# Utilisation des flux, des pipes et des redirections

---

Concepts fondamentaux dans les systèmes Unix/Linux, permettant de gérer efficacement les entrées/sorties des commandes et de manipuler les données dans le terminal.

- Voir aussi la [wikiversité][wiki-redirections].

---

## Les Trois Flux Standard

Les commandes reçoivent et envoient des données via trois flux standard :

- Entrée standard (`stdin`) : Flux de données d'entrée provenant du clavier ou d'un fichier.
- Sortie standard (`stdout`) : Flux de données de sortie affichées à l'écran.
- Erreur standard (`stderr`) : Flux de messages d'erreur affichés à l'écran.

---

## Redirections

Les redirections permettent de gérer les flux standard :

- `>` : Redirige la sortie standard vers un fichier (`commande > fichier`).
- `2>` : Redirige la sortie d'erreur vers un fichier (`commande 2> fichier`).
- `>>` : Ajoute la sortie standard à la fin d'un fichier (`commande >> fichier`).
- `2>>` : Ajoute la sortie d'erreur à la fin d'un fichier (`commande 2>> fichier`).
- `<` : Redirige l'entrée standard depuis un fichier (`commande < fichier`).

### Démo

---

## Pipes

- Permettent de connecter la sortie d'une commande à l'entrée d'une autre :

```
commande1 | commande2
```

---

## Exemples

- `ls | grep keyword` : Recherche un mot clé dans la liste des fichiers.
- `cat fichier.txt | grep pattern` : Recherche un motif dans le contenu d'un fichier. (équivalent `grep pattern fichier.txt`)
- `ps aux | sort -nrk 3,3 | head` : Trie et affiche les processus avec la plus grande utilisation de CPU.
- `commande 2>&1` : Redirige la sortie d'erreur vers la sortie standard.
- Voir le TP dédié [tp-redirections][tp-redirections].

---

# Recherche dans des fichiers texte avec les expressions rationnelles

---

## Quelques caractères spéciaux

- `.` : n'importe quel caractère
- `^` : début de ligne
- `$` : fin de ligne
- `[ati]` : un caractère `a` ou `t` ou `i` 
- `[^ati]` : un caractère **sauf** `a`, `t`, `i`
- `[0-9]`, `[a-z]` : un chiffre entre `0` et `9`, un caractère entre `a` et `z`
- `?`, `*`, `+` : un caractère, 0 ou plusieurs caractères, au moins un caractère
- `\` : caractère d'échappement pour `.^$*[](){}|\` (ex: `\*` : caractère `*`)

---

- Voir la partie sur les expressions régulières du TP sur les flux de texte [tp-texte][tp-texte].
- Voir la [wikiversité][wiki-regex].

---

## Commandes utiles

- `grep`, `egrep`, `fgrep` : recherche avec regex simples, avec regex étendues (idem `grep -E`), sans regex
- `sed` : modifications de flux de texte

### Démo

---

# Édition de fichier simple (vi)

---

## vi

- `vi` : éditeur de texte en mode console
- plusieurs _modes_ : `normal`, `insertion`, `command`
- édition de texte très efficace 
- POSIX
- successeurs : `vim`, `neovim`
- **Pour une introduction à `vi`, utiliser l'excellent tutoriel intégré : taper `vimtutor` dans un terminal.**

### Démo + grep

---

# Gestion des permissions et de la propriété sur les fichiers

---

## Les utilisateurs

- Un fichier appartient à un utilisateur et à un groupe
- trois types d'utilisateurs ayant des droits :
  - `u` (pour `user`) : l'utilisateur auquel appartient le fichier/dossier
  - `g` (pour `group`) : le groupe auquel appartient le fichier/dossier
  - `o` (pour `other`) : les autres utilisateurs

---
 
## Les droits

- `r` (`read`) : lire le fichier/dossier
- `w` (`write`) : modifier le fichier/dossier
- `x` (`execute`) : exécuter le fichier / entrer dans le dossier
- `-` : aucun droit

---

## Affichage des droits

```
$ ls -l
drwxr-xrw- [...]
```

- `d` : type de fichier (dossier)
- `rwx` : droits de l'utilisateur (propriétaire)
- `r-x` : droits du groupe
- `rw-` : droits du reste du monde

---

## Modifier les droits

- `chmod u+x mon_fichier`
- `chmod g-r mon_fichier`
- `chmod o+w mon_fichier`
- `chmod a-x mon_fichier` (all)
- `chmod -R u-x mon_dossier` : récursif
- `chmod 660 mon_fichier` : `660` est l'octal correspondant au masque `rw- rw- ---`

---

| Permission                     | `ls -l` | octal |
|--------------------------------|---------|-------|
| aucun droit                    | `- - -` |   0   |
| exécution seulement            | `- - x` |   1   |
| écriture seulement             | `- w -` |   2   |
| écriture et execution          | `- w x` |   3   |
| lecture seulement              | `r - -` |   4   |
| lecture et exécution           | `r - x` |   5   |
| lecture et écriture            | `r w -` |   6   |
| lecture, écriture et exécution | `r w x` |   7   |

---

## Droits spéciaux

---

### SUID et SGID

- `SUID`, `SGID` (_Set User/Group ID_) : lance la commande avec l'`UID` de l'utilisateur / du groupe
  - Droit `+s` ou 1er bit à 1 (user) ou 2e bit à 1 (group)
  - `chmod u+s /bin/cat`, `chmod 4xxx /bin/cat`
  - `chmod g+s /bin/cat`, `chmod 2xxx /bin/cat`
- `SGID` sur répertoire : les fichiers et sous-répertoires créés dans ce répertoire hériteront du groupe propriétaire du répertoire parent (au lieu du groupe de l'utilisateur créant les fichiers).

---

### Sticky bit

- `Sticky bit` (dossier) : seul le propriétaire d'un fichier contenu dans ce dossier pourra le supprimer ou le renommer (`/tmp`, ...).
  - Droit `+t` ou 3e bit à 1
  - `chmod o+t /home/tom/communs` ou `chmod 1xxx /home/tom/communs`

---

## Lister les groupes

- `getent group` : tous les groupes du système
- `groups tom` : groupes de l'utilisateur `tom`
- `groupmems -g video -l` : utilisateurs du groupe `video`
- En local : fichier `/etc/group`

---

## Permissions par défaut

- `umask`, `umask -S`
- masque des permissions retirées par défaut
- 1 seul masque : fichier standard idem dossier mais droit d'exécution retiré

---

- Voir le TP dédié [tp-fichiers-avance][tp-fichiers-avance].

---

# Création et modification des liens physiques et symboliques sur les fichiers 

---

## inode

- _Index node_ : structure de données qui stocke les attributs d'un fichier
- permissions, propriétaire, bloc disque de stockage, ...

---

## Liens symboliques

- Type spécial de fichier
- _Lien symbolique_ (ou lien faible, _soft link_) : pointe vers le chemin d'un autre fichier (_target_)
  + `ln -s TARGET NOM_DU_LIEN`
  + Si suppression de la target, pointe vers rien
- _Lien réel_ (_hard link_) : 2e référence vers le même fichier
  + toujours 1 seul inode
  + `ln TARGET NOM_DU_LIEN`

---

# Recherche de fichiers et placement des fichiers aux endroits adéquats

---

## find

- Recherche récursive dans un répertoire des **chemins** de fichiers
- critères de recherche nom, type, date, taille utilisateur, ...
- pas de cache

---

## locate

- Interroge une BD des noms de fichiers (cache)
- `updatedb` met à jour le cache

---

## which

- Inverse du `$PATH` : retourne le chemin vers la commande
- `which <commande>` ou `which -a <commande>`

---

## type

- Similaire à `which`
- Ajoute le type de fichier
- `type [-a] [-t] <commande>`

---

## whereis

- Similaire à `which` mais ajoute les _man page_ et le code source
- `whereis [-b|m|s] <commande>` pour limiter la sortie au binaire / man page / source code

---

## Fichiers temporaires (FHS v3)

- `/tmp` : volatile
  + peut être effacé à l'arrêt du programme
  + (normalement) nettoyé au redémarrage
- `/var/tmp` : persistant
  + (normalement) conservé au redémarrage
- `/run` : données runtime (`pid`, ...)
  + précédemment `/var/run`

---

- Voir le TP dédié [tp-fichiers-avance][tp-fichiers-avance].

---

![Les différents répertoires de la Filesystem Hierarchy Standard](@assets/linux/fhs.png)

---

# Shells et scripts Shell

---

## Personnalisation et utilisation de l’environnement du shell

---

### Le shell

- Programme qui exécute les commandes dans le terminal
- `sh` : Bourn Shell, historique, standard, "portable"
- `bash` : Bourn Again Shell Linux, le plus utilisé
- Interactif / Non-interactif
- Shell de Login
- Voir [ces rappels sur la ligne de commande](https://linux.goffinet.org/administration/le-shell/la-ligne-de-commande/)

---

### Fonctions et variables

- Possibilité d'utiliser / ajouter des fonctions (voir TP)
- `ma_var=2` : `ma_var` vaut `2` (pas de type)
- `$ma_var` : contenu de `ma_var`
- Variable `PATH` : lien entre nom de commande et chemin du programme
- Variable `HOME` : chemin du _home_ de l'utilisateur (`/root` ou `/home/…`)

---

## Personnalisation ou écriture de scripts simples

- `for`, `while`, `if`, `&&,` `||`
- `read`, `seq`
- `exec`
- `$?` : code de retour (`exit …`) - `0` si OK
- `|` (pipe) : redirige stdout vers stdin prochaine commande
- `#!/usr/bin/env bash` : shebang
- `chmod +x` : rend le script exécutable

---
 
# Journaux systèmes

---

## systemd

- Commandes dédiées : `systemctl`, `journalctl`
- Voir le TP [tp-sysv-systemd][tp-sysv-systemd].
- `/etc/systemd/journald.conf`

---

## Syslog

- Protocole client/serveur de journaux d'événements :
  - client : envoi d'informations (UDP 514 ou TCP)
  - serveur : collecte centralisée et création des journaux
  - solution de journalisation standard sur Unix, périphériques réseau (commutateurs, routeurs), disponible sous Windows
- fichiers par défaut : `/var/log/syslog`
- implémentations : `syslog`, `rsyslog`, `syslog-ng`

---

Voir le [TP sur les journaux][tp-syslog].

---

# Notions élémentaires sur les protocoles Internet

---

## Rappels

---

### IPv4/IPv6

- Rappels sur l'adressage IPv4/IPv6 :
  - [Cours LPI](https://learning.lpi.org/en/learning-materials/102-500/109/109.1/109.1_01/)
  - [Cours sur le site : "Le Web, HTTP, Introduction au Cloud, architectures client/serveur et types d’applications mobiles"](/cours/cloud/index.html)
  - [Cours TCP/IP de François Goffinet](https://linux.goffinet.org/administration/configuration-du-reseau/introduction-a-tcp-ip/)

---

### Couche de transport

- `TCP`
- `UDP`
- `ICMP`

---

### Ports par défaut

- Principaux services et ports par défaut sur TCP/IP : [voir le cours "Communication entre processus et applications client/serveur sur TCP/IP"](/cours/cloud/index.html)
- `/etc/services` : principaux services

---
 
## Configuration réseau persistante et résolution de problèmes réseaux simples

---

### net-tools vs iproute2

- `net-tools` : anciennes commandes Unix
  - `ifconfig`, `route`, `arp`, `netstat`, `nameif`
  - souvent encore disponibles
- `iproute2` : nouvelles commandes `ip`
  - `ip address`, `ip link`, `ip route`, `ip neighbor`, `ip tunnel`, `ip rule`, `ip maddress`, `ip mroute`, `ip mroute-cache`, `ip netns`, `ip ntable`
  - plus cohérentes, plus de fonctionnalités, recommandées

---

### Noms des interfaces

---

#### Ancien nommage d'interfaces

- `eth0`, `eth1`, … : réseau filaire
- `wlan0`, `wlan1`, … : réseau sans fil
- problème : ordre aléatoire (1e détecté => `0`)

---

#### Nommage `systemd`

- `en` : Ethernet
- `ib` : InfiniBand
- `sl` : Serial line IP (slip)
- `wl` : Wireless local area network (WLAN)
- `ww` : Wireless wide area network (WWAN)

---

#### Algo de nommage `systemd`

1. Index du BIOS du firmware : `eno1`
1. PCI express slot : `ens1`
1. Addresse du bus : `enp3s5`
1. Adresse MAC de l'interface : `enx78e7d1ea46da`
1. Legacy : `eth0`

---

### Gestion des interfaces

- `ifconfig` : ancienne commande
- `ip` : plus puissante, et sépare les couches et services
  - `ip link`, `ip addr`, `ip route`, …
- `ifup` et `ifdown` : gestion simplifiée
  - `/etc/network/interfaces`
  - ⚠️ `ifup` et `ifdown` ne sont pas standardisés :
    - `CentOS` : `/etc/sysconfig/network-scripts/` (un peu différent)

---

#### Fichier `/etc/network/interfaces`

```
# loopback
auto lo
iface lo inet loopback

# `auto` => ifup -a
# `inet`, `ipx` ou `inet6`
# dhcp
auto enp3s5
iface enp3s5 inet dhcp

# static
iface enp3s6 inet static
    address 192.168.1.2/24
    gateway 192.168.1.1
```

---

### Hostname

- commande: `hostname`
- `/etc/hostname`
- `hostnamectl set-hostname monhostname`
- `hostnamectl --pretty set-hostname "LAN Shared Storage"`
- `hostnamectl status`

---

### DNS

- _Name Service Switch_ configuration file: `/etc/nsswitch.conf`
- décrit l'ordre de priorité des résolutions
- `files` => local (`/etc/hosts`)
- `dns` => resolver DNS (`/etc/resolv.conf`)

```
hosts: files dns
```

---

#### Résolution locale

- Fichier `/etc/hosts`

```
127.0.0.1 localhost
192.168.1.10 foo.mydomain.org foo
::1 localhost ip6-localhost ip6-loopback
```

---

#### Configuration DNS

- Fichier `/etc/resolv.conf`

```
# Google
nameserver 8.8.8.8
# Auto-add the domain to short hostnames
domain mydomain.org
# List of domains to search (default: content of `domain`)
search mydomain.net mydomain.com
```

---

#### Résolution DNS

- `nslookup www.wikipedia.fr` : résolution DNS
- `dig @8.8.8.8 www.wikipedia.fr` : résolution DNS en passant par le serveur DNS de Google (`8.8.8.8`)
- `host www.wikipedia.fr` ou `host www.wikipedia.fr 8.8.8.8`
- fichier `/etc/resolv.conf`

---

#### systemd-resolved

- Résolution DNS via `systemd`
- caching, espaces de noms de routage spécifiques (`scope`), DNS via VPN, …
- commande `systemd-resolved`
- config `/etc/systemd/resolved.conf.d/`
- intégration avec `NetworkManager`

---

### Routage

- `route` : ancienne commande `net-tools`
- `ip route` : configuration du routage via `iproute2`
- `traceroute www.google.fr` : utilise UDP
- `tracepath www.google.fr` : utilise ICMP

---

### ICMP

- `ping -4 www.google.fr`
- `ping -6 www.google.fr`

---

### systemd

- `systemd-resolved` : DNS
- `systemd-networkd` : config réseau
- compatibles _legacy_
- `/etc/systemd/network`

---

#### Exemple

```
[Match]
Name=enp3s5
# ou :
#MACAddress=00:16:3e:8d:2b:5b

[Network]
DHCP=yes # ou IPv4 ou IPv6
# ou :
#Address=192.168.0.100/24
#Gateway=192.168.0.1
```

---

### NetworkManager

- Configuration centrale du réseau : 1 seul outil
- commandes `nmcli` et `nmtui`
- intégré par défaut dans la plupart des environnements de bureau
- compatible _legacy_

---

### Vérifier le réseau

1. `ip addr show` : Adresse IP ?
2. `ping www.google.fr` : connectivité ?
3. `ip route` et `traceroute www.google.fr` : routage ?
4. `nslookup www.google.fr` ou `dig www.google.fr` et fichier `/etc/resolv.conf` : DNS ?

---

### Statistiques

- `ss` (socket statistics) : informations sockets réseau et connexions actives
- `netstat` (network statistics) : idem mais ancienne commande

---

### NetworkCat

- `netcat` (`nc`) : lis / écris des données sur des sockets réseau.
  - ouverture de connexions TCP / UDP
  - tunnels réseau
  - transfer de fichiers
  - débug : écoute de ports, …

---

Voir le [TP sur la configuration du réseau sous Linux][tp-network]

---

# Sécurité

![Run as an admin…](@assets/linux/run_as_admin.jpg)

---

## Élévation de privilèges

- `su` : login comme autre utilisateur (par défaut `root`, sinon : `su - mon_utilisateur`)
- `sudo` : effectuer 1 commande avec le contexte de `root`
  - À préférer grandement à `su` ! (audit, …)
  - configuration dans `/etc/sudoers`

---

## SSH [TCP 22]

- `ssh` (Secure SHell) : protocole de communication sécurisé :
  - Utilisé majoritairement pour ouvrir un shell sur un ordinateur distant Unix.
  - Indispensable pour les machines virtuelles

---

- Chiffrement symétrique ou (mieux) asymétrique (clé privée / clé publique)
- Impose un échange de clés de chiffrement en début de connexion : tous les segments TCP sont authentifiés et chiffrés
- sshv2 fournit `scp` et `sftp` avec la même configuration
- Peut encapsuler un autre protocole dans un tunnel (y compris `X11`)
- Supporte différents algorithmes : `RSA`, `DSA`, `RD25519`, …
  - Le "meilleur" est utilisé (supporté par le client et le serveur)

---

- `~/.ssh/id_rsa` (clé privée) et `~/.ssh/id_rsa.pub` (clé publique)
- `~/.ssh/authorized_keys` : clés publiques autorisées à ouvrir une connexion
- `~/.ssh/known_hosts` : IDs des machines distantes connues (pas besoin de revérifier)
- `ssh-keygen` crée les clés SSH (public + privée) dans `~/.ssh`
- `ssh-copy-id -i <public_key> user@cloud_server` : copie la clé publique sur le serveur (dans `~user/.ssh/authorized_keys`)
- Les permissions des fichiers de clés doivent être :
  + `0600` pour la clé privée
  + `0644` pour la clé publique

---

### GNU Privacy Guard (GPG)

- Sécurise les fichiers, les communications et les e-mails : protocole `OpenPGP`
  - Asymétrique
  - Chiffrement et Signature
  - Infrastructure à clé publique (PKI) : partage de clés publiques

---

Voir le [TP sur SSH et GPG][tp-ssh-gpg]

---

<!-- Annexe : liste des TPs -->

[tp-ligne-commande]: tp-ligne-commande.md
[tp-systeme]: tp-systeme.md
[tp-grub]: tp-grub.md
[tp-shared-lib]: tp-shared-lib.md
[tp-sysv-systemd]: tp-sysv-systemd.md
[tp-rpm-apt]: tp-rpm-apt.md
[tp-texte]: tp-texte.md
[tp-fichiers]: tp-fichiers.md
[tp-redirections]: tp-redirections.md
[tp-process]: tp-process.md
[tp-fichiers-avance]: tp-fichiers-avance.md
[tp-partitions]: tp-partitions.md
[tp-cron]: tp-cron.md
[tp-lang]: tp-lang.md
[tp-smtp]: /cours/cloud/exo-smtp.md
[tp-syslog]: tp-syslog.md
[tp-network]: tp-network.md
[tp-security]: tp-security.md
[tp-ssh-gpg]: tp-ssh-gpg.md

<!-- Annexe: liste des liens utiles -->
[wiki-shared-lib]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/Installation_de_Linux_et_gestion_des_packages/G%C3%A9rer_les_biblioth%C3%A8ques_partag%C3%A9es
[wiki-partitions]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/P%C3%A9riph%C3%A9riques_et_syst%C3%A8mes_de_fichiers_Linux/Cr%C3%A9er_des_partitions_et_des_syst%C3%A8mes_de_fichiers
[wiki-filtres]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Ex%C3%A9cution_de_flux_de_textes_en_utilisant_des_filtres
[wiki-fichiers]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Gestion_de_base_des_fichiers
[wiki-redirections]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Utiliser_les_streams,_pipes,_et_redirections
[wiki-regex]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Expressions_r%C3%A9guli%C3%A8res

# Legal

- Linux est une marque déposée par Linus Torvalds aux États Unis et dans d'autres pays.
- Red Hat Linux et Red Hat Enterprise Linux sont des marques déposées par RedHat Inc.
- Mandriva® Linux® est une marque déposée par Mandriva Inc.
- SUSE™ (SUSE est une marque de SUSE LINUX Products GmbH, une filiale de Novell)
- UNIX® est une marque déposée de The Open Group. 
- Other names may be trademarks of their respective owners

