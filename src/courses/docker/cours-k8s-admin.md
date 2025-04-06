---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Administration du cluster
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

- Condensé de [ces slides sur la _disruption_ dans un Cluster](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/disruptions.md)

---

## Panne de _Node_

- Un _Node_ devient `unreachable`
- application automatique de _taints_ `NoSchedule` et `NoExecute`
- _Pods_ reschédulés sur un autre _Node_ (sauf `StatefulSet`)
- Anticipation : > 2 réplicas de _Pod_ & anti-affinité pour exécution sur différents _Node_

---

## Pression mémoire/disque

- Plus assez de mémoire sur le _Node_ ou disque plein (`errno = ENOSPC` & `No space left on device`)
- _éviction_ de _Pod_ sur d'autres _Node_ (candidats triés par `priorityClassName` puis par consommation)
- _graceful shutdown_ pendant `terminationGracePeriodSeconds` puis _kill_
- Atténuation : `resource limits`, `resource requests`

---

## Arrêt manuel d'un _Node_ et PodDisruptionBudget

- Attention (interruption de service) si trop de réplicas sur ce _Node_ ou qui ne devraient pas être interrompues
- `PodDisruptionBudget` : contrat entre "sysops" (admin des _Node_ cluster) et "devops" (déployant les applis)
- ex : *dans cet ensemble de pods, ne pas "perturber" plus de X à la fois*
- Arrêter un _Node_ uniquement lorsqu'il n'y a plus de _Pod_ exécuté dessus (sauf _Pod_ système d'un `DaemonSets`).
- `kubectl drain` :
  - _cordon_ ("boucle") le _Node_ : _taint_ `NoSchedule`
  - _eviction API_ pour supprimer les _Pod_ (respecte les `PodDisruptionBudget`).
  - n'expulsera pas les _Pod_ utilisant des volumes `emptyDir` (sauf `--delete-emptydir-data`)
- Voir aussi [la doc officielle](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)

---

## Upgrade d'un _Node_

- Exemple : upgrade `Kubelet` ou noyau `Linux`
- Si upgrade "safe" : upgrade noyau, patch `Kubelet` (1.X.Y → 1.X.Z) : _normalement_ OK, **à tester en staging!**
- Sinon : migrer d'abord hors du _Node_ (idem arrêt du _Node_).

---

## Rescheduling manuel

- Exemple : le pod X effectue beaucoup d'E/S disque (_starvation_)
- Conséquence : les _Pod_ déplacées sont temporairement interrompus
- Atténuation : définir un nombre approprié de réplicas, déclarer des `PodDisruptionBudget`, utiliser l'[eviction API](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/)

---

