---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Apache
layout: '@layouts/CoursePartLayout.astro'
---

_Apache_ (ou _httpd_) est l'un des serveurs web les plus utilisés au monde. Il est libre, open-source, robuste, extensible, et largement supporté sur les systèmes Unix/Linux.

:::link
Pour plus d'information, voir le document de la formation LPIC-2 :

- [Basic Apache Configuration](https://lpic2book.github.io/src/lpic2.208.1/)
- [Apache configuration for HTTPS](https://lpic2book.github.io/src/lpic2.208.2/)
:::

## 📁 Fichiers et chemins importants

| Fichier/Dossier                 | Rôle                         |
| ------------------------------- | ---------------------------- |
| `/etc/apache2/apache2.conf`     | Fichier principal (Debian)   |
| `/etc/httpd/conf/httpd.conf`    | Fichier principal (Red Hat)  |
| `/etc/apache2/sites-available/` | Hôtes virtuels (Debian)      |
| `/var/www/html/`                | Répertoire racine par défaut |
| `/var/log/apache2/access.log`   | Journal des accès            |
| `/var/log/apache2/error.log`    | Journal des erreurs          |
| `apache2`                       | Service Apache (Debian)      |
| `httpd`                         | Service Apache (Red Hat)     |

---

## 🌐 Configuration des hôtes virtuels (Virtual Hosts)

```apache
Listen 80
<VirtualHost *:80>
    DocumentRoot "/www/example1"
    ServerName www.example.com

    # Other directives here
</VirtualHost>

<VirtualHost *:80>
    DocumentRoot "/www/example2"
    ServerName www.example.org

    <Directory /var/www/exemple2>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/exemple_error.log
    CustomLog ${APACHE_LOG_DIR}/exemple_access.log combined
</VirtualHost>
```

:::tip
Activer un site (Debian) :

```sh
a2ensite exemple.conf && systemctl reload apache2
```
:::

:::link
Voir la documentation : <https://httpd.apache.org/docs/2.4/vhosts/examples.html>
:::

---

## 🔐 Authentification utilisateur via `.htaccess` (`mod_auth_basic`)

```apache
AuthType Basic
AuthName "Accès restreint"
AuthUserFile /etc/apache2/.htpasswd
AuthGroupFile "/www/passwords/group.file"
Require group admins
```

:::tip
```sh
htpasswd -c /etc/apache2/.htpasswd alice
```

Nécessite `AllowOverride AuthConfig` dans la configuration du `<Directory>`.
:::

:::link
Voir la documentation : <https://httpd.apache.org/docs/current/howto/htaccess.html>
:::

---

## ⚙️ Modules de script (`PHP`, `mod_perl`, `mod_wsgi`)

### `PHP`

```sh
apt install libapache2-mod-php
a2enmod php
systemctl reload apache2
```

### `mod_perl`

```sh
apt install libapache2-mod-perl2
```

### `mod_wsgi` (Python)

```sh
apt install libapache2-mod-wsgi-py3
a2enmod wsgi
systemctl restart apache2
```

---

## 📉 Contrôle des ressources

Ajout dans `apache2.conf` ou dans un hôte virtuel :

```apache
<IfModule mpm_prefork_module>
    StartServers          5
    MinSpareServers       5
    MaxSpareServers      10
    MaxRequestWorkers    150
    MaxConnectionsPerChild 1000
</IfModule>
```

:::link
Voir la documentation : <https://httpd.apache.org/docs/2.4/mod/prefork.html>
:::

---

## 🚫 Restriction d'accès

### Exemple : Limiter à un sous-réseau :

```apache
<Directory /var/www/exemple>
    Require ip 192.168.0.0/24
</Directory>
```

### Avec `mod_authz_host` :

```apache
Require host .exemple.com
```

:::link
Voir la documentation :

- <https://httpd.apache.org/docs/2.4/howto/access.html>
- <https://httpd.apache.org/docs/2.4/mod/mod_authz_host.html>
:::

---

## 🔁 Redirections et réécritures

### Redirection simple avec `mod_alias` :

```apache
Redirect /ancien http://www.exemple.com/nouveau
```

### Avec `mod_rewrite` :

```apache
RewriteEngine On
RewriteRule ^ancien$ /nouveau [R=301,L]
```

:::link
Voir la documentation :

- <https://httpd.apache.org/docs/2.4/rewrite/remapping.html>
- <https://httpd.apache.org/docs/2.4/mod/mod_alias.html>
:::

---

## 📈 Surveillance

```sh
apachectl -S         # Affiche les hôtes virtuels
apachectl configtest # Vérifie la configuration
systemctl status apache2
tail -f /var/log/apache2/access.log
```

### Désactiver les modules non nécessaires

```sh
apache2ctl -M # Lister les modules
sudo a2dismod module_name
sudo systemctl restart apache2
```

---

## 🔐 HTTPS

```apache {6:9}
<VirtualHost *:443>
    ServerName www.exemple.org

    DocumentRoot /var/www/exemple

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/exemple.crt
    SSLCertificateKeyFile /etc/ssl/private/exemple.key
    SSLCertificateChainFile /etc/ssl/certs/intermediate.crt

    <Directory "/var/www/exemple">
        Require all granted
    </Directory>
</VirtualHost>
```

---

### 📁 Emplacements typiques des certificats :

| Type de fichier      | Exemple de chemin                 |
| -------------------- | --------------------------------- |
| Clé privée           | `/etc/ssl/private/mon-site.key`   |
| Certificat           | `/etc/ssl/certs/mon-site.crt`     |
| Chaîne intermédiaire | `/etc/ssl/certs/intermediate.crt` |
| Certificat CA        | `/etc/ssl/certs/ca-bundle.crt`    |

---

### 🔒 Renforcement de la sécurité SSL/TLS

```apache
# default-ssl.conf

# Algorithmes de chiffrement robustes
SSLProtocol all -SSLv2 -SSLv3 -TLSv1 -TLSv1.1
SSLCipherSuite HIGH:!aNULL:!MD5:!3DES
SSLHonorCipherOrder on

# Attaque CRIME
SSLCompression off

# Obfuscation du serveur
ServerTokens ProductOnly
ServerSignature Off
```

:::link
Voir la documentation :

- <https://httpd.apache.org/docs/current/mod/mod_ssl.html>
- <https://httpd.apache.org/docs/2.4/mod/core.html>
:::

---

### 🔐 Génération d'une CSR (Certificate Signing Request)

À envoyer à une autorité de certification commerciale (CA) :

```sh
openssl req -new -newkey rsa:2048 -nodes -keyout domaine.key -out domaine.csr
```

:::tip
Générer un certificat "self-signed" pour test :

```sh
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/selfsigned.key \
  -out /etc/ssl/certs/selfsigned.crt
```

- `-x509` : auto-signé
- `-nodes` : pas de passphrase ("no DES")
- `-days` : durée de validité
- `-newkey rsa:2048` : création de la clé RSA
:::

---

### 🌐 SNI : Server Name Indication

Permet d'héberger plusieurs sites HTTPS avec **une seule IP** :

```apache
<VirtualHost *:443>
    ServerName site1.exemple.org
    SSLCertificateFile /etc/ssl/certs/site1.crt
    SSLCertificateKeyFile /etc/ssl/private/site1.key
</VirtualHost>

<VirtualHost *:443>
    ServerName site2.exemple.org
    SSLCertificateFile /etc/ssl/certs/site2.crt
    SSLCertificateKeyFile /etc/ssl/private/site2.key
</VirtualHost>
```

---

## Autres paramètres de sécurité

```apache
# HSTS
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"

# Headers sécurisés
Header set X-Content-Type-Options "nosniff"
Header set X-Frame-Options "SAMEORIGIN"
Header set X-XSS-Protection "1; mode=block"
Header set Referrer-Policy "no-referrer-when-downgrade"
Header set Content-Security-Policy "default-src 'self';"

# Pas de listing ou d'accès aux répertoires
<Directory /var/www/html>
    Options -Indexes
    AllowOverride None
    Require all granted
</Directory>

# Ne pas exposer les fichiers cachés (.git, .htaccess)
<FilesMatch "^\.">
    Require all denied
</FilesMatch>
```

:::link
Pour plus d'information, voir aussi : <https://infosecwriteups.com/strengthening-web-service-security-with-apache2-best-practices-for-2025-32cb57eb7fd2>
:::

---

