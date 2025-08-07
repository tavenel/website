---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CourseLayout.astro'
title: Introduction aux tableaux de bord et feuilles de route
tags:
  - gestion_projet
  - data
---

## Rappel : Découpage en Couches du SI

---

### Pourquoi un Découpage en Couches ?

- **Indépendance fonctionnelle** : Chaque couche remplit un rôle spécifique.
- **Modularité** : Facilite les mises à jour et le remplacement d'une couche.
- **Maintenance simplifiée** : Chaque couche est gérée indépendamment.
- **Scalabilité** : Permet une montée en charge ciblée.

> Un SI bien structuré est plus agile et résilient face aux évolutions technologiques.

---

### Les Principales Couches d'un SI

- Couche _Présentation_ (Front-end)
- Couche _Applicative_ (Back-end)
- Couche _Données_ (Base de données)

---

### Couche Présentation

- **Rôle** :
  Fournir une interface pour **interagir** avec le système.

- **Exemples** :
  - _Applications web : navigateurs._
  - _Applications mobiles : iOS, Android._
  - _Portails utilisateurs : dashboards, ERP._

- **Technologies courantes** :
  - `HTML`, `CSS`, `JavaScript` (Frameworks comme `React`, `Angular`).

---

### Couche Applicative

- **Rôle** :
  Traiter les données et appliquer la **logique métier**.

- **Exemples** :
  - _Services REST ou SOAP._
  - _Moteurs de règles métiers._
  - _API utilisées par la couche présentation._

- **Technologies courantes** :
  - `Java`, `Python`, `Node.js`, `.NET`

---

### Couche Données

- **Rôle** :
  Stocker, structurer et sécuriser les **informations**.

- **Exemples** :
  - _Bases de données relationnelles : MySQL, PostgreSQL._
  - _Bases NoSQL : MongoDB, Cassandra._
  - _Data Warehouses : Snowflake, Redshift._

- **Concepts clés** :
  - Intégrité des données.
  - Sauvegarde et restauration.
  - Optimisation des performances.

---

### Relation entre les Couches

1. **Flux descendant** :
   - L'utilisateur interagit avec la couche présentation.
   - Les requêtes descendent à travers la couche applicative jusqu'à la couche données.

2. **Flux ascendant** :
   - Les données collectées remontent via la couche applicative pour être affichées.

---

### Exemple 1 : Application Web

- **Couche Présentation** : Site web interactif (HTML, CSS, JavaScript).
- **Couche Applicative** : API REST pour gérer les utilisateurs.
- **Couche Données** : Base PostgreSQL pour stocker les profils.

---

### Exemple 2 : Système de Reporting

- **Couche Présentation** : Tableau de bord (Power BI).
- **Couche Applicative** : Calculs analytiques (Python).
- **Couche Données** : Entrepôt de données (Snowflake).

---

## Introduction aux Tableaux de Bord

---

### 🎯 Objectifs de cette partie

- Comprendre ce qu'est un tableau de bord.
- Identifier ses avantages et ses limites.
- Découvrir les types de tableaux de bord.
- Explorer les cas d'utilisation dans un Système d'Information (SI).

---

### Tableau de bord

> Outil _visuel_ permettant de **suivre** les performances, **analyser** les données et aider à la prise de **décision**.

- 🎯 **But** :
  - Fournir une vue **synthétique** des _indicateurs clés_.
  - Faciliter la _gestion et le pilotage_ des applications SI.

---

### 🌟 Avantages

- Visualisation en temps réel des métriques clés.
- Accès aux données critiques à tout moment : prise de décision rapide
- Identification des tendances et des anomalies.
- Présentation claire des informations pour les parties prenantes.

---

### ❌Limites

- Difficulté du choix et de la récupération des données
- Illisible si trop de données affichées

---

### Types de Tableaux de Bord

- **Stratégique** : Suivi des objectifs à long terme
  - _Exemple : Analyse des coûts globaux du parc applicatif._
- **Opérationnel** : Suivi des activités quotidiennes.
  - _Exemple : Temps moyen de résolution des incidents._
- **Analytique** : Analyse approfondie des données historiques.
  - _Exemple : Fréquence de déploiement des mises à jour._

