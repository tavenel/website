---
title: Exercice Tests qualité logicielle et architecture SI
---

## Contexte

Une entreprise de commerce en ligne souhaite refondre son système d’information afin de supporter une forte croissance de son activité.

Le nouveau SI est constitué de plusieurs composants :

- une application Web et mobile ;
- une API exposée aux applications clientes ;
- un service de gestion des commandes ;
- un service de paiement faisant appel à un prestataire externe ;
- un service de gestion des stocks ;
- une base de données ;
- un système de messagerie asynchrone permettant la communication entre certains services ;
- une chaîne CI/CD permettant de déployer plusieurs fois par jour.

L'architecture retenue est une architecture distribuée de type microservices.

Le responsable qualité vous demande de construire une stratégie de tests permettant de vérifier que le système respecte les exigences de qualité attendues.

Les principales exigences sont les suivantes :

- E1 : Une commande valide doit pouvoir être créée et enregistrée correctement.
- E2 : Le montant payé doit être identique au montant de la commande.
- E3 : 95 % des requêtes API doivent répondre en moins de 500 ms en charge nominale.
- E4 : Le système doit supporter 2 000 utilisateurs simultanés.
- E5 : Une indisponibilité temporaire du service de paiement ne doit pas entraîner de perte de commande.
- E6 : Les données personnelles des clients ne doivent pas être accessibles à un utilisateur non autorisé.
- E7 : Une nouvelle version doit pouvoir être déployée sans interruption de service.
- E8 : Après une modification du service de gestion des stocks, les fonctionnalités existantes doivent continuer à fonctionner.
- E9 : Une anomalie dans un service doit pouvoir être détectée et diagnostiquée rapidement en production.
- E10 : Le système doit pouvoir évoluer pour supporter une multiplication par 10 du nombre de commandes sans remise en cause majeure de l'architecture.

### Rappels sur la norme ISO 25010

Le modèle ISO/IEC 25010 définit les principales caractéristiques permettant d'évaluer la qualité d'un produit logiciel.

Les 8 caractéristiques de qualité :

| # | Caractéristique | Question clé | Exemples d'indicateurs |
| --- | ----------------- | -------------- | ------------------------ |
| 1 | Adéquation fonctionnelle | Le logiciel fait-il correctement ce qu'il doit faire ? | Couverture des exigences, taux d'erreurs fonctionnelles, exactitude des résultats |
| 2 | Performance et efficacité | Le système est-il suffisamment rapide et efficace ? | Temps de réponse, p95/p99, débit, CPU, mémoire, utilisateurs simultanés |
| 3 | Compatibilité | Le logiciel fonctionne-t-il correctement avec son environnement ? | Taux d'interopérabilité, incidents d'intégration, compatibilité API/OS/navigateurs |
| 4 | Utilisabilité | Le logiciel est-il facile à comprendre et à utiliser ? | Taux de réussite des tâches, temps d'apprentissage, erreurs utilisateur, satisfaction, SUS |
| 5 | Fiabilité | Le système fonctionne-t-il de manière stable et continue ? | Disponibilité, MTBF, MTTR, taux d'erreur, taux d'incidents |
| 6 | Sécurité | Le système protège-t-il correctement les données et les fonctions ? | Vulnérabilités, taux d'échec des contrôles d'accès, incidents de sécurité, couverture des contrôles |
| 7 | Maintenabilité | Le logiciel est-il facile à analyser, modifier et tester ? | Complexité cyclomatique, couverture de tests, temps de correction, dette technique, couplage |
| 8 | Portabilité | Le logiciel peut-il être transféré vers un autre environnement ? | Effort de migration, temps d'installation, nombre d'environnements supportés, taux de succès du déploiement |

Le modèle peut être utilisé selon la chaîne : Attribut de qualité → Sous-caractéristique → Indicateur → Test / mesure

Exemples :

