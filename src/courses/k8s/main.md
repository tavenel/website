---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Kubernetes
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

## 🚀 Comparaison des Plateformes de Conteneurs

---

### 🌟 Introduction

> Une plateforme de conteneurs est un ensemble d'outils et de services qui permettent de gérer le cycle de vie des applications conteneurisées. 📦

- **Orchestration** : Gestion automatisée du déploiement, de la mise à l'échelle, et de la mise en réseau des conteneurs. 🔄
- **Évolutivité** : Capacité à ajuster les ressources et les services en fonction de la demande. 📈
- **Isolation** : Exécution sécurisée et isolée des applications pour éviter les conflits. 🔒
- **Portabilité** : Exécution cohérente des applications sur différents environnements (développement, test, production ; on-premise et multi-cloud). 🌍

---

### 🧩 Kubernetes

- **Description** : Plateforme open-source pour l'automatisation du déploiement, la mise à l'échelle et la gestion des applications conteneurisées. 🌐
- De loin l'orchestrateur **le plus utilisé avec Docker®** 🏆
- **Avantages** 🌟 :
  - Grande communauté et écosystème 👥
  - Hautement extensible avec de nombreux outils et extensions 🛠️
  - Prise en charge de charges de travail complexes 🏋️
- **Inconvénients** ❌:
  - Courbe d'apprentissage abrupte 📚
  - Configuration complexe ⚙️
- Pour les **déploiements complexes et évolutifs** 🌐

---

### 🚀 OpenShift

- **Description** : Plateforme de conteneurs de Red Hat, basée sur Kubernetes, avec des fonctionnalités supplémentaires pour les entreprises. 🏢
- **Avantages** 🌟 :
  - Intégration facile avec d'autres produits Red Hat 🔄
  - Interface utilisateur intuitive 🖥️
  - Sécurité et conformité renforcées 🔒
- **Inconvénients** ❌:
  - Coût élevé pour les fonctionnalités d'entreprise 💰
  - Moins flexible que Kubernetes seul 🤸
- Pour les **solutions d'entreprise avec support** 🏢

---

### 🐳 Docker Swarm

- **Description** : Solution d'orchestration de conteneurs intégrée à Docker, simple et facile à utiliser. 🐋
- **Avantages** 🌟 :
  - Intégration transparente avec Docker 🔄
  - Facile à configurer et à utiliser 🛠️
  - Idéal pour les petits déploiements 🏠
- **Inconvénients** ❌:
  - Manque de fonctionnalités avancées 🛑
  - Communauté et écosystème plus petits 👥
- Pour les **environnements simples et rapides** 🏡

---

### 🏗️ Apache Mesos

- **Description** : Projet open-source pour la gestion des ressources dans les centres de données, prenant en charge les conteneurs et les charges de travail non conteneurisées. 🏢
- **Avantages** 🌟 :
  - Flexibilité pour gérer divers types de charges de travail 🔄
  - Évolutivité et robustesse 📈
- **Inconvénients** ❌:
  - Complexité de configuration et de gestion ⚙️
  - Moins axé sur les conteneurs que les autres solutions 🎯
- Pour les **environnements hybrides et complexes** 🏗️

---

### 📊 Comparaison

| Plateforme | Facilité d'utilisation | Évolutivité | Écosystème | Coût |
|------------|-----------------------|-------------|------------|------|
| Kubernetes | ⭐️⭐️⭐️ | ⭐️⭐️⭐️⭐️ | ⭐️⭐️⭐️⭐️ | 🆓 |
| OpenShift | ⭐️⭐️⭐️⭐️ | ⭐️⭐️⭐️⭐️ | ⭐️⭐️⭐️ | 💰 |
| Swarm | ⭐️⭐️⭐️⭐️ | ⭐️⭐️⭐️ | ⭐️⭐️ | 🆓 |
| Mesos | ⭐️⭐️ | ⭐️⭐️⭐️⭐️ | ⭐️⭐️ | 🆓 |

