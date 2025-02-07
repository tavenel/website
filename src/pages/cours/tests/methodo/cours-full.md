---
title: Méthodologie des tests logiciels
---

## Chapitres

---

<!-- _class: chapter -->
# Introduction aux tests logiciels

---

# Pourquoi tester le logiciel ?

- Les sondes perdues (Mars Climate Orbiter, Mars Pathfinder)
- Les missiles Patriotes
- 1er vol d’Ariane 5
- Therac-25
- Steam sur Linux
- OpenSSL sur Debian (génération aléatoire suite warning Valgrind)
- Pensions alimentaires britanniques : 1 milliard dollars

---

> En essayant continuellement on finit par réussir. Donc : plus ça rate, plus on a de chance que ça marche. (Devise Shadok)

Voir aussi : [Fireship - The horrors of software bugs](https://www.youtube.com/watch?v=Iq_r7IcNmUk)

---

# Pourquoi tester le logiciel ?

## Les projets logiciels :

- Ne livrent pas le produit dans les temps ;
- Coûtent beaucoup plus chers que prévu ;
- Délivrent un produit de qualité très faible ;
- Échouent dans la majorité des cas !!!

---

> En Europe, grâce aux logiciels de tests nous pourrions économiser plus de 100 milliards d'euros par an. _Klaus Lambertz, Verifysoft Technology GmbH_

---

# Spécificités du logiciel

- Échecs très nombreux ;
- Crash système considéré comme habituel ;
- Cause du bug pas directement identifiable ;
- Dommages (souvent) mineurs ;

---

- A part dans les systèmes critiques, on considère que le logiciel ne peut anticiper toutes les situations ;
- Les systèmes informatiques se complexifient trop vite ;
- Les logiciels passent par des états discrets, dont certains ne sont pas prévus ;
- Ajouts, changements de fonctionnalités, de plate- formes...

---

![](/cours/gestion-projet/gestion_projet_balancoire.jpg)

---

<!-- _class: titre -->
# Enquête 2017-2018 ISTQB (International Software Testing Qualifications Board)

---

Main improvement areas in software testing are :

- Test automation
- Knowledge about test processes
- Communication between development and testing

---

Top five test design techniques utilized by software testing teams are :

- Use case testing
- Exploratory testing
- Boundary value analysis
- Checklist based
- Error guessing

---

New technologies or subjects that are expected to affect software testing in near future are :

- Security
- Artificial intelligence
- Big data

---

Trending topics for software testing profession in near future will be :

- Test automation
- Agile testing
- Security testing

---

Non-testing skills expected from a typical tester are :

- Soft skills
- Business/domain knowledge
- Business analysis skills

---

<!-- _class: titre lead -->
# Les métiers du test logiciel

---

# Test Manager

_Responsable du processus et de la bonne conduite des tests._

---

Des activités techniques de test :

- Planifier les activités de test : objectifs, risques, estimation temps/effort/coût, types et niveaux de tests, gestion des défauts, ...
- Rédiger les plans de test ;
- Concevoir, implémenter, exécuter les tests ;
- Suivre et publier les résultats des tests ;
- Contrôler le niveau de qualité du produit (+métriques) ;

---

Des activités opérationnelles et de gestion :

- Développer une politique et une stratégie de test, gérer les testeurs ;
- Coordonner avec les parties prenantes (chef de projet, PO, ...) ;
- Coordonner avec l'intégration ;
- Gérer les environnements de test et de gestion des défauts (+outils).

---

# Testeur logiciel

Exemples d'activités :

- Analyser et challenger les User Stories ,les spécifications, les modèles pour les rendre testables ;
- Documenter les conditions de test ;
- Concevoir les environnements de test ;

---

- Contribuer aux plans de test ;
- Implémenter les cas de test ;
- Préparer les données de test ;
- Créer le planning détaillé d'exécution des tests ;
- Exécuter les tests et documenter les résultats ;
- Automatiser des tests si nécessaire ;
- Évaluer les caractéristiques non-fonctionnelles : performance, sécurité, ...

---

<!-- _class: chapter -->
# Impact des tests sur l'intégration

---

# Impacts des tests sur l'intégration

- Impact fort sur les processus d'intégration d'un système.
- Parfois vus comme un frein à la réactivité…
- …mais détectent des problèmes inhérents à la gestion du projet mis "sous le tapis"

---

Ce sont donc souvent des bombes à retardement lorsque la problématique apparaît en production et qu'aucun process n'a été pensé en amont (récupération de données de test, réinitialisation d'un système, modification de données pendant l'exécution, gestion des logs, ...)

---

## Anticiper

- Dédier des cycles du projet à des environnements et des outils d'intégration pour anticiper les problèmes en production :
  - tests
  - monitoring
  - gestion des logs
  - aide au redéploiement
  - …
- Généralement très rentable

---

Les réflexions et la mise en place des processus d'intégration (y compris les tests) se font dès le début du projet !

---

## Risques et coûts

Quelques exemples de risques :

- Altérer la confiance des utilisateurs : service non accessible, …
- Non-conformité aux réglementations : _RGPD_, …
- Atteinte à la sécurité des données : perte de données, vol d'informations personnelles

---

Toutes ces risques ont un coût important lorsqu'ils se produisent : on essaiera donc de faire correspondre le coût des tests au risque financier qu'ils protègent. 

---

## Gouvernance

Les tests d'intégration constituent l'étape où l'on commence à assembler les briques applicatives unitaires pour construire un Système d'Information.

- On passe du chacun pour soi à un système commun
- Ne pas négliger les besoins des autres applications
  - d'un modèle producteur / consommateur à un modèle collaboratif
- Problèmes de gouvernance et d'arbitrage
  - À clarifier dès le début du projet
  - Décrire un processus clair

---

## Entraide

- Créer un climat de confiance et **d'aide aux investigations** :
  - entraide plutôt que compétition
  - transmission du savoir
- Ne pas séparer l'équipe d'intégration
  - un seule équipe porte l'ensemble de la responsabilité (Scrum, …)

---

## Réflexions

- Si trop de temps passé aux investigations :
  - soit l'équipe est en sous-effectif
  - soit les outils (monitoring, logs, …) ne sont pas adaptés
- Réfléchir constamment aux outils et processus permettant d'améliorer les investigations

---

## Prioriser les corrections d'erreurs

- Dette technique : coût futur de tous les problèmes techniques (bugs, mauvaises pratiques, … )
- Sans correction, la datte technique augmente avec le projet et le temps
  - le même problème est de plus en plus difficile à corriger !
- Ces erreurs vont aussi faire perdre du temps à tous les consommateurs du service ou de la fonctionnalité
  - l'impact d'une erreur sur l'avancée d'un projet est vite exponentielle.

---

- Solution : prioriser la correction des erreurs :
  - Gestion de processus d'exception ;
  - Arrêt du développement pour corrections critiques ;
  - Budgétisation des erreurs non corrigées et intégration dans les rapports projet.

---

## Tests critiques

- Ensemble de tests à tourner obligatoirement avant de continuer à une autre étape du processus
- Bonne pratique pour limiter les régressions.

---

Dans la pratique :

- Ensemble de tests à valider avant d'intégrer en pré-production
  - Évite d'impacter les autres services lors de l'intégration
- Ensemble de tests manuels d'acceptation avant la mise en production.
  - Minimise les faux positifs à cause d'incohérences difficiles à automatiser (IHM, …)

---

## Environnements dédiés

- Intégration : interactions composants, difficile à tester, erreurs nombreuses
  - à anticiper
- Utiliser des environnements dédiés avant la mise en production : staging, pré-production, …
  - au moins 1 environnement d'intégration technique
  - parfois 1 environnement de recette (test du métier)

---

<!-- _class: chapter -->
# Présentation des tests statiques

---

## Tests statiques vs dynamiques

- **Tests dynamiques** : nécessitent l'exécution du logiciel testé ;
- **Tests statiques** : examen manuel (_revues_) ou évaluation outillée (_analyse statique_) sans exécuter le code.

---

### Exemples

- Systèmes critiques : _aéronautique, médical, ..._
- Très démocratisé : _IDE, CI_
- Tout type de livrable : _spécifications, code, manuel utilisateur, page Web, ..._

---

## Avantages

- **Prévention** des défauts de conception ou de codage ;
  + **Difficulté** à trouver les défauts **dynamiquement** ;
  + Détection et correction **plus efficace** **avant** les tests dynamiques

---

## Avantages

- Meilleure productivité du développement :
  + **Meilleure conception** et **code plus facile à maintenir** ;
  + **Réduction** des coûts et des délais de **développement** ;
  + **Réduction** des coûts et des délais des **tests** ;

---

## Avantages

- Amélioration de la **communication** dans l'équipe : _revues_.

---

<!-- _class: titre -->
# La revue de code

---

# Principe

- Faire relire le code source par une ou plusieurs personnes autres que celles qui l’ont codé ;
- Réalisées par des _développeurs_ ;
- Éventuellement assistés de _testeurs_ des équipes _Qualité_, _Sûreté de Fonctionnement_, ... ;

---

- Fait partie du **contrôle de la qualité**.
- Adaptable à d'**autres livrables** : _spécifications, modèles, ..._

---

# Objectifs

- Vérifier le respect de certains **standards** de codage :
  + Généraux ;
  + Propres à l'équipe / l'entreprise ;
  + Contraintes sur le système, ... ;
- Identifier des pratiques de programmation **suspectes** ;
- Si **connaissance du métier**, peut détecter des **erreurs fonctionnelles**.

---

# Exemples de vérifications

- _Nombre de commentaires_ ;
- _Code structuré_ ;
- _Constantes_ ;
- _Longueur des fonctions_ ;
- _Décision exprimée simplement_ ;

---

- _Boucles lisibles_ : `while i < max` vs `while i != max` ;
- _Variable initialisée_ ;
- _Division par zéro_ ;
- _Indice sortant du tableau_ ;
- _Fichier non fermé_ ;
- _Fuite mémoire_ ;
- _Erreur de précision_ ;
- _Effet de bord : modifier les paramètres dans la fonction_ ;

---

# Conclusion 

- Bonne idée de la qualité du code source ;
  + Bon niveau de **maintenabilité**.
  + Mais NE montre PAS que le code est correct ;
- **Efficaces** mais **coûteuses** en RH ;
- Pas besoin d'outillage particulier ;

---

<!-- _class: chapter -->
# Behavior-Driven Development

---

## But

- **Conversation** entre _Business_, _Développeurs_ et _Testeurs_ pour décrire les **comportements** du programme à **tester** et à **implémenter**.

---

## Spécification par scénarios (User-Story)

- ⭐ Base : exemples issus de cas d'usages précis ;
- 📜 En découlent les scénarios (exemples) : compréhension commune et précise de ce qui est à faire.
- But :
  - 🧑‍💼 Retranscrire le besoin métier dans le code (idem DDD) : **communication** 💬
  - 👍 La fonctionnalité couvre tous les cas d'usages métiers
  - ✅ Un test valide, implémente et documente le scénario

---

> Given Fred has bought a microwave
> And the microwave costs 100eu
> When we refund the microwave
> Then Fred should be refunded 100eu

---

> **Given (a specific context)**
> **When (some action is carried out)**
> **Then (a particular set of observable consequences _should_ occur)**

---

## Chercher les cas d'erreur ❌

---

Dans quel **contexte** l'événement aboutira à un résultat différent ?

> Given Fred has bought a microwave
> And the microwave costs 100eu
> And the microwave was on 10% discount
> When we refund the microwave
> Then Fred should be refunded 90eu

---

Est-ce vraiment le seul **résultat** à vérifier ?

> Given Fred has bought a microwave
> And the microwave costs 100eu
> When we refund the microwave
> Then the microwave should be added to the stock count.

---

## Du scénario au critère d'acceptation 👍

---

> Given Fred has bought a microwave
> And the microwave costs 100eu
> And the microwave was on 10% discount
> When we refund the microwave
> Then Fred should be refunded 90eu

---

> Given an item was sold with a discount
> When the customer gets a refund
> Then he should only be refunded the discounted price

---

> Items should be refunded at the price at which they were sold.

---

## Comment écrire de bons scénarios ✔️

- 📜 Avoir des noms de tests expressifs : le but de BDD est de documenter le produit depuis les scénarios
- 💡 1 phrase = 1 test
- 💬 Utiliser le langage (ubiquitaire) du métier : voir DDD
  - ⚠️ les experts métier doivent être disponibles !
- ⭐ Le BDD est piloté par la valeur métier (et donc, le développement !)

---

## Atelier 3 Amigos

- 🧑‍💼 _Business_ : **Définit** le problème ou la fonctionnalité attendue, défini la valeur business (Product Owner, Business Analyst, ...) ;
- 🧑‍💻 _Développeurs_ : Suggèrent un **moyen** de corriger ce problème ou de créer la fonctionnalité ;
- 🧑‍🔬 _Utilisateur / Testeur_ : Cherchent les **problèmes** et les failles dans le raisonnement.
- Autre rôles si nécessaire : _UX Designer_, _AdminSys_, …

---

### Communication

- BDD privilégie la **communication** plutôt que l'automatisation et la capture des conversations
  - Les scénarios sont avant tout des exemples d'utilisation plus qu'un engagement contractuel

---

![](https://www.arolla.fr/bdd-dialogue-png/)

<span class="legende">©www.arolla.fr</span>

---

![height:600px](https://blog.octo.com/le-bdd/behavior-driven-development-1-702x1024.webp)

<span class="legende">©blog.octo.com</span>

---

## Outils

- `Gherkin` : syntaxe des scénarios
- Implémentation :
  - `Cucumber` (`JavaScript`, `Ruby`, …)
  - `Behat` (`PHP`)
  - `Behave` (`Python`)
  - `JBehave`, `Spock` (`Java`)

---

### Exemple Gherkin

```gherkin
# from https://behat.org/en/latest/user_guide/gherkin.html

Feature: Some terse yet descriptive text of what is desired
  In order to realize a named business value
  As an explicit system actor
  I want to gain some beneficial outcome which furthers the goal

  Additional text...

  Scenario: Some determinable business situation
    Given some precondition
    And some other precondition
    When some action by the actor
    And some other action
    And yet another action
    Then some testable outcome is achieved
    And something else we can check happens too

  Scenario: A different situation
    ...
```

---

## TDD vs BDD

> TDD is building the thing right.
> BDD is building the right thing.

---

<!-- class: liens -->
# Liens

- <https://alexsoyes.com/bdd-behavior-driven-development/>
- <https://cucumber.io/docs/bdd/>
- [Livre open-source sur le BDD (FR)](https://github.com/Halleck45/livre-developpement-pilote-comportement)
- [WealCome – BDD, DDD, ATDD et TDD expliqués ! (Youtube)](https://www.youtube.com/watch?v=jxBmKvS7lAo)
- [Livre _Software craft: TDD, Clean Code et autres pratiques essentielles (Cyrille Martraire, Arnaud Thiéfaine, Dorra Bartaguiz, Fabien Hiegel, Houssam Fakih)](https://www.decitre.fr/livres/software-craft-9782100825202.html)
- [Behavior Driven Development (slides, Liz Keogh)][LizKeogh]
- [Cucumber – Discovery: The first practice of Behaviour-Driven Development (Youtube)](https://www.youtube.com/watch?v=JuWEQsE7Hlo)
- [Matt Brunt – Behaviour Driven Development and Behat: Telling Stories Through Code (Youtube)](https://www.youtube.com/watch?v=bCLlBgYQoIk)

[LizKeogh]: https://www.slideshare.net/lunivore/behavior-driven-development-11754474

---

<!-- _class: chapter -->
# Stratégies de test

---

# Stratégie de test

- Description **générale** du processus de test :
  + Au niveau produit ;
  + Au niveau de l'organisation.

---

<!-- _class: titre -->
# Stratégies courantes

---

## Stratégie Analytique

- Basée sur l'analyse d'**un facteur** : _exigences, risques, ..._
  + ex : _risques_ => tests conçus et priorisés en fonction du niveau de risque.

---

## Stratégie Basée sur des modèles (MBT)

Tests conçus (manuellement ou automatiquement) à partir d'un **modèle abstrait et haut niveau du SUT** :

- ex : fonction, processus métier, structure interne, caractéristique non-fonctionnelle : fiabilité, ...
- Les outils MBT peuvent automatiser le design des tests fonctionnels (boîte noire) :  _MaTeLo, PragmaDev Studio, Time Partition Testing_.

---

Attention : **MBT == modélisation du SUT** (et non modélisation des tests)

---

### Avantages 1/3

- Tests proches du SUT grâce au modèle :
  + Tests **robustes et bien conçus** ;
  + Bonne couverture ;
  + Réduit le coût des tests (modélisation, maintenance).

---

### Avantages 2/3

- Améliore la **qualité de la documentation** des exigences
  + Plateforme commune designers / testeurs

---

### Avantages 3/3

- Améliore la **qualité du processus** de test.

---

### Inconvénients 1/2

- Adhérence forte au modèle :
  + Nécessite un modèle bien fait

---

### Inconvénients 2/2

- Nécessite une adaptation modèle <-> implémentation par le testeur (_concrétisation_) :
 + Prend du temps ;
 + Nécessite compétences : connaissance métier, _UML_

---

## Stratégie Méthodique

Utilisation systématique d'un **ensemble prédéfini** de tests ou conditions de test :

- Défaillances les plus probables ;
- Caractéristiques de qualité importantes ;
- Normes internes à l'entreprise.

---

## Stratégie Conforme à une norme (ou processus)

Analyse, conception et implémentation de tests basés sur des **règles et normes externes** :

- Normes spécifiques à l'industrie ;
- Normes imposées par ou à l'entreprise ;

---

## Stratégie Dirigée (ou consultative)

Test dicté par les **recommandations** des parties prenantes, des **experts** techniques ou du domaine métier.

- Les experts peuvent être extérieurs

---

## Stratégie Anti-régressions

Objectif : **éviter les régressions** :

- Réutilisation des tests existants ;
- Automatisation des tests de régression ;
- Automatisation des cas nominaux.

---

### Avantages

- Si produit en production mais aucune stratégie existante ;
- Effort limité ;
- Pas de détérioration de la qualité.

---

### Inconvénients

- Qualité des intégrations ?
- Pas d'amélioration de la qualité.

---

## Stratégie Réactive

Tests conçus, implémentés et exécutés immédiatement **à partir des résultats de tests antérieurs** :

- Pas de pré-planification ;
- ex : tests exploratoires.

---

### Avantages

- Tests adaptables si spécifications floues ou changeantes ;
- Coût de spécification de test faible.

---

### Inconvénients

- Peu de process :
  + Fort risque d'oublier des tests ;
  + Tests adaptés uniquement au SUT (pas au besoin)
- Non automatisable.

---

<!-- _class: titre -->
# Métriques de tests

---

À recueillir pendant et après les activités de test :

- Avancement par rapport au **calendrier** et au **budget** prévus ;
- **Qualité actuelle** de l'objet de test ;
- **Pertinence** de l'approche de test ;
- **Efficacité** des activités de test par rapport aux objectifs.

---

# Métriques courantes 1/2

- _% temps de travail_ ou _% nombre_ de cas de tests implémentés.
- _% préparation de l'environnement_ de test.
- _Exécution des cas de test_ : exécutés/non exécutés, réussis/échoués, conditions réussies/échouées.

---

# Métriques courantes 2/2

- _Informations sur les défauts_ : densité , corrigés, taux de défaillance, tests de confirmation.
- _Couverture_ : exigences, User Stories, critères d'acceptation, risques, lignes de code.
- _Degré d'achèvement des tâches_, affectation et utilisation des ressources, et temps passé.
- _Rapport Bénéfice / Coût_ de la découverte d'autres défauts ou de l'exécution de tests supplémentaires.

---

<!-- _class: titre -->
# Indépendance des testeurs

---

# Indépendance des testeurs

Principe : avoir une équipe **dédiée** au test **indépendante** des autres équipes (notamment des développeurs).

---

## Avantages

- Détecter des erreurs différentes par rapport aux développeurs ;
- Vérifier et contester les spécifications et l'implémentation du système.

---

## Inconvénients
 
- Manque de collaboration :
  + Manque d'information pour le testeur ;
  + Retards dans les retours d'information et relation conflictuelle avec l'équipe de développement ;
- Problème de gouvernance : _la qualité ne regarde que les testeurs_ ;
- Testeurs vus comme un goulot d'étranglement responsable des retards ;

---

## En pratique

- Petites structures (startups) et/ou projet peu critiques : cercles de travail pluridisciplinaires ;
- Projet critique et/ou organisation très formelle et/ou beaucoup de ressources : équipe(s) dédiée(s) au test.

---

<!-- class: liens -->

# Références

- Model-based testing : _Kramer, A., Legeard, B. (2016): "Model-Based Testing Essentials - Guide to the ISTQB(R) Certified Model-Based Tester - Foundation Level". John Wiley & Sons, 2016, (ISBN 978-1119130017)_
- <https://blog.octo.com/la-pyramide-des-tests-par-la-pratique-1-5>

---

<!-- _class: chapter -->
# Les techniques de tests

---

<!-- _class: titre -->
# Techniques de test boîte-noire

---

# Partitions d'équivalence

- Données **divisées en partitions** supposées être traitées de la même manière (_Kaner 2013_ et _Jorgensen 2014_) ;
- _1 donnée ne peut être dans 2 partition_ ;
- Partition valide vs invalide ;
- **Partitions invalides à tester séparément** (sinon mélange des erreurs).

---

# Analyse des valeurs limites

- Partitions d'équivalence avec **données numériques ou ordonnées**
- On teste seulement les **valeurs limites des partitions** (_Beizer 1990_) ou (variante) les 3 valeurs juste en-dessous, sur et au-dessus (_Jorgensen 2014_)
- Idée : + de risque d'erreur aux limites (normalement, même algo dans la classe).

---

## Exemple

Soit `1<=n<=5` avec `n` un entier positif :

- 3 partitions _invalide A={6..9} (trop grand), valide B={1..5} , invalide C={0} (trop petit)_
- Beizer : `{5,6}` et `{0,1}`
- Jorgensen : `{4,5,6}` et `{0,1,2}`

---

# Test de tables de décision

- Chaque ligne identifie des **conditions** (entrées) (en haut dans le tableau) ou des **sorties** (en bas dans le tableau) du système ;
- Chaque colonne : **combinaison de conditions** ;
- Permet d'identifier les **combinaisons importantes**.
- _Couverture minimale courante : couvrir toutes les combinaisons_

---

# Test des transitions d'état

- Basés sur les événements (ou séquences d'événements) créant un **changement d'état** dans le système ;
- Voir [un exemple de la taverne du testeur][tests-transition-etat]

---

- Si **tableau** : montre toutes les **transitions valides** et les **transitions potentiellement invalides** entre les états d'un système (et les événements, les conditions de garde et les actions résultantes pour les transitions valides).
- Si **diagramme** de transition d'états : montre **uniquement les transitions valides**.

---

- Usage :
  + _Applications basées sur des menus_ ;
  + _Logiciel embarqué_ ;
  + _Métier modélisable par états (aviation, ...)_.

---

# Test des cas d'utilisation

- Tests utilisant des _cas d'utilisation_ : spécifient un **comportement** qu'un système peut accomplir **en collaboration** avec un ou plusieurs acteurs (humains, dépendance externe, autres composants, ...) (_UML 2.5.1 2017_)
- _Les interactions peuvent être représentées graphiquement par des flux de travail, des diagrammes d'activités ou des modèles de processus métier._

---

<!-- _class: titre -->
# Techniques de test boîte-blanche

---

# Test et couverture des instructions

- Exerce les **instructions exécutables** dans le code (lignes de code).
- _Couverture de test : lignes de code exécutées par le test / lignes de code total_.
- Aide à **détecter des zones non testées** par d'autres types de tests.

---

# Test et couverture des décisions

- Exerce les **décisions possibles** dans le code.
  + ex : `if` et `else`
- _Couverture de test : décisions testées / décisions totales_.
- Aide à trouver des **conditions pas totalement testées**.

---

<!-- _class: titre -->
# Techniques de test basées sur l'expérience

---

# Estimation d'erreur

- _Comment l'application a-t-elle fonctionné avant ?_
- _Quels types d'erreurs les développeurs ont-ils tendance à faire ?_
- _Quelles défaillances se sont produites dans d'autres applications ?_

---

- Tests écrits depuis une **liste estimant les erreurs** ;
- Utilise l'**expérience** et les **données recueillies**.

---

# Tests exploratoires

- Tests **informels** réalisés "**en live**" ;
- Utiles si spécifications peu adaptées au test ;
- Rapides à mettre en œuvre.
  + ex : _test de session (temps fixe, objectifs définis, réalisation libre)_.
- Souvent **combinés à d'autres types** de tests.

---

# Tests basés sur des checklists

- Liste d'**éléments à vérifier** ou ensemble de critères pour valider le produit ;
- Souvent **modifiée pendant l'analyse** mais parfois checklist _classique_ réutilisable ;
- _Utile si base de test existante peu formelle_.

---

<!-- _class: titre -->
# Choix des techniques de test

---

# Exemples de facteurs 1/3

- Type de composant ou de système ;
- Complexité du composant ou des systèmes ;
- Normes réglementaires ;
- Exigences client ou contractuelles ;

---

# Exemples de facteurs 2/3

- Niveaux de risque ;
- Types de risques ;
- Objectifs du test ;
- Documentation disponible ;
- Connaissances et compétences des testeurs ;

---

# Exemples de facteurs 3/3

- Outils disponibles ;
- Temps et budget ;
- Modèle de cycle de vie du développement logiciel ;
- Utilisation prévue du logiciel ;
- Expérience des techniques sur le composant ou le système à tester ;
- Types de défauts attendus dans le composant ou le système.

[tests-transition-etat]: https://latavernedutesteur.fr/2018/10/02/techniques-basees-sur-les-specifications-4-7-les-tests-de-transition-detat/