---

### Cas d'Utilisation dans le SI

1. **Surveillance des Applications** :
   - Disponibilité, performance, et utilisation des applications.
2. **Gestion des Incidents** :
   - Temps moyen de résolution, impact des incidents critiques.
3. **Optimisation des Ressources** :
   - Analyse des coûts et des investissements nécessaires.
4. **Conformité Légale** :
   - Respect des réglementations (ex : RGPD).

---

### Bonnes pratiques

- Sélectionner uniquement les indicateurs **principaux**
- Faire le lien avec les **activités de l'entreprise**
- Permet une **stratégie** sur le **futur**
- **Adapter** le vocabulaire et les mesures au profil du destinataire
- Rappeler les unités de mesure
- Utiliser des couleurs
- **Interactivité** : utiliser des filtres ou des options de zoom pour explorer les données.

---

### À éviter

- Présenter des chiffres sans **contexte ou objectif** : stratégie, organisation, personnes
- Utiliser des données disparates sans **consolidation**
- Penser à l'automatisation des **mises à jour**
- Saisir manuellement les données

---

## Indicateurs de Performance et Métriques du Parc Applicatif

---

### 🎯 Objectifs de cette partie

- Comprendre le **rôle des indicateurs** de performance (KPI) dans la gestion du SI.
- **Identifier** les métriques clés selon différents axes.
- Savoir **choisir** les indicateurs pertinents pour un tableau de bord.

---

### Pourquoi des Indicateurs de Performance ?

- Évaluer la **performance** des applications dans le SI.
- Identifier rapidement les **points critiques** et **prioriser** les actions.
- **Suivre les objectifs stratégiques** : Alignement sur les priorités métier.

> _"Un bon indicateur est pertinent, mesurable, et exploitable."_

---

### Axes d'Analyse des Indicateurs

---

#### 💵 Axe Financier

- **Exemples** :

  - Coûts d'exploitation des applications.
  - Pourcentage d'investissements pour les évolutions.

- **Utilité** :
  Suivre la rentabilité et maîtriser les budgets.

---

#### 📈 Axe Technique & Données

- **Exemples** :

  - Taux de disponibilité (% uptime).
  - Temps moyen de résolution d'incidents.
  - Volume de données générées par mois.

- **Utilité** :
  Mesurer la fiabilité et l'efficacité opérationnelle.

---

#### 🔐 Axe Sécurité

- **Exemples** :

  - Taux de vulnérabilité détectées.
  - Fréquence des mises à jour de sécurité.

- **Utilité** :
  Garantir la résilience face aux cyberattaques.

---

#### 🙎 Axe Utilisateur / Fonctionnel

- **Exemples** :

  - Taux de satisfaction utilisateur.
  - Temps moyen passé sur l'application.
  - Accessibilité et utilisabilité.

- **Utilité** :
  Améliorer l'expérience utilisateur et l'adoption.

---

#### 🏛 Axe Légal / Réglementaire

- **Exemples** :

  - Conformité RGPD.
  - Respect des réglementations sectorielles.

- **Utilité** :
  Réduire les risques juridiques et d'amendes.

---

### Exemple d'Indicateurs Clés pour une Application

| Axe 🗃           | Indicateur 📊📈                  | Objectif 🎯            |
| --------------- | ---------------------------- | -------------------- |
| **Financier** 💵   | Coût mensuel de maintenance  | < 5% d'augmentation  |
| **Technique** 📈   | Taux de disponibilité        | 99,9 % d'uptime.     |
| **Sécurité** 🔐    | Nombre de vulnérabilités     | 0 faille critique    |
| **Utilisateur** 🙎 | Satisfaction utilisateur (%) | 90 % minimum.        |
| **Légal** 🏛       | Respect RGPD (%)             | 100 % de conformité. |

---

### Autres exemples d'indicateurs

- Taux de disponibilité des systèmes informatiques
- Temps moyen de réponse aux incidents
- Temps moyen de résolution des incidents
- Taux de satisfaction des utilisateurs
- Coût total de possession des systèmes informatiques
- Pourcentage d'incidents résolus à l'heure
- Pourcentage de demandes satisfaites dans les délais impartis
- Nombre moyen d'incidents résolus par jour
- Nombre de problèmes résolus par le personnel informatique
- Nombre de nouvelles applications informatiques déployées
- Nombre de nouvelles mises à jour des systèmes informatiques
- Taux de sécurité des données
- Taux de conformité réglementaire

