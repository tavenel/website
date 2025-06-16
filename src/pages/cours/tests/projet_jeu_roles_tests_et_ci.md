---
title: Jeu de rôle
date: 2024 / 2025
---

# Projet CI/CD et Automatisation des tests : un jeu de rôle

## Présentation du projet 

Le projet consiste à développer une application Web permettant à un joueur de jouer à un jeu de rôle contre l'ordinateur.

Le détail du cahier des charges est le suivant - en cas de question sur les spécifications, le formateur jouera le rôle du client final pour préciser celles-ci.

_Après étude des besoins du client, vous décidez de développer cette application suivant un processus d'intégration continue, afin d'accélérer le développement du projet et pour garantir la qualité des fonctionnalités implémentées._

### Fonctionnalités

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

## Outils d'intégration continue

### Le gestionnaire de versions

Le gestionnaire de versions a 2 objectifs principaux dans une intégration continue :

- Pouvoir partager les modifications de code entre les développeurs du projet de manière sûre.
- Avoir une référence de code stable pour tester la qualité.
  
En intégration continue, il est important d'intégrer le plus régulièrement possible ses modifications (dans un commit) afin de limiter les changements à tester / valider.

- Utiliser le gestionnaire de versions `git` pour intégrer et partager les modifications du projet au sein du binôme. On pourra utiliser une version hébergée (`Github`, `Bitbucket`, `Gitlab`, ...)
- Configurer votre environnement de développement (IDE) pour associer le versionning Git au projet.

### Les tests unitaires et tests fonctionnels

_Voir la partie Automatisation des tests_

### La qualité du code

La qualité du code ne se limite pas aux tests !

De nombreuses métriques peuvent être mises en place pour limiter les bugs et faciliter la maintenance du code.

Par exemple, pour simplifier la compréhension du code on limitera la profondeur d'héritage dans les classes Java du projet à 2.

- Utiliser les outils d'analyse de l'IDE pour détecter d'éventuels problèmes dans l'application et améliorer la qualité de celle-ci.
- En plus de la profondeur d'héritage, on choisira quelles analyses paraissent pertinentes. Par exemple : < 15 lignes de code dupliquées

### Un pipeline intégré

Les outils précédents, bien que très efficaces, nous ont obligé à configurer notre IDE de manière adéquate.

Cela peut poser problème lorsque le projet devient conséquent, lors de l'arrivée d'un nouveau membre dans l'équipe, ou en cas de changement d'IDE : les critères de qualité risquent de diverger au sein de l'équipe.

Pour éviter cela, on peut essayer de partager au maximum ces critères de 2 manières :

- En intégrant les outils de vérification de la qualité dans les sources du projet
- En déployant un serveur d'intégration dédié

Ces 2 méthodes sont cumulables.

- Intégrer les outils précédents dans un serveur d'intégration continue. On pourra également utiliser un outil de build pour faire le lien entre l'environnement de développement et l'environnement d'intégration continue : `Gradle`, ...

## Automatisation des tests

### 📝 Rédaction d'un Plan de Test

- Réfléchir à un **plan de test** complet qui décrit les objectifs, la portée, l'approche, et les critères des tests. Rédiger succintement ce plan de tests.

### 🧪 Tests unitaires

Il est très compliqué de définir une couverture de test nécessaire et suffisante, car cela dépend énormément du code à tester : on privilégiera donc toujours la qualité du test sur les statistiques de sa couverture de code.

