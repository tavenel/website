---
theme: the-unnamed
slidev: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Dashboard DSI
tags:
  - gestion_projet
  - data
---

# Introduction aux tableaux de bord et feuilles de route

_Tom Avenel_

<https://www.avenel.pro/>

---
layout: section
---

# Rappel : Découpage en Couches du SI

---

# Pourquoi un Découpage en Couches ?

<v-clicks>

- <span v-mark.underline.red="1">**Indépendance fonctionnelle**</span> : Chaque couche remplit un rôle spécifique.
- <span v-mark.underline.red="2">**Modularité**</span> : Facilite les mises à jour et le remplacement d'une couche.
- <span v-mark.underline.red="3">**Maintenance simplifiée**</span> : Chaque couche est gérée indépendamment.
- <span v-mark.underline.red="4">**Scalabilité**</span> : Permet une montée en charge ciblée.

</v-clicks>
<v-clicks>

> Un SI bien structuré est plus agile et résilient face aux évolutions technologiques.

</v-clicks>

---

# Les Principales Couches d'un SI

<v-clicks>

- Couche <span v-mark.underline.red="1">Présentation</span> (Front-end)
- Couche <span v-mark.underline.red="2">Applicative</span> (Back-end)
- Couche <span v-mark.underline.red="3">Données</span> (Base de données)

</v-clicks>

---

# Couche Présentation

- **Rôle** :
  Fournir une interface pour <span v-mark.underline.red="1">interagir</span> avec le système.

- **Exemples** :
  - _Applications web : navigateurs._
  - _Applications mobiles : iOS, Android._
  - _Portails utilisateurs : dashboards, ERP._

- **Technologies courantes** :
  - `HTML`, `CSS`, `JavaScript` (Frameworks comme `React`, `Angular`).

---

# Couche Applicative

- **Rôle** :
  Traiter les données et appliquer la <span v-mark.underline.red="1">logique métier</span>.

- **Exemples** :
  - _Services REST ou SOAP._
  - _Moteurs de règles métiers._
  - _API utilisées par la couche présentation._

- **Technologies courantes** :
  - `Java`, `Python`, `Node.js`, `.NET`

---

# Couche Données

- **Rôle** :
  Stocker, structurer et sécuriser les <span v-mark.underline.red="1">informations</span>.

- **Exemples** :
  - _Bases de données relationnelles : MySQL, PostgreSQL._
  - _Bases NoSQL : MongoDB, Cassandra._
  - _Data Warehouses : Snowflake, Redshift._

- **Concepts clés** :
  - Intégrité des données.
  - Sauvegarde et restauration.
  - Optimisation des performances.

---

# Relation entre les Couches

1. **Flux descendant** :
   - L’utilisateur interagit avec la couche présentation.
   - Les requêtes descendent à travers la couche applicative jusqu’à la couche données.

2. **Flux ascendant** :
   - Les données collectées remontent via la couche applicative pour être affichées.

---

# Exemple 1 : Application Web

- **Couche Présentation** : Site web interactif (HTML, CSS, JavaScript).
- **Couche Applicative** : API REST pour gérer les utilisateurs.
- **Couche Données** : Base PostgreSQL pour stocker les profils.

---

# Exemple 2 : Système de Reporting

- **Couche Présentation** : Tableau de bord (Power BI).
- **Couche Applicative** : Calculs analytiques (Python).
- **Couche Données** : Entrepôt de données (Snowflake).

---
layout: section
---

# Introduction aux Tableaux de Bord

---

# 🎯 Objectifs de cette partie

<v-clicks>

- Comprendre ce qu'est un tableau de bord.
- Identifier ses avantages et ses limites.
- Découvrir les types de tableaux de bord.
- Explorer les cas d’utilisation dans un Système d’Information (SI).

</v-clicks>

---

# Tableau de bord

<v-clicks>

> Outil <span v-mark.box="1">visuel</span> permettant de **suivre** les performances, **analyser** les données et aider à la prise de **décision**.

- 🎯 **But** :
  - Fournir une vue <span v-mark.underline.red="2">synthétique</span> des <span v-mark.underline.red="2">indicateurs clés</span>.
  - Faciliter la <span v-mark.underline.red="2">gestion et le pilotage</span> des applications SI.

</v-clicks>

---

# Avantages

<v-clicks>

- Visualisation en temps réel des métriques clés.
- Accès aux données critiques à tout moment : prise de décision rapide
- Identification des tendances et des anomalies.
- Présentation claire des informations pour les parties prenantes.

</v-clicks>

---

# Limites

<v-clicks>

- Difficulté du choix et de la récupération des données
- Illisible si trop de données affichées

