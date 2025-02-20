---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Cours Linux avancé - partie 2
tags:
- linux
---

# Objectifs - 1/2

- Paramétrer le shell et écrire des scripts simples en `Bash`
- Installer et configurer l'interface graphique
- Connaître les outils d'accessibilité
- Effectuer les tâches d'administration de base : gérer les utilisateurs, utiliser les tâches automatiques, …

---

# Objectifs - 2/2

- Installer et paramétrer les services essentiels : messagerie, impression, horloge système, journaux système
- Avoir les notions de réseau essentielles à l’administration système : protocoles Internet, configuration réseau des postes, résolution `DNS` et dépannage
- Savoir mettre en place un niveau de sécurité sur les postes : services en écoute et ports ouverts, limitations d'accès, et chiffrement des données

---

# Plan de cours

---

## Sujet 105 : Shells et scripts Shell [8]

- 105.1 Personnalisation et utilisation de l’environnement du shell [4]
- 105.2 Personnalisation ou écriture de scripts simples [4]

---

## Sujet 106 : Interfaces et bureaux utilisateur [4]

- 106.1 Installation et configuration de X11 [2]
- 106.2 Bureaux graphiques [1]
- 106.3 Accessibilité [1]

---

## Sujet 107 : Tâches d’administration [12]

- 107.1 Gestion des comptes utilisateurs et des groupes ainsi que des fichiers systèmes concernés [5]
- 107.2 Automatisation des tâches d’administration par la planification des travaux [4]
- 107.3 Paramètres régionaux et langues [3]

---

## Sujet 108 : Services systèmes essentiels [12]

- 108.1 Gestion de l’horloge système [3]
- 108.2 Journaux systèmes [4]
- 108.3 Bases sur l’agent de transfert de courrier (MTA) [3]
- 108.4 Gestion des imprimantes et de l’impression [2]

---

## Sujet 109 : Notions élémentaires sur les réseaux [14]

- 109.1 Notions élémentaires sur les protocoles Internet [4]
- 109.2 Configuration réseau persistante [4]
- 109.3 Résolution de problèmes réseaux simples [4]
- 109.4 Configuration de la résolution de noms [2]

---

## Sujet 110 : Securité [10]

- 110.1 Tâches d’administration de sécurité [3]
- 110.2 Configuration de la sécurité du système [3]
- 110.3 Sécurisation des données avec le chiffrement [4]

---

# Ressources utiles