| Besoin | ISO 25010 | Indicateur Test / mesure |
| -------- | ----------- | -------------------------- |
| Répondre rapidement | Performance | p95 < 500 ms Test de charge |
| Supporter 2 000 utilisateurs | Performance | Nombre max d'utilisateurs simultanés Test de charge / stress |
| Ne pas perdre une commande | Fiabilité | 0 perte lors d'une panne Test de résilience |
| Empêcher un accès non autorisé | Sécurité | 100 % des accès interdits rejetés Test de sécurité |
| Éviter les régressions | Maintenabilité | Taux de réussite de la suite de régression Tests de régression |
| Fonctionner avec un SI externe | Compatibilité | Taux de succès des échanges Tests d'intégration / contrats |
| Faciliter l'utilisation | Utilisabilité | Taux de réussite d'une tâche Tests utilisateurs |
| Faciliter l'évolution | Maintenabilité | Temps nécessaire pour modifier une fonctionnalité Analyse + tests |

ISO/IEC 25010 définit un modèle de qualité, pas une liste universelle de KPI.

Les indicateurs doivent être choisis en fonction :

- du contexte métier ;
- des risques ;
- des exigences de qualité ;
- de l'architecture ;
- du niveau de criticité du système.

On cherche ainsi à établir des éléments mesurables : « Le système atteint un p95 de 420 ms sous 2 000 utilisateurs simultanés et présente un taux d'erreur inférieur à 0,1 %. »

## Partie A - Identifier les attributs de qualité

À partir du modèle ISO/IEC 25010, identifiez le ou les attributs de qualité principalement concernés par chacune des exigences E1 à E10.

Pour chaque exigence, indiquez :

- l'attribut de qualité ISO 25010 concerné ;
- éventuellement le sous-attribut pertinent ;
- une justification de deux ou trois phrases.

Vous pourrez notamment mobiliser les caractéristiques suivantes :

- adéquation fonctionnelle ;
- performance et efficacité ;
- compatibilité ;
- utilisabilité ;
- fiabilité ;
- sécurité ;
- maintenabilité ;
- portabilité.

Question complémentaire : certaines exigences peuvent-elles être associées à plusieurs caractéristiques de qualité ? Donnez deux exemples et expliquez pourquoi.

## Partie B - Relier les types de tests aux qualités recherchées

L'équipe dispose des types de tests suivants :

- tests unitaires ;
- tests d'intégration ;
- tests de composants ;
- tests end-to-end ;
- tests fonctionnels ;
- tests de régression ;
- tests de performance ;
- tests de charge ;
- tests de stress ;
- tests de sécurité ;
- tests de robustesse/résilience ;
- tests d'acceptation ;
- tests de compatibilité ;
- tests d'installabilité/déploiement ;
- tests exploratoires.

Construisez une matrice Tests × Attributs de qualité.

Pour chaque type de test, indiquez :

- les attributs de qualité qu'il permet principalement d'évaluer ;
- les attributs qu'il peut contribuer à évaluer indirectement ;
- son niveau dans la pyramide de tests ;
- son coût relatif ;
- sa fréquence souhaitable dans une chaîne CI/CD.

Vous devrez être capables de justifier les cases les plus importantes de votre matrice.

## Partie C - Étude de scénarios

Pour chacun des scénarios suivants, choisissez au moins deux types de tests complémentaires et expliquez pourquoi.

### Scénario 1 - Paiement

Le service de paiement est modifié. Il communique avec un prestataire externe.

On souhaite vérifier que :

    « Une commande payée 149,90 € ne peut jamais être enregistrée comme ayant été payée 199,90 €. »

Questions :

- Quels tests réalisez-vous ?
- À quel niveau les réalisez-vous ?
- Quelle caractéristique ISO 25010 cherchez-vous principalement à vérifier ?
- Pourquoi un test unitaire seul ne suffit-il pas ?

### Scénario 2 - Performance

Une campagne publicitaire devrait provoquer une augmentation importante du trafic.

