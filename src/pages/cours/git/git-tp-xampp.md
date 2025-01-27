---
title: Xampp
date: 2023 / 2024
---

# TP - Git pour un Projet XAMPP

## Objectif du TP

Configurer un environnement de développement local avec XAMPP et utiliser Git pour versionner une application web stockée dans le dossier `htdocs`.

## Installation de XAMPP

1. **Télécharger XAMPP :**  
   Rendez-vous sur le site officiel de [XAMPP](https://www.apachefriends.org/index.html) et téléchargez la version adaptée à votre système d'exploitation.

2. **Installer XAMPP :**  
   Suivez les instructions d'installation. Assurez-vous que le module Apache et MySQL sont sélectionnés.

3. **Démarrer XAMPP :**  
   Ouvrez le panneau de contrôle XAMPP et démarrez les modules Apache et MySQL.

## Initialiser un dépôt Git dans `htdocs`

1. **Naviguer vers `htdocs` :**  
   Allez dans le dossier d'installation de XAMPP (par défaut `C:\xampp\htdocs` sur Windows ou `/opt/lampp/htdocs` sur Linux).

2. **Cloner un dépôt `Github` pour votre projet dans ce répertoire:**  
   Par exemple, on peut récupérer le projet <https://github.com/banago/simple-php-website> ou <https://github.com/aeimskei/basic-php-website> :

   ```bash
   git clone https://github.com/banago/simple-php-website mon_projet
   ```

## Accéder à l'application dans le navigateur

Ouvrez votre navigateur et accédez à <http://localhost/mon_projet> pour voir l'application en action.


# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries


