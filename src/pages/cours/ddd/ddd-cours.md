---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Domain-Driven Design
tags:
- ddd
- archi
- hexagonal
- clean
---

## Chapitres

---
layout: center
---

# Problèmes communs aux projets informatiques

---
layout: section
---

# MVC comme architecture

---

# MVC comme architecture

```plantuml
@startuml

folder my_app {
  component View
  component Controller
  database Model
  
  View --> Controller
  Controller --> Model
}

@enduml
```

_Quel est le **but** de cette application ?_ 🤔

---

```plantuml
@startuml
folder customer
folder helpbase
folder message
folder staffer
folder ticket
@enduml
```

_Quel est le **but** de cette application django ?_ 💡

---
layout: section
---

# Application _CRUD_

---

# Application _CRUD_

1. Entité (`getter`/`setter`) + BDD auto-générée
2. ??? 🙈
3. API `REST` : _CRUD_ sur l'entité

_Quelle est la **logique métier** derrière ces entités ?_

---
layout: section
---

# Modèle anémique

---

# Modèle anémique

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
layout: section
---

# Domaine incohérent

---

# Domaine incohérent

```plantuml
@startuml

class UserAccount {
  + address: String
}

@enduml
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

![Ce que le client voulait vraiment](@assets/gestion-projet/balancoire.jpg)

<div class="caption">Ce que le client voulait vraiment</div>

---

# Un bon design ?

- Des cas d'utilisation **clairs** 🧑‍💼
- Facile à **maintenir** 🧰
- Facile à **tester** 🧪
- **Cohérent** et **facile** à comprendre 💭
- **Découplé** ⬅️ ➡️
- Résilient au **changement de technologie**

---

# Un bon design ! 🤓

```java
private static final boolean WILL_IT_RAIN_IN_LONDON = true;
```

- Le métier s'apprend en **lisant le code !**

---
layout: center 
---

# Le Domain-Driven Design (DDD)

---

## Objectif 🎯

> Le Domain-Driven Design, c'est avant tout la compréhension du métier par l'ensemble de l’équipe.

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

# Principes

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
      font-family: Arial, sans-serif;
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
layout: center
---

# Stratégie vs tactique

---

# Stratégie vs tactique

- ****Stratégie**** : **définition** de l'objectif
- **Tactique** : comment _atteindre_ l'objectif (organisation du code)
- `DDD` est avant tout **stratégique**

---

# Méthodologie

- 🎯 Commencer par un **design stratégique**
- 💬 Définir le **langage ubiquitaire**
- ✂️ Découper le métier en **Bounded Context**
- 🔃 **Itérer**

---
layout: center
---

# Domaine, Modèle, Bounded Context, Language ubiquitaire

---
layout: section
---

# Domaine 🏢

---

# Domaine 🏢

- _Domaine_ : ce que fait une organisation (et comment)
  - un **langage dédié**
  - des **sous-domaines** : l'espace des problèmes à résoudre

> La sphère d'un métier ou activité pour lequel on développe l'application. (wikipedia)

---
layout: section
---

# Modèle

---

# Modèle

- _Modèle_ : une **abstraction** qui représente une **partie d'un domaine**.

---
layout: section
---

# Bounded Context 🧑‍💼

---

# Bounded Context 🧑‍💼

- _Bounded Context_ : limite de **validité** d'un modèle **(frontière linguistique)**
- Concept **métier** précis qui répond à une **problématique**.

---
layout: section
---

# Architecture 🏗️

---

# Architecture 🏗️

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

```plantuml
@startditaa
+----------------------------+
|       Domaine              |
| +------------------------+ |
| | Bounded Context        | |
| |  +==================+  | |
| |  | Contexte "Vente" |  | |
| |  |                  |  | |
| |  |  ^               |  | |
| |  +==|===============+  | |
| |     |     ^            | |
| +-----|-----|------------+ |
+-------|-----|--------------+
        |     |
        |     |
        |     +--- Bounded Context
        |
        +--- Langage Ubiquitaie

= Domaine, Bounded context, langage ubiquitaire.

