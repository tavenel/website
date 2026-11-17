---
title: 󱃾 Tom Avenel - M1 Devops Avancé
layout: '@layouts/BaseLayout.astro'
---

# Devops avancé

## 📑 Documents

- [🤓 Cours sur le Devops](/esgi/m1/devops/cours)
- [🏆 Projet Devops](/devops/projet-new)

## Ressources

- Gestionnaire de versions : voir les rappels du [cours Git](/git)
- Voir les autres ressources du [cours sur le devops](/devops).
- Intégration continue et déploiement continu : voir le [cours CI/CD](/ci)
- Conteneurs Docker & Kubernetes : voir le [cours Docker](/docker)

## Organisation générale

Les deux promotions travaillent sur une application multi-composants (frontend, backend, base de données), destinée à être déployée dans un environnement de type production.

Une contrainte fondamentale du projet est que **les applications produites par les équipes Développeurs doivent pouvoir être déployées sur les infrastructures fournies par n'importe quelle équipe Administrateurs système**, indépendamment des spécificités de leur plateforme Cloud.

## Module M1 SRC et SI

**Volume horaire : 15 heures**

Objectif : Concevoir, automatiser et maintenir l'infrastructure Cloud. Vous devrez fournir une **plateforme Cloud opérationnelle, reproductible et indépendante des applications métier**.

### Objectifs pédagogiques

1. **Concevoir une infrastructure Cloud adaptée au déploiement d'applications conteneurisées**
   - Définir une architecture permettant d'héberger des applications Docker.
   - Mettre en place un environnement de production reposant sur Kubernetes et deux machines virtuelles.
   - Préparer un environnement de test ou de staging.

2. **Déployer et administrer une plateforme de conteneurisation**
   - Installer et configurer Docker et Kubernetes.
   - Mettre en place un cluster Kubernetes opérationnel.
   - Gérer les ressources, les services et les déploiements applicatifs.

3. **Mettre en œuvre une approche Infrastructure-as-Code**
   - Automatiser l'installation et la configuration des environnements avec Ansible.
   - Automatiser le déploiement et la configuration des composants techniques.
   - Versionner les configurations et scripts d'infrastructure dans Git.
   - Garantir la reproductibilité des environnements.

4. **Préparer une infrastructure adaptée aux contraintes de production**
   - Permettre le déploiement de conteneurs applicatifs provenant de différentes équipes.
   - Préparer le support de l'auto-scaling Kubernetes.
   - Permettre les mises à jour applicatives sans interruption de service.
   - Définir les interfaces nécessaires à l'intégration des applications.

5. **Mettre en place les outils d'observabilité**
   - Déployer Prometheus et Grafana.
   - Superviser les ressources système et les conteneurs.
   - Mettre en place un tableau de bord de supervision.
   - Participer à la centralisation des logs.

### Grille d'évaluation

| Critère d'évaluation | Pondération |
| --- | ---: |
| Conception et architecture de l'infrastructure | 4 |
| Installation et configuration de la plateforme Kubernetes | 5 |
| Automatisation et reproductibilité avec Ansible / Terraform | 6 |
| Gestion des contraintes de production (scaling, mises à jour) | 1 |
| Observabilité et supervision | 2 |
| Documentation, intégration interéquipes | 2 |
| **Total** | **20** |

## Module M1 AL et IW et IADB

**Volume horaire : 15 heures**

Objectif : Productiviser une application et automatiser son cycle de livraison. Vous devrez fournir une **application multi-composants conteneurisée et déployable automatiquement sur les différentes plateformes Cloud proposées par les équipes SysOps**.

### Objectifs pédagogiques

1. **Préparer une application adaptée à un déploiement en production**
   - Identifier les différents composants d'une application multi-composants.
   - Organiser le code source dans un ou plusieurs dépôts Git.
   - Préparer une architecture applicative adaptée à une exécution conteneurisée.
   - Séparer la configuration de l'application de son code source.

2. **Conteneuriser une application**
   - Écrire les Dockerfiles nécessaires à chaque composant métier.
   - Construire et tester les images Docker.
   - Gérer les dépendances entre les composants.
   - Publier les images dans une registry.
   - Garantir la portabilité des images entre les différentes infrastructures Cloud.

3. **Mettre en place une intégration continue (CI)**
   - Configurer un pipeline CI/CD.
   - Automatiser les contrôles de qualité, le lint et les tests.
   - Automatiser la génération des images Docker.
   - Publier automatiquement les images dans une registry.
   - Versionner la configuration du pipeline.

4. **Mettre en place un déploiement continu (CD)**
   - Déployer l'application dans un environnement de staging.
   - Préparer les manifests Kubernetes nécessaires au déploiement en production.
   - Automatiser le déploiement des nouvelles versions.
   - Mettre en œuvre une stratégie de mise à jour sans interruption de service.

5. **Préparer l'application à son exploitation en production**
   - Configurer les paramètres et dépendances externes de l'application.
   - Prévoir les mécanismes de vérification de disponibilité des services.
   - Préparer l'application à supporter l'auto-scaling.
   - Faciliter l'exploitation et le diagnostic à travers les logs et les métriques applicatives.

### Grille d'évaluation

| Critère d'évaluation | Pondération |
| --- | ---: |
| Qualité et fonctionnement de l'application multi-composants | 3 |
| Conteneurisation et portabilité des images Docker | 5 |
| Intégration continue et automatisation des tests | 4 |
| Déploiement continu et intégration Kubernetes | 4 |
| Prise en compte des contraintes de production (zéro-downtime, scaling) | 2 |
| Documentation, intégration interéquipes | 2 |
| **Total** | **20** |

## Résultat global attendu

À l'issue des deux modules, le projet devra donc permettre de démontrer une chaîne complète de livraison et d'exploitation applicative.

Le scénario de démonstration attendu est le suivant :

1. Un développeur modifie le code source de l'application.
2. Il publie un commit dans le dépôt Git.
3. Le pipeline CI/CD exécute les contrôles qualité et les tests.
4. Les images Docker sont construites et publiées dans la registry.
5. Le déploiement de l'application est déclenché automatiquement ou semi-automatiquement.
6. L'application est déployée sur une infrastructure Kubernetes fournie par une équipe SysOps.
7. Une mise à jour applicative est réalisée sans interruption de service.
8. L'application peut bénéficier d'un mécanisme d'auto-scaling.
9. Le fonctionnement de l'application et de l'infrastructure est observable depuis Grafana.
10. Les logs des différents composants sont consultables depuis une solution centralisée, si celle-ci a été mise en place.
