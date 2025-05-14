---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Cours Linux recherche de fichiers
layout: '@layouts/CoursePartLayout.astro'
---

# Recherche de fichiers et placement des fichiers aux endroits adéquats

---

## find

- Recherche récursive dans un répertoire des **chemins** de fichiers
- critères de recherche nom, type, date, taille utilisateur, ...
- pas de cache

---

## locate

- Interroge une BD des noms de fichiers (cache)
- `updatedb` met à jour le cache

---

## which

- Inverse du `$PATH` : retourne le chemin vers la commande
- `which <commande>` ou `which -a <commande>`

---

## type

- Similaire à `which`
- Ajoute le type de fichier
- `type [-a] [-t] <commande>`

---

## whereis

- Similaire à `which` mais ajoute les _man page_ et le code source
- `whereis [-b|m|s] <commande>` pour limiter la sortie au binaire / man page / source code

---

## Fichiers temporaires (FHS v3)

- `/tmp` : volatile
  + peut être effacé à l'arrêt du programme
  + (normalement) nettoyé au redémarrage
- `/var/tmp` : persistant
  + (normalement) conservé au redémarrage
- `/run` : données runtime (`pid`, ...)
  + précédemment `/var/run`

---

- Pour un rappel de la hierarchie standard des fichiers (FHS), voir le cours _104.7 Find system files and place files in the correct location_, p.524
- Voir le TP dédié [tp-fichiers-avance][tp-fichiers-avance].

---

![Les différents répertoires de la Filesystem Hierarchy Standard](@assets/linux/fhs.png)

<div class="caption">Les différents répertoires de la Filesystem Hierarchy Standard (FHS)</div>

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

