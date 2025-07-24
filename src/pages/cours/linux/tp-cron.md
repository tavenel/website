---
title: TP Cron - Planification de tâches
date: 2024 / 2025
correction: false
---

Tâches planifiées

`at`, `cron` et `systemd` sont les programme Linux natifs qui permettent de planifier des tâches.

## Commande `at`

`at` est une commande Unix qui permet de programmer des commandes à n'exécuter qu'une fois - par opposition à `cron` - à un moment donné. La commande enregistrée hérite de l’environnement courant utilisé au moment de sa définition. Par exemple, pour une exécution de la commande à 05:45 :

```sh
echo "touch file.txt" | at 0545
```

- `at -l` ou `atq` : affiche la liste des jobs introduits par la commande `at`.
- `at -r <JOB>` ou `atrm <JOB>` : efface le job identifié par son numéro de job.

:::exo
1. Créer une tâche planifiée. Penser à vérifier la date du système avant.
2. Vérifier que la tâche a bien été planifiée.
3. Supprimer la tâche planifiée.
4. Même exercice sans supprimer la tâche - vérifier sa bonne exécution.
:::

:::correction
Prérequis : installer le package `at` s'il n'est pas déjà installé.

```sh
# Installation du package
sudo apt install at
sudo yum install at

# Vérification du service
sudo systemctl status atd
# Si non activé :
sudo systemctl enable --now atd
```

1. Créer une tâche planifiée. Penser à vérifier la date du système avant.

```console
$ date
$ echo "touch file.txt" | at 0545
warning: commands will be executed using /bin/sh
job 1 at Sat May 17 05:45:00 2025
```

2. Vérifier que la tâche a bien été planifiée.

```console
$ at -l
1	Sat May 17 05:45:00 2025 a root
```

3. Supprimer la tâche planifiée : `at -r <JOB>`.

```sh
at -r 1
at -l
```

4. Même exercice sans supprimer la tâche - vérifier sa bonne exécution.

```sh
date
echo "touch file.txt" | at 0545
# Attendre jusqu'à 05:45 et vérifier que le fichier file.txt a été créé
```

:::

### Fichiers `/etc/at.allow` et `/etc/at.deny`

Ces deux fichiers contrôlent qui peut exécuter des commandes `at`.

- Si `/etc/at.allow` existe et contient des noms d'utilisateurs, seuls ces utilisateurs sont autorisés à utiliser `at`.
- Si `/etc/at.allow` n'existe pas, mais `/etc/at.deny` existe et contient des noms d'utilisateurs, tous les utilisateurs, à l'exception de ceux répertoriés dans `/etc/at.deny`, sont autorisés à utiliser `at`.
- Si ni `/etc/at.allow` ni `/etc/at.deny` n'existent, tous les utilisateurs sont autorisés à utiliser `at`.

## Planification récurrente : `cron`

On utilise `cron` pour planifier des tâches à exécuter périodiquement à des heures fixes, à des dates ou dans des intervalles. Le nom `cron` vient du mot grec pour le temps (chronos).

`cron.d` est normalement lancé comme service.

Le programme `crontab` permet aux utilisateurs de gérer leurs tâches.

### Répertoires `/etc/cron*`

Placer un script dans l’un de ses répertoires l’exécute à un moment prédéfini :

```sh
ls /etc/cron*

/etc/cron.deny  /etc/crontab
/etc/cron.d:
0hourly  raid-check  sysstat  unbound-anchor
/etc/cron.daily:
0yum-daily.cron  logrotate  man-db.cron  mlocate
/etc/cron.hourly:
0anacron  0yum-hourly.cron
/etc/cron.monthly:
/etc/cron.weekly:
```

### Service cron

Sous Ubuntu on trouvera un service `cron.service` :

```sh
sudo systemctl status cron.service
```

:::tip
Le nom du service peut varier dans d'autres distributions : `crond.service` sous CentOS, …
:::

:::tip
Si le système est éteint alors qu'une tâche devrait s'exécuter, celle-ci est perdue et **non exécutée** ! Attention aux backups par exemple.
:::

### Fichier `/etc/crontab`

Le fichier `/etc/crontab` permet de planifier finement la répétition d'une commande.

```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
# For details see man 4 crontabs
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)
# |  |  |  |  |     OR sun,mon,tue,wed,thu,fri,sat
# *  *  *  *  * user-name  command-to-be-executed
```

Par exemple, pour lancer un script toutes les minutes :

```
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7)
# |  |  |  |  |     OR sun,mon,tue,wed,thu,fri,sat
# *  *  *  *  * user-name  command to be executed
* * * * * /home/mon_utilisateur/job1.sh
```