</v-clicks>

---

# Types de Tableaux de Bord

<v-clicks>

- <span v-mark.underline.red="1">**Stratégique**</span> : Suivi des objectifs à long terme
  - _Exemple : Analyse des coûts globaux du parc applicatif._
- <span v-mark.underline.red="2">**Opérationnel**</span> : Suivi des activités quotidiennes.
  - _Exemple : Temps moyen de résolution des incidents._
- <span v-mark.underline.red="3">**Analytique**</span> : Analyse approfondie des données historiques.
  - _Exemple : Fréquence de déploiement des mises à jour._

</v-clicks>

---

# Cas d'Utilisation dans le SI

<v-clicks>

1. **Surveillance des Applications** :
   - Disponibilité, performance, et utilisation des applications.
2. **Gestion des Incidents** :
   - Temps moyen de résolution, impact des incidents critiques.
3. **Optimisation des Ressources** :
   - Analyse des coûts et des investissements nécessaires.
4. **Conformité Légale** :
   - Respect des réglementations (ex : RGPD).

</v-clicks>

---

# Bonnes pratiques

- Sélectionner uniquement les indicateurs **principaux**
- Faire le lien avec les **activités de l'entreprise**
- Permet une **stratégie** sur le **futur**
- **Adapter** le vocabulaire et les mesures au profil du destinataire
- Rappeler les unités de mesure
- Utiliser des couleurs
- **Interactivité** : utiliser des filtres ou des options de zoom pour explorer les données.

---

# À éviter

- Présenter des chiffres sans **contexte ou objectif** : stratégie, organisation, personnes
- Utiliser des données disparates sans **consolidation**
- Penser à l'automatisation des **mises à jour**
- Saisir manuellement les données

---
layout: section
---

# Indicateurs de Performance et Métriques du Parc Applicatif

---

# 🎯 Objectifs de cette partie

<v-clicks>

- Comprendre le <span v-mark.underline.red="1">rôle des indicateurs</span> de performance (KPI) dans la gestion du SI.
- <span v-mark.underline.red="2">Identifier</span> les métriques clés selon différents axes.
- Savoir <span v-mark.underline.red="3">choisir</span> les indicateurs pertinents pour un tableau de bord.

</v-clicks>

---

# Pourquoi des Indicateurs de Performance ?

<v-clicks>

- Évaluer la **performance** des applications dans le SI.
- Identifier rapidement les **points critiques** et **prioriser** les actions.
- **Suivre les objectifs stratégiques** : Alignement sur les priorités métier.

> _"Un bon indicateur est pertinent, mesurable, et exploitable."_

</v-clicks>

---

# Axes d'Analyse des Indicateurs

---

# 1. 💵 **Axe Financier**

- **Exemples** :

  - Coûts d'exploitation des applications.
  - Pourcentage d'investissements pour les évolutions.

- **Utilité** :
  Suivre la rentabilité et maîtriser les budgets.

---

# 2. 📈 **Axe Technique & Données**

- **Exemples** :

  - Taux de disponibilité (% uptime).
  - Temps moyen de résolution d'incidents.
  - Volume de données générées par mois.

- **Utilité** :
  Mesurer la fiabilité et l'efficacité opérationnelle.

---

# 3. 🔐 **Axe Sécurité**

- **Exemples** :

  - Taux de vulnérabilité détectées.
  - Fréquence des mises à jour de sécurité.

- **Utilité** :
  Garantir la résilience face aux cyberattaques.

---

# 4. 🙎 **Axe Utilisateur / Fonctionnel**

- **Exemples** :

  - Taux de satisfaction utilisateur.
  - Temps moyen passé sur l'application.
  - Accessibilité et utilisabilité.

- **Utilité** :
  Améliorer l'expérience utilisateur et l'adoption.

---

# 5. 🏛 **Axe Légal / Réglementaire**

- **Exemples** :

  - Conformité RGPD.
  - Respect des réglementations sectorielles.

- **Utilité** :
  Réduire les risques juridiques et d'amendes.

---

# Exemple d'Indicateurs Clés pour une Application

| Axe 🗃           | Indicateur 📊📈                  | Objectif 🎯            |
| --------------- | ---------------------------- | -------------------- |
| **Financier** 💵   | Coût mensuel de maintenance  | < 5% d'augmentation  |
| **Technique** 📈   | Taux de disponibilité        | 99,9 % d'uptime.     |
| **Sécurité** 🔐    | Nombre de vulnérabilités     | 0 faille critique    |
| **Utilisateur** 🙎 | Satisfaction utilisateur (%) | 90 % minimum.        |
| **Légal** 🏛       | Respect RGPD (%)             | 100 % de conformité. |

