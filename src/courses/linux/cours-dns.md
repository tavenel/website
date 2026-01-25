---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Serveur de nom de domaine - DNS
layout: '@layouts/CoursePartLayout.astro'
---

## Configuration de base d'un serveur DNS

### 📁 Fichiers clés

- `/etc/bind/named.conf` : Fichier principal de configuration BIND.
- `/var/cache/bind/` : Répertoire par défaut des fichiers de zone.

:::tip
Les anciennes versions de bind utilisent plutôt `/etc/named.conf` et `/var/named`.
:::

:::link
Pour plus d'information, voir le document de la formation LPIC-2 :

- []()

Voir aussi le wiki Debian : <https://wiki.debian.org/Bind9>
:::

### ⚙️ Configuration basique

```
// /etc/bind/named.conf

options {
    directory "/var/cache/bind";
    recursion yes;
    allow-query { any; };
};

zone "example.com" {
        type master;
        file "/var/lib/bind/db.example.com";
};
```

### ⚙️ Configuration avancée

```
// /etc/bind/named.conf


// TSIG key used for the dynamic update
include "/etc/bind/ns-example-com_rndc-key";

// Configure the communication channel for Administrative BIND9 with rndc
// By default, they key is in the rndc.key file and is used by rndc and bind9
// on the localhost
controls {
        inet 127.0.0.1 port 953 allow { 127.0.0.1; };
};

options {

    // Répertoire de travail
    directory "/var/cache/bind";
  
    // Exchange port between DNS servers
    query-source address * port *;
  
    // Transmit requests to 192.168.1.1 if
    // this server doesn't know how to resolve them
    forward only;
    forwarders { 192.168.1.1; };

    auth-nxdomain no;    # conform to RFC1035


    // Listen on local interfaces only(IPV4)
    listen-on-v6 { none; };
    listen-on { 127.0.0.1; 192.168.0.1; };


    // Do not transfer the zone information to the secondary DNS
    allow-transfer { none; };
  
    // Accept requests for internal network only
    allow-query { internals; };
  
    // Allow recursive queries to the local hosts
    allow-recursion { internals; };
  
    // Do not make public version of BIND
    version none;

};

include "/etc/bind/named.conf.default-zones";

// prime the server with knowledge of the root servers
zone "." {
        type hint;
        file "/etc/bind/db.root";
};

zone "example.com" {
        type master;
        file "/var/lib/bind/db.example.com";
        allow-update { key rndc-key; };
};
zone "0.168.192.in-addr.arpa" {
        type master;
        file "/var/lib/bind/db.example.com.inv";
        allow-update { key rndc-key; };
};

logging {
        channel update_debug {
                file "/var/log/update_debug.log" versions 3 size 100k;
                severity debug;
                print-severity  yes;
                print-time      yes;
        };
       channel bind_log {
                file "/var/log/bind.log" versions 3 size 1m;
                severity info;
                print-category  yes;
                print-severity  yes;
                print-time      yes;
        };

        category default { bind_log; };
        category lame-servers { null; };
        category update { update_debug; };
        category update-security { update_debug; };
};
```

### 🔧 Commandes utiles

- `rndc reload` : Recharger la configuration.
- `named-checkconf` : Vérifier la validité de la configuration (`named.conf`).
- `dig`, `host` : Tester les requêtes DNS.

### 🔄 Alternatives à BIND

- `dnsmasq` : Léger, adapté aux petites installations.
- `djbdns` : Sécurité renforcée.
- `PowerDNS` : DNS moderne, backends multiples.

---

#### Exemple de configuration dnsmasq

```
# /etc/dnsmasq.conf

# Interface à utiliser (sinon toutes les interfaces du système)
interface=eth0

# Plage DHCP
dhcp-range=192.168.0.101,192.168.0.150,255.255.255.0,6h
# IPs statiques
dhcp-host=ab:cd:ef:12:34:56,example-host,192.168.0.10,infinite

# Si seul serveur DHCP : "serveur d'autorité". Permet d'accepter les renouvellement d'IPs fournies par un autre DHCP.
dhcp-authoritative

# Par défaut les IPs sont associées aux MAC (1 client retrouve la même adresse). Ce paramètre force un incrément (continuité des IPs)
dhcp-sequential-ip

# Nombre max de baux envoyés en parrallèle (défaut 1000)
dhcp-lease-max=100
```

```sh
# Test config
dnsmasq --test
# Activation et démarrage
sudo systemctl enable --now dnsmasq
```

Pour vérifier les baux DHCP (_"leases"_) fournies aux clients :

```sh
cat /var/lib/misc/dnsmasq.leases
```

