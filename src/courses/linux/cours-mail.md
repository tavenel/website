---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Serveurs de Mails
layout: '@layouts/CoursePartLayout.astro'
---

## 🧠 Protocole SMTP

- **SMTP (Simple Mail Transfer Protocol)** est utilisé pour **envoyer** des emails (port 25, 465 (smtps), ou 587 (submission)).
- Fonctionne selon un modèle **push**, de MTA (Mail Transfer Agent) à MTA.
- Utilise des commandes comme `HELO`, `MAIL FROM`, `RCPT TO`, `DATA`.
- 📬 Postfix : serveur mail le plus courant
- 🔹 Sendmail :
  - Historique, complexe à configurer, encore utilisé dans certains environnements.
  - Utilise `/etc/mail/sendmail.cf`, généré depuis un `.mc`.
- 🔸 Exim :
  - Plus simple que Sendmail, très modulaire.
  - Fichier principal : `/etc/exim/exim.conf`

---

## 📬 Serveur Postfix

### 📁 Répertoires et fichiers importants

- `/etc/postfix/main.cf` : Fichier principal de configuration
- `/etc/postfix/master.cf` : Contrôle des services postfix
- `/var/spool/postfix/` : Files d’attente de mails
- `/etc/aliases` : Fichier d’alias utilisateur
- `/var/log/mail.log` (ou `/var/log/maillog` selon distro) : logs d'envoi, réception et erreurs.

### 🔍 Commandes utiles

```sh
mailq            # Voir la file d'attente des mails
postfix flush    # Forcer l'envoi des mails en file
postfix reload   # Recharger la configuration
postsuper -d ALL # Vider la file d’attente
```

---

### 🔧 Configuration minimale

```ini
# main.cf

myhostname = mail.exemple.com
mydomain = exemple.com
myorigin = $mydomain
inet_interfaces = all
mydestination = $myhostname, localhost.$mydomain, localhost
mynetworks = 127.0.0.0/8
relay_domains = $mydestination
home_mailbox = Maildir/
```

:::link
Pour plus d'information, voir : <https://www.postfix.org/BASIC_CONFIGURATION_README.html>
:::

---

### 🔐 TLS

```ini
# main.cf

smtpd_tls_cert_file = /etc/ssl/certs/mail.crt
smtpd_tls_key_file = /etc/ssl/private/mail.key
smtp_tls_security_level = may # STARTTLS
```

:::warn
Vérifier le port TLS (465 ou 587 dans `master.cf`).
:::

:::link
Pour plus d'information, voir : <https://www.postfix.org/TLS_README.html>
:::

---

## 📨 Domaines virtuels

Permet de gérer plusieurs domaines sur le même serveur.

```ini
# main.cf

myhostname = main_domain.com
virtual_mailbox_domains = exemple.com, autre.com
virtual_mailbox_base = /var/mail/vhosts
virtual_mailbox_maps = hash:/etc/postfix/vmailbox
virtual_alias_maps = hash:/etc/postfix/virtual
```

```
# /etc/postfix/vmailbox

user1@main_domain.com    user1/
user2@exemple.com    user2/
```

```
# /etc/postfix/virtual

forward_to_user1@exemple.com user1@main_domain.com
forward_to_user2@exemple.com user2@exemple.com
forward_to_everybody@exemple.com user1@main_domain.com,user2@exemple.com
```

---

## 🔁 Relais sortant de messagerie

```ini
# main.cf

relayhost = [smtp.relais.fr]:587
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = static:relayuser:relaypassword
# ou
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_tls_security_level = encrypt
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
```

```
# /etc/postfix/sasl_passwd

[smtp.relais.fr]:587    user:password
```

---

## ✉️ Alias de messagerie

```
# /etc/aliases

# alias: destination_address
root: admin # system account
contact: jean, pierre
```

📌 Recompiler avec : `newaliases`

---

## Filtrage et tri du courrier

### 🧠 Sieve

Langage déclaratif **côté serveur** conçu pour **trier automatiquement les e-mails** sur les serveurs IMAP (via _Dovecot_, _Cyrus_, …).

#### Commandes et actions

