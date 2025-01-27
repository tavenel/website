---
title: Configuration des clés SSH pour un accès sécurisé
date: 2024 / 2025
correction: false
---

# Configuration des clés SSH pour un accès sécurisé

## Objectifs

- Comprendre les concepts de base de SSH et des clés publiques/privées.
- Générer et configurer des clés SSH pour un accès sécurisé à un serveur.
- Renforcer la sécurité en désactivant l'authentification par mot de passe.

## Prérequis

- Un serveur Linux (ou une VM) avec SSH installé.
- Un utilisateur non root avec des droits `sudo` sur le serveur.

## Concepts

`SSH` (_Secure Shell_) est un protocole de communication sécurisé utilisé pour accéder à des ordinateurs distants via un réseau. Il permet à un utilisateur de se connecter à un système distant de manière sécurisée, d'exécuter des commandes sur ce système et de transférer des fichiers entre les deux systèmes. Il est largement utilisé pour sécuriser les communications réseau et accéder à des services réseau distants de manière sécurisée. `SSH` permet aussi d'utiliser des tunnels (_port forwarding SSH_) pour sécuriser le trafic réseau d'un autre protocole à travers une connexion SSH chiffrée entre un client et un serveur.

Le protocole SSH supporte le chiffrement symétrique mais en pratique on utilise toujours un système de clés asymétriques :

- Chaque tiers possède 2 clés : une clé _privée_ (jamais échangée) et une clé _publique_ (à transmettre à n'importe qui)
  - la clé publique est l'identité de la personne
  - la clé privée est le secret
- La clé privée, gardée **secrète**, est stockée sur la machine cliente ;
- La clé publique est partagée et stockée sur le serveur pour autoriser la connexion : la clé est publique mais le secret réside dans le fait d'accepter ou non cette clé publique
- Lors d'une connexion SSH, on partage la clé publique de chaque tiers et on utilise localement sa clé publique pour générer une nouvelle clé secrète unique et temporaire pour la connexion courante. Cette clé est chiffrée avec chacune des clés des parties, ainsi personne ne peut la déchiffer.

:::warning
En résumé :

- La clé publique est… publique, vous pouvez la distribuer largement : libre à chacun ensuite d'accepter ou non votre connexion
- La clé privée est… **privée!!** - **on ne partage ABSOLUMENT JAMAIS une clé privée** (elle ne sort donc **JAMAIS** de la machine locale).
:::

Dans le TP, l’utilisateur `user_local` (sur la machine cliente) générera une paire de clés SSH et ajoutera la clé publique sur le serveur. Cette clé publique sera placée dans le fichier `authorized_keys` de l'utilisateur `user_remote` avec lequel on se connectera sur le serveur, ce qui autorisera la connexion sans mot de passe pour cet utilisateur.

### Processus

Voici un schéma simplifié du processus :

1. Génération de la clé : on génère une paire de clés (privée et publique) dans le répertoire `~user_local/.ssh` de `user_local` sur la machine cliente.
2. Copie de la clé publique : la clé publique est copiée dans le fichier `~user_remote/.ssh/authorized_keys` de `user_remote` sur le serveur.
3. Connexion SSH : lors de la connexion de `user_local@machine_cliente` vers `user_remote@remote_server`, `user_local` utilise sa clé pour s'authentifier sur le serveur en tant que `user_remote@machine_remote`. Le serveur vérifie la clé publique pour authentifier l’utilisateur, autorisant l'accès si la clé est correcte.

## Partie 1 : Création des clés SSH

### Génération des clés

Depuis la machine cliente (ex. votre ordinateur), ouvrez un terminal et exécutez la commande suivante pour générer une paire de clés :

```bash
ssh-keygen -t rsa -b 4096 -C "votre_email@example.com"
# Options :
# -t rsa : spécifie le type de clé.
# -b 4096 : longueur de la clé.
# -C "commentaire" : ajoute un commentaire (généralement votre email).
```

- Appuyez sur `Entrée` pour accepter le chemin par défaut, ou spécifiez un autre emplacement si vous préférez.
- Vous pouvez choisir de protéger la clé privée avec un mot de passe.

### Vérification des clés générées

Vérifiez que deux fichiers ont été créés dans le répertoire `~/.ssh/` :

```bash
ls ~/.ssh/id_rsa # la clé privée
ls ~/.ssh/id_rsa.pub # la clé publique
```

## Partie 2 : Copie de la clé publique sur le serveur

### Copie de la clé publique

Utilisez la commande `ssh-copy-id` pour copier la clé publique sur le serveur :

```bash
ssh-copy-id utilisateur@adresse_du_serveur
```

Remplacez `utilisateur` par le nom d’utilisateur sur le serveur et `adresse_du_serveur` par l'adresse IP ou le nom de domaine.

### Alternative : Copie manuelle de la clé publique

Si `ssh-copy-id` n'est pas disponible, utilisez cette méthode :

- Connectez-vous au serveur via SSH avec votre mot de passe :
```bash
ssh utilisateur@adresse_du_serveur
```

- Sur le serveur, ouvrez (ou créez) le fichier `~/.ssh/authorized_keys` :

```bash
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```

- Copiez le contenu de votre fichier `id_rsa.pub` (depuis votre machine cliente) et collez-le dans le fichier `authorized_keys`.
- Sauvegardez et fermez le fichier.

## Partie 3 : Configuration du serveur SSH pour désactiver l'authentification par mot de passe

### Éditez le fichier de configuration SSH

Connectez-vous au serveur et ouvrez le fichier de configuration SSH :

```bash
sudo nano /etc/ssh/sshd_config
```

### Modifiez les paramètres

Recherchez les lignes suivantes et modifiez-les comme indiqué :

```conf
PubkeyAuthentication yes
PasswordAuthentication no
```

### Redémarrez le service SSH

Après avoir enregistré les modifications, redémarrez le service SSH pour appliquer les changements :

```bash
sudo systemctl restart ssh
```

## Partie 4 : Test de connexion avec les clés SSH

### Connexion au serveur

Depuis votre machine cliente, essayez de vous reconnecter au serveur :

```bash
ssh utilisateur@adresse_du_serveur
```

Si la configuration est correcte, vous serez connecté sans avoir à entrer de mot de passe.

## Partie 5 : Sécurisation et vérification

### Tester les permissions des fichiers

Assurez-vous que le fichier `~/.ssh/authorized_keys` a les bonnes permissions :

```bash
chmod 600 ~/.ssh/authorized_keys
chmod 700 ~/.ssh
```

### Vérification des logs

En cas de problème, vérifiez les logs SSH sur le serveur :

```bash
sudo tail -f /var/log/auth.log
```

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0

