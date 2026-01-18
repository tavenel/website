---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Introduction aux Virtual Data Center
layout: '@layouts/CoursePartLayout.astro'
---

## Objectifs

- Définir le concept de Virtual Data Center (VDC)
- Expliquer les motivations techniques et économiques des VDC
- Identifier les composants clés d'un VDC
- Comparer un data center traditionnel, un VDC et des environnements cloud
- Comprendre les cas d'usage typiques en entreprise

---

## Du data center traditionnel à la virtualisation

### Data center traditionnel

Un data center traditionnel repose sur :

- Des serveurs physiques dédiés
- Des équipements réseau matériels (switches, routeurs, firewalls)
- Des baies de stockage physiques

Limites principales :

- Faible taux d'utilisation des ressources
- Manque de flexibilité
- Déploiements lents
- Coûts d'exploitation élevés

### Introduction à la virtualisation

La virtualisation permet d'abstraire le matériel physique afin de :

- Mutualiser les ressources
- Isoler les charges de travail
- Simplifier l'administration

Types de virtualisation :

- Virtualisation de calcul (VM)
- Virtualisation réseau
- Virtualisation du stockage

---

## Virtual Data Center (VDC)

Un Virtual Data Center est une représentation logique et entièrement virtualisée d'un data center physique. Il regroupe :

- Des ressources de calcul
- Des ressources réseau
- Des ressources de stockage

Ces ressources sont provisionnées, isolées et administrées de manière logicielle.

### Objectifs d'un VDC

- Fournir un data center "as a service"
- Garantir l'isolation entre tenants
- Offrir élasticité et automatisation
- Simplifier la gouvernance et la facturation interne

---

## Composants d'un VDC

### Calcul (Compute)

- Machines virtuelles (VM)
- Pools de ressources (CPU, RAM)
- Clusters de virtualisation

Exemples de technologies :

- VMware vSphere
- KVM / Proxmox
- Hyper-V

### Réseau (Network)

- Réseaux virtuels (VLAN, VXLAN)
- Routeurs et firewalls virtuels
- Load balancers virtuels

Concepts clés :

- Software Defined Networking (SDN)
- Micro-segmentation

### Stockage (Storage)

- Datastores virtualisés
- Stockage distribué
- Politiques de stockage (performance, réplication)

Exemples :

- vSAN
- Ceph
- SAN/NAS virtualisés

### Gestion et orchestration

- Portails d'administration
- APIs
- Automatisation et Infrastructure as Code (IaC)

---

## VDC et cloud computing

Le VDC est un concept fondamental du cloud, notamment dans le cloud privé et le cloud hybride.
Un cloud public peut être vu comme une fédération de VDC multi-tenants.

| Critère         | Data Center traditionnel | VDC          | Cloud public |
| --------------- | ------------------------ | ------------ | ------------ |
| Provisionnement | Manuel                   | Automatisé   | Automatisé   |
| Élasticité      | Faible                   | Élevée       | Très élevée  |
| Facturation     | CAPEX                    | CAPEX / OPEX | OPEX         |
| Isolation       | Physique                 | Logique      | Logique      |

:::tip
Le **CAPEX** correspond aux dépenses d'investissement visant à **acheter et posséder des infrastructures** sur le long terme (serveurs, stockage, réseau, licences), avec un coût initial élevé amorti dans le temps, comme dans un data center traditionnel, tandis que l'**OPEX** désigne les dépenses d'exploitation liées à la **consommation d'un service** (énergie, maintenance, abonnements, cloud), facturées de manière récurrente et plus flexibles ; dans un **Virtual Data Center**, l'infrastructure reste généralement financée en CAPEX par l'IT centrale, mais les équipes consommatrices perçoivent un modèle proche de l'OPEX via une facturation à l'usage, approche qui devient quasi exclusive dans le cloud public.
:::

---

## Cas d'usage

### En entreprise

- Environnements de test / recette / production
- Mutualisation entre équipes
- Self-service IT

### Chez les fournisseurs de services

- Hébergement multi-clients
- Offres IaaS
- Segmentation par client (tenant)

### Dans la formation

- Plateformes pédagogiques
- Laboratoires virtuels
- Environnements temporaires

---

## Avantages et limites

### Avantages

- Flexibilité et agilité
- Meilleure utilisation des ressources
- Déploiement rapide
- Isolation et sécurité

### Limites

- Complexité de mise en œuvre
- Dépendance aux outils logiciels
- Coûts de licences possibles
- Besoin de compétences spécialisées

---

## Exemples de solutions

- VMware vCloud Director
- OpenStack
- Microsoft Azure Stack
- OpenNebula (open source)
- Proxmox VE (approche simplifiée)

---

## Pour aller plus loin : SDDC

Le **Software-Defined Data Center (SDDC)** est une évolution du data center dans laquelle **l'ensemble de l'infrastructure est piloté par logiciel** : calcul, réseau, stockage et sécurité sont entièrement virtualisés, abstraits du matériel et provisionnés à la demande via des APIs et des outils d'automatisation. L'objectif est d'obtenir un data center **élastique, programmable et automatisé**, proche du fonctionnement du cloud, permettant des déploiements rapides, une meilleure utilisation des ressources et une gestion centralisée, tout en pouvant rester hébergé on-premise ou en cloud privé.

---
