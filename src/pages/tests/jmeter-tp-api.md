---
title: Jmeter - Tests de performance
date: 2023 / 2024
---

# Introduction

Dans ce TP, nous allons utiliser JMeter pour réaliser des tests de performance. JMeter est une application Java permettant de réaliser des tests de charge et est couramment utilisé sur les API d'un projet (au niveau protocole), notamment pour tester les performances du backend des applications Web. JMeter est également capable de réaliser des tests de performance directement sur des méthodes Java, du JMS, des connexions TCP, ...

JMeter propose deux modes de fonctionnement : avec ou sans interface graphique.

L'interface graphique est utile dans un premier temps, pour écrire les scénarios et plans de tests.

Une fois les tests enregistrés, leur exécution est réalisée en ligne de commande (afin de perturber au minimum le système à tester – l'interface graphique pourrait en effet avoir de fortes conséquences sur les résultats de performances).

Pour plus d'informations : <https://jmeter.apache.org/usermanual/get-started.html>.
 
# Découverte de Jmeter et intégration dans Jenkins

1. Télécharger le binaire JMeter : <https://jmeter.apache.org/download_jmeter.cgi>.
2. Installer le plugin `Performance` dans Jenkins.
3. Suivre le tutoriel : <https://www.jenkins.io/doc/book/using/using-jmeter-with-jenkins/> pour créer et intégrer un premier test JMeter dans Jenkins.

# Tests de performance de services Web
 
En utilisant un programme déjà développé par vos soins, réaliser un plan de tests de charge de votre application. Ces tests seront effectués en simulant le comportement d'un client HTTP depuis Jmeter. **Attention, Jmeter ne simule pas un environnement d'exécution EcmaScript ! On pourra donc si besoin limiter certains tests au backend de l'application**.

_Si vous ne disposez pas d'un projet Web à tester, le projet suivant peut être utilisé à la place : <https://github.com/mybatis/jpetstore-6> .

L'écriture d'un plan de tests pour un service Web se fait au minimum de la manière suivante :

- Ajouter un thread d'exécution pour simuler les différents utilisateurs.
- A l'intérieur de cette nouvelle unité d'utilisateurs, on ajoute des échantillons de test (`sampler`) pour exécuter nos scénarios de tests (ici, des requêtes HTTP).
- Ajout de récepteurs (`listeners`) pour récupérer les résultats d'exécution.

On prendra soin d'ajouter d'éventuels `pré-processeurs` si l'usage de l'application le nécessite (authentification et génération de token JWT à injecter ensuite dans les requêtes, etc.)

On pourra également ajouter des assertions pour vérifier la validité des réponses aux requêtes effectuées.
 
On intègrera l'exécution de ce plan de test et les rapports de test dans Jenkins. On prendra soin d'effectuer plusieurs exécutions du (ou des) jobs Jenkins associés au(x) plan(s) de tests afin d'avoir une comparaison par rapport aux builds précédents.

Il y aura donc au moins 2 plans de tests :

- un plan pour les performances de l'API fournie par le backend
- un plan pour les performances Web globales (affichage des pages). Ce plan sera très limité, puisque de nombreuses interactions nécessiteront sûrement un véritable navigateur Web servant du code EcmaScript en interaction avec un DOM (Domain Object Model).

Dans un "vrai" projet, ces tests devraient tourner au maximum dans un environnement proche de la production. Pour des raisons de facilité,on se contentera ici de l'environnement d'exécution du serveur Jenkins.

# Rendu attendu

Il est attendu une archive des tests de performance effectués sur votre application, contenant :

- Le(s) plan(s) de tests de Jmeter (format `.jmx`)
- Les captures d'écran des résultats des tests de performance publiés dans Jenkins (page de rapport des performances)

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Oracle and Java are registered trademarks of Oracle and/or its affiliates.
- Jenkins® is a registered trademark of LF Charities Inc.

