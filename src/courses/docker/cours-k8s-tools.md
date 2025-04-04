---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Outils externes
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

# Helm : déploiement applicatif

- Gestionnaire de "paquets" k8s
  - en fait des fichiers Yaml
  - ajout du versionning
- `chart` : ensemble de fichiers manifests, `templates`, … avec paramètres
- Stockés dans des `repositories` : <https://hub.helm.sh/>, …
- `values.yaml` : valeurs par défaut
- `template` : manifest Kubernetes avec _templates Go_.
- `release` : un déploiement de `chart` (versionnée : upgrade, rollback, uninstall)
- trouver des `chart` : <https://artifacthub.io/>

---

## Charts Helm populaires

---

1. **MySQL** :
   - **Description** : Déploie une instance MySQL.
   - **Repository** : `bitnami/mysql`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-mysql bitnami/mysql
     ```

---

2. **WordPress** :
   - **Description** : Déploie une instance WordPress avec une base de données MySQL.
   - **Repository** : `bitnami/wordpress`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-wordpress bitnami/wordpress
     ```

---

3. **MongoDB** :
   - **Description** : Déploie une instance MongoDB.
   - **Repository** : `bitnami/mongodb`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-mongodb bitnami/mongodb
     ```

---

4. **Redis** :
   - **Description** : Déploie une instance Redis.
   - **Repository** : `bitnami/redis`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-redis bitnami/redis
     ```

---

5. **Nginx** :
   - **Description** : Déploie une instance Nginx.
   - **Repository** : `bitnami/nginx`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-nginx bitnami/nginx
     ```

---

6. **PostgreSQL** :
   - **Description** : Déploie une instance PostgreSQL.
   - **Repository** : `bitnami/postgresql`
   - **Exemple de commande** :
     ```sh
     helm repo add bitnami https://charts.bitnami.com/bitnami
     helm install my-postgresql bitnami/postgresql
     ```

---

7. **Kubernetes Dashboard** :
   - **Description** : Déploie le Kubernetes Dashboard pour la gestion visuelle du cluster.
   - **Repository** : `kubernetes/dashboard`
   - **Exemple de commande** :
     ```sh
     helm repo add kubernetes https://kubernetes.github.io/dashboard
     helm install my-dashboard kubernetes/dashboard
     ```

---

8. **Prometheus & Grafana** :
   - **Description** : Déploie la stack Prometheus & Grafana pour la surveillance et la collecte de métriques.
   - **Repository** : `prometheus-community/prometheus`
   - **Exemple de commande** :
     ```sh
     helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
		 helm install my-prometheus prometheus-community/kube-prometheus-stack
		 # ou seulement Prometheus :
		 # helm install prometheus-community/prometheus
     ```

---

# GitOps : FluxCD, ArgoCD, Jenkins X

- Outils Gitops pour k8s
    - scrute un dépôt Git distant
    - mise à jour automatique des ressources k8s
    - plus de CLI `kubectl`
    - Utilise des `Kustomizations` de `Kustomize` (outil intégré à k8s)
- intégrations Helm et Terraform
- CLI `fluxctl` (pas de GUI)
- Interface Web _Argo CD_, _Jenkins X_

---

![Architecture de FluxCD](https://raw.githubusercontent.com/fluxcd/flux2/main/docs/diagrams/fluxcd-controllers.png)

<div class="caption">Architecture de FluxCD (source: documentation FluxCD)</div>

---

![Architecture d'ArgoCD](https://argo-cd.readthedocs.io/en/stable/assets/argocd_architecture.png)

<div class="caption">Architecture d'ArgoCD (source: documentation ArgoCD)</div>

---

# Kyverno

- Limitations des permissions standard Kubernetes - comment :
  - Interdire l’utilisation du tag `:latest`
  - Obliger chaque _Deployment_, _Service_, … à avoir un label `owner`
  - Obliger chaque conteneur à avoir un `readinessProbe`
  - Obliger chaque `Namespace` à avoir des quotas et des limites
- Solution : utiliser un `AdmissionController`

---

## [Kyverno](https://github.com/kyverno/kyverno/) : moteur de politiques pour k8s

- Gère des règles de sécurité, de conformité et de gestion (fichiers Yaml)
  - _Controller_ ou _Operator_ Kubernetes, _Webhooks_ et _CRDs_ de politiques, principalement :
	- `Policy` ou `ClusterPolicy` (par _Namespace_ ou global au Cluster)
	- `PolicyReport` ou `ClusterPolicyReport` (audit)
- Autres solutions : [Open Policy Agent](https://www.openpolicyagent.org/docs/v0.12.2/kubernetes-admission-control/) ou [Validation des politiques d'admission](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
---

## Fonctionnalités

- *Accepter / Refuser* les manifestes de ressources
- *Modifier* les ressources lors de leur création ou de leur mise à jour
- *Générer* des ressources supplémentaires lors de leur création
- *Auditer* les ressources existantes
- Voir [une introduction à Kyverno](https://2021-05-enix.container.training/4.yml.html#399)

---

## Mises en garde

- L'écriture et la validation de politiques peuvent être difficiles
- Le contexte `{{ request }}` est puissant, mais difficile à valider (Kyverno ne peut pas savoir à l'avance comment il sera rempli)
- Les politiques avancées (avec conditions) ont une syntaxe unique et exotique :
```yaml
spec:
=(volumes):
=(hostPath):
path: "!/var/run/docker.sock"
```

---

# Kubeseal

- Transforme un `Secret` Kubernetes en `SealedSecret` chiffré (clé privée dans le cluster, clé publique pour générer les secrets, contrôleur `SealedSecrets`).
- Seul le cluster peut déchiffrer un `SealedSecret`
- Il devient possible de laisser les _Secret_ chiffrés dans _Git_.

---

