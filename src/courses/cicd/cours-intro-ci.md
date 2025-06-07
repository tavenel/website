---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Introduction à l'intégration continue
layout: '@layouts/CoursePartLayout.astro'
---

# Problèmes courants

- Lenteur des déploiements manuels
- Erreurs humaines fréquentes au déploiement :
  - configurations incorrectes
  - oublis de fichiers, …
  - besoin d'interventions d'urgence
- Modifications difficiles à suivre :
  - quelle version en production ?
  - quels changements sur la production ?
  - conflits de dépendances
- Tests non systématiques
- Pas de communication entre dev et ops

---

# Intégration continue

> Ensemble de pratiques consistant à vérifier que chaque modification du code source ne produit pas de régression

---

> Continuous Integration is a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily – leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop cohesive software more rapidly. Martin Fowler, ThoughtWorks Chief Scientist

---

# Shift Left

La CI se positionne dans une stratégie **Shift Left** :

- Pratique qui consiste à intégrer les tests et la gestion des connaissances dans les étapes initiales du développement logiciel (plutôt que tardivement dans le processus de production).
- Objectif : détecter et corriger les bugs et les erreurs dès les premières étapes du développement

---

# Avantages de l'intégration continue

---

# Feedback loop réduite

- Spécifications
  + Les spécifications sont validées plus tôt
- Build
  + Le build est testé plus tôt
- Erreurs
  + Les erreurs sont détectées plus tôt
- Intégration
  + L'intégration est testée plus tôt

---

# Facilite le travail collaboratif

Les changements concurrents sont validés contre une éventuelle régression

---

# Inconvénients de l'intégration continue

---

- Demande de grosses ressources humaines à la mise en place et matérielles à l'usage
  + Mais le gain est souvent vite compensé par les erreurs en moins à corriger !
- Peut être compliqué sur de gros changements : la CI nécessite d’intégrer souvent les changements sur le serveur…
  + … ce qui peut aussi être un avantage pour vérifier tôt la compatibilité !
+ Peu adapté à certains environnements où les spécifications changent souvent (Proof of Concept, Recherche, ...)

---

- Respecter une méthodologie stricte d’intégration continue demande beaucoup de rigueur
  + Il peut être nécessaire de vérifier le respect de ces méthodes, manuellement ou automatiquement

Le principal défaut est souvent humain !

---
layout: section
---

# Les grands principes de l'intégration continue

- Centralisation du code
- Commit réguliers
- Automatisation des build
- Compilations auto-testantes

---

# Centralisation du code : le gestionnaire de versions

- Segmente les modifications du code source en `commits` et les identifie par des ID de commit.
- Garantit l'intégrité : permet le partage fiable des modifications entre tous les développeurs.
- Référence du contrôle qualité : toute métrique d’intégration continue est faite contre un commit.

---

Exemples : `git`, `mercurial`, `svn` et leurs serveurs hébergés : `github`, `bitbucket`, `gitlab`, ...

Certains gestionnaires de versions permettent d'isoler du tronc commun les modifications dont la qualité n'est pas encore suffisante : branches `git`, ...

---

# Commit réguliers

- But intégration continue : réduire au maximum le temps de feedback.
  + Intégrer les plus petits changements possibles.
  + Intégrer le plus souvent possible.

En principe : intégration continue si `> 1 intégration (commit) par jour`.

---

# Automatisation des build

Nécessaire pour une analyse et validation automatique de la qualité :

- Pas d'intervention manuelle sur l'intégration continue.
- Mais processus manuel possible, par exemple si changements critiques et concurrents entre 2 développeurs.
  + Ces intégrations manuelles sont à exécuter **avant** l'intégration continue - qui validera donc l'ensemble de ces changements

---

# Compilations auto-testantes

- Les outils de build permettent l'exécution de certains outils d’intégration continue : tests, vérification syntaxique, … directement durant la phase de build
- Permet d’exécuter le même outil avec la même configuration à toutes les étapes du pipeline d’intégration : machine personnelle, serveur d’intégration, …
- Une modification du code source ne passant pas l'étape de compilation est en général immédiatement rejetée et la boucle d'intégration continue s'arrête.

---

Lancement de l'outil automatiquement par l'outil de build : pas de programme externe et pas d’oubli de lancer l'outil.

Ex : `gradle build` ou `mvn package` intègrent par défaut l'exécution des tests unitaires.

---


```plantuml
@startditaa

  +------------------------+
  | cYEL                   |
  | Machine du développeur |
  |                        |
  |  +------------------+  |
  |  | Compilation et   |  |
  |  | tests unitaires  |  |
  |  +------------------+  |
  |              :         |
  |              :         |
  |              v         |
  |  +------------------+  |
  |  | Intégration des  |  |
  |  | changements dans |  |
  |  | le dépôt de code |  |
  |  +------------------+  |
  |        :               |
  +--------:---------------+
           :
  +--------:---------------+
  |        v               |
  |  +------------------+  |
  |  | Compilation code |  |
  |  | de production    |  |
  |  +------------------+  |
  |             :          |
  |             :          |
  |             v          |
  |  +------------------+  |
  |  | Affichage des    |  |
  |  | résultats        |  |
  |  +------------------+  |
  |                        |
  | cBLU                   |
  | Serveur                |
  | d'intégration continue |
  +------------------------+

= Exemple de processus d'intégration continue.

@endditaa
```

---

<!-- class: liens -->

# Liens

- Le site de référence de [Martin Fowler sur l'intégration continue](https://martinfowler.com/delivery.html)
- La [traduction en français du site précédent](https://skalp.developpez.com/traductions/martin-fowler-integration-continue/)
- Le livre sur l'intégration continue : [Continuous Integration](https://martinfowler.com/books/duvall.html)
- Le livre sur le déploiement continu : [Continuous Devilery](https://martinfowler.com/books/continuousDelivery.html)
- Intégration continue avec Gitlab CI : <https://gitlab.com/goffinet/gitlab-ci>
- 🚀 Pour aller plus loin : le [cours sur les pratiques DevOps][site-perso].

---

