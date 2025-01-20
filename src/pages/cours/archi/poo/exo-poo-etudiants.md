---
title: Exercice - gestion d'étudiants
author: Tom Avenel
date: 2023 / 2024
correction: false
---

Dans cet exercice, vous allez créer un programme qui permet de stocker et de gérer une liste d'étudiants.

1. Créez une classe `Etudiant` avec les attributs suivants :
  - nom
  - prénom
  - date de naissance (au format "jj/mm/aaaa")
  - liste de notes (sous forme de liste de nombres)
2. Ajoutez une méthode `moyenne` qui calcule la moyenne des notes de l'étudiant.
3. Créez une classe `GestionEtudiants` avec :
  - un attribut liste d'étudiants (sous forme de liste d'objets `Etudiant`)
  - les méthodes suivantes :
    + ajouter un étudiant à la liste ;
    + supprimer un étudiant de la liste ;
    + afficher la liste des étudiants (avec leur nom, prénom, date de naissance et moyenne).
3. Créez une fonction `menu` qui affiche un menu sur la console permettant à l'utilisateur de choisir entre les actions suivantes :
  - ajouter un étudiant ;
  - supprimer un étudiant ;
  - afficher la liste des étudiants ;
  - quitter le programme.
4. Dans une boucle principale, appelez la fonction `menu` pour afficher le menu et traiter l'action choisie par l'utilisateur.