Le système doit supporter :

    2 000 utilisateurs simultanés avec un temps de réponse inférieur à 500 ms pour 95 % des requêtes API.

Questions :

- Quels types de tests mettez-vous en place ?
- Quelle différence faites-vous entre test de charge, test de stress et test de performance ?
- Quels indicateurs mesurez-vous ?
- Quelle caractéristique ISO 25010 est principalement concernée ?

### Scénario 3 - Résilience

Le service de paiement devient indisponible pendant cinq minutes.

Le métier exige que les commandes initiées pendant cette période ne soient pas perdues et puissent être traitées ultérieurement.

Questions :

- Quel type de test permet de vérifier ce comportement ?
- Quelles autres dépendances pourriez-vous volontairement rendre indisponibles ?
- Quels mécanismes architecturaux ce test permet-il indirectement de valider ?
- Quel lien faites-vous avec la fiabilité selon ISO 25010 ?

### Scénario 4 - Sécurité

Un utilisateur authentifié avec le rôle CLIENT tente d'accéder à une API réservée au rôle ADMIN.

Questions :

- Quels tests mettez-vous en place ?
- Pourquoi les tests fonctionnels classiques ne suffisent-ils pas nécessairement ?
- Quelles propriétés de sécurité cherchez-vous à vérifier ?
- Comment intégrer ces tests dans la CI/CD ?

### Scénario 5 - Évolution

L'équipe modifie le calcul des frais de livraison.

Le code modifié ne concerne apparemment que le service de commande, mais ce service communique avec le stock, le paiement et le système de notification.

Questions :

- Quels niveaux de tests doivent être exécutés avant mise en production ?
- Quelle place donner aux tests de régression ?
- Comment limiter le coût des tests end-to-end ?
- Quel attribut ISO 25010 est particulièrement concerné par cette problématique ?

## Partie D - Tests et architecture

Le CTO affirme :

    « Les tests sont une activité de l'équipe de développement. L'architecture n'a rien à voir avec la stratégie de test. »

Discutez cette affirmation.

Votre réponse devra présenter au moins quatre exemples montrant comment un choix architectural influence :

- la testabilité ;
- le coût des tests ;
- le niveau auquel les tests peuvent être réalisés ;
- la capacité à automatiser les tests ;
- la qualité observable du système.

Vous pourrez notamment discuter :

- architecture monolithique vs microservices ;
- communication synchrone vs asynchrone ;
- APIs bien définies ;
- injection de dépendances ;
- bases de données partagées vs isolées ;
- observabilité ;
- architecture hexagonale ;
- gestion des événements ;
- résilience et tolérance aux pannes.

## Partie E - Mise en situation : construire une stratégie de test

Vous êtes architecte logiciel.

Votre équipe dispose de 100 heures de test par sprint.

Vous devez proposer une stratégie permettant de maximiser la confiance dans la qualité du système sans exécuter systématiquement tous les tests end-to-end.

Proposez une répartition indicative entre :

- tests unitaires ;
- tests de composants ;
- tests d'intégration ;
- tests API ;
- tests end-to-end ;
- tests de performance ;
- tests de sécurité ;
- tests de résilience.

Votre proposition doit être accompagnée d'une justification.

Attention : il n'existe pas nécessairement une unique répartition correcte. L'objectif est de justifier les arbitrages.

## Question de synthèse

Complétez le raisonnement suivant :

    Un attribut de qualité n'est pas directement « testé » par un unique test. Il est généralement …

Expliquez ensuite, à l'aide d'un exemple, comment une même caractéristique ISO 25010 peut nécessiter plusieurs niveaux de tests complémentaires.

Enfin, expliquez pourquoi :

    « 90 % de couverture de code » ne signifie pas nécessairement « 90 % de qualité du logiciel ».

:::correction

# Corrigé

## Partie A - Exigences et attributs ISO/IEC 25010

