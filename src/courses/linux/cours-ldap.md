---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: LDAP
layout: '@layouts/CoursePartLayout.astro'
---

## 🧠 LDAP : Lightweight Directory Access Protocol

- Protocole standardisé d’accès à un **annuaire centralisé**
- Structure hiérarchique (arbre DIT - _Directory Information Tree_)
- Utilisé pour stocker des informations : utilisateurs, groupes, appareils, etc.
- Très utilisé pour l'authentification (ex : Active Directory, SSO, Samba)

📚 Serveur libre le plus courant : **OpenLDAP**

:::link
Pour plus d'information, voir le document de la formation LPIC-2 :

- [LDAP client usage](https://lpic2book.github.io/src/lpic2.210.3/)
- [Configuring an OpenLDAP server](https://lpic2book.github.io/src/lpic2.210.4/)
:::

---

### 📦 Installation

```sh
sudo apt install slapd ldap-utils
```

🧙 Suivre l’assistant pour configurer le client LDAP en utilisant dpkg : `dpkg-reconfigure slapd`

---

## 📂 Fichiers importants

- `/etc/ldap/ldap.conf` (remplacé par `/etc/ldap/slapd.d/`) : config client
- `/var/lib/ldap/` : base de données LDAP

---

## 🌲 Structure de l'annuaire LDAP (DIT)

🗂️ Organisation en arbre (inversé) :

```
dc=example,dc=com
├── ou=people
│ └── uid=alice
├── ou=groups
│ └── cn=admins
```

---

### 📌 Principaux types d’objets

- `dc` : composant de domaine
- `ou` : unité d’organisation
  - parents des autres entités, similaire répertoires
- `uid` : utilisateur
- `cn` : nom commun

💡 Les objets sont définis par des **schemas** (modèles)

---

## 🛠️ Ajouter des entrées LDAP

📄 Exemple de fichier LDIF (LDAP Data Interchange Format) pour ajouter un `ou` :

```
dn: ou=people,dc=example,dc=com
objectClass: top
objectClass: organizationalUnit
ou: people
```

📄 Exemple de fichier LDIF pour ajouter un `uid` d'un utilisateur applicatif :

```
dn: uid=alice,ou=people,dc=example,dc=com
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
uid: alice
sn: Dupont
cn: Alice Dupont
userPassword: {SSHA}motdepasse
```

---

🔐 Mot de passe SSHA généré par :

```sh
slappasswd
```

💾 Ajouter à l’annuaire :

```sh
ldapadd -x -D "cn=admin,dc=example,dc=com" -W -f alice.ldif
```

:::tip
Les options `-x`, `-W` et `-D "cn=admin,dc=example,dc=com"` servent à l'authentification sur le serveur LDAP (ici en tant qu'admin) pour la commande `ldapadd`.
:::

---

### `objectClass` utiles

1. `top` : Classe racine dont héritent toutes les autres classes d'objet. Elle est abstraite et ne définit aucun attribut. Requise dans chaque entrée LDAP comme base de la hiérarchie des classes d'objet.
2. `person` : Classe de base utilisée pour représenter un individu. Souvent utilisée comme base de classes d'objets plus spécifiques.
  - `cn` (_Common Name_): Nom complet
  - `sn` (_Surname_): Nom de famille
3. `organizationalPerson` : Extension de `person` pour représenter les individus au sein d'une organisation.
  - `ou` (_Organizational Unit_) : Unité organisationnelle à laquelle appartient la personne.
  - `telephoneNumber`
  - …
4. `inetOrgPerson` (Internet Organizational Person) : Extension de `organizationalPerson` largement utilisée dans les annuaires Internet et Intranet pour représenter les personnes.
  - `mail`
  - `userPassword` (généralement stocké sous forme de hash)
  - `givenName`
  - `displayName`
  - `employeeNumber`
  - …
5. `posixAccount` : Compte utilisateur Unix
  - `uid` (identifiant utilisateur, utilisé comme nom de connexion pour le compte Unix)
  - `uidNumber` (identifiant utilisateur Unix)
  - `gidNumber` (identifiant du groupe Unix)
  - `homeDirectory` (chemin absolu vers le répertoire personnel de l'utilisateur)
  - `loginShell` (chemin vers l'interpréteur de commandes de connexion de l'utilisateur)
6. `shadowAccount` : Utilisé pour stocker les informations de la suite de mots de passe _shadow_ (attributs liés aux politiques d'expiration des mots de passe).
  - `shadowLastChange`
  - `shadowMin` 
  - `shadowMax`
  - `shadowWarning`
7. `domain` : Domaine ou zone DNS
  - `dc` (_Domain Component_)

---

## 🔍 Rechercher des entrées LDAP

🔎 Utiliser `ldapsearch` :

```sh
ldapsearch -x -b "dc=example,dc=com" "(objectClass=inetOrgPerson)"
```

---

### 📌 Principaux filtres

- `(uid=alice)` : utilisateur précis
- `(sn=Dupont)` : nom de famille
- `(&(objectClass=*)(uid=*))` : tout

---

## 🔍 Lister les _organizationalUnit_ (`ou`)

🔎 Utiliser `slapcat` :

```sh
slapcat -n 1 -a '(objectClass=organizationalUnit)' | grep '^dn'
```

---

## 🔧 Intégration LDAP avec PAM/NSS (authentification du système)

- Utilisateurs LDAP visibles via `getent passwd`
- Connexion possible en SSH (si autorisée)

📦 Paquets requis :

```sh
sudo apt install libnss-ldap libpam-ldap nscd
```

🧙 Suivre l’assistant pour configurer le client LDAP

:::tip
Il est souvent intéressant de coupler un service d'authentificatio réseau type _LDAP_ avec _Nscd_ qui cache les requêtes de service de noms (`passwd`, `group`, `host`).
:::

---

