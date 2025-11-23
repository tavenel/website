---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: PAM
layout: '@layouts/CoursePartLayout.astro'
---

## Pluggable Authentication Modules

- Modules d'authentification enfichables
- Bibliothèques permettant aux administrateurs système de définir des politiques d'authentification sans recompiler les programmes.
  - **pam_unix.so** : Authentification Unix traditionnelle.
  - **pam_ldap.so** : Authentification basée sur LDAP.
  - **pam_google_authenticator.so** : Authentification à deux facteurs utilisant Google Authenticator.
  - …
- **Configuration** : 1 fichier par service : `/etc/pam.d/sshd`, …

```
# Exemple de fichier pam.d :
auth required pam_unix.so
account required pam_unix.so
```

:::link
Pour plus d'information, voir :

- Le document de la formation LPIC-2 : [PAM authentication](https://lpic2book.github.io/src/lpic2.210.2/)
- Le blog [linuxembedded : Authentification avec PAM sous Linux](https://www.linuxembedded.fr/2025/10/authentification-avec-pam-sous-linux)

:::

---
