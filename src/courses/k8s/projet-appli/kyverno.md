---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Bonus - Ajouter des politiques de sécurité grâce à Kyverno
layout: '@layouts/CoursePartLayout.astro'
date: 2024 / 2025
---

Dans un cluster Kubernetes, garantir la sécurité passe par le **contrôle des configurations** déployées par les utilisateurs et les applications. **Kyverno** permet d'appliquer, de valider, de muter ou de générer automatiquement des ressources selon des règles déclaratives.

Avec Kyverno, il est possible d'imposer des **politiques de sécurité** telles que : l'obligation d'utiliser des images depuis des registres approuvés, l'interdiction d'exécuter des conteneurs en mode `privileged`, la présence obligatoire de probes (`livenessProbe`, `readinessProbe`), ou encore la vérification de la présence de labels standards. Par exemple, on peut interdire tout pod contenant `hostNetwork: true` ou forcer l'utilisation de `runAsNonRoot`.

Kyverno permet également d'appliquer automatiquement des configurations manquantes : par exemple, injecter un sidecar de logging ou imposer une stratégie de `networkPolicy` sur chaque nouveau namespace. En mode audit ou en mode enforcement, il peut bloquer les déploiements non conformes dès la phase de validation (`admission controller`).