---
layout: two-cols-header
---

# Autres exemples d'indicateurs

::left::

- Taux de disponibilité des systèmes informatiques
- Temps moyen de réponse aux incidents
- Temps moyen de résolution des incidents
- Taux de satisfaction des utilisateurs
- Coût total de possession des systèmes informatiques
- Pourcentage d’incidents résolus à l'heure
- Pourcentage de demandes satisfaites dans les délais impartis

::right::

- Nombre moyen d’incidents résolus par jour
- Nombre de problèmes résolus par le personnel informatique
- Nombre de nouvelles applications informatiques déployées
- Nombre de nouvelles mises à jour des systèmes informatiques
- Taux de sécurité des données
- Taux de conformité réglementaire

---

# Bonnes Pratiques pour Choisir un Indicateur

<v-clicks>

1. **Pertinence** :
   L'indicateur doit répondre à un objectif précis.

2. **Clarté** :
   Il doit être compréhensible par tous les acteurs.

3. **Fiabilité** :
   Les données utilisées doivent être exactes et à jour.

4. **Exploitabilité** :
   Il doit permettre de prendre des décisions concrètes.

</v-clicks>

---

# SLA

- Accord de niveau de service (SLA) : engagement contractuel avec le client sur une métrique
- Indicateur à suivre par excellence

---
layout: section
---

# Construction d'un Tableau de Bord

---

# 🎯 Objectifs de cette partie

<v-clicks>

- Comprendre les étapes nécessaires pour concevoir un tableau de bord.
- Découvrir les bonnes pratiques de conception.
- Créer une structure visuelle adaptée aux besoins du SI.

</v-clicks>

---

# 1. Définir les Objectifs 🎯

- Que voulez-vous mesurer ?
- À qui s'adresse le tableau de bord ?
  - _Exemple : direction, équipe technique, utilisateurs finaux_

---

# 2. Sélectionner les Indicateurs Clés (KPI) 🗂

- Priorisez les métriques en fonction des besoins.
- Assurez-vous qu'ils soient pertinents, mesurables et exploitables.
  - _Exemple : Temps de réponse des applications, taux de disponibilité, coûts d'exploitation._

---

# 3. Concevoir la Structure 📑

- **Types de visualisations** :
  - Graphiques à barres, lignes ou secteurs.
  - Jauges pour des indicateurs spécifiques.
  - Cartes de chaleur pour des comparaisons globales.

> Limitez les visuels à l'essentiel pour éviter la surcharge.

---

# 4. Collecter et Connecter les Données 🗃

- Utilisez des outils adaptés pour centraliser les données :
  - Bases de données.
  - APIs d'applications SI.
  - Outils BI (`Power BI`, `Tableau`, etc.).

---

# 5. Tester et Valider 🧪

<v-clicks>

- Vérifiez :
  - La fiabilité des données.
  - La lisibilité des visualisations.
  - La compréhension par les utilisateurs finaux.

> Un tableau de bord n'est utile que si les utilisateurs peuvent l'exploiter facilement.

</v-clicks>

---

# Exemples de Tableaux de Bord

