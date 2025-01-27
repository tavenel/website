---
title: Projet déploiement continu d'une application
date: 2023 / 2024
---

## Présentation du projet

L'objectif de ce projet est de développer une application dans un contexte d'intégration et de déploiement continu.

Le choix de l'application et des technologies utilisées est laissé libre - on recommande cependant de choisir une application dont les fonctionnalités peuvent être facilement intégrées itérativement, pour faciliter le pipeline CI/CD.

## Outils d'intégration continue

### Le gestionnaire de versions

Le gestionnaire de versions a 2 objectifs principaux dans une intégration continue :

- Pouvoir partager les modifications de code entre les développeurs du projet de manière sûre.
- Avoir une référence de code stable pour tester la qualité.
  
En intégration continue, il est important d’intégrer le plus régulièrement possible ses modifications (dans un commit) afin de limiter les changements à tester / valider.

- Utiliser le gestionnaire de versions `git` pour intégrer et partager les modifications du projet au sein du binôme. On pourra utiliser une version hébergée (`Github`, `Bitbucket`, `Gitlab`, ...)
- Configurer votre environnement de développement (IDE) pour associer le versionning Git au projet.

### Le build

L'étape de build permet la compilation du code source, sa transformation et son packaging sous forme d'un livrable déployable en production.

Il peut s'agir :

- Soit de simples fichiers compilés à déposer au bon endroit (fichiers Java `.class`, binaires C compilés, sources Python à interpréter). Ce choix est rare en CI/CD.
- Soit d'un format type archive (éventuellement avec un installeur) permettant l'installation du programme sur la cible : `jar` Java, `.exe` sur `Windows`, ...
- Soit d'une image déployable d'un système de production complet comportant le programme et toutes ses dépendances : image `Docker`, ... Ce choix est le plus courant en Devops.

Le livrable est généralement stocké dans un gestionnaire d'artéfacts (`Artifactory`, ...). On pourra ici se limiter à un stockage local.

### Les tests unitaires et de comportement

La métrique principale dans un pipeline d’intégration continue est souvent le rapport de test.

Celui-ci permet de valider les modifications d’un commit et d’éviter les régressions.

Intégrer un framework de tests unitaires au projet - par exemple en `Java`, on pourra utiliser le framework `Junit`.

Il est très compliqué de définir une couverture de test nécessaire et suffisante, car cela dépend énormément du code à tester : on privilégiera donc toujours la qualité du test sur les statistiques de sa couverture de code.

Les classes ayant des dépendances externes sont en général difficiles à tester. Au contraire, les classes contenant majoritairement du code métier sont les plus critiques et celles à tester le plus en profondeur dans les tests unitaires.

- On activera la couverture de test dans l'IDE afin de vérifier que les classes sont bien testées.
- On ajoutera les tests unitaires et/ou de comportement nécessaires.
- On modifiera le code source de l'application pour corriger les bugs trouvés au fur et à mesure du développement.
- On pourra également lancer l'application et réaliser des tests de fonctionnalité à la main.

### La qualité du code

La qualité du code ne se limite pas aux tests !

De nombreuses métriques peuvent être mises en place pour limiter les bugs et faciliter la maintenance du code.

- Utiliser les outils d’analyse de l’IDE pour détecter d’éventuels problèmes dans l'application et améliorer la qualité de celle-ci.
- On choisira quelles analyses paraissent pertinentes. Par exemple : < 15 lignes de code dupliquées

### Un pipeline intégré

Les outils précédents, bien que très efficaces, nous ont obligé à configurer notre IDE de manière adéquate.

Cela peut poser problème lorsque le projet devient conséquent, lors de l'arrivée d’un nouveau membre dans l'équipe, ou en cas de changement d’IDE : les critères de qualité risquent de diverger au sein de l'équipe.

Pour éviter cela, on peut essayer de partager au maximum ces critères de 2 manières :

- En intégrant les outils de vérification de la qualité dans les sources du projet
- En déployant un serveur d’intégration dédié

Ces 2 méthodes ne sont pas incompatibles.

- Intégrer les outils précédents dans un serveur d'intégration continue. On pourra également utiliser un outil de build pour faire le lien entre l'environnement de développement et l'environnement d'intégration continue : `Gradle`, ...

### Le déploiement continu

Le déploiement continu consiste à envoyer automatiquement en production le livrable généré depuis son lieu de stockage.

Il s'agit donc :