---

## 🧭 Zone DNS

> Une **zone DNS** est une portion de l'espace de noms de domaine que l'on administre depuis un **serveur DNS** donné. Elle contient les enregistrements DNS (appelés _Resource Records_, ou `RR`) pour un ou plusieurs domaines.

- Une zone peut être :
  - **Directe (forward)** : nom → IP
  - **Inversée (reverse)** : IP → nom (via `in-addr.arpa`)
- Les fichiers de zone sont **définis dans `named.conf`** pour BIND.
- Une zone commence toujours par un enregistrement `SOA` (_Start of Authority_).
- Elle contient aussi des `NS`, `A`, `AAAA`, `CNAME`, `MX`, etc.

:::warn

- Une zone DNS **n'est pas forcément égale à un domaine** : un domaine peut être découpé en plusieurs zones, chacune gérée par un serveur différent.

:::

---

### 📁 Exemple de résolution de nom

Pour le domaine `exemple.com`, une zone peut contenir :

```text title="db.example.com"
;
; Ressource Record pour résolution de nom
;
$TTL    3600
@       IN      SOA     sid.example.com. root.example.com. (
                   2007010401           ; Serial
                         3600           ; Refresh [1h]
                          600           ; Retry   [10m]
                        86400           ; Expire  [1d]
                          600 )         ; Negative Cache TTL [1h]
;
@       IN      NS      sid.example.com.
@       IN      MX      10 sid.example.com.

sid     IN      A       192.168.0.1
etch    IN      A       192.168.0.2

pop     IN      CNAME   sid
www     IN      CNAME   sid
mail    IN      CNAME   sid
```

---

### 🔄 Exemple de résolution inverse

```text title="db.example.com.inv"
;
; Ressource Record pour résolution inverse
;
@       IN      SOA     sid.example.com. root.example.com. (
                   2007010401           ; Serial
                         3600           ; Refresh [1h]
                          600           ; Retry   [10m]
                        86400           ; Expire  [1d]
                          600 )         ; Negative Cache TTL [1h]
;
@       IN      NS      sid.example.com.

1       IN      PTR     sid.example.com.
2       IN      PTR     etch.example.com.
```

### 🛠️ Validation

- `named-checkzone exemple.local exemple.local.zone` : vérification de fichiers de zone
- `named-compilezone -o exemple.local.zone.db -f text exemple.local exemple.local.zone` : lecture de fichier de zone compilé en texte clair

---

## Sécurisation d'un serveur DNS

### 🧍 Exécution en tant qu'utilisateur non-root et dans un `chroot`

- Créer un environnement `chroot` (ex: `/var/named/chroot`). Un _chroot_ est un système de fichiers virtuel : le processus ne peut pas sortir du répertoire courant.
- Modifier `/etc/sysconfig/named` :

```sh
OPTIONS="-t /var/named/chroot -u named"
```

---

### 🔐 TSIG : Secure Zone Transfer

> **TSIG** (_Transaction SIGnature_) est un mécanisme d'**authentification** utilisé dans le protocole _DNS_ pour sécuriser les **transactions entre serveurs DNS** ou entre un client et un serveur DNS (notamment pour les mises à jour dynamiques). Il repose sur l'utilisation de **clés partagées et de signatures HMAC** pour garantir l'**authenticité** et l'**intégrité** des messages DNS.

TSIG est principalement utilisé pour :

- **Authentifier les mises à jour DNS dynamiques** (par exemple avec `nsupdate`)
- **Sécuriser les transferts de zones DNS** entre serveurs maîtres et esclaves
- **Empêcher les attaques de type spoofing ou falsification de données DNS**

---

#### Quand utiliser TSIG

Utiliser TSIG lorsque :

- vous devez **restreindre** qui peut modifier une zone,
- vous effectuez des **transferts de zone** (AXFR/IXFR),
- vous utilisez des **mises à jour dynamiques** (RFC 2136).

Cas typiques :

- synchronisation primaire ↔ secondaire,
- intégration DHCP → DNS (environnements dynamiques),
- automatisation (CI/CD, IaC) pilotant des zones DNS,
- infrastructures internes ou hybrides.

#### Limites de TSIG

- pas de scalabilité à grande échelle (gestion de clés partagées),
- pas adapté à des clients publics,
- ne protège pas la résolution DNS des utilisateurs.

---

#### ⚙️ Fonctionnement

1. **Clé partagée (TSIG key)** : Deux entités (serveurs DNS ou client/serveur) partagent une **clé secrète**.
2. **HMAC** : Lorsqu'un message DNS est envoyé, une **signature HMAC** (ex. HMAC-SHA256) est calculée avec cette clé et ajoutée au message DNS.
3. **Vérification** : Le destinataire utilise la même clé pour vérifier la signature. Si elle correspond, le message est authentifié.

