---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Cours BDD
tags:
- ddd
- bdd
- test
- agile
---

## But

- **Conversation** entre _Business_, _Développeurs_ et _Testeurs_ pour décrire les **comportements** du programme à **tester** et à **implémenter**.

---

## Spécification par scénarios (User-Story)

- ⭐ Base : exemples issus de cas d'usages précis ;
- 📜 En découlent les scénarios (exemples) : compréhension commune et précise de ce qui est à faire.
- But :
  - 🧑‍💼 Retranscrire le besoin métier dans le code (idem DDD) : **communication** 💬
  - 👍 La fonctionnalité couvre tous les cas d'usages métiers
  - ✅ Un test valide, implémente et documente le scénario

---

- Given Fred has bought a microwave
- And the microwave costs 100eu
- When we refund the microwave
- Then Fred should be refunded 100eu

---

- **Given (a specific context)**
- **When (some action is carried out)**
- **Then (a particular set of observable consequences _should_ occur)**

---

## Chercher les cas d'erreur ❌

---

Dans quel **contexte** l'événement aboutira à un résultat différent ?

- Given Fred has bought a microwave
- And the microwave costs 100eu
- And the microwave was on 10% discount
- When we refund the microwave
- Then Fred should be refunded 90eu

---

Est-ce vraiment le seul **résultat** à vérifier ?

- Given Fred has bought a microwave
- And the microwave costs 100eu
- When we refund the microwave
- Then the microwave should be added to the stock count.

---

## Du scénario au critère d'acceptation 👍

---

- Given Fred has bought a microwave
- And the microwave costs 100eu
- And the microwave was on 10% discount
- When we refund the microwave
- Then Fred should be refunded 90eu

---

- Given an item was sold with a discount
- When the customer gets a refund
- Then he should only be refunded the discounted price

---

> Items should be refunded at the price at which they were sold.

---

## Comment écrire de bons scénarios ✔️

- 📜 Avoir des noms de tests expressifs : le but de BDD est de documenter le produit depuis les scénarios
- 💡 1 phrase = 1 test
- 💬 Utiliser le langage (ubiquitaire) du métier : voir DDD
  - ⚠️ les experts métier doivent être disponibles !
- ⭐ Le BDD est piloté par la valeur métier (et donc, le développement !)

---

## Atelier 3 Amigos

- 🧑‍💼 _Business_ : **Définit** le problème ou la fonctionnalité attendue, défini la valeur business (Product Owner, Business Analyst, ...) ;
- 🧑‍💻 _Développeurs_ : Suggèrent un **moyen** de corriger ce problème ou de créer la fonctionnalité ;
- 🧑‍🔬 _Utilisateur / Testeur_ : Cherchent les **problèmes** et les failles dans le raisonnement.
- Autre rôles si nécessaire : _UX Designer_, _AdminSys_, …

---

### Communication

- BDD privilégie la **communication** plutôt que l'automatisation et la capture des conversations
  - Les scénarios sont avant tout des exemples d'utilisation plus qu'un engagement contractuel

---

![Le dialogue en BDD](https://www.arolla.fr/bdd-dialogue-png/) <!-- TODO: REDO DIAG -->

<div class="caption">Le dialogue en BDD ©www.arolla.fr</div>

---

![Résumé du BDD](https://blog.octo.com/le-bdd/behavior-driven-development-1-702x1024.webp) <!-- TODO: REDO DIAG -->

<div class="caption">Résumé du BDD. ©blog.octo.com</div>

---

## Outils

- `Gherkin` : syntaxe des scénarios
- Implémentation :
  - `Cucumber` (`JavaScript`, `Ruby`, …)
  - `Behat` (`PHP`)
  - `Behave` (`Python`)
  - `JBehave`, `Spock` (`Java`)

---

### Exemples

```gherkin
# from https://behat.org/en/latest/user_guide/gherkin.html

Feature: Some terse yet descriptive text of what is desired
  In order to realize a named business value
  As an explicit system actor
  I want to gain some beneficial outcome which furthers the goal

  Additional text...

  Scenario: Some determinable business situation
    Given some precondition
    And some other precondition
    When some action by the actor
    And some other action
    And yet another action
    Then some testable outcome is achieved
    And something else we can check happens too

  Scenario: A different situation
    ...
```

---

```java
# Cucumber framework

# @tag
# Feature: Sale Should Result in Decrease in Inventory
#   When we make a sale inventory should go down
#   Scenario: Make a Sale Check Inventory
#     Given sell 3 items of ABC 
#     When inventory on hand is 9
#     Then remaining inventory is 6

@Given("^sell 3 items of ABC$")
public void makeSale() {
  // Write code here that instantiates sale function in larger order entry system
  throw new PendingException();
}

@When(("^inventory on hand is 9$")
public void checkInventoryNow() {
  // put some code here
  throw new PendingException();
}

@Then("^remaining inventory is 6$")
public void checkInventoryAgain() {
  // put some code here
  throw new PendingException();
}
```

---

```groovy
# Spock framework

def "events are published to all subscribers"() {

  given: "an empty bank account"
    def theAccount = Mock(BankAccount)

  when: "the account is credited $10"
    theAccount.credit(10)

  then: "the account's balance is $10"
    theAccount.balance == 10
}

# Condition not satisfied:
# assert pc.clockRate >= 2333
# |  |         |
# |  1666      false
# ...
```

---

## TDD vs BDD

> TDD is building the thing right.
> BDD is building the right thing.

---

<!-- class: liens -->
# Liens

- <https://alexsoyes.com/bdd-behavior-driven-development/>
- <https://cucumber.io/docs/bdd/>
- [Livre open-source sur le BDD (FR)](https://github.com/Halleck45/livre-developpement-pilote-comportement)
- [WealCome – BDD, DDD, ATDD et TDD expliqués ! (Youtube)](https://www.youtube.com/watch?v=jxBmKvS7lAo)
- [Livre _Software craft: TDD, Clean Code et autres pratiques essentielles (Cyrille Martraire, Arnaud Thiéfaine, Dorra Bartaguiz, Fabien Hiegel, Houssam Fakih)](https://www.decitre.fr/livres/software-craft-9782100825202.html)
- [Behavior Driven Development (slides, Liz Keogh)][LizKeogh]
- [Cucumber – Discovery: The first practice of Behaviour-Driven Development (Youtube)](https://www.youtube.com/watch?v=JuWEQsE7Hlo)
- [Matt Brunt – Behaviour Driven Development and Behat: Telling Stories Through Code (Youtube)](https://www.youtube.com/watch?v=bCLlBgYQoIk)

[LizKeogh]: https://www.slideshare.net/lunivore/behavior-driven-development-11754474

