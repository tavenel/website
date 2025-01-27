---
title: Gestion d'une pharmacie
date: 2023 / 2024
correction: false
---

## Gestion d’une pharmacie

On s'intéresse à la gestion d'une pharmacie qui gère des clients et des produits.

Une _pharmacie_ est caractérisée par son _nom_ (`str`), son _adresse_ (de type `str`), ses _clients_ (liste de `clients`) et ses _produits_ (liste de `produits`).
Un _client_ est caractérisé par son _nom_ (`str`), son _prénom_ (`str`), le _numéro de sa carte vitale_ (`int`).
Un _produit_ est caractérisé par sa _référence_ (`str`) et son _prix_ (`float`).
Les produits que vend cette pharmacie sont soit des _médicaments_, soit des produits de _parapharmacie_.
Les _médicaments_ sont caractérisés par le fait qu’ils peuvent être _génériques_ ou pas, et par le fait qu’ils peuvent être délivrés _sans ordonnance ou pas_.
Les produits de _parapharmacie_ sont quant à eux caractérisés par leur _type de produit_ : _produit de beauté_, _cosmétique_ ou _diététique_.

Le programme doit permettre les opérations de gestion de la pharmacie suivantes :

- L'opération d'_achat_ caractérisée par un produit, un client et une quantité.
- L'opération d'_approvisionnement_ du stock caractérisée par un produit et une quantité.
- L'affichage de la liste des clients de la pharmacie et la liste des produits qu’elle vend.
- L'affichage des informations concernant le client.
- L'affichage des informations concernant un produit.
- L'affichage des informations concernant un médicament.
- L'affichage des informations concernant un produit de parapharmacie.

## Modélisation

Proposer une modélisation orientée objet permettant la gestion d'une pharmacie : donner les classes, leurs attributs et leurs méthodes sous forme d'un schéma, en précisant les relations entre les classes (en utilisant : `hérite de` et `utilise`).
Il n’est pas demandé de donner l'implémentation des méthodes (seulement leur prototype, c'est-à-dire leur nom, le type des arguments en entrée et le type de retour).
Il n'est pas non plus demandé de formalisme strict (type UML) mais plutôt un schéma clair du contenu des classes et de leurs interactions.

## Implémentation

Implémenter en Python la modélisation orientée objet proposée. Pour vérifier cette implémentation, créer une instance de la pharmacie et des instances de clients, de produits, ... Vérifier ensuite le bon déroulement des opérations de gestion de la pharmacie en utilisant ces instances.

