---
title: "Investigation post-compromission sous Linux : Détection et analyse"
date: 2025 / 2026
---

## Objectifs

**Identifier les traces d'une compromission (analyse de logs, rootkits, persistence) et utiliser des outils d'investigation (chkrootkit, rkhunter, auditd, osquery)** :

- Savoir identifier les traces d’une compromission sur un système Linux.
- Analyser les logs système et les mécanismes de persistence.
- Utiliser des outils dédiés à la détection de rootkits et d’anomalies.
- Comprendre le rôle de l’audit et de la surveillance continue.

## Contexte

L'administrateur d'un serveur interne a remarqué une montée d’activité réseau inhabituelle et une entrée suspecte dans `/etc/cron.d`. Après triage initial, il vous demande d’identifier si la machine a été compromise, quelles traces existent, et de produire un rapport avec preuves et actions recommandées.

## Préparation de l’environnement

### Installation des outils nécessaires

Installez les outils suivants sur votre machine :

```bash
# Sur Debian/Ubuntu
sudo apt update && sudo apt install -y chkrootkit rkhunter auditd osquery

# Sur CentOS/RHEL
sudo yum install -y epel-release
sudo yum install -y chkrootkit rkhunter audit osquery
```

### Configuration de base

- Activez et démarrez le service `auditd` :

  ```bash
  sudo systemctl enable auditd --now
  ```

- Vérifiez le statut :

  ```bash
  sudo systemctl status auditd
  ```

## Vérification de l'état général

En utilisant les outils Linux standard, vérifier :

- uptime
- utilisateurs connectés
- processus suspects
- connexions réseau établies ou en écoute
- …

## Analyse des logs système

### Vérification des logs système

- Consultez les logs système avec `journalctl` :

  ```bash
  sudo journalctl -xe
  ```

- Cherchez des connexions suspectes dans `/var/log/auth.log` ou `/var/log/secure` :

  ```bash
  sudo grep -i "failed" /var/log/auth.log
  sudo grep -i "sshd" /var/log/auth.log
  ```

### Détection de connexions inhabituelles

- Listez les utilisateurs connectés :

  ```bash
  who
  w
  last
  ```

- Vérifiez les processus en cours :

  ```bash
  ps aux
  top
  ```

## Détection de rootkits

### Utilisation de `chkrootkit`

- Lancez une analyse complète :

  ```bash
  sudo chkrootkit
  ```

- Interprétez les résultats : toute alerte doit être investiguée.

### Utilisation de `rkhunter`

- Mettez à jour la base de données :

  ```bash
  sudo rkhunter --update
  ```

- Lancez une analyse :

  ```bash
  sudo rkhunter --check
  ```

- Consultez le rapport généré dans `/var/log/rkhunter.log`.

## Analyse de la persistence

### Vérification des tâches planifiées

- Listez les tâches cron :

  ```bash
  crontab -l
  ls -la /etc/cron*
  ```

- Cherchez des entrées suspectes dans `/etc/crontab`.

### Vérification des services et démons

- Listez les services actifs :

  ```bash
  sudo systemctl list-units --type=service
  ```

- Cherchez des services inconnus ou modifiés.

### Vérification des fichiers de démarrage

- Inspectez les fichiers dans `/etc/init.d/` et `/etc/systemd/system/`.

### Librairies dynamiques en pré-chargement

- Le "preload" de librairie dynamique : `/etc/ld.so.preload` est souvent un indicateur de rootkit.

## Utilisation d'osquery

:::tip
Osquery est un outil open source développé par Facebook (Meta) qui permet de transformer les informations système d'un ordinateur en tables relationnelles accessibles via un langage de requête SQL. Il est conçu pour faciliter la surveillance, la détection d'intrusions et l'investigation "forensics" sur les systèmes Linux, macOS et Windows.
:::

### Interrogation du système avec osquery

- Listez les utilisateurs :

  ```bash
  sudo osqueryi --json "SELECT * FROM users;"
  ```

- Listez les processus :

  ```bash
  sudo osqueryi --json "SELECT * FROM processes;"
  ```

- Cherchez des fichiers modifiés récemment :

  ```bash
  sudo osqueryi --json "SELECT * FROM file WHERE directory = '/etc' AND mtime > '$(date +%s -d '1 day ago')';"
  ```

## Audit avec auditd

### Configuration de règles d’audit

- Ajoutez une règle pour surveiller les accès à `/etc/passwd` :

  ```bash
  sudo auditctl -w /etc/passwd -p wa -k passwd_changes
  ```

- Vérifiez les règles actives :

  ```bash
  sudo auditctl -l
  ```

### Analyse des logs d'audit

- Consultez les logs générés :

  ```bash
  sudo ausearch -k passwd_changes | aureport -f -i
  ```

## Synthèse et rapport

### Rédigez un rapport d’investigation

- Résumez les anomalies détectées.
- Proposez des actions correctives (suppression de fichiers suspects, mise à jour des mots de passe, etc.).

### Questions de réflexion

- Quels sont les signes les plus évidents d'une compromission ?
- Comment automatiser la détection avec des outils comme osquery ou auditd ?

## Ressources utiles

- [Documentation chkrootkit](http://www.chkrootkit.org/)
- [Documentation rkhunter](http://rkhunter.sourceforge.net/)
- [Documentation osquery](https://osquery.io/)
- [Guide auditd](https://access.redhat.com/documentation/fr-fr/red_hat_enterprise_linux/7/html/security_guide/chap-system_auditing)