:::tip
- Les trois premières lettres des noms des mois et des jours de la semaine correspondent aux termes anglais quelle que soit la casse.
- On peut écrire des plages de valeurs (inclusif) : `8-11`
- On peut écrire des listes de plages : `1,2,5,9` ou `0-4,8-12`
- Une valeur suivie de `/<nombre>` correspond à une cadence : `0-23/2` est équivalent à `0,2,4,6,8,10,12,14,16,18,20,22`
  - `*/2` : "tous les deux temps"
:::

:::link
Pour s'aider à écrire les `crontab` et les vérifier, on pourra utiliser l'excellent site : <https://crontab.guru/>
:::

### Exemples de planification

- Chaque jour, 5 minutes après minuit : `5 0 * * *`
- Le premier jour de chaque mois à 14h15 : `15 14 1 * *`
- Du lundi au vendredi à 22h : `0 22 * * 1-5`
- Chaque jour, toutes les deux heures à partir de minuit : `23 0-23/2 * * *`
- Chaque dimanche à 4h05 : `5 4 * * sun`

### Commande `crontab`

- La commande `crontab` permet d'afficher / modifier les jobs `cron` : 
  - `crontab -e` : édite un `cron` avec l'éditeur par défaut
  - `crontab -l` : affiche les jobs programmés

:::exo
1. Copier le script suivant et le faire exécuter toutes les 2 minutes.
2. Que fait ce script ?

```sh
#!/usr/bin/env bash
touch /home/mon_utilisateur/cron-$(date +"%Y%H%M")
```
:::

:::correction
Pour exécuter ce script toutes les 2 minutes, ajoutez la ligne suivante à votre crontab :

```sh
crontab -e
```

Ajoutez la ligne suivante :

```
*/2 * * * * /chemin/vers/le/script.sh
```

Ce script crée un fichier dans le répertoire `/home/mon_utilisateur/` avec un nom basé sur la date et l'heure actuelles au format `cron-YYYYHHMM`.

Vérification :

```sh
crontab -l
ls /home/mon_utilisateur/cron-*
```
:::

### Fichiers `/etc/cron.allow` et `/etc/cron.deny`

Ces fichiers limitent les utilisateurs autorisés à lancer des jobs `cron` : voir la section similaire pour la commande `at`.

### `/var/spool/cron/`

Le répertoire `/var/spool/cron` est un répertoire système utilisé pour stocker les fichiers `crontab` pour **chaque utilisateur**.

- `/var/spool/cron/crontabs` : chaque utilisateur a une `crontab` - **le nom du fichier est le nom de l'utilisateur**.
  - Il s'agit souvent d'un lien symbolique vers `/etc/`, par exemple `/etc/crontabs/`
- `/var/spool/cron/lastrun` : Ce répertoire peut contenir des fichiers temporaires utilisés par le service cron pour stocker des informations sur la dernière exécution de certaines tâches.

### Dépannage des tâches `cron`

Les fichiers de journaux système `/var/log/syslog` et/ou `/var/log/cron` fournissent les information de dépannage sur les erreurs et problèmes de configuration de jobs `cron`.

### Exercice

:::exo
1. Configurer une tâche `cron` qui vérifie périodiquement l'utilisation du disque dur et envoie une alerte par e-mail si l'espace disque disponible descend en dessous d'un seuil spécifié.
2. Vérifier la bonne exécution du script.
:::

:::correction
Configurer une tâche cron qui vérifie périodiquement l'utilisation du disque dur et envoie une alerte par e-mail si l'espace disque disponible descend en dessous d'un seuil spécifié.

1. Créer un script pour vérifier l'utilisation du disque dur et envoyer une alerte par e-mail :

```sh
#!/bin/bash
SEUIL=90
UTILISATION=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%')
if [ "$UTILISATION" -gt "$SEUIL" ]; then
    echo "Alerte : L'utilisation du disque dur est à $UTILISATION%" | mail -s "Alerte d'utilisation du disque dur" admin@example.com
else
    echo "Le disque dur est utilisé à moins de $SEUIL%"
fi
```

2. Ajouter ce script à votre crontab pour qu'il s'exécute périodiquement, par exemple toutes les heures :

```sh
crontab -e
```

Ajouter la ligne suivante pour une vérification toutes les heures :

```
0 * * * * /chemin/vers/le/script.sh
```

3. Vérification de l'exécution du script

```sh
cat /var/log/syslog | grep -i cron
```
:::

## Compteurs `systemd`

Les unités de minuterie systemd (_systemd timer units_) sont des fichiers de configuration utilisés par `systemd` pour planifier et exécuter des tâches périodiques. Elles sont utilisées comme alternative aux tâches cron traditionnelles et offrent des fonctionnalités avancées telles que la gestion des dépendances, la précision du calendrier, et la cohérence de l'exécution.

Une unité de minuterie `systemd` est généralement composée de deux fichiers :

