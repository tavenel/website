---
title: TP2 - Une interface de monitoring pour les différents serveurs de chat
date: 2023 / 2024
---
 
# Présentation du projet

Afin de pouvoir avoir une vue centralisée sur l'état des différents serveurs de chat nous allons développer, en utilisant les principes de l'intégration continue, une interface utilisateur permettant de lister les utilisateurs enregistrés et les chatrooms créées.
 
Pour cela, le serveur de chat expose une API REST au travers de la classe `ChatServerService.java`

Cette API expose notamment 2 endpoints permettant de récupérer les utilisateurs et les chatrooms instanciées sur un serveur de chat :
 
Un endpoint `GET /users` permet de récupérer la liste des utilisateurs sur le serveur.

Exemple :

```
[   {     "account": {       "id": 0,       "username": "user1"     },
"currentStatus": "ACTIVE"   } ]
```
 
Un endpoint `GET /chatrooms` permet de récupérer la liste des chatrooms créées sur le serveur.
 
Exemple :

```
[   "chatroom1" ]
```
 
Nous allons utiliser ces 2 endpoints sur les différents serveurs comme backend de notre application de monitoring.

Le monitoring se fera sur plusieurs serveurs de chat en même temps (au moins 2). On pourra par exemple utiliser une instance du serveur corrigé par chacun des membres du binôme dans le TP 1.

Les spécifications de l'application de monitoring sont les suivantes :

- L'application doit agréger les données de différents serveurs de chat
- L'application doit proposer une vue de l'ensemble des utilisateurs enregistrés sur les serveurs de chat
- L'application doit proposer une vue de l'ensemble des chatrooms créées sur les serveurs de chat
 
## Exemple de réalisation

![Exemple d'interface](@assets/apps/simplechat-monitoring-exemple.png) 

<div class="caption">Un exemple de réalisation.</div>

# Travail demandé

Le TP sera effectué en binôme différent du premier TP.

Le développement sera réalisé sur l'IDE `vsCode`.

1. Créer un nouveau projet git sur un hébergeur de projets
2.  Cloner ce projet et le configurer sous `vsCode` pour utiliser le framework UI de votre choix (si nécessaire)
3. Configurer `vsCode` pour intégrer les outils d'intégration continue compatibles avec le développement choisi. On utilisera notamment :
	a. Un framework de tests unitaires
	b. Un framework de couverture de test (si non inclus dans le framework de tests)
	c. Un linter (vérificateur syntaxique et sémantique)
	d. Un outil de formatage du code source
4.  Développer l'interface de monitoring en suivant les principes de l'intégration continue :
	a. Le développement devra être itératif, par exemple :
		i. Mock du backend (liste des utilisateurs et/ou des chatrooms codées en dur dans le frontend)
		ii. Liste des utilisateurs puis liste des chatrooms
		iii. Requêtes sur un seul serveur puis multi-serveur
	b. L'intégration des fonctionnalités devra contenir des tests unitaires
	c. La qualité du code (coding-style, bugs, …) devra être testée et corrigée si besoin à chaque intégration grâce aux linter(s) configurés

On pourra par exemple utiliser les outils suivants dans le cas d'un projet `ReactJS` : `ESLint`, `Jest` (avec couverture), `Prettier`
 
Note 1 : Il n'est pas demandé de rendre l'accès aux différents serveurs backend configurable - la liste des serveurs à surveiller et leurs points d'accès pourront donc être stockés directement dans le code source de l'application de monitoring si besoin.
 
Note 2 : Il n'est pas demandé de réaliser le suivi des messages dans les chatrooms.
 
Note 3 : Afin de pouvoir facilement déployer une UI sur notre machine de travail dans un conteneur applicatif utilisant un port différent du backend (exemple : `Node.Js`), il peut être utile durant la phase de développement d'autoriser les requêtes depuis une origine différente (CORS). Cela évite de devoir passer par un reverse proxy (type `NginX`).
 
Dans le fichier `ChatServerService.java` du serveur, on pourra ajouter à la ligne 37 l'instruction suivante ajoutant des headers autorisant les appels de méthodes GET en cross-origin :

```java
after((Filter) (request, response) -> {
	response.header("Access-Control-Allow-Origin", "*");
    response.header("Access-Control-Allow-Methods", "GET");
	});
```

## Rendus attendus

Il est demandé par binôme, un rendu du code source du projet incluant le projet `vsCode` et ce document

On détaillera ci-dessous :

Le binôme :

Nom, Prénom 1 :

Nom, Prénom 2 :

La technologie frontend utilisée :

Les outils d'intégration continue utilisés et leur but :

Une explication sur le lancement des tests inclus dans le projet (commande à exécuter et/ou intégration dans l'IDE) :

---

[![CC  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/)

_Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations, visiter : [http://creativecommons.org/licenses/by-sa/4.0/](http://creativecommons.org/licenses/by-sa/4.0/)_

_Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries_

