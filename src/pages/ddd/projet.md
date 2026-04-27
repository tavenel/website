---
title: Projet DDD - Logiciel de devis et facturation
date: 2024 / 2025
---

## Présentation du projet

Vous êtes une ESN et vous venez de recevoir un nouveau projet à réaliser, décrit ci-dessous. L'objectif est de réaliser ce projet dans un contexte de Domain-Driven Design (DDD).

### Objectifs du projet

### Contexte 1 - gestion de devis et de facturation

Le projet vise à améliorer l'efficacité opérationnelle, à réduire les erreurs humaines et à renforcer la satisfaction client en automatisant le processus de gestion de devis et factures. L'interface conviviale et les fonctionnalités avancées permettront à l'équipe financière de gagner du temps, de minimiser les retards de paiement et d'améliorer la collaboration interne.

Ce projet s'inscrit dans une démarche globale visant à optimiser l'ensemble du processus financier au sein de l'entreprise. Cette solution complète offre une palette de fonctionnalités permettant une gestion aisée et personnalisée des transactions commerciales. La création de devis est simplifiée, offrant la possibilité d'inclure des détails exhaustifs sur les produits et services, accompagnés de notes et de conditions spécifiques. L'évolution des devis en cours est suivie avec précision, et des versions peuvent être gérées pour assurer une traçabilité complète. Une fois approuvés, ces devis se transforment automatiquement en factures, générées avec une personnalisation avancée intégrant le logo de l'entreprise et d'autres informations pertinentes. La gestion des paiements, des rappels, et des avoirs est intégrée de manière transparente. Les devis et factures sont arrangés selon une organisation intuitive pour faciliter les recherches. Il est possible d'exporter les devis et les factures aux formats CSV, Excel et PDF ou de les envoyer par e-mail. Il est aussi possible d'importer un devis ou une facture depuis Excel. L'intégration d'une blockchain est également envisagée. L'ensemble de ces fonctionnalités vise à améliorer l'efficacité opérationnelle, à réduire les erreurs et à renforcer la satisfaction client, contribuant ainsi à une gestion financière optimisée au sein de l'entreprise.

### Contexte 2 - Plateforme de formation en ligne adaptative

Une organisation internationale spécialisée dans la formation académique et professionnelle souhaite concevoir une plateforme numérique unifiée capable de proposer des parcours d'apprentissage personnalisés à grande échelle, à destination d'universités, d'entreprises et d'organismes de certification. Cette plateforme doit permettre à des apprenants aux profils très variés — étudiants en formation initiale, salariés en reconversion, ou candidats à des certifications professionnelles — d'accéder à des contenus pédagogiques structurés, tout en adaptant en permanence leur progression en fonction de leurs objectifs, de leurs performances et de leurs contraintes individuelles. Chaque apprenant s'inscrit dans un ou plusieurs programmes de formation, qui peuvent être associés à des objectifs explicites tels que l'obtention d'une certification, l'acquisition de compétences spécifiques ou la validation d'un parcours académique, avec éventuellement des échéances temporelles imposées ou des limitations en termes de disponibilité hebdomadaire. Les contenus proposés sont organisés selon des structures pédagogiques hiérarchisées (cours, modules, leçons, exercices), mais leur enchaînement ne doit pas être strictement linéaire : la plateforme doit être capable de modifier dynamiquement le parcours suivi par un apprenant en fonction de son comportement et de ses résultats, par exemple en proposant des contenus de remédiation lorsqu'une notion n'est pas maîtrisée, en accélérant la progression en cas de réussite rapide, ou en introduisant des activités complémentaires ciblées. L'évaluation des apprenants constitue un élément central du système et peut prendre différentes formes, allant de questionnaires classiques à des exercices pratiques ou des mises en situation, avec des mécanismes permettant d'ajuster la difficulté des évaluations en fonction du niveau estimé de l'apprenant ; les résultats obtenus doivent être interprétés en tenant compte de multiples facteurs, tels que la difficulté des questions, la cohérence des réponses ou encore certains indicateurs comportementaux pouvant révéler des anomalies. Par ailleurs, la plateforme doit être en mesure de formuler des recommandations pertinentes concernant les prochaines activités à réaliser, en s'appuyant à la fois sur les résultats des évaluations, sur la progression observée et sur les objectifs déclarés, tout en respectant des contraintes parfois contradictoires, comme la nécessité de couvrir un ensemble de compétences obligatoires dans un délai limité. Dans certains cas, l'atteinte d'un objectif, notamment l'obtention d'une certification, dépend de règles complexes combinant des critères de performance globale, la validation de compétences spécifiques et l'absence d'échecs sur des éléments jugés critiques. Enfin, la solution doit fonctionner dans un contexte multi-organisationnel, où différentes institutions peuvent utiliser la plateforme avec des attentes et des logiques propres, tout en partageant un socle commun de fonctionnalités, ce qui implique de prendre en compte des variations de règles métier, de terminologie et de contraintes opérationnelles selon les contextes d'utilisation.