@endditaa
```

:::tip
Un _Domaine_ peut englober plusieurs _Bounded Context_.
:::

---
layout: section
---
# D'un langage ubiquitaire au modèle

---

# D'un langage ubiquitaire… 💬

- Pas uniquement un glossaire, des _phrases entières (simples)_
- Provient du **métier**
  - Éliminer les **synonymes**
  - Coder dans la **langue du métier**…
  - …ou s'accorder sur les **traductions** !

---
layout: quote
---

> Si vous ne pouvez expliquer un concept à un enfant de six ans, c'est que vous ne le comprenez pas complètement. (Albert Einstein)

---

# …Au modèle 🗂️

- **Le langage est le modèle**
  - langage => modèle (puis => langage)
- Pas de **duplication du modèle** 🚫
- Privilégier plusieurs éléments **simples** pour faire des modèles plus complexes 🖇️
- Pas de **technique** dans le modèle
- Utiliser les termes **métiers** dans le code 🧑‍💼

---

![Un exemple de fonction mal nommée](https://programmerhumor.io/wp-content/uploads/2021/05/programmerhumor-io-8fb4c03b81cbbab-758x621.png)

<div class="caption">Un exemple de fonction mal nommée. Source: programmerhumor.io</div>

---
layout: center
---

# Définir le langage 💬

---

# Objectifs 🎯

1. Clarifier le **besoin métier** entre les différents experts du domaine
2. **Simplifier** les définitions

---
layout: section
---

# Event storming

---

# L'atelier d'Event Storming

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

# Brainstorming

1. Trouver les **idées** 💡 (penser _objectifs_ 🎯 )
2. **Regrouper **les idées 🖇️
3. Trouver les **déclencheurs** (_event triggers_) ▶️

[Exemple de brainstorming][brainstorming-example]

---

# Formalisation

1. Identifier les **acteurs** 🙋 et les **prioriser** 🔢
2. Identifier les **cas d'utilisation** 🤹
3. Identifier les **interactions** entre les cas d'utilisation 🤼‍♂️
4. Identifier les **entités**
5. Diagramme de **classes** (ou **code** directement) : décrit le **glossaire** 📒

---

# Diagramme de cas d'utilisation

```plantuml
@startuml

caption
= Exemple : diagramme de cas d'utilisation d'un vidéoclub
endcaption

left to right direction
skinparam actorStyle awesome

actor Adhérent as adherent
actor "Non adhérent" as nadherent
Client <|-- adherent
Client <|-- nadherent

actor "Abonné" as abo
actor "Non abonné" as nabo
adherent <|-- abo
adherent <|-- nabo