---

### Bonnes Pratiques pour Choisir un Indicateur

1. **Pertinence** :
	L'indicateur doit répondre à un objectif précis.

2. **Clarté** :
	Il doit être compréhensible par tous les acteurs.

3. **Fiabilité** :
	Les données utilisées doivent être exactes et à jour.

4. **Exploitabilité** :
	Il doit permettre de prendre des décisions concrètes.

---

### SLA

- Accord de niveau de service (SLA) : engagement contractuel avec le client sur une métrique
- Indicateur à suivre par excellence

---

## Construction d'un Tableau de Bord

---

### 🎯 Objectifs de cette partie

- Comprendre les étapes nécessaires pour concevoir un tableau de bord.
- Découvrir les bonnes pratiques de conception.
- Créer une structure visuelle adaptée aux besoins du SI.

---

### Définir les Objectifs 🎯

- Que voulez-vous mesurer ?
- À qui s'adresse le tableau de bord ?
- _Exemple : direction, équipe technique, utilisateurs finaux_

---

### Sélectionner les Indicateurs Clés (KPI) 🗂

- Priorisez les métriques en fonction des besoins.
- Assurez-vous qu'ils soient pertinents, mesurables et exploitables.
- _Exemple : Temps de réponse des applications, taux de disponibilité, coûts d'exploitation._

---

### Concevoir la Structure 📑

- **Types de visualisations** :
- Graphiques à barres, lignes ou secteurs.
- Jauges pour des indicateurs spécifiques.
- Cartes de chaleur pour des comparaisons globales.

> Limitez les visuels à l'essentiel pour éviter la surcharge.

---

### Collecter et Connecter les Données 🗃

- Utilisez des outils adaptés pour centraliser les données :
- Bases de données.
- APIs d'applications SI.
- Outils BI (`Power BI`, `Tableau`, etc.).

---

### Tester et Valider 🧪

- Vérifiez :
- La fiabilité des données.
- La lisibilité des visualisations.
- La compréhension par les utilisateurs finaux.

> Un tableau de bord n'est utile que si les utilisateurs peuvent l'exploiter facilement.

---

### Exemples de Tableaux de Bord