- de préparer la production à la livraison (si besoin)
- de déployer le livrable
- d'effectuer les actions post-livraison nécessaires (au besoin) sur la production

# Travail demandé 

Dans le respect du cahier des charges, il est attendu :

- La définition d’un pipeline d’intégration continue et de déploiement continu pour le développement d’une application respectant ce cahier des charges (tests unitaires et d’intégration, analyse de code source, création des binaires, publication des rapports, ...). On séparera clairement la partie _intégration continue_ et la partie _déploiement continu_ (génération d’artéfacts de production, livraison, déploiement, ...). On décrira également le modèle de déploiement continu mis en place.
- La mise en place d’un serveur Jenkins correctement administré et réalisant le pipeline CI/CD défini précédemment. Les différents jobs configurés dans Jenkins devront s’interfacer avec les outils d’intégration continue et de déploiement continu.
- Le développement de l’application en suivant ce processus d’intégration, dans un contexte de développement itératif. Le choix des technologies de développement est laissé libre.
- La mise en place d’outils de l’intégration continue sur la machine du développeur (tests unitaires, analyse statique, formatage du code, ...) pour les technologies choisies lors du développement.
- L’intégration des rapports des tests automatisés dans Jenkins.
- La mise en place du déploiement continu de l'application. Il n'est **PAS** demandé de mettre en place une gestion poussée de stockage des artéfacts ni la mise en place d'une réelle infrastructure de production : on pourra se limiter à déployer localement sur sa machine personnelle hébergeant le serveur Jenkins pour simuler la partie CD du pipeline.

Le projet étant réalisé en intégration continue, on sera particulièrement vigilant :

- à utiliser un outil de gestion des versions du code source (git) et à intégrer ses changements le plus souvent possible.
- à travailler sur des branches git dédiées avant d'intégrer ses changements dans la ou les branche(s) commune(s) (`master`, `main`) et à réaliser des revues de code avant d'intégrer les changements.
- à penser aux différents tests dès le début du projet, voir à écrire les tests avant l'implémentation du code (TDD, BDD).

# Rendus attendus 

On fournira donc :

- Un rapport sur la réalisation de l’étude de cas, notamment sur l'intégration continue mise en place. Voir la partie suivante : _rapport de votre étude_.
- Un ensemble de dépôts de code source référencés dans le rapport et contenant les différentes parties du projet. Ces dépôts de code devront contenir le code de production ainsi que le code de test.
- Les captures d'écran de revues de code effectuées pour l'intégration de changements dans le projet.
- Les captures d'écran de la configuration de Jenkins et des différents jobs et pipelines créés.
- La description de l'implémentation technique du pipeline de déploiement continu.

Le barème est le suivant :

- 2 points pour la qualité du rapport
- 3 points pour le schéma du pipeline CI/CD
- 3 points pour le développement itératif (git, branches, revues de code)
- 4 points pour le déploiement de Jenkins et la configuration des jobs
- 4 points pour la mise en place du framework de test, son intégration dans les différents outils (environnement de développement, Jenkins) et la qualité des tests fournis.
- 3 points pour le déploiement continu de l'application

_Un bonus de 2 points sera accordé pour chacune des parties pour la qualité de l'application développée._

# Rapport de votre étude

L'équipe projet (noms, prénoms) : 

1. Décrire succintement votre application et les technologies choisies pour son développement.
1. Quels outils d'intégration continue avez-vous conseillé à l'équipe de développement d'installer sur leur machine personnelle ? Justifiez votre réponse. 
1. Quels sont les différents dépôts de code source utilisés pour l'ensemble du projet ?
1. Quel est le workflow Git mis en place ? Pourquoi avoir fait ce choix de découpage ? 
1. Quel(s) pipeline(s) CI/CD continue avez-vous défini(s) pour gérer votre projet ? 
    - Insérez un schéma des grandes étapes du processus complet d’intégration continue que vous avez définies, depuis l'environnement du développeur à la validation finale des changements.
    - Décrire également le déploiement continu de l'application et les binaires de production générés.
1. Quels jobs et/ou pipelines avez-vous définis dans Jenkins ? Justifier ces choix. 
1. Pour chaque job de Jenkins, fournir une capture d'écran des rapports affichés sur la page principale du job. 
1. Quel modèle de déploiement continu avez-vous choisi ? Pourquoi ?
1. Comment le déploiement continu est-il réalisé dans votre projet ? Inclure les éventuels scripts permettant ce déploiement.
