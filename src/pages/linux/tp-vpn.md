---
title: TP Installation d'un service VPN
date: 2025 / 2026
---

Voici une configuration de base de WireGuard pour établir un VPN entre deux machines : un serveur et un client.

## 🌐 Activation du routage sur le serveur

Configurer le paramètre `ip_forward` du noyau et rendre le changement persistant :

```ini
# /etc/sysctl.conf
net.ipv4.ip_forward = 1
```

```sh
sudo sysctl -p
```

## 📥 Installation et configuration du serveur

1. Installer Wireguard

2. Générer des clés publiques et privées.

```sh
wg genkey | tee privatekey | wg pubkey > publickey
```

3. Configurer le fichier de configuration `/etc/wireguard/wg0.conf` côté serveur, par exemple :

```ini
# /etc/wireguard/wg0.conf
[Interface]
PrivateKey = <clé_privée_serveur>
Address = 10.0.0.1/24
ListenPort = 51820
# Autorise le routage IP
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -A FORWARD -o wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -D FORWARD -o wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
PublicKey = <clé_publique_client>
AllowedIPs = 10.0.0.2/32
```

4. Activer le service au démarrage :

```sh
sudo systemctl enable wg-quick@wg0
```

Pour démarrer le service immédiatement on pourra lancer la commande :

```sh
sudo wg-quick up wg0
```

## 🛠️ Installation et configuration du client

1. Installer Wireguard

2. Configurer le fichier de configuration `/etc/wireguard/wg0.conf` côté client, par exemple :

```ini
[Interface]
PrivateKey = <clé_privée_client>
Address = 10.0.0.2/24

[Peer]
PublicKey = <clé_publique_serveur>
Endpoint = <IP_publique_du_serveur>:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

3. Wireguard inclut une commande clé en main pour la création et configuration d'une interface dédiée au VPN :

```sh
sudo wg-quick up wg0
```

## ✅ Vérification de la connexion

1. Visualiser la configuration Wireguard :

```sh
sudo wg show
```

2. Utiliser les utilitaires réseau standard :

```sh
ip addr show
ping 10.0.0.1
ping 10.0.0.2
```

