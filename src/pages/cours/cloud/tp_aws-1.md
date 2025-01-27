---
title: Introduction au Cloud Amazon Web Services
author: Tom Avenel
date: 2023 / 2024
---

# Remarques importantes sur l’utilisation des services `AWS` dans ce module de formation :

## La facturation des services

Une limitation forte d’`AWS` est sa complexité à limiter l’usage des services à un budget prédéfini.

De même, il n’est pas possible d’utiliser un service `AWS` sans fournir un moyen de paiement, même en utilisant les services gratuits.

Pour les différentes expérimentations de ce module, on se limitera à un usage gratuit (ou un coût très limité). Ainsi :

- Contrairement à ce qui est indiqué dans les différents sujets de TP, et afin d’éviter aux apprenants de devoir fournir un moyen de paiement pour réaliser la formation, les apprenants pourront (sauf choix contraire de leur part) utiliser le compte `AWS` commun fourni par le formateur (avec un utilisateur qui leur sera dédié).
- On sera donc particulièrement vigilant sur l’usage et **la facturation des différents services** :
  + **Arrêter et détruire les instances de services qui ne sont plus utilisés**
  + Pour les expérimentations, on choisira toujours **les versions minimales des serveurs** (qui suffisent amplement à nos cas d’utilisation)
  + Le formateur se réserve le droit de détruire toute instance de service dont l'utilisation dépasserait un budget raisonnable

## Le partage des services

Pour les apprenants ayant fait le choix d’utiliser le compte commun fourni par le formateur, il faut être conscient qu’`AWS` partage toutes les instances de ses services au sein d’un même compte (cependant, l’utilisation de droits appropriés peut permettre de masquer certaines instances).

On prendra bien soin de **nommer chaque instance avec un suffixe spécifique à l’apprenant**, pour éviter les conflits de nommage entre apprenants, mais aussi pour retrouver ses propres instances et ne pas se les faire supprimer par un autre utilisateur !

## La cohérence du système

`AWS` est un ensemble extrêmement vaste et complexe de services, dont la cohérence peut rapidement être mise à mal.

De plus, les différentes opérations que nous allons exécuter sur le datacenter `AWS` (Créer une instance, la sauvegarder, ...) peuvent prendre un certain temps. Pour éviter toute incohérence dans le système, on s'assurera de **bien attendre la fin des différentes opérations**.

De même, on prendra le temps de **bien lire et comprendre les consignes** de chaque étape des différentes parties pratiques, car une incohérence dans le système implique généralement de tout nettoyer pour reprendre l’étape courante, voir les étapes précédentes.

## Les nouvelles interfaces `AWS`

De nombreux services `AWS` (`EC2`, `S3`, …) ont bénéficié récemment d’une refonte globale de leur interface utilisateur récemment. Si cette interface est plus simple à utiliser, ce n'est pas celle qui est décrite dans les différents tutoriels. Le passage à la nouvelle interface est généralement assez trivial à comprendre, mais en cas de doute on pourra revenir à l'interface précédente grâce au switch en haut à gauche de l’écran :

![](./switch-interface.png)

# TP `AWS` 1. Introduction au Cloud Amazon (`EC2`, `S3`, `RDS`) : les services de base d’un Cloud

Dans ce premier TP Amazon Web Services, nous allons découvrir ce qu'est concrètement un fournisseur de services Cloud, comment `AWS` modélise le Cloud et les services qu'il fournit pour mettre en place une infrastructure distante permettant l'hébergement d’un site Web.

Pour réaliser l'ensemble de cette partie pratique, on utilisera comme support le (très bon) [tutoriel OpenClassrooms][intro-aws].

Note : Dans l'ensemble de ce TP, on utilise comme exemple une application `PHP` fourni en exemple. On pourra remplacer cet exemple par une autre application de notre choix.

## Partie 1 :  Introduction aux services `AWS`

Le but de cette première partie est de se familiariser avec le Cloud et la console `AWS`.

- Réaliser les étapes du tutoriel OpenClassrooms: [Premiers pas dans la console `AWS`][premiers-pas] à [Créer un serveur facilement avec Elastic Beanstal][beanstal-quizz]. Répondre et s'arrêter au quizz.

Note : Pour les apprenants utilisant le compte commun, il n’est pas nécessaire de définir un budget (celui-ci est déjà défini au niveau du compte).

## Partie 2 :  EC2 : Infrastructure-as-a-Service (IaaS)

Le but de cette partie est de d’utiliser les principaux services d’IaaS d’Amazon (`EC2` notamment)

- Commencer par supprimer le service `BeanStalk` créé lors de la première partie
- Réaliser les étapes : [Introduction aux services d'Amazon EC2](https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/4871326-introduction-aux-services-damazon-ec2) à [Sauvegarder et restaurer une instance](https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/exercises/2269). Répondre et s'arrêter au quizz.

**Note 1 : Au lancement de l'instance de la VM (Etape 7 d'EC2), vérifier que le coût de l'instance est nul**

![](./cout-instance.png)


Note 2 : Pour vérifier le bon lancement de la stack `LAMP` dans le serveur, on peut essayer d’atteindre l'URL du `DNS` publique du serveur dans un navigateur (ce nom `DNS` peut être récupéré depuis l’instance du serveur qui héberge la stack `LAMP`, dans `EC2`).

Par exemple : <http://ec2-35-181-153-53.eu-west-3.compute.amazonaws.com/>

![](lamp.png)

Note 3 : Contrairement à ce qui est annoncé dans le sujet du TP, l'utilisateur à utiliser pour la connexion `SSH` n’est pas `ubuntu` mais `bitnami`.

## ` `Partie 3 : Intégrer des services Cloud (1) : `RDS`, le `DBaaS` d'`AWS`

Réaliser les étapes : [Pourquoi utiliser RDS](https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/5017546-pourquoi-utiliser-rds) à [Utiliser RDS depuis son serveur web EC2](https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/exercises/2272). Répondre et s'arrêter au quizz.


## Partie 4 : Intégrer des services Cloud (2) : `S3`, le service de stockage d'`AWS`

- Finir les dernières étapes du TP depuis l’étape : [Qu’est-ce que Simple Storage Service (S3)](https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/5038626-quest-ce-que-simple-storage-service-s3).

Note : Les noms des buckets `S3` sont très sensibles à la casse et aux caractères spéciaux : préférer un nom entièrement en minuscule et sans caractère spécial !

[intro-aws]: https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/4819941-premiers-pas-dans-la-console-aws
[premier-pas]: http://ttps://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/4819941-premiers-pas-dans-la-console-aws
[beanstal-quizz]: https://openclassrooms.com/fr/courses/4810836-decouvrez-le-cloud-avec-amazon-web-services/exercises/2087

---

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- “Amazon Web Services", the “Powered by Amazon Web Services” logo, Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), Amazon Relational Database Service (Amazon RDS) are trademarks of Amazon.com, Inc. or its affiliates in the United States and/or other countries
