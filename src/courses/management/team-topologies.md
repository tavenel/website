---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Team Topologies
tags:
- gestion_projet
- management
- agile
- topology
---

La topologie d'équipe est une théorie de management d'équipes très populaire en Devops, agilité et DDD. Elle a été formalisée par _Manuel Pais_ et _Matthew Skelton_ pour décrire les spécialisations et interactions entre sous-équipes d'un projet.

:::link
Pour plus d'information, voir le site officiel : <https://teamtopologies.com>
:::

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
- Les CoP pourraient être des enabling team [TODO]

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

### X-a-a-service

- Analogie avec l'acronyme "Software-As-A-Service"
- Permet une relation d'**autonomie** des équipes
- Relation **client / fournisseur** entre deux équipes, souvent **formalisée**

---

### Facilitating

- Pour aider des équipes
- ex : coachs, mentors, _Enabling Teams_

---

