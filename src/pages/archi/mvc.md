---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CourseLayout.astro'
title: Le pattern MVC
tags:
- architecture
- mvc
---

## Modèle/Vue/Contrôleur (`MVC`)

Design pattern populaire dans les applications web, permettant :

- De séparer la présentation des données de leur modélisation et de leur manipulation.
- La mise à jour de la couche de représentation lorsque les données changent.

---

## Composants 

MVC est composé de 3 modules :

- Modèle : contient les données ainsi que de la logique en rapport avec les données (validation, ...)
- Vue : partie visible d'une interface graphique. Une vue contient des éléments visuels ainsi que la logique nécessaire pour afficher les données provenant du modèle
- Contrôleur : module qui traite les actions de l'utilisateur, modifie les données du modèle et de la vue.

---

```mermaid
---
title: Le pattern MVC.
---
flowchart LR
    %% Définition des composants
    subgraph Modele
        model["Modèle<br/>ex: Mettre à jour l'application<br/>pour représenter l'ajout d'un élément<br/><i>Définit les structures de données</i>"]
    end

    subgraph Vue
        view["Vue<br/>ex: L'utilisateur clique sur 'Ajouter au panier'<br/><i>Définit l'affichage (UI)</i>"]
    end

    subgraph Controleur
        controller["Contrôleur<br/>ex: Reçoit une mise à jour de la vue<br/>et notifie le modèle d'un 'ajout d'élément'"]
    end

    %% Relations
    model -- "Met à jour" --> view
    view -- "Notifie des interactions utilisateur" --> controller
    controller -- "Peut mettre à jour directement" --> view
    controller -- "Manipule" --> model
```

---

> Architecture of an application is all about its intent. _(Robert Martin)_

---

**MVC N'EST PAS UNE ARCHITECTURE**

- MVC est un mécanisme de livraison de données (par exemple, par le Web) : l'architecture et la logique métier de l'application sont décorrélées de ce pattern
- Les exemples (nombreux) d'application MVC avec persistance directe de la couche _Model_ en base de données sans logique métier sont des anti-patterns !!!

---

```mermaid
---
title: Anti-pattern MVC
---
flowchart LR
    user(["Utilisateur"])
    model[["Modèle<br/>(Base de données)"]]
    view["Vue<br/>(HTML)"]
    controller["Contrôleur"]

    user --> |Affiche la page dans son navigateur| controller
    view --> |Retourne la page HTML demandée| user
    controller --> view
    controller <--> model
```

---

![Schema de requête Spring MVC](https://terasolunaorg.github.io/guideline/5.3.0.RELEASE/en/_images/RequestLifecycle.png)

<div class="caption">Une implémentation MVC : Spring MVC Request Lifecycle (source : terasolunaorg.github.io).</div>

---

## Legal

- Spring® is a trademark of Pivotal Software, Inc. in the U.S. and other countries.
- Other names may be trademarks of their respective owners