![Exemple de tableau de bord de support utilisateur](https://www.geckoboard.com/uploads/Live-customer-support-dashboard-example.png)

<div class="caption">Exemple de tableau de bord de support utilisateur</div>

---

![Exemple de tableau de bord IT](https://www.geckoboard.com/uploads/IT-dashboard-example.png)

<div class="caption">Exemple de tableau de bord IT</div>

---

![Exemple de tableau de bord de durabilité environnementale](https://www.geckoboard.com/uploads/sustainability-dashboard-example.png)

<div class="caption">Exemple de tableau de bord de durabilité environnementale</div>

---

## Introduction à PowerBI

---

### Types d'applications

- Power BI **Service** <https://app.powerbi.com> : focus sur la création de _dashboard_
- Power BI **Desktop** (à installer) : focus sur la _transformation_ de données et la création de rapports complexes
- Power BI **Mobile** : lecture des dashboards, …

---

### Glossaire Power BI

- Les données servant au suivi des indicateurs sont regroupées dans un ou plusieurs **modèles sémantiques**.
- Un **rapport** est une visualisation graphique d'un (et un seul) **modèle sémantique**.
- Un **tableau de bord** (_Dashboard_) est un écran généré depuis un ou plusieurs **rapports**.

---

### Principales Visualisations Power BI  

---

### Graphique à Barres / Colonnes

![Exemple de graphique à barres](@assets/bi/visual-bar-chart.png)

- **Comparer des valeurs** entre différentes catégories.
- Mettre en évidence les **différences** importantes.

#### Exemple

- _**Cas pratique** : Comparaison des coûts mensuels des applications._
- _**Visualisation** : Barres verticales pour les coûts par application (janvier à décembre)._

---

### Graphique en Secteurs

![Exemple de graphique en secteurs](@assets/bi/visual-pie-chart.png)

- Montrer la **répartition** d'une valeur totale en pourcentages.
- Analyser les parts relatives.

#### Exemple

- _**Cas pratique** : Répartition du budget SI entre les catégories (applications, matériel, personnel)._
- _**Visualisation** : Diagramme circulaire avec des segments pour chaque catégorie._

---

### Graphique en courbes

![Exemple de courbe](@assets/bi/visual-line-chart.png)

- Suivre l'**évolution** d'une valeur dans le temps.
- Identifier des **tendances** ou des **variations**.

#### Exemple

- _**Cas pratique** : Suivi du taux de disponibilité des applications mois par mois._
- _**Visualisation** : Ligne représentant l'évolution du pourcentage de disponibilité._

---

### Graphique en Aire

![Exemple de graphique en aire](@assets/bi/basic-area-map-small.png)

- Montrer une **évolution** et l'**accumulation** de valeurs.
- Mettre en évidence les **proportions** dans une série temporelle.

#### Exemple

- _**Cas pratique** : Volume de données générées par trois applications sur une année._
- _**Visualisation** : Aires empilées montrant les contributions cumulatives._

---

### Jauge

![Exemple de jauge](@assets/bi/gauge-m.png)

- Suivre une valeur par rapport à un **objectif** ou un **seuil**.
- Idéal pour des KPI simples.

#### Exemple

- _**Cas pratique** : Suivi du taux d'incidents résolus par rapport à l'objectif de 95 %._
- _**Visualisation** : Une jauge montrant la progression vers l'objectif._

---

### Carte de Chaleur (Heatmap)

![Exemple de graphique à barres](@assets/bi/7-power-bi-matrix-with-heatmap-1.png)

<div class="caption">Source: https://blog.coupler.io/wp-content/uploads/2024/03/7-power-bi-matrix-with-heatmap-1.png</div>

- Identifier des modèles ou des **anomalies** dans des données tabulaires.
- Comparer de grandes quantités de données rapidement.
- 🚨 Attention : pas de visualisation de type _Heatmap_ par défaut dans PowerBI (à installer ou à simuler en utilisant un formattage des données). 🚨 
- _**Cas pratique** : Analyse des performances des serveurs (temps moyen de réponse)._
- _**Visualisation** : Couleurs variant du vert (bon) au rouge (mauvais)._

---

### Carte Géographique

![Exemple de carte](@assets/bi/visual-map.png)

- Visualiser des données **géolocalisées**.
- Identifier des modèles géographiques.

#### Exemple

- _**Cas pratique** : Répartition des utilisateurs d'une application par région._
- _**Visualisation** : Carte avec des points ou des zones colorées selon le nombre d'utilisateurs._

---

### Tableau Croisé Dynamique (Matrice)

![Exemple de matrice](@assets/bi/matrix.png)

- Présenter des données **multi-dimensionnelles** sous forme de tableau interactif.
- Explorer des hiérarchies.

#### Exemple

- _**Cas pratique** : Analyse des coûts par département et par catégorie._
- _**Visualisation** : Tableau croisé dynamique avec lignes et colonnes imbriquées._

---

## Élaboration d'une Feuille de Route (Roadmap)

---

### 🎯 Objectifs de cette partie

- Comprendre l'utilité d'une feuille de route.
- Identifier les éléments clés d'une roadmap.
- Découvrir les bonnes pratiques de conception.
- Apprendre à utiliser des outils adaptés.

---

### Roadmap

> Représentation **visuelle** et **structurée** des étapes, ressources et échéances nécessaires pour atteindre des objectifs stratégiques.

- 🎯 **Objectif principal** :
  **Planifier l'évolution** des applications du SI de manière claire et réaliste.

---

### Pourquoi une Roadmap pour le SI ?

- **Planification stratégique** : définir des **priorités** pour l'évolution des applications.
- Aligner les parties prenantes sur une **vision commune**.
- Évaluer les **jalons** atteints et **ajuster** si nécessaire.

> Une roadmap claire réduit les incertitudes et améliore la coordination des équipes.

---

### Éléments Clés d'une Roadmap

1. **Objectifs** :
   Quels sont les résultats attendus ?

   _Exemple : Augmenter la disponibilité de 99 % à 99,9 %._

2. **Étapes principales** :
   Les grandes phases du projet.

   _Exemple : Audit, développement, tests, déploiement._

3. **Ressources nécessaires** :
   Compétences, outils, budget.

   _Exemple : Équipe de DevOps, Power BI._

4. **Échéances** :
   Dates clés et jalons.

   _Exemple : Déploiement final dans 6 mois._

---

### Bonnes Pratiques pour Construire une Roadmap

- **Clarté et simplicité** : Définissez des étapes atteignables dans le temps imparti.
- **Évolutivité** : Prévoyez des ajustements en cas d'imprévus.
- **Collaboration** : Impliquez toutes les parties prenantes dès le début.

---

### Outils pour Créer une Roadmap

- **[Lucidchart](https://www.lucidchart.com)** : Création intuitive de diagrammes et roadmaps.
- **[Miro](https://miro.com/)** : Plateforme collaborative pour brainstorming et planification.
- **Microsoft PowerPoint / Excel** : Simples et accessibles pour des présentations rapides.
- **Outils de gestion de projet** : [Atlassian Jira](https://www.atlassian.com/software/jira), [Monday.com](https://monday.com/), …

---

### Exemple de Roadmap

- **Objectif principal** : Migration d'une application vers le cloud.

---

![Exemple de roadmap technologique IT](@assets/roadmap/roadmap1.png)

<div class="caption">Exemple de roadmap technologique IT. Source: https://www.lucidchart.com/blog/what-is-a-technology-roadmap</div>

---

![Exemple de roadmap de projet IT](@assets/roadmap/roadmap2.jpg)

<div class="caption">Exemple de roadmap de projet IT. Source: https://www.productplan.com/templates/it-project-roadmap-template/</div>

---

![Exemple de roadmap d'architecture IT](@assets/roadmap/roadmap3.jpg)

<div class="caption">Exemple de roadmap d'architecture IT. Source: https://www.productplan.com/templates/it-architecture-roadmap/</div>

---

## Ressources

---

### Livres

- [Pocket CIO](https://univ.scholarvox.com/catalog/book/docid/88856824)
- [Microsoft Power BI Complete Reference](https://univ.scholarvox.com/catalog/book/docid/88865488)
- [Enterprise Solution Architecture - Strategy Guide](https://univ.scholarvox.com/catalog/book/docid/88939086)

---

### Webographie

- [MTBF, MTTR, MTTA et MTTF : Maîtriser quelques-unes des métriques d'incident les plus courantes](https://www.atlassian.com/fr/incident-management/kpis/common-metrics)
- [Atlassian - Indicateurs de performance SI](https://www.atlassian.com/fr/itsm/service-request-management/it-metrics-and-reporting)
- [Exemples : 12 tableaux de bord pour piloter ses activités informatiques][exemples-tableaux]
- [70 Exemples de dashboard](https://www.geckoboard.com/dashboard-examples/)
- [Concepts de base de Power BI](https://learn.microsoft.com/fr-fr/power-bi/consumer/end-user-basic-concepts)
- [Types de visualisations dans Power BI](https://learn.microsoft.com/fr-fr/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)
- [Tutoriel : générer un rapport Power BI à partir d'un classeur Excel](https://learn.microsoft.com/fr-fr/power-bi/create-reports/service-from-excel-to-stunning-report)
- [Exemples de données pour PowerBI](https://learn.microsoft.com/fr-fr/power-bi/create-reports/sample-datasets)
- [PowerBI : essential training](https://www.linkedin.com/learning/power-bi-essential-training-17362720)
- [Power BI : Data visualization and dashboard tips and tricks](https://www.linkedin.com/learning/power-bi-data-visualization-and-dashboard-tips-tricks-techniques)
- <https://generatedata.com/> : générer des donnée de test
- [Lucidchart - Roadmap technologique](https://www.lucidchart.com/blog/fr/fonction-d-une-roadmap-technologique)

[exemples-tableaux]: https://www.journaldunet.com/solutions/dsi/1002623-12-tableaux-de-bord-pour-piloter-ses-activites-informatiques/

---

