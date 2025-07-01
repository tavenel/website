---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Le Shell
layout: '@layouts/CoursePartLayout.astro'
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

## Personnalisation ou écriture de scripts simples

- `for`, `while`, `if`, `&&,` `||`
- `read`, `seq`
- `exec`
- `$?` : code de retour (`exit …`) - `0` si OK
- `|` (pipe) : redirige stdout vers stdin prochaine commande
- `#!/usr/bin/env bash` : shebang
- `chmod +x` : rend le script exécutable

---

