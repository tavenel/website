---
marp: true
paginate: true
#footer: _© 2024 Tom Avenel under 󰵫  BY-SA 4.0_
title: Industrialisation des tests
keywords:
- tests
- patterns
---

# Industrialisation des tests

_Tom Avenel_

<https://www.avenel.pro/>

---

<!-- _class: titre lead -->

# Automatisation des Tests

---

# POURQUOI AUTOMATISER DES TESTS ?

- Test automatisé : test dont l'exécution ne nécessite pas l'intervention d'un humain.
- Tests fonctionnels manuels nécessaires...
- ...Mais beaucoup de tests basiques exécutés régulièrement : exécution manuelle fastidieuse, retour sur investissement faible.
- Dans certains contextes (projets web, ...) : différentes plateformes, différents navigateurs, différentes versions.

---

- Pour toutes ces raisons, il est souvent intéressant d'automatiser certains tests fonctionnels.
- Les tests non-fonctionnels demandent souvent de grandes ressources pour être exécutés manuellement (par exemple : simuler 1000 utilisateurs concurrents). Pour cette raison, ils sont presque toujours automatisés.

---

# AVANTAGES DE L'AUTOMATISATION

Automatiser un test a plusieurs avantages :

- Libère des ressources humaines (le testeur)
- La reproductibilité du test est simplifiée : le test automatisé vérifie toujours la même chose

---

# INCONVÉNIENTS DE L'AUTOMATISATION

- Coût du développement d'automatisation (principal frein) :  mettre en place l'environnement, les vérifications, ...
- Responsabilité du testeur : il est parfois préférable de tester des interfaces à destination d'autres humains par un humain.

---

# CHOISIR LES TESTS À AUTOMATISER

- Quels sont les tests les plus exécutés ?
- Quel est le coût de leur automatisation ? 

---

- Les tests unitaires sont les tests les plus exécutés et les plus faciles à automatiser.
  + Presque toujours automatisés : frameworks `*Unit` et dérivés.

---

- Les tests d'API sont relativement aisés à automatiser et fastidieux à tester manuellement
  + Souvent automatisés : `Swagger`, frameworks `*Unit`

---

- Les tests d'interface graphique sont compliqués et fragiles
  + Souvent les derniers à être automatisés : `Selenium`

---

Quels sont les tests critiques ?

- Dans le pratique, souvent au moins un test manuel d'interface utilisateur.
  + Permet de valider d'un point de vue utilisateur des éléments difficiles à automatiser : aspect `CSS`, ...
- Les parties les plus critiques du produit sont souvent testées manuellement, parfois en supplément de tests automatisés.

---

<!-- _class: titre lead -->

# Jenkins : serveur d'intégration continue