### Contexte 3 - Plateforme de mobilité type VTC et covoiturage

Une entreprise souhaite concevoir une plateforme numérique de mobilité permettant de mettre en relation, en temps réel, des utilisateurs souhaitant effectuer un trajet avec des conducteurs disponibles, dans un contexte couvrant à la fois des usages proches du transport à la demande et du covoiturage planifié. Le système doit gérer un volume potentiellement élevé de demandes simultanées, avec des utilisateurs répartis sur différentes zones géographiques, et doit être capable de proposer des correspondances pertinentes en tenant compte de nombreux paramètres tels que la localisation, la destination, le temps estimé de trajet, les conditions de circulation et les préférences individuelles. Lorsqu'un utilisateur formule une demande de trajet, celle-ci peut être satisfaite de différentes manières selon le contexte : affectation immédiate d'un conducteur disponible, regroupement avec d'autres passagers partageant un itinéraire similaire, ou planification différée dans le cas de trajets programmés à l'avance. La plateforme doit intégrer un mécanisme de tarification dynamique capable d'ajuster le prix des trajets en fonction de critères variés, notamment la demande en temps réel, la disponibilité des conducteurs, la distance, la durée estimée, ainsi que des règles commerciales spécifiques pouvant inclure des majorations, des réductions ou des offres promotionnelles. Le déroulement d'un trajet implique plusieurs états successifs — demande initiale, proposition à un ou plusieurs conducteurs, acceptation, prise en charge, trajet en cours, arrivée à destination, paiement — chacun étant soumis à des contraintes et à des règles de transition précises, notamment en cas d'annulation, de retard, d'incident ou de désistement de l'une des parties. La plateforme doit également gérer des systèmes de réputation et d'évaluation réciproque, permettant aux utilisateurs et aux conducteurs de noter leurs expériences respectives, ces évaluations pouvant influencer ultérieurement les décisions de mise en relation ou l'accès à certaines fonctionnalités. Des mécanismes de pénalisation ou de restriction peuvent être appliqués en cas de comportements jugés inappropriés, comme des annulations répétées ou des retards fréquents. Par ailleurs, le système doit être capable de prendre en compte des contraintes spécifiques liées aux conducteurs, telles que leurs disponibilités, leurs zones d'activité, leurs préférences de trajets ou encore les caractéristiques de leur véhicule, ainsi que des exigences particulières des passagers, comme le nombre de places, la présence de bagages ou des options spécifiques. Enfin, la solution doit fonctionner dans un environnement multi-territorial, où les règles opérationnelles, les contraintes réglementaires, les modes de tarification ou les usages peuvent varier selon les régions ou les pays, tout en maintenant une cohérence globale du service et une capacité à évoluer rapidement face à des changements de conditions, qu'ils soient liés à la demande, à la réglementation ou à la stratégie commerciale de l'entreprise.

### Échéancier

Le développement du projet sera divisé en phases, avec des jalons clés à atteindre à chaque étape. Les tests approfondis seront effectués pour garantir la fiabilité et la sécurité de la solution avant son déploiement à l'échelle de l'entreprise.

## Travail à réaliser

Afin de réaliser ce projet, vous pensez qu'une approche DDD serait adaptée à ce projet (justifiez cette déclaration).
Mettre en place les différentes étapes nécessaires à la réalisation complète du projet.

_Le formateur jouera le rôle du client à l'origine du projet, formé aux pratiques DDD._

### Rendus

Ce projet comportera 4 rendus notés :

1. L'event storming et le langage ubiquitaire du projet (à rendre le 1e jour)
2. La carte de contexte (à rendre le 2e jour)
3. La description des cas d'utilisation, au choix :

- Diagramme UML de cas d'utilisation
- Description des fonctionnalités en Gherkin (BDD)
- User stories (backlog)

1. Soutenance projet et rendu du code du projet (dernière séance)
