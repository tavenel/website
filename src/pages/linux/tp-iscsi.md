---
title: TP Introduction et mise en œuvre d'iSCSI
date: 2025 / 2026
---

## 🎯 Objectifs pédagogiques

- Mettre en place un serveur iSCSI (target) et un client (initiator) sous Linux.
- Configurer la découverte, la connexion et le montage d’un volume iSCSI.
- Automatiser la reconnexion au démarrage du système.

## 🧩 Environnement de TP

### Configuration recommandée sous VirtualBox

| Machine | Rôle | OS recommandé | Interface réseau | Disque |
|----------|------|----------------|------------------|--------|
| `iscsi-target` | Serveur iSCSI | Debian 13 ou Ubuntu Server 24.04 | Réseau interne `iscsi-net` | 20 Go (dont 10 Go pour le LUN) |
| `iscsi-initiator` | Client iSCSI | Debian 13 ou Ubuntu Server 24.04 | Réseau interne `iscsi-net` | 10 Go |

### Préparation réseau
Assurez-vous que :
- Les deux VMs sont sur le même réseau interne (`iscsi-net`).
- Elles peuvent se **pinguer** mutuellement.

Exemple :
```bash
# Sur iscsi-target
ip addr add 192.168.50.10/24 dev eth1

# Sur iscsi-initiator
ip addr add 192.168.50.20/24 dev eth1
````

---

## 🧱 Configuration du serveur iSCSI Target

### Installation du paquet

```bash
sudo apt update
sudo apt install targetcli-fb -y
```

### Création d'un disque virtuel pour le LUN

```bash
sudo mkdir -p /srv/iscsi_disks
sudo dd if=/dev/zero of=/srv/iscsi_disks/disk01.img bs=100M count=10
```

### Configuration avec `targetcli`

Lancez l’outil d’administration interactif :

```bash
sudo targetcli
```

Puis exécutez les commandes suivantes dans le shell `targetcli` :

```
/> backstores/fileio create disk01 /srv/iscsi_disks/disk01.img 1G
/> iscsi/ create iqn.2025-10.local.iscsi:target01
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/luns/ create /backstores/fileio/disk01
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/acls/ create iqn.2025-10.local.iscsi:initiator01
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/portals/ create 192.168.50.10
/> saveconfig
/> exit
```

### Vérification du service

```bash
sudo systemctl enable target.service --now
sudo targetcli ls
```

## 💻 Configuration du client iSCSI Initiator

### Installation du client

```bash
sudo apt update
sudo apt install open-iscsi -y
```

### Définir l'IQN du client

Fichier : `/etc/iscsi/initiatorname.iscsi`

```bash
InitiatorName=iqn.2025-10.local.iscsi:initiator01
```

Redémarrer le service :

```bash
sudo systemctl restart iscsid
```

### Découverte des targets disponibles

```bash
sudo iscsiadm -m discovery -t sendtargets -p 192.168.50.10
```

Vous devriez voir quelque chose comme :

```
192.168.50.10:3260,1 iqn.2025-10.local.iscsi:target01
```

### Connexion à la target

```bash
sudo iscsiadm -m node --targetname iqn.2025-10.local.iscsi:target01 --portal 192.168.50.10:3260 --login
```

Vérifiez :

```bash
lsblk
```

Vous devriez voir un nouveau disque (`/dev/sdb` par exemple).

## 🧮 Utilisation du volume iSCSI

### Création d'un système de fichiers

```bash
sudo mkfs.ext4 /dev/sdb
```

### Montage du volume

```bash
sudo mkdir /mnt/iscsi
sudo mount /dev/sdb /mnt/iscsi
```

### Automatisation du montage au démarrage

Ajoutez dans `/etc/fstab` :

```
/dev/sdb    /mnt/iscsi    ext4    _netdev    0    0
```

## 🔒 Sécurisation avec CHAP

### Côté Target

```bash
sudo targetcli
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1 set attribute authentication=1
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/acls/iqn.2025-10.local.iscsi:initiator01 set auth userid=admin
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/acls/iqn.2025-10.local.iscsi:initiator01 set auth password=supersecret
/> saveconfig
/> exit
```

### Côté Initiator

Fichier : `/etc/iscsi/iscsid.conf`

```bash
node.session.auth.authmethod = CHAP
node.session.auth.username = admin
node.session.auth.password = supersecret
```

Reconnectez ensuite :

```bash
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.50.10 --logout
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.50.10 --login
```


## 📚 Pour aller plus loin

- Documentation officielle : [https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/storage_administration_guide/index](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/storage_administration_guide/index)
- RFC iSCSI : [RFC 3720](https://datatracker.ietf.org/doc/html/rfc3720)

