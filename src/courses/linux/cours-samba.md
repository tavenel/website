---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Samba - partage de fichiers Linux et Windows
layout: '@layouts/CoursePartLayout.astro'
---

## 🌐 Samba

- Partage de fichiers et d'imprimantes entre systèmes Linux/Unix et Windows
- Intégration dans un domaine _Active Directory_ (AD)
- Gestion des utilisateurs et des autorisations (comme un contrôleur de domaine)
- 📡 Implémente le protocole _SMB/CIFS_ (_Server Message Block_).

:::link
Pour plus d'information, voir le document de la formation LPIC-2 :

- [SAMBA Server Configuration](https://lpic2book.github.io/src/lpic2.209.1/)
:::

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

✅ Tester l'accès depuis un client :

- Windows : `\\IP_serveur\partage`
- Linux : `smbclient //IP/partage -U alice`

---

## 💡 Comment intégrer LDAP avec Samba

1. Utiliser `smbldap-tools` pour générer les schémas LDAP pour Samba :
  - `smbldap-config`
  - `smbldap-populate`
2. Création d'un utilisateur Samba :
  - Récupérer le SID local => `BASE_SID=$(net getlocalsid)`
  - Calculer le SID du user Samba => `SAMBA_SID="${BASE_SID}-$((USER_UID * 2 + 1000))`

Exemple de LDIF Samba :

```
# smbuser.ldif

dn: uid=smbuser,ou=people,dc=example,dc=com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: sambaSamAccount
cn: SMB User
sn: User
uid: smbuser
uidNumber: 10001
gidNumber: 100
homeDirectory: /home/smbuser
loginShell: /bin/bash
sambaSID: # TODO REPLACE
# sambaNTPassword: <NT_HASH>
sambaAcctFlags: [U]
```

```sh
# Ajout de l'utilisateur au LDAP
ldapadd … -f smbuser.ldif
# Complète le champ `sambaNTPassword` (sinon à calculer manuellement)
sudo smbpasswd -a smbuser

# Vérification de la disponibilité du point de montage
smbclient -L //localhost -U smbuser
```

---
