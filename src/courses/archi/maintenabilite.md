---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Analyse de code et maintenabilité
tags:
- architecture
- dette-technique
---

## Introduction

### Pourquoi analyser le code ?

Une application logicielle n'est pas seulement un programme qui « fonctionne ».

Au cours de sa vie, une application doit être :

* corrigée ;
* modifiée ;
* adaptée à de nouveaux besoins ;
* sécurisée ;
* optimisée ;
* portée vers de nouvelles versions de ses dépendances ou de son environnement ;
* comprise par de nouveaux développeurs.

Cette activité constitue une part importante de la **maintenance logicielle**.

> **Question :** qu'est-ce qui rend un code facile ou difficile à maintenir ?

Plusieurs facteurs interviennent :

* sa complexité ;
* sa lisibilité ;
* sa structure ;
* le couplage entre ses composants ;
* la cohésion de ses modules ;
* la duplication ;
* la présence de défauts ;
* la couverture par les tests ;
* la documentation ;
* la stabilité de ses dépendances.

L'**analyse de code** fournit des techniques permettant d'observer et de mesurer certains de ces aspects.

---

## Analyse de code

L'analyse de code consiste à examiner un programme afin d'en extraire des informations sur :

* sa structure ;
* son comportement ;
* sa complexité ;
* ses dépendances ;
* ses défauts potentiels ;
* ses caractéristiques de qualité.

Elle peut être réalisée à différents moments :

```text
             Code source
                 │
        ┌────────┴────────┐
        │                 │
 Analyse statique   Analyse dynamique
        │                 │
        │                 │
 sans exécuter       pendant
 le programme        l'exécution
        │                 │
        ▼                 ▼
 structure          comportement
 complexité         performances
 style               mémoire
 défauts potentiels  traces
```

### Analyse statique

L'analyse statique examine le code **sans l'exécuter**.

Exemples :

```java
if (user != null) {
    if (user.getAddress() != null) {
        if (user.getAddress().getCity() != null) {
            System.out.println(user.getAddress().getCity());
        }
    }
}
```

Un analyseur peut détecter :

* une complexité excessive ;
* du code dupliqué ;
* des variables inutilisées ;
* des branches suspectes ;
* certaines erreurs potentielles ;
* des violations de conventions ;
* des problèmes de sécurité.

### Analyse dynamique

L'analyse dynamique observe le programme **pendant son exécution**.

Elle permet notamment d'étudier :

* le temps d'exécution ;
* la consommation mémoire ;
* les appels de fonctions ;
* les allocations ;
* les exceptions ;
* les accès réseau ou fichiers ;
* les comportements concurrents.

Exemples d'outils :

* profilers ;
* outils de tracing ;
* analyseurs mémoire ;
* observabilité applicative.

### Analyse statique et tests : deux approches complémentaires

Il ne faut pas confondre analyse de code et tests automatisés.

Un test cherche généralement à répondre à une question du type :

> « Pour cette entrée, le programme produit-il le résultat attendu ? »

Une analyse statique cherche plutôt :

> « Existe-t-il dans ce code une construction qui pourrait indiquer un problème ? »

Par exemple :

```java
String getName(User user) {
    return user.getName();
}
```

Une analyse statique peut identifier un risque de `NullPointerException`.

Un test pourrait ensuite vérifier :

```java
@Test
void shouldHandleNullUser() {
    ...
}
```

Les deux approches sont donc complémentaires.

---

## Cycle de vie

L'analyse de code intervient à plusieurs niveaux du cycle de développement.

```text
Développement
     │
     ▼
Commit ──► Analyse ──► Tests ──► Build
                         │
                         ▼
                       CI/CD
                         │
                         ▼
                     Déploiement
                         │
                         ▼
                    Production
                         │
                         ▼
                    Maintenance
                         │
                         └──────► nouveau changement
```

L'objectif n'est donc pas uniquement de détecter des erreurs avant la mise en production.

L'analyse peut également permettre de **surveiller la dégradation progressive de la qualité**.

---

## Objectifs

On peut regrouper les objectifs du module en trois grandes catégories :

1. **détecter des erreurs et défauts potentiels** ;
2. **améliorer et maintenir la qualité du code** ;
3. **identifier et comprendre les problèmes de performance**.

Ces objectifs se recouvrent partiellement, mais utilisent des techniques différentes.

---

## Détection des erreurs

### Les erreurs ne sont pas toutes des bugs visibles

Considérons :

```python
def calculate_average(values):
    return sum(values) / len(values)
```

Le code paraît correct.

Mais que se passe-t-il avec :

```python
calculate_average([])
```

L'analyse du code et les tests permettent de rechercher différentes catégories de problèmes.

### Erreurs syntaxiques

