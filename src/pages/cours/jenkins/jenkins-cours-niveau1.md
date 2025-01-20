---
marp: true
paginate: true
#footer: _© 2024 Tom Avenel under 󰵫  BY-SA 4.0_
title: Jenkins
keywords:
- tests
- ci
- jenkins
---

# Jenkins : serveur d'intégration continue

_Tom Avenel_

<https://www.avenel.pro/>

---

<!-- _class: titre lead -->

# Jenkins : serveur d'intégration continue

![The Jenkins logo][jenkins-logo]

Le [logo Jenkins®][jenkins-website].

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

```{render="{{ditaa.svg}}" alt="Architecture d'un serveur d'intégration continue : gestion des sources, orchestration des builds, exécution des tests, génération des rapports"}
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
- Fork open-source de Hudson (nombreuses traces dans documentation et configurations).

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

La documentation de Jenkins est très complète, on pourra notamment citer :

- La [site officiel][jenkins-website]
- La page d'accueil de la [documentation][doc-jenkins-main]
- Comment gérer la [sécurité de Jenkins ?][doc-jenkins-secu]
- Comment installer et gérer les [plugins Jenkins ?][doc-jenkins-plugins]
- Comment utiliser les [pipelines Jenkins ?][doc-jenkins-pipelines]
- Comment mettre en oeuvre les [builds dans Jenkins ?][doc-jenkins-builds]
- [Guide complet de Jenkins][jenkins-guide-complet]

[jenkins-logo]: https://www.jenkins.io/images/logos/jenkins/256.png
[jenkins-website]: https://www.jenkins.io/
[doc-jenkins-main]: https://www.jenkins.io/doc/
[doc-jenkins-secu]: https://www.jenkins.io/doc/book/managing/security/
[doc-jenkins-plugins]: https://www.jenkins.io/doc/book/managing/plugins/
[doc-jenkins-pipelines]: https://www.jenkins.io/doc/tutorials/#pipeline
[doc-jenkins-builds]: https://www.jenkins.io/doc/tutorials/#tools
[jenkins-guide-complet]: https://jenkins-le-guide-complet.github.io/html/book.html

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
