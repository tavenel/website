---
title: Configuration réseau sous Linux
date: 2024 / 2025
correction: false
---

## Commandes utiles

| Fonction                              | Net-tools   | iproute2             |
|---------------------------------------|-------------|----------------------|
| Adresses IP et interface (L2)         | `ifconfig`  | `ip addr`, `ip link` |
| Tables de routage                     | `route`     | `ip route`           |
| Tables de voisinage                   | `arp`       | `ip neigh`           |
| VLAN                                  | `vconfig`   | `ip link`            |
| Tunnels                               | `iptunnel`  | `ip tunnel`          |
| Commutation (Bridges)                 | `brctl`     | `ip link`, `bridge`  |
| Multicast                             | `ipmaddr`   | `ip maddr`           |
| Statistiques                          | `netstat`   | `ip -s`, `ss`        |

:::link
Voir aussi : <https://www.linuxtricks.fr/wiki/la-commande-ip-reseau-interfaces-routage-table-arp>
:::

## Gestion des interfaces

### Visualiser les adresses

::: exo
1. En utilisant la commande `ifconfig -a`, visualisez les interface et les adresses IP associées sur votre système.
2. Même exercice en utilisant les commandes `ip` : `ip addr show` et `ip link show`.
3. Bonus : utiliser un filtre `grep` et `awk` pour n'afficher que les adresses IP des interfaces `inet`.
:::

::: {.correction .if correction="true"}
1. `ifconfig | grep -w inet | awk '{ print $2}'`
2. `ip a s | grep -w inet | awk '{ print $2}'`
:::

### Activer / désactiver une interface

::: exo
1. En utilisant les scripts `ifup` et `ifdown`, désactiver puis réactiver une interface réseau.
2. Même question en utilisant `ifconfig`.
3. Même question en utilisant `ip`.
:::

::: {.correction .if correction="true"}
1. En utilisant les scripts `ifup` et `ifdown`, désactiver puis réactiver une interface réseau.
```
sudo ifdown eth0
sudo ifup eth0
```
2. Même question en utilisant `ifconfig`.
```
sudo ifconfig eth0 down
sudo ifconfig eth0 up
```
3. Même question en utilisant `ip`.
```
sudo ip link set eth0 down
sudo ip link set eth0 up
```
:::

### Ajouter / supprimer une adresse IPv4

::: exo
1. En utilisant `ifconfig` ajouter une adresse IP. La syntaxe est : `ifconfig <interface> <IP>`
2. En utilisant `ip addr` ajouter une adresse IP. La syntaxe est : `ip addr add <IP> dev <interface>`
3. Supprimer l'adresse IP.
4. Ajouter une interface alias (par exemple `eth0:1`) et lui assigner une IP avec `ifconfig`
5. Même question avec `ip addr`.
:::

::: {.correction .if correction="true"}
```
# Ajout IP
sudo ifconfig eth0 192.168.0.77/24
sudo ip address add 192.168.0.77/24 dev eth0

# Suppression IP
sudo ip addr del 192.168.0.77/24 dev eth0

# Alias
sudo ifconfig eth0:1 10.0.0.1/8
sudo ip addr add 10.0.0.1/8 dev eth0 label eth0:1

```
:::

### Persistance : fichier `/etc/network/interfaces`

Le fichier `/etc/network/interfaces` permet de configurer le réseau de manière statique.

#### Exemple de fichier `/etc/network/interfaces`

```/etc/network/interfaces
# loopback
auto lo
iface lo inet loopback
allow-hotplug eth0

# `auto` => ifup -a
# `inet`, `ipx` ou `inet6`
# dhcp
auto enp3s5
iface enp3s5 inet dhcp

# static
iface enp3s6 inet static
    address 192.168.1.2/24
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 192.0.2.71

iface eth0 inet6 static
    address 2001:db8::6726
    netmask 32
    gateway 2001:db8::1
    dns-nameservers 2001:db8::12
```

:::exo
Utiliser le fichier `/etc/network/interfaces` et les commandes `ifup` / `ifdown` pour persister la configuration réseau précédente.
:::

### Dénomination traditionnelle

