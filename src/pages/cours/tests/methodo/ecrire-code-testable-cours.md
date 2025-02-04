---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Écrire du code testable
tags:
- tests
- patterns
- architecture
---

# Écrire du code testable

_Tom Avenel_

<https://www.avenel.pro/>

---

<!-- _class: titre lead -->

# Comment écrire du code testable ?

---

# QUELQUES BONNES PRATIQUES GÉNÉRALES

- Nous écrivons tous du code buggué, acceptez-le et faites avec. 
- Écrivez votre code avec le test et le débuggage à l'esprit. 
- Quelle est la chose la plus simple qui pourrait fonctionner ? 
- Ne vous répétez pas. 

---

- Chaque bout de connaissance doit avoir une seule représentation autorisée et non ambiguë dans un système. 
- Constantes, algorithmes, etc. 
- Essayez de limiter l'interdépendance de votre code. (Loose Coupling) 
- Donnez à vos variables, fonctions et modules des noms explicites (pas des noms mathématiques). 

---

<!-- _class: subtitle lead -->

# QUALITÉ DE LA CONCEPTION OBJET

---

# ABSTRACTION ET RESPONSABILITÉ

- Programmation Objet = responsabilité unique : une et une seule raison de modifier une classe/un module.
  + bon indicateur : nom simple de classe (sinon : trop de responsabilités)
  + Augmente la cohésion de la classe

---

- Encapsule toutes (et uniquement) les variables internes nécessaires au bon fonctionnement de cette responsabilité
  + Raison d'être d'un objet qui abstrait une responsabilité à un endroit unique du code.

---

- Principe simple mais souvent transgressé
  + Souvent respecté à la création
  + Cassé lors de modifications ultérieures (souvent par négligence de refactoring).
- Test unitaire de responsabilité pour limiter les transgressions :
  + Ne doit valider qu'une seule et unique classe du code.
  + Les autres classes instanciées ne servent qu'à créer la classe principale (dépendances).

---

# CLASSES ABSTRAITES

- Permet de factoriser un comportement commun à plusieurs classes...
- ...En laissant des spécificités dans chaque héritage.
- Écriture difficile :
  + Principe de responsabilité unique
  + Principe de Liskov : l'héritage ne doit pas changer le comportement du parent.
  + On pourra privilégier le pattern de délégation.

---

- On pourra architecturer les classes en suivant le principe `Stable Abstractions Principle` :
  + Les packages les plus stables doivent être les plus abstraits.
  + Les packages instables doivent être concrets.
  + Le degré d'abstraction d'un package doit correspondre à son degré de stabilité.

---

# KEEP IT SIMPLE, STUPID (KISS)

- Ligne directrice : toute complexité non indispensable doit être évitée.
- Complexité = coûts de conception et de maintenance et source potentielle d'erreurs.
- Ne pas optimiser avant de maîtriser totalement une version simple.

---

- KISS ne proscrit pas la complexité lorsqu'elle est nécessaire !
  + Paradoxalement, tenter d'utiliser des moyens simples pour résoudre un problème complexe peut conduire à une complexité encore plus grande.

---

# Interfaces

- Une des fonctionnalités les plus intéressantes des langages objets.
- Programmation par contrat : l'objet qui en hérite s'engage à suivre le comportement qu'elle décrit.
- En test boîte noire (y compris tests unitaires), on utilisera uniquement des interfaces :
  + Permet de vérifier uniquement le contrat, sans se soucier de l'implémentation.
  + Test plus robuste au changement d'implémentation.

---

<!-- _class: subtitle lead -->

# LES MOCKS

---

# Les mocks

- Une bonne conception objet permet de séparer la logique métier des dépendances techniques.
  + par exemple par usage massif de délégation
- Comment tester cette logique métier si le code possède toujours des dépendances à intégrer (base de données, valeurs non déterministes comme la date d'exécution, ...) ?

---

- Mocks : simulacres d'objets créés et contrôlés par nos soins (ou le framework de test).
  + Permettent de simuler le comportement des dépendances en respectant le même contrat.
  + La dépendance technique est éliminée => on peut se focaliser sur le code métier.
  + Le contrat objet est bien respecté => le code métier est testable.

---

# Mocks vs stubs

On sépare parfois les objets de type Mock en deux types distincts :

- Stubs : objets sans logique.
  + Permettent uniquement de vérifier que la classe ou la méthode a bien été appelée.
  + Exemple : Stub simulant une insertion en base de données pour vérifier qu'un appel à ce composant a bien été réalisé depuis l'API, mais ne fera aucun changement d'état dans le programme. En cas de listing des données, celles-ci ne seront pas mises à jour.

---

- Mocks : regroupent uniquement les simulacres possédant également une logique métier.
  + Exemple : Mock simulant une base de données pour stocker en mémoire les données ajoutées pour retourner une liste à jour en cas de listing.

---

<!-- _class: subtitle lead -->

# EXCEPTIONS ET GESTION DES ERREURS 

---

# UTILISATION DES EXCEPTIONS

- Coupe-circuit permettant de gérer des erreurs… exceptionnelles.
- Permettent d'obtenir un type d'erreur spécifique au problème et d'ajouter du contexte à l'erreur
  + donc des informations métier lors d'un problème technique : nom d'utilisateur, nom de fichier, … ce qui est un gain énorme pour le débuggage du code !

---

Comme le reste du code, les exceptions doivent être testées : elles font partie des branches d'exécution du code.

On sera particulièrement attentif au code métier remonté, pour faciliter le débuggage et l'écriture de logs en production.

---

<!-- _class: subtitle lead -->

# Test-driven development (TDD) et Behavior-driven development (BDD)

---

# Test-driven development (TDD)

- Si possible, un test doit toujours être écrit AVANT l'implémentation qu'il vérifie, et ce afin de certifier que le test lui-même est correct !
- On pourra utiliser la méthode TDD :
  + Écrire un test couvrant un code qui n'existe pas encore : le test doit échouer
  + Lorsque le code est ajouté, le test doit devenir positif

---

# Behavior-driven development (BDD)

- En TDD traditionnel, les tests (unitaires) sont très proches de l'implémentation :
  + Le refactoring peut être compliqué, beaucoup de tests deviennent obsolètes
  + Seul le besoin métier est invariant, le reste dépend de l'implémentation
- En BDD, on préfèrera des tests validant les fonctionnalités du programme plutôt que les détails d'implémentation.

---

- Chaque méthode a ses avantages, il est possible de cumuler les 2 suivant le besoin.
- Ces méthodes améliorent considérablement les temps de développement.

---

<!-- class: liens -->

# Références

- Pour aller plus loin : <https://java.developpez.com/tutoriels/programmation-orientee-objet/principes-avances/>

---

<!-- class: legal -->

# Legal

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
