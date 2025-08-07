---
title: TP Administration d'un système Linux
date: 2024 / 2025
---

# TP : Administration d'un système Linux

## Objectif principal

Mettre en pratique les commandes shell sous Linux, en se concentrant sur :

- La gestion des droits des utilisateurs et des groupes.
- Une recherche et configuration sur l'élévation de privilèges.

## Contexte du Cas Fictif d'Entreprise : TechNova Solutions

Vous êtes en charge de l'administration d'un serveur Linux pour une entreprise fictive. Votre mission consiste à configurer le système pour assurer une gestion sécurisée et efficace des utilisateurs, groupes et permissions, en suivant les consignes de sécurité de base.

### Contexte de l'entreprise

**TechNova Solutions** est une petite entreprise spécialisée dans le développement de logiciels pour le secteur médical. Avec une équipe de 14 employés, l'entreprise est divisée en trois départements principaux :

1. **Développement** - chargé de la conception et du développement des applications.
2. **Support** - responsable de l'assistance technique aux clients et de la maintenance des systèmes.
3. **Administration** - gère les finances, la gestion RH et les opérations administratives.

TechNova Solutions utilise un serveur Linux pour héberger ses fichiers internes, gérer les droits d'accès, et assurer la sécurité des données.

### Structure des Utilisateurs et Groupes

Pour une meilleure gestion de ses services, TechNova Solutions organise ses utilisateurs en fonction des départements :

| Département   | Utilisateurs         |
|---------------|----------------------|
| Développement | 5 développeurs       |
| Support       | 5 techniciens        |
| Administration| 2 administrateurs    |
| IT            | 2 administrateurs système |

Le service IT dispose de privilèges élevés pour gérer le serveur, tandis que les autres départements ont accès uniquement aux ressources nécessaires à leur travail.

Les développeurs ont besoin de pouvoir lancer une base de données partagée à des buts de test. Cette base de données doit pouvoir être lancée par tous les développeurs.

#### Dossiers partagés

Les différents services doivent pouvoir partager des documents :

- Le service IT a besoin de partager des documents entre utilisateurs du département IT
- Le service administration a besoin de partager des documents entre utilisateurs du département administration.
- Le service Développement a besoin de partager des documents entre utilisateurs du département développement.
- Le service Support a besoin de partager des documents entre utilisateurs du département support.
- Le service Support a besoin d'accéder aux documents du département développement sans pouvoir les modifier.

#### Droits sudoers

- L'IT a tout les droits sur le serveur
- Les Développeurs ont le droit d'installer des programmes
- Le Support et les Développeurs ont le droit de lister tous les fichiers de configuration du système

### Objectifs de Sécurité

1. **Séparation des Permissions** : Chaque groupe de travail doit avoir accès uniquement aux dossiers et fichiers nécessaires pour son département.
2. **Sécurité des Données** : Les données confidentielles (ex. financières et personnelles) doivent être accessibles uniquement aux administrateurs.
3. **Gestion des Privilèges** : Seuls les administrateurs système du groupe ont les privilèges pour installer des logiciels et configurer le serveur.

### Environnement d'Exécution

- **Système d'exploitation** : Ubuntu Server 20.04 LTS.
- **Configuration matérielle** : Serveur avec 4 CPU et 16 Go de RAM.
- **Accès distant** : Les utilisateurs se connectent via SSH pour accéder au serveur et exécuter leurs tâches.

## Plan du TP

### Étape 1 : Introduction et préparation

- **Objectif** : Comprendre le contexte fictif et les tâches à réaliser.
- **Tâches** :
  - Lire le contexte fictif et les objectifs de l'entreprise.
  - Lister les utilisateurs et groupes actuels
- **Résultat attendu** : Une vue d'ensemble des utilisateurs et groupes présents sur le système.

### Étape 2 : Gestion des utilisateurs et des groupes

- **Objectif** : Créer, modifier et supprimer des utilisateurs et des groupes.
- **Tâches** :
  - Créer des utilisateurs avec des rôles spécifiques
  - Créer des groupes pour chaque département de l'entreprise fictive
  - Associer des utilisateurs aux groupes appropriés
- **Résultat attendu** : Les utilisateurs et groupes sont correctement créés et assignés, avec une documentation des commandes utilisées.

### Étape 3 : Gestion des droits et permissions

- **Objectif** : Configurer les droits d'accès aux fichiers et répertoires.
- **Tâches** :
  - Utiliser `chmod`, `chown` et `chgrp` pour définir des permissions spécifiques
  - Tester les accès pour chaque type d'utilisateur et groupe.
- **Résultat attendu** : Les permissions sont correctement configurées pour chaque dossier.

### Étape 4 : Élévation des privilèges

- **Objectif** : Introduire les notions de sécurité et d'élévation des privilèges.
- **Tâches** :
  - Utiliser `sudo` pour permettre à certains utilisateurs d'exécuter des commandes administratives.
  - Configurer le fichier `sudoers` pour restreindre l'accès à certaines commandes sensibles.
  - Vérifier que seuls les utilisateurs autorisés peuvent exécuter les commandes sensibles.
- **Résultat attendu** : Les utilisateurs autorisés sont capables d'utiliser `sudo` pour les commandes spécifiées.

### Bonus - Étape 5 : Gestion des quotas

- **Objectif** : Ajouter des quotas d'utilisation d'espace disque

En vous inspirant des liens suivants, ajouter des quotas disque :

- <https://doc.ubuntu-fr.org/quota>
- <https://www.linuxtricks.fr/wiki/gestion-des-quotas-sous-linux-ext4-xfs>

### Étape 5 : Conclusion et évaluation

- **Récapitulation** des commandes utilisées.
- **Discussion** sur les problèmes rencontrés et les solutions appliquées.
- **Remise d'un rapport** décrivant les étapes suivies et les résultats obtenus.

