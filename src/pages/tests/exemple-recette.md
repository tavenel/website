---
title: Exemple de Cahier de Recette Fonctionnelle
date: 2025 / 2026
---

Le cahier de recette sert de **référence contractuelle** entre le métier et l'équipe technique.
Il formalise **ce qui doit fonctionner**, **comment vérifier**, et **à partir de quand le produit est jugé acceptable**.


## 1. Présentation du projet

**Nom du projet :**
**Version :**
**Date :**
**Responsable recette :**
**Équipe projet :**

**Description succincte :**
Brève explication de l'application ou du système testé et de son objectif métier.

## 2. Objectifs de la recette

La recette fonctionnelle a pour objectif de :

* Vérifier la conformité aux besoins métier
* Valider les fonctionnalités principales
* Détecter les anomalies bloquantes avant mise en production
* Garantir l'acceptation par les utilisateurs finaux

## 3. Périmètre de test

### Inclus

* Fonctions utilisateur principales
* Interfaces critiques
* Règles de gestion métier

### Exclus

* Tests de performance
* Tests de sécurité avancés
* Tests techniques internes (code, architecture)

## 4. Environnement de recette

| Élément            | Valeur |
| ------------------ | ------ |
| URL / Application  |        |
| Version logicielle |        |
| Navigateur / OS    |        |
| Base de données    |        |
| Comptes de test    |        |

## 5. Stratégie de test

* Tests manuels / automatisés
* Jeux de données réels ou anonymisés
* Priorisation des fonctionnalités critiques
* Validation par profils utilisateurs (admin, client, invité…)

## 6. Cas de tests

### Structure d'un cas de test

**ID :**
**Nom :**
**Description :**
**Préconditions :**
**Étapes :**
1.
2.
3.

**Résultat attendu :**
**Résultat obtenu :**
**Statut :** OK / KO / Bloqué
**Commentaire :**

## 7. Gestion des anomalies

| ID | Description | Gravité | Priorité | Statut | Responsable |
| -- | ----------- | ------- | -------- | ------ | ----------- |

**Gravité :**

* Bloquant : empêche l'utilisation
* Majeur : fonction critique dégradée
* Mineur : gêne faible
* Cosmétique : visuel uniquement

## 8. Critères d'acceptation

* 0 anomalie bloquante
* < X anomalies majeures
* 100 % des fonctionnalités critiques validées
* Messages d'erreur compréhensibles
* Cohérence des données

## 9. Planning de recette

| Phase | Date début | Date fin | Responsable |
| ----- | ---------- | -------- | ----------- |

## 10. Validation finale

**Décision :**

* Accepté
* Accepté avec réserves
* Refusé

**Signataires :**

* Responsable métier
* Responsable projet
* Responsable qualité

# Exemple : Application de Gestion de bibliothèque en ligne

## 1. Contexte

Application web permettant aux utilisateurs de :

* créer un compte,
* rechercher des livres,
* réserver un livre,
* consulter l'historique de prêts.

## 2. Objectif de la recette

Valider que les fonctionnalités principales sont conformes aux exigences métier avant mise en production.

## 3. Environnement de test

* URL : [https://test-biblio.exemple.com](https://test-biblio.exemple.com)
* Navigateur : Firefox / Chrome
* Base de données : copie anonymisée de production
* Comptes de test fournis

## 4. Cas de tests fonctionnels

### Cas 1 - Création de compte utilisateur

**Préconditions :**

* L'utilisateur n'a pas encore de compte.

**Étapes :**

1. Accéder à la page “Inscription”.
2. Renseigner nom, prénom, email valide, mot de passe.
3. Cliquer sur “Créer un compte”.

**Résultat attendu :**

* Message de confirmation affiché.
* Email de validation reçu.
* Compte visible dans l'administration.

**Statut :** À tester / OK / KO

### Cas 2 - Recherche de livre

**Préconditions :**

* Utilisateur connecté.

**Étapes :**

1. Saisir “Harry Potter” dans la barre de recherche.
2. Lancer la recherche.

**Résultat attendu :**

* Liste de livres correspondant au mot-clé.
* Affichage titre, auteur, disponibilité.

**Statut :** À tester / OK / KO

### Cas 3 - Réservation d'un livre disponible

**Préconditions :**

* Livre marqué “Disponible”.

**Étapes :**

1. Cliquer sur “Réserver”.
2. Confirmer la réservation.

**Résat attendu :**

* Message “Réservation confirmée”.
* Livre marqué “Réservé”.
* Historique mis à jour.

**Statut :** À tester / OK / KO

### Cas 4 - Tentative de réservation d'un livre indisponible

**Préconditions :**

* Livre déjà réservé par un autre utilisateur.

**Étapes :**

1. Cliquer sur “Réserver”.

**Résultat attendu :**

* Message d'erreur clair.
* Aucune réservation créée.

**Statut :** À tester / OK / KO

## 5. Critères d'acceptation

* 100 % des cas critiques = OK
* Aucune anomalie bloquante
* Messages d'erreur compréhensibles
* Données cohérentes après action utilisateur

## 6. Anomalies

| ID     | Description    | Gravité | Statut |
| ------ | -------------- | ------- | ------ |
| BUG-01 | Email non reçu | Majeur  | Ouvert |


