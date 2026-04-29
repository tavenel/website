---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Domain-Driven Design
tags:
- ddd
- archi
- hexagonal
- clean
---

## Problèmes communs aux projets informatiques

---

### MVC comme architecture

```mermaid
graph TD
  subgraph my_app
    View
    Controller
    Model[(Model)]
  end

  View --> Controller
  Controller --> Model
```

_Quel est le **but** de cette application ?_

---

```
📁 customer  
📁 helpbase  
📁 message  
📁 staffer  
📁 ticket
```

_Quel est le **but** de [cette application django](https://github.com/johnnncodes/ddd-python-django) ?_ 💡

---

### Application _CRUD_

1. Entité (`getter`/`setter`) + BDD auto-générée
2. ??? 🙈
3. API `REST` : _CRUD_ sur l'entité

_Quelle est la **logique métier** derrière ces entités ?_

---

### Modèle anémique

````md magic-move
```java
public class User {

    private String name;
    private String login;

}
```
```java
public class User {

    private String name;
    private String login;

    public String getName() { return this.name; }
    public void setName(String name) { this.name = name; }

    public String getLogin() { return this.login; }
    public void setLogin(String login) { this.login = login; }
}
```
````

- _Relation `name` / `login` ?_
- _Conditions de validation `name` et `login` ?_
- _Contexte de validité d'une instance ?_

---

### Domaine incohérent

```mermaid
classDiagram
  class UserAccount {
    +String address
  }
```

Problème : addresse de livraison différente ?

---

Solution : ajouter un champ optionnel ?

````md magic-move
```java
class UserAccount {
  address: String
}
```
```java
class UserAccount {
  address: String
  shippingAddress: String [0..1]
}
```
````

```java
mainAddress = userAccount.address ;
if (shippingAddress != null) {
    mainAddress = shippingAddress;
}
[…]
```

Et des **rustines** partout dans le code… 🙈

---

> Le produit en production est la compréhension du problème par le développeur.

---

![Ce que le client voulait vraiment](@assets/projet/balancoire.jpg)

<div class="caption">Ce que le client voulait vraiment</div>

---

## Un bon design ?

- Des cas d'utilisation **clairs** 🧑‍💼
- Facile à **maintenir** 🧰
- Facile à **tester** 🧪
- **Cohérent** et **facile** à comprendre 💭
- **Découplé** ⬅️ ➡️
- Résilient au **changement de technologie**

---

### Un bon design ! 🤓

```java
private static final boolean WILL_IT_RAIN_IN_LONDON = true;
```

- Le métier s'apprend en **lisant le code !**

---

# Le Domain-Driven Design (DDD)

---

## Objectif 🎯

> Le Domain-Driven Design, c'est avant tout la compréhension du métier par l'ensemble de l'équipe.

### Origine

_Eric Evans_, 2003

---

## Vision des équipes métier 🧑‍💼

> Le Domain-Driven Design c'est avant tout faire comprendre le cœur du métier à l'équipe technique.

---

## Vision des équipes techniques 🧑‍💻

> Le Domain-Driven Design c'est avant tout transcrire l'intention du métier dans le code.

---

![Le langage ubiquitaire](https://alexsoyes.com/wp-content/uploads/2022/04/ddd-ubiquitous-language-912x697.png)

<div class="caption">Le langage ubiquitaire. Source: alexsoyes.com</div>

---

## Principes

- **Modéliser** les conceptions complexes (`UML`, …)
- Mettre en avant le **domaine** et la **logique métier** associée plutôt que la technologie
- **Langage commun** pour tous (_ubiquitaire_)

---

<svg width="700" height="500" xmlns="http://www.w3.org/2000/svg">
  <style>
    .venn-circle {
      fill-opacity: 0.5;
      stroke: black;
      stroke-width: 2;
    }
    .text-label {
      font-size: 14px;
      text-anchor: middle;
    }
  </style>

  <circle cx="250" cy="250" r="200" stroke="#4DA6FF" stroke-width="3" fill="none" />
  <text x="150" y="190" text-anchor="middle" stroke="#4DA6FF" alignment-baseline="middle" font-size="18">
  <tspan>Contexte</tspan>
  <tspan dx="-90" dy="20">métier</tspan>
 </text>

  <circle cx="450" cy="250" r="200" stroke="#FF7B54" stroke-width="3" fill="none" />
  <text x="550" y="190" text-anchor="middle" stroke="#FF7B54" alignment-baseline="middle" font-size="18">
  <tspan>Conception</tspan>
  <tspan dx="-90" dy="20">technique</tspan>
 </text>

  <text x="270" y="250" fill="purple" font-size="22">
  <tspan>Langage</tspan>
  <tspan dx="-120" dy="20">Ubiquitaire</tspan>
 </text>
</svg>

<div class="caption">Le langage ubiquitaire à la rencontre du contexte métier et de la conception technique</div>

---

## Pourquoi utiliser DDD ? ✅

- Application **techniquement complexe**
- **Métier complexe**
- Haut **risque dans le métier** (banque, santé, …)
- L'efficacité de la solution dépend de la **compréhension du métier**

---

## Pourquoi ne pas utiliser DDD ? ❌

- Application basée **data / contenu** **(CMS, CRUD)**
- Application **techniquement simple**
- Domaine très **générique** ou peu de complexité métier
- Le DDD **prend du temps** (time to market)

---

# Stratégie vs tactique

- ****Stratégie**** : **définition** de l'objectif
- **Tactique** : comment _atteindre_ l'objectif (organisation du code)
- `DDD` est avant tout **stratégique**

---

## Méthodologie

- 🎯 Commencer par un **design stratégique**
- 💬 Définir le **langage ubiquitaire**
- ✂️ Découper le métier en **Bounded Context**
- 🔃 **Itérer**

---

## Domaine, Modèle, Bounded Context, Language ubiquitaire

---

### Domaine 🏢

- _Domaine_ : ce que fait une organisation (et comment)
  - un **langage dédié**
  - des **sous-domaines** : l'espace des problèmes à résoudre

> La sphère d'un métier ou activité pour lequel on développe l'application. (wikipedia)

---

### Modèle

- _Modèle_ : une **abstraction** qui représente une **partie d'un domaine**.

---

### Bounded Context 🧑‍💼

- _Bounded Context_ : limite de **validité** d'un modèle **(frontière linguistique)**
- Concept **métier** précis qui répond à une **problématique**.

---

## Architecture 🏗️

- Suit les _Bounded Context_
  - Pas de partage de code mais des **interactions** entre _Bounded Context_
  - Séparation en **modules**, **packages**, **mico-services**, …
  - Découpage en **couches** (si besoin) dans chaque _Bounded Context_.

> L'Architecture est une affaire d'Intention, pas de Frameworks. (Uncle Bob)

---

- **1 bounded context == 1 langage ubiquitaire**
  - Dans le contexte _culinaire_ : 🍅 est un _légume_
  - Dans le contexte _botanique_ : 🍅 est un _fruit_
  - Dans le contexte _théatral_ : 🍅 est un _feedback_

---

```mermaid
---
title: Domaine, Bounded Context & Langage Ubiquitaire.
---
graph TD
    subgraph Domaine
   subgraph Bounded_Context [Bounded Context]
        Vente["Contexte Vente (langage ubiquitaire)"]
   end
    end
```

:::tip
Un _Domaine_ peut englober plusieurs _Bounded Context_.
:::

---

## D'un langage ubiquitaire au modèle

---

### D'un langage ubiquitaire… 💬

- Pas uniquement un glossaire, des _phrases entières (simples)_
- Provient du **métier**
  - Éliminer les **synonymes**
  - Coder dans la **langue du métier**…
  - …ou s'accorder sur les **traductions** !

---

> Si vous ne pouvez expliquer un concept à un enfant de six ans, c'est que vous ne le comprenez pas complètement. (Albert Einstein)

---

### …Au modèle 🗂️

- **Le langage est le modèle**
  - langage => modèle (puis => langage)
- ~Pas de **duplication du modèle**~ 🚫
- Privilégier plusieurs éléments **simples** pour faire des modèles plus complexes 🖇️
- ~Pas de **technique** dans le modèle~
- Utiliser les termes du **métier** dans le code 🧑‍💼

---

![Un exemple de fonction mal nommée](https://programmerhumor.io/wp-content/uploads/2021/05/programmerhumor-io-8fb4c03b81cbbab-758x621.png)

<div class="caption">Un exemple de fonction mal nommée. Source: programmerhumor.io</div>

---

## Définir le langage 💬

---

### Objectifs 🎯

1. Clarifier le **besoin métier** entre les différents experts du domaine
2. **Simplifier** les définitions

---

### L'atelier d'Event Storming

- Réunit les parties prenantes 👥
  - **inclus les développeurs** 🧑‍💻
- Brainstorming :
  - **fonctionnalités** 💡
  - **vocabulaire** 💬
  - pas de **détail technique** ! ⛔

---

![Livre Event Storming (Alberto Brandolini)](https://www.eventstorming.com/images/book-cover.11a5.jpg)

<div class="caption">Livre Event Storming (Alberto Brandolini).</div>

---

### Brainstorming

1. Trouver les **idées** 💡 (penser _objectifs_ 🎯 )
2. **Regrouper** les idées 🖇️
3. Trouver les **déclencheurs** (_event triggers_) ▶️

[Exemple de brainstorming][brainstorming-example]

---

### Formalisation

1. Identifier les **acteurs** 🙋 et les **prioriser** 🔢
2. Identifier les **cas d'utilisation** 🤹
3. Identifier les **interactions** entre les cas d'utilisation 🤼‍♂️
4. Identifier les **entités**
5. Diagramme de **classes** (ou **code** directement) : décrit le **glossaire** 📒

---

### Diagramme de cas d'utilisation

```mermaid
---
title: Diagramme de cas d'utilisation d'un vidéoclub 
---
flowchart LR
    %% Acteurs
    Client["🧑 Client"]
    adherent["🧑 Adhérent"]
    nadherent["🧑 Non adhérent"]
    abo["🧑 Abonné"]
    nabo["🧑 Non abonné"]

    %% Cas d'utilisation
    adhesion["(Demande d'adhésion)"]
    location["(Location cassettes)"]
    retour["(Retour Cassette)"]
    abonnement["(Demande d'abonnement)"]
    auth["(Authentification)"]

    %% Hiérarchie des acteurs
    Client --> adherent
    Client --> nadherent
    adherent --> abo
    adherent --> nabo

    %% Relations acteur → cas d'utilisation
    nadherent --> adhesion
    adherent --> location
    adherent --> retour
    nabo --> abonnement

    adhesion -->|utilise| auth
    location -->|utilise| auth
    retour -->|utilise| auth
    abonnement -->|utilise| auth
```

---

### Diagramme de classe

```mermaid
---
title: Exemple de diagramme de classes pour le modèle d'une librairie
---

classDiagram

  class Book {
    +String title
    +Author author
    +String summary
    +String ISBN
    +List~Genre~ genre
    +Language language
  }

  class Genre {
    +String name
  }

  class Language {
    +String name
  }

  class BookInstance {
    +String uniqueId
    +DateField due_back
    +LOAN_STATUS status
    +Book book
    +String imprint
    +User borrower
  }

  class Author {
    +String name
    +DateField date_of_birth
    +DateField date_of_death
    +List~Book~ books
  }

  Author "1" --> "1..*" Book
  Book "1..*" --> "1..*" Genre
  Book "1" --> "1" Language
  Book "1" --> "0..*" BookInstance
```

---

### Loi de Brandolini

> La quantité d'énergie nécessaire pour réfuter des sottises […] est supérieure d'un ordre de grandeur à celle nécessaire pour les produire.
>
> _Bullshit asymmetry principle, Brandolini_

- Event storming (très) long (~3 jours) 💤
  - à **découper** (meilleure acceptation) 🪚

---

## Patterns stratégiques

- Comment définir et découper le domaine ?

---

### Distillation du Core Domain

La **distillation du Core Domain** permet de se concentrer sur les éléments les plus importants du modèle du domaine.

Plusieurs stratégies permettent d'y parvenir :

---

1. **Sous-domaines génériques**  
   - Extraire les sous-domaines qui ne sont pas la raison principale de construire le système.
2. **Déclaration de vision du domaine**  
   - Vision haut niveau du système pour définir le domaine principal.
3. **Domaine principal mis en évidence**  
   - Identifier les parties principales du modèle appartenant au Core (sans les extraire pour l'instant).
4. **Mécanismes cohérents**  
   - Repérer les mécanismes du modèle qui fonctionnent généralement ensemble.
5. **Core séparé**
   - Détacher les fonctionnalités de support du Core.
6. **Core abstrait**  
   - Viser des concepts abstraits dans le Core réutilisables dans les sous-domaines spécialisés.

---

```mermaid
---
title: Exemple de Domaine
---
graph TD
  subgraph Domain
    TR[Trading Room]
    Risk[Risk]
    IT[Information Technology]
    Financial[Financial]
    HR[Human Ressources]
    Account[Account]
  end
```

```mermaid
---
title: Exemple de Domaine distillé
---
graph TD
  subgraph Domain
    tr[Trading Room]
    r[Risk]
    subgraph b[" "]
      HR[Human Ressources]
      IT[Information Technology]
    end
    f[Financial]
    a[Account]
  end

  tr --- r
  tr --- f
  tr --- b
  r --- b
  r --- a
  a --- b
  f --- b
```

---

### Découpage

- ⭐ un **core domain** : le _problème principal_
  - c'est la **raison d'exister** de l'organisation
  - **petit**, à **refactorer**
  - 🚨 doit être bien conçu (_design hexagonal_, …)
- 🙏 au moins un **sous-domaine** venant en **support**
  - moins critique
- (éventuellement) des sous-domaines **génériques**
  - aident le métier
  - souvent des intégrations de solutions externes

---

```mermaid
---
title: Un découpage en sous-domaines
---
graph TD
 SD1["Sous-domaine de Support"]
 SD2["Sous-domaine Générique"]
 SD3["Sous-domaine Générique"]
 SD4["Sous-domaine de Support"]
 CD["Domaine Principal (Core Domain)"]
 SD5["Sous-domaine Générique"]
```

---

### Comparaison des domaines

| Type de domaine | Complexité du modèle | Différenciant business |
|-----------------|----------------------|------------------------|
| Core Domain     |   Très complexe      |   Élevé                |
| Support         |    Complexe          |   Moyen                |
| Générique       |    Simple            |   Faible               |

---

```mermaid
flowchart TD
    A["La solution peut-elle être achetée/intégrée?"] -->|Oui| B["Cela mettra-t-il en péril l'entreprise ?"]
    A -->|Non| C["Complexité de la logique métier?"]
    B -->|Oui| D["Domaine Principal"]
    B -->|Non| E["Sous-domaine Générique"]
    C -->|Complexe| D
    C -->|Simple| F["Sous-domaine Support"]
```

---

### Exemple d'un dentiste

- Le **core domain** 🦷 : **soigner** les dents du patient
  - Notion de `patient` 🤕 (historique des soins, …)
- Un sous-domaine de **support** 📅 : gérer les **rdv** du patient
  - Notion de `patient` 👤 (informations de contact, paiement, …)
- Les 2 domaines ont besoin d'un modèle **différent** de patient (chacun dans son `Bounded Context`)
- Un sous-domaine **générique** de **facturation**

---

:::tip
La frontière entre domaines peut être floue !
:::

> All models are wrong, but some are useful. (George Box)

---

## Propagation du domaine

- Quelles relations entre domaines ?
- Comment faire interagir différents domaines ?

---

### Carte de contexte

- Document représentant les **relations** entre Bounded Context
- Diagramme ou document écrit
- Niveau de détail variable

---

```mermaid
---
title: Une Context Map simple.
---
graph TD
  subgraph Domaine
    BC1["Bounded Context : Customer (Downstream)"]
    BC2["Bounded Context : Sales (Upstream)"]

    BC1 -.-|Relation Upstream/Downstream| BC2
  end
```

---

## Patterns de collaboration

---

### Shared Kernel (Noyau partagé)

- Relation entre 2+ _Bounded Context_ qui partagent du code, des données, …
- Création d'un **contexte partagé** (en dépendance) :
  - évite la **duplication**
  - **collaboration forte** : doit **notifier** chaque contexte dépendant des changements

---

#### Exemple de noyau partagé

- Plateforme de commerce électronique :
  - une boutique en ligne
  - une application mobile
- Mêmes comptes clients, même historique des commandes, …
  - dans un noyau partagé
  - BDD commune

---

```mermaid
---
title: Shared Kernel (LIB)
---
flowchart LR
 subgraph s1["RÉSERVATION"]
        booking[["Réservation"]]
        comfort_class["Classe"]
        schedule["Horaires"]
  end
 subgraph subGraph1["SHARED-KERNEL (LIB)"]
        shared_comfort_class["Classe<br>(économique, business, …)"]
        shared_schedule["Horaires"]
  end
 subgraph RECHERCHE["RECHERCHE"]
        search[["Recherche"]]
        search_comfort_class["Classe"]
        search_schedule["Horaires"]
  end
    booking --> comfort_class & schedule
    comfort_class -.-> shared_comfort_class
    schedule -.-> shared_schedule
    search --> search_comfort_class & search_schedule
    search_comfort_class -.-> shared_comfort_class
    search_schedule -.-> shared_schedule

    class comfort_class,shared_comfort_class,search_comfort_class blue
    class schedule,shared_schedule,search_schedule green
```

---

### Partnership

- Deux équipes co-conçoivent un processus critique (ex. : paiement + facturation)
- **Coopération étroite** avec **responsabilité partagée**.
- Direction **Bilatérale**
- **Couplage élevé**
- **Coordination forte** : les équipes travaillent ensemble, co-décident des événements partagés, synchronisent leurs livraisons.

---

#### Exemple de Partnership

- Contexte métier : Billetterie en ligne
- Deux Bounded Context : _Réservations_ et _Paiement_ qui doivent travailler ensemble de façon étroite car :
  - La réservation d'une place dépend directement de la validation du paiement.
  - Pas de réservation si le paiement échoue, pas de paiement si l'événement est complet.
- Les deux équipes doivent **décider ensemble** :
  - Des **événements métier** à émettre (ex. : `PaiementAutorisé`, `RéservationConfirmée`).
  - Des **modèles** de données minimaux à **partager**.
  - Du protocole de **communication** (saga, orchestration, messages, etc.).
- Les **évolutions** sont **coordonnées** (release synchronisées, backlog partagé, etc.).

---

### Customer / Supplier (Client / Fournisseur)

- Relation : un _Bounded Context_ **expose un service** (ou des données) à un autre.
- Aussi appelé : _Downstream_ (Client) / _Upstream_ (Supplier)
- Le contexte _Upstream_ (_Supplier_) **publie** un modèle ou des données
- Le contexte _Downstream_ (_Client_) **consomme** ces données pour répondre à ses propres besoins métier.
- Relation asymétrique :
  - Le fournisseur n'a **pas connaissance de ses clients** (forte autonomie).
  - Le **client s'adapte** aux évolutions de l'upstream en subissant ses choix (mais peut gérer son propre modèle).
  - **Couplage faible à moyen**

---

#### Exemple de Customer / Supplier

Un système de gestion d'inventaire (_downstream_) consomme les définitions de produits d'un système de catalogue produits (_upstream_), mais ne peut pas modifier ce modèle.

- Contexte "**Gestion des Produits et des Clients**" (_Upstream_ / _Fournisseur_) :
  - Responsable centralisé de la définition du modèle des produits, des clients et de leurs règles métier.
  - Publie les événements de modification (ajout, mise à jour, suppression) des produits et expose une API publique (ou un flux d'événements)
- Contexte "**Gestion de l'Inventaire**" (_Downstream_ / _Client_) :
  - Dépend des données produit fournies par le contexte "Gestion des Produits".
  - Consomme les événements ou les API exposées pour maintenir sa propre vue locale de l'inventaire des produits.
  - Adapte son modèle interne en fonction du modèle publié en amont.
- Contexte "**Réservation**" (_Downstream_ / _Client_) :
  - S'appuie sur le modèle produit du contexte "Gestion des Produits".
  - Consomme les mêmes interfaces publiques pour proposer des réservations cohérentes avec les produits disponibles.
  - Peut enrichir localement le modèle sans influencer le fournisseur.

```mermaid
---
title: Exemple de relation Client/Fournisseur
---
graph LR
  Products["Gestion des Produits<br/>(et des Clients)"]
  Inventory["Gestion de l'Inventaire"]
  Reservation["Réservation"]

  Products -->|"Fournit<br/>(Modèle produit,<br/>Événements,<br/>API publique)"| Inventory
  Products -->|"Fournit<br/>(Modèle produit,<br/>Événements,<br/>API publique)"| Reservation
```

---

### Conformiste

- Relation subie ou acceptée : le client **adhère pleinement** au modèle (et conventions, règles, …) de l'équipe fournisseur
- Pas de séparation stricte : le client reprend **tel quel** le modèle, les règles métier, voire les implémentations.

:::warn
Introduit un **fort couplage** et réduit la flexibilité du client.
:::

---

#### Exemple de Conformiste

- Équipe chargée de gérer l'inventaire des produits dans un entrepôt.
  - même modèle que dans le contexte responsable de la gestion des commandes, des clients et des produits.
- Module de _Recherche_ conforme à un module de _Réservation_ .

---

```mermaid
---
title: CONFORMISTE (COMPOSANTS)
---
graph LR
  subgraph ReservationContext["RÉSERVATION"]
    subgraph selection[«Sélection»]
      getter("getSelection() : SPI")
    end
  end

  subgraph RechercheContext["RECHERCHE"]
    subgraph selection2[«Sélection»]
      getter2("getSelection() : API")
    end
  end

  getter2 -->|Conformiste| getter

  class selection2,getter,getter2 blue
```

---

```mermaid
---
title: CONFORMISTE (LIB)
---
graph LR
  subgraph ReservationContext["RÉSERVATION"]
    price[«Component» Prix]
    discount[«Component» Discount]
    amount[Quantité]
    currency[Devise]

    price --> amount
    price --> currency
    discount --> amount
    discount --> currency
  end

  subgraph MonnaieLib["MONNAIE (LIB)"]
    amount2[Quantité]
    currency2[Devise]
  end

  amount -.-|Conformist| amount2
  currency -.-|Conformist| currency2

  class ReservationContext,price,discount blue
  class MonnaieLib,amount,amount2,currency,currency2 green
```

---

### Open Host Services (Services Hôtes)

- Rend disponible **explicitement** des systèmes / services **communs** à différents _Bounded Context_
  - _RESTful API_, …
- Définit un **modèle commun d'intégration**
- Encourage le **découplage** et la **stabilité contractuelle**.

:::tip
C'est un point d'entrée standardisé, conçu pour l'interopérabilité.
:::

---

#### Exemple de pattern Open Host Service

- _Open Host Service_ de paiement à distance (possède sa propre logique)
- À intégrer dans différents contextes de l'application

---

```mermaid
graph LR
  subgraph ReservationContext["RÉSERVATION"]
    subgraph domain1["Domain"]
      train[«Entity» Train]
      getTrainsToBook["getTrainsToBook()<br/>(SPI)"]
    end
  end

  subgraph RechercheContext["RECHERCHE"]
    subgraph domain2["Domain"]
      domain_selection[«Entity» Selection]
      getSelection["getSelection()<br/>(API)"]
    end

    subgraph infra["Infrastructure"]
      inproc_train["«Entity» Train<br/>(copie locale)"]
      selection[«Adapter» Sélection]
      getTrainsToBookImpl["getTrainsToBook()<br/>(implémentation)"]

      selection -->|Open Host| inproc_train
    end
  end

  getSelection --> getTrainsToBookImpl
  getTrainsToBookImpl --> getTrainsToBook

  class domain1,train,inproc_train,getTrainsToBook,getTrainsToBookImpl blue
  class domain2,domain_selection,selection,getSelection green
```

---

### Published Language (Langage publié)

- Version formelle des service hôtes : **publication du modèle (et donc langage) commun**
  - `JSON`, `XML`, …

---

### Couche Anticorruption (ACL)

- **Protège** un _Bounded Context_ des complexités et incohérences d'un autre modèle
- **Traducteur** et **validateur** entre deux modèles
- **Inverse** de l'_Open Host_
- Souvent utilisé dans un _Customer/Supplier_

---

#### Exemple de pattern ACL

- Système e-commerce s'intégrant à un ancien système de gestion des stocks (ancien modèle de données)
- L'_ACL_ traduit les concepts, données et messages entre les 2 systèmes

---

```mermaid
---
title: Couche Anticorruption
---
graph LR
  subgraph ReservationContext["RÉSERVATION"]
    subgraph domain1["Domain"]
      train[«Entity» Train]
      getTrainsToBook["getTrainsToBook()<br/>(SPI)"]
    end

    subgraph infra1["Infrastructure"]
      selection[«ACL Adapter» Sélection]
      getTrainsToBookImpl["getTrainsToBook()<br/>(implémentation)"]
      selection -->|ACL| train
    end
  end

  subgraph RechercheContext["RECHERCHE"]
    subgraph domain2["Domain"]
      domain_selection[«Entity» Selection]
      getSelection["getSelection()<br/>(API)"]
    end
  end

  getSelection --> getTrainsToBookImpl
  getTrainsToBookImpl --> getTrainsToBook

  class domain1,train,infra1,getTrainsToBook,getTrainsToBookImpl blue
  class domain2,domain_selection,selection,getSelection green
```

---

### Separate Ways (Chemins Séparés)

- Contextes très **indépendants** les uns des autres (_y compris technologiquement_)
- Évoluent **séparément**
- Idée de **modularité**

---

#### Exemple de Chemins Séparés

1. Application principale de e-commerce
2. Système de gestion des stocks indépendant (propre domaine et logique métier)

- Communique avec l'application via une file de messages bien définie
- Développé et maintenu par une équipe distincte

---

```mermaid
---
title: Separate Ways
---
classDiagram
    note for ClientPourFacturation "Classe dupliquée contexte Facturation"
    class ClientPourFacturation {
        +addresseDeFacturation
        +récupérerDevis()
    }

    note for ClientPourMarketing "Classe dupliquée contexte Marketing (aucun lien)"
    class ClientPourMarketing {
        +addresseDeContact
        +listerProduitsRécents()
    }
```

---

### 📊 Tableau comparatif

| Pattern                         | Type de relation        | Couplage            | Autonomie du client | Collaboration entre équipes | Cas typique                                                 |
| ------------------------------- | ----------------------- | ------------------- | ------------------- | --------------------------- | ----------------------------------------------------------- |
| **Conformiste**                 | Dépendance passive      | Fort            | Nulle               | Faible / subie              | L'équipe cliente reprend tel quel le modèle de l'upstream   |
| **Upstream / Downstream**       | Dépendance déclarée     | Variable            | Moyenne à forte     | Faible ou indirecte         | Un fournisseur expose des données, un client les consomme   |
| **Partnership**                 | Coopération symétrique  | Contrôlé            | Partagée            | Forte                   | Deux domaines fortement liés conçus ensemble                |
| **Open Host**                   | Interface d'intégration | Faible              | Variable            | Faible                      | API ou événements publics accessibles à tout autre contexte |
| **Published Language**          | Langage partagé         | Moyen               | Moyenne             | Moyenne                     | JSON schema, GraphQL, ou Avro communs à plusieurs équipes   |
| **Anti-Corruption Layer (ACL)** | Barrière d'adaptation   | Faible (localement) | Forte           | Faible / unilatérale        | Adapter un modèle externe sans l'importer tel quel          |
| **Separate Ways**               | Aucune relation         | Aucun           | Totale          | Nulle                   | Les domaines évoluent totalement indépendamment             |

---

### 📌 Résumé mnémotechnique

| Besoin                                | Pattern recommandé        |
| ------------------------------------- | ------------------------- |
| Reprendre un modèle existant tel quel | **Conformiste**           |
| Coopérer à égalité                    | **Partnership**           |
| Protéger mon modèle                   | **ACL**                   |
| Exposer un contrat public             | **Open Host**             |
| Partager un langage stable            | **Published Language**    |
| Ne pas collaborer                     | **Separate Ways**         |
| Définir une relation asymétrique      | **Upstream / Downstream** |

---

### Context Map

- **Carte de contexte** : formalise les relations entre les _Bounded Context_.

---

#### Exemple de context map

```mermaid
---
title: Exemple de Context Map d'une compagnie d'assurance
---
graph LR
  %% Bounded Contexts
  subgraph CSSC["Customer Self-Service"]
    cssc_d[D]
  end

  subgraph PC["Printing"]
    pc_u["OHS ou PL<br/>U"]
  end

  subgraph CMC["Customer Management"]
    cmc_u[U]
    cmc_d["ACL<br/>D"]
    cmc_u2["OHS ou PL</br/>U"]
  end

  subgraph DCC["Debt Collection"]
    dcc_d["ACL<br/>D"]
  end

  subgraph rmc["Risk Management"]
  end

  subgraph PMC["Policy Management"]
    pmc_d["ACL<br/>D"]
    pmc_d2["CONFORMIST<br/>D"]
  end

  %% Relations
  cmc_u -->|Upstream/Downstream| cssc_d
  cmc_u2 -->|Conformist| pmc_d2

  pc_u -->|ACL| cmc_d
  pc_u -->|ACL| pmc_d
  pc_u -->|ACL| dcc_d

  pmc ---|Shared Kernel| DCC
  pmc ---|Partnership| rmc
```

---

```mermaid
mindmap
  root((Context Map))

    Superposition de contextes
      Shared Kernel

    Contextes coopérant fortement
      Partnership

    Crée un lien de coopération
      Customer/Supplier Teams

    Crée un lien unidirectionnel
      Conformist

    Supporte différents clients
      Open Host Service
        Version formelle
          Published Language

    Libère les contraintes entre équipes
      Separate Ways

    Traduis et isole unilatéralement
      Anticorruption Layer

    Évaluation et examen des relations
      Bounded Context
        nommage
          Ubiquitous Language
        garde le modèle unifié
          Continuous Integration
```

<div class="caption">Résumé des patterns stratégiques.</div>

---

### Objectifs

- Limiter la complexité du système à la charge cognitive de l'équipe
- Collaboration a minima (complexe)
  - sinon : envisager la creation d'un nouveau composant au milieu pour limiter les impacts

---

## Patterns tactiques

---

- `Entity` - Objet modélisant une partie du domaine - a un ID et est mutable.
- `Value Object` - Objet immuable identifiée par ses attributs.
- `Aggregate` - Encapsule différentes entitées et value objects.
- `Repository` - Bibliothèque permettant d'accéder aux aggrégats.
- `Module` - Abstraction permettant de réduire la charge mentale.
- `Factory` - Design pattern permettant de créer des objets.
- `Domain Service` - Objet sans état qui encapsule une logique compliquée du domaine.
- `Application Service` - Orchestrateur entre le monde extérieur (interface utilisateur, API, etc.) et le domaine métier.

---

- `Dependency Injection` : L'objet ne crée pas lui-même ses dépendances, elles sont injectées depuis l'extérieur.
- `Split Entities` : Diviser une `Entity` en plusieurs entités dans différents _Bounded Context_.
- `Policy` : Règle métier qui décrit une contrainte métier applicable à un _Bounded Context_.
- `Invariant` : Règle métier toujours vraie garantissant la cohérence et l'intégrité du modèle de domaine.
- `Specification Pattern` : Encapsuler des règles métier dans un objet réutilisable, combinable et testable.
- `Command Query Responsibility Segregation (CQRS)` : Sépare les responsabilités de lecture (`Query`) et d'écriture (`Command`)

---

- `Domain Event` : Événement significatif dans le domaine métier (changement d'état, action importante).
- `Eventual Consistency` : Permet à des _Bounded Context_ de communiquer via des événements, sans nécessiter une synchronisation immédiate. La cohérence avec le domaine est effectuée plus tard.
- `Event Sourcing` : Reconstruit l'état du domaine à partir d'une série d'événements.
- `Saga` : Gère la _cohérence éventuelle_ de processus métier de longue durée impliquant plusieurs services ou agrégats.
- `Process Manager` : Orchestrateur central qui coordonne des processus métier complexes qui impliquent plusieurs services ou agrégats.

---

- Rappels sur les [Value Object et Factory](https://opus.ch/en/ddd-concepts-and-patterns-value-object-and-factory/)
- Rappels sur les [Services et Bibliothèques](https://opus.ch/en/ddd-concepts-and-patterns-service-and-repository/)
- Rappels sur les [Aggrégats et les Modules](https://opus.ch/en/ddd-concepts-and-patterns-aggregate-and-module/)
- Voir le document de cours sur les patterns tactiques.

---

```mermaid
mindmap
  root((Domain-Driven Design))

    expression du modèle
      Services
      Value Objects
      Entities
        Propriété, frontières et intégrité des objets
          Aggregates

    Accès aux données, ignore la persistance
      Repositories

    Création des objets
      Factories
```

<div class="caption">Patterns tactiques de base.</div>

---

## Intégration continue

- 🔃 Le DDD est **itératif** (=> CI)
- 🤔 **Repenser** régulièrement les `Bounded Context` et **changer le type de propagation** au besoin

---

## XP, Agilité, BDD

- `DDD` s'associe particulièrement bien avec les méthodes agiles (`XP`, …)
- Le `BDD` (Behavior-Driven Development) permet de faire le lien par le langage des spécifications (**par l'exemple**) au code

---

## Architecture

---

### Patterns spécifiques d'architecture

- DDD ne définit pas d'architecture spécifique
- Candidats intéressants :
  - _Architecture Hexagonale_
  - _Clean Architecture_
  - _[L'architecture explicite][archi-explicite] combine le tout_

---

### Architecture à Grande Échelle

DDD utilise les concepts d'**architecture à grande échelle** pour organiser le système au niveau des composants ou des couches. Cette organisation guide les développeurs sur la l'endroit où trouver ou ajouter une fonctionnalité dans le code.

- Architectures classiques : basées sur des considérations techniques
- Archicture à grande échelle : basée sur des concepts liés au domaine

---

- **Ordre évolutif** : laisser la structure évoluer avec le temps.
- **Métaphore système** : rechercher une métaphore globale pour le système.
- **Couches de responsabilité** : organiser le modèle de domaine en plusieurs couches.
- **Niveau de connaissance** : permettre la configuration des opérations principales à partir d'un niveau de connaissance.
- **Cadre de composants plug-and-play** : abstraction du cœur avec une infrastructure de plugins.

---

### Design Souple (Supple Design)

Idée : concevoir le logiciel de manière intuitive pour le développement et la maintenance.

Voici des **patterns** qui favorisent un design souple :

---

1. **Interfaces explicites**
   - Noms significatifs, utilisation du langage ubiquitaire.
2. **Fonctions sans effets de bord**  
   - Privilégier les fonctions qui renvoient des résultats sans modifier d'état du système.
3. **Assertions**  
   - Énoncer explicitement les post-conditions et les invariants des classes.
4. **Contours conceptuels**  
   - Décomposer le logiciel en unités cohérentes.

---

1. **Classes autonomes**  
   - Réduire les dépendances pour alléger la charge mentale.
2. **Opérations dans des ensembles clos**  
   - Les opérations doivent idéalement retourner le même type que leurs arguments.
3. **Design déclaratif**  
   - Utiliser un style de programmation déclaratif si possible.

---

## Résumé

```mermaid
mindmap
((Domain-Driven Design))
  isolate domain with
    )Layered Architecture(
  express model with
    {{Services}}
    {{Domain Events}}
    {{Entities}}
    {{Value Objects}}
    encapsulate with
      {{Aggregates}}
      {{Factories}}
    access with
      {{Repositories}}
  model gives structure to
    )Ubiquitous Language(
      cultivate rich model with
        Core Domain
          avoid overinvesting in
            Generic Subdomains
      names enter
        )Bounded Context(
  define model within
     )Bounded Context(
       keep model unified by
         Continuous Integration
       assess/overview relationships with
         )Context Map(
           overlap allied contexts through
             {{Shared Kernel}}
           relate allied contexts as
             {{Customer / Supplier}}
           minimize translation
             {{Conformist}}
           support multiple clients through
             {{Open Host Service}}
               formalize as
                 {{Published Language}}
           free teams to go
             {{Separate Ways}}
           translate and insulate unilaterally with
             {{Anti-Corruption Layer}}
           segregate the conceptual messes
             )Big Ball of Mud(
```

<div class="caption">Résumé du Domain Driven Design. Inspiré de : <a href="https://www.domainlanguage.com/ddd/reference/">Eric Evans (CC By).</a></div>

---

## Conseils et points de vigilance

---

- 🚫 Ne pas utiliser la **même architecture** pour tous les contextes bornés.
  - Certains contextes sont moins complexes que d'autres.
- 🚫 Ne pas **réutiliser** un modèle existant ( ⚠  **1 domaine == 1 problématique** )
- 💡 **Comprendre** les problèmes métier avant d'essayer des résoudre une problématique technique.
- ⚠ Ne pas négliger la **carte de contexte**.
- ✂️ Définir clairement les **limites du contexte**.
- 🤔 Résoudre les problèmes d'**ambiguité** (impact fort sur le logiciel).
  - En particulier lorsque la logique métier est complexe.

---

- 🤓 DDD n'a **PAS** pour but ~~d'ajouter des couches d'abstraction~~
  - Mais **d'isoler la logique métier** !
- ❌ Peu adapté à un ~~domaine simple~~
  - ou si les acteurs du métier ne sont pas impliqués
  - 💵 **coûteux** en ressources et en temps
- ❌ DDD est **incompatible** avec un design par _Smart UI_

---

- Partage de base de données possible entre contextes mais **séparer les schémas**
- Les **tests** doivent aussi êtres **séparés par contextes**
- _Shared kernel_ : OK si partagé comme librairie, sinon sûrement un _code smell_ !
- _Conformist_ : toujours ajouter un _Service Provider Interface (SPI)_, même si le contrat est le même (voir architecture hexagonale)
- Éviter trop de verbiage entre modules (~~RPC~~, …)
- _DDD_ n'est pas ~~synonyme de _microservice_~~ : commencer par un monolithe modulaire, tester en production, passer aux microservices (si besoin ops)

---

## DDD depuis l'existant

- Peut être complexe à mettre en place (métier mal défini, mal isolé, …)
- Privilégier des patterns stratégiques pour isoler le nouveau métier
- 💡 : générer un nuage de mots depuis le code pour extraire le langage

---

## Exemples de langage ubiquitaire

Voici quelques exemples de **mauvaise communication entre métier et technique** à corriger par l'usage du **langage ubiquitaire** :

---

### ⚠️ **Exemple 1 : Nom de fonction technique non explicite**

#### ❌ Avant (langage technique ambigu)

```java
userService.processData(user);
```

**Problème** : que signifie "processData" ? Est-ce une mise à jour du profil ? Une inscription ? Un calcul ? Aucun lien avec le métier.

:::correction

#### ✅ Après (langage ubiquitaire orienté métier)

```java
userService.registerNewCustomer(user);
```

**Amélioration** : Le terme métier _"register"_ est explicite et repris des discussions avec les experts. "Customer" est un mot métier utilisé dans les specs.
:::

---

### ⚠️ **Exemple 2 : Nom d'entité incohérent avec le métier**

#### ❌ Avant (nom générique ou erroné)

```java
class Transaction { 
    private Date startDate; 
    private Date endDate;
}
```

**Problème** : en contexte métier, il s'agit de **réservations**, pas de transactions financières.

:::correction

#### ✅ Après

```java
class Reservation {
    private LocalDate startDate;
    private LocalDate endDate;
}
```

**Amélioration** : "Reservation" correspond au langage des utilisateurs métier (hôtellerie, location, etc.). Cela améliore la communication et la compréhension du code.
:::

---

### ⚠️ **Exemple 3 : Vocabulaire flou ou contradictoire entre équipes**

#### ❌ Avant (entendu en réunion technique)

> "On a un `client`, c'est l'utilisateur connecté, mais aussi un `customer` dans Stripe, et parfois un `user` dans l'app mobile."

**Problème** : 3 termes pour désigner la même chose = confusion sur les rôles, les permissions, les données.

:::correction

#### ✅ Après (langage ubiquitaire)

> "On utilise **Customer** partout pour désigner l'utilisateur qui paie, y compris dans Stripe et dans notre modèle métier. Pour les logins et tokens, on parle d'**Account**."

**Amélioration** : unification du vocabulaire métier > technique. Plus de synonymes inutiles. Le mot "Customer" devient une **pièce centrale du modèle**.
:::

---

### ⚠️ **Exemple 4 : Problème de contexte implicite**

#### ❌ Avant

```java
product.getPrice();
```

**Problème** : le prix dépend-il d'une réduction ? D'une devise ? D'une date ? C'est flou.

:::correction

#### ✅ Après

```java
product.getEffectivePriceAt(date, country, customerGroup);
```

**Amélioration** : l'intention métier est exprimée clairement ; les dépendances contextuelles sont explicites.
:::

---

### ⚠️ **Exemple 5 : Utilisation d'abréviations obscures**

#### ❌ Avant

```python
svc.add_cr2(u);
```

**Problème** : "svc" ? "cr2" ? "u" ? Incompréhensible hors contexte.

:::correction

#### ✅ Après

```python
courseService.createRecurringCourseRequest(user);
```

**Amélioration** : expression claire, alignée avec les termes métier ("Recurring Course Request").
:::

---

# Ressources

- [Articles sur le DDD (opus.ch)](https://opus.ch/en/category/ddd-en/)
- [Présentation du DDD (dieuxducode.com)](https://lesdieuxducode.com/blog/2019/7/introduction-au-domain-driven-design)
- [Résumé du DDD (blog.scottlogic.com)](https://blog.scottlogic.com/2018/03/28/domain-driven-design.html)
- [Alex Soyes - DDD](https://alexsoyes.com/ddd-domain-driven-design/)
- [Blog Opus Software - articles DDD](https://opus.ch/en/blog/)
- [DDD 101 - The 5-Minute Tour (medium.com)](https://medium.com/the-coding-matrix/ddd-101-the-5-minute-tour-7a3037cf53b8)
- [DDD en 5 minutes (cdiese.fr)](https://cdiese.fr/domain-driven-design-en-5-min/)
- [DDD vs Clean architecture en images](https://khalilstemmler.com/articles/software-design-architecture/domain-driven-design-vs-clean-architecture/)
- [Exemple de brainstorming (event storming)][brainstorming-example]
- Ressources pour l'event storming : <https://github.com/mariuszgil/awesome-eventstorming>

- [Stratégies d'organisation du code (medium.com)](https://medium.com/@msandin/strategies-for-organizing-code-2c9d690b6f33)
- [Martin Fowler : domain data layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html)
- [De CRUD à DDD - Comment Meetic a sauvé son legacy (slides)](https://speakerdeck.com/jmlamodiere/de-crud-a-ddd-comment-meetic-a-sauve-son-legacy)
- [Architecture explicite][archi-explicite]
- [Application de poésie](https://github.com/tpierrain/hexagonalThis)
- [Exemple complet en DDD, de l'Event Storming à l'implémentation](https://github.com/ddd-by-examples/library/)
- [Exemple d'application en DDD (Eric Evans)](https://github.com/citerus/dddsample-core)
- [Un autre exemple de DDD](https://github.com/mattia-battiston/clean-architecture-example)
- [Exemple d'application Django en DDD](https://github.com/johnnncodes/ddd-python-django)
- [Exemple d'application Python en Clean Architecture](https://github.com/stkrizh/realworld-aiohttp)
- [Discussion about DDD in Symfony issues](https://github.com/symfony/symfony-docs/issues/8893)
- <https://dddinpython.com/>
- <https://teamtopologies.com>
- [Exemples de ContextMap et outil permettant de générer les cartes](https://github.com/ContextMapper/context-mapper-examples)

[brainstorming-example]: https://openclassrooms.com/fr/courses/5647281-appliquez-le-principe-du-domain-driven-design-a-votre-application/6828051-identifiez-les-objectifs-de-votre-application-avec-levent-storming#/id/r-6828246
[archi-explicite]: https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/

---

## Livres

- _Domain-Driven Design, Tackling Complexity in the Heart of Software, Eric Evans, 2003._
- _Implementing Domain-Driven Design, Vaughn Vernon, 2013._
- [Living Documentation (Cyrille Martaire)](https://leanpub.com/livingdocumentation)

---

## Vidéos

- [Domain-Driven Design pour de vrai (Cyrille Martraire)](https://www.canal-u.tv/chaines/cemu/printemps-agile-2017/06-atelier-2-domain-driven-design-pour-de-vrai-pa2017)
- [Aggregates, Entities & Value Objects (Amichai Mantinband)](https://www.youtube.com/watch?v=UEtmOW8uZZY)
- [Clean Architecture vs Domain-Driven Design (DDD) - Understand the Difference](https://www.youtube.com/watch?v=eUW2CYAT1Nk)
- [Playlist: REST API following CLEAN ARCHITECTURE (Youtube)](https://www.youtube.com/playlist?list=PLzYkqgWkHPKBcDIP5gzLfASkQyTdy0t4k)
- [DDD en DotNet (linkedin learning)](https://www.linkedin.com/learning/expert-domain-driven-design-ddd-implementation-in-dot-net)
- [Model Mitosis : ne plus se tromper entre les microservices et le monolithe (Julien Topcu)](https://julientopcu.com/talks/model-mitosis)
- [Le pattern Hive : une stratégie de modularisation pour votre monolithe modulaire ou vos microservice (Julien Topcu)](https://julientopcu.com/talks/hive)