nadherent --> (Demande d'adhésion)
adherent --> (Location cassettes)
adherent --> (Retour Cassette)
nabo --> (Demande d'abonnement)

(Demande d'adhésion) --> (Authentification) : <<utilise>>
(Location cassettes) --> (Authentification) : <<utilise>>
(Retour Cassette) --> (Authentification) : <<utilise>>
(Demande d'abonnement) --> (Authentification) : <<utilise>>

@enduml
```

---

# Diagramme de classe

```plantuml
@startuml

caption
= Exemple de diagramme de classes pour le modèle d'une librairie.
endcaption

class Book {
  +title: String
  +author: Author[1]
  +summary: String
  +ISBN: String
  +genre: Genre[1..*]
  +language: Language[1]
}

class Genre {
  +name: String
}

class Language {
  +name: String
}

class BookInstance {
  +uniqueId: String
  +due_back: DateField
  +status: LOAN_STATUS
  +book: Book[1]
  +imprint: String
  +borrower: User[1]
}

class Author {
 +name: String
  +date_of_birth: DateField
  +date_of_death: DateField
  +books: Book[1..*]
}

Book "1..*" -- "1" Author
Book "0..*" -- "1..*" Genre
Book "0..*" -- "1" Language
Book "1" -- "0..*" BookInstance

@enduml
```

---
layout: default
---

# Loi de Brandolini

> La quantité d'énergie nécessaire pour réfuter des sottises […] est supérieure d'un ordre de grandeur à celle nécessaire pour les produire.
>
> _Bullshit asymmetry principle, Brandolini_

- Event storming (très) long (~3 jours) 💤
  - à **découper** (meilleure acceptation) 🪚

---
layout: center
---

# Patterns stratégiques

---

# Distillation du Core Domain

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

```plantuml
@startuml
title: Exemple de Domaine

rectangle "Domain" {

  rectangle "Trading Room"
  rectangle "Risk"
  rectangle "Information Technology"
  rectangle "Financial"
  rectangle "Human Ressources"
  rectangle "Account"
}
@enduml
```

```plantuml
@startuml
title: Exemple de Domaine distillé

rectangle "Domain" {

  rectangle "Trading Room" as tr
  rectangle "Risk" as r
  rectangle " " as b {
    rectangle "Human Ressources"
    rectangle "Information Technology"
  }
  rectangle "Financial" as f
  rectangle "Account" as a
}

tr -- r
tr -- f
tr -- b
r -- b
r -- a
a -- b
f -- b

@enduml
```

---

# Découpage

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

```plantuml
@startditaa
+---------------------+   +---------------------+   +---------------------+
| Sous-domaine de     |   | Sous-domaine        |   | Sous-domaine        |
| Support             |   | Générique           |   | Générique           |
+---------------------+   +---------------------+   +---------------------+

+---------------------+   +---------------------+   +---------------------+
| Sous-domaine de     |   | Domaine Principal   |   | Sous-domaine        |
| Support             |   | (Core Domain)       |   | Générique           |
+---------------------+   +---------------------+   +---------------------+
@endditaa
```

---

## Comparaison des domaines

| Type de domaine | Complexité du modèle | Différenciant business |
|-----------------|----------------------|------------------------|
| Core Domain     |   Très complexe      |   Élevé                |
| Support         |    Complexe          |   Moyen                |
| Générique       |    Simple            |   Faible               |

---

```mermaid
flowchart TD
    A["La solution peut-elle être achetée/intégrée?"] -->|Yes| B["Cela mettra-t-il en péril l’entreprise ?"]
    A -->|Non| C["Complexité de la logique métier?"]
    B -->|Oui| D["Domaine Principal"]
    B -->|Non| E["Sous-domaine Générique"]
    C -->|Complexe| D
    C -->|Simple| F["Sous-domaine Support"]
```

---

# Exemple d'un dentiste

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
layout: center
---
# Propagation du domaine

---

# Propagation du domaine

- Quelles relations entre domaines ?
- Comment faire interagir différents domaines ?

---

# Carte de contexte

- Document représentant les **relations** entre Bounded Context
- Diagramme ou document écrit
- Niveau de détail variable

---

```plantuml
@startditaa
                    Domaine
                      |
                      v
+------------------------------------------------------------+
|                                                            |
|    +===================+                +=============+    |
| +->| Customer Context  |----------------| Sales       |<-+ |
| |  |                   |  ContextMap    | Context     |  | |
| |  +===================+                +=============+  | |
| |      Downstream                        Upstream        | |
| |                                                        | |
+-|--------------------------------------------------------|-+
  |                                                        |
Bounded Context                                   Bounded Context
@endditaa
```

---
layout: section
---

# Patterns de collaboration

---

# Shared Kernel (Noyau partagé)

- Relation entre 2+ _Bounded Context_ qui partagent du code, des données, …
- Création d'un **contexte partagé** (en dépendance) :
  - évite la **duplication**
  - **collaboration forte** : doit **notifier** chaque contexte dépendant des changements

---

# Exemple de noyau partagé

- Plateforme de commerce électronique :
  - une boutique en ligne
  - une application mobile
- Mêmes comptes clients, même historique des commandes, …
  - dans un noyau partagé
  - BDD commune

---

```plantuml
@startuml
title: SHARED-KERNEL (LIB)
left to right direction

package "RÉSERVATION" #LightGreen {
	[Réservation] as booking #LightGreen
	rectangle "Classe" as comfort_class #LightPink
	rectangle "Horaires" as schedule #LightPink

	booking --> comfort_class
	booking --> schedule
}

rectangle "SHARED-KERNEL (LIB)" #LightPink {
	rectangle "Classe\n(économique, business, …)" as shared_comfort_class #LightPink
	rectangle "Horaires" as shared_schedule #LightPink

	comfort_class -[dotted]- shared_comfort_class
	schedule -[dotted]- shared_schedule
}

package "RECHERCHE" #LightBlue {
	[Recherche] as search #LightBlue
	rectangle "Classe" as search_comfort_class #LightPink
	rectangle "Horaires" as search_schedule #LightPink

	search_comfort_class <-- search
	search_schedule <-- search
}

shared_comfort_class -[dotted]- search_comfort_class
shared_schedule -[dotted]- search_schedule
@enduml
```

---

# Customer / Supplier (Client / Fournisseur)

- Relation : un _Bounded Context_ **fournit un service** (ou des données) à un autre.
- **Collaboration forte**
- Aussi appelé : `Downstream` (Client) / `Upstream` (Supplier)

---

# Exemple de Customer / Supplier

- Processus de gestion des catalogues produits :
  - _Client_ : définition des exigences et des règles commerciales
  - _Fournisseur_ : mise en œuvre de l'infrastructure technique

---

```plantuml
@startuml
title: relation Client/Fournisseur
left to right direction

package "Facturation (Supplier)" {
  class "Client" as client1 {
    +addresseDeFacturation
    +récupérerDevis()
  }

}

package "Marketing (Customer)" {
  class "Client" as client2 {
    +addresseDeContact
    +listerProduitsRécents()
  } 

}

client2 -- client1
@enduml
```

---

# Conformiste

- Le client **adhère** au modèle (et conventions, règles, …) de l'équipe fournisseur
- _C'est au client de s'adapter_

---

# Exemple de Conformiste

- Équipe chargée de gérer l'inventaire des produits dans un entrepôt.
  - même modèle que dans le contexte responsable de la gestion des commandes, des clients et des produits.
- Module de _Recherche_ conforme à un module de _Réservation_ .

---

```plantuml
@startuml
title: CONFORMISTE (COMPOSANTS)
left to right direction

package "RÉSERVATION" #LightGreen {
    [Sélection] as selection #LightBlue
    () "getSelection() : SPI" as getter #LightGreen
}

