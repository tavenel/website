---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Écrire du code testable
tags:
- tests
- patterns
- architecture
---

# Comment écrire du code testable ?

---

# Bonnes pratiques générales

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
layout: section
---

# Qualité de la conception objet

---

# Abstraction et responsabilité

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

# Classes abstraites

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

# KISS : Kit it simple stupid

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
layout: section
---

# Les Mocks

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
layout: section
---

# Exceptions et gestion des erreurs

---

# Utilisation des exceptions

- Coupe-circuit permettant de gérer des erreurs… exceptionnelles.
- Permettent d'obtenir un type d'erreur spécifique au problème et d'ajouter du contexte à l'erreur
  + donc des informations métier lors d'un problème technique : nom d'utilisateur, nom de fichier, … ce qui est un gain énorme pour le débuggage du code !

---

Comme le reste du code, les exceptions doivent être testées : elles font partie des branches d'exécution du code.

On sera particulièrement attentif au code métier remonté, pour faciliter le débuggage et l'écriture de logs en production.

---

<!-- class: liens -->

# Références

- 🚀 Pour aller plus loin : <https://java.developpez.com/tutoriels/programmation-orientee-objet/principes-avances/>

