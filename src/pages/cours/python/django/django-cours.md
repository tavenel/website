---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Le framework Django
tags:
- python
- web
- django
---

![bg left:40% 80%](https://www.djangoproject.com/m/img/logos/django-logo-positive.svg)

# **Django**

_Tom Avenel_

<https://www.avenel.pro/>

---

# Présentation de Django

Framework Python gratuit et open-source de haut niveau pour développer une application Web

---

## Complet

- Framework pour application Web complète : backend, frontend, persistance, sécurité, administration, ...
- écosystème complet : documentation, tests, ...

---

## Polyvalent

- Développement possible de tout type de site Web ;
- Nombreuses infrastructures client ;
- Quasiment tout type de format d'échange de données : `Json`, `XML`, ... ;
- Extensible.

---

## ORM puissant

- Abstraction de la couche de persistance ;
- Nombreuses bases de données : nativement `PostgreSQL`, `MySQL`, `Oracle`, `SQLite` ;
- Librairies externes pour la plupart des BD `SQL` et `NoSQL`.

---

## Sécurisé

- "Security by design" ;
- Gestion sécurisée des utilisateurs ;
- Protection par défaut contre de nombreuses vulnérabilités : injections `SQL`, `XSS`, ...

---

## Scalable

- Architecture composite "shared-nothing" : composants indépendants et remplaçables
- Scalabilité à tous les niveaux : serveurs cache, bases de données, serveurs d'application
- Utilisé par des sites à très forte fréquentation : `Instagram`, ...

---

## Maintenable

- Design favorisant un code simple et réutilisable : template, … 
- DRY : interfaces d'administration, …
- Développement en _applications_ réutilisables
- MVC

---

## Portable

- Python : presque toutes plateformes
- Disponible sur beaucoup d'hébergeurs PaaS

---

# Installation

- Nombreuses distributions : package de distribution, `virtualenv`, ...
- Le plus simple (dernière version officielle) :
  ```bash
  python -m pip install django
  ```
- Framework Python => attention à avoir une version récente et correctement installée de Python sur votre système !
- Vérifier l'installation : `python -m django --version`

---

# Environnement de développement

- Scripts Python pour créer et travailler avec des projets `Django` :
  + `django-admin` pour créer un nouveau projet
  + fichier `./manage.py` pour gérer le projet courant
  + Inclut un serveur web de développement
- Plugin IDE

---

# Projet vs applications

- **Projet** : capsule vide gérant le site en entier
- **Application** : élément réutilisable du site (login, recherche, ...)

---

```plantuml
@startuml

caption
= Un projet est une aggrégation d'applications
endcaption

left to right direction

class Projet {
  nom
  configuration
  contrôleur frontal
}
class Application {
  nom
  configuration
  contrôleur frontal
}
Model : nom
Vue : nom
Template : fichier
class Champ {
  nom
  type
}

Projet o-- "*" Application
Application *-- "*" Model
Application *-- "*" Vue
Application *-- "*" Template
Model *-- "*" Champ
@enduml
```

---

# Cheatsheet

- Créer un nouveau projet : `django-admin startproject <mon_projet>`
- Démarrer le serveur Web : `python manage.py runserver`
- Réaliser une migration : `python manage.py makemigrations && python manage.py migrate`

---

<!-- class: liens -->

# Liens

- [Tutoriel première application Django][tuto-django]
- [Génération de diagrammes de classe UML depuis un projet Django][uml]

[tuto-django]: https://docs.djangoproject.com/en/4.2/intro/tutorial01/
[uml]: https://gist.github.com/perrygeo/5380196

---

<!-- class: legal -->

# Legal

- Django and the Django logo are registered trademarks of the Django Software Foundation.
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
