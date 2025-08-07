---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Projet LPIC-2 - Mise en place d'une infrastructure système complète sécurisée et supervisée
---

## Contexte du projet

Une entreprise fictive, **TechCorp**, souhaite mettre en place une infrastructure système Linux robuste pour héberger ses services internes (partage de fichiers, messagerie, accès distant sécurisé, services DNS/DHCP, etc.). Cette infrastructure doit être redondante, sécurisée et supervisée.

### Objectif pédagogique

L'objectif de ce projet est de mettre en œuvre tous les savoir-faire clés de la certification LPIC-2 à travers la configuration d'une infrastructure réseau cohérente, intégrée et sécurisée.

### Livrables attendus

- Documentation d'installation et de configuration (Markdown ou PDF)
- Diagrammes d'architecture (réseau, services, stockage)
- Journaux d'exploitation (checklists, logs d'installation)
- Rapport de monitoring (graphes, statistiques, alertes)

### Scénario d'exploitation

- Déployer les services sur plusieurs VM
- Au minimum : 1 VM Serveur, 1 VM Cliente

:::tip
On ne demande pas de réaliser de déploiement hautement disponible.
:::

## Périmètre technique

### Stockage & sécurité

- Création de volumes LVM
- Mise en place d'un RAID logiciel (niveau 1 ou 5)
- Chiffrement avec LUKS
- Sauvegardes automatisées (rsnapshot, borg, duplicity, etc.)
- Critères :
  - RAID fonctionnel, LVM opérationnel, disque chiffré accessible, …
  - Sauvegarde automatisée, restauration testée, snapshots, …

### Accès sécurisé et distant

- Installation d'un serveur OpenVPN
- Configuration du serveur SSH (authentification par clé, bannissement, etc.)
- Critères :
  - VPN : Connexion fonctionnelle, sécurité TLS, …
  - SSH : Accès par clés, chroot ou restrictions configurées, …

### Annuaire LDAP

- Déploiement d'un serveur LDAP
- Import de structures via LDIF
- Intégration des clients (authentification PAM/LDAP)
- Critères : Arbre LDIF complet, intégration PAM, test utilisateur, …

### Services de fichiers

- Serveur NFS (partage Unix/Linux)
- Serveur Samba (intégration Windows/Linux)
- Gestion fine des ACL et quotas
- Critères : Accès différencié, partages configurés, test client, …

### Services réseau

- DNS interne (bind ou unbound)
- DHCP avec réservations statiques
- Intégration DNS/DHCP
- Critères : DNS résolu correctement, distribution d'IP par DHCP, logs exploitables, …

### Messagerie

- Serveur SMTP avec Postfix
- IMAP avec Dovecot
- Mise en place de Sieve (tri, redirection, message d'absence)
- Critères : Réception/envoi de mails, message d'absence, tri des mails, …

### Serveurs web et proxy

- Apache avec HTTPS (certificat auto-signé ou Let's Encrypt)
- Nginx en reverse proxy (accès aux applis internes)
- Proxy Squid avec filtrage ACL et authentification
- Critères : Nginx reverse proxy, Apache HTTPS, Squid avec filtrage, …

### Supervision & performance

- Supervision active des ressources de l'infrastructure : (CPU, mémoire, réseau, disque)
- Optimisation des ressources allouées
- Prévision du besoin de réquisition de ressources supplémentaires
- Critères : Suivi charge, journalisation, alertes rudimentaires, …

## Évaluation

### Critères techniques

- Fonctionnalité des services (tests fonctionnels, script de vérification)
- Sécurisation des accès (firewall, certificats, SSH, LDAP)
- Intégration cohérente des services (ex : DNS utilisé partout, Samba/NFS montés correctement)
- Monitoring opérationnel (alertes visibles, graphes clairs)
- Robustesse (RAID, sauvegardes testées)

### Critères de groupe

- Qualité du rapport (Documentation claire, précise, architecture décrite)
- Présentation finale

### Critères individuels

- Implication dans le projet et interaction avec le groupe
- Difficulté de la tâche réalisée
- Réponses techniques aux questions lors de la soutenance