:::warn

- TSIG **ne chiffre pas** les données DNS : il **authentifie** seulement l'origine et l'intégrité.
- Pour des besoins modernes et automatisés, certains systèmes remplacent _TSIG_ par des méthodes basées sur **TLS (_DoT_)** ou **HTTPS (_DoH_)**, mais TSIG reste courant dans les infrastructures internes.

:::

---

- Créer une clé :

```sh
tsig-keygen transfert-securise > tsig.key
```

- Ajouter dans `named.conf` :

```text ins={2-6,9,15}
// /etc/bind/named.conf

key transfert-securise {
    algorithm hmac-sha256;
    secret "base64clé==";
};

server 192.168.0.100 {
    keys { transfert-securise; };
};

zone "example.com" {
    type master;
    file "db.example.com";
    allow-transfer { key transfer-key; };
};
```

---

### 🔐 DNSSEC : Signature des zones

> **DNSSEC** (_Domain Name System Security Extensions_) est un ensemble d'extensions de sécurité pour le système DNS, qui a pour but de **garantir l'intégrité** et **l'authenticité** des données DNS. Il **ne chiffre pas** les données, mais il protège contre certaines attaques, comme :

- **Le spoofing DNS** (falsification de réponses DNS)
- **Le cache poisoning** (empoisonnement de cache DNS)

En effet, le DNS traditionnel ne vérifie pas si les réponses proviennent bien d'une source authentique. Un attaquant peut donc injecter de fausses réponses (ex : rediriger `www.banque.fr` vers un serveur malveillant).

**DNSSEC ajoute des signatures numériques aux enregistrements DNS** pour que le résolveur puisse vérifier qu'ils n'ont pas été modifiés.

#### ⚠️ Limitations et points de vigilance

- **Complexité de gestion** : renouvellement des clés, propagation des DS, …
- **Taille des réponses DNS** plus grande et peut poser problème avec certains pare-feux.
- **DNSSEC n'empêche pas l'écoute (pas de chiffrement)** : utiliser _DoT_/_DoH_ pour la confidentialité.

---

#### Quand utiliser DNSSEC

Utiliser DNSSEC lorsque :

- vous exploitez une **zone publique** (ex. domaine Internet),
- vous voulez garantir que les clients reçoivent des réponses DNS **non falsifiées**,
- vos utilisateurs dépendent de la **fiabilité des résolutions** (services exposés, e-commerce, APIs, etc.).

Cas typiques :

- serveurs DNS faisant autorité pour des domaines publics,
- environnements où la sécurité de la chaîne de résolution est critique,
- infrastructures soumises à des exigences de conformité ou de bonnes pratiques (ANSSI, RFC, etc.).

#### Quand DNSSEC n'est pas pertinent

