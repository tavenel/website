---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Déploiement continu avec Flagger
layout: '@layouts/CoursePartLayout.astro'
date: 2024 / 2025
---

Dans un contexte de déploiement continu, la mise en production de nouvelles versions d'une application peut présenter des risques si elle est réalisée brutalement. C’est là qu’intervient **Flagger**, un opérateur Kubernetes qui automatise les **modèles de déploiement progressif** tels que *canary*, *blue/green*, ou *A/B testing*. Flagger s’intègre avec des outils de service mesh ou d’ingress controller comme **Istio**, **Linkerd**, **NGINX**, ou **Traefik** pour rediriger progressivement le trafic vers la nouvelle version.

Concrètement, lors d’un déploiement canary, Flagger commence par envoyer un faible pourcentage du trafic (ex. 5 %) vers la nouvelle version. Si les métriques (latence, taux d’erreur, disponibilité) sont stables, le trafic est augmenté par paliers. En cas de dégradation, Flagger interrompt le déploiement et revient à la version stable automatiquement, évitant ainsi une indisponibilité totale de l'application.

Flagger peut surveiller des **métriques Prometheus** ou effectuer des requêtes HTTP de santé. Il s’intègre facilement dans un pipeline GitOps (par exemple avec **Argo CD**), ce qui permet d’avoir des mises à jour contrôlées, validées, et traçables, tout en réduisant les risques.

Utiliser Flagger dans un processus CI/CD Kubernetes permet donc d’automatiser des stratégies de déploiement avancées avec une logique de validation en continu, renforçant la **résilience** et la **confiance** dans les mises en production.

:::exo
Utiliser _Flagger_ pour mettre en place un modèle avancé de déploiement continu.
:::

