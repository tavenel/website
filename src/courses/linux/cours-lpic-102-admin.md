---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Administration système Linux
layout: '@layouts/CoursePartLayout.astro'
---

# Sujet 107 : Tâches d’administration

---

## 107.1 Gestion des comptes utilisateurs et des groupes ainsi que des fichiers systèmes concernés [5]

---

### Utilisateurs

- `useradd` : crée un utilisateur
- `userdel` : supprime un utilisateur
- `usermod` : modifie un utilisateur
  - `usermod --append --groups group1,group2,... username`
- `/etc/passwd` : fichier comptes utilisateurs (locaux)
- `/etc/skel/` : squelette copié dans le `home` d'un nouvel utilisateur

---

### Mots de passe

- `/etc/shadow` : fichier mots de passe (comptes locaux)
- `passwd` : changer un mot de passe
- `chage` : change l'expiration d'un mot de passe

---

### Groupes

- `/etc/group` : fichier groupes et utilisateurs rattachés
- `groupadd` : crée un groupe
- `groupdel` : supprime un groupe
- `groupmod` : modifie un groupe
  - `groupmod --new-name new_group group_name`

---

### getent

- `getent` : affiche les infos d'une BDD Unix (`passwd`, `shadow`, `group`, …)
  - fichiers locaux + services externes : `NIS`, `LDAP`, …
  - `getent group docker`

---
 
## 107.2 Automatisation des tâches d’administration par la planification des travaux [4]

---

### `at`

- programme 1 exécution unique
- `echo "il est sept heures et demi" | at 0730`

---

### `cron`

- Service historique de planification
  - éxécution répétée de tâches
- Service `cron.d` (`/etc/cron.d/`)
- `/etc/crontab` : format de description des récurrences
  - très réutilisé dans d'autres programmes
  - commande `crontab -l` et `crontab -e`
- `/etc/cron.{daily/,hourly/,monthly/,weekly/}` contiennent des scripts à exécuter chaque jour, heure, mois, semaine

---

### `systemd`

- `systemd timer units` : fichiers de configuration `systemd` pour planifier et exécuter des tâches périodiques
- gestion des dépendances, intégration aux services `systemd`, …

---

Voir le [tp sur les tâches planifiées (cron)][tp-cron]

---

## 107.3 Paramètres régionaux et langues [3]

---

### Normes encodage

- `ASCII` : codage de base (anglais) ;
- `ISO-8859` : extension pour d'autres langues européennes ;
- `Unicode` : pour représenter tous les caractères de toutes les langues du monde ;
- `UTF-8`, `UTF-16` : encodages flexibles compatibles `Unicode` et `ASCII`.
- `iconv -f ASCII -t UTF-8 input.txt > output.txt`

---

### Langue

- variable `LANG` : langage utilisée par les programmes
- exemple: `LANG=fr_FR.UTF-8`
- `LANG=C` : force `ASCII` et Anglais
  - tri `ASCII` : `fichier9` > `fichier10`
  - dates : `MM/DD/YYYY` (vs. européen : `DD/MM/YYYY`)
  - utile dans script Shell pour éviter un comportement aléatoire

---

### _Locale_

- variables `LC_*` : gèrent les _locale_ à utiliser
- `LC_ADDRESS` ,`LC_COLLATE` ,`LC_CTYPE` ,`LC_IDENTIFICATION` ,`LC_MEASUREMENT` ,`LC_MESSAGES` ,`LC_MONETARY` ,`LC_NAME` ,`LC_NUMERIC` ,`LC_PAPER` ,`LC_TELEPHONE` ,`LC_TIME`
  - exemple : `LC_TIME=fr_FR.UTF-8`
  - `LC_ALL` : surcharge tous les autres `LC_*` si définie
- commande: `locale`

---

Voir le [tp dédié aux langues][tp-lang].

---
 
# Sujet 108 : Services systèmes essentiels

---

## 108.1 Gestion de l’horloge système [3]

---

### Temps universel

- `date` : affichage / gestion date et heure
- Heure _UNIX_ : nombre de secondes écoulées depuis le 1er janvier 1970
- Convention UNIX : stocker l'heure `UTC` (Temps Universel Coordonné)

---

### Timezone

- Modifie l'heure affichée par un fuseau horaire : `Europe/Paris`, …
- `/etc/timezone` ou `/etc/localtime`
- timezones disponibles dans: `/usr/share/zoneinfo/`
- commande: `tzselect`
- ou variable `TZ` : `export TZ='Europe/Paris'`
- ou (Debian/Ubuntu) : `sudo dpkg-reconfigure tzdata`

---

### Hardware clock