| Exigence | Caractéristique ISO 25010 | Sous-caractéristique | Justification |
| --- | --- | --- | --- |
| E1 — Création correcte d'une commande | Adéquation fonctionnelle | Exactitude fonctionnelle | Le système doit produire le résultat attendu lorsqu'une commande valide est créée. |
| E2 — Montant payé conforme | Adéquation fonctionnelle | Exactitude fonctionnelle | Le résultat métier doit être correct et cohérent entre commande et paiement. La sécurité et la fiabilité peuvent également être concernées. |
| E3 — 95 % \< 500 ms | Performance et efficacité | Comportement temporel | L'exigence porte directement sur le temps de réponse du système. |
| E4 — 2 000 utilisateurs simultanés | Performance et efficacité | Capacité | Le système doit supporter une charge simultanée donnée. |
| E5 — Pas de perte de commande lors d'une panne | Fiabilité | Tolérance aux fautes / récupérabilité | Le système doit continuer à assurer un service acceptable malgré une défaillance externe et récupérer correctement. |
| E6 — Protection des données personnelles | Sécurité | Confidentialité / contrôle d'accès | Seules les personnes autorisées doivent pouvoir accéder aux informations sensibles. |
| E7 — Déploiement sans interruption | Fiabilité + Maintenabilité | Disponibilité / modifiabilité | L'architecture et le processus de déploiement doivent permettre une évolution sans interruption du service. |
| E8 — Absence de régression | Maintenabilité | Stabilité / testabilité | Une modification doit pouvoir être effectuée sans dégrader les fonctionnalités existantes. |
| E9 — Détection et diagnostic rapide | Fiabilité + Maintenabilité | Disponibilité / analysabilité | Le système doit permettre de détecter et analyser rapidement les défaillances. |
| E10 — Croissance ×10 | Performance et efficacité + Maintenabilité | Capacité / modifiabilité | L'architecture doit pouvoir évoluer pour absorber la croissance sans remise en cause majeure. |

### Remarque

Une exigence peut parfaitement relever de plusieurs caractéristiques.
Par exemple, **E5** ne relève pas uniquement de la fiabilité : la sécurité peut intervenir si la reprise après incident doit préserver l'intégrité des données.
De même, **E7** peut mobiliser à la fois la fiabilité, la maintenabilité et, selon le périmètre retenu, la portabilité ou la compatibilité.
L'objectif n'est donc pas de faire mémoriser une correspondance « 1 exigence = 1 attribut », mais de faire comprendre que les attributs de qualité sont **multidimensionnels**.

## Partie B - Matrice Tests × Qualité

Une réponse possible est la suivante.

 | Type de test | Adéquation fonctionnelle | Performance | Fiabilité | Sécurité | Maintenabilité | Compatibilité |
| --- | --- | --- | --- | --- | --- | --- |
| Tests unitaires | ● | ○ | ○ | ○ | ● | — |
| Tests de composants | ● | ○ | ● | ○ | ● | — |
| Tests d'intégration | ● | ○ | ● | ○ | ○ | ● |
| Tests API | ● | ○ | ● | ● | ○ | ● |
| Tests end-to-end | ● | ○ | ● | ○ | ○ | ● |
| Tests fonctionnels | ● | — | ○ | ○ | — | ○ |
| Tests de régression | ● | ○ | ● | ○ | ● | ○ |
| Tests de performance | — | ● | ○ | — | — | — |
| Tests de charge | — | ● | ● | — | — | — |
| Tests de stress | — | ● | ● | — | — | — |
| Tests de sécurité | — | — | ○ | ● | ○ | — |
| Tests de résilience | — | ○ | ● | ○ | ○ | — |
| Tests d'acceptation | ● | ○ | ○ | ○ | — | ○ |
| Tests de compatibilité | — | ○ | ○ | — | — | ● |
| Tests de déploiement | — | — | ● | ○ | ● | ● |
| Tests exploratoires | ● | ○ | ○ | ○ | ○ | ○ |

