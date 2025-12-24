---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: LDAPS
layout: '@layouts/CoursePartLayout.astro'
---

## LDAPS : LDAP sécurisé

### Serveur

#### Certificat

LDAPS nécessite un certificat SSL/TLS valide. Vous pouvez utiliser un certificat d'une autorité de certification (CA) de confiance ou générer un certificat auto-signé à des fins de test.

##### Certificat auto-signé

```bash
sudo apt install openssl
sudo openssl req -new -x509 -nodes -days 365 -keyout /etc/ssl/private/ldap.key -out /etc/ssl/certs/ldap.crt
sudo chmod 600 /etc/ssl/private/ldap.key
sudo chown openldap:openldap /etc/ssl/private/ldap.key
```

- `CN` doit être le nom du serveur ou son adresse IP

---

#### Configurations

```ini
# /etc/default/slapd
SLAPD_SERVICES="ldap:/// ldapi:/// ldaps:///"
```

Ou pour forcer LDAPS uniquement :

```ini
# /etc/default/slapd
SLAPD_SERVICES="ldapi:/// ldaps:///"
```

```ini
# /etc/ldap/ldap.conf
TLS_CACERT /etc/ssl/certs/ldap.crt
TLS_REQCERT allow
```

- `TLS_REQCERT allow` accepte les certificats "self-signed" (utiliser `demand` pour un certificat validé par un CA en production).

```bash
sudo systemctl restart slapd
```

Vérification du service slapd :

```bash
sudo ss -tulnp | grep 636
```

---

### Client

```ini
# /etc/nslcd.conf
uri ldaps://ldap_server_ip/
base dc=example,dc=com
tls_reqcert allow
```

```ini
# /etc/ldap/ldap.conf
TLS_CACERT /etc/ssl/certs/ldap.crt
TLS_REQCERT allow
```

```bash
sudo systemctl restart nslcd
```

---

### Test LDAPS

```bash
ldapsearch -x -H ldaps://ldap_server_ip -b "dc=example,dc=com"
```

```bash
getent passwd alice
```

```bash
su - testuser
```

```bash
ssh testuser@localhost
```

---

### Troubleshooting

Logs des services :

```bash
journalctl -u slapd
journalctl -u nslcd
```

"Trust" du Certificat :

```bash
openssl s_client -connect ldap_server_ip:636 -showcerts
```

Pare-feu :

```bash
sudo ufw allow 636/tcp
```

---
