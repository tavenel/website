---
title: 🚀 Intégration continue - pour aller plus loin
date: 2023 / 2024
---

## Contexte

Le TP noté nous a permis de mettre en place un pipeline simpliste d'intégration continue. Afin d'améliorer la qualité de notre application, ce pipeline peut être amélioré en utilisant les méthodes décrites dans les sections suivantes. Ces sections sont indépendantes, on pourra les réaliser dans l'ordre qui semble le plus utile à l'amélioration du produit. 

## Reporting du pipeline d'intégration continue 

L'un des intérêts d'un pipeline d'intégration continue est de réduire la "feedback loop", c'est-à-dire d'obtenir des retours d'informations le plus rapidement possible. 

On pourra donc chercher à améliorer cette boucle de retour dans notre pipeline, par exemple : 

- Afficher le statut du commit (suite à l'exécution du pipeline) dans l'outil hébergeant le code source du projet. On pourra également ajouter un lien vers le job Jenkins ayant testé le commit. 
- Envoyer des notifications (notamment en cas d'échec), dans `Slack` ou dans un autre outil de notifications.
 

## Tests d'interface graphique 

S'ils n'ont pas encore été intégrés dans le projet, on pourra ajouter dans le pipeline un framework de tests d'interface utilisateur (par exemple : Sélénium). Développer ensuite les tests associés à l'application et les intégrer dans le pipeline d'intégration continue.


## Tests non fonctionnels (tests de charge, ...) 

Maintenant que nous avons testé nos fonctionnalités, il est également intéressant d'ajouter des tests non-fonctionnels. Ces tests vont qualifier notre application, pour savoir "à quel point" celle-ci est plaisante pour l'utilisateur. 

On pourra notamment réaliser des tests de charge et de performance (à l'aide d'un outil tel `JMeter` ou `Gatling` par exemple). 


## Déploiement continu 

Maintenant que notre pipeline d'intégration continue est assez évolué pour nous donner une bonne confiance dans nos intégrations, pourquoi ne pas tenter de réaliser un déploiement automatique en production lorsque la qualité du commit est suffisante ? 

Pour cela : 

- On commencera par générer des livrables prêts à être déployés en production. On pourra par exemple utiliser des images Docker, et on utilisera les bonnes pratiques de production des framework et des librairies utilisés.
- Ces changements peuvent nécessiter de générer un nouveau build du commit. Ce nouveau build a-t-il un impact sur le pipeline existant ? Quelle compilation utiliser pour les différents tests ? 
- Une fois les livrables générés, ceux-ci doivent être stockés dans un gestionnaire de livrables sécurisé afin de garantir l'authenticité et l'intégrité des images à déployer. Déployer une instance `Nexus` afin de gérer un `repository` propre à notre application. 
- La dernière étape consiste à définir et installer un environnement de production. Le pipeline sera mis à jour pour que Jenkins réalise le déploiement automatique en production depuis la récupération du commit (sauf, bien sûr, en cas d'erreur dans le pipeline). 

## Monitoring applicatif 

La plupart des tests que nous avons développé sont des tests "boîte noire" : ces tests vérifient les fonctionnalités mais ne s'intéressent pas au fonctionnement à l'intérieur de l'application. Inspecter une application de l'intérieur permet de détecter d'autres erreurs difficiles à observer de l'extérieur : fuites mémoire, problèmes de dépendances, inter-locking de threads, … 

Afin d'améliorer la qualité de notre application, intégrer un outil de surveillance applicatif (on pourra par exemple utiliser `Prometheus` pour surveiller la machine virtuelle Java). 

De nombreux framework permettent une intégration avec des outils de monitoring (par exemple : `Spring` possède une intégration `Prometheus` poussée). 

## Raffinage du pipeline d'intégration continue 

Les différentes étapes ajoutées au pipeline d'intégration continue peuvent aboutir à des jobs longs à exécuter et coûteux en ressources matérielles. Si cela permet d'augmenter notre confiance sur chaque commit, la "feedback loop" peut en être impactée si les commit sont trop longs à tester. 

On pourra se demander comment raffiner le pipeline d'intégration continue afin d'optimiser au mieux la gestion des ressources dans les étapes coûteuses. On pourra notamment : 
* Ne pas exécuter toutes les étapes à chaque commit (quel modèle adopter alors ?) 
* Mutualiser une ou des plateformes pour exécuter certaines étapes sans tout réinstaller (à quel moment ? Quel est le risque ?) 
* Mettre en place le nouveau pipeline d'intégration continue. 

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Spring® is a trademark of Pivotal Software, Inc. in the U.S. and other countries.
- Prometheus® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Oracle and Java are registered trademarks of Oracle and/or its affiliates.
- Jenkins® is a registered trademark of LF Charities Inc.
- SELENIUM is a trademark of Software Freedom Conservancy, Inc.
- Docker, Docker Swarm and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- NEXUS is a trademark of GOOGLE LLC.
- SLACK is a trademark of Slack Technologies, Inc.
