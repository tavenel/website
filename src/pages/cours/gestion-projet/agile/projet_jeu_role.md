---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Projet Scrum Jeu de rôle
layout: '@layouts/CoursePartLayout.astro'
date: 2023 / 2024
---

# Présentation du projet 

Vous êtes une équipe ayant recu une commande pour un nouveau projet qui consiste à développer une application Web permettant à un joueur de jouer à un jeu de rôle contre l'ordinateur.

Le détail du cahier des charges est le suivant - en cas de question sur les spécifications, le formateur jouera le rôle du client final pour préciser celles-ci.

## Fonctionnalités

- Le joueur possède un `personnage` ayant des `caractéristiques` et des `objets` 
  + les différentes caractéristiques seront à choisir par les développeurs ;
  + les valeurs des caractéristiques du personnage doivent **évoluer** en fonction des événements de jeu.
  + la liste des objets est choisie par les développeurs ;
  + le personnage doit **acquérir et perdre des objets** en fonction des événements de jeu.
- Le joueur doit pouvoir **personnaliser** son personnage au démarrage de la partie. Cette personnalisation a un impact sur les caractéristiques du personnage.
- Le jeu se déroule en une suite d'`événements`.
  + certains événements ont un impact **positif** pour le joueur, d'autres ont un impact **négatif** ;
  + le jeu doit proposer des `actions` à réaliser à chaque événement, ces actions ont un impact sur le déroulement des événements et le choix des événements suivants ;
  + certains événements font interagir d'**autres personnages non jouables** (ex : combat contre des ennemis, ...)
- Le jeu doit contenir une part d'**aléatoire** (par exemple, la valeur exacte de certaines caractéristiques des ennemis ou l'enchaînement des événements).
- Le jeu possède des conditions de **victoire** et des conditions de **défaite** (événement et/ou conditions sur les objets acquis ou les caractéristiques du personnage).

# Travail à réaliser 
 
Le projet sera réalisé en plusieurs itérations, en utilisant la méthodologie Scrum. 

### Répartition des rôles Scrum 

Assigner à chaque membre de l'équipe, un ou plusieurs rôles nécessaires à la conduite d'un projet suivant la méthode Scrum. 

Le formateur jouera l'ensemble des rôles externes à l'équipe projet (et donc principalement celui de client). 

### Création du backlog 

Réaliser un backlog initial du projet. On pourra s'aider d'un story mapping, mais cela n'est pas une obligation. 

De même, l'utilisation d'Epics est possible mais n'est pas obligatoire. 

### Réaliser les sprints 

Les projets Scrum utilisent en général des sprints de 1 à 3 semaines. Pour s'entraîner à la gestion itérative d'un projet, ce projet sera réalisé en simulant 3 sprints de 30 minutes chacun. 

Chaque Sprint sera composé de 3 "journées" de 10 minutes. 

Ici, chaque sprint correspond à la livraison d'une nouvelle partie de l'histoire pour le prochain magazine à publier. On ajoutera chaque élément de l'histoire (nouveau personnage, nouvel événement, mise à jour d'un décor, …) sous forme de user-story dédiées. 


L'ensemble des cérémonies Scrum devra être respecté pendant l'itération, notamment : 

- La réunion de planification du Sprint 
- Les réunions de stand-up avant chaque nouvelle journée 
- La revue puis la rétrospective en fin de Sprint 

On prendra soin également de calculer la `vélocité` et le `burndown` après chaque Sprint. 
 
## Outil utilisé 

Le suivi du projet sera réalisé grâce à l'outil `Jira` d'Atlassian, disponible gratuitement en SaaS pour de petites équipes : <https://www.atlassian.com/fr/software/jira>  

Pour réaliser le suivi du projet : 

1. Créer un nouveau projet de type "Scrum" (ce choix est disponible à l'inscription) 
2. Commencer par remplir l'onglet Backlog 
	- Entrer les User Stories du backlog 
	- Penser à remplir les Story Points lorsque nécessaire, pour permettre la génération des rapports 
	- Entrer les sous-tâches des stories lorsque nécessaire, depuis la vue d'une User Story 
3. Dans l'onglet Backlog, il est possible de : 
	- Créer un (ou plusieurs) Sprint(s) 
	- Planifier un (ou plusieurs) Sprint(s) 
	- Démarrer le prochain Sprint 
4. Une fois démarré, le Sprint en cours est visible dans l'onglet "Sprints actifs" 
	- Déplacer les différentes Tâches (et/ou User Story directement) du tableau Kanban pendant l'exécution du Sprint, afin de refléter leur état à chaque instant. Penser à assigner les tâches ! 
	- Une fois le Sprint réalisé, cliquer sur "Terminer le Sprint". 
	- Analyser les différents rapports générés. Depuis l'onglet "Rapport de Sprint", cliquer sur "Exécuter la rétrospective" pour démarrer une rétrospective en utilisant Confluence (l'outil de Wiki d'Atlassian). _On pourra également utiliser l'outil EasyRetro (<https://easyretro.io/>)_


## Résultat attendu  

Il est attendu pour chaque groupe : 

* Un projet Scrum configuré dans Jira, avec l'ensemble des User Story et Tâches enregistrées et à jour 
	- Penser à donner les droits d'accès au formateur ! Une solution simple est d'inclure le formateur dans l'équipe projet.
	- Attention à ajouter les droits d'accès en cas d'utilisation d'autres outils ! 
* L'exécution de 3 sprints, avec pour chacun d'entre eux : 
	- Un livrable, c'est-à-dire un produit prêt à être livré au client 
	- Un calcul de la vélocité et du burndown 
	- Une revue de Sprint, qui sera effectuée avec le client (i.e. le formateur). Cette revue comportera une démonstration du travail réalisé pendant le Sprint. Attention, il n'est pas demandé de détailler l'ensemble du produit, mais bien de proposer au client une démonstration de ce qui l'intéresse. 
	- Une rétrospective du Sprint. 
	- La page Confluence générée par Jira pour la rétrospective devra être utilisée comme la page d'accueil du rapport, même s'il est possible d'utiliser un autre outil (par exemple : https://easyretro.io/ ) et d'ajouter un lien dans Confluence vers la rétrospective générée dans cet autre outil. 
	- On intègrera également le résultat de la revue (livrable et commentaires éventuels) sur cette page, directement ou via un lien vers ce livrable 

