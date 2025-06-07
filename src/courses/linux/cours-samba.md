---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Samba - partage de fichiers Linux et Windows
layout: '@layouts/CoursePartLayout.astro'
---

## 🌐 Samba

- Partage de fichiers et d'imprimantes entre systèmes Linux/Unix et Windows
- Intégration dans un domaine _Active Directory_ (AD)
- Gestion des utilisateurs et des autorisations (comme un contrôleur de domaine)
📡 Implémente le protocole _SMB/CIFS_ (_Server Message Block_).

---

## 🏗️ Architecture

- **smbd** : Service principal de partage de fichiers
- **nmbd** : Gestion des noms NetBIOS (découverte réseau)
- **winbindd** : Intégration à Active Directory

📁 Samba permet aux clients :

- Windows de voir des partages Linux
- Linux de monter des partages Windows (`cifs`)

---

## 🔐 Sécurité et gestion des droits

🧾 Contrôle d'accès :

- Droits Unix classiques (`chmod`, `chown`)
- Contrôle via Samba (`valid users`, `write list`, etc.)

🛡️ Modes de sécurité dans Samba :

- **security = user** (recommandé)
- **security = share** (ancien, obsolète)
- **security = domain / ads** (intégration Active Directory)

---

## 🔧 Dépannage

🛠️ Commandes utiles :

- `testparm` : vérifier la syntaxe de `smb.conf`
- `smbclient -L //localhost -U utilisateur` : liste des partages
- `systemctl status smbd`
- `netstat -tuln | grep 445` : vérifier le port SMB

📄 Logs :
- `/var/log/samba/log.smbd`
- `/var/log/syslog` ou `journalctl -xe`

---

## 🛠️ Exemple de configuration `/etc/samba/smb.conf`

```ini
[global]
   workgroup = WORKGROUP
   server string = Serveur Samba
   security = user
   map to guest = Bad User

[partage]
   path = /srv/samba/partage
   browsable = yes
   read only = no
   guest ok = yes
```

---

✅ Créer le dossier et ajuster les droits :

```sh
sudo mkdir -p /srv/samba/partage
sudo chmod -R 0775 /srv/samba/partage
```

👥 Ajouter un utilisateur au système Samba :

```sh
sudo smbpasswd -a alice
```

✅ Tester l’accès depuis un client :

- Windows : `\\IP_serveur\partage`
- Linux : `smbclient //IP/partage -U alice`

---