package "RECHERCHE" #LightBlue {
    [Sélection] as selection2 #LightBlue
    () "getSelection() : API" as getter2 #LightBlue
}

getter2 ..> getter
@enduml
```

---

```plantuml
@startuml
title: CONFORMISTE (LIB)
left to right direction

package "RÉSERVATION" #LightGreen {
	[Prix] as price #LightGreen
	[Discount] as discount #LightGreen
	rectangle "Quantité" as amount #LightPink
	rectangle "Devise" as currency #LightPink

	price --> amount
	price --> currency
	discount --> amount
	discount --> currency
}

rectangle "MONNAIE (LIB)" #LightPink {
	rectangle "Quantité" as amount2 #LightPink
	rectangle "Devise" as currency2 #LightPink
}

amount -[dotted]- amount2
currency -[dotted]- currency2
@enduml

```

---

# Open Host Services (Services Hôtes)

- Rend disponible des systèmes / services **communs** à différents _Bounded Context_
  - _RESTful API_, …
- Définit un **modèle commun d'intégration**

---

# Exemple de pattern Open Host Service

- _Open Host Service_ de paiement à distance (possède sa propre logique)
- À intégrer dans différents contextes de l'application

---

```plantuml
@startuml
title: OPEN HOST
left to right direction

package "RÉSERVATION" #LightGreen {
  package "DOMAIN" as domain1 {
    [Train] as train #LightGreen
    () "getTrainsToBook()\n(SPI)" as getTrainsToBook #LightGreen
  }
}

package "RECHERCHE" #LightBlue {
  package "DOMAIN" as domain2 {
    [Selection] as domain_selection #LightBlue
    () "getSelection()\n(API)" as getSelection #LightBlue
  }

  package "INFRASTRUCTURE" #LightGreen {
    [Train] as inproc_train #LightGreen
    [Sélection] as selection #LightBlue
    selection --> inproc_train : OpenHost
    () "getTrainsToBook()\n(implémentation)" as getTrainsToBookImpl #LightGreen
  }
}

