---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Le Shell
layout: '@layouts/CoursePartLayout.astro'
---

# Personnalisation et utilisation de l’environnement du shell

---

## Le shell

- Programme qui exécute les commandes dans le terminal
- `sh` : Bourn Shell, historique, standard, "portable"
- `bash` : Bourn Again Shell Linux, le plus utilisé
- Interactif / Non-interactif
- Shell de Login
- Voir [ces rappels sur la ligne de commande](https://linux.goffinet.org/administration/le-shell/la-ligne-de-commande/)

---

## Fonctions et variables

- Possibilité d'utiliser / ajouter des fonctions (voir TP)
- `ma_var=2` : `ma_var` vaut `2` (pas de type)
- `$ma_var` : contenu de `ma_var`
- Variable `PATH` : lien entre nom de commande et chemin du programme
- Variable `HOME` : chemin du _home_ de l'utilisateur (`/root` ou `/home/…`)

---

# Personnalisation ou écriture de scripts simples

- `for`, `while`, `if`, `&&,` `||`
- `read`, `seq`
- `exec`
- `$?` : code de retour (`exit …`) - `0` si OK
- `|` (pipe) : redirige stdout vers stdin prochaine commande
- `#!/usr/bin/env bash` : shebang
- `chmod +x` : rend le script exécutable

---

<!-- Annexe : liste des TPs -->

[tp-ligne-commande]: tp-ligne-commande.md
[tp-systeme]: tp-systeme.md
[tp-grub]: tp-grub.md
[tp-shared-lib]: tp-shared-lib.md
[tp-sysv-systemd]: tp-sysv-systemd.md
[tp-rpm-apt]: tp-rpm-apt.md
[tp-texte]: tp-texte.md
[tp-fichiers]: tp-fichiers.md
[tp-redirections]: tp-redirections.md
[tp-process]: tp-process.md
[tp-fichiers-avance]: tp-fichiers-avance.md
[tp-partitions]: tp-partitions.md

[tp-ligne-commande]: tp-ligne-commande.md
[tp-systeme]: tp-systeme.md
[tp-grub]: tp-grub.md
[tp-shared-lib]: tp-shared-lib.md
[tp-sysv-systemd]: tp-sysv-systemd.md
[tp-rpm-apt]: tp-rpm-apt.md
[tp-texte]: tp-texte.md
[tp-fichiers]: tp-fichiers.md
[tp-redirections]: tp-redirections.md
[tp-process]: tp-process.md
[tp-fichiers-avance]: tp-fichiers-avance.md
[tp-partitions]: tp-partitions.md
[tp-cron]: tp-cron.md
[tp-lang]: tp-lang.md
[tp-smtp]: /cours/cloud/exo-smtp.md
[tp-syslog]: tp-syslog.md
[tp-network]: tp-network.md
[tp-security]: tp-security.md
[tp-ssh-gpg]: tp-ssh-gpg.md

