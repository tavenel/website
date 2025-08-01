---
title: 🧪 Projet Déploiement et Administration d'une Application Web sous Linux
date: 2024 / 2025
---

## 🎯 Objectif

Mettre en œuvre un environnement Linux complet pour déployer et administrer une application web développée en interne, en s'appuyant exclusivement sur des outils natifs à l’écosystème Linux.

## 📝 Contexte

Vous êtes développeur dans une petite entreprise. En plus du développement de l'application, on vous confie la mission de **préparer un serveur Linux** capable d'héberger celle-ci, **de manière autonome et sécurisée**.

L'objectif est de montrer votre **maîtrise de l’administration système Linux**, en allant jusqu'au déploiement final de votre application web.

## 📦 Livrables attendus

* Image ou VM Ubuntu Server prête à être lancée (ou script d'installation automatisée)
* Code source de l’application
* Fichiers de configuration des services système
* Rapport technique expliquant l'installation, la configuration et la sécurisation
* Documentation utilisateur pour la prise en main de l'environnement
* Présentation orale avec démonstration

## 🔧 Travaux à réaliser

### Préparation du système

* Installer un serveur Linux (par exemple Ubuntu Server 22.04)
* Configuration réseau manuelle (adresse IP statique)
* Activation de l'accès SSH avec clé uniquement
* Création d'un ou plusieurs utilisateurs non-root avec droits adaptés (`sudo`, `groupadd`, etc.)

### Déploiement de l'application

* L'application (simple CRUD en Python/Flask, Node.js, PHP ou autre) doit être déployée **manuellement sans Docker**.
* Mise en place d'un serveur web natif : `Apache2` ou `Nginx` par exemple.
* Intégration à un service système (`systemd`) pour l'exécuter comme un daemon.
* Base de données installée et configurée localement (ex : `MySQL`, `PostgreSQL`, `SQLite`).
* Permissions fichiers et accès restreints selon les bonnes pratiques.

### Services Linux

* Mise en place d’un **serveur DNS local** ou redirection DNS avec `/etc/hosts`
* Installation et configuration de **Samba** pour l'accès distant aux fichiers partagés
* Déploiement d’un service **LDAP** et configuration d'un service local s'appuyant dessus (authentification utilisateur, ou autre)
* Configuration des logs applicatifs et système (`journald`, `rsyslog`, `logrotate`)

### Supervision et planification

* Planification automatique de tâches via `cron` (sauvegarde de la BDD, redémarrage de service, etc.)
* Mise en place d’un outil de supervision natif ou léger (ex : `glances`, `htop`, `monit`)
* Alertes simples par mail ou fichier journal en cas d’échec de service

### Résilience et dépannage

* Procédure de réinitialisation du mot de passe root (documentée et testée)
* Scénario de "crash recovery" à simuler et documenter
* Vérification des journaux pour diagnostiquer et résoudre une erreur système

## 💡 Comment intégrer LDAP avec Samba

1. Utiliser `smbldap-tools` pour générer les schémas LDAP pour Samba :
  - `smbldap-config`
  - `smbldap-populate`
2. Création d'un utilisateur Samba :
  - Récupérer le SID local => `BASE_SID=$(net getlocalsid)`
  - Calculer le SID du user Samba => `SAMBA_SID="${BASE_SID}-$((USER_UID * 2 + 1000))`

Exemple de LDIF Samba :

```
# smbuser.ldif

dn: uid=smbuser,ou=people,dc=example,dc=com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: sambaSamAccount
cn: SMB User
sn: User
uid: smbuser
uidNumber: 10001
gidNumber: 100
homeDirectory: /home/smbuser
loginShell: /bin/bash
sambaSID: # TODO REPLACE
# sambaNTPassword: <NT_HASH>
sambaAcctFlags: [U]
```

```sh
# Ajout de l'utilisateur au LDAP
ldapadd … -f smbuser.ldif
# Complète le champ `sambaNTPassword` (sinon à calculer manuellement)
sudo smbpasswd -a smbuser

# Vérification de la disponibilité du point de montage
smbclient -L //localhost -U smbuser
```