Détectées généralement par :

* le compilateur ;
* l'interpréteur ;
* l'IDE.

### Erreurs de typage

Exemple :

```typescript
function add(a: number, b: number): number {
    return a + b;
}

add("10", 20);
```

Le système de types peut détecter le problème avant l'exécution.

### Erreurs potentielles

Exemple :

```java
User user = repository.findById(id);

return user.getName();
```

L'analyse peut signaler que `user` pourrait être `null`.

### Erreurs de logique

Elles sont beaucoup plus difficiles à détecter automatiquement.

```python
if age > 18:
    access = "denied"
```

Le programme peut être syntaxiquement correct, mais son comportement peut être incorrect.

C'est pourquoi l'analyse de code **ne remplace pas les tests**.

---

### Analyse des défauts potentiels

Les analyseurs statiques recherchent généralement des **patterns connus comme étant suspects**.

Exemple :

```java
String password = "admin123";
```

Un outil de sécurité peut identifier :

> Hard-coded credential

Autre exemple :

```javascript
const query = "SELECT * FROM users WHERE id = " + id;
```

Un analyseur peut détecter un risque potentiel d'injection SQL.

L'outil ne dit pas nécessairement :

> « votre application est vulnérable ».

Il peut plutôt dire :

> « cette construction correspond à un pattern présentant un risque ».

Cette distinction est importante.

---

## Faux positifs et faux négatifs

Une analyse automatique peut se tromper.

### Faux positif

L'outil signale un problème alors qu'il n'y en a pas.

```text
Code correct
    │
    ▼
Analyseur
    │
    ▼
⚠️ Problème signalé
    │
    ▼
Mais le code est effectivement correct
```

### Faux négatif

Un problème existe mais n'est pas détecté.

```text
Code problématique
    │
    ▼
Analyseur
    │
    ▼
✓ Aucun problème détecté
```

Ces deux phénomènes expliquent pourquoi les outils d'analyse doivent être utilisés avec discernement.

> **Un outil d'analyse fournit des informations : il ne remplace pas le jugement du développeur.**

---

## Qualité du code et maintenabilité

### Qu'est-ce qu'un code maintenable ?

Un code maintenable est notamment un code :

* compréhensible ;
* modifiable ;
* testable ;
* suffisamment modulaire ;
* prévisible ;
* peu couplé ;
* cohérent avec les conventions du projet.

Une définition utile consiste à considérer la maintenabilité comme la facilité avec laquelle une équipe peut **comprendre et modifier le logiciel sans introduire de nouveaux problèmes**.

---

## Les principales dimensions de la qualité

Plusieurs propriétés peuvent être observées.

| Propriété     | Question                                              |
| ------------- | ----------------------------------------------------- |
| Lisibilité    | Peut-on comprendre rapidement le code ?               |
| Complexité    | Est-il difficile à raisonner ?                        |
| Cohésion      | Un module possède-t-il une responsabilité claire ?    |
| Couplage      | Dépend-il excessivement d'autres modules ?            |
| Duplication   | Le même comportement est-il répété ?                  |
| Testabilité   | Peut-on facilement le tester ?                        |
| Documentation | Les informations importantes sont-elles disponibles ? |
| Cohérence     | Les mêmes conventions sont-elles utilisées partout ?  |

---

## Complexité cyclomatique

La **complexité cyclomatique** est une métrique classique d'analyse de code.

Elle mesure approximativement le nombre de chemins indépendants dans un morceau de code.

Exemple :

```python
def calculate_price(user, product):
    price = product.price

    if user.is_premium:
        price *= 0.9

    if product.on_sale:
        price *= 0.8

    return price
```

Chaque branche augmente la complexité.

On peut retenir une approximation simple :

```text
Complexité ≈ nombre de points de décision + 1
```

Les points de décision comprennent notamment :

* `if`
* `for`
* `while`
* `case`
* certaines expressions logiques

Plus la complexité augmente, plus il devient difficile :

* de comprendre le code ;
* de tester tous les chemins ;
* de prévoir les effets d'une modification ;
* de maintenir le programme.

Mais une métrique élevée n'est pas automatiquement un bug.! Une fonction complexe peut être nécessaire dans certains domaines.

La métrique constitue un **signal**, pas un verdict.

---

### Exemple : réduire la complexité

Code initial :

```python
def calculate_shipping(order):
    if order.country == "FR":
        if order.total > 50:
            return 0
        else:
            return 5
    else:
        if order.total > 100:
            return 0
        else:
            return 15
```

On peut introduire une abstraction :

```python
def calculate_shipping(order):
    if order.country == "FR":
        return shipping_fr(order.total)

    return shipping_international(order.total)
```

Le but du refactoring n'est pas nécessairement de diminuer mécaniquement une métrique.

