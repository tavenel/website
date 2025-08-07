---
title: De la modélisation UML® au développement
date: 2023 / 2024
---

## Présentation de l'étude de cas

Cette étude de cas porte sur la réalisation d'une application de gestion d'une bibliothèque. L'étude de cas est inspirée de l'exemple suivant : <https://www.uml-diagrams.org/library-domain-uml-class-diagram-example.html>.

## Le projet 

Le projet a été spécifié grâce à un ensemble de diagrammes de classes et de composants.

- Il s'agit d'une application Web client-serveur.
- La persistance des données n'est pas une priorité - on pourra utiliser une méthode non optimisée, y compris un composant de persistance en mémoire vive.
- Le seul client attendu dans cette version est un client Web.

## Diagramme de cas d'utilisation

```mermaid
---
title: Diagramme de cas d'utilisation
---
flowchart LR
    Patron["🧑 Patron"]
    Librarian["🧑 Librarian"]

    Patron --> Login
    Patron --> Search
    Librarian --> Login
    Librarian --> Search
    Librarian --> Manage_subscriptions

```

L'application décrit trois cas d'utilisation :

- La connexion d'un utilisateur.
- Une interface de recherche pour l'usager et le libraire.
- Une interface de gestion pour le libraire.

La vue de connexion est la première vue commune.

Les deux interfaces correspondent à deux vues différentes dans l'application Web.

## Diagrammes de composants

```mermaid
---
title: Diagramme de composants
---

graph TD

subgraph Persistence
  PersistenceDB[Database: Persistence]
end

subgraph Backend
  subgraph Web_API
    Authentication[Component: Authentication]
    Library[Component: Library]
  end
end

subgraph Frontend
  Login[Component: Login]
  Search[Component: Search]
  Manage[Component: Manage]
end

Login -->|Web Login| Authentication
Search -->|Search inventory| Library
Manage -->|Add/Update/Delete inventory| Library
Library -->|Load/Persist| PersistenceDB
Authentication -->|Load/Persist| PersistenceDB
```

L'application est composée de trois composants principaux :

- Un composant de persistance (base de données ou autre).
- Un backend exposant une Web API.
- Un frontend déployant le client Web dans le navigateur et utilisant l'API du Backend.

## Diagrammes de classes du Domain Model de la bibliothèque

```mermaid
---
title: Diagramme de classe pour le domaine d'une librairie
---
classDiagram
    class Library {
      String name
      Address address
    }

    class Catalog {
    }

    class Search {
      <<interface>>
    }

    class Manage {
      <<interface>>
    }

    class Librarian {
      FullName name
      Address address
      String position
    }

    class Patron {
      FullName name
      Address address
    }

    class Account {
        <<entity>>
        int number : id
        List~History~ history
        Date opened
        AccountState state
    }

    class Book {
        String ISBN : id 0..1
        String name
        String subject
        String overview
        String publisher
        Date publicationDate
        String lang
    }

    class BookItem {
        <<entity>>
        String barcode : id 0..1
        RFID tag : id 0..1
        String ISBN : 0..1
        String subject
        String title : redefines name
        Boolean isReferenceOnly = false
        Language lang : redefines lang
        Integer numberOfPages
        Format format
        Date borrowed
        Integer loanPeriod : readOnly
        Date dueDate : readOnly
        Boolean isOverdue = false        
    }

    class Author {
      String name : id
      String biography
      Date birthDate
    }

    class Language {
        <<enum>>
        English
        French
        German
        Spanish
        Italian
    }

    class AccountState {
        <<enum>>
        Active
        Frozen
        Closed
    }

    class Format {
        <<enum>>
        Paperback
        Hardcover
        Audiobook
        Audio_CD
        MP3_CD
        PDF
    }

    class Address {
      <<dataType>>
    }

    class FullName {
      <<dataType>>
    }   

    %% Associations
    Search <|.. Catalog
    Manage <|.. Catalog
    
    Catalog "1" -- "*" BookItem : records
    Book <|-- BookItem
    Book "1..*" -- "1..*" Author : wrote

    Librarian ..> Manage : uses
    Librarian ..> Search : uses
    Patron ..> Search : uses

    Patron o-- "account" Account
    Library o-- "*" BookItem
    Library "1" o-- "* accounts" Account
    Library *-- Catalog

    BookItem "0..3" -- Account : reserved
    BookItem "0..12" -- Account : borrowed
```

<div class="caption">Exemple de diagramme de classe pour le domaine d'une librairie. <a href="https://www.uml-diagrams.org/library-domain-uml-class-diagram-example.html">Source et crédit</a></div>

Ce diagramme représente le domain model de la bibliothèque, c'est-à-dire les classes comportant et interagissant avec la donnée de l'application dans le composant `Backend`.

Les interfaces `search` et `manage` sont les deux points d'entrée utilisateur tels que décrits dans le diagramme de cas d'utilisation.

Précision sur le type `History` : ce type est décrit par une classe `History` comportant l'historique des opérations `borrowed` et `reserved`. Étant un attribut de l'entité `Account`, cet attribut doit être persisté, cependant il n'est pas demandé d'exposer cet attribut aux acteurs de l'application via l'interface graphique.

Les autres classes à ajouter sont à la discrétion de l'équipe de développement.

# Travail à réaliser

Ce projet sera réalisé en groupes de 3 apprenants.

En utilisant la technologie de votre choix, développer **et tester** une application dans une architecture client-serveur implémentant les diagrammes de classe et de composants fournis. On veillera à bien respecter le formalisme UML® mais on pourra bien sûr ajouter d'autres classes et composants mineurs si nécessaire.

# Rendus attendus

Il est attendu un fichier de rapport contenant :

- Les noms et prénoms des membres du groupe.
- Une description des technologies utilisées.
- Une documentation technique afin d'installer et de déployer localement l'application.
- Un lien vers le ou les dépôts de code.

## Références

Les liens suivants peuvent servir de rappels de cours concernant la modélisation UML® :

- [Référence officielle de la norme UML](https://www.omg.org/spec/UML)
- [Cours complet et libre sur UML 2](https://laurent-audibert.developpez.com/Cours-UML/)
- [Article Wikipédia - résumé des diagrammes UML principaux](https://fr.wikipedia.org/wiki/UML_(informatique))

# Legal

- UML is either a registered trademark or a trademark of Object Management Group, Inc. in the United States and/or other countries.
- [Source et crédit](https://www.uml-diagrams.org/library-domain-uml-class-diagram-example.html) du diagramme de classe UML pour le modèle.

