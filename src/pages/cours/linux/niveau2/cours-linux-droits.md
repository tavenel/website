---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Linux - gestion des droits
tags:
- linux
---

<!-- _class: titre lead -->

# Linux - gestion des droits

_Tom Avenel_

<https://www.avenel.pro/>

<!-- _footer: "© 2025 Tom Avenel under 󰵫  BY-SA 4.0" -->

---

# Gestion des comptes utilisateurs et des groupes ainsi que des fichiers systèmes concernés

---

## Utilisateurs

- `useradd` : crée un utilisateur
- `userdel` : supprime un utilisateur
- `usermod` : modifie un utilisateur
  - `usermod --append --groups group1,group2,... username`
- `/etc/passwd` : fichier comptes utilisateurs (locaux)
- `/etc/skel/` : squelette copié dans le `home` d'un nouvel utilisateur

---

## Mots de passe

- `/etc/shadow` : fichier mots de passe (comptes locaux)
- `passwd` : changer un mot de passe
- `chage` : change l'expiration d'un mot de passe

---

## Groupes

- `/etc/group` : fichier groupes et utilisateurs rattachés
- `groupadd` : crée un groupe
- `groupdel` : supprime un groupe
- `groupmod` : modifie un groupe
  - `groupmod --new-name new_group group_name`

---

# Gestion des permissions et de la propriété sur les fichiers

---

## Les utilisateurs

- Un fichier appartient à un utilisateur et à un groupe
- trois types d'utilisateurs ayant des droits :
  - `u` (pour `user`) : l'utilisateur auquel appartient le fichier/dossier
  - `g` (pour `group`) : le groupe auquel appartient le fichier/dossier
  - `o` (pour `other`) : les autres utilisateurs

---
 
## Les droits

- `r` (`read`) : lire le fichier/dossier
- `w` (`write`) : modifier le fichier/dossier
- `x` (`execute`) : exécuter le fichier / entrer dans le dossier
- `-` : aucun droit

---

## Affichage des droits

```
$ ls -l
drwxr-xrw- [...]
```

- `d` : type de fichier (dossier)
- `rwx` : droits de l'utilisateur (propriétaire)
- `r-x` : droits du groupe
- `rw-` : droits du reste du monde

---

## Modifier les droits

- `chmod u+x mon_fichier`
- `chmod g-r mon_fichier`
- `chmod o+w mon_fichier`
- `chmod a-x mon_fichier` (all)
- `chmod -R u-x mon_dossier` : récursif
- `chmod 660 mon_fichier` : `660` est l'octal correspondant au masque `rw- rw- ---`

---

| Permission                     | `ls -l` | octal |
|--------------------------------|---------|-------|
| aucun droit                    | `- - -` |   0   |
| exécution seulement            | `- - x` |   1   |
| écriture seulement             | `- w -` |   2   |
| écriture et execution          | `- w x` |   3   |
| lecture seulement              | `r - -` |   4   |
| lecture et exécution           | `r - x` |   5   |
| lecture et écriture            | `r w -` |   6   |
| lecture, écriture et exécution | `r w x` |   7   |

---

## Droits spéciaux

---

### SUID et SGID

- `SUID`, `SGID` (_Set User/Group ID_) : lance la commande avec l'`UID` de l'utilisateur / du groupe
  - Droit `+s` ou 1er bit à 1 (user) ou 2e bit à 1 (group)
  - `chmod u+s /bin/cat`, `chmod 4xxx /bin/cat`
  - `chmod g+s /bin/cat`, `chmod 2xxx /bin/cat`
- `SGID` sur répertoire : les fichiers et sous-répertoires créés dans ce répertoire hériteront du groupe propriétaire du répertoire parent (au lieu du groupe de l'utilisateur créant les fichiers).

---

### Sticky bit

- `Sticky bit` (dossier) : seul le propriétaire d'un fichier contenu dans ce dossier pourra le supprimer ou le renommer (`/tmp`, ...).
  - Droit `+t` ou 3e bit à 1
  - `chmod o+t /home/tom/communs` ou `chmod 1xxx /home/tom/communs`

---

## Lister les groupes

- `getent group` : tous les groupes du système
- `groups tom` : groupes de l'utilisateur `tom`
- `groupmems -g video -l` : utilisateurs du groupe `video`
- En local : fichier `/etc/group`

---

## Permissions par défaut

- `umask`, `umask -S`
- masque des permissions retirées par défaut
- 1 seul masque : fichier standard idem dossier mais droit d'exécution retiré

---

## Access Control List (ACL)

- Permissions `rwx` spécifiques par utilisateur / groupe
  - possibles pour tout utilisateur et/ou groupe
  - plus fines que le triplet _user_ / _group_ / _other_

---

```bash
# Lister ACL
getfacl <nom_fichier>
# Ajouter / Modifer (-m) ACL
# setfacl -m u:<utilisateur>:<permission> <fichier>
# setfacl -m g:<groupe>:<permission> <fichier>
setfacl -m g:group1:rw fichier_test.txt
# Supprimer un ACL
setfacl -x u:<utilisateur> <fichier>
# Supprimer tous les ACL
setfacl -b <fichier>
```

---

<!-- Annexe: liste des liens utiles -->
[wiki-partitions]: https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/P%C3%A9riph%C3%A9riques_et_syst%C3%A8mes_de_fichiers_Linux/Cr%C3%A9er_des_partitions_et_des_syst%C3%A8mes_de_fichiers

<!-- class: legal -->

# Legal

- Linux est une marque déposée par Linus Torvalds aux États Unis et dans d'autres pays.
- UNIX® est une marque déposée de The Open Group. 
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
