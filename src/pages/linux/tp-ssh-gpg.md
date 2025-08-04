---
title: TP Sécurité des échanges - SSH et GPG
date: 2024 / 2025
correction: false
---

# Secure Shell : SSH

`SSH` (_Secure Shell_) est un protocole de communication sécurisé utilisé pour accéder à des ordinateurs distants via un réseau. Il permet à un utilisateur de se connecter à un système distant de manière sécurisée, d'exécuter des commandes sur ce système et de transférer des fichiers entre les deux systèmes. Il est largement utilisé pour sécuriser les communications réseau et accéder à des services réseau distants de manière sécurisée. `SSH` permet aussi d'utiliser des tunnels (_port forwarding SSH_) pour sécuriser le trafic réseau d'un autre protocole à travers une connexion SSH chiffrée entre un client et un serveur.

Le protocole SSH supporte le chiffrement symétrique mais en pratique on utilise toujours un système de clés asymétriques :

- Chaque tiers possède 2 clés : une clé _privée_ (jamais échangée) et une clé _publique_ (à transmettre à n'importe qui)
  - la clé publique est l'identité de la personne
  - la clé privée est le secret
- La clé privée, gardée **secrète**, est stockée sur la machine cliente ;
- La clé publique est partagée et stockée sur le serveur pour autoriser la connexion : la clé est publique mais le secret réside dans le fait d'accepter ou non cette clé publique
- Lors d'une connexion SSH, on partage la clé publique de chaque tiers et on utilise localement sa clé publique pour générer une nouvelle clé secrète unique et temporaire pour la connexion courante. Cette clé est chiffrée avec chacune des clés des parties, ainsi personne ne peut la déchiffer.

:::warn
En résumé :

- La clé publique est… publique, vous pouvez la distribuer largement : libre à chacun ensuite d'accepter ou non votre connexion
- La clé privée est… **privée!!** - **on ne partage ABSOLUMENT JAMAIS une clé privée** (elle ne sort donc **JAMAIS** de la machine locale).
:::

## Exercice

:::exo
- Effectuer le TP [Configuration des clés SSH pour un accès sécurisé](/devops/tp_ssh).
- On pourra également consulter le [TP Secure Shell de François Goffinet](https://linux.goffinet.org/administration/secure-shell) pour vous connecter en `SSH` depuis votre machine hôte (Windows, MacOS, Linux) à votre machine virtuelle `Ubuntu`.

Attention, la partie : "Configuration du pare-feu `Firewalld`" n'est pas à effectuer. Si vous utilisez Ubuntu, le pare-feu par défaut est actuellement `ufw` qui est configuré automatiquement à l'installation de `ssh`.
:::

## Le fichier `/etc/nologin`

- Fichier spécial `SSH` permettant de bloquer les connexions
- Le contenu du fichier est affiché (ex : "Le système est actuellement en cours de maintenance. Veuillez réessayer plus tard.")
- Utile pour la maintenance

:::exo
Créer un fichier `/etc/nologin` avec un message de maintenance et vérifier que le message est bien affiché et la connexion SSH refusée.
:::

## Utilisation d'un tunnel SSH pour accéder à un service distant

* SSH permet de mettre en oeuvre un tunnel local (`-L`) et distant (`-R`) pour sécuriser l'accès à un service non exposé directement

### 🖥️ Contexte

Vous disposez des 3 machines suivantes :

| Machine        | IP Privée      | Rôle                                                |
| -------------- | -------------- | --------------------------------------------------- |
| **client**     | `192.168.1.10` | Votre poste de travail                              |
| **bastion**    | `192.168.1.20` | Serveur SSH accessible                              |
| **app-server** | `192.168.1.30` | Contient un service web en local (`localhost:8080`) |

Le service web sur `app-server:8080` n’est **pas exposé sur le réseau**, il est uniquement accessible en local. Vous devez configurer un tunnel SSH **via le bastion** pour y accéder depuis votre machine `client`.

1. **Test de connectivité SSH**

   * Depuis `client`, vérifiez que vous pouvez vous connecter au `bastion` :

     ```sh
     ssh user@192.168.1.20
     ```

2. **Création d'un tunnel SSH local**

   * Créez un tunnel SSH local permettant d'accéder à `app-server:8080` depuis `client:8080` en passant par `bastion` :

     ```sh
     ssh -L 8080:192.168.1.30:8080 user@192.168.1.20
     ```

   * En gardant cette session SSH ouverte, ouvrez un navigateur sur `http://localhost:8080` depuis `client`. Vérifiez que la page du service web s'affiche.

3. **Utilisation d'un tunnel SSH distant**

   * Connectez-vous à `app-server` via `bastion` et redirigez son port `8080` vers un port de `client` (par exemple `8888`) :

     ```sh
     ssh -R 8888:localhost:8080 user@192.168.1.10
     ```

   * Que devez-vous faire pour que cette commande fonctionne ? (indice : `sshd_config`)

:::correction
- `-R` crée un tunnel distant.
- Cela redirige les connexions sur `client:8888` vers `app-server:8080`.
- Cela suppose que `sshd` sur le client accepte les tunnels :

```ini
# /etc/ssh/sshd_config
GatewayPorts yes
AllowTcpForwarding yes
```
:::

4. **(Bonus)** : Reverse Proxy

   * Utilisez `ssh -D` pour créer un proxy SOCKS et configurez votre navigateur pour l'utiliser.

:::correction
```sh
ssh -D 1080 user@192.168.1.20
```
:::

# Chiffrement et signature de fichiers : GPG (GNU Privacy Guard)

_Objectif : Apprendre à utiliser GPG pour chiffrer, déchiffrer, signer et vérifier des fichiers._

## Exercice 1 : Chiffrer et Déchiffrer des Fichiers

1. Générez une paire de clés GPG (privée/publique) en utilisant la commande suivante :

```sh
gpg --gen-key
```

2. Chiffrez un fichier texte en utilisant la clé publique d'un autre utilisateur :

```sh
gpg --encrypt --recipient destinataire fichier.txt
```

3. Déchiffrez le fichier chiffré en utilisant votre propre clé privée :

```sh
gpg --decrypt fichier.txt.gpg
```

## Exercice 2 : Signature et Vérification de Fichiers

1. Signez un fichier en utilisant votre propre clé privée :

```sh
gpg --sign fichier.txt
```

2. Vérifiez la signature du fichier en utilisant la clé publique correspondante :

```sh
gpg --verify fichier.txt
```

## Exercice 3 : Gestion des Clés

1. Exportez votre clé publique vers un fichier pour la partager avec d'autres utilisateurs :

```sh
gpg --export --armor votre_email > cle_publique.asc
```

2. Importez la clé publique d'un autre utilisateur depuis un fichier :

```sh
gpg --import cle_publique.asc
```

3. Affichez la liste des clés publiques disponibles sur votre système :

```sh
gpg --list-keys
```

4. Exportez votre clé publique vers un serveur central d'échange de clés.

```sh
gpg --keyserver keyserver.example.com --search-keys email@example.com
gpg --keyserver keyserver.example.com --recv-keys ABCDEF0123456789
gpg --keyserver keyserver.example.com --send-keys ABCDEF0123456789
```

:::link
Il existe de nombreux serveurs d'échange de clés publiques, les principaux étant :

- `pgp.mit.edu` - MIT's Public Key Server
- `keys.openpgp.org` - OpenPGP Keyserver operated by the OpenPGP Working Group
- `pool.sks-keyservers.net` - SKS OpenPGP Keyserver Pool
- `keyserver.ubuntu.com` - Ubuntu Key Server
:::

## Exercice 4 : GPG et mails

:::tip
`gpg` est intégrable dans beaucoup d'outils : il permet notamment de chiffer et/ou de signer des mails facilement !
:::

1. En utilisant votre client Mail (par exemple Thunderbird et un plugin GPG comme `Enigmail`), tester le chiffrement et la signature de vos mails.

