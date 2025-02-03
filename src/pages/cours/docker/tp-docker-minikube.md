---
title: Premiers pas Kubernetes avec Minikube
date: 2023 / 2024
---

_L'objectif de ce TP est de découvrir Kubernetes à travers Minikube, une installation (très) simplifiée pour tester Kubernetes sur un seul serveur._

## Installation

1. Installer `minikube` depuis la documentation officielle : <https://minikube.sigs.k8s.io/docs/start/>
2. Installer `kubectl`, la CLI de Kubernetes : `minikube kubectl -- get po -A`

:::tip
`kubectl` est la CLI de Kubernetes. Pour l'utiliser avec Minikube, on utilisera la notation suivante :

```
minikube kubectl -- …
```

Attention à bien ajouter les caractères `--` qui permettent de séparer la sous-commande `kubectl` de `minikube` des paramètres passés à `kubectl`.
:::

## Création d'un service de test

Déployer un 1er service de test : `hello-minikube` tel que décrit sur la page d'installation <https://minikube.sigs.k8s.io/docs/start/> :

```
minikube kubectl -- create deployment hello-minikube --image=kicbase/echo-server:1.0
minikube kubectl -- expose deployment hello-minikube --type=NodePort --port=8080
minikube kubectl -- get services hello-minikube
minikube service hello-minikube
```

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
