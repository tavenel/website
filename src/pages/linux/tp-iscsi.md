---
title: TP Introduction et mise en œuvre d'iSCSI
date: 2025 / 2026
---

## 🎯 Objectifs pédagogiques

- Mettre en place un serveur iSCSI (target) et un client (initiator) sous Linux.
- Configurer la découverte, la connexion et le montage d'un volume iSCSI.
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

Lancez l'outil d'administration interactif :

```bash
sudo targetcli
```

Puis exécutez les commandes suivantes dans le shell `targetcli` :

```
/> backstores/fileio create disk01 /srv/iscsi_disks/disk01.img 1G
/> iscsi/ create iqn.2025-10.local.iscsi:target01
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/luns/ create /backstores/fileio/disk01
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/acls/ create iqn.2025-10.local.iscsi:initiator01
/> saveconfig
/> exit
```

#### 🧩 Étapes détaillées

```bash
/> backstores/fileio create disk01 /srv/iscsi_disks/disk01.img 1G
```

➡️ Crée un **backstore de type fileio** (fichier disque virtuel) :

- Nom : `disk01`
- Fichier image : `/srv/iscsi_disks/disk01.img`
- Taille : `1G`

👉 Représente la "brique de stockage" physique exportée via iSCSI.

```bash
/> iscsi/ create iqn.2025-10.local.iscsi:target01
```

➡️ Crée une **cible iSCSI** avec l'identifiant :

```
iqn.2025-10.local.iscsi:target01
```

✅ Format : `iqn.YYYY-MM.domain:label`

```bash
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/luns/ create /backstores/fileio/disk01
```

➡️ Associe le backstore `disk01` à la cible iSCSI sous forme de **LUN** (Logical Unit Number).

* `tpg1` : Target Portal Group 1 (le groupe par défaut).

```bash
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/acls/ create iqn.2025-10.local.iscsi:initiator01
```

➡️ Crée une **ACL (Access Control List)** pour autoriser un initiateur spécifique :

```
iqn.2025-10.local.iscsi:initiator01
```

➡️ Cet IQN doit correspondre à celui du client initiateur iSCSI.

#### Choix de l'interface réseau

```bash
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/portals/ delete 0.0.0.0 3260
/> iscsi/iqn.2025-10.local.iscsi:target01/tpg1/portals/ create 192.168.50.10
```

➡️ Supprime l'**interface réseau (portal)** créée par défaut sur toutes les interfaces réseau pour en recréer un uniquement sur l'interface sur laquelle la cible écoutera :

* IP : `192.168.50.10`
* Port par défaut : `3260`

### ✅ Vérification du service

```bash
sudo targetcli ls
```

```
/backstores/fileio
    disk01  (fileio, /srv/iscsi_disks/disk01.img) write-back activated
/iscsi
    iqn.2025-10.local.iscsi:target01
        tpg1
            acls: iqn.2025-10.local.iscsi:initiator01
            luns: lun0 -> /backstores/fileio/disk01
            portals: 192.168.50.10:3260
```

## 💻 Configuration du client iSCSI Initiator

### Installation du client

```bash
sudo apt update
sudo apt install open-iscsi -y # Debian/Ubuntu
sudo dnf install iscsi-initiator-utils  # CentOS/RHEL/Fedora
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
/> cd iscsi/iqn.2025-10.local.iscsi:target01/tpg1/acls/iqn.2025-10.local.iscsi:initiator01
/> /iscsi/iqn.../tpg1> set attribute authentication=1
/> /iscsi/iqn.../tpg1> set auth userid=admin
/> /iscsi/iqn.../tpg1> set auth password=supersecret
/> cd /
/> saveconfig
/> exit
```

### Côté Initiator

Ajout des identifiants CHAP :

```bash
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.authmethod -v CHAP
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.username -v admin
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.password -v supersecret
```

Vérification :

```bash
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102 -o show | grep -A3 auth
iface.chap_auth = <empty>
iface.bidi_chap = <empty>
iface.strict_login_compliance = <empty>
iface.discovery_auth = <empty>
iface.discovery_logout = <empty>
node.discovery_address = 192.168.1.102
node.discovery_port = 3260
--
node.session.auth.authmethod = CHAP
node.session.auth.username = admin
node.session.auth.password = ********
node.session.auth.username_in = <empty>
node.session.auth.password_in = <empty>
node.session.auth.chap_algs = MD5
```

:::tip
Il est aussi possible de remplir les informations CHAP dans le fichier : `/etc/iscsi/iscsid.conf`

```bash
node.session.auth.authmethod = CHAP
node.session.auth.username = admin
node.session.auth.password = supersecret
```
:::

Reconnectez ensuite :

```bash
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.50.10 --logout
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.50.10 --login
```

### CHAP mutuel

Nous avons mis en place une authentification à sens unique mais CHAP supporte également une authentification bidirectionnelle :

- Utiliser `usename`/`password` pour que seul l'initiateur s'authentifie auprès de la cible (unidirectionnel).
- Ajouter `username_in`/`password_in` pour que l'initiateur et la cible s'authentifient mutuellement (bidirectionnel/CHAP mutuel).


| Credential | Direction | But |
|------------|-----------|-----|
| `username`/`password` | Initiator → Target | Initiator authenticates to the target. |
| `username_in`/`password_in` | Target → Initiator | Target authenticates to the initiator (Mutual CHAP). |


```bash
# target

targetcli

/> /iscsi/iqn.20...i:initiator01> set auth mutual_userid=admin2
Parameter mutual_userid is now 'admin2'.
/> /iscsi/iqn.20...i:initiator01> set auth mutual_password=supersecret2
Parameter mutual_password is now 'supersecret2'.

saveconfig
```

```bash
# initiator
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.authmethod -v CHAP
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.username -v admin
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.password -v supersecret
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.username_in -v admin2
sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102   --op update -n node.session.auth.password_in -v supersecret2

sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.1.102 -o show | grep -A3 auth
iface.chap_auth = <empty>
iface.bidi_chap = <empty>
iface.strict_login_compliance = <empty>
iface.discovery_auth = <empty>
iface.discovery_logout = <empty>
node.discovery_address = 192.168.1.102
node.discovery_port = 3260
--
node.session.auth.authmethod = CHAP
node.session.auth.username = admin
node.session.auth.password = ********
node.session.auth.username_in = admin2
node.session.auth.password_in = ********
node.session.auth.chap_algs = MD5
[…]

sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.50.10 --logout

sudo iscsiadm -m node -T iqn.2025-10.local.iscsi:target01 -p 192.168.50.10 --login
```

## 📚 Pour aller plus loin

- Documentation officielle : [https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/storage_administration_guide/index](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/storage_administration_guide/index)
- RFC iSCSI : [RFC 3720](https://datatracker.ietf.org/doc/html/rfc3720)

