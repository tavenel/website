---
title: Introduction au Cloud Amazon Web Services
date: 2023 / 2024
tags:
- aws
- cloud
---

# Remarques importantes sur l'utilisation des services `AWS` dans ce module de formation :

## La facturation des services

Une limitation forte d'`AWS` est sa complexité à limiter l'usage des services à un budget prédéfini.

De même, il n'est pas possible d'utiliser un service `AWS` sans fournir un moyen de paiement, même en utilisant les services gratuits.

Pour les différentes expérimentations de ce module, on se limitera à un usage gratuit (ou un coût très limité). Ainsi :

- Contrairement à ce qui est indiqué dans les différents sujets de TP, et afin d'éviter aux apprenants de devoir fournir un moyen de paiement pour réaliser la formation, les apprenants pourront (sauf choix contraire de leur part) utiliser le compte `AWS` commun fourni par le formateur (avec un utilisateur qui leur sera dédié).
- On sera donc particulièrement vigilant sur l'usage et **la facturation des différents services** :
  + **Arrêter et détruire les instances de services qui ne sont plus utilisés**
  + Pour les expérimentations, on choisira toujours **les versions minimales des serveurs** (qui suffisent amplement à nos cas d'utilisation)
  + Le formateur se réserve le droit de détruire toute instance de service dont l'utilisation dépasserait un budget raisonnable

## Le partage des services

Pour les apprenants ayant fait le choix d'utiliser le compte commun fourni par le formateur, il faut être conscient qu'`AWS` partage toutes les instances de ses services au sein d'un même compte (cependant, l'utilisation de droits appropriés peut permettre de masquer certaines instances).

On prendra bien soin de **nommer chaque instance avec un suffixe spécifique à l'apprenant**, pour éviter les conflits de nommage entre apprenants, mais aussi pour retrouver ses propres instances et ne pas se les faire supprimer par un autre utilisateur !

## La cohérence du système

`AWS` est un ensemble extrêmement vaste et complexe de services, dont la cohérence peut rapidement être mise à mal.

De plus, les différentes opérations que nous allons exécuter sur le datacenter `AWS` (Créer une instance, la sauvegarder, ...) peuvent prendre un certain temps. Pour éviter toute incohérence dans le système, on s'assurera de **bien attendre la fin des différentes opérations**.

De même, on prendra le temps de **bien lire et comprendre les consignes** de chaque étape des différentes parties pratiques, car une incohérence dans le système implique généralement de tout nettoyer pour reprendre l'étape courante, voir les étapes précédentes.

## Les nouvelles interfaces `AWS`

De nombreux services `AWS` (`EC2`, `S3`, …) ont bénéficié récemment d'une refonte globale de leur interface utilisateur récemment. Si cette interface est plus simple à utiliser, ce n'est pas celle qui est décrite dans les différents tutoriels. Le passage à la nouvelle interface est généralement assez trivial à comprendre, mais en cas de doute on pourra revenir à l'interface précédente grâce au switch en haut à gauche de l'écran :

# TP `AWS` 1. Introduction au Cloud Amazon (`EC2`, `S3`, `RDS`) : les services de base d'un Cloud

Dans ce premier TP Amazon Web Services, nous allons découvrir ce qu'est concrètement un fournisseur de services Cloud, comment `AWS` modélise le Cloud et les services qu'il fournit pour mettre en place une infrastructure distante permettant l'hébergement d'un site Web.

Pour réaliser l'ensemble de cette partie pratique, on utilisera comme support le (très bon) [tutoriel OpenClassrooms](https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/4819941-premiers-pas-dans-la-console-aws)
Note : Dans l'ensemble de ce TP, on utilise comme exemple une application `PHP` fourni en exemple. On pourra remplacer cet exemple par une autre application de notre choix.

Note : Pour les apprenants utilisant le compte commun, il n'est pas nécessaire de définir un budget (celui-ci est déjà défini au niveau du compte).

**Note : Au lancement de l'instance de la VM (Etape 7 d'EC2), vérifier que le coût de l'instance est nul**

Note : Pour vérifier le bon lancement de la stack `LAMP` dans le serveur, on peut essayer d'atteindre l'URL du `DNS` publique du serveur dans un navigateur (ce nom `DNS` peut être récupéré depuis l'instance du serveur qui héberge la stack `LAMP`, dans `EC2`).

Par exemple : `http://ec2-35-181-153-53.eu-west-3.compute.amazonaws.com/`

![La page d'accueil du serveur LAMP](@assets/apps/lamp.png)

<div class="caption">La page d'accueil du serveur LAMP.</div>

:::tip
Note : Les noms des buckets `S3` sont très sensibles à la casse et aux caractères spéciaux : préférer un nom entièrement en minuscule et sans caractère spécial !
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- "Amazon Web Services", the "Powered by Amazon Web Services" logo, Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), Amazon Relational Database Service (Amazon RDS) are trademarks of Amazon.com, Inc. or its affiliates in the United States and/or other countries
