---
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Tests de données
keywords:
- integration
- data
- tests
---

# Tests de données

_Tom Avenel_

<https://www.avenel.pro/>

---

# Tests de données

- Comment tester l'intégration de données ?
- Comment réussir sa migration de données ?
- Comment valider la reprise de données ?

---

# Tests d'intégration des données

---

# Intégration de données

L'intégration des données consiste à combiner les données résidant sur différentes sources afin que les utilisateurs puissent en obtenir une vue unifiée.

Les tests d'intégration de données correspondent donc à l'ensemble des scénarios et procédures permettant de valider cette intégration.

---

# Automatisation des tests d'intégration de données

Afin d'augmenter la qualité des données testées, il est intéressant d'automatiser ces tests, (voir les avantages et risques décrits précédemment)

La stratégie d'automatisation peut suivre: 

- une approche "bottom-up" en partant de tests d'unités de données pour créer un jeu de données intégrées.
- une approche "top-down" en testant directement la régression sur le jeu de données intégré.

---

# Utiliser des données de production

Cette approche a l'avantage de demander peu d'investissement quand on peut s'appuyer sur les outils de sauvegarde et de rechargement déjà en place. Elle présente cependant certains inconvénients :
Confidentialité : utiliser des données client est risqué, voir interdit par la réglementation (`GDPR`, ...)
Les données peuvent ne pas exister encore (nouvelle fonctionnalité, changement de format des données, ...), ou ne plus exister en production (résiliation du client)

---

# Utiliser des données de référence

Les tests d'intégration ont vocation à être exécutés lors de chaque modification du système. Pour certifier leur répétabilité et faciliter leur cohérence, on utilise un jeu réduit de données communes, proches de données réelles en production.

Ces données peuvent prendre plusieurs formes, et pas seulement celles de données statiques :

- Bases de données que l'on va recopier (solution basique mais qui rend plus difficile le versionning des données avec le code) 
- Scripts `SQL`
- Données dans des fichiers de configuration (`XML` par exemple)
- Code permettant d'insérer les données de manière paramétrable, éventuellement par une API minimaliste dédiée.

---

Les données de référence sont généralement générées manuellement, en s'inspirant de données trouvées en production, ou en anonymisant ces données.

Utiliser des données de référence permet également de tester les limites des données.

En générant des données soi-même, on peut choisir les plus pertinentes et s'attarder aux cas aux limites de l'application : champ optionnel vide, noms avec accents ou espaces, ...

---

On parle aussi de "génération de données synthétiques" pour des données de référence : données partiellement synthétiques lorsqu'elles sont anonymisées depuis la production, données entièrement synthétiques lorsqu'elles sont créées de toute pièce.

Exemple de générateur : <https://gitlab.com/healthdatahub/synthetic-generator>.

---

# Gestion des données de tests

Maintenir ces données présente un coût. Il peut être pertinent de développer des outils permettant d'extraire des données de la production et de les anonymiser afin d'en faire des données de référence.

Le processus de réinitialisation des données  : il est nécessaire de pouvoir régulièrement remettre les données à zéro sur les environnements d'intégration. Il faut donc un processus permettant de le faire, si possible de manière automatisée.

---

# Tests de migration des données

---

# Migration de données

La migration des données consiste à :

- déplacer les données d'un emplacement vers un autre
- ou d'une application vers une autre
- ou à les convertir dans un autre format.

---

Elle comporte 3 étapes principales (ETL) :

- Extraction des données
- Transformation des données
- Chargement des données

---

Cette opération inclut le profilage, le nettoyage et la validation des données, ainsi qu'un processus d'assurance qualité continu sur le système cible. Dans un scénario de migration des données standard, la conversion ne constitue que la première étape d'un processus complexe

Elle est généralement liée à l'introduction d'un nouveau système ou d'un nouvel emplacement pour les données :  consolidation pour remplacer des anciens systèmes,  l'ajout de nouvelles applications sur les mêmes données, passage au stockage cloud, ....

