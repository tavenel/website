---
title: TP Dashboard PowerBI et Roadmap 
date: 2024 / 2025
---

L'objectif de ces exercices est de réfléchier à l'amélioration de la strate / couche applicative du SI, voir de la couche inférieure technique.

## Exercice 1 : Indicateurs

### Indicateurs de suivi d'une application

L'objectif de cet exercice est de vous entraîner à sélectionner des indicateurs pertinents pour une application du SI.

1. Identifiez 2 indicateurs par axe pour une application que vous avez réalisée (ou demandez un exemple d'application au formateur).
2. Justifiez pourquoi ces indicateurs sont pertinents.
3. Imaginez une visualisation pour chaque indicateur (graphique, jauge...).
4. Retours croisés : présentez vos indicateurs à un autre groupe et faites des retours sur la réalisation de ce groupe.

> Exemples : "Temps moyen de résolution d'incidents", représenté par une jauge avec une cible. "Temps moyen de réponse (opérationnel)", présenté sous forme de graphique à barres.

### Indicateurs de projets d'évolution du SI

_Même exercice pour déterminer les indicateurs les plus pertinents à présenter à une direction pour lancer des projets d'évolution du SI._

## Exercice 2 : Tableau de bord PowerBI

### Tutoriels

Dans un premier temps, nous allons nous familiariser avec l'utilisation de PowerBI avant de réaliser notre propre dashboard. Power BI est un outil de Business Intelligence permettant de réaliser de la transformation de données et des rapports de tout type. Son utilisation basique est assez intuitive mais l'interface utilisateur est très riche et il est facile de s'y perdre, attention à ne pas partir sur des exemples trop compliqués dès le début.

Il exite de nombreux concepts dans Power BI mais pour réaliser des tableaux de bord simples, il suffit de connaître les notions suivantes :

- Les données servant au suivi des indicateurs sont regroupées dans un ou plusieurs **modèles sémantiques**.
- Un **rapport** est une visualisation graphique d'un (et un seul) **modèle sémantique**.
- Un **tableau de bord** est un écran généré depuis un ou plusieurs **rapports**.

Nous utiliserons le **service** Power BI : <https://app.powerbi.com> (et non l'application _Desktop_). Connectez-vous avec votre compte fourni par l'école.

1. Commencer par se familiariser avec les concepts de base de Power BI : <https://learn.microsoft.com/fr-fr/power-bi/consumer/end-user-basic-concepts>
2. Suivre le tutoriel _"Exemple de dépenses d'entreprise pour Power BI"_ contenant un exemple déjà réalisé de suivi des coûts réels par rapport aux prévisions pour un service informatique : <https://learn.microsoft.com/fr-fr/power-bi/create-reports/sample-corporate-spend>
3. Faire de même avec le tutoriel _"Exemple d'Analyse des dépenses informatiques"_ contenant un tableau de bord, un rapport et un modèle sémantique avec une représentation différente : <https://learn.microsoft.com/fr-fr/power-bi/create-reports/sample-it-spend>

### Réalisation du Tableau de bord

L'objectif de cet exercice est de réaliser son propre dashboard dans PowerBI.

_Le but est la création d'un tableau de bord incluant la représentation visuelle des indicateurs pertinents pour déterminer les projets (applicatifs) à mener._

1. Définissez les objectifs de votre tableau de bord. _Exemple : Améliorer la performance d'une application critique._
2. Sélectionnez 3 indicateurs pertinents. _Exemple : Taux de disponibilité, temps moyen de résolution, coût mensuel._
3. Dessinez un brouillon de la structure visuelle.
4. Réalisez le tableau de bord en utilisant Power BI.
5. Retours croisés : présentez votre dashboard à un autre groupe et faites des retours sur la réalisation de ce groupe.

> Le but ici n'est pas de faire de la transformation complexe de données mais bien de représenter graphiquement ces données. On pourra donc s'aider d'une IA pour générer de la donnée à utiliser.

## Exercice 3 : Roadmap

L'objectif de cet exercice est de réaliser une roadmap pour prévoir l'évoluation future de votre SI.

1. Identifiez un objectif clé pour une évolution future de votre SI. _Exemple : Améliorer la sécurité en réduisant les vulnérabilités._
2. Listez les étapes nécessaires pour atteindre cet objectif. _Exemple : Audit, patching, suivi._
3. Utilisez un outil de diagramme (`Lucidchart`, `draw.io`, …) pour construire une roadmap simple.  
4. Retours croisés : présentez votre roadmap à un autre groupe et faites des retours sur la réalisation de ce groupe.

## Exemple de contexte

Une entreprise de e-commerce de taille intermédiaire, spécialisée dans la vente de matériel électronique grand public en Europe, dispose d'un système d'information fortement orienté services numériques et applications web.
Son SI repose sur une architecture hybride combinant un cloud public pour la partie front-office (site web, applications mobiles iOS/Android, API publiques pour partenaires) et un datacenter interne pour les applications cœur de métier (ERP, gestion des stocks, facturation, CRM et data warehouse).

L'entreprise connaît une croissance rapide de son volume de transactions, avec des pics d'activité importants lors d'événements promotionnels, ce qui met sous tension la couche applicative, notamment les microservices liés au panier, au paiement et à la recommandation de produits.

Les équipes techniques observent régulièrement des dégradations de performance lors des montées en charge, des incidents de synchronisation entre le stock réel et le stock affiché, ainsi que des problèmes de disponibilité intermittente sur certaines API internes utilisées par le service logistique.
Par ailleurs, le service support client signale une augmentation des tickets liés à des lenteurs d'affichage, des erreurs de paiement et des retards de confirmation de commande.

L'organisation du SI est répartie entre plusieurs équipes (développement, exploitation, data, sécurité) qui utilisent des outils différents de supervision, de ticketing et de reporting, rendant la vision globale difficile pour la direction informatique.

La direction souhaite donc mettre en place des tableaux de bord décisionnels permettant d'améliorer la performance de la couche applicative (qualité de service, stabilité, scalabilité, maintenabilité) tout en gardant une visibilité sur les dépendances techniques sous-jacentes (infrastructure cloud, bases de données, réseau, conteneurs).

Vous vous positionnez comme des analystes SI chargés d'identifier des indicateurs pertinents couvrant la disponibilité des applications, la performance transactionnelle, la qualité du code, la satisfaction utilisateur, la fiabilité des intégrations inter-applicatives et l'efficacité opérationnelle des équipes, puis proposez des visualisations adaptées dans Power BI afin d'aider à la prise de décision stratégique et à l'amélioration continue du système applicatif.
