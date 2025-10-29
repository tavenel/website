---
title: 🐧 Advanced Linux administration expert
layout: '@layouts/BaseLayout.astro'
---

# 🐧 Advanced Linux administration expert

## Présentation du module

### 🎯 Objectifs pédagogiques

#### 1. **Maîtrise avancée du système Linux**

- Comprendre en profondeur le fonctionnement du noyau, de l'espace utilisateur et des processus.
- Diagnostiquer et résoudre des problèmes complexes de performance (CPU, mémoire, I/O, réseau).
- Gérer et analyser les logs systèmes et applicatifs.
- Mettre en œuvre des configurations avancées du système d'initialisation (systemd, cgroups, namespaces).

#### 2. **Gestion avancée du stockage et des systèmes de fichiers**

- Mettre en place et administrer des volumes LVM et des RAID logiciels.
- Configurer le chiffrement de disque (LUKS) et les montages sécurisés.
- Gérer les quotas, snapshots, et politiques de sauvegarde/restauration.
- Automatiser la gestion du stockage via des scripts et outils IaC (ex : Ansible).

#### 3. **Réseaux Linux et sécurité réseau**

- Configurer et dépanner des interfaces réseau complexes (bonding, VLANs, bridges, routage).
- Mettre en œuvre des pare-feu et filtres avancés avec `iptables`/`nftables`.
- Mettre en place du NAT, du proxy et du reverse-proxy sécurisé.
- Superviser le trafic réseau et détecter des anomalies (tcpdump, Wireshark, Suricata, etc.).

#### 4. **Gestion des incidents et continuité d'activité**

- Mettre en place des stratégies de sauvegarde et restauration.
- Simuler et gérer un incident : compromission, panne disque, corruption de configuration.
- Concevoir et tester des plans de reprise d'activité (PRA/PCA).

### 📋 Prérequis

Bases de Linux :

- <https://openclassrooms.com/fr/courses/2356316-montez-un-serveur-de-fichiers-sous-linux>
- <https://openclassrooms.com/fr/courses/1733551-gerez-votre-serveur-linux-et-ses-services>

### 📅 Déroulé des séances

Module de 4 journées

## 📑 Documents

### Cours

- [🤓 Cours Linux administration avancée](/estiam/linux/cours)

### Environnement

- [Installer un serveur Ubuntu sous Virtualbox](https://www.eugenetoons.fr/installer-un-serveur-ubuntu-sous-virtualbox/)
- [  TP : Utilisation efficace de la ligne de commande](/linux/tp-ligne-commande)

### TPs de rappels

- [📦 TP : Gestion de paquetages](/linux/tp-rpm-apt) : gérer (installer, mettre à jour, désinstaller) des programmes depuis des packets RedHat via rpm, yum et dnf et des packets Debian via dpkg et apt.
- [📂 TP : Gestion basique des fichiers - déplacement, copie, liste, types de fichiers](/linux/tp-fichiers)
- [⚙️ TP : Gestion des processus et de leur priorité](/linux/tp-process)
- [▶️ TP : Systemd init](/linux/tp-systemd) : administrer les services et changer de runlevel dans un système systemd.
- [💽 TP : Gestion des partitions et des systèmes de fichiers](/linux/tp-partitions)
- [👥 TP : Gestion des utilisateurs et de la sécurité](/linux/tp-utilisateurs)

### TPs d'administration expert

- [📀 TP : utiliser un Live CD/USB pour une restauration système](/linux/tp-rescue)
- [🔐 TP : Gestion des permissions avancées avec SUID, SGID et ACL](/linux/tp-droits-avance)
- [⌨️ TP : affichage de la configuration du système et des périphériques, gestion des modules noyau](/linux/tp-systeme)
- [📡 TP : Configuration réseau](/linux/tp-network) : gérer la configuration réseau d'un système Linux en utilisant les outils historiques `net-tools`, les outils modernes `iproute2`, ou les implémentations `systemd`. L'utilisation de `Network Manager` est aussi abordée.
- [🔐 TP : Sécurité des échanges avec SSH et GPG](/linux/tp-ssh-gpg)
- [🔒 TP : Notions de sécurité : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …](/linux/tp-security)
- [🔐 TP : Mise en place de règles de filtrage sous Debian avec Netfilter](/linux/projet-netfilter) : Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu.
- [🌐 TP : Installation d'un service VPN](/linux/tp-vpn)
- [💽 TP : Utiliser LVM pour créer, gérer et étendre des volumes logiques](/linux/tp-lvm)
- [💽 TP : Mise en place d'un partage NFS (Network File System) sous Debian](/linux/tp-nfs)
- [💽 TP : Utiliser iSCSI pour gérer des disques réseau](/linux/tp-iscsi)
- [💾 TP Sauvegarde et Restauration sous Linux](/linux/tp-backup)
- [📦 TP : Découverte des Cgroups](/linux/tp-cgroup) : une introduction aux cgroups, permettant de limiter les ressources utilisées par des processus.
- [🔐 TP : Investigation post-compromission sous Linux : Détection et analyse](/linux/tp-forensics) : Identifier les traces d'une compromission (analyse de logs, rootkits, persistence) et utiliser des outils d'investigation (chkrootkit, rkhunter, auditd, osquery).

### Projet

- [🔐 Projet : Infrastructure Linux sécurisée pour un centre de données confidentiel](/linux/projet-cyber) : L'objectif est de concevoir, déployer et sécuriser une infrastructure Linux complète répondant à des exigences fortes de disponibilité, confidentialité et intégrité des données.

### Optionnels

- [📁 TP : Gestion avancée de fichiers - permissions, liens, recherche](/linux/tp-fichiers-avance)
- [📜 TP : Journalisation avec Syslog](/linux/tp-syslog) : gérer les journaux (logs) système et utilisateur, en local ou vers un serveur centralisé, notamment par le biais de `syslog` et ses différentes implémentations : `syslog`, `rsyslog` et `syslog-ng`.

## 🚀 Pour aller plus loin

- Voir les autres ressources du [cours sur Linux](/linux).

