---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Le pattern MVC
keyworkds:
- architecture
- mvc
---

<!-- _class: titre lead -->

# Pattern MVC : Modèle / Vue / Contrôleur

_Tom Avenel_

<https://www.avenel.pro/>

---

# Modèle/Vue/Contrôleur (`MVC`)

Design pattern populaire dans les applications web, permettant :

- De séparer la présentation des données de leur modélisation et de leur manipulation.
- La mise à jour de la couche de représentation lorsque les données changent.

---

# Composants 

MVC est composé de 3 modules :

- Modèle : contient les données ainsi que de la logique en rapport avec les données (validation, ...)
- Vue : partie visible d'une interface graphique. Une vue contient des éléments visuels ainsi que la logique nécessaire pour afficher les données provenant du modèle
- Contrôleur : module qui traite les actions de l'utilisateur, modifie les données du modèle et de la vue.

---

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

caption
= Le pattern MVC.
endcaption

HIDE_STEREOTYPE()

Container(model, "Modèle", "ex: Mettre à jour l'application pour représenter l'ajout d'un élément", "Définit les structures de données")
Container(view, "Vue", "ex: L'utilisateur clique sur 'Ajouter au panier'", "Définit l'affichage (UI)")
Container(controller, "Contrôleur", "ex: Reçois une mise à jour de la vue et notifies le modèle d'un 'ajout d'élément'")

Rel_D(model, view, "Met à jour")
Rel_R(view, controller, "Notifie des interactions utilisateur")
Rel_L(controller, view, "Peut mettre à jour directement")
Rel_U(controller, model, "Manipule")
@enduml
```

---

> Architecture of an application is all about its intent. _(Robert Martin)_

---

**MVC N’EST PAS UNE ARCHITECTURE**

- MVC est un mécanisme de livraison de données (par exemple, par le Web) : l'architecture et la logique métier de l'application sont décorrélées de ce pattern
- Les exemples (nombreux) d’application MVC avec persistance directe de la couche _Model_ en base de données sans logique métier sont des anti-patterns !!!

---

```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

caption
= Anti-pattern MVC
endcaption

HIDE_STEREOTYPE()

Person(user, "Utilisateur")

ContainerDb(model, "Modèle", "Base de données", $sprite="&folder,scale=2.0")
Container(view, "Vue", "HTML")
System(controller, "Contrôleur")

Rel(user, controller, "Affiche la page dans son navigateur")
Rel(view, user, "Retourne la page HTML demandée")
Rel(controller, view, " ")
BiRel(controller, model, " ")
@enduml
```

---

![width:600px](https://terasolunaorg.github.io/guideline/5.3.0.RELEASE/en/_images/RequestLifecycle.png)
_Une implémentation MVC : Spring MVC Request Lifecycle (source : terasolunaorg.github.io)._

---

<!-- class: legal -->

# Legal

- Spring® is a trademark of Pivotal Software, Inc. in the U.S. and other countries.
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