| Action     | Description                                     |
| ---------- | ----------------------------------------------- |
| `keep`     | Conserver dans la boîte de réception par défaut |
| `fileinto` | Déplacer dans un dossier spécifique             |
| `redirect` | Rediriger le mail vers une autre adresse        |
| `reject`   | Refuser le mail avec une erreur                 |
| `discard`  | Supprimer silencieusement                       |
| `stop`     | Arrêter l’évaluation du script                  |

#### Conditions

- `if address`
- `if header`
- `if size`
- `if allof`
- `if anyof`
- …

---

```
require ["fileinto", "vacation"];

if address :is "From" "newsletter@exemple.com" {
  fileinto "Newsletters";
  stop;
}

if size :over 5M {
  discard;
}

vacation
  :days 7
  :subject "Absent"
  "Je suis actuellement en congé et je répondrai à mon retour.";
```

---

### 🧙 Procmail

- Outil de filtrage de mails basé sur `.procmailrc` ;
- Fonctionne avec les _MDA_ (Mail Delivery Agents) ;
- Ancien, moins lisible que Sieve, mais toujours utilisé.

```sh
# .procmailrc

MAILDIR=$HOME/Mail
DEFAULT=$MAILDIR/inbox

:0:
* ^From.*boss@example.com
work
```

---

## 🧠 Protocoles IMAP vs POP3


| Protocole | Comportement                                           | Utilisation recommandée       |
| --------- | ------------------------------------------------------ | ----------------------------- |
| IMAP      | Messages stockés sur le serveur, accès distant complet | Appareils multiples           |
| POP3      | Messages téléchargés localement, souvent supprimés     | Connexion ponctuelle, offline |

---

## ⚙️ Dovecot

- Serveur mail open-source pour Linux
- `doveconf` : Affiche la configuration effective
- `doveadm` : Outil d'administration (sessions, tests)

```sh
doveadm who
doveadm auth test user@example.com password
```

```ini
# /etc/dovecot/dovecot.conf

# Start new configs with the latest Dovecot version numbers here:
dovecot_config_version = 2.4.0
dovecot_storage_version = 2.4.0

# Enable wanted protocols:
protocols {
  imap = yes
  lmtp = yes
}

mail_home = /srv/mail/%{user}
mail_driver = sdbox
mail_path = ~/mail

mail_uid = vmail
mail_gid = vmail

# By default first_valid_uid is 500. If your vmail user's UID is smaller,
# you need to modify this:
#first_valid_uid = uid-number-of-vmail-user

namespace inbox {
  inbox = yes
  separator = /
}

# Authenticate as system users:
passdb pam {
}

# Preferred permissions: root:root 0444
ssl_server_cert_file = /etc/dovecot/ssl-cert.pem
# Preferred permissions: root:root 0400
ssl_server_key_file = /etc/dovecot/ssl-key.pem
```

:::link
Voir la documentation : <https://doc.dovecot.org/main/core/config/quick.html>
:::

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

### 🧩 Intégrations

#### Sieve

- _Dovecot_ doit être configuré en [LDA](https://doc.dovecot.org/main/core/config/delivery/lda.html) ou [LMTP](https://doc.dovecot.org/main/core/config/delivery/lmtp.html) :

```ini
protocol lda {
  mail_plugins {
    sieve = yes
  }
}

protocol lmtp {
  mail_plugins {
    sieve = yes
  }
}
```

:::link
Voir la documentation : <https://doc.dovecot.org/main/core/plugins/sieve.html#sieve-plugin-sieve>
:::

#### ✉️ Répondeur automatique : extension `vacation`

```ini
# Use vacation-seconds
sieve_extensions {
  vacation-seconds = yes
}

# One hour at minimum
sieve_vacation_min_period = 1h

# Ten days default
sieve_vacation_default_period = 10d

# Thirty days at maximum
sieve_vacation_max_period = 30d
```

```
vacation
  :days 1
  :addresses ["toto@example.com"]
  :subject "Absent du bureau"
  "Je répondrai à votre message dès mon retour.";
```

:::link
Voir la documentation : <https://doc.dovecot.org/main/core/config/sieve/extensions/vacation.html#sieve-vacation-extension>
:::

---

## 📨 Alternative : Courier

* Moins utilisé aujourd’hui ;
* Utilise `imapd`, `pop3d`, fichiers séparés ;
* Configuration dans `/etc/courier/` (ex: `imapd`, `pop3d`, `authdaemonrc`).

---