Pour activer la dénomination traditionnelle, il faut éditer le fichier `/etc/default/grub` en ajoutant la valeur `net.ifnames=0 biosdevname=0` à la variable `GRUB_CMDLINE_LINUX`.

```
GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
```

Il sera alors nécessaire de mettre à jour grub et de redémarrer le système :

```
sudo update-grub
sudo reboot
```

Attention, il sera aussi indispensable d’adapter le fichier de configuration `/etc/network/interfaces` avec le nouveau nom d'interface.

:::exo
1. Changer la dénomination des interfaces pour utiliser la dénomination traditionnelle.
2. Revenir ensuite sur la nouvelle dénomination.
:::

## Hostname

:::exo
1. Afficher le nom réseau de la machine.
2. Changer le _hostname_ de 2 manières différentes, depuis un fichier de configuration et depuis une commande dédiée provenant de `systemd`
:::

::: {.correction .if correction="true"}
1. Afficher le hostname : `hostname`
2. Changer le hostname :

```
echo 'monhostname' > /etc/hostname
hostnamectl set-hostname monhostname
```
:::

## DHCP

::: exo
1. En utilisant `dhclient`, libérer un bail et arrêter le client DHCP.
2. Relancer le client et obtenir de nouveaux paramètres DHCP.
:::

::: {.correction .if correction="true"}
1. En utilisant `dhclient`, libérer un bail et arrêter le client DHCP.
  ```
  sudo dhclient -r
  ip addr show
  ```
2. Relancer le client et obtenir de nouveaux paramètres DHCP : `sudo dhclient -d`
  ```
  Internet Systems Consortium DHCP Client 4.2.5
  Copyright 2004-2013 Internet Systems Consortium.
  All rights reserved.
  For info, please visit https://www.isc.org/software/dhcp/
  
  Listening on LPF/eno16777736/00:0c:29:7b:c0:98
  Sending on   LPF/eno16777736/00:0c:29:7b:c0:98
  Sending on   Socket/fallback
  DHCPDISCOVER on eno16777736 to 255.255.255.255 port 67 interval 4 (xid=0x5511e5b4)
  DHCPREQUEST on eno16777736 to 255.255.255.255 port 67 (xid=0x5511e5b4)
  DHCPOFFER from 192.168.95.254
  DHCPACK from 192.168.95.254 (xid=0x5511e5b4)
  bound to 192.168.95.128 -- renewal in 766 seconds.
  ```
:::

## Table de voisinage

::: exo
En utilisant `ip neigh` afficher la table de voisinage. À quoi correspondent ces informations ?
:::

::: {.correction .if correction="true"}
```
ip neigh show

192.168.1.254 dev wlan0 lladdr 7c:16:89:cf:91:7c used 0/0/0 probes 1 STALE
172.17.0.3 dev docker0 lladdr 02:42:ac:11:00:03 used 0/0/0 probes 1 STALE
172.17.0.2 dev docker0 lladdr 02:42:ac:11:00:02 used 0/0/0 probes 4 STALE
192.168.1.43 dev wlan0 lladdr 4a:71:eb:bc:93:ea used 0/0/0 probes 0 STALE
172.23.0.5 dev br_website  used 0/0/0 probes 6 FAILED
192.168.1.112 dev wlan0 lladdr 10:b1:df:8a:96:b7 used 0/0/0 probes 0 STALE
fe80::7e16:89ff:fecf:917c dev wlan0 lladdr 7c:16:89:cf:91:7c router used 0/0/0 probes 1 STALE
```

Il s'agit de la table `ARP` qui affiche les corrélations entre adresses IP et adresses MAC pour les machines connues sur le réseau ("voisins").
:::

## DNS

### Ordre de résolution

L'ordre de résolution des noms est géré par priorité dans le fichier de configuration _Name Service Switch_ : `/etc/nsswitch.conf`

```/etc/nsswitch.conf
hosts: files dns
```

### Résolution locale

- Le fichier `/etc/hosts` contient les résolutions codées en dur sur la machine locale (par exemple : `localhost`)

```/etc/hosts
127.0.0.1 localhost
192.168.1.10 foo.mydomain.org foo
::1 localhost ip6-localhost ip6-loopback
```

### Résolution DNS distante

- Le fichier `/etc/resolv.conf` contient les adresses des serveurs de noms distants