### Interprétation

Cette matrice n'est pas une vérité absolue.

Par exemple :

- un test unitaire peut vérifier un comportement de sécurité dans une fonction d'autorisation ;
- un test de sécurité peut révéler une faiblesse ayant un impact sur la fiabilité ;
- un test de charge peut révéler un problème de disponibilité ;
- un test end-to-end peut détecter un problème d'intégration mais également fournir une information sur la performance.

La question importante est donc :

> **« Quelle propriété cherche-t-on à démontrer avec ce test ? »**

plutôt que :

> **« À quelle catégorie appartient ce test ? »**

## Pyramide de tests

Une stratégie cohérente privilégie généralement un grand nombre de tests rapides et ciblés, complétés par un nombre plus limité de tests coûteux.

### Niveau 1 - Tests unitaires

- très rapides ;
- nombreux ;
- exécutables à chaque commit ;
- permettent de vérifier les règles métier isolées ;
- coût de maintenance relativement faible lorsqu'ils sont bien conçus.

Exemple :

```
calculateTotal(order)
    → 3 articles × 20 €
    → frais de livraison 5 €
    → total attendu = 65 €
```

### Niveau 2 - Tests de composants / API

Ils permettent de vérifier un service dans un environnement relativement contrôlé.

Exemple :

```
OrderService
    → POST /orders
    → vérification de la validation
    → vérification de la persistance
    → vérification des événements produits
```

Ils constituent souvent un excellent compromis entre rapidité et représentativité.

### Niveau 3 - Tests d'intégration

 Ils vérifient les interactions entre composants réels :

```
Order Service
      ↓
Database
      ↓
Stock Service
      ↓
Message Broker
```

 Ils permettent notamment de détecter les problèmes de contrats, de sérialisation, de transactions ou de communication.

### Niveau 4 - Tests end-to-end

Ils reproduisent un scénario utilisateur complet :

```
Client
  ↓
Web/API
  ↓
Order
  ↓
Stock
  ↓
Payment
  ↓
Notification
```

Ils offrent une forte confiance sur le fonctionnement global mais sont généralement plus :

- lents ;
- fragiles ;
- coûteux à maintenir ;
- difficiles à diagnostiquer.

Ils doivent donc être utilisés de manière ciblée.

## Partie C - Scénario 1 : paiement

### Question 1 - Quels tests ?

Une réponse solide combine plusieurs niveaux :

#### Tests unitaires

 Tester le calcul et les règles métier :

```
Commande = 149,90 €
Paiement attendu = 149,90 €
```

 On peut tester également :

- arrondis ;
- devises ;
- remises ;
- frais ;
- cas limites.

#### Tests d'intégration

Vérifier que le service de commande et le service de paiement échangent correctement les données.

Exemple :

```
OrderService
    ↓ 149,90 €
PaymentService
    ↓
Provider
```

#### Tests de contrat/API

Vérifier que le contrat entre les services reste respecté :

```
{
  "orderId": "123",
  "amount": 149.90,
  "currency": "EUR"
}
```

#### Test end-to-end

Vérifier le scénario complet :

```
Création commande
      ↓
Calcul montant
      ↓
Paiement
      ↓
Confirmation
      ↓
Commande "PAYÉE"
```

### Question 2 - ISO 25010

La caractéristique principale est : **Adéquation fonctionnelle → exactitude fonctionnelle.**

Mais la sécurité et la fiabilité peuvent également être concernées.

### Question 3 - Pourquoi un test unitaire ne suffit-il pas ?

Parce qu'un test unitaire peut démontrer :

> « La fonction de calcul du montant est correcte. »

mais pas :

> « Le montant transmis au prestataire est correct et le résultat du paiement est correctement répercuté dans le système. »

Il faut donc tester les **interactions entre composants**.

## 5 Scénario 2 - Performance

L'exigence est :

> 2 000 utilisateurs simultanés et 95 % des requêtes sous 500 ms.

