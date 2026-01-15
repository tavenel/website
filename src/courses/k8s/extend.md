---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Étendre Kubernetes
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

Voir aussi : [ces slides de formation](https://2021-05-enix.container.training/4.yml.html#103)

---

## 🎛 Controller

> Controllers are control loops that watch the state of your cluster, then make or request changes where needed. Each controller tries to move the current cluster state closer to the desired state. 🔄
> <https://kubernetes.io/docs/concepts/architecture/controller/>

- Surveille des ressources 👀
- Applique des changements : API uniquement (`Deployment`, `ReplicaSet`), configure des ressources (`kube-proxy`), provisionne des ressources (_Load Balancer_) 🔧
- `kube-scheduler` est un _Controller_ ! 🤖
- [Admission Controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) et [extension](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) : peut examiner ou transformer les requêtes à l'`API Server` avant la création des ressources : `ServiceAccount`, `LimitRanger`, `Kyverno`, `Open Policy Agent`, … 🛡️
- Voir la partie _Sécurité_ du cours pour plus de détails ! 🔒

---

## 🔧 CRD

- Kubernetes permet d'ajouter des types de `Ressource` personnalisés 🛠️
- Nouveau `kind: …` 🏷️
- Appelées _Custom Resource Definition (CRD)_ 📝
- `kubectl api-resources` (toutes les ressources) 📋
- `kubectl get crds` (CRD) 📋
- <https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/> 📚
- <https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/> 📚

---

## 🔄 Aggregation Layer
- Ressources [APIServer](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) : lien `kind: …` à un service externe 🔗
- Délègue des parties de l'`API Server` à des API externes 🔄
- Exemple : `metrics-server` 📊
- `kubectl get apiservices` 📋
- (Autre option: [Service catalog](https://kubernetes.io/id/docs/concepts/extend-kubernetes/service-catalog/) utilisant l'_Open Service Broker API_) 📂

---

## 🤖 Operators

> An operator represents human operational knowledge in software, to reliably manage an application. - [CoreOS](https://coreos.com/blog/introducing-operators.html) 🤖

- Un _Operator_ permet d'ajouter au cluster des _CRDs_ et un _Controller_ pour les gérer 🛠️
- Liste : <https://operatorhub.io/> 📋
- Exemples :
  - BDD répliquées primaire / secondaire : `MariaDB`, `MySQL`, `PostgreSQL`, `Redis` 🗃️
  - _Node_ qui n'ont pas le même rôle : `ElasticSearch`, `MongoDB` 🏷️
  - Dépendances complexes : `Flink` & `Kafka` avec dépendance `Zookeeper` 🔗
  - Ressources externes : `AWS S3` ☁️
  - Add-ons complexes : `Istio`, `Consul` 🧩
  - Gérer ses propres applications 🛠️
- Kubernetes a pour projet de tout déléguer dans le futur à des _Operator_ : `Service`, `Deployment`, … 🔮
- [Exemple de création d'Operator par Ansible](https://blog.stephane-robert.info/post/ansible-kubernetes-operator/) 📝

---

## 🛠️ Kustomize

- Permet d'ajouter / modifier des ressources Kubernetes par `Kustomization` (fichier YAML) 📝
- Intégré dans `kubectl` : `apply -k …` 🔧
- Utile pour :
  - Config dev vs prod, … 🔄
  - Scaling : `replicas: …` 📈
  - Mettre à jour l'image d'un conteneur 🔄

![Exemple d'utilisation de Kustomize](https://kustomize.io/images/header_templates.png)

<div class="caption">Exemple d'usage de Kustomize. Credits: kustomize.io</div>

---

### Vocabulaire Kustomize

- **kustomization** : une **base** ou un **overlay** 📂
- **base** : _kustomization_ **référencée par** d'autres _kustomization_ 🔗
- **overlay** : _kustomization_ **qui référence** d'autres _kustomization_ (récursif) 🔄
- **patch** : une **modification** d'une ressource Kubernetes existante 🛠️
- **variant** : **version finale** de la ressource Kubernetes après application des _bases_ et _overlay_ 📦

---