Il est de rendre le code :

* plus compréhensible ;
* plus modulaire ;
* plus facilement testable ;
* plus facilement modifiable.

---

## Duplication de code

Considérons :

```java
double calculatePrice(Product p) {
    double price = p.getPrice();

    if (p.isDiscounted()) {
        price *= 0.8;
    }

    return price;
}
```

et :

```java
double calculatePrice(OrderLine line) {
    double price = line.getPrice();

    if (line.isDiscounted()) {
        price *= 0.8;
    }

    return price;
}
```

La duplication peut sembler anodine.

Mais imaginons que la règle change :

```text
20 % de réduction
        ↓
25 % de réduction
```

Il faut modifier plusieurs endroits.

La duplication augmente donc le **coût de maintenance** et le risque d'incohérence.

---

## Code smells

Un **code smell** est un indice indiquant qu'une partie du code pourrait présenter un problème de conception ou de maintenabilité.

Exemples :

* méthode trop longue ;
* classe trop volumineuse ;
* duplication ;
* trop nombreux paramètres ;
* couplage excessif ;
* responsabilités multiples ;
* conditions imbriquées ;
* noms peu explicites ;
* commentaires compensant une conception difficile à comprendre.

Un code smell n'est pas nécessairement une erreur.

```text
Code smell
    │
    ▼
Signal
    │
    ▼
Investigation
    │
    ├── problème réel ?
    │       │
    │       ▼
    │    refactoring
    │
    └── choix de conception justifié ?
            │
            ▼
          conserver
```

---

## Refactoring

Le **refactoring** consiste à modifier la structure interne du code sans modifier son comportement observable.

Exemple :

```java
if (user.getRole().equals("ADMIN")) {
    ...
}
```

peut devenir :

```java
if (user.isAdmin()) {
    ...
}
```

Le comportement attendu reste identique, mais le code exprime mieux l'intention.

Le refactoring est particulièrement important dans un contexte de maintenance.

---

## Analyse des performances

L'analyse de code peut également contribuer à identifier des problèmes de performance.

Exemple :

```python
for user in users:
    for permission in permissions:
        if permission.user_id == user.id:
            ...
```

Pour de grandes collections, cette structure peut devenir coûteuse.

Un analyseur ou un profiler peut aider à identifier :

* une fonction trop lente ;
* une boucle coûteuse ;
* un nombre excessif d'appels ;
* une allocation mémoire importante ;
* un accès réseau répété ;
* une requête SQL coûteuse.

---

### Analyse statique et performance

Certains problèmes peuvent être détectés statiquement.

Exemple :

```javascript
array.filter(...).map(...).filter(...).map(...)
```

Un analyseur peut identifier certaines constructions inefficaces.

Mais beaucoup de problèmes de performance dépendent du contexte réel.

Par exemple :

```text
Code
 │
 ▼
Complexité théorique
 │
 ▼
Données réelles
 │
 ▼
Infrastructure
 │
 ▼
Réseau / disque / base de données
 │
 ▼
Performance observée
```

C'est pourquoi les performances nécessitent souvent une **analyse dynamique**.

---

## Big O et analyse algorithmique

L'analyse de la complexité algorithmique complète les outils d'analyse de code.

Exemple :

```python
def contains_duplicate(values):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return True

    return False
```

Complexité approximative :

```text
O(n²)
```

Une autre approche :

```python
def contains_duplicate(values):
    return len(values) != len(set(values))
```

Complexité moyenne :

```text
O(n)
```

L'analyse algorithmique permet donc d'identifier certaines limites structurelles du programme.

---

## Analyse de code dans une CI

L'un des intérêts majeurs des outils d'analyse est leur intégration dans la CI.

Exemple :

```text
              Git push
                  │
                  ▼
             CI pipeline
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
    Linter      Tests      Analyse
                           statique
       │          │          │
       └──────────┼──────────┘
                  ▼
              Quality Gate
                  │
            ┌─────┴─────┐
            ▼           ▼
          PASS          FAIL
            │
            ▼
           Build
```

Le module **CI/CD** peut traiter l'orchestration du pipeline.

Le module **automatisation des tests** peut traiter :

* tests unitaires ;
* tests d'intégration ;
* tests end-to-end ;
* couverture.

Le module **analyse de code et maintenabilité** se concentre sur :

* ce qui est analysé ;
* pourquoi ;
* comment interpréter les résultats ;
* quelles métriques utiliser ;
* comment améliorer le code.

---

## Quality Gate

Un **quality gate** définit des conditions minimales avant de poursuivre le pipeline.

Exemple :

```yaml
quality:
  rules:
    - no_critical_vulnerabilities
    - max_complexity: 15
    - max_duplication: 5%
    - lint_errors: 0
```