```/etc/resolv.conf
# Google
nameserver 8.8.8.8
# Auto-add the domain to short hostnames
domain mydomain.org
# List of domains to search (default: content of `domain`)
search mydomain.net mydomain.com
```

### systemd-resolved

`systemd` dispose de son propre utilitaire de résolution de noms : le service `systemd-resolved` (et sa commande associée `resolvectl`). Voir le fichier de configuration : `/etc/systemd/resolved.conf`

### Exercice

:::exo
1. Inspecter les différents fichiers permettant la résolution des noms de domaines sur la machine courante.
2. En utilisant la commande `dig` ou `nslookup`, vérifier la bonne résolution de noms sur le système (`localhost`, `google.fr`, …).
:::

## Routage et ping

:::exo
1. Tester la connexion vers le serveur distant `google.fr` en IPv4 puis en IPv6.
2. Afficher la table de routage avec une commande de `net-tools` puis avec une commande de `iproute2`.
3. Afficher la passerelle permettant le routage vers l'adresse IP de `google.fr` : `216.58.212.99`
4. Tracer le routage vers `google.fr`. Attention, le réseau local peut bloquer une partie des résultats !
5. En utilisant `ip`, ajouter une nouvelle route par défaut via l'IP de la passerelle de votre réseau et utilisant votre interface de connexion.
5. En utilisant `ip`, ajouter une nouvelle route pour le réseau auquel vous êtes connecté uniquement, via l'IP de la passerelle de votre réseau et utilisant votre interface de connexion.
:::


::: {.correction .if correction="true"}
1. `ping -4 google.fr` et `ping -6 google.fr`
2. `route` et `ip route list`
3. `ip route get 216.58.212.99`
4. `traceroute google.fr`
5. `ip route add default via 192.168.1.254 dev wlan0`
6. `ip route add 192.168.1.0/24 via 192.168.1.254 dev wlan0`
:::

## Bonus : `systemd-networkd`

:::exo
Reprendre l'exercice de persistance en utilisant `/etc/network/interfaces` et utiliser un fichier de configuration `systemd-networkd` à la place.
:::

:::link
Pour plus d'information, voir la page de cours sur `systemd-networkd` : <https://learning.lpi.org/en/learning-materials/102-500/109/109.2/109.2_02/>
:::

## Network Manager

Il existe de nombreux programmes sous Linux pour simplifier la configuration du réseau en un seul outil, plutôt que d'utiliser un ensemble de scripts et de fichiers de configuration.

Le plus connu est `Network Manager` et ses interfaces : `nmcli` en ligne de commandes, `nmtui` pour l'interface graphique.

La plupart des environnements de bureau intègrent _Network Manager_ par défaut.

:::exo
Exécuter [le TP de gestion du réseau Linux avec Network Manager](https://linux.goffinet.org/administration/configuration-du-reseau/gestion-du-reseau-linux-avec-networkmanager/) de _François Goffinet_
:::

## Transfert de données avec `netcat` (`nc`)

Netcat permet d'établir une connexion réseau entre deux machines et de transférer des données.

:::exo
1. Ouvrez deux terminaux (dans votre machine virtuelle)
2. Dans le 1er terminal, démarrez Netcat en mode écoute sur un port spécifique, par exemple : `nc -l -p 12345`
3. Dans le 2nd terminal, établir une connexion en spécifiant le nom local (`localhost`) le port sur lequel Netcat écoute (12345 dans cet exemple) : `nc localhost 12345`
4. Une fois la connexion établie, vous pouvez commencer à transférer des données. Tapez du texte dans le 1er terminal et appuyez sur Entrée. Vous devriez voir le texte apparaître dans le 2nd terminal - et réciproquement.
5. Reproduire le même exercice sur le réseau entre 2 machines distantes.
  - Attention aux éventuels problèmes de pare-feu !
:::

## Monitoring réseau

::: exo
1. Vérifier et noter les paramètre des interfaces réseau :
  - Nom
  - Statut
  - Adresse IP et masque
  - Passerelle
  - Serveur(s) DNS
:::

Voir le TP sur la sécurité pour une analyse réseau plus poussée : scan des ports ouverts, …

