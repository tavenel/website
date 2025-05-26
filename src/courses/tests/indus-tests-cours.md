---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Industrialisation des tests
tags:
- tests
- patterns
---

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

# Structure d'un test automatisé

---

## Framework de tests

- On utilise généralement un _framework de tests unitaires_ (`*unit`) comme **ordonnanceur de tests** (exécution, méthodes de vérification, …)
  - y compris pour d'autres contextes : _end-to-end_, _performance_, … en ajoutant des librairies externes

---

## Classes de test

- Tests regroupés dans des _classes de test_ :
  + Regroupe les tests sur le même _SUT_ ou avec le même but.
  + Doit souvent hériter d'une classe de test fournie par le framework : `unittest.TestCase`, …
  + 1 test = 1 méthode dont le nom commence par `test` ou une annotation `@test`, …

---

## Code avant/après chaque test

- Les frameworks unitaires fournissent des méthodes :
  - `setUp()` et `tearDown()` exécutées avant / après **chaque** test
  - `beforeAll()` et `afterAll()` exécutées **1 fois** au début / à la fin de toute la classe de tests
  - Les noms peuvent varier suivant le framework

---

# Exemples

```java
// arrange
var repository = Substitute.For<IClientRepository>();
var client = new Client(repository);

// act
client.Save();

// assert
mock.Received.SomeMethod();
```

---

```js
// Mocha framework

it('should validate a form with all of the possible validation types', function () {

    const name = form.querySelector('input[name="first-name"]');
    const age = form.querySelector('input[name="age"]');

    name.value = 'Bob';
    age.value = '42';

    const result = validateForm(form);
    expect(result.isValid).to.be.true;
    expect(result.errors.length).to.equal(0);
});
```

---

# Test et IA

> L'IA peut ne pas comprendre pleinement le contexte métier ou les subtilités des exigences, ce qui peut conduire à des tests inadéquats ou incomplets. L'idéal est souvent une combinaison des deux approches, où l'IA aide à automatiser les tâches répétitives et les développeurs se concentrent sur les aspects plus complexes et nuancés des tests. (réponse de Mistral AI).

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