- `hwclock` : affichage / gestion horloge matérielle
- `hwclock --systohc` : synchronisation horloge système vers matérielle

---

### Synchronisation réseau

- Réseau => besoin de cohérence des horloges (journalisation, sécurité, …)
- `Network Time Protocol` (`NTP`) : synchronisation des horloges depuis des serveurs de temps fiables
  - hiérarchie pyramidale : strate 0 (horloges atomiques ou GPS) puis synchronisation strate 1, … , 15
  - algorithmes puissants : retard réseau, …
- Dæmons de synchronisation :
  - `ntpd` : `/etc/ntp.conf`, commande `ntpdate`
  - `chrony` : `/etc/chrony.conf`, commande `chronyc`

---

### Serveurs de temps de référence

- Europe Time Servers : <europe.pool.ntp.org> : pool communautaire Europe
- Stratum-1 servers : <pool.ntp.org> : pool communautaire monde
- NIST Time Servers : <time.nist.gov>
- US Naval Observatory : <ntp.usno.navy.mil>

---

### systemd : timedatectl

- `timedatectl` : affichage date et heure
- `timedatectl set-timezone Europe/Paris`
- `timedatectl set-ntp true`
- `timedatectl timesync-status`
- `timedatectl set-time`

---
 
## 108.2 Journaux systèmes [4]

---

### Rappel : logs système

- Voir le TP [tp-systeme][tp-systeme] pour les rappels sur les logs système.

---

### Rappel systemd

- Voir le cours et le TP sur `systemd` dans la partie LPIC-101 :
- Commandes dédiées : `systemctl`, `journalctl`
- Voir le TP [tp-sysv-systemd][tp-sysv-systemd].
- `/etc/systemd/journald.conf`

---

### Syslog

- Protocole client/serveur de journaux d'événements :
  - client : envoi d'informations (UDP 514 ou TCP)
  - serveur : collecte centralisée et création des journaux
  - solution de journalisation standard sur Unix, périphériques réseau (commutateurs, routeurs), disponible sous Windows
- fichiers par défaut : `/var/log/syslog`
- implémentations : `syslog`, `rsyslog`, `syslog-ng`

---

Voir le [TP sur les journaux][tp-syslog].

---
 
## 108.3 Bases sur l’agent de transfert de courrier (MTA) [3]

---

### SMTP(S)

- `Simple Mail Transfer Protocol` : envoi d'e-mail (protocole ultra majoritaire) :
  1. expéditeur
  2. destinataires
  3. transfert du corps du message
- TCP 25 / implicite:465 / explicite:587

---

### Mail Transfert Agent (SMTP)

- `sendmail`, `postfix`, `exim`
- Possibilité d'envoyer des mails aux comptes locaux

---

### Mail User Agent

- Programmes clients de lecteur/envoi de mails : `Thunderbird`, `mail`, …

```sh
$ mail -s "Maintenance fail" henry@lab3.campus <<<"The maintenance script failed at `date`"
```

---

### Transfert de courriers

```sh
$ cat ~/.forward
emma@lab1.campus
```

---

Voir le [TP sur SMTP][tp-smtp].

---
 
## 108.4 Gestion des imprimantes et de l’impression [2]

---

### Common Unix Printing System (CUPS)

1. L'utilisateur soumet un fichier pour impression.
2. Le dæmon `cupsd` dépile le job d'impression (numéro de job, queue d'impression, nom du document).
3. `CUPS` utilise des filtres installés sur le système pour générer un fichier au format utilisable par l'imprimante.
4. `CUPS` envoie le fichier re-formatté à l'imprimante

- `/etc/cups/cupsd.conf`
- Interface héritée de `lpd` (`lpadmin`, `lpinfo`, `lpoptions`, `lpr`, `lpstat`, `lp`, …)

---

<!-- Annexe : liste des TPs -->

[tp-systemd]: tp-systemd.md

[tp-ligne-commande]: tp-ligne-commande.md
[tp-systeme]: tp-systeme.md
[tp-grub]: tp-grub.md
[tp-shared-lib]: tp-shared-lib.md
[tp-rpm-apt]: tp-rpm-apt.md
[tp-texte]: tp-texte.md
[tp-fichiers]: tp-fichiers.md
[tp-redirections]: tp-redirections.md
[tp-process]: tp-process.md
[tp-fichiers-avance]: tp-fichiers-avance.md
[tp-partitions]: tp-partitions.md
[tp-cron]: tp-cron.md
[tp-lang]: tp-lang.md
[tp-smtp]: /cours/cloud/exo-smtp.md
[tp-syslog]: tp-syslog.md
[tp-network]: tp-network.md
[tp-security]: tp-security.md
[tp-ssh-gpg]: tp-ssh-gpg.md

