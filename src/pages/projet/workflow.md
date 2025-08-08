---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CourseLayout.astro'
title: Méthodologie de travail en équipe
tags:
- projet
---

## Mail

- Minimiser le nombre de mails (préférer la messagerie instantanée)
- **Asynchrone** : pas de notification
- Pas de status "read" automatique
- Tout (très) gros changement dans le produit : mail d'information
- Si équipe très asynchrone : mail récap après chaque Sprint
- Inbox 0 => vider au maximum la boîte mail. (status "lu" un fois lu, mail en Inbox => tâche à réaliser)

## Messagerie instantanée (Slack, …)

- Globalement **synchrone** : besoin de notification
- Créer des canaux temporaires dès que besoin (à détruire après usage)
- Avec notification :
  - Canal #urgent : blocages, problèmes prod, …
	  - Messages rares, besoin de prise de connaissance et d'action immédiate
	- Canal #ping : revue de code en attente, demande d'attention (changements importants, blocage, doc à lire)
	  - À traîter dans la journée
- Sans notification :
	- Canal #backlog : PR mergée, ticket fermé, bug fermé
	- Canal #watercooler (machine à café virtuelle) : échanges informels, anecdotes, recommandations, événements.

## Meeting

- Si possible, privilégier asynchrone (messagerie, …)
- Inviter seulement les intéressés
- Toujours finir par un envoi de "minutes" (résumé & liste d'actions)
  - Si besoin, informer les non présents

## Git

- Point central du projet : essayer d'y inclure un maximum de code, configurations, docs, …
- Formaliser le workflow d'équipe
- Privilégier un workflow simple et le complexifier au besoin
- Bon point de départ : 1 branche "main" et des branches de fonctionnalité

## Tableau de bord

- Sélectionner quelques indicateurs clés (3 à 5)
- Spécifiques au projet
- Asynchrone : utiliser des alertes en cas de souci

## Doc

- Doc as Code : privilégier toute la doc dans le dépôt Git, et (mieux) directement dans le code source.
- Test as Doc : les tests documentent les "corner case".
- Tester la documentation : liens morts, dates de vérification récentes (utiliser des cartouches)
- Wiki sous forme d'arbre : une page "index" permettant d'atteindre toutes les ressources par transitivité (doc, dépôts git, outils, …).
- Page "onboarding" pour l'arrivée d'un nouveau membre d'équipe : décrit tout le process et les outils de l'équipe.
- Bonnes pratiques de documentation technique : <https://www.writethedocs.org/guide/>

## Daily meetings

- Tous les jours sauf si équipe très autonome
- Chacun (**tout** le monde) parle à tour de rôle
  - y compris juste : "je continue cette tâche"
- Seul ordre du jour : avancement / attribution des tâches / ping collectif (demander à lire la documentation des changements, …)
- Maxi 2 min. par personne
  - sinon scheduler un meeting avec les intéressés
- Maxi 15 min. pour l'équipe
- Utiliser un timer pour contrôler le temps

## 🔗 Liens

- <https://sklein.xyz/fr/garden/007-comment-j-utilise-slack/>
- <https://sklein.xyz/fr/garden/028-notificaton-acknowledge/>
- <https://sklein.xyz/fr/garden/009-team-workflow/>

