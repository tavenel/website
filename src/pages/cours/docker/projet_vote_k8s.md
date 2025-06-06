---
title: TP Docker,k8s
date: 2023 / 2024
---

## Présentation de l'application

Récupérer les sources de l'application en clonant le dépôt git :

```sh
git clone https://git.sr.ht/~toma/docker-vote
```

Le fichier `README.md` dans les sources décrit l'application et ses spécificités de déploiement.

## Travail attendu

Pour permettre ce déploiement, il faudra donc :

- Un fichier `Dockerfile` pour chacun des 4 composants `vote`, `result`, `worker` et `proxy`. Un template est fourni pour chacun de ces services dans le répertoire de chaque composant.
- Déployer la stack applicative dans `kubernetes`. On privilégiera l'utilisation de fichiers de configuration `Yaml` ou `Json` et on utilisera `kubectl` uniquement pour appliquer ces fichiers (et non pour configurer directement les `pod`).
- Pour améliorer les performances, on déploiera 2 conteneurs `vote`.

## Rendu attendu 

- Les 4 `Dockerfile`.
- Les fichiers et/ou commandes de configuration `kubernetes`.

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0

