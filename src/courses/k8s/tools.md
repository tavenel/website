---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Outils externes
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

## Krew : Gestionnaire de plugins kubectl

- Gestionnaire officiel de plugins kubectl
- Étend `kubectl` sans modifier le binaire principal et standardise l'accès aux outils communautaires.

---

### Plugins incontournables

#### 🔍 Observation & diagnostic

| Plugin           | Usage                                      |
| ---------------- | ------------------------------------------ |
| **ctx**          | Changement rapide de contexte              |
| **ns**           | Changement rapide de namespace             |
| **tree**         | Vue hiérarchique des ressources            |
| **neat**         | **Nettoyage des manifests (YAML propre)**      |
| **view-secret**  | Lecture de secrets décodés                 |
| **describe-all** | Describe sur toutes les ressources         |
| **get-all**      | Liste toutes les ressources d'un namespace |

#### 🧠 Debug & Troubleshooting

| Plugin         | Usage                                    |
| -------------- | ---------------------------------------- |
| **debug**      | Debug éphémère avec ephemeral containers |
| **doctor**     | Diagnostic du cluster                    |
| **node-shell** | Shell direct sur un nœud                 |
| **status**     | **Résumé de l'état du cluster**              |
| **trace**      | Tracing syscalls (eBPF)                  |

#### 📦 Gestion des ressources

| Plugin                | Usage                               |
| --------------------- | ----------------------------------- |
| **resource-capacity** | Vue CPU/Mem par nœud                |
| **topology**          | Vue topology-aware du cluster       |
| **konfig**            | Fusion / nettoyage de kubeconfig    |
| **split-yaml**        | Découpe de manifests YAML           |
| **modify-secret**     | Modification interactive de secrets |

#### 🔐 Sécurité & audit

| Plugin            | Usage                       |
| ----------------- | --------------------------- |
| **access-matrix** | Matrice RBAC                |
| **rbac-view**     | Visualisation RBAC          |
| **auth-can-i**    | Vérification de permissions |
| **who-can**       | Qui peut faire quoi         |

#### 🚀 Développement & CI/CD

| Plugin             | Usage                                  |
| ------------------ | -------------------------------------- |
| **exec-as**        | Tester RBAC en changeant d'identité    |
| **rollout-status** | Suivi avancé de rollout                |
| **reap**           | Nettoyage de ressources orphelines     |
| **score**          | Scoring des manifests (best practices) |

---

## 📦 Helm : déploiement applicatif

- Gestionnaire de "paquets" k8s 📦
  - En fait des fichiers Yaml 📄
  - Ajout du versioning 🔄
- `chart` : ensemble de fichiers manifests, `templates`, … avec paramètres 📋
- Stockés dans des `repositories` : <https://hub.helm.sh/>, … 🌐
- `values.yaml` : valeurs par défaut 📝
- `template` : manifest Kubernetes avec _templates Go_. 📜
- `release` : un déploiement de `chart` (versionnée : upgrade, rollback, uninstall) 🔄
- Trouver des `chart` : <https://artifacthub.io/> 🔍

---

### 🌟 Exemples de Chart Helm

---

1. **Kubernetes Dashboard** :
   - **Description** : Déploie le Kubernetes Dashboard pour la gestion visuelle du cluster.
   - **Repository** : `kubernetes/dashboard`
   - **Exemple de commande** :

     ```sh
     helm repo add kubernetes https://kubernetes.github.io/dashboard
     helm install my-dashboard kubernetes/kubernetes-dashboard
     ```

---

2. **Prometheus & Grafana** :
   - **Description** : Déploie la stack Prometheus & Grafana pour la surveillance et la collecte de métriques.
   - **Repository** : `prometheus-community/prometheus`
   - **Exemple de commande** :

     ```sh
     helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
     helm install my-prometheus prometheus-community/kube-prometheus-stack
     # ou seulement Prometheus
     helm install prometheus-community/prometheus
     ```

---

3. **Nginx** :
   - **Description** : Déploie une instance Nginx.
   - **Repository** : `helm.nginx.com`
   - **Exemple de commande** :

     ```sh
     helm repo add nginx-stable https://helm.nginx.com/stable
     helm install nginx-ingress nginx-stable/nginx-ingress
     ```

---

## 🔄 GitOps : FluxCD, ArgoCD, Jenkins X

- Outils GitOps pour k8s 🔄
  - Scrute un dépôt Git distant 🌐
  - Mise à jour automatique des ressources k8s 🔄
  - Plus de CLI `kubectl` ❌
  - Utilise des `Kustomizations` de `Kustomize` (outil intégré à k8s) 🛠️
- Intégrations Helm et Terraform 🔄
- CLI `fluxctl` (pas de GUI) 🖥️
- Interface Web _Argo CD_, _Jenkins X_ 🌐

---

![Architecture de FluxCD](https://raw.githubusercontent.com/fluxcd/flux2/main/docs/diagrams/fluxcd-controllers.png)
<div class="caption">Architecture de FluxCD (source: documentation FluxCD)</div>

---

![Architecture d'ArgoCD](https://argo-cd.readthedocs.io/en/stable/assets/argocd_architecture.png)
<div class="caption">Architecture d'ArgoCD (source: documentation ArgoCD)</div>

---

## 🔒 Kyverno

- Limitations des permissions standard Kubernetes - comment :
  - Interdire l'utilisation du tag `:latest` ❌
  - Obliger chaque _Deployment_, _Service_, … à avoir un label `owner` 🏷️
  - Obliger chaque conteneur à avoir un `readinessProbe` 🔍
  - Obliger chaque `Namespace` à avoir des quotas et des limites 📏
- Solution : utiliser un `AdmissionController` 🔄

---

### [Kyverno](https://github.com/kyverno/kyverno/) : moteur de politiques pour k8s 🔒

- Gère des règles de sécurité, de conformité et de gestion (fichiers Yaml) 📜
  - _Controller_ ou _Operator_ Kubernetes, _Webhooks_ et _CRDs_ de politiques, principalement :
    - `Policy` ou `ClusterPolicy` (par _Namespace_ ou global au Cluster) 📋
    - `PolicyReport` ou `ClusterPolicyReport` (audit) 🔍
- Autres solutions : [Open Policy Agent](https://www.openpolicyagent.org/docs/v0.12.2/kubernetes-admission-control/) ou [Validation des politiques d'admission](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) 🔒

---

### 🛠️ Fonctionnalités

- _Accepter / Refuser_ les manifestes de ressources ✅❌
- _Modifier_ les ressources lors de leur création ou de leur mise à jour 🔄
- _Générer_ des ressources supplémentaires lors de leur création 🔄
- _Auditer_ les ressources existantes 🔍
- Voir [une introduction à Kyverno](https://2021-05-enix.container.training/4.yml.html#399) 📚

---

### ⚠️ Mises en garde

- L'écriture et la validation de politiques peuvent être difficiles ⚠️
- Le contexte `{{ request }}` est puissant, mais difficile à valider (Kyverno ne peut pas savoir à l'avance comment il sera rempli) ⚠️
- Les politiques avancées (avec conditions) ont une syntaxe unique et exotique :

```yaml
spec:
=(volumes):
=(hostPath):
path: "!/var/run/docker.sock"
```

---

## 🔐 Kubeseal

- Transforme un `Secret` Kubernetes en `SealedSecret` chiffré (clé privée dans le cluster, clé publique pour générer les secrets, contrôleur `SealedSecrets`). 🔒
- Seul le cluster peut déchiffrer un `SealedSecret` 🔒
- Il devient possible de laisser les _Secret_ chiffrés dans _Git_. 🔐

---
