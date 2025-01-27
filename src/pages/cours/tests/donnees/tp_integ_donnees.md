---
title: Intégration de données depuis différents sites
date: 2023 / 2024
---

# Cas pratique 1 : Intégration de données depuis différents sites

> Dans ce premier cas pratique, nous allons mettre en place des tests d'intégration de données pour valider le rapatriement de toutes les données des employés d'une entreprise.

Le but de ce cas pratique est de valider la fusion des données éparses déjà récupérées.

## Contexte

Au cours de son évolution, le S.I de l'entreprise a évolué à de nombreuses reprises. Ce S.I a notamment possédé 3 différents systèmes d'archivage notés `20_1`, `20_2`, `20_3`.

Afin de rationaliser les données de ses employés depuis la création de l'entreprise, il a été décidé d'intégrer les différentes données des employés dans un même format `XML` dans une archive unique.

## Récupération des données de production

Afin de simplifier ce cas pratique, les différentes données des employés ont été récupérées sur les différents sites au format `XML` et sont disponibles dans une archive : <https://cloud.leviia.com/s/ZnIx.faPETT7DDxcoBAC> (_données de test fictives générées par Fusheng Wang and Carlo Zaniolo at Siemens Corporate Research_).

Cette archive contient :

* les schémas des employés et des départements au format `xsd`
* les données des départements dans un fichier unique : `departements.xml`.
* les données des employés récupérés sur les 3 systèmes d'archivage (un dossier par système d'archivage) : `20_1`, `20_2`, `20_3`

Toutes les données sont censées avoir suivi un schéma commun depuis la création du S.I. de l'entreprise validé par les schémas `xsd` (un fichier `xsd` définit un schéma de données dans un fichier XML : cela permet de s'assurer que le type des données est bien celui attendu).

## Résultats attendus

- Explications sur la stratégie de tests : identification des techniques de tests, des critères de complétion des tests.
- Définition des scénarios et cas de tests
- Conception d'un plan de tests
- Pour chaque type de test :
  + Description du test, explications sur son implémentation et son exécution
  + Si non implémenté ou exécuté, explications des raisons
  + Données utilisées (connues ? contrôlées ? ...)
- Explications des défaillances et anomalies éventuellement relevées ainsi que les solutions apportées
- Présentation de la recette
- Les scripts d'automatisation des tests (si automatisation)
- Suite à la réalisation de ces tests, quels sont vos conclusions sur l'intégration de ces données ?