---

## 🎭 Présentation de Kubernetes

---

`Kubernetes` (ou `k8s`) est un orchestrateur de déploiement et de gestion de conteneurs applicatifs dans un cluster de machines virtuelles. 🚀

- Indépendant de Docker® mais même runtime `containerd` => peut tourner les mêmes images 🐳
- Configure et gère un cluster applicatif complexe : nœuds du cluster, réseau, stockage, ... 🌐
- Possibilité de gérer tout le cluster via API `kubectl` 🔧
- Mais configuration recommandée via `Yaml` / `Json` pour audit 📝

---

## 💡 Recommandations

- `Docker®` seul / `docker compose` pour CI/CD et outils internes 🛠️
- `k8s®` pour gestion applicative de l'environnement de production 🏗️
- `k8s®` duplique des fonctionnalités de Docker® => préférer 100% Docker® ou k8s® 🔄

---

## 📦 Technologies de conteneurs supportées

1. `containerd` : projet open-source créé pour Kubernetes (runtime de `Docker` : _Docker sans la CLI_) 🐳
2. `Docker Engine` : _Docker avec la CLI_ 🐳
3. `Podman` : alternative _serverless_ à Docker 🐳
4. `CRI-O` : conteneurs légers 📦
5. `Mirantis Container Runtime (MCR)` (anciennement _Docker Enterprise_) 🏢

---

```mermaid
---
title: Architecture des technologies de conteneurs
---
flowchart TD
    A["Docker (CLI)"]
    B[Kubernetes]
    
    A --> ContainerD
    B --> CRI

    CRI["Container Runtime Interface (CRI)<br/>[Kubernetes API]"]
    CRI --> ContainerD
    CRI --> CRIO

    ContainerD["ContainerD (pull images, network, storage)"]
    CRIO[CRI-O]

    ContainerD --> OCI
    CRIO --> OCI

    OCI["Open Container Interface (OCI) spec"]
    OCI --> runC

    runC["runC (create / run containers)"]
    runC --> Container[Container]
```

---

## 🌐 Plugin réseau (CNI)