- DNS interne sans validation côté résolveur,
- environnements fermés sans risque de falsification,
- besoin d'authentification ou de contrôle d'accès (ce n'est pas son rôle).

---

#### 🧠 Fonctionnement

##### Signatures cryptographiques

- Chaque enregistrement DNS (`A`, `MX`, `TXT`, …) est signé numériquement à l'aide d'une **clé privée**. Le résolveur utilise la **clé publique** pour vérifier la signature.
- **ZSK** (Zone Signing Key) : signe les enregistrements DNS d'une zone.
- **KSK** (Key Signing Key) : signe la ZSK pour établir une chaîne de confiance.

##### Chaîne de confiance

Chaque zone signe sa propre clé, et la clé publique est **déclarée dans la zone parente** (via un **DS record**). Exemple :

- `. (root)` ➜ signe la clé publique de `.fr`
- `.fr` ➜ signe celle de `banque.fr`
- `banque.fr` ➜ signe ses enregistrements

Le résolveur peut ainsi **remonter la chaîne jusqu'à la racine** pour vérifier l'authenticité.

##### Enregistrements DNS spécifiques à DNSSEC

| Type d'enregistrement | Rôle                                            |
| --------------------- | ----------------------------------------------- |
| **RRSIG**             | Contient la signature des enregistrements       |
| **DNSKEY**            | Clé publique (ZSK/KSK)                          |
| **DS**                | Lien de confiance vers la clé d'une zone enfant |
| **NSEC / NSEC3**      | Prouve qu'un nom n'existe pas (anti-forgery)    |

---

##### Commandes

- Générer les clés :

```sh
dnssec-keygen -a RSASHA256 -b 2048 -n ZONE exemple.local.
```

- Signer la zone :

```sh
dnssec-signzone -o exemple.local exemple.local.zone ZSK
```

---

### 📌 DANE

> **DANE** (_DNS-based Authentication of Named Entities_) est un protocole qui permet d'associer un certificat _TLS_ à un enregistrement DNS sécurisé via _DNSSEC_.

---

Traditionnellement, les certificats TLS sont validés via une **chaîne de confiance de l'autorité de certification (CA)**.
Avec **DANE**, on peut **publier le certificat ou son empreinte directement dans le DNS**, signé par **DNSSEC**.

Cela permet :

- De **protéger contre les certificats frauduleux ou compromis**
- De **se passer totalement des autorités de certification** (modèle "CA-less")
- Ou de **renforcer leur validation** (authentification multiple)

---

#### 🔧 Fonctionnement

DANE utilise un **enregistrement DNS de type `TLSA`**, associé à un service TLS (ex : _HTTPS_, _SMTP_, _XMPP_, …).

:::warn

- **DNSSEC doit être activé et fonctionnel**
- Tous les résolveurs DNS intermédiaires doivent **supporter DNSSEC**
- Les **clients/serveurs** doivent être **compatibles** avec DANE (ex : Postfix, Exim, OpenSSL avec libunbound)

:::

:::tip
Dane fonctionne même avec des certificats auto-signés (si publiés dans DNSSEC).
:::

##### 🔑 Exemple d'enregistrement TLSA

```
_443._tcp.exemple.com. IN TLSA (
  0 0 1 d2abde240d7cd3ee6b4b28c54df034b721ed3c5e0c2ff2c9c8d1d6cd53b6d23b
)
```

Ce champ indique :

- **Port 443**, **protocole TCP**, **nom de domaine**
- Le **certificat attendu** (empreinte du cert ou de la CA)
- Les 3 premiers chiffres (`3 1 1`) précisent le mode d'utilisation :

| Champ | Signification                                                |
| ----- | ------------------------------------------------------------ |
| 3     | Mode : certificat à valider doit correspondre **exactement** |
| 1     | Sélecteur : **certificat de l'entité** (pas de la CA)        |
| 1     | Association : **empreinte SHA-256** du certificat            |

---

#### Usages

- _SMTP_ avec _STARTTLS_ : _DANE_ est très utilisé pour sécuriser la communication entre serveurs de messagerie. Il empêche :
  - Le **downgrade d'un STARTTLS** en SMTP non chiffré
  - La **falsification de certificats TLS** (attaque _MITM_)
- HTTPS : plus rare aujourd'hui (remplacé plutôt par **CAA + CT logs**), mais possible : publication de son certificat TLS dans DNS pour contourner les CAs.
- XMPP / SIP / LDAP over TLS : tous les protocoles basés sur TLS peuvent théoriquement tirer parti de DANE.

---

### 🔍 Outils de vérification et de debug

- `dig +dnssec www.exemple.local`
- `host -t tlsa _443._tcp.exemple.local`
- `journalctl -u named`

Pour forcer la libération d'une _"lease"_ DHCP côté client :

```sh
dhcpcd -k
dhclient -r
```

---

## DNSSEC vs TSIG

| Critère               | DNSSEC                      | TSIG                       |
| --------------------- | --------------------------- | -------------------------- |
| Type de sécurité      | Cryptographique asymétrique | Cryptographique symétrique |
| Protège quoi          | Réponses DNS                | Transactions DNS           |
| Authentifie           | Les données                 | Les serveurs               |
| Cas d'usage principal | Résolution fiable           | Administration DNS         |
| Public / privé        | Public principalement       | Privé / interne            |
| Chiffrement           | Non                         | Non                        |

---

## Utilisation conjointe

DNSSEC et TSIG sont **complémentaires** et souvent utilisés ensemble :

- **TSIG** pour sécuriser :

  - transferts de zone,
  - mises à jour dynamiques,
  - relations maître/esclave.

> Je veux contrôler qui peut modifier ou synchroniser mes zones

- **DNSSEC** pour garantir :

  - la validité des réponses servies aux clients.

> Je veux garantir que les réponses DNS ne sont pas falsifiées

---

## 🔗 Liens

:::link
Pour plus d'information, voir le document de la formation LPIC-2 :

- [Basic DNS server configuration](https://lpic2book.github.io/src/lpic2.207.1/)
- [Create and maintain DNS zones](https://lpic2book.github.io/src/lpic2.207.2/)
- [Securing a DNS Server](https://lpic2book.github.io/src/lpic2.207.3/)

:::

---
