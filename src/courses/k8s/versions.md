---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Versions et upgrade
layout: '@layouts/CoursePartLayout.astro'
---

- Kubernetes suit un versionning _sémantique_ vMAJOR.MINOR.PATCH (ex 1.28.9).
- Il est _recommandé_ (pas obligatoire) d'exécuter des versions homogènes sur l'ensemble du cluster mais :
- Les `APIServer` (en H/A) peuvent avoir différentes versions
  - et donc le résultat de `kubectl` peut être … exotique !
- Différents _Node_ peuvent exécuter différentes versions de `Kubelet` et/ou du noyau Linux et/ou différents engines de conteneurs
- Les composants peuvent être mis à niveau un par un sans problème (c'est même recommandé).
- Il est toujours possible de combiner différentes versions de _PATCH_ (par exemple, 1.28.9 et 1.28.13 sont compatibles) mais il est recommandé de toujours mettre à jour vers la dernière version de _PATCH_
- **L'`APIServer` doit être plus récent** que ses clients (`Kubelet` et _Control Plane_), donc **être mis à jour en premier**
- Tous les composants supportent (au moins) une **différence d'une version _MINEURE_** => upgrade à chaud possible
- Voir [la documentation sur les versions non homogènes](https://kubernetes.io/releases/version-skew-policy/)
- Mettre à jour avec **le même outil qui a servi à l'installation du composant** : gestionnaire de package, `kubeadm`, Pod, conteneur, …
- En moyenne, **une mise à jour tous les 3 mois**

