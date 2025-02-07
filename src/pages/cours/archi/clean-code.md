---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Clean Code
tags:
- architecture
- dette-technique
---

<!-- _class: titre lead -->

# Pourquoi un Clean Code ?

---

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand. _Martin Fowler, Refactoring: Improving the Design of Existing Code._

---

> On passe 10 fois plus de temps à lire le code qu'à en écrire.  _Robert C. Martin (Uncle Bob), Clean Code: A Handbook of Agile Software Craftsmanship._

---
> Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it. _Brian Kernighan_

---

- Évite les erreurs
- Plus facile et moins cher à _maintenir_ (> 60 % du coût de l’application) : [How Software Maintenance Fees Are Siphoning Away Your IT Budget – and How to Stop It, Accenture](https://silo.tips/download/procurement-category-information-technology-how-software-maintenance-fees-are-si)
- Plus facile à tester
- Limitent la charge mentale de l'équipe : _l'entreprise n'est qu'un des clients de son produit_
- Impactent les performances, la consommation énergétique, ...
- Poser un cadre mais pas de limites : **votre responsabilité**

---

<!-- _class: titre lead -->

# Règles générales

---

## Normes et conventions

- Suivez des conventions reconnues :
  + Constantes en majuscules
  + `snake_case` vs `CamelCase`

---

## KISS

- Keep it simple stupid :
  + simple : noms de variables, héritage faible, ...
  + non complexe => utiliser des abstractions
  + Voir [cet article](https://www.lilobase.me/la-complexite-une-histoire-de-charge-cognitive/).

---

```python
# bad
for i in range(10):
...

# good
for student_no in range(total_students):
...
```

---

## Boy Scout

- Laissez le code plus propre que l'état dans lequel vous l'avez trouvé.
  + Refactoring permanent
  + Attention aux régressions (tests !)

---

## Root cause

- Lors de résolution d'un problème, toujours chercher et trouver la cause racine.
  + Éviter les "rustines"
  + Si besoin impératif de "rustine", identifier et reporter la dette technique associée.

---

```python
for student_no in range(total_students):
    # KO for student_no == total_students
    print( students[student_no] )

# Bad
for student_no in range(total_students):
    if student_no != total_students:
        print( students[student_no] )

# Good
for student in students:
    print(student)
```

---

## Least Astonishment (POLA) ou Least Surprise (POLS)

- Éviter à un utilisateur toutes les (mauvaises) surprises :
  + Suivre les conventions d'IHM, de nommage, ...
  + UX simple et évidente
  + Modéliser les interfaces graphiques comme machines d'états finis
  + Voir [l'article wikipedia](https://fr.wikipedia.org/wiki/Principe_de_moindre_surprise).

---

## DRY

- Do Not Repeat Yourself :
  + Éviter les copier-coller ;
  + Utiliser des patterns de généralisation (fonctions, classes, délégation, ...).

---

## Single-Source of Trust (SSoT)

- Source de vérité unique
- Éviter les duplications de code métier (voir _Domain-Driven Development_) ;
- Nécessite des données centralisées et des processus dédiés (actualisation, accessibilité).

---

## Les erreurs arrivent

- Partir du principe que les erreurs se produiront :
  + éviter les bugs (bien)
  + maîtriser la reprise en cas d'erreur (mieux)
  + Voir [l'article Wikipedia sur le Chaos Engineering](https://en.wikipedia.org/wiki/Chaos_engineering).

---

## Surveillance utilisateur

- Monitorer les erreurs côté utilisateur.
- Mettre en place des alertes pour le développeur (analyse des logs, API, ...).
- À utiliser pendant les tests fonctionnels.

---

<!-- _class: titre lead -->

# Design

---

## Configurations

- Toutes les constantes doivent être configurables à haut niveau.

---

## Polymorphisme

- Partir d'un type et le modifier
- Évite les `if/else` ou `switch/case`.

---

```python
import math
class Forme:
    def aire(self):
        raise NotImplementedError()

class Carre(Forme):
    def __init__(self, cote):
        self.cote = cote

    def aire(self):
        return self.cote * self.cote

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon * self.rayon
```

---

## YAGNI : You Ain’t Gonna Neet It

- Évitez la sur-configurabilité et le _au cas où_.
- Résoudre le vrai problème plutôt que de futurs potentiels problèmes.
- Limiter la généricité.
- Voir [cet article](https://damien.pobel.fr/post/au-cas-ou/).

---

## Injection de dépendances

- Une classe déclare ses dépendances : `délégation`.
- Un objet n'instancie pas d'autres objets à sa création ou après.
- Utiliser des `Factory` ou un framework.
- Voir le [cours sur l'héritage, le polymorphisme et la délégation][site-perso].

---

## Loi de Déméter

- Une classe devrait faire aussi peu d’hypothèses que possible à propos de la structure de quoi que ce soit d’autre, y compris ses propres sous-composants.
- Voir [l'article Wikipedia sur le sujet](https://fr.wikipedia.org/wiki/Loi_de_D%C3%A9m%C3%A9ter).

```java
// Bad
auto.getMotor().getState().isRunning();

// Good
auto.isRunning();
```

---

## Contraintes en amont

- ex `Google Chrome™` : test automatisé de performances dans CI dès le début du projet

---

<!-- _class: titre lead -->

# Compréhension

---

## Explicite > Implicite

- Noms de variables explicites.

```js
// Bad
const searchUser = (phone) => {
    // ...
}

// Good
const searchUserByPhoneNo = (phone) => {
    // ...
}
```

---

> You should name a variable using the same care with which you name a first-born child.
> Robert C. Martin, Clean Code: A Handbook of Agile Software Craftsmanship

---

## Cohérence

- Si vous faites quelque chose d'une certaines manière, toutes les choses similaires devraient être faites de la même manière.

---

```js
// Bad
const searchUserByPhoneNo = (phone) => {
    // ...
}
const getUserByUsername = (username) => {
    // ...
}

// Good
const searchUserByPhoneNo = (phone) => {
    // ...
}
const searchUserByUsername = (username) => {
    // ...
}
```

---

## Déclaratif > Impératif

- Déclaratif => intention du code (proche du métier, voir BDD).
- Impératif => suite d'actions et comment les exécuter

```php
$Listeparticipants = [1 => 'Pierre', 2 => 'Paul', 3 => 'Sarah'];
$prénom = [];

// Imperative
foreach ($Listeparticipants as $id => $nom) {
    $prénom[] = $nom;
}

// Declarative
$prénom = array_values($Listeparticipants);
```

---

## Encapsuler les conditions limites

- Conditions limites compliquées : créer fonction dédiée au test

```java
// BAD
private User loginWithDifficultCheck(String username) {
    var result = User(username);
    if (username != null) {
        // ...
        if (username.isEmpty()) || !username.matches("^[A-Za-z][A-Za-z0-9_]{7,29}$")) {
            throw InvalidArgumentException(username);
        }
        return user;
    }
}
```

---

```java
// GOOD
private User loginWithEasyCheck(String username) {
    if (usernameInvalid(username)) {
        // Error...
        return User.invalid(username);
    }
    // Username valid...
    return User.valid(username);
}

private static boolean usernameInvalid(String username) {
    return username == null
        || username.isEmpty()
        || !username.matches("^[A-Za-z][A-Za-z0-9_]{7,29}$");
}
```

---

## Value Objects

- `Value Objects` > types primitifs.
  + ajoute du sens
  + évolution du type facile
  + voir [cet exemple en Scala](https://www.baeldung.com/scala/type-declaration).
  + voir [cet article en Python](https://patricklouys.com/2017/06/04/value-objects-explained/).

```scala
type Username = String
```

---

## Conditions positives

- Évitez les négations, surtout les doubles

```python
# bad
if (!isInvalid(...)):

# good
if (isValid(...)):
```

---

<!-- _class: titre lead -->

# Noms

---

- Choisissez des noms descriptifs et sans ambiguïté.
- Faites des distinctions qui ont du sens.
- Utilisez des noms prononçables.
- Utilisez des noms faciles à chercher.
- Évitez d'ajouter des préfixes ou des informations sur les types.

---

## Nombres magiques

- Remplacez les nombres magiques par des constantes bien nommées.

```python
# Bad
for i in range(10):
...

# Good
for i in range(NUMBER_OF_STUDENTS):
...
```

---

<!-- _class: titre lead -->

# Fonctions

---

- Courtes.
- Ne fait qu'une chose et la fait bien.
- Nom descriptif.
- Peu d'arguments : < 3.
- Pas d'effet de bord (_side-effect_).

---

## Retour au plus tôt

```java
// Bad
public int confusingFonction(String name, int value, AuthenticationInfo permissions) {
    int retval = SUCCESS;
    if (globalCondition) {
        if (name != null && !name.equals("")) {
            if (value != 0) {
                if (permissions.allow(name)) {
                    // Action if allowed
                } else {
                    retval = DENY;
                }
            } else {
                retval = BAD_VALUE;
            }
        } else {
            retval = INVALID_NAME;
        }
    } else {
        retval = BAD_COND;
    }
    return retval;
}
```

---

```java
// Good
public int lessConfusingFonction(String name, int value, AuthenticationInfo perms) {
    if (!globalCondition) {
        return BAD_COND;
    }

    if (name == null || name.equals("")) {
        return BAD_NAME;
    }

    if (value == 0) {
        return BAD_VALUE;
    }

    if (!perms.allow(name)) {
        return DENY;
    }

    // Action if allowed
    return SUCCESS;
}
```

---

## Flag

- Pas de _flag_ booléen - écrire plusieurs fonctions

```python
# Bad
widget.repaint(false);

# Good
widget.repaintLater();
```

---

<!-- _class: titre lead -->

# Commentaires

---

- Normalement, un commentaire est inutile.
  + Souvent signe d'un code à retravailler
- Ne pas décrire l'évident (`i++; // increment i`).
- Bon commentaire :
  + explique l'intention
  + averti des conséquences

---

> Code never lies, comments sometimes do. _Ron Jeffries_

---

<!-- _class: titre lead -->

# Structure du code source

---

## Style

- Respecter l'indentation.
- Lignes courtes.

---

## Proximité géographique

- Déclarez les variables à proximité de leurs usages.
- Les fonctions dépendantes les unes des autres devraient être à proximité.
- Les fonctions similaires devraient être à proximité les unes des autres.

---

## Espaces

- Espaces et sauts de lignes :
  + Peu d'espaces, code dense : liens forts
  + Beaucoup d'espaces : liens faibles

---

<!-- _class: titre lead -->

# Objets et structures de données

---

- Petit objet
- Cache les structures internes.
- Responsabilité unique :
  + ne fait qu'une chose
  + peu d'attributs
- Principe de Liskov :
  + une classe de base ne devrait rien connaître de ses classes dérivées.
- Éviter le code statique (partagé entre les objets)
- Voir le [cours sur la Programmation Orientée Objet et les principes SOLID][site-perso].

---

<!-- _class: titre lead -->

# Tests

---

- Un concept par test.
- Rapides.
- Indépendants.
- Répétables.
- Auto validants.
- Utiles.
- Lisibles.
- Faciles à lancer.
- Couverture de code (automatique).
- Voir le [cours sur la méthodologie des tests][site-perso].

---

<!-- _class: titre lead -->

# Code smells

---

- Complexité inutile.
- Répétition inutile.
- Opacité : le code est difficile à comprendre.

---

## Rigidité

- Logiciel difficile à faire évoluer.
- Une petite modification peut causer une cascade de changements.

---

## Immobilité

- Code non réutilisable dans d'autres projets :
  + trop risqué
  + trop coûteux

---

## Fragilité

- Erreurs à plusieurs endroits après un unique changement.

---

## Niveaux d'imbrication

- Limiter la profondeur d'héritage
  + Implémentation d'interface uniquement
- Limiter les niveaux d'imbrication

---

```python
array_3d = [ [ [ 'a', 'b', 'c' ] ] ]
# BAD
for elem_first in array_3d:
    for elem_second in elem_first:
        for elem in elem_second:
            print(elem)

# GOOD
for elem in enumerate_array(array_3d):
    print(elem)

def enumerate_array(my_array):
    ...
```

---

## Voir aussi

- Voir [cet article de CodeGuru](https://refactoring.guru/refactoring/smells) pour des exemples de _code smell_.

---

<!-- _class: titre lead -->

# Gestion des erreurs

---

- Gestion des erreurs séparée du code.
- `Exception` > codes d'erreurs.
  + Ajouter du contexte métier aux messages des exceptions
  + Ne jamais masquer une exception

---

## Null pointer

- Jamais de `null` (surtout pas en `return null`).
- Bonne pratique : programmation défensive sur les interfaces aux limites (API, ...) pour empêcher la propagation d'un objet null.
- Voir [cet article Wikipedia sur le Null Pointer](https://en.wikipedia.org/wiki/Null_pointer#History) expliquant le _billion-dollar mistake_ d'après _Tony Hoare_

---

```java
// Bad
public User login(String username, String password) {
    var user = checkCredentialsInDatabase(username, password);
    if (user == null) {
        throw new IllegalArgumentException("Bad credentials");
    } else {
        return user;
    }
}

private User checkCredentialsInDatabase(String username, String password) {
    User result = null;
    if (username != null) && password != null) {
        var creds = jpa.getCredentials(username, password);
        if (creds == null) {
            result = new User(creds);
        }
    }
    return result;
}
```

---

```java
// Good
public User login(String username, String password) {
    Objects.requireNotNull(username);
    Objects.requireNotNull(password);

    return checkCredentialsInDatabase(username, password);
}

private User checkCredentialsInDatabase(String username, String password) {
    return Optional.ofNullable( jpa.getCredentials(username, password) )
                   .map(User::valid)
                   .orElse( User.invalid(username) );
}
```

---

<!-- class: liens -->

# Liens

- 60 principes essentiels du Clean Code : <https://www.getnobullshit.com/>
- Référentiel de qualité du Web : <https://checklists.opquast.com/fr/assurance-qualite-web/>
- Tests de page Web : <https://www.webpagetest.org>
- Analyses de sécurité Web (entêtes HTTP principalement) : <https://observatory.mozilla.org/>
- <https://github.com/cnumr/best-practices-mobile>
- Voir aussi le cours d'écoconception.

---

# Legal

- Google Chrome™ is a trademark of Google LLC
- Other names may be trademarks of their respective owners