- [Support de cours](https://learning.lpi.org/en/learning-materials/102-500/)
- [Objectifs détaillés de la certification LPIC-102](https://www.lpi.org/fr/our-certifications/exam-102-objectives)
- [Livre Bash beginner's guide](https://ftp.traduc.org/doc-vf/guides/Bash-Beginners-Guide/)
- Aide simple sur les commandes : <https://cheat.sh/>
- Explication graphique de commandes Shell complexes : <https://explainshell.com/>
- [Créer une distribution "Live" (qui reste en mémoire) - tuto complet, reprend les principes de base, du boot à un système minimal](https://zestedesavoir.com/tutoriels/268/creer-son-premier-rim-linux/)

---

## Conventions de notation

- Les commandes et noms de fichiers apparaissent dans le texte avec `cette syntaxe`.
- Les descriptions de commandes suivent le formalisme des _man pages_ :
  - Les symboles `<>` indiquent un argument obligatoire.
  - Les symboles `[]` indiquent un argument optionnel.  

---

# Sujet 105 : Shells et scripts Shell

---

## 105.1 Personnalisation et utilisation de l’environnement du shell [4]

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

## 105.2 Personnalisation ou écriture de scripts simples [4]

- `for`, `while`, `if`, `&&,` `||`
- `read`, `seq`
- `exec`
- `$?` : code de retour (`exit …`) - `0` si OK
- `|` (pipe) : redirige stdout vers stdin prochaine commande
- `#!/usr/bin/env bash` : shebang
- `chmod +x` : rend le script exécutable

---
 
# Sujet 106 : Interfaces et bureaux utilisateur

---

## 106.1 Installation et configuration de X11 [2]

---

### X11

- Système graphique historique de Linux
- Modèle client / serveur
- Session X courante dans variable `DISPLAY` (en principe: `:0`)
- `/etc/X11/xorg.conf`
- `~/.xsession-errors`

---

![Architecture de X11](https://learning.lpi.org/en/learning-materials/102-500/106/106.1/106.1_01/images/image_01.png)

_Architecture de X11 (crédits: learning.lpi.org)_

---

### Wayland

- Successeur de `X11` : adopté par défaut sur `Ubuntu`, `Fedora`, …
- Session courante : variable `WAYLAND_DISPLAY` : (`wayland-0`, …)

---

## 106.2 Bureaux graphiques [1]

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

## 106.3 Accessibilité [1]

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

# Sujet 107 : Tâches d’administration

---

## 107.1 Gestion des comptes utilisateurs et des groupes ainsi que des fichiers systèmes concernés [5]

---

### Utilisateurs

- `useradd` : crée un utilisateur
- `userdel` : supprime un utilisateur
- `usermod` : modifie un utilisateur
  - `usermod --append --groups group1,group2,... username`
- `/etc/passwd` : fichier comptes utilisateurs (locaux)
- `/etc/skel/` : squelette copié dans le `home` d'un nouvel utilisateur

---

### Mots de passe

- `/etc/shadow` : fichier mots de passe (comptes locaux)
- `passwd` : changer un mot de passe
- `chage` : change l'expiration d'un mot de passe

---

### Groupes

- `/etc/group` : fichier groupes et utilisateurs rattachés
- `groupadd` : crée un groupe
- `groupdel` : supprime un groupe
- `groupmod` : modifie un groupe
  - `groupmod --new-name new_group group_name`

---

### getent

- `getent` : affiche les infos d'une BDD Unix (`passwd`, `shadow`, `group`, …)
  - fichiers locaux + services externes : `NIS`, `LDAP`, …
  - `getent group docker`

---
 
## 107.2 Automatisation des tâches d’administration par la planification des travaux [4]

---

### `at`

- programme 1 exécution unique
- `echo "il est sept heures et demi" | at 0730`

---

### `cron`

- Service historique de planification
  - éxécution répétée de tâches
- Service `cron.d` (`/etc/cron.d/`)
- `/etc/crontab` : format de description des récurrences
  - très réutilisé dans d'autres programmes
  - commande `crontab -l` et `crontab -e`
- `/etc/cron.{daily/,hourly/,monthly/,weekly/}` contiennent des scripts à exécuter chaque jour, heure, mois, semaine

---

### `systemd`

- `systemd timer units` : fichiers de configuration `systemd` pour planifier et exécuter des tâches périodiques
- gestion des dépendances, intégration aux services `systemd`, …

---

Voir le [tp sur les tâches planifiées (cron)][tp-cron]

---

## 107.3 Paramètres régionaux et langues [3]

---

### Normes encodage

- `ASCII` : codage de base (anglais) ;
- `ISO-8859` : extension pour d'autres langues européennes ;
- `Unicode` : pour représenter tous les caractères de toutes les langues du monde ;
- `UTF-8`, `UTF-16` : encodages flexibles compatibles `Unicode` et `ASCII`.
- `iconv -f ASCII -t UTF-8 input.txt > output.txt`

---

### Langue

- variable `LANG` : langage utilisée par les programmes
- exemple: `LANG=fr_FR.UTF-8`
- `LANG=C` : force `ASCII` et Anglais
  - tri `ASCII` : `fichier9` > `fichier10`
  - dates : `MM/DD/YYYY` (vs. européen : `DD/MM/YYYY`)
  - utile dans script Shell pour éviter un comportement aléatoire

---

### _Locale_

- variables `LC_*` : gèrent les _locale_ à utiliser
- `LC_ADDRESS` ,`LC_COLLATE` ,`LC_CTYPE` ,`LC_IDENTIFICATION` ,`LC_MEASUREMENT` ,`LC_MESSAGES` ,`LC_MONETARY` ,`LC_NAME` ,`LC_NUMERIC` ,`LC_PAPER` ,`LC_TELEPHONE` ,`LC_TIME`
  - exemple : `LC_TIME=fr_FR.UTF-8`
  - `LC_ALL` : surcharge tous les autres `LC_*` si définie
- commande: `locale`

---

Voir le [tp dédié aux langues][tp-lang].

---
 
# Sujet 108 : Services systèmes essentiels

---

## 108.1 Gestion de l’horloge système [3]

---

### Temps universel

- `date` : affichage / gestion date et heure
- Heure _UNIX_ : nombre de secondes écoulées depuis le 1er janvier 1970
- Convention UNIX : stocker l'heure `UTC` (Temps Universel Coordonné)

---

### Timezone

- Modifie l'heure affichée par un fuseau horaire : `Europe/Paris`, …
- `/etc/timezone` ou `/etc/localtime`
- timezones disponibles dans: `/usr/share/zoneinfo/`
- commande: `tzselect`
- ou variable `TZ` : `export TZ='Europe/Paris'`
- ou (Debian/Ubuntu) : `sudo dpkg-reconfigure tzdata`

---

### Hardware clock

- `hwclock` : affichage / gestion horloge matérielle
- `hwclock --systohc` : synchronisation horloge système vers matérielle

---

### Synchronisation réseau

- Réseau => besoin de cohérence des horloges (journalisation, sécurité, …)
- `Network Time Protocol` (`NTP`) : synchronisation des horloges depuis des serveurs de temps fiables
  - hiérarchie pyramidale : strate 0 (horloges atomiques ou GPS) puis synchronisation strate 1, … , 15
  - algorithmes puissants : retard réseau, …
- Dæmons de synchronisation :
  - `ntpd` : `/etc/ntp.conf`, commande `ntpdate`
  - `chrony` : `/etc/chrony.conf`, commande `chronyc`

---

### Serveurs de temps de référence

- Europe Time Servers : <europe.pool.ntp.org> : pool communautaire Europe
- Stratum-1 servers : <pool.ntp.org> : pool communautaire monde
- NIST Time Servers : <time.nist.gov>
- US Naval Observatory : <ntp.usno.navy.mil>

---

### systemd : timedatectl

- `timedatectl` : affichage date et heure
- `timedatectl set-timezone Europe/Paris`
- `timedatectl set-ntp true`
- `timedatectl timesync-status`
- `timedatectl set-time`

---
 
## 108.2 Journaux systèmes [4]

---

### Rappel : logs système

- Voir le TP [tp-systeme][tp-systeme] pour les rappels sur les logs système.

---

### Rappel systemd

- Voir le cours et le TP sur `systemd` dans la partie LPIC-101 :
- Commandes dédiées : `systemctl`, `journalctl`
- Voir le TP [tp-sysv-systemd][tp-sysv-systemd].
- `/etc/systemd/journald.conf`

---

### Syslog

- Protocole client/serveur de journaux d'événements :
  - client : envoi d'informations (UDP 514 ou TCP)
  - serveur : collecte centralisée et création des journaux
  - solution de journalisation standard sur Unix, périphériques réseau (commutateurs, routeurs), disponible sous Windows
- fichiers par défaut : `/var/log/syslog`
- implémentations : `syslog`, `rsyslog`, `syslog-ng`

---

Voir le [TP sur les journaux][tp-syslog].

---
 
## 108.3 Bases sur l’agent de transfert de courrier (MTA) [3]

---

### SMTP(S)

- `Simple Mail Transfer Protocol` : envoi d'e-mail (protocole ultra majoritaire) :
  1. expéditeur
  2. destinataires
  3. transfert du corps du message
- TCP 25 / implicite:465 / explicite:587

---

### Mail Transfert Agent (SMTP)

- `sendmail`, `postfix`, `exim`
- Possibilité d'envoyer des mails aux comptes locaux

---

### Mail User Agent

- Programmes clients de lecteur/envoi de mails : `Thunderbird`, `mail`, …

```sh
$ mail -s "Maintenance fail" henry@lab3.campus <<<"The maintenance script failed at `date`"
```

---

### Transfert de courriers

```sh
$ cat ~/.forward
emma@lab1.campus
```

---

Voir le [TP sur SMTP][tp-smtp].

---
 
## 108.4 Gestion des imprimantes et de l’impression [2]

---

### Common Unix Printing System (CUPS)

1. L'utilisateur soumet un fichier pour impression.
2. Le dæmon `cupsd` dépile le job d'impression (numéro de job, queue d'impression, nom du document).
3. `CUPS` utilise des filtres installés sur le système pour généré un fichier au format utilisable par l'imprimante.
4. `CUPS` envoie le fichier re-formatté à l'imprimante

- `/etc/cups/cupsd.conf`
- Interface héritée de `lpd` (`lpadmin`, `lpinfo`, `lpoptions`, `lpr`, `lpstat`, `lp`, …)

---
 
# Sujet 109 : Notions élémentaires sur les réseaux

---

## 109.1 Notions élémentaires sur les protocoles Internet [4]

---

### Rappels

---

#### IPv4/IPv6

- Rappels sur l'adressage IPv4/IPv6 :
  - [Cours LPI](https://learning.lpi.org/en/learning-materials/102-500/109/109.1/109.1_01/)
  - [Cours sur le site : "Le Web, HTTP, Introduction au Cloud, architectures client/serveur et types d’applications mobiles"](/cours/cloud/index.html)
  - [Cours TCP/IP de François Goffinet](https://linux.goffinet.org/administration/configuration-du-reseau/introduction-a-tcp-ip/)

---

#### Quatre couches

- Couche _Application_ : `HTTP`, `DNS`, `DHCP`, `FTP`, …
  - couche de communication entre utilisateurs (sur machines hôtes)
- Couche _Transport_ : `TCP`, `UDP`, `ICMP`
  - filtrage par routeurs NAT et pare-feu
- Couche Internet : `IPv4`, `IPv6`
  - chemins dans le réseau
  - transfert par routeurs
- Couche _Accès au réseau_
  - flux binaire et identification physique des machines (non décrit par TCP/IP)

---

#### Ports par défaut

- Principaux services et ports par défaut sur TCP/IP : [voir le cours "Communication entre processus et applications client/serveur sur TCP/IP"](/cours/cloud/index.html)
- `/etc/services` : principaux services

---
 
## 109.2 Configuration réseau persistante [4]
## 109.3 Résolution de problèmes réseaux simples [4]
## 109.4 Configuration de la résolution de noms [2]

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

# Sujet 110 : Securité

---

## 110.1 Tâches d’administration de sécurité [3]
## 110.2 Configuration de la sécurité du système [3]

![Run as an admin…](@assets/linux/run_as_admin.jpg)

---

### Exemples de thèmes de sécurité

- Limites utilisateurs pour les connexions, processus, utilisation mémoire : `usermod`, `ulimit`
- Mots de passe : `passwd`, `chage`
- Élévation de privilèges : `su`, `sudo`, `/etc/sudoers`
- Ports ouverts : `nmap`, `ss`
- Audit des fichiers avec permissions `suid` / `guid`
- Fichiers ouverts (et donc processus, ports, …) : `lsof`, `fuser`
- Monitorer et arrêter les services inutiles

---

### Mots de passe

- Rappel : `/etc/passwd` : fichier comptes utilisateurs (locaux)
- MDP dans fichier `/etc/shadow`
- Format :
  - `usename`
  - `hash` du MDP : `md5`, `sha256`, `sha512`, …
  - `last pass change` : # jours depuis 1970
  - `min pass age` : # jours avant de changer de MDP
  - `max pass age` : # jours MDP valide
  - `pass expiry warning` : # jours avant avertissement
  - `pass inactivity period` : # jours après expiration où le compte reste ouvert (MDP à changer)
  - `account expiration date`: date d'expiration du compte
  - dernier champ: réservé utilisation future

---

### TCP wrappers

- `/etc/hosts.allow` (`/etc/hosts.deny`): adresses IP autorisées (refusées) à se connecter aux services réseau sur le système.
- Si même IP dans `/etc/hosts.allow` et `/etc/hosts.deny` : **autorisé**
- Par défaut : autorisé
- Facile à usurper (changer d'IP)

---

### Démarrage dynamique de service depuis une socket

- Démarrage à la demande de services **uniquement** lorsque des connexions sont établies sur des sockets spécifiques.
- `xinetd` (historique) : `/etc/xinetd.conf` et scripts dans : `/etc/xinetd.d/`
- `systemd.socket` : configurations dans `/etc/systemd/system/` et services actifs dans `/etc/systemd/systemd/socket.target.wants/`

---

### `/etc/inittab`

- Configure le processus initial du système
- Définit les actions à exécuter lors de différents événements système : démarrage, changement de niveau d'exécution, …
  - inclus des restrictions d'accès
- Legacy : Obsolète si `systemd`

---

#### Exemple

```
# /etc/inittab

::sysinit:/sbin/openrc sysinit
::sysinit:/sbin/openrc boot
::wait:/sbin/openrc default

# Set up a couple of getty's
tty1::respawn:/sbin/getty 38400 tty1
[...]
tty6::respawn:/sbin/getty 38400 tty6

# Put a getty on the serial port
#ttyS0::respawn:/sbin/getty -L 115200 ttyS0 vt100

# Stuff to do for the 3-finger salute
::ctrlaltdel:/sbin/reboot

# Stuff to do before rebooting
::shutdown:/sbin/openrc shutdown
```

---

Voir le [TP sur la sécurité d'un système Linux][tp-security]

---
 
## 110.3 Sécurisation des données avec le chiffrement [4]

---

### SSH

- Chiffrement symétrique ou (mieux) asymétrique (clé privée / clé publique)
- Peut encapsuler un autre protocole dans un tunnel (y compris `X11`)
- Supporte différents algorithmes : `RSA`, `DSA`, `RD25519`, …
  - Le "meilleur" est utilisé (supporté par le client et le serveur)
- `~/.ssh/id_rsa` (clé privée) et `~/.ssh/id_rsa.pub` (clé publique)
- `~/.ssh/authorized_keys` : clés publiques autorisées à ouvrir une connexion
- `~/.ssh/known_hosts` : IDs des machines distantes connues (pas besoin de revérifier)

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

# Legal

- Linux est une marque déposée par Linus Torvalds aux États Unis et dans d'autres pays.
- Red Hat Linux et Red Hat Enterprise Linux sont des marques déposées par RedHat Inc.
- Mandriva® Linux® est une marque déposée par Mandriva Inc.
- SUSE™ (SUSE est une marque de SUSE LINUX Products GmbH, une filiale de Novell)
- UNIX® est une marque déposée de The Open Group. 
- Other names may be trademarks of their respective owners

