---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Le réseau sous Linux
type: cours
sidebar:
  order: 11
description: Le réseau sous Linux
---
## Notions élémentaires sur les protocoles Internet

---

### IPv4/IPv6

- Rappels sur l'adressage IPv4/IPv6 :
  - [Cours LPI](https://learning.lpi.org/en/learning-materials/102-500/109/109.1/109.1_01/)
  - [Cours sur le site : "Le Web, HTTP, Introduction au Cloud, architectures client/serveur et types d'applications mobiles"](/web)
  - [Cours TCP/IP de François Goffinet](https://linux.goffinet.org/administration/configuration-du-reseau/introduction-a-tcp-ip/)
- Rappels sur les réseaux virtuels : 
  - <https://www.it-connect.fr/le-nat-et-le-pat-pour-les-debutants/>
  - <https://www.it-connect.fr/comprendre-les-differents-types-de-reseaux-de-vmware-workstation-pro/>
  - NAT vs BRIDGE : <https://blog.stephane-robert.info/docs/homelab/bridge-nat/>

---

### Quatre couches

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

### Ports par défaut

- Principaux services et ports par défaut sur TCP/IP : [voir le cours "Communication entre processus et applications client/serveur sur TCP/IP"](/web)
- `/etc/services` : principaux services

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

## Configuration du réseau

---

### Gestion dynamique des interfaces sans persistance

- `ifconfig` : ancienne commande
- `ip` : plus puissante, et sépare les couches et services
  - `ip link`, `ip addr`, `ip route`, …
- `ifup` et `ifdown` : gestion simplifiée
  - `/etc/network/interfaces`
  - ⚠️ `ifup` et `ifdown` ne sont pas standardisés :
    - `CentOS` : `/etc/sysconfig/network-scripts/` (un peu différent)
- `iw` : outil moderne pour interfaces réseau sans fil (`nl80211`) : information sur les interfaces Wi-Fi, gestion des connexions … ;
  - À coupler avec `wpa_supplicant` pour les connexions sécurisées.

---

### Persistance des configurations

- La configuration réseau sous Linux est réalisable de différentes façons.
- Elle dépend fortement du **contexte** : serveur vs poste de travail, serveur headless vs station nomade, distribution Linux utilisée.
- Plusieurs outils existent qui peuvent entrer en conflit (éviter de les mélanger).

---

### Méthode traditionnelle : `/etc/network/interfaces`

- Historiquement très utilisée sur Debian et dérivés
- Fichier `/etc/network/interfaces`
- Simple
- Facile à versionner pour serveur simple
- Peu adaptée aux environnements modernes multiplateformes (Wi-Fi, VPN, changement d'interface dynamique).
- Ne gère pas bien les événements dynamiques, changements d'interface

#### Utilisation

1. Ouvrir `/etc/network/interfaces`, éditer l'interface.
2. Relancer : `ifdown enp0s3 && ifup enp0s3` ou redémarrer le service `networking` (`systemd`, `rc-service`, …).

Exemple d'entrée pour une interface en DHCP ou statique :

```
# loopback
auto lo
iface lo inet loopback

# dhcp
auto enp3s5 # interface activée au démarrage (ou par `ifup -a`)
iface enp3s5 inet dhcp # `inet`, `ipx` ou `inet6`

# static
iface enp3s6 inet static
    address 192.168.1.2
    netmask 255.255.255.0 # ou directement : address 192.168.1.2/24
    gateway 192.168.1.1
    dns-nameservers 8.8.8.8 1.1.1.1 # optionnel
```

---

### systemd‑networkd

- `systemd-networkd` : service _systemd_
- Léger
- Gestion nette et déclarative des interfaces
  - Repertoire : `/etc/systemd/network/`
  - Fichiers avec extension `.network`, `.netdev`, `.link`
  - Compatible _legacy_ (`/etc/network/interfaces`)
- Très bien documenté, supporte VLAN, bridges, bonds, virtualisation.
- Moins orienté poste de travail (Wi-Fi, network-profiles, VPN)
- Souvent utilisé pour des serveurs, containers et environnements minimalistes

#### Utilisation

Exemple :

```ini
# /etc/systemd/network/05-eth0.network

[Match]
Name=eth0

[Network]
DHCP=no
Address=192.0.2.123/24
Gateway=192.0.2.1
DNS=203.0.113.1 203.0.113.2
IPv6AcceptRA=true
```

Ou en DHCP :

```
# /etc/systemd/network/20-dhcp.network

[Match]
Name=enp0s3

[Network]
DHCP=yes
```

```bash
systemctl enable --now systemd-networkd
systemctl restart systemd-networkd
```

---

### Netplan

- Surcouche introduite par Ubuntu Server
- Syntaxe simple YAML : facile à comprendre et versionner
  - `/etc/netplan/…`
- Utilise backend `networkd` ou `NetworkManager`
- Bien adapté aux distributions modernes qui souhaitent une configuration unifiée
- Moins de granularité que config "manuelle" : certains boutons "magiques" peuvent surprendre

#### Utilisation

Exemple :

```yaml
# /etc/netplan/01-static.yaml
network:
	version: 2
	ethernets:
		enp0s3:
			addresses:
				- 192.168.1.10/24
			gateway4: 192.168.1.1
			nameservers:
				addresses: [1.1.1.1, 8.8.8.8]
```

```bash
netplan try
netplan apply
```

---

### NetworkManager

- Configuration centrale du réseau : 1 seul outil
- Daemon réseau pensé pour les environnements "poste de travail"
- Excellent pour Wi-Fi, configuration VPN, passer d'un réseau à l'autre (portable), VPN
- Gestion des "profils" réseau, grande flexibilité
- Fortement utilisé sur Fedora, Ubuntu Desktop, …
- Lourd et incompatible avec autre outil

---

#### Utilisation

- Ligne de commande : `nmcli device show`, `nmcli connection up/down`
- Interface en mode texte : `nmtui`
- Interface graphique intégrée par défaut dans la plupart des environnements de bureau : Gnome, KDE, …
- Configuration manuelle possible via fichiers `.nmconnection` dans `/etc/NetworkManager/system-connections/`

Exemple de connexion Ethernet statique :

```bash
nmcli connection add type ethernet ifname enp0s3 con-name static-enp0s3 ipv4.addresses 192.168.1.20/24 ipv4.gateway 192.168.1.1 ipv4.dns 1.1.1.1 ipv4.method manual
nmcli connection up static-enp0s3
```

Exemple de connexion Wi-Fi avec WPA2 :

```bash
nmcli device wifi list
nmcli device wifi connect SSID-nom password motdepasse
```

---

### Recommandations

- Pour un **serveur de production** : privilégier `systemd-networkd` ou bien _Netplan_ avec backend `networkd`.
- Pour un environnement **desktop** ou **laptop** : `NetworkManager` est souvent le bon choix.
- Toujours désactiver les autres gestionnaires pour éviter les conflits (ex. ne pas avoir à la fois `systemd-networkd`` et `NetworkManager` gérant la même interface).
- Documenter la configuration (quel fichier fait quoi) pour l'équipe.

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

- `resolvectl query www.wikipedia.fr` : résolution DNS par `systemd-resolved`
- `nslookup www.wikipedia.fr` : résolution DNS
- `drill @8.8.8.8 www.wikipedia.fr` : résolution DNS en passant par le serveur DNS de Google (`8.8.8.8`)
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

### Vérifier le réseau

1. `ip addr show` : Adresse IP ?
2. `ping www.google.fr` : connectivité ?
3. `ip route` et `traceroute www.google.fr` : routage ?
4. `nslookup www.google.fr` ou `drill www.google.fr` et fichier `/etc/resolv.conf` : DNS ?

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

### 🧭 mtr : diagnostic réseau

`mtr` (My Traceroute) est un outil de diagnostic réseau combinant les fonctionnalités de `traceroute` et de `ping`.

- Il affiche la route réseau vers une destination (IP ou nom DNS)
- Il mesure les statistiques de latence et de perte de paquets pour chaque routeur (ou "saut")
- Il permet une analyse continue, utile pour détecter les problèmes intermittents

#### 🔍 Cas d'usage

- Identifier une latence ou une perte de paquets anormale
- Diagnostiquer des problèmes réseau intermittents
- Vérifier la qualité du chemin réseau entre deux hôtes

---

## Pare-feu : Netfilter/IpTables/NfTables

- `Netfilter` : module noyau pare-feu, traduction d'adresse (NAT) et historique réseau
- Intercepte et manipule les paquets IP **avant** et **après** le routage.
- `iptables` / `ip6tables` : commande de configuration de `Netfilter`.

```sh
iptables -P INPUT DROP
iptables -A OUTPUT -o eth0 -p tcp -s 192.168.1.2 -d 192.168.1.0/24 --dport 22 -j ACCEPT
```

:::tip
`iptables` est déprécié : préférer `nftables` (voir ci-dessous) mais les concepts sont les mêmes.
:::

---

### Modèle

- Les paquets passent à travers des chaînes qui vont déterminer ce que le système doit en faire
  - bloquer le paquet
  - le laisser passer
  - le transmettre (forward)
  - …

---

### Politiques principales

- Politiques principales (option `-j`) :
- **bloqué** en avertissant l'émetteur : `REJECT`
- **jeté** sans avertir l'émetteur : `DROP`
- **accepté** : `ACCEPT`
- **loggé** : `LOG`

---

### Chaînes iptables

- chaîne : ensemble de règles qui indiquent ce qu'il faut faire des paquets qui la traversent.
  - règle : combinaison de critères de matching et une cible du paquet.
- 3 chaînes principales pour filtrer (option `-A` (règle) ou `-P` (policy)) :
  - `INPUT` : paquets à destination du système,
  - `OUTPUT` : paquets émis par le système,
  - `FORWARD` : paquets à transmettre.

---

### Algorithme

- `Netfilter` applique la 1e règle qui match le paquet
- …jusqu'à trouver une règle
- sinon politique par défaut

---

### Tables principales

- `filter` : table principale pour intervenir sur les paquets et analyser leur contenu : `DROP`, `ACCEPT`, `FORWARD`, …
- `nat` : table dont le but est de faire de la _translation_ d'adresses (uniquement pour les nouvelles connexions)
- `conntrack` : composant et table rendant `Netfilter` _stateful_ (suit le cycle de vie de la connexion).

---

#### Exemples de règles :

1. Bloquer des connexions entrantes

```sh
iptables -A INPUT -s 192.168.2.1 -j DROP
```

2. Autoriser des connexions SSH entrantes (et utiliser CONNTRACK pour garder l'état des connexionx ouvertes) :

```sh
iptables -A INPUT -i eth0 -p tcp -s 192.168.1.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
```

---

### Nftables

- Remplaçant moderne de `iptables` pour _Netfilter_ (à privilégier).
- Fonctionnement similaire : _chaînes_ et _règles_
- Configuration unifiée IPv4 + IPv6
- Pas de chaîne de base (pas de `INPUT`, …)

:::tip
`iptables-translate` permet de transformer des règles `iptables` en `nftables`
:::

#### Exemples de règles :

1. Bloquer des connexions entrantes

```sh
nft add rule ip filter INPUT ip saddr 192.168.2.1 counter drop
```

2. Autoriser des connexions SSH entrantes (et utiliser CONNTRACK pour garder l'état des connexionx ouvertes) :

```sh
nft add rule ip filter INPUT iifname eth0 ip saddr 192.168.1.0/24 tcp dport 22 ct state new,established counter accept
```

---

### Autres pare-feux

Il existe aussi d'autres pare-feux populaires :

- _Uncomplicated Firewall_ : `ufw` (par défaut sous Ubuntu) qui est une autre sur-couche à `iptables`.
- `firewalld` (par défaut sous Fedora) qui est une interface de pare-feu dynamique sur `netfilter`.

---

# Ressources

:::note
- Pour des exemples de base de `iptables`, voir [la documentation Ubuntu](https://doc.ubuntu-fr.org/iptables)
- Voir aussi la [wikiversité](https://fr.wikibooks.org/wiki/Administration_r%C3%A9seau_sous_Linux/Netfilter)
- Tutoriel complet : <https://www.inetdoc.net/guides/iptables-tutorial/>
- Tutoriel sur `Conntrack` : <https://www.malekal.com/conntrack-sur-linux-comment-ca-marche/>
- Passer de `iptables` à `nftables` : <https://linuxhandbook.com/iptables-vs-nftables/>
- Voir aussi : <https://blog.stephane-robert.info/docs/admin-serveurs/linux/reseaux/> et <https://blog.stephane-robert.info/docs/admin-serveurs/linux/network/#les-outils-de-configuration-r%C3%A9seau-sous-linux>
- Voir le [TP sur la configuration du réseau sous Linux](/linux/tp-network)
- Pour UFW, voir : <https://blog.stephane-robert.info/docs/securiser/reseaux/ufw/>
- Pour Firewalld, voir : <https://blog.stephane-robert.info/docs/securiser/reseaux/firewalld/>
:::

---