![](https://www.geckoboard.com/uploads/Live-customer-support-dashboard-example.png)

---

![](https://www.geckoboard.com/uploads/IT-dashboard-example.png)

---

![](https://www.geckoboard.com/uploads/sustainability-dashboard-example.png)

---
layout: section
---

# Introduction à PowerBI

---

# Types d'applications

- Power BI <span v-mark.underline.red="0">**Service**</span> <https://app.powerbi.com> : focus sur la création de <span v-mark.box="0">dashboard</span>
- Power BI <span v-mark.underline.red="0">**Desktop**</span> (à installer) : focus sur la t<span v-mark.box="0">ransformation</span> de données et la création de rapports complexes
- Power BI <span v-mark.underline.red="0">Mobile</span> : lecture des dashboards, …

---

# Glossaire Power BI

<v-clicks>

- Les données servant au suivi des indicateurs sont regroupées dans un ou plusieurs <span v-mark.underline.red="1">**modèles sémantiques**</span>.
- Un <span v-mark.underline.red="2">**rapport**</span> est une visualisation graphique d'un (et un seul) **modèle sémantique**.
- Un <span v-mark.underline.red="3">**tableau de bord**</span> (_Dashboard_) est un écran généré depuis un ou plusieurs **rapports**.

</v-clicks>

---

# Principales Visualisations Power BI  

---
layout: image-left
image: /visual-bar-chart.png
backgroundSize: contain
---

# Graphique à Barres / Colonnes

- <span v-mark.underline.red="1">Comparer des valeurs</span> entre différentes catégories.
- Mettre en évidence les <span v-mark.underline.red="1">différences</span> importantes.

## Exemple

- _**Cas pratique** : Comparaison des coûts mensuels des applications._
- _**Visualisation** : Barres verticales pour les coûts par application (janvier à décembre)._

---
layout: image-left
image: /visual-pie-chart.png
backgroundSize: contain
---

# Graphique en Secteurs

- Montrer la <span v-mark.underline.red="1">répartition</span> d'une valeur totale en pourcentages.
- Analyser les parts relatives.

## Exemple

- _**Cas pratique** : Répartition du budget SI entre les catégories (applications, matériel, personnel)._
- _**Visualisation** : Diagramme circulaire avec des segments pour chaque catégorie._

---
layout: image-left
image: /visual-line-chart.png
backgroundSize: contain
---

# Graphique en courbes

- Suivre l'<span v-mark.underline.red="1">évolution</span> d'une valeur dans le temps.
- Identifier des <span v-mark.underline.red="1">tendances</span> ou des <span v-mark.underline.red="1">variations</span>.

## Exemple

- _**Cas pratique** : Suivi du taux de disponibilité des applications mois par mois._
- _**Visualisation** : Ligne représentant l'évolution du pourcentage de disponibilité._

---
layout: image-left
	image: /basic-area-map-small.png
backgroundSize: contain
---

# Graphique en Aire

- Montrer une <span v-mark.underline.red="1">évolution</span> et l'<span v-mark.underline.red="1">accumulation</span> de valeurs.
- Mettre en évidence les <span v-mark.underline.red="1">proportions</span> dans une série temporelle.

## Exemple

- _**Cas pratique** : Volume de données générées par trois applications sur une année._
- _**Visualisation** : Aires empilées montrant les contributions cumulatives._

---
layout: image-left
image: /gauge-m.png
backgroundSize: contain
---

# Jauge

- Suivre une valeur par rapport à un <span v-mark.underline.red="1">objectif</span> ou un <span v-mark.underline.red="1">seuil</span>.
- Idéal pour des KPI simples.

## Exemple

- _**Cas pratique** : Suivi du taux d'incidents résolus par rapport à l'objectif de 95 %._
- _**Visualisation** : Une jauge montrant la progression vers l'objectif._

---

# Carte de Chaleur (Heatmap)

![](https://blog.coupler.io/wp-content/uploads/2024/03/7-power-bi-matrix-with-heatmap-1.png)

- Identifier des modèles ou des <span v-mark.underline.red="1">anomalies</span> dans des données tabulaires.
- Comparer de grandes quantités de données rapidement.
- 🚨 Attention : pas de visualisation de type _Heatmap_ par défaut dans PowerBI (à installer ou à simuler en utilisant un formattage des données). 🚨 
- _**Cas pratique** : Analyse des performances des serveurs (temps moyen de réponse)._
- _**Visualisation** : Couleurs variant du vert (bon) au rouge (mauvais)._

---
layout: image-left
image: /visual-map.png
backgroundSize: contain
---

# Carte Géographique

- Visualiser des données <span v-mark.underline.red="1">géolocalisées</span>.
- Identifier des modèles géographiques.

## Exemple

- _**Cas pratique** : Répartition des utilisateurs d'une application par région._
- _**Visualisation** : Carte avec des points ou des zones colorées selon le nombre d’utilisateurs._

---

# Tableau Croisé Dynamique (Matrice)

![](https://learn.microsoft.com/fr-fr/power-bi/visuals/media/power-bi-visualization-types-for-reports-and-q-and-a/matrix.png)
- Présenter des données <span v-mark.underline.red="1">multi-dimensionnelles</span> sous forme de tableau interactif.
- Explorer des hiérarchies.

## Exemple

- _**Cas pratique** : Analyse des coûts par département et par catégorie._
- _**Visualisation** : Tableau croisé dynamique avec lignes et colonnes imbriquées._

---
layout: section
---

# Élaboration d'une Feuille de Route (Roadmap)

---

# 🎯 Objectifs de cette partie

<v-clicks>

- Comprendre l'utilité d'une feuille de route.
- Identifier les éléments clés d'une roadmap.
- Découvrir les bonnes pratiques de conception.
- Apprendre à utiliser des outils adaptés.

</v-clicks>

---

# Roadmap

> Représentation **visuelle** et **structurée** des étapes, ressources et échéances nécessaires pour atteindre des objectifs stratégiques.

- 🎯 **Objectif principal** :
  <span v-mark.underline.red="1">Planifier l'évolution</span> des applications du SI de manière claire et réaliste.

---

# Pourquoi une Roadmap pour le SI ?

<v-clicks>

- **Planification stratégique** : définir des <span v-mark.underline.red="1">**priorités**</span> pour l'évolution des applications.
- Aligner les parties prenantes sur une <span v-mark.underline.red="2">**vision commune**</span>.
- Évaluer les <span v-mark.underline.red="3">**jalons**</span> atteints et <span v-mark.underline.red="3">**ajuster**</span> si nécessaire.

</v-clicks>
<v-clicks>

> Une roadmap claire réduit les incertitudes et améliore la coordination des équipes.

</v-clicks>

---

# Éléments Clés d'une Roadmap

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

# Bonnes Pratiques pour Construire une Roadmap

<v-clicks>

- <span v-mark.underline.red="1">**Clarté et simplicité**</span> : restez synthétique.
- <span v-mark.underline.red="2">**Réalisme**</span> : Définissez des étapes atteignables dans le temps imparti.
- <span v-mark.underline.red="3">**Évolutivité**</span> : Prévoyez des ajustements en cas d'imprévus.
- <span v-mark.underline.red="4">**Collaboration**</span> : Impliquez toutes les parties prenantes dès le début.

</v-clicks>

---

# Outils pour Créer une Roadmap

- **[Lucidchart](https://www.lucidchart.com)** : Création intuitive de diagrammes et roadmaps.
- **[Miro](https://miro.com/)** : Plateforme collaborative pour brainstorming et planification.
- **Microsoft PowerPoint / Excel** : Simples et accessibles pour des présentations rapides.
- **Outils de gestion de projet** : [Atlassian Jira](https://www.atlassian.com/software/jira), [Monday.com](https://monday.com/), …

---

# Exemple de Roadmap

- **Objectif principal** : Migration d'une application vers le cloud.

---
layout: image
image: /roadmap1.png
backgroundSize: contain
---

---
layout: image
image: /roadmap2.jpg
backgroundSize: contain
---

---
layout: image
image: /roadmap3.jpg
backgroundSize: contain
---

---
layout: two-cols
---

# Ressources

<!-- https://www.lucidchart.com/blog/what-is-a-technology-roadmap -->
<!-- https://www.productplan.com/templates/it-project-roadmap-template/ -->
<!-- https://www.productplan.com/templates/it-architecture-roadmap/ -->

## Livres

- [Pocket CIO](https://univ.scholarvox.com/catalog/book/docid/88856824)
- [Microsoft Power BI Complete Reference](https://univ.scholarvox.com/catalog/book/docid/88865488)
- [Enterprise Solution Architecture - Strategy Guide](https://univ.scholarvox.com/catalog/book/docid/88939086)

## Liens

- [MTBF, MTTR, MTTA et MTTF : Maîtriser quelques-unes des métriques d'incident les plus courantes](https://www.atlassian.com/fr/incident-management/kpis/common-metrics)
- [Atlassian - Indicateurs de performance SI](https://www.atlassian.com/fr/itsm/service-request-management/it-metrics-and-reporting)

::right::

- [Exemples : 12 tableaux de bord pour piloter ses activités informatiques][exemples-tableaux]
- [70 Exemples de dashboard](https://www.geckoboard.com/dashboard-examples/)
- [Concepts de base de Power BI](https://learn.microsoft.com/fr-fr/power-bi/consumer/end-user-basic-concepts)
- [Types de visualisations dans Power BI](https://learn.microsoft.com/fr-fr/power-bi/visuals/power-bi-visualization-types-for-reports-and-q-and-a)
- [Tutoriel : générer un rapport Power BI à partir d’un classeur Excel](https://learn.microsoft.com/fr-fr/power-bi/create-reports/service-from-excel-to-stunning-report)
- [Exemples de données pour PowerBI](https://learn.microsoft.com/fr-fr/power-bi/create-reports/sample-datasets)
- [PowerBI : essential training](https://www.linkedin.com/learning/power-bi-essential-training-17362720)
- [Power BI : Data visualization and dashboard tips and tricks](https://www.linkedin.com/learning/power-bi-data-visualization-and-dashboard-tips-tricks-techniques)
- <https://generatedata.com/> : générer des donnée de test
- [Lucidchart - Roadmap technologique](https://www.lucidchart.com/blog/fr/fonction-d-une-roadmap-technologique)

[exemples-tableaux]: https://www.journaldunet.com/solutions/dsi/1002623-12-tableaux-de-bord-pour-piloter-ses-activites-informatiques/

---
layout: end
---

<!-- class: legal -->

# Legal

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg)                                                                                        | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg)                                                                                        | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
