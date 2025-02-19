---
title: TP Podman
date: 2024 / 2025
correction: false
---

# TP Podman - Conteneurs et Pods sans serveur

## Présentation de Podman

`Podman` est un moteur de conteneur open-source conçu pour créer, exécuter et gérer des conteneurs de manière sécurisée et efficace. Il se distingue par sa capacité à fonctionner sans nécessiter de démon, ce qui permet une exécution en mode _rootless_ (comme un utilisateur standard) pour une sécurité accrue. Podman est compatible avec l'API Docker, facilitant ainsi la transition pour les utilisateurs habitués à Docker. Il prend en charge la gestion des pods, un regroupement de conteneurs qui partagent des ressources, ce qui le rend idéal pour le développement et pour tester des pods Kubernetes en local sans nécessiter de cluster Kubernetes complet.

## Tester des fichiers k8s avec Podman

Voici comment procéder pour utiliser Podman comme environnement de développement Kubernetes :

### Installer Podman

Podman peut interpréter et exécuter des fichiers de configuration Kubernetes en utilisant son propre moteur de conteneur sans nécessiter de serveur.

### Définir les Manifests Kubernetes

Créez un fichier manifest Kubernetes (YAML) pour votre pod ou application, comme vous le feriez dans un vrai environnement Kubernetes. Ce fichier peut inclure des pods, des services, des configurations de volumes, etc.

Exemple de manifest nginx-pod.yaml :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: web
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```

### Lancer le Pod avec Podman en Mode Kubernetes

Podman peut interpréter des fichiers de pod Kubernetes directement avec la commande `podman play kube`.

```bash
podman play kube nginx-pod.yaml
```

Cela va :

- Créer le pod tel que défini dans le fichier manifest.
- Configurer le réseau et les ports en fonction de la spécification du pod.

### Vérifier les Pods en Exécution

Utilisez `podman pod ps` pour vérifier l’état de vos pods et `podman ps` pour voir les conteneurs en cours d'exécution :

```bash
podman pod ps
podman ps
```

Ces commandes listent tous les pods et conteneurs, fournissant leur statut, les ports exposés, et d’autres détails utiles.

### Tester l’Application

Accédez à votre application via le port spécifié en utilisant `localhost`. Si vous avez exposé le port 80 de Nginx comme dans l'exemple, ouvrez <http://localhost:80> dans un navigateur ou utilisez `curl` pour vérifier la réponse (dans une VM par exemple).

### Arrêt et Suppression

Pour arrêter et supprimer un pod :

```bash
podman pod stop nginx
podman pod rm nginx
```

Cela stoppe et supprime le pod, y compris tous les conteneurs associés.

### Travailler avec des Volumes et ConfigMaps

Si votre pod nécessite des `Volume` ou des `ConfigMap`, vous pouvez définir ces éléments dans le fichier manifest Kubernetes. Podman gère ces configurations en local pour émuler l’environnement Kubernetes autant que possible.

- Ajouter un `Volume` et une `ConfigMap` au `Pod` précédent.

### Limitations

- Certaines fonctionnalités avancées de Kubernetes (comme les Ingress, les contrôleurs de service) ne sont pas entièrement supportées par Podman.
- Les comportements réseau peuvent différer légèrement d'un vrai cluster Kubernetes.

## Environnements de développement avec Podman

Le projet <https://containertoolbx.org/> permet d'utiliser `Podman` pour créer des environnements de développement sur mesure en utilisant des conteneurs _stateful_.

## Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- K8s® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Podman® is a registered trademark of The Linux Foundation in the United States and/or other countries.

