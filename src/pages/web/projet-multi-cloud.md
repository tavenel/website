---
title: Exécution de programmes dans un environnement Cloud multi-provider
date: 2023 / 2024
tags:
- cloud
---

## Contexte du projet

L'utilisation massive d'architectures de type Client/Serveur au sein de réseaux `TCP/IP` a permis de déporter une grande partie de l'infrastructure de certaines entreprises vers des offres Cloud.
Les différents fournisseurs de Cloud permettent ainsi de rationaliser une partie des ressources d'infrastructure au sein de déploiements uniques, et peuvent être amenés à coopérer entre eux pour étendre leur offre de services.

Dans ce projet, chaque groupe représente un fournisseur de Cloud différent, ayant sa propre solution de Cloud et ses propres clients.

Les fonctionnalités offertes par les différents fournisseurs de Cloud sont cependant identiques : un système d'exécution de différents types de programmes fournis par les clients, et un système de notification des résultats par mail (voir ci-dessous).


### Exécution des programmes clients :

#### Types de fichiers

Chaque fournisseur de Cloud propose un service d'exécution de programmes légers :

- fichier de script à exécuter (script `Bash` sous Linux ou script `Batch` sous Windows)
- fichier de script `Python` à exécuter (fichier unique sans dépendance)

#### Fichier annexe descripteur

En plus du fichier contenant le programme en lui-même (exemple : `mon_programme.sh`), un deuxième fichier sera également fourni par le client. Ce fichier contiendra les paramètres à passer au programme, le type de programme à exécuter, et une adresse mail de réponse.

#### Environnement d'exécution

Afin de rationaliser les coûts d'infrastructure, les différents fournisseurs de Cloud se sont entendus pour partager leurs ressources. Ainsi, les programmes ne seront pas exécutés sur la plateforme du fournisseur ayant récupéré le fichier, mais sur n'importe quelle plateforme ayant des ressources disponibles.

#### Résultats d'exécution

Le résultat de l'exécution du programme devra être envoyé par mail par le fournisseur de Cloud ayant exécuté le programme sur ses machines, à l'adresse fournie par le client dans le fichier annexe au programme.


### Notes générales :

- On ne demande pas de mettre en place un service de tarification / gestion de quotas / … que ce soit par rapport aux utilisateurs finaux ou pour la coopération entre fournisseurs de Cloud.
- Pour pouvoir exécuter les programmes des clients dans différents environnements, on utilisera au minimum 2 environnements d'exécution par groupe (serveur, machine personnelle, machine virtuelle, ...) dont au moins une machine Windows et une machine Linux.
- A terme, il est prévu d'ajouter à chaque fournisseur de Cloud un nouvel environnement d'exécution spécifique à lui seul (par exemple : `Java`, `C`, `C#`, …). Les clients de chaque fournisseur de Cloud pourront déposer des programmes de ces nouveaux environnements, qui seront automatiquement transférés sur le seul site capable de les exécuter. Il n'est pas demandé d'implémenter ce nouveau cas, mais la future norme doit être rétro-compatible avec la norme actuelle.

## Travail attendu

Il est attendu, par groupe de 5 apprenants :

- La mise en place de l'infrastructure supportant ce projet
- La possibilité, par déploiement de solutions applicatives ou par développement d'une solution dédiée, de coopération avec les autres plateformes de Cloud
- Une interface utilisateur dédiée aux clients du groupe
- L'envoi automatique de mail de résultat au client (on pourra utiliser l'adresse mail de l'un des apprenants du groupe comme expéditeur)

Il n'est pas demandé de réaliser un déploiement de production mais plutôt un prototypage. L'utilisation de machines personnelles comme environnement d'exécution est accepté.

L'ensemble des groupes fournisseurs de services Cloud devra également s'entendre sur un ensemble de normes à respecter pour pouvoir faire interagir les différents sites.

## Rendus attendus

Il est attendu, par groupe de 5 apprenants :

- Une copie de la norme permettant la coopération entre les différents fournisseurs de Cloud (commune à tous les groupes)
- Un rapport de projet décrivant :
  + l'infrastructure mise en place 
  + les choix d'architecture (différents composants déployés et leur utilité)
  + les différentes applications client/serveur sur `TCP/IP` déployées dans ce projet
- Des copies d'écran des interface(s) utilisateur(s)
- Le code source du ou des programmes d'interface(s) utilisateur(s)
- Le code source du ou des programmes internes, s'ils existent
- Les fichiers de configuration des différents services
- Un email de résultat d'exécution sera envoyé à l'adresse du formateur par l'ajout de cette adresse mail dans un fichier annexe d'un court script choisi par le groupe. L'expéditeur de ce mail devra être l'adresse d'un des apprenants du groupe.

Il n'est pas demandé d'accès au déploiement final de la solution.