![The Jenkins logo](https://www.jenkins.io/images/logos/jenkins/jenkins.svg)

Le logo Jenkins®.

---


# Serveur d'intégration continue

Outil permettant d'orchestrer le lancement de l'intégration continue, l'exécution des différent outils et la génération de rapports sur la qualité du code après leur exécution.

Le code source est monitoré (ou une notification reçue) pour chaque nouveau changement à analyser, afin de lancer la boucle d'intégration continue.

---

# Types de serveurs CI

- Combinant hébergement des sources et intégration continue du projet : `Github®`, `Gitlab®`, `Bitbucket®`, ...
  + Ces serveurs proposent des solutions cloud gérant tout le cycle de vie du projet.
- Dédiés à l'intégration continue uniquement : `Jenkins®`, `TeamCity®`
  + S'interfacent avec un hébergement distant.
  + Peuvent être hébergés en ligne ou déployés sur un serveur dédié.

---

# Architecture d'un serveur d'intégration continue

```ditaa

 +-------------+  +---------------+  
 | cBLU        |  | cPNK          |
 | Gestion des |  | Orchestration |
 |   sources   |  |  des builds   |
 +-------------+  +---------------+
           /---------\
           |{s} cBLK |
           | Serveur |
       	   |   CI    |
           \---------/
 +-------------+  +--------------------+
 | cGRE        |  | cYEL               |
 | Exécution   |  | Génération des     |
 |  des tests  |  | rapports et notifs |
 +-------------+  +--------------------+

```

<!-- _class: legende -->

Les 4 composants d'un serveur d'intégration continue.

---


<!-- _class: subtitle lead -->

# Présentation du produit

---

# Présentation de Jenkins®

- Serveur d'intégration continue en Java.
- Système simple mais entièrement configurable.
- Intégration continue et DevOps par plugins : `Git`, `Maven 2 project`, `Amazon EC2`, `HTML Publisher`, ...

---

- Outil d'intégration continue le plus utilisé : vaste communauté, 1500 plugins...
- ...Mais système vieillissant et difficile à maintenir (en cours de réécriture)
- Fork open-source de `Hudson` (nombreuses traces dans documentation et configurations).

---
<!-- _class: subtitle lead -->

# Installation et déploiement

---

# Installation de Jenkins

- Installation comme application indépendante
  + facile et rapide sur toute machine
  + serveur d'applications dédié ou container servlet Java Jetty (voir doc)
- Installation comme servlet dans un serveur d'applications Java : `Apache Tomcat`, `GlassFish®`, ...
  + serveur applicatif à administrer
  + stabilité accrue des tests et du déploiement
- Déploiement dans des conteneurs `Docker`

---

_Pour nos besoins, nous nous limiterons à l'utilisation de Jenkins dans son propre serveur d'applications, en lançant directement le JAR récupéré sur la page du projet._

---

<!-- _class: subtitle lead -->

# Les jobs Jenkins

---

# Les jobs

- Jenkins fonctionne essentiellement sous la forme de jobs (enchaînement d'étapes), de types variés.
- 1 projet de build = un job.
- Peut enregistrer et afficher des processus exécutés à l'extérieur de Jenkins.

---

_Un job multi-configuration peut être d’une grande utilité dans des projets plus sophistiqués, notamment lorsque des builds spécifiques à chaque plateforme sont nécessaires._

---

<!-- _class: subtitle lead -->

# Tests unitaires et d'intégration

---

# Automatisation des tests unitaires et d'intégration

Jenkins est un orchestrateur : il permet donc d'automatiser les tests unitaires et/ou d'intégration, de plusieurs manières :

- En utilisant des plugins dédiés.
- En s'intégrant avec des outils de build : `Maven`, `Gradle`, ...
- En fournissant des scripts à exécuter

---

_Jenkins permet de s'interfacer avec de nombreux outils d'exécution ou de reporting de tests. Nous verrons comment intégrer Jenkins avec les principaux outils de tests._

---

<!-- class: liens -->

# Références

Des références pour automatiser les tests dans différents langages :

- [Junit pour Java][zds-junit]
- [Phpsec pour PHP][zds-phpsec]

[zds-junit]: https://zestedesavoir.com/tutoriels/274/les-tests-unitaires-en-java/
[zds-phpsec]: https://zestedesavoir.com/tutoriels/411/les-tests-automatises-avec-phpspec/

---

- [Outils de test open-source](https://www.guru99.com/best-open-source-testing-tools.html)
- [Outil d'automatisation de tests d'acceptance FitNesse et intégratoin avec Junit](http://fitnesse.org/FitNesse.UserGuide.WritingAcceptanceTests.RunningFromJunit)
- [Tutoriel sur les tests en Java](https://openclassrooms.com/fr/courses/6100311-testez-votre-code-java-pour-realiser-des-applications-de-qualite)
- [Vidéo tests sur Android](https://openclassrooms.com/fr/courses/6100311-testez-votre-code-java-pour-realiser-des-applications-de-qualite)

---

<!-- class: legal -->

# Legal

- SELENIUM is a trademark of Software Freedom Conservancy, Inc.
- SWAGGER is a trademark and brand of Smartbear Software Inc, Somerville , MA . 
- Oracle and Java are registered trademarks of Oracle and/or its affiliates
- Jenkins® and the Jenkins logo are registered trademarks of LF Charities Inc.
- TeamCity is a trademark or registered trademark of JetBrains, s.r.o.
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- Apache, Apache Subversion, and the Apache feather logo are trademarks of The Apache Software Foundation.
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.
- Bitbucket is a registered trademark of Atlassian Pty Ltd.
- GitLab is a registered trademark of GitLab Inc.

---

- GRADLE is a trademark of GRADLE, INC
- Apache, Apache Maven, and Maven are trademarks of the Apache Software Foundation
- The project name “webpack” is a trademark of the JS Foundation.
- GlassFish® is a trademark of Eclipse Foundation, Inc.
- Apache, Apache Tomcat, and Tomcat are trademarks of the Apache Software Foundation
- SONARQUBE is a trademark of SonarSource SA.
- Linux is a registered trademark of Linus Torvalds.
- Mac and Mac OS are trademarks of Apple Inc., registered in the U.S. and other countries.
- Windows is a registered trademark of Microsoft Corporation in the United States and other countries.
- The name SpotBugs and the SpotBugs logo are trademarked by the University of Maryland.

---

- "Python" is a registered trademark of the PSF. The Python logos (in several variants) are use trademarks of the PSF as well.
- Kotlin is a trademark or registered trademark of JetBrains, s.r.o.
- Docker, Docker Swarm and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