### Test de performance

Mesurer :

- temps de réponse ;
- débit ;
- consommation CPU ;
- mémoire ;
- I/O ;
- latence ;
- taux d'erreur.

### Test de charge

Faire progressivement monter la charge :

```
100 utilisateurs
      ↓
500
      ↓
1000
      ↓
1500
      ↓
2000
```

On vérifie notamment que les objectifs sont toujours respectés à 2 000 utilisateurs.

### Test de stress

Dépasser volontairement la charge nominale :

```
2000 → 2500 → 3000 → 4000 ...
```

L'objectif n'est plus seulement de vérifier le SLA mais d'identifier le comportement du système lorsqu'il atteint ses limites.

On cherche notamment :

- le point de saturation ;
- le comportement en dégradation ;
- le taux d'erreur ;
- la récupération après diminution de la charge.

### Indicateurs

On pourra mesurer :

- p50 ;
- p95 ;
- p99 ;
- throughput ;
- taux d'erreur ;
- CPU ;
- mémoire ;
- saturation des bases de données ;
- latence réseau.

### ISO 25010

La caractéristique principalement concernée est :

**Performance et efficacité → comportement temporel + capacité.**

## Scénario 3 — Résilience

Le service de paiement devient indisponible pendant cinq minutes.

 On réalise des **tests de résilience / fault injection**.

 Par exemple :

```
Order Service
     ↓
Payment Service
     X
  indisponible
```

 On vérifie que :

- la commande n'est pas perdue ;
- elle est correctement enregistrée dans un état intermédiaire ;
- elle peut être retraitée ;
- aucune double facturation n'est créée ;
- le système récupère lorsque le paiement revient.

### Autres pannes possibles

On peut injecter :

- timeout ;
- erreur HTTP 500 ;
- réseau indisponible ;
- base de données indisponible ;
- message perdu ;
- message dupliqué ;
- message reçu deux fois ;
- réponse très lente ;
- indisponibilité du broker.

### Mécanismes architecturaux testés

 Ces tests permettent notamment de vérifier :

- retry ;
- timeout ;
- circuit breaker ;
- files de messages ;
- persistance des événements ;
- idempotence ;
- mécanismes de reprise ;
- transactions distribuées ou mécanismes de compensation.

### ISO 25010

**Fiabilité**, notamment :

- tolérance aux fautes ;
- récupérabilité ;
- disponibilité.

## Scénario 4 - Sécurité

Un utilisateur `CLIENT` tente d'appeler :

```
GET /admin/users
```

### Tests

Il faut notamment mettre en place des tests :

- d'authentification ;
- d'autorisation ;
- de contrôle d'accès ;
- de gestion des rôles ;
- de validation des tokens ;
- de non-divulgation d'informations.

Exemple :

```
CLIENT
  ↓
GET /admin/users
  ↓
403 Forbidden
```

et :

```
ADMIN
  ↓
GET /admin/users
  ↓
200 OK
```

### Pourquoi les tests fonctionnels ne suffisent-ils pas ?

Une fonctionnalité peut fonctionner correctement pour un utilisateur autorisé tout en présentant une vulnérabilité pour un utilisateur non autorisé.

Exemple :

```
Test fonctionnel :
ADMIN → GET /admin/users → OK

Vulnérabilité potentielle :
CLIENT → GET /admin/users → OK
```

Le premier test est vert alors que le système reste vulnérable.

### CI/CD

On peut intégrer :

- tests automatisés d'autorisation ;
- SAST ;
- DAST ;
- analyse des dépendances ;
- scans de configuration ;
- tests d'API sécurisés.

La sécurité devient ainsi une activité continue plutôt qu'une phase uniquement située avant la mise en production.

## Scénario 5 - Évolution

Le calcul des frais de livraison est modifié.

### Tests unitaires

Vérifier la nouvelle règle métier.

### Tests de composants

