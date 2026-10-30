---
title: 🔧 Administration du cluster
description: 🔧 Administration du cluster
type: cours
sidebar:
  order: 8
tags:
- docker
- kubernetes
- devops
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
---
- Condensé de [ces slides sur la _disruption_ dans un Cluster](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/disruptions.md)

---

## 🛑 Panne de _Node_

- Un _Node_ devient `unreachable` 🚨
- Application automatique de _taints_ `NoSchedule` et `NoExecute` 🔧
- _Pods_ reschédulés sur un autre _Node_ (sauf `StatefulSet`) 🔄
- Anticipation : > 2 réplicas de _Pod_ & anti-affinité pour exécution sur différents _Node_ 🛡️

---

## 💾 Pression mémoire/disque

- Plus assez de mémoire sur le _Node_ ou disque plein (`errno = ENOSPC` & `No space left on device`) 💥
- _Éviction_ de _Pod_ sur d'autres _Node_ (candidats triés par `priorityClassName` puis par consommation) 📊
- _Graceful shutdown_ pendant `terminationGracePeriodSeconds` puis _kill_ ⏳
- Atténuation : `resource limits`, `resource requests` 🛠️

---

## 🛑 Arrêt manuel d'un _Node_ et PodDisruptionBudget

- Attention (interruption de service) si trop de réplicas sur ce _Node_ ou qui ne devraient pas être interrompues ⚠️
- `PodDisruptionBudget` : contrat entre "sysops" (admin des _Node_ cluster) et "devops" (déployant les applis) 🤝
- Ex : *dans cet ensemble de pods, ne pas "perturber" plus de X à la fois* 📝
- Arrêter un _Node_ uniquement lorsqu'il n'y a plus de _Pod_ exécuté dessus (sauf _Pod_ système d'un `DaemonSets`). 🛑
- `kubectl drain` :
  - _Cordon_ ("boucle") le _Node_ : _taint_ `NoSchedule` 🔒
  - _Eviction API_ pour supprimer les _Pod_ (respecte les `PodDisruptionBudget`). 🗑️
  - N'expulsera pas les _Pod_ utilisant des volumes `emptyDir` (sauf `--delete-emptydir-data`) 📦
- Voir aussi [la doc officielle](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) 📖

---

### 📋 Recommandations de `PodDisruptionBudget`
| Nombre de Replica | minAvailable | maxUnavailable |
|---------------|--------------|----------------|
| **Exactement 1** | | 🚫 ~Ne pas utiliser de PDB~ |
| **Exactement 2** | | Affecter l'un ou l'autre (❌ pas les deux !) à **1** |
| **HPA entre 1 et 2** | | **1** (⚠️ mais risque de downtime) |
| **Minimum 2 (avec HPA)** | ⚡ **1** pour une remédiation rapide | OU 💪 **1** pour H/A |

:::tip
💡 Dans tous les cas, ajouter `UnhealthyPodEvictPolicy: AlwaysAllow` pour autoriser l'éviction de Pod _unhealthy_ sans condition.
:::

---

## 🆙 Upgrade d'un _Node_

- Exemple : upgrade `Kubelet` ou noyau `Linux` 🔄
- Si upgrade "safe" : upgrade noyau, patch `Kubelet` (1.X.Y → 1.X.Z) : _normalement_ OK, **à tester en staging!** 🧪
- Sinon : migrer d'abord hors du _Node_ (idem arrêt du _Node_). 🚚

---

## 🔄 Rescheduling manuel

- Exemple : le pod X effectue beaucoup d'E/S disque (_starvation_) 💽
- Conséquence : les _Pod_ déplacées sont temporairement interrompus ⏸️
- Atténuation : définir un nombre approprié de réplicas, déclarer des `PodDisruptionBudget`, utiliser l'[eviction API](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/) 🛡️

---

