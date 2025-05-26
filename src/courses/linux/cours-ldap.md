---
title: LDAP
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
date: 2024 / 2025
---

## 🧠 LDAP : Lightweight Directory Access Protocol

- Protocole standardisé d’accès à un **annuaire centralisé**
- Structure hiérarchique (arbre DIT - _Directory Information Tree_)
- Utilisé pour stocker des informations : utilisateurs, groupes, appareils, etc.
- Très utilisé pour l'authentification (ex : Active Directory, SSO, Samba)

📚 Serveur libre le plus courant : **OpenLDAP**

### 📦 Installation

```sh
sudo apt install slapd ldap-utils
```

🧙 Suivre l’assistant pour configurer le client LDAP : `dpkg-reconfigure slapd`

## 📂 Fichiers importants

- `/etc/ldap/ldap.conf` (remplacé par `/etc/ldap/slapd.d/`) : config client
- `/var/lib/ldap/` : base de données LDAP

## 🌲 Structure de l'annuaire LDAP (DIT)

🗂️ Organisation en arbre (inversé) :

```
dc=example,dc=com
├── ou=people
│ └── uid=alice
├── ou=groups
│ └── cn=admins
```

### 📌 Principaux types d’objets

- `dc` : composant de domaine
- `ou` : unité d’organisation
- `uid` : utilisateur
- `cn` : nom commun

💡 Les objets sont définis par des **schemas** (modèles)

## 🛠️ Ajouter des entrées LDAP

📄 Exemple de fichier LDIF (LDAP Data Interchange Format) :

```ldif
dn: uid=alice,ou=people,dc=example,dc=com
objectClass: inetOrgPerson
uid: alice
sn: Dupont
cn: Alice Dupont
userPassword: {SSHA}motdepasse
```

🔐 Mot de passe SSHA généré par :

```sh
slappasswd
```

💾 Ajouter à l’annuaire :

```sh
ldapadd -x -D "cn=admin,dc=example,dc=com" -W -f alice.ldif
```

## 🔍 Rechercher des entrées LDAP

🔎 Utiliser `ldapsearch` :

```sh
ldapsearch -x -b "dc=example,dc=com" "(objectClass=inetOrgPerson)"
```

### 📌 Principaux filtres

- `(uid=alice)` : utilisateur précis
- `(sn=Dupont)` : nom de famille
- `(&(objectClass=*)(uid=*))` : tout

## 🔧 Intégration LDAP avec PAM/NSS (authentification du système)

- Utilisateurs LDAP visibles via `getent passwd`
- Connexion possible en SSH (si autorisée)

📦 Paquets requis :

```sh
sudo apt install libnss-ldap libpam-ldap nscd
```

🧙 Suivre l’assistant pour configurer le client LDAP