Vérifier le service de commande dans son ensemble.

### Tests d'intégration

Vérifier les interactions avec :

- stock ;
- paiement ;
- notification.

### Tests end-to-end ciblés

Tester les parcours critiques :

```
Commande
→ calcul livraison
→ paiement
→ stock
→ confirmation
```

### Tests de régression

Vérifier que les fonctionnalités existantes continuent à fonctionner.

Pourquoi les tests de régression ? Parce qu'une modification locale peut avoir des effets non locaux dans un SI distribué.

```
Modification
    ↓
Order Service
    ↓
API / événements
    ↓
Payment / Stock / Notification
```

### Comment limiter le coût des tests E2E ?

 On peut utiliser :

- tests unitaires nombreux ;
- tests de composants ;
- tests de contrats ;
- tests d'intégration ciblés ;
- sélection automatique des tests impactés ;
- quelques scénarios E2E critiques.

 L'objectif est de déplacer autant que possible la détection des erreurs vers des niveaux **plus rapides et plus faciles à diagnostiquer**.

### ISO 25010

La caractéristique principalement concernée est la **maintenabilité**, notamment :

- modifiabilité ;
- testabilité ;
- stabilité.

## Partie D - Tests et architecture

L'affirmation :

> « Les tests sont une activité de l'équipe de développement. L'architecture n'a rien à voir avec la stratégie de test. »

est incorrecte.

L'architecture influence directement la **testabilité** du système et donc le coût et l'efficacité de la stratégie de test.

### Exemple 1 - Couplage

Architecture fortement couplée :

```
A → B → C → D → Database
```

Pour tester A, il faut potentiellement démarrer toute la chaîne.

Architecture découplée :

```
A → interface B
```

B peut être remplacé par un mock ou un stub.

**Conséquence :** les tests sont plus rapides et plus isolés.

### Exemple 2 - API et contrats explicites

Des APIs clairement définies permettent de mettre en place :

- tests de contrat ;
- tests d'intégration ciblés ;
- mocks ;
- tests automatisés.

Une architecture basée sur des interfaces explicites facilite donc la vérification indépendante des composants.

### Exemple 3 - Injection de dépendances

Avec une dépendance codée en dur :

```
OrderService
    ↓
PaymentProvider réel
```

les tests nécessitent le prestataire réel ou une infrastructure complexe.

Avec injection de dépendances :

```
OrderService
    ↓
PaymentInterface
    ↑
    ├── RealPaymentProvider
    └── FakePaymentProvider
```

le composant peut être testé isolément.

### Exemple 4 - Base de données partagée

Si tous les microservices utilisent la même base :

```
Service A ─┐
Service B ─┼→ Database
Service C ─┘
```

les tests deviennent plus interdépendants.

Avec des données et responsabilités mieux isolées, les tests peuvent être davantage ciblés.

### Exemple 5 - Architecture événementielle

Une architecture asynchrone introduit de nouveaux comportements à tester :

- duplication ;
- perte ;
- ordre des messages ;
- retard ;
- rejeu ;
- idempotence.

Elle nécessite donc une stratégie de test spécifique.

### Exemple 6 - Observabilité

Une architecture dotée de :

- logs structurés ;
- métriques ;
- traces distribuées ;
- correlation IDs ;

facilite fortement le diagnostic des échecs.

Un test qui échoue est alors plus facile à analyser.

On peut donc établir le lien :

```
Architecture
     ↓
Testabilité
     ↓
Automatisation
     ↓
Feedback rapide
     ↓
Maintenabilité
```

## Partie E - Répartition des 100 heures

Il n'existe pas de répartition unique.

Une proposition raisonnable pourrait être :

 | Type de test | Temps indicatif | Justification |
