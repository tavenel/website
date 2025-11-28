---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Relations entre équipes
tags:
- gestion_projet
- management
- agile
- topology
---

![Photo de l'intérieur d'un PC portable](@assets/sysadmin/EBMotherboard.jpg)

<div class="caption">Photo de l'intérieur d'un PC portable. By <a href="https://en.wikipedia.org/wiki/User:Ravenperch" class="extiw" title="wikipedia:User:Ravenperch">Ravenperch</a> at <a href="https://en.wikipedia.org/wiki/" class="extiw" title="wikipedia:">English Wikipedia</a> - <span class="int-own-work" lang="en">Own work</span> (<span lang="en" dir="ltr">Original text: Self created</span>), <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=18540450">Link</a></div>

À votre avis, quelles sont les différentes équipes à travailler sur la réalisation de cet ordinateur ?

---

### Loi de Conway

> Les organisations produisent des systèmes qui reflètent leur structure de communication

- Exemple :
  - _facturation_
  - _gestion des stocks_
  - _gestion des comptes_

---

### Team topologies

La topologie d'équipe est une théorie de management d'équipes très populaire en Devops, Agilité et DDD. Elle a été formalisée par _Manuel Pais_ et _Matthew Skelton_ pour décrire les spécialisations et interactions entre sous-équipes d'un projet.

- Idée : refléter le découpage en composants dans le découpage des équipes
- **Team Topologies** : pattern d'organisation complémentaire au DDD
  - inverse de la loi de Conway (adapter l'organisation aux modules et pas l'inverse)

---

## Types d'équipes

---

### Stream-aligned Team

- Type d'équipe de base : **autonome** et **pluridisciplinaire** (ex : _SCRUM_)
- Travaille sur un **flux de valeur** (ex : produit)
- Pas obligatoirement au contact des utilisateurs finaux (ex : utilisateurs internes)

---

### Enabling Team

- Ne produisent pas directement de la valeur
- En **support continu des autres équipes**
- **Transverses**
- Souvent une posture de coach : font monter en compétence les autres équipes

---

### Complicated-Subsystem Team

- **Experts techniques** (donc rarement experts produit)
- Ni _Stream-aligned_ ni _Enabling_ Team
- Équipe spécialisée, se concentre sur un aspect technique complexe
- Isolées pour ne pas être dérangées : Peuvent être problématiques et devenir des _Component team_
- À utiliser en dernier recours

---

### Plateform Team

- Fournissent une plateforme, un service ou une abstraction de ces services.
- Simplifient les choses pour les _Stream-Aligned Team_
- Exemple: abstraction k8s

---

## Interactions entre équipes

---

### Collaboration

- 2 équipes travaillent **ensemble** : beaucoup d'**interaction**
- Compliqué si beaucoup de personnes
- Accélère l'**innovation**
- Recommandé comme **interaction de départ**

---

### X-as-a-service

- Analogie avec l'acronyme "Software-As-A-Service"
- Permet une relation d'**autonomie** des équipes
- Relation **client / fournisseur** entre deux équipes, souvent **formalisée**

---

### Facilitating

- Pour aider des équipes
- ex : coachs, mentors, _Enabling Teams_

---

## Dépendances

---

### Dépendance mutuelle

- Dépendance mutuelle (en DDD : Shared Kernel)
- Relation **succès/échec partagée**
  - besoin de **collaboration forte**
  - relation de **partenariat**

---

### Dépendance Upstream / Downstream

- **Upstream impacte le succès Downstream**
- Downstream n'impacte pas le succès Upstream
  - soit : collaboration par **requêtes** (en DDD : envie du _Customer_ à remonter au _Supplier_), pas par ~~exigence (besoin)~~
  - soit : API publique (en DDD : _Open Host Service_) indépendant du consommateur (le _Customer_ doit s'adapter au _Supplier_)

:::link
Pour plus d'information, voir le site officiel : <https://teamtopologies.com>
:::

---
