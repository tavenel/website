---
title: TP Mise en place de règles de filtrage sous Debian avec Netfilter nftables
date: 2025 / 2026
---

Ce TP est une réécriture du sujet Netfilter `iptables` **en version `nftables`**.

## Contexte

Vous êtes administrateur système dans une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu avec **nftables** afin de :

1. **Autoriser uniquement les connexions SSH provenant du réseau local.**
2. **Bloquer tout autre trafic entrant**, à l'exception des **réponses aux connexions sortantes légitimes**.
3. **Permettre l'accès HTTP/HTTPS (ports 80 et 443) uniquement depuis une plage IP spécifique.**
4. **Journaliser dans les logs système toutes les connexions bloquées.**

La configuration du pare-feu devra être **persistante**, c'est-à-dire automatiquement restaurée après un redémarrage.

Vous devez également écrire un **script shell** automatisant la configuration, et faire en sorte qu'un **utilisateur non privilégié** puisse exécuter ce script.

Vous utiliserez des outils comme `ping`, `curl`, `nc` ou `nmap` pour vérifier le comportement du pare-feu depuis différentes machines ou réseaux.

## Rappels : syntaxe de base nftables

La syntaxe `nftables` repose sur une logique différente d'`iptables` :

- On manipule des **tables**
- Chaque table contient une ou plusieurs **chains**
- Les règles sont écrites dans ces chains
- Les règles s'expriment sous forme déclarative, par exemple :

```sh
nft add rule inet filter input iif eth0 tcp dport 22 accept
```

## Aide à la construction du script

:::tip
Exemple de structure générale d'un script nftables :

```sh
#!/usr/bin/env bash

# 1. Installation des packages nécessaires : nftables

# 2. Suppression des règles existantes
nft flush ruleset

# 3. Création de la table et des chaînes
nft add table inet filter
nft add chain inet filter input   { type filter hook input priority 0 \; policy drop \; }
nft add chain inet filter forward { type filter hook forward priority 0 \; policy drop \; }
nft add chain inet filter output  { type filter hook output priority 0 \; policy accept \; }

# 4. Règles générales (équivalent policies)
# - accepter les connexions établies
# - accepter le trafic loopback

# 5. Cas particuliers (ajout des règles spécifiques)

# 6. Rendre la configuration persistante

# 7. Documentation et configuration des droits d'accès du script
```

:::

## Indications techniques pour réussir le TP

### Autoriser les connexions établies

Avec nftables :

```sh
nft add rule inet filter input ct state established,related accept
```

### Autoriser l'accès SSH uniquement depuis le réseau local

Par exemple, pour un réseau local : `192.168.1.0/24`

```sh
nft add rule inet filter input ip saddr 192.168.1.0/24 tcp dport 22 accept
```

### Autoriser HTTP/HTTPS uniquement depuis une plage IP spécifique

Exemple : `203.0.113.0/28`

```sh
nft add rule inet filter input ip saddr 203.0.113.0/28 tcp dport { 80, 443 } accept
```

### Journaliser les paquets bloqués

```sh
nft add rule inet filter input log prefix "NFT-DROP: " level info
```

:::warn
Le log devra être placé **avant** le drop final si vous utilisez une `chain` explicitement terminée par un `drop` implicite (`policy drop`).
:::

### Rendre la configuration persistante

Package Debian :

```sh
sudo apt install nftables
sudo systemctl enable nftables
```

Le fichier permanent sera alors dans :

```
/etc/nftables.conf
```

## Livrables attendus

1. **Un script `firewall.sh` fonctionnel**, appliquant l'ensemble de la configuration nftables et assurant la persistance.
2. **Une capture d'écran ou un rapport** montrant les tests réalisés (`curl`, `ping`, `nmap`…).
3. **Une explication claire des droits d'exécution du script**, justifiant comment un utilisateur non privilégié peut l'exécuter sans disposer d'un accès root complet.