- **Container Networking Interface** (_CNI_) : 🌍
  - Permet la communication réseau au sein du cluster 🌐
  - Parfois intégré à la distribution, sinon à installer séparément 🛠️
  - [GitHub - CNI](https://github.com/containernetworking/cni/) 🔗
  - Par défaut, _Kubelet_ charge les configurations des plugins réseau depuis : `/etc/cni/net.d` 📂

---

### 🔄 CNI (Kubernetes) vs CNM (Docker)

- **Docker** : 🐳
  - Réseaux **multiples** et **isolés** 🌐
  - DNS par **réseau** 📡
  - **Pas d'interconnexion** des réseaux ❌

- **Kubernetes** : 🚀
  - **1 seul** réseau de conteneurs (_flat_) 🌍
  - DNS par **`Namespace`** 📡
  - **Aucune isolation** des réseaux par défaut (utiliser des `NetworkPolicies`) ⚠️

---

### 🌐 Flannel

- Réseau de sous-réseaux pour Kubernetes 🌐
- Fonctionne avec divers backends (VXLAN, UDP, etc.) 🔄
- Offre une isolation réseau par pod 🔒
- Plus simple à configurer que les autres options 🛠️
- Inconvénients : Peut introduire une latence supplémentaire, moins de fonctionnalités avancées (`NetworkPolicies`, …), moins adapté aux très grands clusters ⚠️

:::link
Pour plus d'information sur Flannel, voir : <https://msazure.club/flannel-networking-demystify/>
:::

---

### 🛡️ Calico

- Supporte plusieurs modes de réseau : 🌐
  - routage direct
  - VXLAN seul
  - IPIP + BGP
  - eBPF
  - cross-subnet possible (tout ou aucun traffic ou uniquement la partie qui traverse un subnet) : AWS multi-AZ, azure vnets, réseaux L2 hétérogènes
- Propose une isolation réseau granulaire (par pod) 🔒
- Intègre de la sécurité 🛡️
- Conçu pour des (très) grands clusters 🏗️
- S'intègre bien avec l'infrastructure existante 🔄
- Souvent utilisé dans les déploiements Cloud ☁️
- Inconvénients : Complexe, besoin de compatibilité réseau (BGP) ⚠️

:::link
Voir aussi :

- Calico en VXLAN ou IPIP : <https://docs.tigera.io/calico/latest/networking/configuring/vxlan-ipip>
- Introduction à eBPF et utilisation en Calico : <https://docs.tigera.io/calico/latest/about/kubernetes-training/about-ebpf>

:::

---

### 🕸️ Weave

- Crée un réseau virtuel entre tous les conteneurs 🌐
- Utilise le DNS intégré de Docker 📡
- Propose une isolation réseau par pod 🔒
- Facile à configurer mais peut être moins performant que les autres options 🛠️

---

### ⚡ Cilium

- Utilise _eBPF_ (_Berkeley Packet Filter_) ⚡
  - (Très) performant, débit élevé et latence réduite ⚡
- Métriques détaillées sur le trafic réseau 📊
- Supporte dynamiquement l'ajout et la suppression de nœuds 🔄
- Conçu pour gérer des clusters de grande taille 🏗️
- Inconvénients : Complexe (eBPF et concepts réseau avancés), eBPF doit être activé dans le noyau Linux ⚠️

:::tip

- Cilium fournit un outil de monitoring (_Hubble_) avec une CLI et UI permettant de visualiser les communications au sein du cluster.
- Cilium fournit un "_Cluster Mesh_" (⚠️ à ne pas confondre avec un _Service Mesh_ k8s) permettant une communication load balancé entre _Service_ de différents clusters.

:::

---

### ❔ Autres

- D'autres CNI exotiques existent :
- `Canal` (`Flannel` + `Calico`) pour ajouter les `NetworkPolicies` (ou avant le support des VXLAN par Flannel)
- CNIs Cloud : _Amazon VPC CNI_ (_EKS_), _Azure CNI_ (_AKS_), _GCP CNI_ (_GKE_), _NSX-T CNI_ (_VMware Tanzu_), _Cisco ACI CNI_, …
- _SR-IOV CNI_ (haute performance, accès direct au _NIC_)
- _Macvlan CNI_
- `kindnetd` pour _kind_
- …

---

| Critère | Calico | Flannel | Weave Net | Cilium |
|-------------|------------|-------------|---------------|------------|
| **Type de Réseau** | Couche 3 (IPIP, BGP, VXLAN) | Couche 3 (VXLAN, UDP) | Couche 2 (Overlay) | Couche 3 (eBPF) |
| **Sécurité** | Politiques de réseau granulaires | Politiques de réseau basiques | Politiques de réseau basiques | Politiques de réseau granulaires |
| **Performance** | Haute | Moyenne | Moyenne | Très haute |
| **Scalabilité** | Très élevée | Moyenne | Moyenne | Très élevée |
| **Complexité** | Moyenne à élevée | Faible | Faible à moyenne | Élevée |
| **Fonctionnalités** | Avancées (BGP, IPIP, VXLAN) | Basiques | Basiques à moyennes | Avancées (eBPF, DNS, chiffrement) |
| **Compatibilité** | Kubernetes, OpenShift, Docker | Kubernetes, Docker | Kubernetes, Docker, Mesos | Kubernetes |
| **Résilience** | Élevée | Moyenne | Élevée | Élevée |

---

## 📦 Distributions Kubernetes

---

1. **Kubeadm** 🛠️
   - Outil officiel
   - Installation de chaque composant séparément
   - Le plus configurable mais le plus complexe

---

1. **Kubespray** 🔄
   - Utilise `Ansible` pour (re)déployer automatiquement un cluster
   - Compatible _bare-metal_ et _cloud_ ☁️

---

1. **Rancher (RKE)** 🏗️
   - Plateforme complète pour gérer des clusters Kubernetes
   - Propose des fonctionnalités avancées comme la gestion multi-cluster 🌐
   - Offre une interface graphique intuitive 🖥️

---

1. **K3s (Rancher Labs)** 📦
   - Version allégée de Kubernetes conçue pour les environnements embarqués
   - Consomme moins de ressources que Kubernetes standard 🔋
   - Idéal pour les systèmes à faible puissance ⚡
   - Utilise le CNI `flannel` 🌐
   - Voir aussi : _k3d_ (_k3s in Docker_) : similaire _kind_ (voir ci-dessous) pour k3s 🐳

---

1. **K0s (CNCF)** 📦
   - Autre version allégée Kubernetes
   - Très minimale, aucun composant additionnel 🔧
   - Compatible on-premise, edge, IoT, … 🌍

---

1. **OpenShift** 🏢
   - Distribution propriétaire de Red Hat basée sur Kubernetes
   - Inclut des fonctionnalités supplémentaires comme l'orchestration d'applications 🛠️
   - Forte sécurité et conformité 🔒

---

1. **Docker Kubernetes Service (DKS)** 🐳
   - Surveillance intégrée du cluster et des applications 👁️
   - Nombreux drivers storage 💾

---

1. **MicroK8s (Ubuntu)** 📦
   - Distribution légère et sécurisée de Kubernetes
   - Conçue pour les environnements Ubuntu 🐧
   - Propose des fonctionnalités avancées comme l'installation de paquets 📦

---

1. **Minikube** 🧪
   - Version légère pour le développement et le test
   - Fonctionne sur un seul ordinateur 💻
   - Idéal pour débutants et environnement de développement 🛠️

---

1. **Docker Desktop** 🐳
    - Intègre Kubernetes nativement
    - Offre une expérience utilisateur simplifiée 🖥️
    - Adapté aux développeurs utilisant Docker 🛠️

---

1. **Kind (Kubernetes IN Docker)** 🧪
    - Déploie Kubernetes dans un conteneur pour le développement et le test
    - Crée rapidement un ou plusieurs clusters localement 🏗️
    - Utile pour tester plusieurs clusters : upgrade, changements d'infrastructure, … 🔄
    - CNI custom : `kindnetd` 🌐
    - Utilise `kubeadm` 🛠️

---

1. **Talos Linux** 🐧
    - Distribution Linux dédiée
    - OS immuable : pas de SSH, shell, … 🔒

---

### ☁️ Plateformes managées

- Amazon Elastic Kubernetes Service (EKS) 🌐
- Google Kubernetes Engine (GKE) 🌐
- Azure Kubernetes Services (AKS) 🌐
- Oracle Kubernetes Engine (OKE) 🌐
- IBMCloud K8s 🌐
- OVHCloud K8s 🌐

:::tip
Les services gérés coûtent souvent 30 à 50 % de plus que les services autogérés, mais réduisent considérablement les frais opérationnels ([source](https://testkube.io/blog/when-to-adopt-kubernetes-pay-now-or-pay-later-dilemma)).
:::

---

:::link
Il existe de (très) nombreuses manières d'installer Kubernetes : voir <https://github.com/zwindler/101-ways-to-deploy-kubernetes>
:::

---

## 🏗️ Architecture

---

### 🛠️ Installation

- Plusieurs méthodes :
  - `kubeadm` : l'outil officiel (installation de chaque composant séparément) 🛠️
  - Installeur intégré dans la distribution : `k3s`, `minikube`, `microk8s`, … 📦
  - Versions managées : outils dédiés au fournisseur de Cloud ☁️

---

### 📂 Modèle

- Un cluster k8s est composé de plusieurs `Node` 🌐
- Chaque `Node` fait tourner des `Pod` (ensemble de conteneurs - c'est l'unité atomique de k8s !) 📦
- Un `Deployment` gère _déclarativement_ des ressources à déployer (pods, replicas, mise à jour, …) 🔄
- Un `Service` permet d'exposer les ports d'un pod (interne ou externe) 🌍
  - _Aucun lien avec un `service` de `docker-compose` !_ ⚠️

---

### 🏷️ Types de Nodes

- Node de rôle `master` : le `control pane`, gère le cluster (orchestration, API server, …) 🏢
- Node de type `worker` (sans rôle) : exécute les pods et leur fournit les ressources 🛠️

---

### ❌Limites

- k8s est fait pour gérer de gros clusters : 🏗️
- Limitations Kubernetes v1.31 :
  - < 5,000 Node 🌐
  - < 110 Pod / Node 📦
  - < 150,000 Pod (total) 📦
  - < 300,000 Containers (total) 📦

---

![Architecture d'un cluster Kubernetes](https://kubernetes.io/images/docs/kubernetes-cluster-architecture.svg)

<div class="caption">Architecture d'un cluster Kubernetes (source: kubernetes.io)</div>

---

```mermaid
---
title: Architecture d'un Pod
---
flowchart TD
    subgraph Node
        subgraph "Pod : 1 adresse IP"
            Logger[Conteneur docker : logger]
            Nginx[Conteneur docker : nginx]
        end
    end

  class Logger,Nginx blue
```

<div class="caption">Architecture d'un Pod</div>

---

## 🧩 Composants

- `APIServer` : API de gestion du cluster 🌐
- `etcd` : Stockage de la configuration du cluster 📂
- `Controller Manager` : Gère les `WorkerNode` depuis le `MasterNode` 🏢
- `Kubelet` : Exécute et gère les conteneurs sur les `Node` 📦
- `Kube-proxy` : Équilibre le trafic sur chaque `Node` 🌍
- `Scheduler` : Assigne les `Pod` à un `Node` 📅

---

### 📂 etcd

- Backend k8s : État du cluster (le reste est stateless) 📂
  - Store clé=valeur 🔑
- Dans ou en dehors du cluster 🌐
- 1 leader (par consensus) 🏆
  - Déployer un nombre impair d'instances 🔢
  - Supporte N/3 instances défaillantes ⚠️
- Jamais utilisé directement (`APIServer`) ⚠️
- Critique ! 🚨
  - Machine dédiée ou environnement isolé 🏢
  - Bonnes performances réseau / disque ⚡

---

### 🔄 ControllerManager

- Compare l'état désiré (déclaratif) à l'état actuel 🔄
- En déduit (et applique) les actions nécessaires (`APIServer`) 🛠️
- Beaucoup de contrôleurs différents 🧩
  - Possibilité d'installer des contrôleurs externes pour gérer de nouvelles ressources (`Custom Resource Definition`) 🔧
  - Exemple : Load Balancer AWS, … ☁️
- Boucles de réconciliation : 🔄
  - Reconstruit des ressources si besoin pendant le cycle de vie du cluster 🔄
  - Sans besoin d'intervention 🛠️
- Contient toute l'intelligence de Kubernetes 🧠

---

```mermaid
---
title: "Boucle de réconciliation"
---
flowchart TD
    Observation --> Diff
    Diff --> Action
    Action --> Observation

```

---

### 📅 Scheduler

- Assigne les `Pod` (en state: `Pending`) aux `Node` 📅
  - Techniquement : crée un `Binding` et change le `nodeName` du `Pod` 🔧
- Calcule de score par _filtrage_ puis _score_ : 📊
  1. _Filtrage_ : Capacité, tolérance, affinité, sélecteurs, … 🔍
  2. _Score_ : Load-balancing, … ⚖️
- Possibilité d'installer un `Scheduler` customisé 🔧

---

### 📦 Kubelet

- 1 `Kubelet` par `Node` 📦
  - Un `kubelet` est souvent installé sur le `MasterNode` pour y gérer ses composants dans des pods (optionnel) 🏢
  - En général, on y ajoute le `taint` : `node-role.kubernetes.io/control-plane:NoSchedule` pour ne pas utiliser le _Master_ comme un _Worker_. ⚠️
- Connexion permanente à l'`APIServer` 🌐
- Déploie le `Pod` s'il a le `nodeName` du `Node` courant : 📦
  1. Récupération de l'image (format `OCI`) 📥
  2. Création des ressources : `Volumes`, `Networks`, `Containers` 🛠️
  3. États du `Pod` : `pending` -> `running` / `failed` -> `succeeded` (terminé) 🔄
  4. Remonte l'information à l'`APIServer` 📤

---

### 🌐 Kube-proxy

- Gère le réseau sur chaque `Node` (entre Pods et vers extérieur) 🌍
- Plusieurs modes : 🔄
  - Tout trafic par (anciennement: `iptables`) `nftables`, règles `DNAT` (⚠️ CPU si beaucoup de règles) ⚠️
    - Load-balancer : _round-robin_ 🔄
  - Si CNI `Cilium` : Règles `eBPF` dans le noyau, plus besoin de `Kube-proxy` 🌟
    - Voir section sur les CNI 📚
- Connexion entre `Pods` : Niveau 3 (_IP_) 🌐
- Connexion par `Services` : Niveau 4 (_TCP_, _UDP_) 🌍
- Connexion par `Ingress` : Niveau 7 (_HTTP_) 🌐

---

:::link
**Voir : <https://2021-05-enix.container.training/5.yml.html#50> pour un exemple de fonctionnement du _Control Plane_ suite à la création d'un `Deployment`**
:::

---

## 🛠️ Gestion du cluster

- Fichiers de configuration `yml` (à privilégier autant que possible !) 📄
- Interface en ligne de commande `kubectl` (surtout pour lancer les fichiers de config) 🖥️
- Interface web (peu utilisée) 🌐

---

## 📂 Ressources basiques du cluster

---

### 🔄 Interactions entre ressources

- Les `Pod` exécutent les microservices. 📦
- Les `Service` exposent ces pods pour permettre leur communication et leur accès. 🌐
- Les `ConfigMap` et `Secret` injectent les configurations et les données sensibles. 🔐
- Le/Les `Ingress` gèrent le trafic externe (routage par _URI_ ou header _host_) et les certificats SSL/TLS. 🌍
- Les `PersistentVolume` et `StatefulSet` supportent les applications avec état. 💾
- Les `DaemonSet` assurent le fonctionnement des outils d'administration sur chaque nœud. 🛠️

---

### 📦 Gestion des applications

- `Deployment` : Gère le déploiement d'un `ReplicaSet` 📦
  - Et la mise à jour des applications (rolling update, rollback, scaling) 🔄
- `ReplicaSet` : Crée et gère le suivi (réplicas) d'un pod 📦
  - Ne pas utiliser de `ReplicaSet` directement mais passer par un `Deployment` (plus puissant) 🛠️
- `Pod` : Gère un ensemble de conteneurs partageant la même isolation : stack réseau, stockage, … 📦
  - Démarré directement ou (mieux) par un `deployment` créant un `ReplicaSet` 📦
  - Éphémère : Pas de données critiques dans le pod ⚠️
  - 1 IP par pod partagée entre tous les conteneurs (mais l'IP peut changer) 🌐
    - Accès par `localhost` aux autres conteneurs et **partage des ports ouverts** 🔄

---

```mermaid
---
title: Deployment, ReplicaSet et Pods
---
flowchart TD
    subgraph "Deployment : replicas = 2"
        subgraph "ReplicaSet : 2 Pods"
            Pod1[Pod 1 : nginx]
            Pod2[Pod 2 : nginx]
        end
    end

    class Pod1,Pod2 green
```

<div class="caption">Un Deployment gérant un ReplicaSet gérant un Pod</div>

---

### 🏷️ Labels

- Attributs clé=valeur des objets du cluster 🏷️
- Utilisé par Kubernetes 🛠️
- `NodeSelector` : Lance un pod sur un `Node` ayant ce label 🏷️
- `NodeAffinity` : Décrit des affinités entre un `Pod` et un `Node` 🏷️
- `podAffinity`, `podAntiAffinity` : (Anti)affinité entre `Pod` 🏷️
- Il existe aussi des `annotations` : Idem mais NON utilisé par k8s ensuite 📝

---

#### 🐛 Labels et debug

- Beaucoup de ressources utilisent les labels pour sélectionner les ressources (`Pod`, …) à manager 🏷️
- Pour debugger un `Pod` fautif, on peut changer son `Label` : 🐛
  - Le Pod fautif sera retiré du Service (plus de Load balancing) ⚖️
  - Un nouveau Pod est créé par le `ReplicaSet` ou le `DaemonSet` 📦
  - Le Pod fautif est toujours actif pour du debug 🐛

---

### 🌐 Service

- Service DNS load-balancé permettant d'accéder à 1 ou plusieurs Pods 🌐
- Exemple : `<service_name>.<namespace>`
- Plusieurs types de services :
  - `ClusterIP` accessible uniquement dans le cluster
  - `NodePort` pour un accès depuis l'extérieur
  - `LoadBalancer` pour utiliser un Load Balancer externe (cloud)
  - `ExternalName` pour un alias DNS

---

### 🛠️ Configuration des applications

- `ConfigMap` pour modifier la configuration des applications 📝
  - Décorrélé du code de l'application 🛠️
- `Secret` (mots de passe, …) : Assez similaire 🔐
  - [Différents types de Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#secret-types) 🔗
  - ⚠️ Par défaut, **simple encodage** : Voir les [bonnes pratiques de sécurité](https://kubernetes.io/docs/concepts/security/secrets-good-practices/) 🔒
  - [Chiffrement possible](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) des accès _REST_ mais l'_API Server_ ne peut plus démarrer automatiquement (si très fort besoin de sécurité uniquement) 🔒
- `ConfigMap` et `Secret` peuvent être _immuable_ 🔒

---

### 💾 Stockage

- `PersistentVolume` (`PV`) => Vision _storage_ du cluster Kubernetes, un espace de stockage 💾
- `PersistentVolumeClaim` (`PVC`) => Un type de `Volume` permettant de réquisitionner et d'utiliser un `PV` dans un `Pod` 📝

---

## 🛠️ Ressources avancées

---

### 🛡️ DaemonSet

- Assure que des pods tournent sur tous les nœuds du cluster 🛠️
- Utile pour monitoring & logs 📊
- Exemple : Installation d'un _Load Balancer_ `MetalLB` sur tous les _Node_ du cluster ⚖️

---

### 💾 StatefulSet

- Déploie des applications avec état : BDD, … 💾
- Metadatas semblables au `Deployment` mais très différent des autres ressources en pratique (beaucoup de cas particuliers à k8s)
- Ressources **ordonnées** (ordre de lancement) 📜
- Un `PV` par _Pod_ (vs. _ReplicaSet_ où les volumes sont partagés) 💾
- _Persistent volume claim templates_ (`spec.volumeClaimTemplates`) : Crée un `PVC` par _Pod_ nommé `<claim-name>.<stateful-set-name>.<pod-index>` 📝
- Un même volume monté dans un pod (`PVC`) le reste pour toujours (même après recréation) 🔄
- Un DNS dédié (_service headless_) : 📡
  - Load-balancing sur tous les pods du set ⚖️
  - Sélection d'un pod en particulier 🎯

:::tip
Le _StatefulSet_ est utile lorsque l'on doit pouvoir différencier et sélectionner les différentes instances à déployer (par exemple BDD SQL : Pod `primaire` vs Pod `secondaire`)
:::

---

#### Deployment vs StatefulSet

| Caractéristique | Deployment | StatefulSet |
|----------------|------------|-------------|
| **Nom des pods** | Aléatoire (app-xxx-yyy) | Ordonné (app-0, app-1, app-2) |
| **Identité** | Interchangeable | Unique et stable |
| **Nom DNS** | Variable | Stable et prévisible |
| **Ordre de déploiement** | Parallèle | Séquentiel (0→1→2) |
| **Ordre de suppression** | Aléatoire | Inverse (2→1→0) |
| **Stockage** | Partagé ou éphémère | Dédié par pod |
| **Persistance après redémarrage** | Non garantie | Garantie |
| **Scaling** | Parallèle | Séquentiel |

---

### ⏳ Job et CronJob

- Pour travaux "longs" (> minutes / heures) ⏳
- `Job` : Démarre un `Pod`, en cas d'échec, relance jusqu'au _backoff limit_ (default=6) 🔄
  - Paramètres : `completions` (default=1) => Nombre d'exécutions, `parallelism` (default=1) ⚙️
- `CronJob` : Nécessite un `schedule` (idem _Cron_ sur _UNIX_) ⏰

---

### 💿 Device Plugin

- Permet de déclarer des ressources au _Kubelet_ pour les utiliser des les _Pod_
- ex : `nvidia-device-plugin` pour les GPU nvidia

:::tip
Les _Device_ sont assez limités (statiques, réquisition unique, …). Kubernetes introduit les [_Dynamic Ressource Allocation_ (_DRA_)](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
:::

:::link
Pour débugger les Pods avec Device, voir : <https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/>
:::

---

### 🔐 cert-manager (TLS)

- CRD à ajouter au Cluster pour générer et signer des `Certificat` 🔐
- Stocke la `key` et le `crt` dans un `Secret` 🔒
  - Réutilisables dans `Ingress`, … 🌐
- Utilise des `Issuer` (namespace-limited) ou des `ClusterIssuer` (cluster-wide) 🏷️

---

## 🛠️ Configuration du cluster

- `Metadata` pour chaque ressource (nom, labels, annotations, …) 🏷️
- `Namespace` : Espaces de noms isolant des ressources 🏷️
  - Cloisonne une partie du cluster 🏗️
  - Similaire namespace Linux 🐧
  - Namespaces spéciaux : 🏷️
    - `kube-public` : Ressources accessibles à tous (par ex pour le _bootstrap_ du cluster) 🌍
    - `kube-system` : Composants Kubernetes 🏗️
    - `default` : Si aucun namespace spécifié 🏷️
- Rôles 👥

---

## 🛡️ Service Mesh

- Ajoute les services d'infrastructure communs 🛠️
  - Authentification 🔐
  - Sécurité 🛡️
  - Logs 📝
- Gère la communication sécurisée entre conteneurs sur des architectures micro-services 🌐
- À installer : `Istio`, `linkerd`, `consul`, … 🛠️
  - Voir la [page des outils Devops](https://www.avenel.pro/tools#-kubernetes-specific) 🔗

---

## 📚 Commandes de base de Kubernetes®

Voir la [cheatsheet sur Kubernetes®](https://www.avenel.pro/k8s/cheatsheet) 📚

---

## Structure d'un fichier k8s

```yaml
apiVersion: v1 # Version de l'APIServer k8s
kind: … # Le type de ressource à gérer : Pod, Deployment, Service, …
metadata: # Métadatas de la ressource
  name: … # nom (interne) de la ressource à créer et/ou monitorer
  namespace: mon-namespace # Namespace spécial (optionnel - sinon default)
  labels: # ajout de labels (optionnel)
    ma-cle: ma-valeur 
  […]
spec: # Les spécifications de la ressource. Différent pour chaque type de ressource
  […]
```

---