| --- | --- | --- |
| Tests unitaires | 30 h | Nombreux, rapides, feedback très précoce |
| Tests de composants | 15 h | Bon compromis entre isolation et réalisme |
| Tests API / contrats | 15 h | Vérification des interfaces entre services |
| Tests d'intégration | 15 h | Vérification des interactions réelles |
| Tests E2E | 8 h | Parcours critiques uniquement |
| Tests performance/charge | 7 h | Vérification des exigences de capacité |
| Tests sécurité | 7 h | Vérification automatisée des contrôles critiques |
| Tests résilience | 3 h | Scénarios de panne ciblés |
| **Total** | **100 h** | |

Cette répartition doit être adaptée au contexte.

Par exemple, une application bancaire pourrait consacrer davantage de ressources à la sécurité, tandis qu'un système temps réel pourrait investir davantage dans la performance.

 Le but n'est pas d'avoir beaucoup de tests mais **d'obtenir suffisamment de preuves de qualité au moindre coût et avec un feedback suffisamment rapide.**

## Partie F - Question de synthèse

 Une formulation attendue est :

 > **Un attribut de qualité n'est pas directement « testé » par un unique test. Il est généralement évalué par un ensemble de tests, de métriques et d'observations réalisés à différents niveaux du système.**

### Exemple : fiabilité

Pour évaluer la fiabilité, on peut combiner :

```
Tests unitaires
      ↓
Tests d'intégration
      ↓
Tests E2E
      ↓
Tests de charge
      ↓
Tests de résilience
      ↓
Tests en production / observabilité
```

Chaque niveau répond à une question différente.

 | Test | Question |
| --- | --- |
| Unitaire | La logique de gestion d'erreur est-elle correcte ? |
| Intégration | Les composants coopèrent-ils correctement en cas d'erreur ? |
| E2E | Le parcours métier reste-t-il fonctionnel ? |
| Charge | Le système reste-t-il fiable sous charge ? |
| Résilience | Que se passe-t-il lorsqu'une dépendance tombe ? |
| Production | Les incidents peuvent-ils être détectés et diagnostiqués ? |

## Pourquoi 90 % de couverture ne signifie-t-il pas 90 % de qualité ?

La couverture de code mesure principalement **quelles portions du code sont exécutées par les tests**.

Elle ne démontre pas nécessairement :

- que les exigences métier sont correctes ;
- que les résultats sont corrects ;
- que les interactions entre services fonctionnent ;
- que le système supporte la charge ;
- que les contrôles de sécurité sont efficaces ;
- que le système résiste aux pannes ;
- que l'expérience utilisateur est satisfaisante.

Exemple :

```
if (amount > 0) {
    payment();
}
```

Un test peut exécuter cette ligne et augmenter la couverture à 100 %, mais ne vérifier qu'un montant positif arbitraire.

Il pourrait ne jamais tester :

- 0 € ;
- montant négatif ;
- dépassement ;
- devise incorrecte ;
- double paiement ;
- timeout du prestataire ;
- réponse frauduleuse ;
- paiement concurrent.

On peut donc avoir 100 % de couverture de code et une couverture insuffisante des risques.

## Synthèse

```
                    EXIGENCES MÉTIER
                           │
                           ▼
                  RISQUES QUALITÉ
                           │
                           ▼
                  ISO 25010
                           │
                           ▼
                 STRATÉGIE DE TEST
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       Unitaire       Intégration          E2E
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    MÉTRIQUES / PREUVES
                           │
                           ▼
                  DÉCISION D'ARCHITECTURE
                           │
                           ▼
                  QUALITÉ DU SYSTÈME
```

Le point essentiel est que **les tests ne sont pas simplement une activité de détection de bugs**. Ils constituent un moyen de produire des **preuves concernant les attributs de qualité**, et ces preuves permettent d'évaluer les choix d'architecture et de réduire les risques du SI.

Ainsi :

> **Architecture → influence la qualité → influence la testabilité → influence le coût des tests → influence la stratégie CI/CD.**

Et réciproquement, les difficultés rencontrées lors des tests peuvent révéler des **problèmes d'architecture**.
:::
