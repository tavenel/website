---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: NFS - Network File System
layout: '@layouts/CoursePartLayout.astro'
---

## NFS

- Protocole client / serveur de partage de fichiers (_TCP_ ou _UDP_)
- Permet à un client Linux/Unix de **monter un répertoire distant** comme s'il était local :
  - Partage de fichiers entre serveurs
  - Centralisation des données dans des environnements multi-utilisateurs
  - Montage automatique de répertoires utilisateurs dans des infrastructures réseau

---

## Configuration du serveur NFS

### Configuration

Fichier : `/etc/exports`

Exemple :

```
/srv/nfs/data 192.168.1.0/24(rw,sync,no_subtree_check)
```

- `rw` : lecture/écriture
- `sync` : données écrites immédiatement sur le disque
- `no_subtree_check` : désactive la vérification du sous-répertoire
- Les permissions sont **gérées côté serveur** : `root_squash`, `no_root_squash`, `anonuid`, `anongid`
- Par défaut, l'utilisateur root sur le client devient `nobody` sur le serveur (_squash_).

### Appliquer les exports

```sh
sudo exportfs -a           # (ré)exporte tous les partages
sudo exportfs -v           # voir les détails
```

### Services

```bash
sudo systemctl enable --now nfs-server
sudo systemctl start nfs-server
```

### Vérifier les exports disponibles

```sh
showmount -e 192.168.1.10
```

---

## Configuration du client NFS

### Monter manuellement un partage

```sh
sudo mount -t nfs 192.168.1.10:/srv/nfs/data /mnt
```

### Montage permanent avec `/etc/fstab`

```
192.168.1.10:/srv/nfs/data /mnt nfs defaults 0 0
```

### Vérification

```bash
mount | grep nfs
df -h /mnt
```

---

## NFS v3 vs v4

| Caractéristique   | NFS v3            | NFS v4                          |
| ----------------- | ----------------- | ------------------------------- |
| Support de l'état | Stateless         | Stateful                        |
| Authentification  | Basée sur UID/GID | Supporte Kerberos (`RPCSEC_GSS`) |
| Port unique       | Non               | Oui (2049)                      |
| Performances      | Bonne             | Meilleures avec cache           |

:::tip
Grâce à Kerberos et à l'utilisation d'un port unique, NFS v4 est plus sécurisé et traverse mieux les firewalls.
:::

---

