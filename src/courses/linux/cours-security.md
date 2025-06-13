---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Sécurité
layout: '@layouts/CoursePartLayout.astro'
---

# Tâches d’administration de sécurité et configuration de la sécurité du système

![Run as an admin…](@assets/linux/run_as_admin.jpg)

<div class="caption">Run as an admin…</div>

---

## Exemples de thèmes de sécurité

- Limites utilisateurs pour les connexions, processus, utilisation mémoire : `usermod`, `ulimit`
- Mots de passe : `passwd`, `chage`
- Élévation de privilèges : `su`, `sudo`, `/etc/sudoers`
- Ports ouverts : `nmap`, `ss`
- Audit des fichiers avec permissions `suid` / `guid`
- Fichiers ouverts (et donc processus, ports, …) : `lsof`, `fuser`
- Monitorer et arrêter les services inutiles

---

## Mots de passe

- Rappel : `/etc/passwd` : fichier comptes utilisateurs (locaux)
- MDP dans fichier `/etc/shadow`
- Format :
  - `usename`
  - `hash` du MDP : `md5`, `sha256`, `sha512`, …
  - `last pass change` : # jours depuis 1970
  - `min pass age` : # jours avant de changer de MDP
  - `max pass age` : # jours MDP valide
  - `pass expiry warning` : # jours avant avertissement
  - `pass inactivity period` : # jours après expiration où le compte reste ouvert (MDP à changer)
  - `account expiration date`: date d'expiration du compte
  - dernier champ: réservé utilisation future

---

## TCP wrappers

- `/etc/hosts.allow` (`/etc/hosts.deny`): adresses IP autorisées (refusées) à se connecter aux services réseau sur le système.
- Si même IP dans `/etc/hosts.allow` et `/etc/hosts.deny` : **autorisé**
- Par défaut : autorisé
- Facile à usurper (changer d'IP)

```ini
sshd : 10.10.136.241
sshd : example.com
all : 1.2.3.4
```

---

## Démarrage dynamique de service depuis une socket

- Démarrage à la demande de services **uniquement** lorsque des connexions sont établies sur des sockets spécifiques.
- `xinetd` (historique) : `/etc/xinetd.conf` et scripts dans : `/etc/xinetd.d/`
- `systemd.socket` : configurations dans `/etc/systemd/system/` et services actifs dans `/etc/systemd/systemd/socket.target.wants/`

---

## `/etc/inittab`

- Configure le processus initial du système
- Définit les actions à exécuter lors de différents événements système : démarrage, changement de niveau d'exécution, …
  - inclus des restrictions d'accès
- Legacy : Obsolète si `systemd`

---

### Exemple

```
# /etc/inittab

::sysinit:/sbin/openrc sysinit
::sysinit:/sbin/openrc boot
::wait:/sbin/openrc default

# Set up a couple of getty's
tty1::respawn:/sbin/getty 38400 tty1
[...]
tty6::respawn:/sbin/getty 38400 tty6

# Put a getty on the serial port
#ttyS0::respawn:/sbin/getty -L 115200 ttyS0 vt100

# Stuff to do for the 3-finger salute
::ctrlaltdel:/sbin/reboot

# Stuff to do before rebooting
::shutdown:/sbin/openrc shutdown
```

---

Voir le [TP sur la sécurité d'un système Linux][tp-security]

---
 
# Sécurisation des données avec le chiffrement

---

## SSH

- Chiffrement symétrique ou (mieux) asymétrique (clé privée / clé publique)
- Peut encapsuler un autre protocole dans un tunnel (y compris `X11`)
- Supporte différents algorithmes : `RSA`, `DSA`, `RD25519`, …
  - Le "meilleur" est utilisé (supporté par le client et le serveur)
- `~/.ssh/id_rsa` (clé privée) et `~/.ssh/id_rsa.pub` (clé publique)
- `~/.ssh/authorized_keys` : clés publiques autorisées à ouvrir une connexion
- `~/.ssh/known_hosts` : IDs des machines distantes connues (pas besoin de revérifier)
- `fail2ban` permet de refuser des connexions

---

## GNU Privacy Guard (GPG)

- Sécurise les fichiers, les communications et les e-mails : protocole `OpenPGP`
  - Asymétrique
  - Chiffrement et Signature
  - Infrastructure à clé publique (PKI) : partage de clés publiques

---

Voir le [TP sur SSH et GPG][tp-ssh-gpg]

---

- Voir aussi [GTF0bins : exploits classiques sur Linux (tuto)](https://blog.stephane-robert.info/docs/securiser/menaces/gtfobins/)

<!-- Annexe : liste des TPs -->
[tp-security]: tp-security.md
[tp-ssh-gpg]: tp-ssh-gpg.md

---

