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

---