_On appelle code métier du code lié directement aux exigences fonctionnelles (et donc compréhensible par un expert du domaine - par exemple, la gestion des conditions de vol dans un programme d'aviation) et non un code ajouté simplement à cause de contraintes techniques (par exemple, comment interagir avec la base de données)._

Les parties de code _métier_ d'une application sont les plus critiques et celles à tester le plus en profondeur dans les tests unitaires. Au contraire, les classes ayant des dépendances externes sont en général difficiles à tester et sensibles aux changements d'implémentation : il est normal que leur couverture de tests unitaires soit moins importante.

- On activera la couverture de test dans l’IDE afin de vérifier que les classes sont bien testées.
- **Backend** : Écrire des tests unitaires pour le backend en utilisant des frameworks appropriés (par exemple, JUnit pour Java, pytest pour Python, phpunit en PHP, …).
- **Frontend** : Écrire des tests unitaires pour le frontend en utilisant des frameworks comme Jest ou Mocha.
- On pensera à utiliser des substituts (`Mock`, `Stub`) lorsque c'est nécessaire pour s'abstraire des dépendances.
- On modifiera le code source de l’application pour corriger les bugs trouvés au fur et à mesure du développement (Test-Driven Development).

### 📦 Tests d'Intégration

- Utiliser **Postman** pour créer, exécuter et **automatiser** des tests d'intégration sur les API du projet. On testera notamment les cas limites et cas d'erreur des API.

### 🧑‍💻 Tests end-to-end

- En utilisant le framework d'automatisation de navigateurs `Selenium`, ajouter des tests de fonctionnalité depuis l'interface Web pour simuler les interactions des utilisateurs avec l'application.
  + On utilisera un design pattern de `PageObject`, c'est-à-dire que les pages et les éléments de l'interface graphique seront décrits dans des classes de tests dédiées (voir cours).
- On pourra également lancer l’application et réaliser des tests de fonctionnalité à la main - ceux-ci seront à documenter dans le rapport.

### ⚡ Bonus: Tests de Performance

- Utiliser **JMeter** pour créer et exécuter des tests de performance afin de mesurer la capacité de l'application à gérer des charges élevées. Analyser les résultats des tests de performance et identifier les **goulots d'étranglement**.

### 🛡️ Bonus: Tests de Fiabilité et de Sécurité

- **Simian Army (Cloud)** : Utiliser les outils du Simian Army pour tester la résilience et la fiabilité de l'application dans le cloud.
- **Chaos Toolkit (Local)** : Utiliser le Chaos Toolkit pour simuler des défaillances en local et tester la robustesse de l'application.

## Travail demandé 

Dans le respect du cahier des charges, il est attendu :

- Le développement de l’application en suivant un processus de **test-driven development** :
  + L'application sera une **application Web** ;
  + L'application devra utiliser un système de persistance (base de données `SQL`, ...);
  + Le backend sera écrit en `Python` ou en `Java` ;
  + Le reste des choix de technologies (notamment le frontend) est laissé libre ;
- Partie CI/CD :
  + La définition d'un pipeline d'intégration continue et de déploiement continu (tests unitaires et d'intégration, analyse de code source, création des binaires, publication des rapports, … ). On séparera clairement la partie _intégration continue_ et la partie _déploiement continu_ (génération d'artéfacts de production, livraison, déploiement, … ). On décrira également le modèle de déploiement continu mis en place.
  + La mise en place d'un serveur Jenkins correctement administré et réalisant le pipeline CI/CD défini précédemment. Les différents jobs configurés dans Jenkins devront s'interfacer avec les outils d'intégration continue et de déploiement continu.
  + La mise en place d'outils de l'intégration continue sur la machine du développeur (tests unitaires, analyse statique, formatage du code, ...) pour les technologies choisies lors du développement.
  + L'analyse du code source de l'application dans un serveur `SonarQube`, et l'intégration des rapports dans `Jenkins`. 
  + L'intégration des rapports des tests automatisés dans `Jenkins`.
  + La mise en place du déploiement continu de l'application. Il n'est **PAS** demandé de mettre en place une gestion poussée de stockage des artéfacts ni la mise en place d'une réelle infrastructure de production : on pourra se limiter à déployer localement sur sa machine personnelle hébergeant le serveur Jenkins pour simuler la partie CD du pipeline.
- Partie Automatisation des tests :

Le projet étant réalisé en intégration continue, on sera particulièrement vigilant :

- à utiliser un outil de gestion des versions du code source (`git`) et à intégrer ses changements le plus souvent possible.
- à travailler sur des branches git dédiées avant d'intégrer ses changements dans la branche commune (`master`, `main`) et à réaliser des revues de code avant d'intégrer les changements.
- à penser aux différents tests dès le début du projet, voir à écrire les tests avant l'implémentation du code (TDD, BDD).
- un soin tout particulier sera apporté aux tests unitaires qui devront être nombreux.

- L'application sera testée fonctionnellement dans plusieurs environnements en utilisant le framework `Selenium`, par exemple : `Firefox` et `Google Chrome`.

### Rendus attendus 

On fournira donc :

- Un rapport sur la réalisation de l'étude de cas, notamment sur l'intégration continue mise en place. Voir la partie suivante : _rapport de votre étude_.
- Un ensemble de dépôts de code source référencés dans le rapport et contenant les différentes parties du projet. Ces dépôts de code devront contenir le code de production ainsi que le code de test.
- Les captures d'écran de revues de code effectuées pour l'intégration de changements dans le projet
- Les captures d'écran de la configuration de Jenkins et des différents jobs et pipelines créés
- Les captures d'écran des résultats d'analyse dans `SonarQube` 

Le barème est le suivant :

- Partie Intégration Continue
  + 3 points pour le rapport
  + 4 points pour le schéma du pipeline d'intégration (CI uniquement)
  + 3 points pour le développement itératif (git, branches, revues de code)
  + 5 points pour le déploiement de `Jenkins` et la configuration des jobs
  + 2 points pour l'intégration dans `SonarQube`
  + 3 points pour le déploiement continu de l'application
- Partie Automatisation des tests
  + 1 note sur la partie tests unitaires (/10) ;
  + 1 note sur la partie tests end-to-end (/10) ;

Le barème est le suivant :

- Chaque partie a le même barème :
  + 3 points pour la partie tests unitaires (ou tests end-to-end) du rapport ;
  + 6 points pour la couverture de tests (nombre de tests, choix des scénarios, ...)
    * il est attendu une bonne couverture par lignes de code pour les tests unitaires sur les classes métier du backend et du frontend (environ 80%) ;
	* il est attendu au moins 5 tests `Selenium`.
  + 6 points pour la qualité des tests (design patterns utilisés, lisibilité du code de test, ...)
  + 5 points pour le développement de l'application (aboutissement du projet, qualité du code, ...)
- Le rapport sur la réalisation de l'étude de cas devra contenir :

_Un bonus de 3 points sera accordé pour chacune des parties pour la qualité de l'application développée_

### Rapport de votre étude : 

L'équipe projet (noms, prénoms) : 

#### Partie Intégration Continue :

1. Décrire succintement votre application et les technologies choisies pour son développement.
1. Une documentation courte expliquant comment installer un environnement de développement sur l'installation (installation des dépendances, lancement de l'application, exécution des tests, ...) ;
1. Quels outils d'intégration continue avez-vous conseillé à l'équipe de développement d'installer sur leur machine personnelle ? Justifiez votre réponse. 
1. Quels sont les différents dépôts de code source utilisés pour l'ensemble du projet ?
1. Quel est le workflow Git mis en place ? Pourquoi avoir fait ce choix de découpage ? 
1. Quel(s) pipeline(s) CI/CD continue avez-vous défini(s) pour gérer votre projet ? 
    - Insérez un schéma des grandes étapes du processus complet d'intégration continue que vous avez définies, depuis l'environnement du développeur à la validation finale des changements.
    - Décrire également le déploiement continu de l'application et les binaires de production générés.
