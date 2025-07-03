---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
theme: the-unnamed # slidev
title: Clean Architecture
layout: '@layouts/SlideLayout.astro'
tags:
- ddd
- archi
- hexagonal
- clean
---

## Idées

- Règles métier au centre (_Enterprise Business Rules_)
- **Use Cases** autour : uniques composants appelant des règles métier (_Application Business Rules_)
- puis ajout de **Contrôleurs** autour
- puis ajout des **Frameworks** et **Dépendances** autour

> Uncle Bob, 2017

---

![Diagramme de Clean Architecture](https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg)

<div class="caption">Clean Architecture. Credits: Robert C. Martin (Uncle Bob)</div>

---

## Entities

- Cœur de la Clean Architecture
- Domaine métier (voir DDD)
- ✅ objets simples
- ✅ Peuvent être utilisées par toutes les couches de l'application.
- ❌ Pas de dépendance technique (Framework, BDD)
- ❌ Pas de logique spécifique à un cas d'usage

---

## Use Cases

- Encapsulent **toute** la logique métier spécifique à l'application.
- ⬅️ ➡️ Interagit avec les entités
- Détermine comment les données doivent être transmises entre les entités et les couches extérieures.
- ⚠️ 1 Use Case == 1 Processus métier
- Indépendant des détails de l'implémentation externe
  - format de donnée agnostique (transformé par le **Presenter**)

---

## Interface Adapters

- ⬅️ ➡️ Fait le lien entre les `Use Case` et les couches externes
- 🏗️ Adapte les données pour les cas d'usage…
- 🏗️ …puis les présente dans le bon format à l'interface utilisateur ou d'autres API.
- Isolent la logique métier des détails techniques de l’application.
- `controllers`, `presenters`, `gateways`, …

---

## Couche externe : UI, Frameworks, Drivers

- ➡️ Tout ce qui est en contact avec le monde extérieur : interface utilisateur, BDD, serveurs web, …
- ⚠️ Séparé des règles métier
- ⚠️ Sert uniquement à communiquer avec d'autres systèmes (ou l'utilisateur)
- Utiliser les adapteurs pour s'adapter facilement aux changements

---

## Règle de dépendance

> Toute modification dans les couches externes ne doit pas affecter les couches internes

---

## Mise en œuvre - 1/2

- 💡 Analyse et Conception initiales : comprendre le domaine, identifier les entités, les règles métier, les cas d'usage
- ✂️ Définir des frontières entre les couches
- 👥 Créer les Entités
- 🧑‍💼 Développement des Cas d'Usage
- 🏗️ Conception des Adaptateurs

---

## Mise en œuvre - 2/2

- ➡️ Développement et intégration des composants externes : UI, BDD, Service Web, …
- 🧪 Tests Rigoureux :
  - la logique métier fonctionne comme prévu ?
  - les couches externes interagissent correctement avec les cas d'usage ?
- 🔄 Révision et Refactorisation

---
layout: section
---

# Liens

- [Uncle Bob : clean architecture (2012-08-13)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Uncle Bob : clean architecture (2016-01-04)](https://blog.cleancoder.com/uncle-bob/2016/01/04/ALittleArchitecture.html)
- [Robert C Martin - Clean Architecture and Design (Youtube)](https://www.youtube.com/watch?v=Nsjsiz2A9mg)
- [Clean architecture - summary](https://gist.github.com/ygrenzinger/14812a56b9221c9feca0b3621518635b)
- [Daniel Oliveira : How to write robust apps every time, using "The Clean Architecture"](https://www.freecodecamp.org/news/how-to-write-robust-apps-consistently-with-the-clean-architecture-9bdca93e17b)
- [Clean Architecture et Laravel](https://laravel-france.com/posts/clean-architecture-laravel)

