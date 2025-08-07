---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Projet Scrum InfraCampus
date: 2023 / 2024
---

# Présentation du projet 

L'université lance une nouvelle plateforme de gestion des inscriptions et des services aux étudiants, baptisée **InfraCampus**. Ce service IT critique doit être déployé sur une infrastructure robuste, sécurisée et capable de gérer des pics d'activité, tout en garantissant une haute disponibilité.

Les objectifs de ce projet sont les suivants :

- Mettre en place une infrastructure IT fiable et évolutive répondant aux exigences de sécurité et de performance.
- Anticiper et gérer les incidents (pannes, cyberattaques, défaillances matérielles) grâce à une approche agile.
- Assurer une coordination efficace entre les équipes techniques pour le déploiement et la maintenance du service.

Tâches et scénarios à simuler :

- **Configuration des serveurs** : Déploiement de serveurs web et de bases de données en environnement virtualisé pour garantir la flexibilité et la redondance.
- **Mise en place d'un monitoring avancé** : Installation et configuration d'outils de surveillance pour détecter les anomalies et prévenir les interruptions de service.
- **Planification des sauvegardes et de la sécurité** : Élaboration de stratégies de backup et de restauration, ainsi que le déploiement de correctifs et mesures de sécurité pour protéger l'infrastructure.
- **Simulation d'incidents** : Organisation de scénarios d'urgence (pannes, attaques DDoS, défaillance d'un serveur critique) pour entraîner l'équipe à réagir rapidement et efficacement en mode agile.
- **Collaboration inter-équipes** : Coordination avec les développeurs pour garantir une intégration continue entre le déploiement de nouvelles fonctionnalités et la stabilité de l'infrastructure.

En cas de question sur les spécifications, le formateur jouera le rôle du client final pour préciser celles-ci.

# Travail à réaliser 
 
Vous utiliserez la méthode agile Scrum pour organiser le développement du projet en plusieurs sprints, avec des rituels dédiés (Sprint Planning, Daily Scrum, Review et Rétrospective).

### Répartition des rôles Scrum 

Assigner à chaque membre de l'équipe, un ou plusieurs rôles nécessaires à la conduite d'un projet suivant la méthode Scrum. 

Le formateur jouera l'ensemble des rôles externes à l'équipe projet (et donc principalement celui de client). 

### Création du backlog 

Réaliser un backlog initial du projet. On pourra s'aider d'un story mapping, mais cela n'est pas une obligation. 

De même, l'utilisation d'Epics est possible mais n'est pas obligatoire. 

### Réaliser les sprints 

Les projets Scrum utilisent en général des sprints de 1 à 3 semaines. Pour s'entraîner à la gestion itérative d'un projet, ce projet sera réalisé en simulant 3 sprints de 30 minutes chacun. 

Chaque Sprint sera composé de 3 "journées" de 10 minutes. 

L'ensemble des cérémonies Scrum devra être respecté pendant l'itération, notamment : 

- La réunion de planification du Sprint 
- Les réunions de stand-up avant chaque nouvelle journée 
- La revue puis la rétrospective en fin de Sprint 

On prendra soin également de calculer la `vélocité` et le `burndown` après chaque Sprint. 
 
On ajustera également le Sprint en fonction des imprévus signalés durant des mini Daily Scrums.

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

