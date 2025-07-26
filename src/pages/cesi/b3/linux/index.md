---
title: 🐧 Linux avancé
layout: '@layouts/BaseLayout.astro'
---

# 🐧 INF13 - Administration avancée de Linux

## Présentation du module

### 🎯 Objectifs opérationnels

- Concevoir et administrer une architecture système basée sur les technologies Linux, répondant aux besoins des entreprises
- Installer, administrer et faire évoluer une distribution en autonomie.

### 🎯 Objectifs d'apprentissage

- Décrire comment paramétrer finement le système
- Justifier l'intégration de Linux avec l'existant dans l'entreprise

### 📋 Prérequis

Bases de Linux :

- <https://openclassrooms.com/fr/courses/2356316-montez-un-serveur-de-fichiers-sous-linux>
- <https://openclassrooms.com/fr/courses/1733551-gerez-votre-serveur-linux-et-ses-services>

### 📅 Déroulé des séances

Module de 3 journées

- Jour 1 : Administration avancée et tâches de maintenance en CLI
  - Boot-loader (Grub) et séquences de boot (kernel, initramfs, init et runlevel) 
  - Mise en place du mode maintenance et crash recovery 
  - Gestion des paquetages sous RedHat/Fedora et sous Debian/Ubuntu
- Jour 2 : Configuration avancée des services réseaux
  - Protocole IP et services TCP, UDP et ICMP
  - Configuration statique des interfaces réseaux
  - Définition des règles de routage et utilisation du protocole DHCP
  - Mise en place de serveur VPN
- Jour 3 : Virtualisation et continuité de service
  - Gestion des données et shell scripts :
    - Chiffrement et sécurisation des données (SSH, SSH tunneling, Firewall Netfilter avec iptables, outils de monitoring réseau) 
    - PAM et Sudo 
  - Utilitaires : tar, rsync, dump/restore, …
  - Produits : Partimage, MondoRescue, backuppc, …
  - Continuité de service

## 📑 Documents

- [󰣛 Machine virtuelle Fedora Desktop dans VirtualBox](/linux/tp-installation-vbox-fedora-workstation)
- [󰕈 Machine virtuelle Ubuntu Desktop dans VirtualBox](/linux/tp-installation-vbox-ubuntu-workstation)
- [🤓 Cours Linux administration avancée](/cesi/b3/linux/cours)
- [📀 TP : utiliser GRUB pour une restauration système](/linux/tp-grub)
- [📀 TP : utiliser un Live CD/USB pour une restauration système](/linux/tp-rescue)
- [📦 TP : Gestion de paquetages](/linux/tp-rpm-apt) : gérer (installer, mettre à jour, désinstaller) des programmes depuis des packets RedHat via rpm, yum et dnf et des packets Debian via dpkg et apt.
- [📡 TP : Configuration réseau](/linux/tp-network) : gérer la configuration réseau d'un système Linux en utilisant les outils historiques `net-tools`, les outils modernes `iproute2`, ou les implémentations `systemd`. L'utilisation de `Network Manager` est aussi abordée.
- [🌐 TP : Installation d'un service VPN](/linux/tp-vpn)
- [🔐 TP : Sécurité des échanges avec SSH et GPG](/linux/tp-ssh-gpg)
- [🔐 TP : Notions de sécurité : limitations des comptes utilisateurs, élévation de privilèges, audit de sessions, fichiers et ports ouverts, …](/linux/tp-security)
- [💾 TP Sauvegarde et Restauration sous Linux](/linux/tp-backup)
- [🔐 TP : Mise en place de règles de filtrage sous Debian avec Netfilter](/linux/projet-netfilter) : Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu.

## 🚀 Pour aller plus loin

- Voir les autres ressources du [cours sur Linux](/linux).

