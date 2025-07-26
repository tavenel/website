---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Recherche de fichiers et placement des fichiers aux endroits adéquats
layout: '@layouts/CoursePartLayout.astro'
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

- Pour un rappel de la hierarchie standard des fichiers (FHS), voir le cours _104.7 Find system files and place files in the correct location_, p.524 de la certification LPIC-1.
- Voir le TP dédié [tp-fichiers-avance][tp-fichiers-avance].

---

![Les différents répertoires de la Filesystem Hierarchy Standard](@assets/linux/fhs.png)

<div class="caption">Les différents répertoires de la Filesystem Hierarchy Standard (FHS)</div>

[tp-fichiers-avance]: /linux/tp-fichiers-avance

---