- L'unité de minuterie `*.timer` qui définit quand la tâche doit être déclenchée.
- L'unité à activer (`*.service`, `*.target`, …) qui définit ce qui doit être exécuté lorsque la minuterie est déclenchée.

Les unités de minuterie sont configurées à l'aide de directives telles que `OnCalendar` pour spécifier les horaires d'exécution, `OnBootSec` pour définir un délai après le démarrage du système, `OnUnitActiveSec` pour définir un délai après l'activation de la minuterie, …

Une fois les unités de minuterie configurées, elles doivent être activées à l'aide de la commande `systemctl enable` pour qu'elles soient prises en compte par systemd et déclenchent les actions spécifiées.

### Exemple de Timer

```ini
[Unit]
Description=
[Timer]
OnBootSec=
OnUnitActiveSec=
OnCalendar=
Persistent=
[Install]
WantedBy=timers.target
```

```ini
[Unit]
Description=Daily rotation of log files
[Timer]
OnCalendar=daily
AccuracySec=1h
Persistent=true
[Install]
WantedBy=timers.target
```

### Syntaxe de timer

- `OnBootSec` : Démarre le service du même nom que le timer après X secondes
- `OnUnitActiveSec` : Répétition toutes les X secondes tant que le système est en fonctionnement
- `OnCalendar` : Quand lancer le timer :
  - `hourly` = chaque heure (à 0 minute)
  - `daily` = à minuit chaque jour
  - `weekly` = tous les lundis à minuit
  - `DayOfWeek Year-Month-Day Hour:Minute:Second`
    - `OnCalendar=*-*-* 1:00:00` : Tous les jours à 1h du matin
    - `OnCalendar=Sun *-*-* 12:00:00` : Tous les dimanches à midi
    - `OnCalendar=*-*-1 00:20:00` : Tous les premiers du mois à 00h20
    - `OnCalendar=Mon *-*-1..7 6:00:00` ; Du 1 au 7 du mois, qui soit un lundi, à 6h (traduisez le premier lundi du mois à 6h)
- `Persistent` : `yes` = Si le système était à l'arrêt pendant le déclenchement, le lancement raté est rattrapé (utilisé avec `OnCalendar`)

:::tip
Le paramètre `Persistent=true` est très utile pour rattraper des tâches non exécutées parce que le système était éteint (backup, …) : c'est un gros avantage sur _Cron_ !
:::

#### Occurences

- `*` : Toutes les occurrences
- `1` : Occurrence 1
- `1..7` : Occurrences de 1 à 7
- `0,12` : Occurrences 0 et 12


### Exemples sur le système

```sh
grep OnCalendar -r /usr/lib/systemd/
```

:::link
Pour plus d'information sur les timers systemd, voir ces liens :

- [wiki Archilinux](https://wiki.archlinux.org/title/Systemd_(Fran%C3%A7ais)/Timers_(Fran%C3%A7ais))
- [wiki Gentoo](https://wiki.gentoo.org/wiki/Systemd#Timer_services)
- [Fedora magazine](https://fedoramagazine.org/systemd-timers-for-scheduling-tasks/)
- [Blog stephane-robert](https://blog.stephane-robert.info/docs/admin-serveurs/linux/timers/)
:::

### Exercice

:::exo
Porter la tâche `cron` en utilisant un timer `systemd`.
Pour rappel, la tâche consiste à vérifier périodiquement l'utilisation du disque dur et envoie une alerte par e-mail si l'espace disque disponible descend en dessous d'un seuil spécifié.
:::

:::tip
On pourra utiliser `systemd-cat` pour rediriger les sorties standard et d'erreur (`stdout` et `stderr` des commandes `echo`) dans le journal de _systemd_.
:::

:::correction
1. Créer un fichier de service pour la tâche :

```ini
# /etc/systemd/system/disk-check.service
[Unit]
Description=Check disk usage

[Service]
ExecStart=/chemin/vers/le/script.sh | systemd-cat
```

2. Créer un fichier de timer pour planifier la tâche :

```ini
# /etc/systemd/system/disk-check.timer
[Unit]
Description=Run disk check every hour

[Timer]
OnCalendar=hourly
# Ou pour tester toutes les minutes :
OnCalendar=*-*-* *:*:00
Persistent=true

[Install]
WantedBy=timers.target
```

3. Activer et démarrer le timer :

```sh
sudo systemctl enable disk-check.timer
sudo systemctl start disk-check.timer
```

4. Vérification

```sh
# Vérification de l'activation du timer
sudo systemctl status disk-check.timer
sudo systemctl list-timers
# Logs du timer (heure d'exécution)
sudo journalctl -u disk-check.timer
# Logs de systemd-cat (résultat du script)
sudo journalctl -b
```

:::
