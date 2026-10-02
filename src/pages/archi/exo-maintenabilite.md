---
title: Étude de cas — Analyse et refactoring d'une fonction Python
date: 2026-2027
---

## Situation

Vous rejoignez une équipe qui maintient une application de gestion de commandes.

Une fonction existante est utilisée pour traiter une commande :

```python
def process_order(order, user, database):
    if user is not None:
        if order is not None:
            if len(order.items) > 0:
                if user.is_active:
                    total = 0

                    for item in order.items:
                        total += item.price * item.quantity

                    if user.is_premium:
                        total *= 0.9

                    database.save(
                        user.id,
                        order.id,
                        total
                    )

                    return total

    return None
```

L'équipe souhaite améliorer la maintenabilité du projet avant d'ajouter de nouvelles fonctionnalités.

Analysez cette fonction sans la modifier dans un premier temps.

## Question 1 — Imbrication

Combien de niveaux d'imbrication conditionnelle observez-vous ?

Identifiez les différentes conditions concernées.

## Question 2 — Complexité

Estimez la **complexité cyclomatique** de la fonction.

Quels sont les points de décision qui contribuent à cette complexité ?

## Question 3 — Responsabilités

Identifiez les différentes responsabilités prises en charge par `process_order`.

Représentez-les sous forme d'arbre.

Exemple :

```text
process_order
 ├── ...
 ├── ...
 └── ...
```

## Question 4 — Testabilité

Peut-on facilement tester cette fonction ?

Identifiez au moins **quatre scénarios de test** pertinents.

## Question 5 — Gestion des erreurs

Que se passe-t-il si :

```python
database.save(...)
```

échoue ?

Envisagez plusieurs causes possibles :

* exception ;
* indisponibilité de la base de données ;
* erreur réseau ;
* erreur de contrainte ;
* timeout.

Le comportement de la fonction est-il clairement défini ?

## Question 6 — Refactoring

Proposez une ou plusieurs transformations permettant d'améliorer la fonction.

Votre proposition doit chercher à améliorer au moins deux des propriétés suivantes :

* lisibilité ;
* complexité ;
* testabilité ;
* séparation des responsabilités ;
* gestion des erreurs.

## Question 7 — Analyse automatique

Quels problèmes pourraient être détectés par un outil d'analyse de code ?

Classez vos réponses dans les catégories suivantes :

| Catégorie            | Problèmes potentiels |
| -------------------- | -------------------- |
| Style                |                      |
| Complexité           |                      |
| Maintenabilité       |                      |
| Sécurité             |                      |
| Erreurs potentielles |                      |

## Question 8 — Analyse humaine

Quels problèmes ne peuvent pas être correctement évalués uniquement avec un outil automatique ?

Justifiez votre réponse.

:::correction

# Correction

## 1. Imbrication

La fonction présente **quatre niveaux d'imbrication conditionnelle** :

```python
if user is not None:             # niveau 1
    if order is not None:        # niveau 2
        if len(order.items) > 0: # niveau 3
            if user.is_active:   # niveau 4
                ...
```

À cela s'ajoutent ensuite :

```python
if user.is_premium:
```

qui se trouve à l'intérieur du quatrième niveau.

Cette structure augmente la charge cognitive nécessaire pour comprendre le chemin d'exécution.

### Premier problème identifié

Le code utilise une succession de conditions positives :

```text
user existe
    └── order existe
        └── order contient des éléments
            └── user actif
                └── calcul
                    └── utilisateur premium ?
```

Une approche avec des **early returns** permettrait de réduire cette imbrication.

## 2. Complexité cyclomatique

Une approximation courante est :

```text
complexité cyclomatique = nombre de points de décision + 1
```

On trouve ici :

1. `if user is not None`
2. `if order is not None`
3. `if len(order.items) > 0`
4. `if user.is_active`
5. `for item in order.items`
6. `if user.is_premium`

Soit :

```text
6 décisions + 1 = 7
```

La complexité cyclomatique est donc approximativement de **7**. Cette valeur doit cependant être interprétée avec prudence.

La complexité cyclomatique n'indique pas directement que le code est « mauvais ». Elle constitue un **indicateur** permettant d'identifier des fonctions qui méritent une attention particulière.

## 3. Responsabilités

La fonction réalise plusieurs opérations différentes.

On peut identifier au minimum :

```text
process_order
 ├── validation de l'utilisateur
 ├── validation de la commande
 ├── validation du contenu de la commande
 ├── vérification de l'état du compte
 ├── calcul du montant
 ├── application d'une réduction
 └── persistance de la commande
```

On peut regrouper ces opérations en quatre grandes responsabilités :

```text
process_order
 ├── validation
 ├── calcul du prix
 ├── application de la réduction
 └── persistance
```

