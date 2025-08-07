---
title: Analyse de Amazon et YouTube
---

1. En analysant le site web de YouTube :
  - Trouver les différents _Bounded Context_ du projet
  - Décrire les interactions (patterns stratégiques) entre les différents contextes
2. Mêmes questions pour le site web d'Amazon

:::correction
## Version complexe

### Youtube

| Bounded Context                    | Acteurs Principaux           | Métier Central                      |
|-----------------------------------|------------------------------|-------------------------------------|
| Content Management                | Créateurs                    | Gestion du contenu vidéo            |
| Playback & Streaming              | Tous utilisateurs            | Distribution efficace de la vidéo   |
| User Management                   | Tous utilisateurs            | Identité et sécurité                |
| Recommendation & Discovery        | Utilisateurs finaux          | Personnalisation                    |
| Search                            | Utilisateurs finaux          | Trouver du contenu                  |
| Monetization & Ads                | Créateurs, annonceurs        | Générer des revenus                 |
| Comments & Engagement             | Tous utilisateurs            | Interaction et engagement           |
| Live Streaming                    | Créateurs, spectateurs       | Diffusion en direct                 |
| Analytics & Insights              | Créateurs                    | Suivi des performances              |
| Moderation & Policy Enforcement   | YouTube, communauté          | Respect des règles                  |
| Notification                      | Tous utilisateurs            | Communication proactive             |
| Channel & Subscription            | Créateurs, abonnés           | Relation abonné-créateur            |


### Amazon

| Bounded Context                    | Acteurs Principaux           | Métier Central                           |
|-----------------------------------|------------------------------|------------------------------------------|
| Product Catalog                   | Clients, vendeurs            | Consultation et gestion des produits     |
| Search & Filtering                | Clients                      | Recherche et découverte de produits      |
| Customer Account                  | Clients                      | Gestion de l'identité et du profil       |
| Order Management                  | Clients, service client      | Commande, paiement, validation           |
| Shopping Cart                     | Clients                      | Sélection d'articles à acheter           |
| Pricing & Promotions              | Marketing, vendeurs          | Gestion des prix, réductions, coupons    |
| Checkout & Payment                | Clients, systèmes de paiement| Paiement sécurisé et validation          |
| Shipping & Fulfillment            | Clients, logistique          | Livraison, suivi, options de transport   |
| Inventory Management              | Vendeurs, entrepôts          | Suivi du stock et disponibilité produit  |
| Customer Support                  | Clients, agents support      | Gestion des réclamations, retours        |
| Reviews & Ratings                 | Clients                      | Feedback produit et fiabilité vendeur    |
| Recommendation Engine            | Clients                      | Suggestion personnalisée de produits     |
| Notification & Messaging          | Clients                      | Emails, SMS, notifications push          |
| Vendor & Seller Management        | Vendeurs tiers               | Gestion des comptes vendeurs             |
| Loyalty & Membership              | Clients                      | Amazon Prime, abonnements, avantages     |
| Analytics & Reporting             | Internes, vendeurs           | Données d'activité, ventes, performances |
| Fraud Detection & Security        | Systèmes internes            | Sécurité des transactions et comptes     |


## Version simple

### Youtube

| Bounded Context           | Acteurs Principaux     | Métier Central                    |
|--------------------------|------------------------|-----------------------------------|
| Content Management       | Créateurs              | Gestion des vidéos                |
| Playback & Streaming     | Tous utilisateurs      | Lecture et diffusion des vidéos   |
| User Management          | Tous utilisateurs      | Comptes, profils, sécurité        |
| Recommendation Engine    | Utilisateurs finaux    | Suggestions personnalisées        |
| Monetization & Ads       | Créateurs, annonceurs  | Revenus et publicité              |

### Amazon

| Bounded Context           | Acteurs Principaux     | Métier Central                        |
|--------------------------|------------------------|---------------------------------------|
| Product Catalog          | Clients, vendeurs      | Affichage des produits                |
| Search & Filtering       | Clients                | Recherche et navigation               |
| Order Management         | Clients, support       | Commandes, paiements, suivi           |
| Shipping & Fulfillment   | Clients, logistique    | Livraison et gestion des colis        |
| Customer Account         | Clients                | Connexion, profil, préférences        |
:::
