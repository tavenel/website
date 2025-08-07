---
title: TP Langue et encodage
date: 2024 / 2025
---

## Encodage

L'encodage est une norme qui décrit comment stocker et afficher les caractères dans un fichier.

### Normes d'encodage

- `ASCII` : codage de base (anglais) ;
- `ISO-8859` : extension pour d'autres langues européennes ;
- `Unicode` : pour représenter tous les caractères de toutes les langues du monde ;
- `UTF-8`, `UTF-16` : encodages flexibles compatibles `Unicode` et `ASCII`.

### Conversions d'encodages

#### La commande `iconv` 

La commande `iconv` permet de changer l'encodage d'un fichier : `iconv -f <FORMAT_ACTUERL> -t <FORMAT-DESTINATION> input.txt > output.txt`

`iconv --list` fournit une liste des encodages disponibles.

:::exo
1. Créer un fichier contenant la phrase suivante : `Une phrase accentuée en français.`
2. Changer l'encodage de ce fichier en `ASCII`.
3. Afficher le contenu du fichier. Que remarquez-vous ?
:::

#### Sauts de ligne Windows vs Unix

Les conventions de fin de ligne ne sont pas les mêmes sous Windows et sous Unix.

En principe :

- Une fin de ligne sous Dos/Windows s'écrit par un retour chariot (`CR`) suivi d'une terminaison de ligne (`LF`)
- Une fin de ligne sous Unix (Linux/MacOS > 10) s'écrit par une terminaison de ligne uniquement (`LF`)
- Une fin de ligne sous MacOS <= 9 s'écrit par un retour chariot uniquement (`CR`)

La plupart des programmes savent gérer les 2 types d'écriture mais il peut être utile de convertir par exemple les fichiers de script dans le format attendu sur la machine qui l'exécutera.

Pour s'assurer d'utiliser la convention Unix (donc: supprimer les retours chariot) on peut utiliser l'utilitaire _POSIX_ `tr` (donc disponible sur presque tout système Unix) ligne par ligne : `tr -d '\r'`.

Pour modifier directement des retours de ligne Windows en Unix dans `mon_fichier` :

```sh
echo "$(tr -d '\r' < mon_fichier)" > mon_fichier
```

#### En utilisant `vim`

`vim` supporte différents encodages et peut changer l'encodage courant d'un fichier.

:::exo
1. Vérifier que la version de `vim` supporte l'encodage : `vim --version | grep multi_byte`
2. Afficher l'encodage d'affichage courant : `:set encoding?`
  - Linux utilise presque toujours `UTF-8` pour le contenu d'un fichier.
  - Il existe des exception : `python`, …
3. Modifier l'encodage d'écriture courant en `UTF-16`. Attention il s'agit de `fileencoding` et non de `encoding` !
  - `:set fileencoding=utf-16`
4. Enregistrer le fichier : `:w`
5. Quitter `vim` : `:q`
6. Réouvrir le fichier. Deux possibilités :
  - Soit le fichier est lisible - l'encodage a été automatiquement mis à jour. Vérifier avec `:set encoding?`
  - Soit le fichier est illisible - il faut rééditer le fichier avec le bon encodage : `:e ++encoding=utf-16`
7. Même exercice pour le format de fichier en utilisant la commande `:set ff=dos` ou `:set ff=unix`
8. Pour plus d'information, depuis une fenêtre `vim` : `:h encoding`, `:h fileencoding`, `:h ff`
:::

## Langue

- Pour configurer la langue, on utilise des _LOCALE_ du système.
- Le changement de langue a un impact fort (format d'affichage des heures et des dates, devises, …) et est donc séparé en plusieurs options : les variables `LC_*`.
- Les _locale_ à générer sur le système sont décrites dans `/etc/locale.gen` (seules les lignes non commentées sont utilisées)
- La `locale` par défaut du système est écrite dans : `/etc/default/locale`.


:::tip
Sous Ubuntu, on peut utiliser un utilitaire lié à la (re)configuration du package `locales` :

```sh
dpkg-reconfigure locales
```
:::

:::exo
1. Afficher les informations de `locale` actuels.
  - Exécuter la commande `ls /toto` : une erreur en anglais devrait être retournée.
2. Ajouter la locale `fr_FR.UTF-8` aux locales à générer
3. Afficher les locales disponibles sur le système : `locale -a`
4. Générer la nouvelle locale : `locale-gen`.
5. Ajouter la ligne : `LANG=fr_FR.UTF-8 LANGUAGE=fr_FR` dans le fichier de locale par défaut
6. Exporter la locale courante pour votre shell `BASH` de votre utilisateur courant :
  - Dans le fichier `~/.bashrc` ajouter les lignes suivantes :
  - `export LANG=fr_FR.UTF-8`
  - `export LANGUAGE=fr_FR`
  - `export LC_ALL="fr_FR.UTF-8"`
7. Exécutez la commande `bash` pour relancer un shell et vérifier que la `locale` est correcte.
8. Sous Ubuntu, il faut installer le package supplémentaire `language-pack-fr` pour mettre à jour la langue pour les commandes système.
9. Vérifier que la commande `ls /toto` renvoit maintenant un message d'erreur en français
:::

