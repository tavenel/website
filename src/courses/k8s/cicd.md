---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: CI/CD sur Kubernetes
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
- cicd
---

## 🔔 Rappels

### 🔄 CI/CD : Définitions
- **CI (Intégration Continue)** : Automatisation de la compilation, des tests et des validations à chaque modification du code source. 🛠️
- **CD (Déploiement Continu / Continuous Deployment)** : Automatisation de la mise en production de l'application à chaque validation réussie. 🚀

---

## 🛠 Chaîne d'outils typique

   Étape | Outil recommandé | Rôle |
 |------|------------------|------|
 | Versioning | Git (GitHub, GitLab, etc.) | Suivi du code source 📜 |
 | Build & Test | GitLab CI / Jenkins / GitHub Actions | Construction d'images et tests 🧪 |
 | Packaging | Docker, Buildah | Création d'images de conteneur 📦 |
 | Déploiement | Helm / Kustomize / Argo CD | Déploiement déclaratif 📝 |
 | Monitoring | Prometheus / Grafana | Supervision du déploiement 📊 |

---

## 🏗 Exemple de pipeline CI/CD avec GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - push
  - deploy
variables:
  IMAGE_TAG: \$CI_REGISTRY_IMAGE:\$CI_COMMIT_SHORT_SHA
build:
  stage: build
  script:
    - docker build -t \$IMAGE_TAG .
  only:
    - main
test:
  stage: test
  script:
    - docker run --rm \$IMAGE_TAG pytest tests/
  only:
    - main
push:
  stage: push
  script:
    - echo \$CI_REGISTRY_PASSWORD | docker login -u \$CI_REGISTRY_USER --password-stdin \$CI_REGISTRY
    - docker push \$IMAGE_TAG
  only:
    - main
deploy:
  stage: deploy
  script:
    - helm upgrade --install my-app ./charts --set image.tag=\$CI_COMMIT_SHORT_SHA
  environment:
    name: production
  only:
    - main
```

---

## ⚙️ Helm : gestion déclarative du déploiement

- Réutilisabilité des chartes. ♻️
- Paramétrage par environnement. 🔧
- Rollback facile. 🔄

```yaml
# values.yaml
image:
  repository: registry.gitlab.com/my-group/my-app
  tag: latest

service:
  type: ClusterIP
  port: 80
```

---

## 🌐 Argo CD : GitOps pour Kubernetes

- L'**état cible** est défini dans **Git** (_Helm_/_Kustomize_). 📂
- Argo CD **synchronise automatiquement** l'état réel avec l'état désiré. 🔄
- Déploiements **auditables** et **versionnés**. 📜
- **Observabilité** des écarts d'état. 👁️
- **Rollback** automatique possible. 🔙

---

## 📈 Observabilité et résilience

- **Prometheus** : collecte des métriques de pods/applications. 📊
- **Grafana** : tableaux de bord temps réel. 📈
- **Alertmanager** : notifications sur échecs de déploiement. 🚨
- **Liveness/Readiness probes** : assurent la robustesse des applications déployées. 🛡️

---

## ✅ Bonnes pratiques

- Garder la pipeline **simple** et **modulaire**. 🧩
- **Versionner** les manifests Kubernetes. 📝
- Utiliser des environnements de **staging** pour les tests. 🧪
- Déployer en **rolling update** avec stratégie de **rollback**. 🔄
- Ne jamais stocker les ~secrets~ dans le dépôt Git : utiliser **Kubernetes Secrets** ou des solutions comme **_Vault_/_Sealed Secrets_**. 🔒

---