getSelection --> getTrainsToBookImpl
getTrainsToBookImpl --> getTrainsToBook
@enduml
```

---

# Published Language (Langage publié)

- Version formelle des service hôtes : **publication technique du modèle commun**
  - `JSON`, `XML`, …

---

# Couche Anticorruption (ACL)

- **Protège** un _Bounded Context_ des complexités et incohérences d'un autre modèle
- **Traducteur** et **validateur** entre deux modèles
- **Inverse** de l'_Open Host_

---

# Exemple de pattern ACL

- Système e-commerce s'intégrant à un ancien système de gestion des stocks (ancien modèle de données)
- L'_ACL_ traduit les concepts, données et messages entre les 2 systèmes

---

```plantuml
@startuml
title: COUCHE ANTICORRUPTION
left to right direction

package "RÉSERVATION" #LightGreen {
  package "DOMAIN" as domain1 {
    [Train] as train #LightGreen
    () "getTrainsToBook()\n(SPI)" as getTrainsToBook #LightGreen
  }

  package "INFRASTRUCTURE" {
    [Train] as inproc_train #LightGreen
    [Sélection] as selection #LightBlue
    selection --> inproc_train : ACL
    () "getTrainsToBook()\n(implémentation)" as getTrainsToBookImpl #LightGreen
  }
}

package "RECHERCHE" #LightBlue {
  package "DOMAIN" as domain2 {
    [Selection] as domain_selection #LightBlue
    () "getSelection()\n(API)" as getSelection #LightBlue
  }

}

getSelection --> getTrainsToBookImpl
getTrainsToBookImpl --> getTrainsToBook
@enduml
```

---

# Separate Ways (Chemins Séparés)

- Contextes très **indépendants** les uns des autres (_y compris technologiquement_)
- Évoluent **séparément**
- Idée de **modularité**

---

# Exemple de Chemins Séparés

1. Application principale de e-commerce
2. Système de gestion des stocks indépendant (propre domaine et logique métier)
  - Communique avec l'application via une file de messages bien définie
  - Développé et maintenu par une équipe distincte

---

```plantuml
@startuml
title: Separate Ways
left to right direction

package "Facturation" {
  class "ClientPourFacturation" as client1 {
    +addresseDeFacturation
    +récupérerDevis()
  }

}

package "Marketing" {
  class "ClientPourMarketing" as client2 {
    +addresseDeContact
    +listerProduitsRécents()
  } 

}

client2 .. client1  #red : "<color:red>Aucun lien (duplication)</color>"
@enduml
```

---
layout: section
---

# Context Map

---

# Context Map

- **Carte de contexte** : formalise les relations entre les bounded context.

---

# Exemple de context map

```plantuml
@startuml
title: Exemple de Context Map d'une compagnie d'assurance

' Contexts
package "Customer Self-Service Context" as cssc {
  rectangle D as cssc_d
}

package "Printing Context" as pc {
  rectangle "OHS ou PL\nU" as pc_u
}

package "Customer Management Context" as cmc {
  rectangle U as cmc_u
  rectangle "ACL\nD" as cmc_d
  rectangle "OHS ou PL\nU" as cmc_u2
}

package "Debt Collection Context" as dcc {
  rectangle "ACL\nD" as dcc_d
}

rectangle "Risk Management Context" as rmc

package "Policy Management Context" as pmc {
  rectangle "ACL\nD" as pmc_d
  rectangle "CONFORMIST\nD" as pmc_d2
}

' Relationships
cmc_u -- cssc_d : "Customer/Supplier"
cmc_u2 -- pmc_d2

pc_u -- cmc_d
pc_u -- pmc_d
pc_u -- dcc_d

