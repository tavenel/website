---
title: TP - Mise en place d'un partage NFS (Network File System) sous Debian
---

## 🎯 Objectifs

- Installer et configurer un serveur NFS sous Debian.
- Exporter un dossier pour un ou plusieurs clients Linux.
- Monter un partage NFS manuellement et automatiquement.
- Vérifier les permissions et la sécurité des partages NFS.

## 🧠 Pré-requis

- Deux machines virtuelles Debian (ou équivalent Linux) :
  - **Serveur NFS** : `nfs-server`
  - **Client NFS** : `nfs-client`
- Accès root sur les deux systèmes.
- Connectivité réseau entre les deux (ping OK) sur le CIDR 192.168.56.0/24 (adapter le TP si un autre CIDR est utilisé).

## 🪜 Étapes du TP

### 1️⃣ Installation du serveur NFS

Sur le serveur :

```bash
sudo apt update
sudo apt install nfs-kernel-server -y
```

Créer le répertoire à partager :

```bash
sudo mkdir -p /srv/partage_nfs
sudo chown nobody:nogroup /srv/partage_nfs
sudo chmod 755 /srv/partage_nfs
```

### 2️⃣ Configuration des exports

Éditer le fichier `/etc/exports` :

```bash
sudo nano /etc/exports
# ou
sudo vi /etc/exports
```

Ajouter la ligne suivante :

```
/srv/partage_nfs 192.168.56.0/24(rw,sync,no_subtree_check)
```

:::tip
💡 *Explications :*

- `rw` : lecture/écriture autorisée (sinon `ro` pour lecture seule)
- `sync` : écriture synchrone (plus sûr)
- `subtree_check` : si un répertoire est exporté au lieu d'un système de fichiers complet, l'hôte doit vérifier l'emplacement des fichiers et des répertoires sur le système de fichiers hôte.
- `no_subtree_check` : l'hôte ne doit pas vérifier l'emplacement des fichiers accédés dans le système de fichiers hôte.
- `sync` : garantit que l'hôte conserve la synchronisation des modifications écrites dans le répertoire partagé.
- `async` : ignore les vérifications de synchronisation au profit d'une vitesse accrue.
- `no_root_squash` : option extrêmement dangereuse qui accorde aux utilisateurs `root` distants les mêmes privilèges qu'à l'utilisateur `root` de la machine hôte.
:::

Appliquer la configuration :

```bash
sudo exportfs -rav
sudo systemctl restart nfs-kernel-server
```

Vérifier :

```bash
sudo exportfs -v
showmount -e server_IP
```

### 3️⃣ Configuration du client NFS

Installer le client :

```bash
sudo apt update
sudo apt install nfs-common -y
```

Créer le point de montage :

```bash
sudo mkdir -p /mnt/nfs_partage
```

Monter le partage :

```bash
sudo mount 192.168.56.10:/srv/partage_nfs /mnt/nfs_partage
# ou en spécifiant explicitement les options de montage :
sudo mount -t nfs -o vers=4 192.168.1.102:/srv/nfs /mnt/nfs
```

Vérifier le montage :

```bash
df -h | grep nfs
```

Créer un fichier test :

```bash
touch /mnt/nfs_partage/test.txt
ls -l /mnt/nfs_partage/
```

### 4️⃣ Montage automatique au démarrage

Sur le client, éditer `/etc/fstab` :

```bash
sudo nano /etc/fstab
```

Ajouter la ligne suivante :

```
192.168.56.10:/srv/partage_nfs  /mnt/nfs_partage  nfs  defaults  0  0
```

Tester :

```bash
sudo umount /mnt/nfs_partage
sudo mount -a
```

Vérifier que le partage est monté automatiquement.

### 5️⃣ Sécurisation

- Restreindre l'accès à un seul client dans `/etc/exports` :

  ```
  /srv/partage_nfs 192.168.56.20(rw,sync,no_subtree_check)
  ```
- Mettre en place un firewall (`ufw` ou `nftables`) pour limiter l'accès au port NFS (2049/tcp).

## 🔍 Vérifications

Sur le **serveur** :

```bash
showmount -e
```

Sur le **client** :

```bash
# Afficher les partages NFS exportés
showmount -e server_IP
# Vérifier les montages
mount | grep nfs
# Vérifier les écoutes du serveur NFS
rpcinfo -p server_IP
```

:::warn
Attention dans le cas d'utilisation d'un conteneur (par exemple LXC), par défaut le conteneur n'a **pas la capacité kernel requise pour monter le pseudo-système NFS**:

- le conteneur n'a pas accès aux modules noyau (`modprobe`, `lockd`, `sunrpc`…),
- il ne peut pas monter des pseudo-systèmes (`proc`, `sysfs`, `rpc_pipefs`) sauf s'ils sont explicitement autorisés,
- et il ne dispose pas de certaines capabilities nécessaires (`SYS_ADMIN`, `DAC_READ_SEARCH`, etc.).

```bash
sudo systemctl list-units --failed
  UNIT                 LOAD   ACTIVE SUB    DESCRIPTION
* run-rpc_pipefs.mount loaded failed failed RPC Pipe File System
```
:::

## 🚀 Pour aller plus loin

- <https://linux-nfs.org>
- <https://documentation.ubuntu.com/server/how-to/networking/install-nfs/>
- <https://help.ubuntu.com/community/NFSv4Howto>
- <https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_using_network_file_services/deploying-an-nfs-server>
- <https://www.redhat.com/en/blog/configure-nfs-linux>
- <https://linuxconfig.org/how-to-configure-nfs-on-linux>

