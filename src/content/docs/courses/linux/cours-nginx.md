---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Nginx
type: cours
sidebar:
  order: 16
description: Nginx
---
Nginx est un serveur HTTP rapide et léger. Il est souvent utilisé comme :

- **Serveur web** statique ou dynamique (avec plugins CGI/FastCGI)
- **Reverse Proxy** (et load balancing, SSL termination)
- **Serveur de cache**
- **Proxy pour d'autres protocoles (SMTP, IMAP)**

---

## 📁 Fichiers de configuration

| Fichier/Dossier               | Rôle                                           |
| ----------------------------- | ---------------------------------------------- |
| `/etc/nginx/nginx.conf`       | Fichier principal de config                    |
| `/etc/nginx/conf.d/`          | Contient des fichiers de conf. supplémentaires |
| `/etc/nginx/sites-available/` | Configuration des "sites" (optionnel)          |
| `/etc/nginx/sites-enabled/`   | Sites activés (via symlink)                    |
| `/var/www/html/`              | Racine web par défaut (attention aux droits) |


---

## 🌐 Serveur HTTP simple


```nginx
# /etc/nginx/conf.d/site.conf

server {
    listen 80;
    server_name www.exemple.local;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

---

## 🔁 Reverse Proxy

Reverse proxy agissant comme intermédiaire entre les clients et les applications vers un backend sur le port 8080.

```nginx
server {
    listen 80;
    server_name api.exemple.local;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

:::tip
Les directives `proxy_set_header` sont essentielles pour passer les bons en-têtes au backend.
:::

---

### 🔐 Avec TLS (HTTPS)

Utiliser _Certbot_ ou manuellement :

```nginx
server {
    listen 443 ssl;
    server_name monsite.local;

    ssl_certificate     /etc/ssl/certs/monsite.crt;
    ssl_certificate_key /etc/ssl/private/monsite.key;

    location / {
        proxy_pass http://localhost:8000;
    }
}
```

---