pmc -- dcc : "Shared Kernel"
pmc -- rmc : "Partnership"
@enduml
```

---
layout: section
---

# Relations entre équipes

---

![Photo de l'intérieur d'un PC portable](@assets/sysadmin/EBMotherboard.jpg)

<div class="caption">Photo de l'intérieur d'un PC portable. By <a href="https://en.wikipedia.org/wiki/User:Ravenperch" class="extiw" title="wikipedia:User:Ravenperch">Ravenperch</a> at <a href="https://en.wikipedia.org/wiki/" class="extiw" title="wikipedia:">English Wikipedia</a> - <span class="int-own-work" lang="en">Own work</span> (<span lang="en" dir="ltr">Original text: Self created</span>), <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=18540450">Link</a></div>

À votre avis, quelles sont les différentes équipes à travailler sur la réalisation de cet ordinateur ?

---

# Loi de Conway

> Les organisations produisent des systèmes qui reflètent leur structure de communication

- Exemple :
  - _facturation_
  - _gestion des stocks_
  - _gestion des comptes_

---

# Team topologies

- idée : refléter le découpage en composants dans le découpage des équipes
- **Team Topologies** : pattern d'organisation complémentaire au DDD
  - inverse de la loi de Conway (adapter l'organisation aux modules et pas l'inverse)

---

# Dépendance mutuelle

- Dépendance mutuelle (Shared Kernel)
- Relation **succès/échec partagée**
  - besoin de **collaboration forte**
  - relation de **partenariat**

---

# Dépendance Upstream / Downstream 

- **Upstream impacte le succès Downstream**
- Downstream n'impacte pas le succès Upstream
  - soit : collaboration par **requêtes** (envie du Customer à remonter au Supplier), pas par ~~exigence (besoin)~~
  - soit : API publique (Open Host Service) indépendant du consommateur (le Customer doit s'adapter au Supplier)

---

```plantuml
@startmindmap
* Context Map

  **_ Superposition de contextes coopérant
    *** Shared Kernel

  **_ Crée un lien de coopération
    *** Customer/Supplier Teams

  **_ Crée un lien unidirectionnel
    *** Conformist

  **_ Supporte différents clients
    *** Open Host Service
      ****_ Version formelle
        ***** Published Language

  **_ Libère les contraintes entre équipes
    *** Separate Ways

  **_ Traduis et isole unilatéralement
    *** Anticorruption Layer

left side

  **_ Évaluation et examen des relations
    *** Bounded Context

      ****_ nommage
        ***** Ubiquitous Language

      ****_ garde le modèle unifié
        ***** Continuous Integration

