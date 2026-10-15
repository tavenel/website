---
title: Projet Infrastructure Linux sécurisée pour un centre de données confidentiel
date: 2025 / 2026
type: projet
sidebar:
  order: 500
description: Projet Infrastructure Linux sécurisée pour un centre de données confidentiel
---
## 🧩 Contexte

Vous êtes administrateurs système d'un centre de données spécialisé dans la gestion de données sensibles pour des entreprises partenaires.
L'objectif est de concevoir, déployer et sécuriser une infrastructure Linux complète répondant à des exigences fortes de **disponibilité**, **confidentialité** et **intégrité des données**.

L'ensemble des services devra être installé sur un cluster de **3 machines virtuelles Linux** (par exemple _Debian_ ou _Rocky Linux_), en respectant les bonnes pratiques de **sécurité système** et de **segmentation réseau**.

## ⚙️ Objectifs techniques

### Stockage et gestion des volumes

- Mettre en place un **RAID** logiciel pour assurer la redondance des données.
- Utiliser **LVM** au-dessus du RAID pour la flexibilité du partitionnement.
- Chiffrer les volumes critiques avec **LUKS**.
- Exposer un volume partagé via :

  - **NFS** (lecture seule pour les serveurs applicatifs)
  - **iSCSI** (lecture/écriture pour le serveur de sauvegarde)

### Sauvegarde et restauration

- Configurer un système de **sauvegarde automatisée** (via `rsnapshot`, `borgbackup`, ou `restic`) :

  - Sauvegarde chiffrée.
  - Planification (_cron_ ou _systemd timer_).
  - Restauration testée sur un volume monté temporairement.

### Service web sécurisé

- Déployer un **serveur Apache** hébergeant un mini-site interne d'administration :

  - HTTPS activé avec **certificat SSL/TLS** auto-signé ou Let's Encrypt.
  - Accès restreint par **authentification** (_Basic_ ou _LDAP_).
  - Sécurisation renforcée des en-têtes HTTP et du chiffrement (TLS 1.3, ciphers forts).

### Réseau et sécurité

- Segmentation en **zones réseau** :

  - `admin` : accès SSH, supervision.
  - `web` : services HTTP/HTTPS.
  - `storage` : services NFS/iSCSI.
- Configurer un **pare-feu** (`iptables` ou `nftables`) et des règles strictes par zone.
- Activer et configurer un **IDS/IPS léger** (comme `Fail2ban` ou `Suricata`).
- Activer le **logging centralisé** (`rsyslog` ou `journalctl --forward-to`).

### VPN sécurisé

- Mettre en place un **VPN** (_WireGuard_ ou _OpenVPN_) :

  - Authentification par clé.
  - Routage du trafic de l'administrateur via le VPN uniquement.
  - Pare-feu intégré et règles de filtrage.

### Gestion des ressources

- Utiliser des **cgroups** pour :

  - Limiter la mémoire et le CPU de certains services.
  - Empêcher qu'un processus utilisateur monopolise les ressources.
  - Superviser l'utilisation des ressources via `systemd-cgtop` ou `cgroups-monitor`.

## 🧠 **Travail attendu**

### 🧩 Partie 1 - Conception

- Schéma d'architecture réseau et stockage (avec légendes).
- Justification du choix des technologies (RAID niveau, VPN type, outil de backup…).
- Politique de sécurité et segmentation réseau.

### ⚙️ Partie 2 - Déploiement

- Scripts d'installation et de configuration reproductibles (`bash`, `ansible` ou `systemd`).
- Documentation d'installation détaillée.
- Tests de validation (connectivité, restauration de backup, chiffrement, VPN…).

### 🔒 Partie 3 - Sécurité et audit

- Politique de chiffrement et de rotation des clés.
- Résultats de tests de sécurité (`nmap`, `ss`, `curl -v`, `fail2ban-client status`, etc.).
- Vérification de la résilience en cas de panne disque, coupure réseau ou attaque brute force.

## 📊 Livrables

1. **Dossier d'architecture technique** (PDF ou Markdown)
2. **Scripts / fichiers de configuration** (GitLab ou archive `.tar.gz`)
3. **Journal de tests et de validation**
4. **Rapport de sécurité** (analyse des menaces, mesures préventives, durcissement appliqué)

## 🧾 Grille d'évaluation (sur 100 points)

| Domaine                       | Critère                                                         | Points |
| ----------------------------- | --------------------------------------------------------------- | ------ |
| **Stockage**                  | RAID fonctionnel, LVM dynamique, chiffrement LUKS opérationnel  | 15     |
| **Partage**                   | NFS et iSCSI correctement configurés et sécurisés               | 10     |
| **Sauvegarde**                | Sauvegarde automatisée, chiffrée et restaurable                 | 10     |
| **Web sécurisé**              | Apache SSL, configuration TLS, durcissement et authentification | 10     |
| **Réseau**                    | Segmentation logique, firewall, IDS/IPS fonctionnel             | 15     |
| **VPN**                       | Tunnel sécurisé, filtrage et authentification par clé           | 10     |
| **Cgroups**                   | Limitation et supervision des ressources                        | 10     |
| **Sécurité globale**          | Respect des bonnes pratiques (permissions, audit, logs)         | 10     |
| **Documentation & cohérence** | Clarté, justification des choix, reproductibilité               | 10     |
| **BONUS: Haute Disponibilité** | Cluster HA sur 3 noeuds, Corosync + Pacemaker, services sur VIP | +20     |
| **BONUS: Détection d'anomalies** | Outils d'investigation : chkrootkit, rkhunter, auditd, osquery | +10     |

