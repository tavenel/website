---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Tests de Performance
tags:
- tests
- performance
type: cours
sidebar:
  order: 5
description: Tests de Performance
---
## Principes

- 🎯 Objectif : évaluer la capacité, la robustesse et l'efficacité d'un système sous différentes contraintes.
- 📈 Toujours définir **des SLA ou objectifs de performance** : temps de réponse max, taux d'erreur toléré.
- Faire varier uniquement 1 paramètre pour pouvoir analyser les résultats : uniquement le nombre de connexion simultanées ou uniquement le nombre de requêtes d'un utilisateur (mais pas les 2 à la fois)
- Tester progressivement : charge normale → forte → extrême

---

## 1️⃣ Tests de **charge** (Load Testing)

- Objectif : vérifier le comportement du système sous **une charge normale ou attendue**.
- Exemple : un serveur web qui doit gérer 1000 utilisateurs simultanés.
- Mesures : temps de réponse moyen, taux d'erreurs, utilisation CPU/mémoire.

---

## 2️⃣ Tests de **pic / stress** (Stress Testing)

- Objectif : pousser le système **au-delà de sa capacité maximale** pour identifier son point de rupture.
- Exemple : augmenter le nombre de requêtes jusqu'à saturation.
- Mesures : performance sous forte charge, dégradation progressive, récupération après dépassement.

---

## 3️⃣ Tests de **capacité / scalability** (Capacity / Scalability Testing)

- Objectif : déterminer combien d'utilisateurs ou de requêtes le système peut gérer avant de tomber en dessous des critères de performance.
- Variante : **scaling vertical** (CPU/mémoire) ou **scaling horizontal** (ajout de serveurs).

---

## 4️⃣ Tests de **endurance / soak testing**

- Objectif : vérifier le comportement **sur le long terme**, notamment fuite de mémoire, dégradation des performances ou corruption de données.
- Exemple : faire tourner une application sous charge modérée pendant 24-72 heures.

---

## 5️⃣ Tests de **latence / temps de réponse**

- Objectif : mesurer **le délai entre une requête et sa réponse**.
- Utile pour APIs, systèmes distribués, bases de données ou IA générative.
- Mesures : temps moyen, percentile 95 ou 99 (p95/p99), distribution des temps de réponse.

---

## 6️⃣ Tests de **débit / throughput**

- Objectif : mesurer **la quantité maximale de données traitées par unité de temps**.
- Exemple : nombre de requêtes HTTP par seconde, transactions par minute, généralisé aux pipelines IA.

---

## 7️⃣ Tests de **ressources / profiling**

- Objectif : mesurer l'usage des ressources système sous charge (CPU, RAM, GPU, I/O).
- Permet de détecter des **goulots d'étranglement** ou des optimisations possibles.

---

## 8️⃣ Tests de **résilience / failover**

- Objectif : vérifier que le système **reste fonctionnel en cas de panne partielle** (serveur, réseau, base de données).
- Exemple : déconnecter un nœud dans un cluster Kubernetes et observer si le trafic est correctement redirigé.

---

## 9️⃣ Tests de **concurrence / multi-utilisateur**

- Objectif : tester le système quand **plusieurs utilisateurs accèdent en parallèle** aux mêmes ressources ou données.
- Mesure des conflits, des locks, et des performances globales.

---
