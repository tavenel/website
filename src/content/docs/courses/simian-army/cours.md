---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: 🦍 Introduction au Simian Army
type: cours
sidebar:
  order: 1
description: 🦍 Introduction au Simian Army
---
## 🤔 Simian Army

- Suite d'outils développée par Netflix pour tester la résilience des systèmes distribués dans des environnements Cloud (_AWS_, …). 🛠️
- Provoquent **intentionnellement** des **défaillances** pour s'assurer que les systèmes peuvent les gérer efficacement (**tests de Chaos**). 🌪️

---

## 🧪 Outils du Simian Army

---

### 🐒 Chaos Monkey

- **Fonction** : Désactive aléatoirement des instances de production pour s'assurer que le système reste résilient. 🌪️
- **Objectif** : Vérifier que les services peuvent survivre à la perte d'instances. 🛡️
- **Exemple** : Configurez Chaos Monkey pour qu'il désactive aléatoirement une instance de votre application une fois par jour.

:::tip
Chaos Monkey est principalement conçu pour fonctionner dans des environnements cloud comme AWS, où il peut désactiver des instances pour tester la résilience des systèmes. Si vous souhaitez tester des concepts similaires en local, vous pouvez écrire des scripts pour arrêter ou redémarrer aléatoirement des composants (par exemple arrêter des conteneurs Docker aléatoirement). Dans un cluster _Kubernetes_, on pourra également utiliser <https://chaos-mesh.org/>
:::

---

### 🦍 Chaos Kong

- **Fonction** : Désactive une région AWS entière pour simuler une panne majeure. 🌍
- **Objectif** : Tester la capacité du système à gérer des pannes à grande échelle. 🏗️
- **Exemple** : Planifiez Chaos Kong pour désactiver une région entière pendant une fenêtre de maintenance.
  - Vérifiez que le trafic est automatiquement redirigé vers les autres régions disponibles, et les utilisateurs ne subissent qu'une légère augmentation de la latence.

---

### 🦺 Latency Monkey

- **Fonction** : Introduit des latences artificielles dans les communications entre services. ⏳
- **Objectif** : Vérifier que les services peuvent gérer des retards de communication sans défaillir. ⚡
- **Exemple** : Configurez Latency Monkey pour introduire des latences aléatoires de 1 à 5 secondes dans les communications entre vos microservices. Identifiez les goulots d'étranglement potentiels et optimisez les temps de réponse de vos services.

---

### 🔌 Conformity Monkey

- **Fonction** : Désactive les instances qui ne se conforment pas aux meilleures pratiques. 📋
- **Objectif** : S'assurer que toutes les instances respectent les configurations et pratiques recommandées. ✅

---

### 🛡️ Security Monkey

- **Fonction** : Recherche les failles de sécurité et les configurations incorrectes. 🔒
- **Objectif** : Identifier et corriger les vulnérabilités de sécurité. 🛡️

---

### 👮 Doctor Monkey

- **Fonction** : Supervise les indicateurs de santé des instances et des services. 🏥
- **Objectif** : Détecter et traiter les problèmes de santé des services avant qu'ils ne deviennent critiques. 💉

---

### 🧠 Janitor Monkey

- **Fonction** : Nettoie les ressources inutilisées dans l'environnement cloud. 🗑️
- **Objectif** : Optimiser l'utilisation des ressources et réduire les coûts. 💰

---

## 💡 Conseils pour une Utilisation Efficace

- **Commencer Petit** : Commencer par des tests de chaos à petite échelle et augmenter progressivement l'impact. 📏
- **Automatiser** : Automatiser les tests de chaos pour les intégrer facilement dans le cycle de vie du développement (CI/CD, voir production). 🤖
- **Collaborer** : Impliquer toutes les équipes (développement, opérations, sécurité) dans les tests de chaos. 👥
- ⚠️ **Ne pas Tester en ~Isolation~** : Les tests de chaos doivent être effectués dans un environnement réaliste. 🌍

---

