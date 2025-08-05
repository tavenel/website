---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Serveur de nom de domaine - DNS
layout: '@layouts/CoursePartLayout.astro'
---

## Configuration de base d'un serveur DNS

### 📁 Fichiers clés

- `/etc/named.conf` : Fichier principal de configuration BIND.
- `/var/named/` : Répertoire par défaut des fichiers de zone.

### ⚙️ Configuration basique dans `/etc/named.conf`

```conf
options {
    directory "/var/named";
    recursion yes;
    allow-query { any; };
};

zone "exemple.local" IN {
    type master;
    file "exemple.local.zone";
};
```

### 🔧 Commandes utiles

- `rndc reload` : Recharger la configuration.
- `named-checkconf` : Vérifier la validité de la configuration.
- `kill -HUP $(pidof named)` : Relancer le démon (peu recommandé).
- `dig`, `host` : Tester les requêtes DNS.

### 🔄 Alternatives à BIND

- `dnsmasq` : Léger, adapté aux petites installations.
- `djbdns` : Sécurité renforcée.
- `PowerDNS` : DNS moderne, backends multiples.

---

## 🧭 Zone DNS

> Une **zone DNS** est une portion de l'espace de noms de domaine que l'on administre depuis un **serveur DNS** donné. Elle contient les enregistrements DNS (appelés *Resource Records*, ou `RR`) pour un ou plusieurs domaines.

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

### 📁 Exemple de zone

Pour le domaine `exemple.com`, une zone peut contenir :

```dns
$TTL 86400
@   IN  SOA ns1.exemple.com. admin.exemple.com. (
        2025080501 ; Serial
        3600       ; Refresh
        1800       ; Retry
        604800     ; Expire
        86400 )    ; Minimum

    IN  NS  ns1.exemple.com.
    IN  NS  ns2.exemple.com.

@   IN  A   192.0.2.10
www IN  A   192.0.2.11
mail IN  A   192.0.2.12
@   IN  MX  10 mail.exemple.com.
```

---


### 🧾 Exemple de fichier de zone (`exemple.local.zone`)

```zone
$TTL 86400
@   IN  SOA ns1.exemple.local. admin.exemple.local. (
        2025080501 ; Serial
        3600       ; Refresh
        1800       ; Retry
        604800     ; Expire
        86400 )    ; Minimum TTL

    IN  NS      ns1.exemple.local.
    IN  A       192.168.0.10
ns1 IN  A       192.168.0.10
www IN  A       192.168.0.20
```

### 🔄 Zone inverse (`0.168.192.in-addr.arpa.zone`)

```zone
$TTL 86400
@   IN  SOA ns1.exemple.local. admin.exemple.local. (
        2025080501 ; Serial
        3600       ; Refresh
        1800       ; Retry
        604800     ; Expire
        86400 )    ; Minimum TTL

    IN  NS  ns1.exemple.local.
10  IN  PTR ns1.exemple.local.
20  IN  PTR www.exemple.local.
```

### 🛠️ Validation

- `named-checkzone exemple.local exemple.local.zone`
- `named-compilezone -o exemple.local.zone.db -f text exemple.local exemple.local.zone`

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

* **Authentifier les mises à jour DNS dynamiques** (par exemple avec `nsupdate`)
* **Sécuriser les transferts de zones DNS** entre serveurs maîtres et esclaves
* **Empêcher les attaques de type spoofing ou falsification de données DNS**

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

```conf
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

#### ⚠️ Limitations et points de vigilance :

- **Complexité de gestion** : renouvellement des clés, propagation des DS, …
- **Taille des réponses DNS** plus grande et peut poser problème avec certains pare-feux.
- **DNSSEC n'empêche pas l'écoute (pas de chiffrement)** : utiliser _DoT_/_DoH_ pour la confidentialité.

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
dnssec-keygen -a RSASHA256 -b 2048 -n ZONE exemple.local
```

- Signer la zone :

```sh
dnssec-signzone -o exemple.local -k KSK exemple.local.zone ZSK
```

---

### 📌 DANE

> **DANE** (_DNS-based Authentication of Named Entities_) est un protocole qui permet d'associer un certificat _TLS_ à un enregistrement DNS sécurisé via _DNSSEC_.

---

Traditionnellement, les certificats TLS sont validés via une **chaîne de confiance de l'autorité de certification (CA)**.
Avec **DANE**, on peut **publier le certificat ou son empreinte directement dans le DNS**, signé par **DNSSEC**.

👉 Cela permet :

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
_443._tcp.exemple.com. IN TLSA 3 1 1 (
  d2abde240d7cd3ee6b4b28c54df034b721ed3c5e0c2ff2c9c8d1d6cd53b6d23b
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

---

