---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Les 4 C de la Sécurité Cloud
layout: '@layouts/CoursePartLayout.astro'
---

## Cloud

- Sécurité **de l'infrastructure fournie par le provider**
- Responsabilité du fournisseur (AWS, Azure, GCP…)
- Inclut :
  - Datacenters
  - Réseau physique
  - Hyperviseurs
  - Matériel

---

## Cluster

- Sécurité de l'orchestration (ex : Kubernetes)
- Gestion :
  - Nœuds
  - API server
  - Etcd
  - RBAC
- Risques : mauvaise configuration, accès non restreints

---

## Container

- Sécurité des images et de l'exécution
- Bonnes pratiques :
  - Images minimales
  - Scan de vulnérabilités
  - Non-root user
  - Signature d'images
- Risques : images corrompues, dépendances obsolètes

---

## Code

- Sécurité applicative
- Concerne :
  - Secrets
  - Dépendances logicielles
  - Injection / XSS / RCE
  - CI/CD sécurisé
- Responsabilité **100 % développeur / équipe projet**

---

## Responsabilité

- **Plus on monte dans les C, plus la responsabilité revient à l'équipe projet.**
- Cloud Provider → DevOps → Développeurs → Sécurité Applicative

---

