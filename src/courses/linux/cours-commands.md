---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Commandes GNU et Unix
layout: '@layouts/CoursePartLayout.astro'
---

Voir les rappels de cours sur les commandes de base d'un système Linux.

---

# Travail en ligne de commande

- Échapper les caractères spéciaux avec `"` et `'`
- Wildcards `*`, `?`, `[a-zA-Z]`, `{toto,titi}`
- Voir le cours _Quoting to Escape Special Characters_, 103.1 Lesson 2 p.185
- Voir le cours _Types of Wildcards_, 103.3 Lesson 1 p.238
- Voir la page (FR) [wikiversité sur les filtres](https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Ex%C3%A9cution_de_flux_de_textes_en_utilisant_des_filtres)
- Voir le TP dédié [tp-ligne-commande][tp-ligne-commande].

---

# Traitement de flux de type texte avec des filtres

Voir le TP dédié [tp-texte][tp-texte].

### Démo

---

# Gestion élémentaire des fichiers

---

- Voir les rappels de cours sur les fichiers dans un système Linux.
- Voir la page (FR) [wikiversité sur la gestion des fichiers](https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Gestion_de_base_des_fichiers)

---

# Types de fichiers

- Fichier standard : majorité des fichiers : données, configurations, binaires, ...
- Répertoires : fichier spécial contenant d'autres fichiers
- Autres fichiers spéciaux (par exemple pour les entrées/sorties)

---

# Commandes utiles

- `touch`, `ls`
- `mkdir`, `rmdir`
- `cp`, `mv`, `rm`
- `find`, `file`
- `dd`, `tar`, `cpio`, `gzip`, `gunzip`, `bzip2`, `bunzip2`
- Voir le TP dédié [tp-fichiers][tp-fichiers].

### Démo

---

# Utilisation des flux, des pipes et des redirections

---

Concepts fondamentaux dans les systèmes Unix/Linux, permettant de gérer efficacement les entrées/sorties des commandes et de manipuler les données dans le terminal.

- Voir rappels de cours sur les flux, les pipes et les redirections.
- Voir aussi la [wikiversité sur les redirections](https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Utiliser_les_streams,_pipes,_et_redirections)

---

## Les Trois Flux Standard

Les commandes reçoivent et envoient des données via trois flux standard :

- Entrée standard (`stdin`) : Flux de données d'entrée provenant du clavier ou d'un fichier.
- Sortie standard (`stdout`) : Flux de données de sortie affichées à l'écran.
- Erreur standard (`stderr`) : Flux de messages d'erreur affichés à l'écran.

---

## Redirections

Les redirections permettent de gérer les flux standard :

- `>` : Redirige la sortie standard vers un fichier (`commande > fichier`).
- `2>` : Redirige la sortie d'erreur vers un fichier (`commande 2> fichier`).
- `>>` : Ajoute la sortie standard à la fin d'un fichier (`commande >> fichier`).
- `2>>` : Ajoute la sortie d'erreur à la fin d'un fichier (`commande 2>> fichier`).
- `<` : Redirige l'entrée standard depuis un fichier (`commande < fichier`).

### Démo

---

## Pipes

- Permettent de connecter la sortie d'une commande à l'entrée d'une autre :

```sh
commande1 | commande2
```

---

## Exemples

- `ls | grep keyword` : Recherche un mot clé dans la liste des fichiers.
- `cat fichier.txt | grep pattern` : Recherche un motif dans le contenu d'un fichier. (équivalent `grep pattern fichier.txt`)
- `ps aux | sort -nrk 3,3 | head` : Trie et affiche les processus avec la plus grande utilisation de CPU.
- `commande 2>&1` : Redirige la sortie d'erreur vers la sortie standard.
- Voir le TP dédié [tp-redirections][tp-redirections].

---

# Création, contrôle et interruption des processus

---

Voir rappels de cours sur les processus.

---

# Modification des priorités des processus

- priorité demandée par l'utilisateur : `nice` (-20 à 20)
  - champ `NI` de `ps`
- transformé par le scheduler en priorité effective (0 à 100)
  - champ `PRI` de `ps`

---

# Commandes utiles

- `ps` (`ps aux`), `top`, `pgrep`, `watch`
- `kill`, `pkill`, `killall`
- `nice`, `renice`
- fichiers `/proc/<PID>`

Voir cours LPIC-1 section _Process Monitoring_, 103.5 Lesson 1 p.295

### Démo

---

# Jobs

- Processus démarré interactivement dont l'exécution continue en arrière-plan
- `jobs`, `fg`, `bg`, `&`, `nohup`

Voir cours LPIC-1 section _Job Control_, 103.5 Lesson 1 p.290

### Démo

---

Voir le TP dédié [tp-process][tp-process].

---

# Multiplexers de terminal

- `tmux` (le plus utilisé)
- `screen`  
- d'autres existent (bien moins utilisés)
- gèrent des _sessions_ de terminal en mode client/serveur :
  - écran découpé pour tourner des commandes en parallèle
  - déconnexion et reconnexion sans perdre l'exécution des commandes
  - très utiles pour gérer un serveur

Voir cours LPIC-1 section _Features of Terminal Multiplexers_, 103.5 Lesson 2 p.318

---

# Recherche dans des fichiers texte avec les expressions rationnelles

---

# Quelques caractères spéciaux

- `.` : n'importe quel caractère
- `^` : début de ligne
- `$` : fin de ligne
- `[ati]` : un caractère `a` ou `t` ou `i` 
- `[^ati]` : un caractère **sauf** `a`, `t`, `i`
- `[0-9]`, `[a-z]` : un chiffre entre `0` et `9`, un caractère entre `a` et `z`
- `?`, `*`, `+` : un caractère, 0 ou plusieurs caractères, au moins un caractère
- `\` : caractère d'échappement pour `.^$*[](){}|\` (ex: `\*` : caractère `*`)

---

- Voir cours LPIC-1 section "103.7 Lesson 1" sur les expressions régulières, p.361
- Voir la partie sur les expressions régulières du TP sur les flux de texte [tp-texte][tp-texte].
- Voir la [wikiversité sur les regex](https://fr.wikiversity.org/wiki/Certification_Linux_LPI/Administrateur_syst%C3%A8me_d%C3%A9butant/Examen_101/GNU_et_commandes_Unix/Expressions_r%C3%A9guli%C3%A8res)

---

# Commandes utiles

- `grep`, `egrep`, `fgrep` : recherche avec regex simples, avec regex étendues (idem `grep -E`), sans regex
- `sed` : modifications de flux de texte

Voir cours LPIC-1 section "103.7 Lesson 2" sur `grep` et `sed` p.372

### Démo

---

# Édition de fichier simple (vi)

---

# vi

- `vi` : éditeur de texte en mode console
- plusieurs _modes_ : `normal`, `insertion`, `command`
- édition de texte très efficace 
- POSIX
- successeurs : `vim`, `neovim`
- Voir cours LPIC-1 section 103.8 _Basic file editing_ p.390
- **Pour une introduction à `vi`, utiliser l'excellent tutoriel intégré : taper `vimtutor` dans un terminal.**

### Démo + grep

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

