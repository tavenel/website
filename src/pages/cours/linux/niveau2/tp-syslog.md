---
title: Journalisation - Syslog
date: 2024 / 2025
correction: false
---

## Syslog

Syslog est la solution de journalisation standard sur Unix, et est également disponible sur de nombreux périphériques réseau (commutateurs, routeurs) et d'autres OS (Windows, …)

Il s'agit d'un protocole et d'une implémentation (programme `syslog`).

Le protocole définit des échanges client/serveur de journaux d'événements :

- client : envoi d'informations (UDP 514 ou TCP)
- serveur : collecte centralisée et création des journaux

### Format Syslog

Un journal au format Syslog comporte dans l’ordre les informations suivantes :

- la date à laquelle a été émis le log,
- le nom de l’équipement ayant généré le log (`hostname`),
- une information sur le processus qui a déclenché cette émission,
- le niveau de gravité du log,
- un identifiant du processus ayant généré le log
- et enfin un corps de message.

Certaines de ces informations sont optionnelles.

Par exemple :

```log
Sep 14 14:09:09 machine_de_test dhcp service[warning] 110 corps du message
```

Les origines peuvent être multiples et sont juxtaposées à l’aide d’un `;`

Elles sont construites sous la forme :

```
facility.criticity
```

- La gravité (`criticity`) doit être comprise comme la criticité minimale, ainsi `user.critical` correspond au message d’origine utilisateur pour le niveau de gravité critical et les niveaux supérieurs, en l'occurrence `alert` et `emergency`.
- Le mot-clef `none` peut lui aussi être utilisé afin de filtrer les messages, il est alors utilisé en lieu et place de la gravité.

### Niveaux de gravité

| N  | Niveau        | Signification                               |
|----|---------------|---------------------------------------------|
| 0  | Emerg         | Système inutilisable                        |
| 1  | Alert         | Une intervention immédiate est nécessaire   |
| 2  | Crit          | Erreur critique pour le système             |
| 3  | Err           | Erreur de fonctionnement                    |
| 4  | Warning       | Avertissement                               |
| 5  | Notice        | Événement normal méritant d’être signalé    |
| 6  | Informational | Pour information seulement                  |
| 7  | Debug         | Déboggage                                   |

### Origine

Les messages sont aussi orientés au regard de leur origine, dont les codes sont regroupés suivant des types que l’on appelle des “facilités”, soit l’origine, de `local0` à `local7` à personnaliser. On peut trouver :

| Facilité        | Origine                                           |
|-----------------|---------------------------------------------------|
| AUTH            | Message de sécurité/autorisation                  |
| AUTHPRIV        | Message de sécurité/autorisation (privé)          |
| CRON            | Message d'un démon horaire                        |
| DAEMON          | Démon du système sans classification particulière |
| FTP             | Démon ftp                                         |
| KERN            | Message du noyau                                  |
| LOCAL0 à LOCAL7 | Réservé pour des utilisations locales             |
| LPR             | Message du sous-système d'impression              |
| MAIL            | Message du sous-système de courrier               |
| NEWS            | Message du sous-système des news USENET           |
| SYSLOG          | Message interne de syslogd                        |
| USER (défaut)   | Message utilisateur générique                     |
| UUCP            | Message du sous-système UUCP                      |

### Fichiers de logs

```
/var/log/syslog
```

:::tip
Attention à la place que peuvent mettre les logs : mettre en place une rotation !

- Voir `logrotate`
- Voir le TP sur les tâches planifiées (cron)
:::

### rsyslog et syslog-ng

Bien que `syslog` soit le démon de journalisation standard, `rsyslog` et `syslog-ng` sont généralement préférés pour leur extensibilité, leurs performances améliorées et leurs fonctionnalités avancées de gestion des journaux. `rsyslog` est souvent choisi pour sa facilité d'utilisation et son support actif, tandis que `syslog-ng` est privilégié pour ses fonctionnalités avancées et son haut niveau d'extensibilité.

`syslog`, `rsyslog` et `syslog-ng` suivent tous le protocole `Syslog` (et peuvent être mélangés en client/serveur).

| Fonctionnalité           | syslog           | rsyslog                            | syslog-ng                                     |
|--------------------------|------------------|------------------------------------|-----------------------------------------------|
| Gestion des journaux     | Standard         | Implémentation avancée             | Implémentation avancée                        |
| Configuration            | /etc/syslog.conf | /etc/rsyslog.conf                  | /etc/syslog-ng/syslog-ng.conf                 |
| Extensibilité            | Limitée          | Hautement extensible               | Très extensible                               |
| Optimisé Performances    | NON              | OUI                                | OUI                                           |
| Fonctionnalités avancées | Basiques         | Filtrage dynamique, réplication, … | Filtrage, traitement et stockage avancés      |
| Support actif            | NON              | OUI                                | OUI                                           |

#### Forwarding rsyslog

