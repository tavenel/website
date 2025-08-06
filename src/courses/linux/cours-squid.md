---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Squid Proxy
layout: '@layouts/CoursePartLayout.astro'
---

- _Squid_ est un serveur mandataire (proxy) et de cache pour HTTP open-source.
- Toutes les requêtes sont gérées en un seul processus d'entrée/sortie asynchrone.
- Principales configurations :
  - `acl` : définir des conditions d'accès (IP, ports, méthode, URL…) ;
  - `http_access` : autoriser ou refuser en fonction des ACL ;
  - `http_port` (défaut `3128`) : peut être changé ou dupliqué (ex: SSL Bump ou proxy transparent) ;
  - Paramètres de performances : cache, log, ports, etc.

---

## 🧱 Listes de contrôle d'accès (ACL)

Les **ACL** définissent des conditions. Par exemple :

```
# squid.conf

acl reseau_local src 192.168.0.0/16
acl heures_travail time MTWHF 08:00-18:00
acl sites_bloques dstdomain .facebook.com .youtube.com
```

### ➕ Couplées avec `http_access`

```
# squid.conf

http_access deny sites_bloques
http_access allow reseau_local heures_travail
http_access deny all
```

:::warn
L'ordre est **important** : Squid lit les règles de haut en bas.
:::

---

### 🧪 Exemples de configuration

#### Bloquer les téléchargements :

```ini
# squid.conf

acl interdits urlpath_regex \.mp3$ \.mp4$ \.exe$
http_access deny interdits
```

#### Rediriger les utilisateurs vers une page d'erreur :

```ini
# squid.conf

deny_info http://intranet/interdit.html interdits
```

---

## 🔐 Authentification des utilisateurs

---

### Méthode basique avec fichiers

```ini
# squid.conf

auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic realm Proxy Squid
acl utilisateurs_ldap proxy_auth REQUIRED
http_access allow utilisateurs_ldap
```

:::tip
Nécessite de créer le fichier de mots de passe : `htpasswd -c /etc/squid/passwd utilisateur1`
:::

---

### Digest (authentification chiffrée HTTP)

Contrairement à Basic (en clair), **Digest** chiffre le mot de passe avec un hash MD5.

```ini
# squid.conf

auth_param digest program /usr/lib/squid/digest_file_auth -c /etc/squid/passwd.digest
auth_param digest realm MonProxy
acl utilisateurs proxy_auth REQUIRED
http_access allow utilisateurs
```

:::tip
Nécessite de générer le fichier avec `htdigest`.
:::

---

### PAM

```ini
# squid.conf

auth_param basic program /usr/lib/squid/basic_pam_auth
auth_param basic realm "Proxy PAM"
acl utilisateurs proxy_auth REQUIRED
http_access allow utilisateurs
```

:::tip
Requiert un service PAM `squid` dans `/etc/pam.d/squid`.
:::

---


### LDAP ou Active Directory

```ini
# squid.conf

auth_param basic program /usr/lib/squid/basic_ldap_auth -b "dc=exemple,dc=local" -D "cn=admin,dc=exemple,dc=local" -w "motdepasse" -f "uid=%s" -h ldap.exemple.local
auth_param basic realm "Proxy LDAP"
acl utilisateurs proxy_auth REQUIRED
http_access allow utilisateurs
```

---

### NTLM / Kerberos (SSO Active Directory)

- Permet l'authentification **transparente** (SSO) avec des machines intégrées à un domaine Windows (invisible pour l'utilisateur) ;
- Plus complexe à mettre en place.

```ini
# squid.conf

auth_param ntlm program /usr/bin/ntlm_auth --helper-protocol=squid-2.5-ntlmssp
auth_param ntlm children 10
acl utilisateurs proxy_auth REQUIRED
http_access allow utilisateurs
```

---

## 📈 Suivi des performances

- Squid permet de gérer des logs dédiés.
- Outils d'analyse : **SARG**, **Lightsquid**, **SquidAnalyzer**.

```ini
# squid.conf

access_log /var/log/squid/access.log
cache_log /var/log/squid/cache.log
```

---

