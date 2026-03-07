---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Tâches d'administration de sécurité et configuration de la sécurité du système
layout: '@layouts/CoursePartLayout.astro'
---


![Run as an admin…](@assets/linux/run_as_admin.jpg)

<div class="caption">Run as an admin…</div>

---

## Exemples de thèmes de sécurité

- Droits sur les fichiers : `rwx`, _ACL_
  - Audit des fichiers avec permissions `suid` / `guid`
- Limites utilisateurs pour les connexions, processus, utilisation mémoire : `usermod`, `ulimit`
- Mots de passe : `passwd`, `chage`
- Élévation de privilèges : `su`, `sudo`, `/etc/sudoers`
- Ports ouverts : `nmap`, `ss`
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

## Capabilities

- Objectif : accorder à un processus uniquement les "droits" dont il a besoin dans l'ensemble des droits de `root`.
- Très utile dans les conteneurs (_Docker_, _Kubernetes_)
- Par processus :
  - **Permitted (Prm)** : capabilities que le processus est autorisé à activer.
  - **Effective (Eff)** : capabilities actuellement actives.
  - **Inheritable (Inh)** : capabilities que le processus peut transmettre à ses enfants.
- Par fichier exécutable :
  - `getcap`, `setcap` : le processus hérite des capabilities du fichier exécutable (sans avoir besoin d'être `root`)

### Principales capabilities

- `CAP_NET_BIND_SERVICE` : utiliser ports < 1024.
- `CAP_SYS_ADMIN` : très large : montage de fichier systèmes, gestion de namespaces, …
- `CAP_NET_RAW` : manipulation directe de paquets (audits, `tcpdump`).
- `CAP_DAC_OVERRIDE` : ignorer les restrictions classiques d'accès aux fichiers.
- `CAP_SYS_TIME` : modifier l'horloge système.
- `CAP_SYS_PTRACE` : débogger (`strace`/`gdb`) d'autres processus.
- `CAP_CHOWN` : changer propriétaire/groupe de fichiers.

---

## Sécurisation des données avec le chiffrement

---

### SSH

- Chiffrement symétrique ou (mieux) asymétrique (clé privée / clé publique)
- Peut encapsuler un autre protocole dans un tunnel (y compris `X11`)
- Supporte différents algorithmes : `RSA`, `DSA`, `RD25519`, …
  - Le "meilleur" est utilisé (supporté par le client et le serveur)
- `~/.ssh/id_rsa` (clé privée) et `~/.ssh/id_rsa.pub` (clé publique)
- `~/.ssh/authorized_keys` : clés publiques autorisées à ouvrir une connexion
- `~/.ssh/known_hosts` : IDs des machines distantes connues (pas besoin de revérifier)
- `fail2ban` permet de refuser des connexions

---

### GNU Privacy Guard (GPG)

- Sécurise les fichiers, les communications et les e-mails : protocole `OpenPGP`
  - Asymétrique
  - Chiffrement et Signature
  - Infrastructure à clé publique (PKI) : partage de clés publiques

---

## Auditd

- Système d'audit du noyau Linux
- Objectifs :
  - Traçabilité des actions
  - Détection d'intrusions
  - Conformité (ISO 27001, PCI-DSS, etc.)
  - Investigation post-incident
- `auditd` (daemon), `auditctl` (CLI de configuration, volatil), `ausearch` & `aureport` (analyse des logs)

---

### Exemples d'usage

- Surveiller `/etc/shadow`
- Tracer `sudo`
- Détecter suppression de logs
- Audit des changements de permissions
- Audit des connexions root

---

#### Surveiller un fichier

Exemple : surveiller `/etc/passwd`

```bash
auditctl -w /etc/passwd -p wa -k passwd_changes
```

- `-w` : watch file
- `-p wa` : write + attribute change (au choix parmis `rwxa`)
- `-k` : mot-clé pour filtrer dans les logs

---

#### Surveiller un syscall

Exemple : tracer `execve`

```bash
auditctl -a always,exit -S execve -k exec_monitor
```

- `always,exit` : audit à la sortie du syscall
- `-S` : syscall ciblé
- Permet de voir **toutes les commandes exécutées**

---

### Consultation des logs

Logs : `/var/log/audit/audit.log`

```bash
ausearch -k passwd_changes
aureport
```

---

## DAC vs MAC

---

### 🔐 DAC : Discretionary Access Control

- Droits standards d'un système Unix :
- Le **propriétaire** d'un objet (fichier, dossier, processus, etc.) décide **qui peut y accéder** et avec quels droits.
- Basé sur les **utilisateurs, groupes et permissions** (rwx).
- Chaque utilisateur gère librement ses propres ressources.
- Le système se base sur l'**identité** de l'utilisateur pour autoriser l'accès.
- **Simple**

```bash
ls -l /home/user/file.txt
chmod 640 /home/user/file.txt
```

---

### 🛡️ MAC : Mandatory Access Control

- Les règles d'accès sont **définies par une politique centrale** et **imposées par le système**, pas par les utilisateurs.
- Basé sur des **étiquettes de sécurité** (_SELinux_, _AppArmor_)
- Chaque interaction (processus ↔ fichier, réseau, mémoire…) est évaluée selon la politique.
- Même le superutilisateur (`root`) ne peut pas ignorer la politique.
- **Complexe** mais **sécurité renforcée**

**Exemple :**
SELinux bloque un serveur web (`httpd_t`) qui tente d'accéder à `/home` même si les permissions Unix le permettent.

---

## 🧱 SELinux

- _Security-Enhanced Linux_
- Développé par la _NSA_
- Intégré nativement aux distributions RHEL : Fedora, CentOS, Rocky, Alma
- Basé sur le **LSM** : _Linux Security Modules_.
- Notions de **contexte de sécurité** : `user:role:type:level`.
- Modes :
  - **Enforcing** : les politiques sont appliquées.
  - **Permissive** : les violations sont enregistrées mais pas bloquées.
  - **Disabled** : désactivé.

---

### Targeted Policy

- Politiques ciblées :
- Démons système sensibles (`httpd`, `sshd`, `named`, `mysqld`, …) confinés :
  - domaines SELinux spécifiques avec règles précises (ex : `httpd_t`, `sshd_t`, `named_t`).
- Processus utilisateurs classiques et programmes standards non confinés :
  - domaine générique `unconfined_t`.
- Mode de politique par défaut sur la plupart des distributions Linux modernes
  - bon compromis sécurité vs compatibilité

---

D'autres politiques existent, par exemple :

- **mls** (Multi-Level Security) :
  - niveaux de classification : _Top Secret_, _Secret_, …
  - Environnements gouvernementaux ou militaires.
- **mcs** (Multi-Category Security) :
- variante simplifiée de MLS (catégories sans hiérarchie)
- conteneurs, environnements multi-utilisateurs.

---

### Commandes utiles

```bash
getenforce # Status
sestatus # Status
setenforce 0 # mode Permissive
```

- Vérifier les contextes incorrects : `ls -Z`
- Corriger avec `restorecon` ou `chcon`.
- Diagnostiquer via `ausearch` + `sealert`, audits dans `/var/log/audit/audit.log`
- Génération automatique : `audit2allow` et `semodule`
  - `audit2why` pour comprendre les blocages.

---

## 🧰 AppArmor

- Approche simplifiée du confinement
- Développé par **Immunix**, puis intégré à Ubuntu, Debian, SUSE.
- Fonctionne aussi via **LSM**
- Logique basée **chemins de fichiers** (et non étiquettes comme SELinux).
- Profils définissant ce qu'un programme peut faire :
  - Lecture, écriture, exécution, accès réseau.
  - Profils stockés dans `/etc/apparmor.d/`.
- Modes :
  - **Enforce** : profil appliqué.
  - **Complain** : enregistre les violations sans bloquer.

---

### Commandes utiles

```bash
aa-status
aa-enabled
aa-complain /etc/apparmor.d/usr.bin.firefox
aa-enforce /etc/apparmor.d/usr.sbin.nginx
aa-genprof nginx # Création de profile
aa-logprof # Génération automatique de profil depuis les logs
```

---

## Seccomp - Secure Computing Mode

- Problématique :
  - Les processus Linux disposent de centaines de _syscalls_ (appels système).
  - \+ de syscalls disponibles = \+ de surface d'attaque.
- Fonctionnalité du noyau Linux.
- Filtre les _syscalls_ (appels système) qu'un processus peut exécuter.
- Principe du **moindre privilège**.
- Peu d'impact sur la performance.
- Deux modes :
  - **Strict mode**
  - **Filter mode (BPF)**

---

### Mode Strict

- Mode historique, très limité.
- Autorise uniquement :
  - `read`
  - `write`
  - `exit`
  - `sigreturn`
- Tout autre syscall → **processus tué**.
- Trop restrictif pour la plupart des applications modernes.
- Rarement utilisé aujourd'hui.

---

### Mode Filter

- Utilise **BPF (Berkeley Packet Filter)**.
- Permet de définir des règles fines.
- Décisions possibles :
  - `ALLOW`
  - `KILL` (tue le processus)
  - `ERRNO` (erreur)
  - `TRACE`
  - `LOG`

---

- Très utilisé par :
  - Docker (bloque par défaut `kexec_load`, `delete_module`, `swapon`)
  - Kubernetes
  - Sandbox applicatives : _systemd_, navigateurs Web, …
- Politique typique :
  - Autoriser : `read`, `write`, `openat`, `close`
  - Refuser : `mount`, `ptrace`, `reboot`

---

## SELinux vs AppArmor vs Seccomp

| Caractéristique | SELinux                          | AppArmor                               | seccomp                                |
| --------------- | -------------------------------- | -------------------------------------- | -------------------------------------- |
| Basé sur        | Étiquettes (contexts)            | Chemins de fichiers                    | Appels système (syscalls)              |
| Difficulté      | Plus complexe                    | Plus simple                            | Simple à intermédiaire                 |
| Granularité     | Très fine                        | Moins précise                          | Très fine sur les appels noyau         |
| Adoption        | Red Hat, Fedora, CentOS          | Ubuntu, Debian                         | Large (Docker, Kubernetes, conteneurs) |
| Cas d'usage     | Data centers, serveurs sensibles | Postes utilisateurs, serveurs généraux | Sandboxing d'applications, conteneurs  |

---

## 📚 Ressources

:::link

- Voir le [TP sur SSH et GPG](/linux/tp-ssh-gpg)
- Voir le [TP sur la sécurité d'un système Linux](/linux/tp-security)
- Voir aussi [GTF0bins : exploits classiques sur Linux (tuto)](https://blog.stephane-robert.info/docs/securiser/menaces/gtfobins/)
- Voir la page sur les capabilities : <https://blog.stephane-robert.info/docs/admin-serveurs/linux/capabilities/>
- Documentation SELinux : <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/>
  - guide : <https://blog.stephane-robert.info/docs/securiser/durcissement/selinux/>
- Guide Ubuntu AppArmor : <https://ubuntu.com/server/docs/security-apparmor>
  - guide : <https://blog.stephane-robert.info/docs/securiser/durcissement/apparmor/>
- Voir le wiki Arch Linux : <https://wiki.archlinux.org/title/Security>

:::

---