@endmindmap
```

<div class="caption">Résumé des patterns stratégiques.</div>

---

# Objectifs

- Limiter la complexité du système à la charge cognitive de l'équipe
- Collaboration a minima (complexe)
  - sinon : envisager la creation d'un nouveau composant au milieu pour limiter les impacts

---
layout: center
---

# Patterns tactiques

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

```plantuml
@startmindmap
* Domain-Driven Design
  **[#lightgreen] expression du modèle
    ***[#lightgreen] Services
    ***[#lightgreen] Value Objects
    ***[#lightgreen] Entities
      ****[#FFBBCC] Propriété, frontières et intégrité des objets
        *****[#FFBBCC] Aggregates

  **[#lightblue] Accès aux données, ignore la persistance
    ***[#lightblue] Repositories

  **[#Orange] Création des objets
    ***[#Orange] Factories
@endmindmap
```

<div class="caption">Patterns tactiques de base.</div>

---

# Intégration continue

- 🔃 Le DDD est **itératif** (=> CI)
- 🤔 **Repenser** régulièrement les `Bounded Context` et **changer le type de propagation** au besoin

---

# XP, Agilité, BDD

- `DDD` s'associe particulièrement bien avec les méthodes agiles (`XP`, …)
- Le `BDD` (Behavior-Driven Development) permet de faire le lien par le langage des spécifications (**par l'exemple**) au code

---
layout: section
---

# Architecture

---

# Patterns spécifiques d'architecture

- DDD ne définit pas d'architecture spécifique
- Candidats intéressants :
  - _Architecture Hexagonale_
  - _Clean Architecture_
  - _[L'architecture explicite][archi-explicite] combine le tout_

---

# Architecture à Grande Échelle

DDD utilise les concepts d'**architecture à grande échelle** pour organiser le système au niveau des composants ou des couches. Cette organisation guide les développeurs sur la l'endroit où trouver ou ajouter une fonctionnalité dans le code.

- Architectures classiques : basées sur des considérations techniques
- Archicture à grande échelle : basée sur des concepts liés au domaine

---

1. **Ordre évolutif**  
  - Laisser la structure évoluer avec le temps.
2. **Métaphore système**  
  - Rechercher une métaphore globale pour le système.
3. **Couches de responsabilité**  
  - Organiser le modèle de domaine en plusieurs couches.
4. **Niveau de connaissance**  
  - Permettre la configuration des opérations principales à partir d’un niveau de connaissance.
5. **Cadre de composants plug-and-play**  
  - Abstraction du cœur avec une infrastructure de plugins.

---

# Design Souple (Supple Design)

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

5. **Classes autonomes**  
   - Réduire les dépendances pour alléger la charge mentale.
6. **Opérations dans des ensembles clos**  
   - Les opérations doivent idéalement retourner le même type que leurs arguments.
7. **Design déclaratif**  
   - Utiliser un style de programmation déclaratif si possible.

---
layout: center
---

# Résumé

---

# Résumé

![Résumé du Domain Driven Design](@assets/ddd/DomainDrivenDesignReference.png)

<div class="caption">Résumé du Domain Driven Design. CC By: Eric Evans. https://www.domainlanguage.com/ddd/reference/</div>

---
layout: section
---

# Conseils et points de vigilance

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
layout: two-cols
---

<!-- class: liens -->
# Liens

- [Articles sur le DDD (opus.ch)](https://opus.ch/en/category/ddd-en/)
- [Présentation du DDD (dieuxducode.com)](https://lesdieuxducode.com/blog/2019/7/introduction-au-domain-driven-design)
- [Résumé du DDD (blog.scottlogic.com)](https://blog.scottlogic.com/2018/03/28/domain-driven-design.html)
- [Alex Soyes - DDD](https://alexsoyes.com/ddd-domain-driven-design/)
- [Blog Opus Software - articles DDD](https://opus.ch/en/blog/)
- [DDD 101 — The 5-Minute Tour (medium.com)](https://medium.com/the-coding-matrix/ddd-101-the-5-minute-tour-7a3037cf53b8)
- [DDD en 5 minutes (cdiese.fr)](https://cdiese.fr/domain-driven-design-en-5-min/)
- [DDD vs Clean architecture en images](https://khalilstemmler.com/articles/software-design-architecture/domain-driven-design-vs-clean-architecture/)
- [Exemple de brainstorming (event storming)][brainstorming-example]

- [Stratégies d'organisation du code (medium.com)](https://medium.com/@msandin/strategies-for-organizing-code-2c9d690b6f33)
- [Martin Fowler : domain data layering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html)
- [De CRUD à DDD - Comment Meetic a sauvé son legacy (slides)](https://speakerdeck.com/jmlamodiere/de-crud-a-ddd-comment-meetic-a-sauve-son-legacy)
- [Architecture explicite][archi-explicite]
- [Application de poésie](https://github.com/tpierrain/hexagonalThis)
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

# Livres

- _Domain-Driven Design, Tackling Complexity in the Heart of Software, Eric Evans, 2003._
- _Implementing Domain-Driven Design, Vaughn Vernon, 2013._
- [Living Documentation (Cyrille Martaire)](https://leanpub.com/livingdocumentation)

---

# Vidéos

- [Domain-Driven Design pour de vrai (Cyrille Martraire)](https://www.canal-u.tv/chaines/cemu/printemps-agile-2017/06-atelier-2-domain-driven-design-pour-de-vrai-pa2017)
- [Aggregates, Entities & Value Objects (Amichai Mantinband)](https://www.youtube.com/watch?v=UEtmOW8uZZY)
- [Clean Architecture vs Domain-Driven Design (DDD) - Understand the Difference](https://www.youtube.com/watch?v=eUW2CYAT1Nk)
- [Playlist: REST API following CLEAN ARCHITECTURE (Youtube)](https://www.youtube.com/playlist?list=PLzYkqgWkHPKBcDIP5gzLfASkQyTdy0t4k)
- [DDD en DotNet (linkedin learning)](https://www.linkedin.com/learning/expert-domain-driven-design-ddd-implementation-in-dot-net)
- [Model Mitosis : ne plus se tromper entre les microservices et le monolithe (Julien Topcu)](https://julientopcu.com/talks/model-mitosis)
- [Le pattern Hive : une stratégie de modularisation pour votre monolithe modulaire ou vos microservice (Julien Topcu)](https://julientopcu.com/talks/hive)

