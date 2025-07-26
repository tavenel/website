---
title: Projet OSIRIS 4.0
---

## Description

Cette étude de cas porte sur l'analyse du projet Osiris, dont un compte rendu est disponible à l'adresse suivante :

[Sybord, C., & Fedrici, B. (Août 2020). Impacts des objets connectés dans le secteur de la chimie - Cas du projet OSIRIS 4.0. Management et Datascience, 4(6).](https://management-datascience.org/articles/13977/)

Cette étude décrit un environnement organisationnel, technique et fonctionnel lié à l'introduction de technologies IoT (Internet des Objets) dans une entreprise du secteur de la chimie.

Pendant cette étude, un prototype (Proof of Concept) a été réalisé avec succès et l'entreprise souhaite maintenant aller plus loin dans la réalisation du projet.

## Annexe méthodologique 

### Méthodologie

La méthodologie retenue est la recherche action ; la richesse de ce type de recherche, qualitative et participante, est son processus flexible qui, partant d’une question saillante, permet de rester ancré aux besoins réels du terrain en réalisant des actions innovantes qui apporteront des réponses à la question posée ; d’ailleurs, cet atout correspondait à la demande de la DSI d’OSIRIS : expérimenter, à toute petite échelle, avec la POC, l’impact des compteurs connectés sur le suivi des utilités énergétiques pour ensuite convaincre progressivement les différentes parties prenantes de la faisabilité du projet OSIRIS 4.0. Pour mener cette recherche, un poste de data scientist a été créé pour une durée de 6 mois, dont 1/3 à temps plein sur le terrain. 

Pour mieux comprendre la demande, rajoutons qu’OSIRIS est le gestionnaire d’une offre de services et d’infrastructures mutualisées pour les 17 entreprises présentes sur la plate-forme ; ses missions vont du maintien de la sécurité sur la plate-forme à la logistique en passant par le contrôle analytique, la gestion du parc informatique ou encore la production et la distribution des utilités énergétiques (vapeur, gaz naturel, électricité, eau brute, eau déminéralisée, eau potable, azote, air comprimé). Ces différentes activités, historiquement organisées en silos, doivent être réorganisées pour répondre aux nouveaux services générés par l’industrie 4.0. (Cf. Partie 1). 

### Collecte de données 

Plusieurs outils de collecte de données ont été mis en œuvre dans le cadre de l’étude. 

Tout d’abord, 15 entretiens semi-directifs ont été réalisés avec les personnes de la DSI et, en particulier, avec le responsable du G.E.E.F. Les informations recueillies ont permis de comprendre les défis organisationnels et humains de la numérisation des utilités énergétiques ainsi que le rôle de la POC. Ont ensuite été réalisés de nombreuses séquences d’observation participante (une trentaine), notamment lors de réunions associant OSIRIS et des clients de la plate-forme : ces observations ont permis d’appréhender les difficultés à co-construire des solutions facilitant la transition numérique. Enfin, pour formaliser davantage le travail poursuivi et donner de la perspective au sujet, ont été effectuées des recherches documentaires pour articuler le côté terrain avec des concepts et des idées. 

### Déroulement de la recherche action 

Avec des personnes de la DSI, le déroulement a été structuré en 2 actions effectuées en parallèle : réalisation de la P.O.C ; construction du modèle général des données de la future flotte des compteurs connectés. 

S’agissant de la réalisation de la P.O.C., précisons qu’elle visait à automatiser la collecte de données en provenance de deux puits d'extraction d'eau de la nappe phréatique situés aux abords de la plate-forme. Un tel choix avait été motivé par le fait que l'eau extraite constitue le premier maillon de la chaîne de la vapeur. Idéalement, les informations pertinentes à faire remonter sont, pour chaque puits, la pression, le débit, la force motrice (i.e. la consommation électrique) et la température. Selon cette perspective, le premier travail a été donc de faire un état des lieux des infrastructures existantes ; cet état a servi d'étape préliminaire à l’étude de connectivité. L'étude de connectivité ayant été faite, est venue ensuite l'étape de collecte de données au moyen d'une plateforme informatique de test et d'un kit incluant passerelle(s) et serveur. Enfin, a été réalisée la production de tableaux de bord à destination des utilisateurs finaux. 

S’agissant de la construction du modèle général des données, le travail a consisté à évaluer l’intégralité des données provenant de la plate-forme : toutes utilités confondues et tous types de capteurs confondus (distribution, consommation, mixte). Dans ces conditions, la première étape a été d’analyser les besoins de données en amont de la construction du modèle. Une fois la liste des données pertinentes établie, une analyse sur le type de base de données à utiliser a, ensuite, été menée en comparant différentes solutions techniques existantes sur le marché : enfin, cette étude comparative a permis à OSIRIS d’orienter ses choix pour la construction du futur modèle de données des utilités énergétiques. 

## Exercice

- En vous basant sur le rapport de l'étude, quelles sont les spécificités de votre nouveau projet qui utilise de l'IoT dans le domaine de la chimie ?
- Quelles exigences et quelles contraintes peut-on prédire ?
- Certaines exigences vous semblent-ils critiques ? Quels sont les risques associés ?
- Quelles sont les dépendences entre ces exigences ?

