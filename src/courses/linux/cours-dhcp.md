---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: DHCP
layout: '@layouts/CoursePartLayout.astro'
---

- 🎯 But du serveur DHCP (`dhcpd`) : distribuer des adresses IP dynamiquement ou statiquement, aussi bien en IPv4 qu'en IPv6
- Parfois simplement dans un rôle d'agent relais.

---

### 📁 Fichiers et journaux importants

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

### 🔧 Exemple de configuration : `/etc/dhcp/dhcpd.conf`

#### ✅ Déclaration globale

```conf
default-lease-time 600;
max-lease-time 7200;
authoritative;
```

#### 🧭 Configuration d'un sous-réseau

```conf
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8, 1.1.1.1;
  option domain-name "exemple.local";
}
```

#### 📌 Attribution fixe par adresse MAC

```conf
host imprimante {
  hardware ethernet 00:11:22:33:44:55;
  fixed-address 192.168.1.10;
}
```

---

### 📡 BOOTP

BOOTP est un prédécesseur de DHCP, encore pris en charge pour compatibilité :

```conf
allow bootp;
```

---

### 🌍 DHCPv6 et `radvd`

* DHCPv6 nécessite `dhcpd` compilé avec le support IPv6.
* Pour la configuration automatique sans état (stateless), on utilise `radvd`.

Exemple `radvd.conf` :

```conf
interface eth0 {
  AdvSendAdvert on;
  prefix 2001:db8:1::/64 {
    AdvOnLink on;
    AdvAutonomous on;
  };
};
```

---

### 🔁 Agent relais DHCP

Pour relayer les requêtes DHCP vers un autre serveur :

* Utilitaire : `dhcrelay`
* Exemple :

```sh
dhcrelay -i eth0 -i eth1 192.168.1.1
```

---

### 🧪 Vérifications & maintenance

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