Une migration peut être initiale (à la mise en production) ou quotidienne (migration constante de données d'un système/format à un autre durant le fonctionnement "normal")

---

# Réaliser la migration

Exemple de processus de migration :

- Planification de la migration préalable : évaluer la stabilité des données à déplacer.
- Lancement du projet : identifier et informer les principales parties prenantes.
- Analyse de l'environnement : établir un processus fiable de gestion des règles de qualité des données. Informer l'entreprise des objectifs du projet et de l'arrêt des anciens systèmes.

---

- Design de la solution : déterminer les données à déplacer, ainsi que leur qualité, avant et après la migration.
- Développement et test : développer le code de la logique de migration et tester la migration avec un miroir de l'environnement de production.
- Exécution et validation : Démontrer la conformité de la migration aux exigences définies et la viabilité des données déplacées pour le métier.
- Mise hors service et surveillance : Arrêter et supprimer les anciens systèmes.

---

# Définir les échéances

Une fois la migration définie, l'étape suivante consiste à définir les échanges :

- Formats d'échange (`XML`, `CSV`, `JSON`, ...)
- Noms des flux et fichiers à échanger

Ainsi que la temporalité :

- Fréquence de l'import
- Heure d'exécution
- Mise en place d'alertes et gestion des archives

---

# Tableau de mapping

On pourra représenter la migration à l'aide d'un tableau de mapping source et données.

Ce tableau permet de lister les données sources et les champs de destination pour stocker les données.
Il peut s'agir d'un document simple dans le cas de données simples et/ou maîtrisées (document texte, fichier `Excel`, ...) ou d'un outil complexe permettant de visualiser chaque migration (cas de données complexes)

---

# Suivi de l'intégrité

Pour réaliser le suivi de l'intégrité de la migration, on pourra s'aider de la section correspondante dans le manuel d'exploitation.

Cette section décrit la ou les procédures permettant de réaliser le suivi de l'intégrité du système et de ses données. Il s'agit donc non seulement de décrire les opérations mises en place (sauvegarde, archivage, ...) mais aussi la surveillance de cette intégrité.

---

Cette section mentionne également les procédures à suivre pour réagir en cas de problème spécifique lié à cette intégrité de données.

Les procédures d'exploitation ne contiennent pas uniquement des opérations techniques ! Dans le cas du suivi de l'intégrité notamment, on prendra soin de préciser le processus administratif à suivre (personne à prévenir, ...) en cas de fuite des données.

Voir le [cours sur le document d'exploitation][site-perso].

---

# Importance des tests de migration et de validation

Les tests de migration et de validation sont primordiaux : comme tous les tests, ceux-ci doivent donc être budgétisés, et inclure une gestion des risques associés.

Les scénarios de migration ne doivent pas décrire la migration de manière abstraite mais être précis et quantitatifs (système source, destination, résultats attendus, procédures de suivi, ...)

---

# Les points à surveiller

- Absence d'informations : informer les parties prenantes, expliquer les raisons de la migration et son impact.
- Absence de communication : Maintenir les parties prenantes informées de l'avancement des opérations : rapport d'état hebdomadaire à jour fixe, ...
- Manque de gouvernance des données : Identifier clairement les personnes qui disposent d'autorisations pour créer, approuver, modifier et supprimer les données du système source. Consigner ces informations par écrit dans le plan du projet.

---

- Manque de planification : migration "simple" => 20 à 40H de préparation
- Méthodologie de migration qui n'a pas fait ses preuves : étudier l'état de l'art, éviter une solution trop générique.
- Dépendances entre objets ; souvent détectées tard - prévoir un plan d'urgence
- Gestion des fournisseurs et des projets
- Manque d'expertise et outils mal adaptés

---

# Tests de reprise de données

---

# La reprise de données

La reprise des données est la phase qui consiste à récupérer un ensemble de données existantes pour les importer dans un nouveau logiciel.

Tout comme la migration, celle-ci se réalise également en 3 phases `ETL`.

La reprise de données peut s'exécuter :

- soit à travers un outil `ETL` existant
- soit en développant son propre `ETL` via une approche scriptée

---

# Préparation de la reprise de données

Avant de pouvoir exécuter la reprise de données, il est nécessaire de la préparer :

- Phase de cadrage : cette phase réalise l'état des lieux du modèle de données. On sera également attentif à bien comprendre le contexte métier afin de pouvoir mettre du sens sur les données analysées.
- Évaluation en termes de volume et de complexité : nécessaires pour anticiper l'envergure des opérations à effectuer
- Priorisation des scénarios de reprise : grâce à la compréhension du métier, l'effort est mis en priorité sur les cas d'utilisation les plus importants pour le métier de l'entreprise.

---

# Les outils ETL

Un `ETL` est un middleware permettant d'effectuer des synchronisations de données entre différents systèmes.

Il extrait les données, les manipule (conversion, suppression des doublons, etc.) et les intègre dans un référentiel commun : l'entrepôt de données (datawarehouse).

---

La technologie `ETL` repose sur :

- des connecteurs permettant de récupérer et transférer des données,
- des transformateurs permettant d'effectuer des manipulations complexes sur ces données,
- des mises en correspondance afin de faire correspondre le schéma des données au schéma du ou des systèmes cibles.

---

# Avantages d'un ETL

- Dispose de connecteurs bdd, webservices et fichiers plats prêts à l'emploi.
- Permet de structurer et rassembler l'ensemble des morceaux de code nécessaires aux transferts et aux transformations des données.
- Offre une représentation graphique des flux et opérations.
- Permet de traiter rapidement un grand nombre de données.
- Facilite la maintenance et l'évolution de l'`ETL`.

---

- Gère nativement le chiffrement des données.
- Intègre la gestion des métadonnées, la gestion des erreurs, la gestion des processus et de leur hiérarchie, la gestion de la documentation.
- Permet un déploiement facile des flux sur un environnement de production.
- Est compréhensible par une une personne sans connaissances avancées en développement.
- Gère l'équilibrage de charge entre serveurs.
- Est extensible à l'aide de script.

---

# Inconvénients d'un ETL

- Nécessite un ou plusieurs développeurs avec des connaissances sur l'outil d'`ETL` utilisé ou nécessite un temps d'apprentissage.
- Est difficilement intégrable à un outil de gestion de versions.

---

# Approche scriptée

L'approche scriptée consiste à développer le ou les outils nécessaires à la mise en place d'un traitement `ETL`, à l'aide d'un ou plusieurs langages de programmation.

Ces outils consistent généralement en une combinaison de procédures stockées au niveau des bases de données ainsi que de différents scripts nécessaires au transport des données et aux transformations complexes.

Il peut aussi s'agir d'un outil technique lié au langage de l'application.

---

# Avantages de l'approche scriptée

- Homogénéité technologique avec les solutions déjà en place au niveau du SI.
- Utiliser les langages que les équipes maîtrisent déjà, sans apprentissage et médiation d'un outil tiers.
- Simplifier le traitement des fichiers plats.
- Intégration poussée avec des outils de gestion de versions.

---

# Inconvénients de l'approche scriptée

- Nécessite de tout développer.
- Impose de nombreuses modifications lors d'une modification au niveau de la source, du contenu ou de la destination.
- Facteur d'un grand nombre de bugs et de régressions à chaque modification.
- Nécessite l'utilisation d'un planificateur de tâches externe.
- Nécessite de tout documenter, au risque de se perdre dans le code produit.
- Peut être éparpillé sur plusieurs serveurs.

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