Cette dernière représentation est particulièrement intéressante pour réfléchir au refactoring.

## 4. Testabilité

La fonction est testable, mais plusieurs scénarios doivent être envisagés.

Au minimum :

| Cas                            | Résultat attendu    |
| ------------------------------ | ------------------- |
| `user is None`                 | aucun traitement    |
| `order is None`                | aucun traitement    |
| commande vide                  | aucun traitement    |
| utilisateur inactif            | aucun traitement    |
| utilisateur actif, non premium | prix normal         |
| utilisateur actif, premium     | réduction de 10 %   |
| plusieurs articles             | somme correcte      |
| erreur de persistance          | comportement défini |

On peut également tester :

```text
quantité = 1
quantité > 1
prix = 0
plusieurs articles
```

### Problème de conception

La fonction retourne :

```python
None
```

dans plusieurs situations différentes.

Par exemple :

```python
user is None
```

et :

```python
user.is_active is False
```

produisent tous deux :

```python
None
```

Le contrat de la fonction ne permet donc pas de distinguer facilement les différentes causes d'échec.

Cela peut être acceptable selon le domaine, mais mérite d'être explicitement décidé.

## 5. Échec de database.save()

Actuellement :

```python
database.save(
    user.id,
    order.id,
    total
)
```

est appelé sans gestion explicite d'erreur.

Si `save()` lève une exception, celle-ci remonte vers l'appelant.

Par exemple :

```text
process_order()
      │
      ▼
database.save()
      │
      X
   Exception
      │
      ▼
appelant
```

La fonction ne définit donc pas elle-même de comportement particulier.

Ce n'est pas nécessairement incorrect.

La bonne question est :

> **Qui doit être responsable de la gestion de cette erreur ?**

Plusieurs stratégies sont possibles :

### Stratégie A — laisser remonter l'exception

```python
database.save(...)
```

L'appelant gère l'erreur.

### Stratégie B — traduire l'exception

```python
try:
    database.save(...)
except DatabaseError as exc:
    raise OrderProcessingError(...) from exc
```

La couche métier expose alors une exception adaptée à son domaine.

### Stratégie C — retourner un résultat explicite

Par exemple :

```python
return Result.failure(...)
```

Le choix dépend de l'architecture et du contrat de l'application.

## 6. Premier refactoring : early returns

Une première amélioration consiste à supprimer l'imbrication.

```python
def process_order(order, user, database):
    if user is None:
        return None

    if order is None:
        return None

    if not order.items:
        return None

    if not user.is_active:
        return None

    total = 0

    for item in order.items:
        total += item.price * item.quantity

    if user.is_premium:
        total *= 0.9

    database.save(
        user.id,
        order.id,
        total
    )

    return total
```

La complexité cyclomatique reste approximativement la même.

En revanche, l'imbrication diminue fortement.

### Avant

```text
if
 └── if
      └── if
           └── if
                └── traitement
```

### Après

```text
if → return
if → return
if → return
if → return

traitement
```

Il s'agit d'un bon exemple d'une distinction importante :

> **Une métrique peut rester identique alors que la lisibilité s'améliore.**

## 7. Deuxième refactoring : extraire le calcul

On peut isoler le calcul du prix :

```python
def calculate_order_total(order, user):
    total = sum(
        item.price * item.quantity
        for item in order.items
    )

    if user.is_premium:
        total *= 0.9

    return total
```

Puis :

```python
def process_order(order, user, database):
    if user is None:
        return None

    if order is None:
        return None

    if not order.items:
        return None

    if not user.is_active:
        return None

    total = calculate_order_total(order, user)

    database.save(
        user.id,
        order.id,
        total
    )

    return total
```

On sépare alors :

```text
process_order
 ├── validation
 ├── calcul
 └── persistance
```

Le calcul devient également plus facile à tester indépendamment.

## 8. Troisième refactoring : séparation plus forte des responsabilités

Une architecture plus structurée pourrait être :

```python
def validate_order(order, user):
    if user is None:
        return False

    if order is None:
        return False

    if not order.items:
        return False

    if not user.is_active:
        return False

    return True
```

```python
def calculate_order_total(order, user):
    total = sum(
        item.price * item.quantity
        for item in order.items
    )

    if user.is_premium:
        total *= 0.9

    return total
```

Puis :

```python
def process_order(order, user, database):
    if not validate_order(order, user):
        return None

    total = calculate_order_total(order, user)

    database.save(
        user.id,
        order.id,
        total
    )

    return total
```

On obtient :

```text
process_order
       │
       ├── validate_order()
       │
       ├── calculate_order_total()
       │
       └── database.save()
```

Cette solution est plus modulaire, mais elle introduit également davantage de fonctions.

> Le refactoring n'est donc pas une course au nombre maximal de petites fonctions.

:::
