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

---

## Java

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

## JS

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

## C#

```csharp
[TestMethod]
public void Debit_WithValidAmount_UpdatesBalance()
{
    // Arrange
    double beginningBalance = 11.99;
    double debitAmount = 4.55;
    double expected = 7.44;
    BankAccount account = new BankAccount("Mr. Bryan Walton", beginningBalance);

    // Act
    account.Debit(debitAmount);

    // Assert
    double actual = account.Balance;
    Assert.AreEqual(expected, actual, 0.001, "Account not debited correctly");
}
```

---

## PHP

```php
# https://docs.phpunit.de/en/10.5/writing-tests-for-phpunit.html

<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

final class GreeterTest extends TestCase
{
    public function testGreetsWithName(): void
    {
        $greeter = new Greeter;
        $greeting = $greeter->greet('Alice');
        $this->assertSame('Hello, Alice!', $greeting);
    }

    public function testException(): void
    {
        $this->expectException(InvalidArgumentException::class);
    }
}
```

---

## Mock en PHP

```php
# https://docs.phpunit.de/en/10.5/test-doubles.html#mock-objects

// ------------
// INITIALISATION
// ------------

// Création du Mock
$mock = $this->createMock(MyClass::class);
// MyClass->someMethod() retournera 'mocked result'
$mock->method('someMethod')->willReturn('mocked result');


// ------------
// UTILISATION
// ------------

// Boîte noire
// appel de la méthode du Mock et vérification classique de résultat
$result = $mock->someMethod();
$this->assertEquals('mocked result', $result);

// Boîte blanche
// vérification des appels : la bonne méthode du Mock a été appelée
$mock->expects($this->once())->method('someMethod');
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

