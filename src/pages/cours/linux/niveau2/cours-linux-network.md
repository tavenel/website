---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Cours Linux Networking
tags:
- linux
---

# Objectifs

- Découvrir la gestion du réseau sous Linux

---

# Notions élémentaires sur les réseaux

---

## Notions élémentaires sur les protocoles Internet

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
 
## Configuration réseau persistante

## Résolution de problèmes réseaux simples

## Configuration de la résolution de noms

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

# Pare-feu : Netfilter/IpTables

- `Netfilter` : module noyau pare-feu, traduction d'adresse (NAT) et historique réseau
- Intercepte et manipule les paquets IP **avant** et **après** le routage.
- `iptables` / `ip6tables` : commande de configuration de `Netfilter`.

---

## Modèle

- Les paquets passent à travers des chaînes qui vont déterminer ce que le système doit en faire
  - bloquer le paquet
  - le laisser passer
  - le transmettre (forward)
  - …

---

## Chaînes iptables

- chaîne : ensemble de règles qui indiquent ce qu'il faut faire des paquets qui la traversent.
  - règle : combinaison de critères de matching et une cible du paquet.
- 3 chaînes principales pour filtrer :
  - `INPUT` : paquets à destination du système,
  - `OUTPUT` : paquets émis par le système,
  - `FORWARD` : paquets à transmettre.

---

## Algorithme

- `Netfilter` applique la 1e règle qui match le paquet
- …jusqu'à trouver une règle
- sinon politique par défaut

---

## Tables principales

- `filter` : table principale pour intervenir sur les paquets et analyser leur contenu : `DROP`, `ACCEPT`, …
- `conntrack` : composant et table rendant `Netfilter` _stateful_ (suit le cycle de vie de la connexion)

---

- Voir aussi la [wikiversité][wiki-netfilter]
- Tutoriel complet : <https://www.inetdoc.net/guides/iptables-tutorial/>
- Tutoriel sur `Conntrack` : <https://www.malekal.com/conntrack-sur-linux-comment-ca-marche/>

---

<!-- Annexe: liste des liens utiles -->
[wiki-netfilter]: https://fr.wikibooks.org/wiki/Administration_r%C3%A9seau_sous_Linux/Netfilter

# Legal

- Linux est une marque déposée par Linus Torvalds aux États Unis et dans d'autres pays.
- Red Hat Linux et Red Hat Enterprise Linux sont des marques déposées par RedHat Inc.
- Mandriva® Linux® est une marque déposée par Mandriva Inc.
- SUSE™ (SUSE est une marque de SUSE LINUX Products GmbH, une filiale de Novell)
- UNIX® est une marque déposée de The Open Group. 
- Other names may be trademarks of their respective owners

