---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Compilation et installation de programmes à partir des sources
layout: '@layouts/CoursePartLayout.astro'
---

## 🌟 Avantages

Compiler un logiciel depuis ses sources permet :

- d'avoir un meilleur contrôle sur la version et les fonctionnalités,
- d'optimiser la compilation pour sa machine,
- mais cela demande plus de rigueur dans la gestion des dépendances et des mises à jour.

## 📁 Structure typique d'un logiciel source

Les logiciels libres sont souvent distribués sous forme d'archives compressées traditionnellement extraites dans des emplacements spécifiques :

- `/usr/src/` : utilisé par le noyau Linux ou des logiciels spécifiques
- `/usr/local/src/` : emplacement privilégié pour des compilations manuelles
- `~/…` (répertoire utilisateur) : recommandé pour une compilation non-root

Une fois extrait, un logiciel source contient généralement :

- un fichier `README` ou `INSTALL`
- un script `configure` : configuration du build
- un fichier `Makefile` : cibles pour `make`
- un répertoire `src/` contenant les sources en C/C++

:::tip
L'utilitaire `patch` permet d'appliquer des correctifs au code source principal.
:::

:::tip
Il peut être utile d'utiliser le gestionnaire de paquets pour installer / upgrader automatiquement les sources des dépendances nécessaires (paquets `…-src`, `…-dev`, …).
:::

---

## 📦 Compilation avec `configure` et `make`

```sh
# Compilation et installation :

cd monlogiciel-1.0/
./configure         # Prépare l'environnement de compilation
make                # Compile le programme
sudo make install   # Installe les fichiers dans le système
```

Paramètres courants pour `./configure` :

- `--prefix=/opt/logiciel` : définir le répertoire d'installation
- `--enable-feature` / `--disable-feature` : activer/désactiver des fonctionnalités

```sh
# Nettoyage :

make clean       # Supprime les fichiers objets
make distclean   # Supprime aussi les fichiers générés par configure
```

---

