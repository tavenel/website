---
title: Exercices Méthodologie des tests
author: Tom Avenel
---
 
## Questions générales 

### Question 1 : 

> Valider qu'un retrait \<$20 n'est pas permis
> Valider que le retrait reçu est égal au montant demandé

_Ces deux exemples décrivent-ils des cas de tests ? Pourquoi ?_

### Question 2 : 

Voici le rapport d'exécution d'un test : 

> L'utilisateur a inséré sa carte bancaire dans le distributeur automatique de billets, entré le code de sa carte bancaire et demandé un retrait de 50 euros. Le distributeur a fourni un billet de 50 euros : le retrait automatique d'espèces par carte bancaire fonctionne donc correctement.

_Que pensez-vous de ce rapport ?_ 

### Question 3 : 

Le constructeur du distributeur automatique de billets vous demande de l'aider à créer un ensemble de tests permettant de valider le comportement de son produit de manière exhaustive. 

- _Que pensez-vous de cette demande ?_
- _Que conseillez-vous à ce constructeur ?_

### Question 4 : 

Un logiciel utilise un annuaire `LDAP` pour identifier ses utilisateurs. Cet annuaire est testé à chaque mise à jour du composant, environ 2 fois dans l'année. 

Après de nombreux problèmes en production liés à cet annuaire, afin d'améliorer la qualité du produit le chef de projet propose d'exécuter ces mêmes tests relatifs à l'annuaire `LDAP` chaque semaine. 

Cependant, après une année passée à utiliser cette nouvelle méthode, les mêmes tests exécutés chaque semaine ne détectent jamais d'anomalies et les problèmes en production sont toujours aussi fréquents. 

_A votre avis, quel est le principe de test qui n'a pas été respecté pour résoudre ces problèmes ?_

### Question 5 : 

Une équipe de développement propose à son client de réserver des ressources de test à la vérification poussée d'un composant ayant créé de nombreux problèmes durant l'intégration. 

Le client propose au contraire de réaliser des tests de manière équitable sur l'ensemble des composants afin d'avoir la même couverture de tests sur l'ensemble du projet. 

_Quelle solution vous paraît la plus adaptée ? Pourquoi ?_

### Question 6 : 

Dans l'équipe de développement d'un projet, l'un des développeurs propose d'écrire l'ensemble des tests du projet (tests unitaires, tests d'intégration, tests d'acceptation, …) avant de commencer l'implémentation du projet. 

Un second développeur lui répond qu'il vaut mieux finir l'implémentation du projet, et écrire tous les tests ensuite en s'adaptant à cette implémentation. 

_Que pensez-vous de ces deux approches ?_

### Question 7 :

_Afin de valider le bon fonctionnement d'un serveur de fichiers FTP, on effectue le scénario suivant :_

- Vérifier que l'URL du serveur est accessible
- Vérifier que l'utilisateur de test (nom : `testUser`, mot de passe : `test`) peut se connecter
- Vérifier que le serveur affiche bien la liste des fichiers de l'utilisateur de test
- Vérifier que le serveur affiche uniquement les fichiers de cet utilisateur

Ce scénario est-il un bon exemple de test ? Pourquoi ?

## Tests boîte blanche / boîte noire 
 
Décrire un ensemble de tests permettant de valider le bon assemblage d'un ordinateur personnel (c'est-à-dire l'intégration des différents composants :

- carte mère
- carte graphique
- mémoire vive
- disque dur
-  etc..

Pour chaque test, on précisera s'il s'agit d'un test boîte blanche ou boîte noire.

## Niveaux de tests 

Soit un programme en python qui transforme un fichier `XML` issu du logiciel `Netresto` contenant des données nécessaires à l'établissement de la paye en un ou plusieurs fichiers destinés à être importés dans le logiciel de comptabilité `SILAE`. Le programme dépose ensuite les fichiers dans un serveur `FTP` dédié et ces fichiers sont récupérés automatiquement par le logiciel `SILAE`. 

_Décrire un test unitaire, un test d'intégration entre 2 composants, un test système et un test d'acceptation._

## Tests fonctionnels

On souhaite garantir la qualité d'un environnement Cloud d'Infrastructure-as-a-Service (IaaS). Cet environnement fournit à l'utilisateur :

- Des services fournissant un OS Windows ou Linux dans une machine virtuelle
- Des services fournissant du stockage (avec réplication et sauvegarde) dans la machine virtuelle
- Des services fournissant une connexion de la machine virtuelle à un réseau privé et/ou public

Décrire un ensemble de tests fonctionnels permettant de valider le bon fonctionnement de ce Cloud d'un point de vue utilisateur

## Tests non fonctionnels

En utilisant l'environnement d'IaaS décrit précédemment :

Décrire un ensemble de tests non fonctionnels permettant de valider le bon fonctionnement de ce Cloud d'un point de vue utilisateur

## Plans de tests

### Tests d'acceptation

Décrire un plan de tests permettant de vérifier le bon fonctionnement d'une voiture à la sortie de la chaîne de production.

_On se focalisera uniquement sur le fonctionnement attendu d'un point de vue utilisateur, sans vérifier les spécifications techniques du produit._

### Tests d'intégration

Décrire un plan de tests permettant de vérifier l'intégration de différents composants lors de l'assemblage d'une voiture sur une chaîne de production.

_On supposera les différents composants déjà réalisés et testés unitairement : ce plan de tests devra vérifier l'intégration des composants sans tester la ou les fonctionnalités finales du produit._

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
