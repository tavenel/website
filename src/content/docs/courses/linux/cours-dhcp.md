---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: DHCP
type: cours
sidebar:
  order: 13
description: DHCP
---
- 🎯 But du serveur DHCP (`dhcpd`) : distribuer des adresses IP dynamiquement ou statiquement, aussi bien en IPv4 qu'en IPv6
- Parfois simplement dans un rôle d'agent relais.

:::link
Pour plus d'information, voir le document de la formation LPIC-2 :

- [DHCP Configuration](https://lpic2book.github.io/src/lpic2.210.1/)
:::

---

## 📁 Fichiers et journaux importants

| Fichier / Outil                            | Description                                               |
| ------------------------------------------ | --------------------------------------------------------- |
| `/etc/dhcp/dhcpd.conf`                     | Fichier principal de configuration DHCP                   |
| `/var/lib/dhcp/dhcpd.leases`               | Historique des baux d'adresses IP allouées                |
| `dhcpd`                                    | Démon serveur DHCP                                        |
| `systemctl status dhcpd`                   | Vérifier l'état du service DHCP                           |
| `/var/log/syslog` ou `journalctl -u dhcpd` | Journaux DHCP                                             |
| `radvd`                                    | Démon pour l'annonce de routeurs IPv6                     |
| `/etc/radvd.conf`                          | Configuration de `radvd`                                  |
| `arp`                                      | Permet de vérifier les adresses MAC actives sur le réseau |

---

## 🔧 Exemple de configuration : `/etc/dhcp/dhcpd.conf`

### ✅ Déclaration globale

```
# Paramètres des baux
default-lease-time 600;
max-lease-time 7200;

# Seul serveur DHCP dans le subnet : refuse IPs invalides
authoritative;
```

### 🧩 Configuration des services

```
# DNS
option domain-name-servers 21.31.0.2;
# SMTP
option smtp-server 21.31.0.3;
# POP3
option pop-server 21.31.0.4;
# NEWS
option nntp-server 21.31.0.5;
# NTP
option time-servers 21.31.0.6;

# ou par nom de domaine

# DNS
option domain-name-servers dns.company.com;
# SMTP
option smtp-server smtp.company.com;
# POP3
option pop-server pop3.company.com;
# NEWS
option nntp-server news.company.com;
# NTP
option time-servers ntp.company.com;
```

### 🧭 Configuration d'un sous-réseau

```
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8, 1.1.1.1;
  option domain-name "exemple.local";
}
```

### 🧭 Configuration de réseau partagé

```
# Réseau physique
shared-network mon-reseau {

  # Paramètres communs à tous les subnets
  option routers 21.31.17.1;
  option lpr-servers 21.31.17.2, 21.31.18.2, 21.31.19.2, 21.31.18.3;
  option broadcast-address 21.31.31.255;

  subnet 21.31.17.0 netmask 255.255.240.0 {
    range 21.31.17.11 21.31.17.210;
  }
  subnet 21.31.18.0 netmask 255.255.240.0 {
    range 21.31.18.11 21.31.18.210;
  }
}
```

### 📌 Attribution fixe par adresse MAC

```
group {
  # Options communes à tous les `host`
  option routers 21.31.55.1;
  option lpr-servers 21.31.56.3;
  option broadcast-address 21.31.63.255;
  netmask 255.255.240.0;

  host luke {
    # specifique à luke
    hardware ethernet AA:88:54:72:7F:92;
    fixed-address 21.31.55.211;
    option host-name "luke";
  }

  host leah {
    # specifique à leah
    hardware ethernet CC:88:54:72:84:4F;
    fixed-address 21.31.55.212;
    option host-name "leah";
  }
}
```

---

## 📡 BOOTP

BOOTP est un prédécesseur de DHCP, encore pris en charge pour compatibilité.

---

## 🌍 DHCPv6 et `radvd`

* DHCPv6 nécessite `dhcpd` compilé avec le support IPv6.
* Pour la configuration automatique sans état (stateless), on utilise `radvd`.

Exemple `radvd.conf` :

```
interface eth0 {
  AdvSendAdvert on;
  MinRtrAdvInterval 3; 
  MaxRtrAdvInterval 10;
  prefix 2001:db8:1::/64 {
    AdvOnLink on;
    AdvAutonomous on;
    AdvRouterAddr on;
  };
};
```

---

## 🔁 Agent relais DHCP

Pour relayer les requêtes DHCP vers un autre serveur :

* Utilitaire : `dhcrelay`
* Exemple :

```sh
dhcrelay -i eth0 -i eth1 192.168.1.1
```

---

## 🧪 Vérifications & maintenance

* Afficher les baux actifs :

```sh
cat /var/lib/dhcp/dhcpd.leases
```

* Redémarrer le service :

```sh
systemctl restart isc-dhcp-server
```

* Voir les logs :

```sh
journalctl -u isc-dhcp-server
```

---