1. Quels jobs et/ou pipelines avez-vous définis dans Jenkins ? Justifier ces choix. 
1. Pour chaque job de Jenkins, fournir une capture d'écran des rapports affichés sur la page principale du job. 
1. Comment avez-vous interfacé l'analyse du code source avec `SonarQube` ? On fournira des captures d'écran des rapports de `SonarQube` pour chaque job intégré. 
1. Quel modèle de déploiement continu avez-vous choisi ? Pourquoi ?
1. Comment le déploiement continu est-il réalisé dans votre projet ? Inclure les éventuels scripts permettant ce déploiement.

#### Partie tests :

1. Lien vers le 1er dépôt contenant le code source de l'application et les tests unitaires ;
1. Lien vers le 2e dépôt de code contenant les tests `Selenium` ;
1. Quel(s) framework(s) de tests avez-vous choisi d'utiliser ? Pourquoi ?
1. Les choix de réalisations de tests, par exemple : donner un exemple expliquant pourquoi vous avez choisi de tester plus fortement certaines parties du code que d'autres ;
1. Processus de tests : donner un exemple expliquant en quoi l'écriture et l'exécution des tests en parallèle de la réalisation de l'application a impacté l'écriture de votre code de production.
1. Avez-vous réalisé des tests manuels ? Si oui, lesquels ?


# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- SELENIUM is a trademark of Software Freedom Conservancy, Inc.
- "Python" is a registered trademark of the PSF.
- Java is a registered trademark of Oracle and/or its affiliates.
- Firefox® is a registered trademark of the Mozilla Foundation.
- Chrome™ is a trademark of Google LLC.
- Apache, Apache Maven, and Maven are trademarks of the Apache Software Foundation
- Bitbucket is a registered trademark of Atlassian Pty Ltd.
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.
- GitLab is a registered trademark of GitLab Inc.
- GRADLE is a trademark of GRADLE, INC
- Jenkins® is a registered trademark of LF Charities Inc.
- SONARQUBE is a trademark of SonarSource SA.
- The name SpotBugs and the SpotBugs logo are trademarked by the University of Maryland.

