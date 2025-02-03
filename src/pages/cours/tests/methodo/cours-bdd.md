---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: BDD
keywords:
- ddd
- bdd
- test
- agile
---

<!-- _class: titre lead -->

# Behavior-Driven Development

_Tom Avenel_

<https://www.avenel.pro/>

<!-- _footer: "© 2025 Tom Avenel under 󰵫  BY-SA 4.0" -->

---

## But

- **Conversation** entre _Business_, _Développeurs_ et _Testeurs_ pour décrire les **comportements** du programme à **tester** et à **implémenter**.

---

## Spécification par scénarios (User-Story)

- :star: Base : exemples issus de cas d'usages précis ;
- :scroll: En découlent les scénarios (exemples) : compréhension commune et précise de ce qui est à faire.
- But :
  - :office_worker: Retranscrire le besoin métier dans le code (idem DDD) : **communication** :speech_balloon:
  - :thumbsup: La fonctionnalité couvre tous les cas d'usages métiers
  - :white_check_mark: Un test valide, implémente et documente le scénario

---

> Given Fred has bought a microwave
> And the microwave costs 100eu
> When we refund the microwave
> Then Fred should be refunded 100eu

---

> **Given (a specific context)**
> **When (some action is carried out)**
> **Then (a particular set of observable consequences _should_ occur)**

---

## Chercher les cas d'erreur :x:

---

Dans quel **contexte** l'événement aboutira à un résultat différent ?

> Given Fred has bought a microwave
> And the microwave costs 100eu
> And the microwave was on 10% discount
> When we refund the microwave
> Then Fred should be refunded 90eu

---

Est-ce vraiment le seul **résultat** à vérifier ?

> Given Fred has bought a microwave
> And the microwave costs 100eu
> When we refund the microwave
> Then the microwave should be added to the stock count.

---

## Du scénario au critère d'acceptation :thumbsup:

---

> Given Fred has bought a microwave
> And the microwave costs 100eu
> And the microwave was on 10% discount
> When we refund the microwave
> Then Fred should be refunded 90eu

---

> Given an item was sold with a discount
> When the customer gets a refund
> Then he should only be refunded the discounted price

---

> Items should be refunded at the price at which they were sold.

---

## Comment écrire de bons scénarios :heavy_check_mark:

- :scroll: Avoir des noms de tests expressifs : le but de BDD est de documenter le produit depuis les scénarios
- :bulb: 1 phrase = 1 test
- :speech_balloon: Utiliser le langage (ubiquitaire) du métier : voir DDD
  - :warning: les experts métier doivent être disponibles !
- :star: Le BDD est piloté par la valeur métier (et donc, le développement !)

---

## Atelier 3 Amigos

- :office_worker: _Business_ : **Définit** le problème ou la fonctionnalité attendue, défini la valeur business (Product Owner, Business Analyst, ...) ;
- :technologist: _Développeurs_ : Suggèrent un **moyen** de corriger ce problème ou de créer la fonctionnalité ;
- :scientist: _Utilisateur / Testeur_ : Cherchent les **problèmes** et les failles dans le raisonnement.
- Autre rôles si nécessaire : _UX Designer_, _AdminSys_, …

---

### Communication

- BDD privilégie la **communication** plutôt que l'automatisation et la capture des conversations
  - Les scénarios sont avant tout des exemples d'utilisation plus qu'un engagement contractuel

---

![](http://www.arolla.fr/blog/wp-content/uploads/2012/06/bdd-dialogue.png)

<span class="legende">©www.arolla.fr</span>

---

![height:600px](https://blog.octo.com/le-bdd/behavior-driven-development-1-702x1024.webp)

<span class="legende">©blog.octo.com</span>

---

## Outils

- `Gherkin` : syntaxe des scénarios
- Implémentation :
  - `Cucumber` (`JavaScript`, `Ruby`, …)
  - `Behat` (`PHP`)
  - `Behave` (`Python`)
  - `JBehave`, `Spock` (`Java`)

---

### Exemple Gherkin

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

---

<!-- class: legal -->

# Legal

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]
- Exemples de user stories BDD provenant de [Liz Keogh][LizKeogh]

[site-perso]: https://www.avenel.pro/