Attention : une quality gate doit être conçue avec soin !

Des règles trop strictes peuvent produire :

* beaucoup de faux positifs ;
* des contournements ;
* une fatigue face aux alertes ;
* une perte de confiance dans l'outil.

Des règles trop permissives peuvent rendre l'analyse inutile.

> Une quality gate est très utile pour du développement agentique !

---

## Dette technique

La **dette technique** désigne notamment les coûts futurs induits par des choix techniques ou de conception qui rendent les évolutions plus difficiles.

Exemple :

```text
Solution rapide
     │
     ▼
Dette technique
     │
     ▼
Maintenance plus coûteuse
     │
     ▼
Nouvelles modifications
     │
     ▼
Encore plus de complexité
```

L'analyse de code peut aider à rendre cette dette **observable**.

Exemples :

* augmentation de la complexité ;
* augmentation de la duplication ;
* augmentation du couplage ;
* diminution de la couverture ;
* augmentation du nombre de vulnérabilités.

---

## Exemple : évolution d'un projet

Imaginons un projet observé sur six mois.

| Métrique                 | Mois 1 | Mois 3 | Mois 6 |
| ------------------------ | -----: | -----: | -----: |
| Duplication              |    2 % |    4 % |    8 % |
| Complexité moyenne       |      4 |      6 |      9 |
| Bugs détectés            |      5 |      8 |     17 |
| Vulnérabilités critiques |      0 |      1 |      3 |

Pris isolément, chaque chiffre est difficile à interpréter.

Mais leur **évolution** peut attirer l'attention sur une dégradation de la qualité.

L'objectif de l'analyse est alors de poser de nouvelles questions :

* quelles parties du code évoluent ?
* pourquoi la duplication augmente-t-elle ?
* quelles équipes ou fonctionnalités sont concernées ?
* certains modules sont-ils particulièrement complexes ?
* les mêmes défauts se répètent-ils ?

---

## Bonnes pratiques

* Automatiser ce qui peut l'être
* Analyser tôt
* Intégrer l'analyse au workflow Git
* Traiter les alertes

## Analyse automatique et revue humaine

Les outils et les développeurs ont des rôles différents.

| Analyse automatique    | Revue humaine               |
| ---------------------- | --------------------------- |
| règles répétitives     | intention du code           |
| conventions            | architecture                |
| patterns connus        | choix de conception         |
| métriques              | compromis                   |
| vulnérabilités connues | contexte métier             |
| duplication            | pertinence de l'abstraction |

Une bonne démarche combine les deux.

---

## À retenir

* **Analyse de code** : Examiner automatiquement ou manuellement un programme afin d'identifier des propriétés, des défauts potentiels et des caractéristiques de qualité.
* **Analyse statique** : Analyse réalisée sans exécuter le programme.
* **Analyse dynamique** : Analyse réalisée pendant l'exécution du programme.
* **Maintenabilité** : Capacité d'un logiciel à être compris, corrigé et modifié avec un coût et un risque raisonnables.
* **Code smell** : Indice d'un problème potentiel de conception ou de maintenabilité.
* **Refactoring** : Modification de la structure interne du code sans modification de son comportement observable.
* **Quality gate** : Ensemble de règles permettant de décider automatiquement si un changement satisfait un niveau de qualité défini.
* **Principe essentiel** : **Les outils d'analyse ne remplacent ni les tests ni les développeurs : ils augmentent leur capacité à détecter et comprendre les problèmes.**

---

## Questions de révision

1. Quelle différence existe-t-il entre analyse statique et analyse dynamique ?
2. Quelle différence existe-t-il entre analyse de code et test automatisé ?
3. Qu'est-ce qu'un faux positif ?
4. Qu'est-ce qu'un faux négatif ?
5. Pourquoi la complexité cyclomatique est-elle intéressante ?
6. Pourquoi une métrique ne constitue-t-elle pas à elle seule une preuve de mauvaise qualité ?
7. Qu'est-ce qu'un code smell ?
8. Qu'est-ce que le refactoring ?
9. Quelle différence existe-t-il entre un linter et un formatter ?
10. Que signifie SAST ?
11. Pourquoi analyser les dépendances d'une application ?
12. Pourquoi intégrer l'analyse de code dans une CI ?
13. Qu'est-ce qu'une quality gate ?
14. Pourquoi les règles d'analyse doivent-elles être adaptées au contexte du projet ?
15. Quelles sont les limites de l'analyse automatique ?
16. Comment l'analyse de code contribue-t-elle à la maintenabilité ?
17. Pourquoi suivre l'évolution d'une métrique peut-il être plus intéressant que sa valeur absolue ?
18. Comment combiner analyse de code, tests automatisés et revue de code ?
