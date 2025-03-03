---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Cours Linux - B3 ASRBD
tags:
- linux
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

# Disques, systèmes de fichiers Linux, arborescence de fichiers standard (FHS)

[TODO]

---


# Gestion des permissions et de la propriété sur les fichiers

[TODO]