La configuration de `rsyslog.conf` supporte l'envoi de logs vers un serveur central.

Côté serveur :

```
# Provides UDP syslog reception
$ModLoad imudp
$UDPServerRun 514

# Provides TCP syslog reception
$ModLoad imtcp
$InputTCPServerRun 514
```

Côté client :

```
*.*  action(type="omfwd" target="192.0.2.2" port="514" protocol="tcp"
            action.resumeRetryCount="100"
            queue.type="linkedList" queue.size="10000")
```

:::link
Voir aussi [cette page rsyslog](https://www.rsyslog.com/sending-messages-to-a-remote-syslog-server/).
:::

#### Envoi de mails

Il est possible d'utiliser un serveur `SMTP` `mail.example.com` pour envoyer les journaux par mail :

```
$ActionMailSMTPServer mail.example.com
$ActionMailFrom rsyslog@example.com
$ActionMailTo recipient@example.com

*.err;*.crit        :ommail:mail.example.com
```

### logger

La commande `logger` permet d'écrire facilement un message de l'utilisateur dans le fichier `/var/log/syslog`.

```sh
logger -p err "Un message d'erreur"
```

### Exercice rsyslog

:::exo
1. Installer le package `rsyslog` et vérifier le démarrage du service `rsyslog`.
2. En utilisant le fichier de configuration de rsyslog, rediriger les messages de journalisation de niveau : 
  - `err` et `crit` dans un fichier de journal appelé `errors.log`
  - `info` et `notice` dans un fichier de journal appelé `info.log`.
  - Assurez-vous que rsyslog est correctement redémarré après la modification de la configuration.
3. Vérifier que les règles de filtrage sont correctement appliquées en testant l'envoi de messages de différents niveaux de priorité et en vérifiant les fichiers de journal correspondants.
4. Configurer une règle de filtrage supplémentaire pour enregistrer les messages de journalisation provenant de l'installation du service `ssh` dans un fichier de journal distinct appelé `ssh.log`.
  - Assurez-vous que seuls les messages de journal relatifs au service `ssh` sont enregistrés dans ce fichier.
5. Envoyer les logs d'erreur sur un serveur distant (par exemple, utiliser le serveur de la 2e VM).
:::

:::correction

#### Installation de rsyslog

```sh
sudo apt install rsyslog
sudo systemctl status rsyslog
rsyslogd -v
```

#### Configuration de rsyslog

`/etc/rsyslog.d/01-exo.conf`

```
# Redirection des messages de niveau "err" et "crit" vers errors.log
*.err;*.crit    /var/log/errors.log

# Redirection des messages de niveau "info" et "notice" vers info.log
*.info;*.notice /var/log/info.log
```

Redémarrage du service :

```sh
sudo systemctl restart rsyslog
```

#### Tests

```sh
logger -p err "Ceci est un message d'erreur"
logger -p crit "Ceci est un message critique"
logger -p info "Ceci est un message d'information"
logger -p notice "Ceci est un message de notification"

cat /var/log/errors.log
cat /var/log/info.log
```

#### SSH

SSH est utilisé pour les sessions d'authorisation.

`/etc/rsyslog.d/02-ssh.conf`

```
# Redirection des messages du service SSH vers ssh.log
auth,authpriv.* /var/log/ssh.log
```

```sh
sudo systemctl restart rsyslog
cat /var/log/ssh.log
```

#### Remote

```
*.*  action(type="omfwd" target="192.0.2.2" port="10514" protocol="tcp"
            action.resumeRetryCount="100"
            queue.type="linkedList" queue.size="10000")
```
:::

## Rappels systemd-journald

`systemd` propose sa propre implémentation de journalisation (compatible avec `syslog`) nommée `journald` (service) et `journalctl` (commande).

Voir le TP [tp-systemd](tp-systemd.md) pour des rappels sur `journalctl`.

### systemd-cat

`systemd-cat` redirige la sortie d'un script vers le journal de `systemd` :

```sh
echo "Un message d'erreur" | systemd-cat -p err
```

:::tip
- `syslog` peut rediriger les messages de journalisation vers `systemd-journald` pour une journalisation centralisée ou pour une gestion des journaux centralisée.
- `systemd-journald` peut également envoyer des messages de journalisation à `syslog` pour une journalisation étendue ou pour un traitement spécifique des journaux.
- Les deux services peuvent coexister sur le même système et fonctionner simultanément. Cependant, il est recommandé de configurer correctement les règles de filtrage et de redirection pour éviter toute duplication ou conflit dans la gestion des journaux.
- En pratique, on utilise plutôt :
  - `rsyslog` ou `syslog-ng` seuls sur des systèmes sans `systemd`
  - `journald` seul pour un système simple utilisant `systemd`
  - `journald` en point d'entrée, redirigeant les logs vers un serveur `rsyslog` pour un post-traitement avancé.
:::

