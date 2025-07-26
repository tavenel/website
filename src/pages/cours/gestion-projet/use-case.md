---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Diagrammes de Cas d'Utilisation et de Séquence
tags:
- projet
- uml
---

## Diagrammes de Cas d'Utilisation (Use Case)

- Représentation graphique des interactions entre les acteurs et le système.
- Capture les exigences fonctionnelles d'un système.
- Représente les cas d'utilisation principaux et les acteurs qui interagissent avec le système.

---

### Avantages

- Aide à comprendre le comportement attendu du système.
- Permet d'identifier les rôles et les responsabilités dans un système.
- Facilite la communication entre les développeurs et les parties prenantes.

---

### Composants

1. **Acteurs** : entités externes qui interagissent avec le système.
2. **Cas d'Utilisation** : actions ou scénarios que le système peut effectuer pour les acteurs.
3. **Relations** :
   - **Association** : lien entre un acteur et un cas d'utilisation.
   - **Héritage** : un acteur ou un cas d'utilisation peut hériter des caractéristiques d'un autre.
   - **Extend** : un cas d'utilisation optionnel qui étend le comportement d'un autre cas d'utilisation.
   - **Include** : un cas d'utilisation inclut systématiquement un autre cas d'utilisation.

---

### Exemple de Diagramme de Cas d'Utilisation

Système de gestion de bibliothèque :

```plantuml
@startuml

actor "Utilisateur" as user
actor "Bibliothécaire" as librarian

user -> (Rechercher un livre)
(Rechercher un livre) -> (Emprunter un livre)
user -> (Retourner un livre)
librarian -> (Gérer les emprunts)
librarian -> (Ajouter un nouveau livre)
librarian -> (Supprimer un livre)
user --> (S'inscrire à la bibliothèque)

@enduml
```

---

## Diagrammes de Séquence

---

- Représentation graphique des interactions entre les objets dans un système.
- Met l'accent sur l'ordre des messages échangés.
- Utilisé pour :
  - Visualiser des scénarios.
  - Clarifier le comportement d'un système.
  - Préparer la conception du code.

---

### Élément de Base

- **Lifeline (ligne de vie)** : représentation d'un objet ou d'une classe.
- **Message** : communication entre les objets.
  - **Synchronous (synchronisé)** : l'émetteur attend une réponse.
  - **Asynchronous (asynchronisé)** : l'émetteur continue sans attendre.
- **Activation Bar (barre d'activation)** : indique le temps pendant lequel un objet est actif.

---

### Exemple

```plantuml
@startuml
!theme sketchy-outline

actor Utilisateur
participant "Système" as Sys
participant "Base de données" as DB

Utilisateur -> Sys : Se connecter
activate Sys

Sys -> DB : Vérifier les identifiants
activate DB
DB --> Sys : Résultat de la vérification
deactivate DB

alt Authentification réussie
  Sys -> Utilisateur : Afficher page d'accueil
else Authentification échouée
  Sys -> Utilisateur : Afficher erreur
end

deactivate Sys
@enduml
```

---

### Avantages

- Décris le flux d'interactions d'un cas d'utilisation.
- Clarifie les dépendances entre les composants.

---

### Limitations

- Complexe pour de grands systèmes.
- Pas de détails structurels du système.

---

