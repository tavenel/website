---
title: Réseau
description: Réseau
type: cours
sidebar:
  order: 4
tags:
- docker
- kubernetes
- devops
- network
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
---
## 🌐 CIDRs

- Kubernetes utilise uniquement 3 réseaux : 🌐
  - Un CIDR pour faire communiquer les _Nodes_ 🌐
  - Un CIDR _flat_ (en principe isolé) pour les Pods 📦
  - Un CIDR publique (routé par le plugin CNI) pour communiquer au sein du Cluster (pour les `Service`, …) 🌍
- Peuvent s'ajouter des _external IP_ (Load Balancer, …) 🌐

:::tip
v1.33.0 introduit le _Service IP Expansion_ : l'API `ServiceCIDR` permet d'ajouter (dynamiquement) autant de CIDRs que voulu aux `Service`.
:::

---

## DNS

- DNS interne k8s : Pods _CoreDNS_ tournant le namespace `kube-system`
  - Pods `pending` jusqu'à l'installation d'un CNI
- exposés par _Service_ `kubedns` (IP: `10.96.0.10`)
- DNS resolver dans les Pod : service `kubedns`
  - permet de joindre tous les _Service_ par nom _DNS_ :
  - `<nom-du-service>` dans le même _Namespace_
  - `<nom-du-service>.<namespace>.svc.<clustername>` sinon (`<clustername>`: `cluster.local` ou config _CoreDNS_)

---

## 🌐 Service

- Service DNS permettant d'accéder à 1 (ou plusieurs) Pods 🌐
  - Nom DNS court (dans le namespace) : `<service_name>.<namespace>` (ou `<service_name>` si dans le même `namespace`) 📡
  - Nom DNS complet : `<service_name>.<namespace>.svc.<cluster-domain>` 📡
  - Exemple : `mon_service.mon_namespace.svc.mon_cluster` 📡
- Association `Service` <-> `Pod`(s) grâce aux _labels_ 🏷️
  - **Avec gestion des réplicas** 🔄
- Au moins 2 CIDR (plages réseau) : CIDR Pod et CIDR Services 🌐

:::note
Pour des exemples d'usage concrets, voir : <https://sheakimran.hashnode.dev/kubernetes-services-a-deep-dive-with-examples>
:::

---

### 🌐 Service: ClusterIP

- Expose à l'intérieur du cluster uniquement 🏢
- Crée une Virtual IP 🌐
- Accès via le nom du service 📡
- Load balancer interne sur les Pods ⚖️

---

```mermaid
---
title: ClusterIP Multi-Nodes
---
flowchart TD

  subgraph Cluster ["Cluster"]

    svcA["Service blue<br/>clusterIP 10.0.0.5<br/>port 81"]
    svcB["Service green<br/>clusterIP 10.0.0.7<br/>port 82"]
    class svcA blue
    class svcB green

    subgraph node1 ["Node 1"]
        pod1_1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
        class pod1_1 blue
    end

    subgraph node2 ["Node 2"]
        pod2_1["pod-blue-2<br/>10.4.32.5<br/>port 8181"]
        pod2_2["pod-green-1<br/>10.4.32.6<br/>port 8282"]
        class pod2_1 blue
        class pod2_2 green
    end

    subgraph node3 ["Node 3"]
        pod3_1["pod-green-2<br/>10.4.32.8<br/>port 8282"]
        class pod3_1 green
    end

    svcA -.-> pod1_1
    svcA -.-> pod2_1

    svcB -.-> pod2_2
    svcB -.-> pod3_1

  end
```

<div class="caption">ClusterIP multi Nodes</div>

---

```mermaid
---
title: Communication entre Pods par ClusterIP - par Pod 1
---
flowchart TD

    svcB["Service green<br/>clusterIP 10.0.0.7<br/>port 82"]
    class svcB green

    subgraph Cluster ["Cluster"]

        subgraph node1 ["Node 1"]
            pod1_1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
            class pod1_1 blue
        end

        subgraph node2 ["Node 2"]
            pod2_1["pod-blue-2<br/>10.4.32.5<br/>port 8181"]
            pod2_2["pod-green-1<br/>10.4.32.6<br/>port 8282"]
            class pod2_1 blue
            class pod2_2 green
        end

        subgraph node3 ["Node 3"]
            pod3_1["pod-green-2<br/>10.4.32.8<br/>port 8282"]
            class pod3_1 green
        end
    end

    %% Connexions services → pods
    svcB -.-> pod2_2
    svcB -.-> pod3_1

    %% Communication entre pod et service
    pod1_1 e1@-->|"1 - http:// green:82"| svcB
    svcB e2@-->|"2 - http:// 10.4.32.6:8282"| pod2_2

    e1@{ animate : true }
    e2@{ animate : true }
```

```mermaid
---
title: Communication entre Pods par ClusterIP - par Pod 2
---
flowchart TD

    svcB["Service green<br/>clusterIP 10.0.0.7<br/>port 82"]
    class svcB green

    subgraph Cluster ["Cluster"]

        subgraph node1 ["Node 1"]
            pod1_1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
            class pod1_1 blue
        end

        subgraph node2 ["Node 2"]
            pod2_1["pod-blue-2<br/>10.4.32.5<br/>port 8181"]
            pod2_2["pod-green-1<br/>10.4.32.6<br/>port 8282"]
            class pod2_1 blue
            class pod2_2 green
        end

        subgraph node3 ["Node 3"]
            pod3_1["pod-green-2<br/>10.4.32.8<br/>port 8282"]
            class pod3_1 green
        end
    end

    %% Connexions services → pods
    svcB -.-> pod2_2
    svcB -.-> pod3_1

    %% Communication entre pod et service
    pod1_1 e1@-->|"1 - http:// green:82"| svcB
    svcB e2@-->|"2 - http:// 10.4.32.8:8282"| pod3_1

    e1@{ animate : true }
    e2@{ animate : true }
```

<div class="caption">Communication entre Pods par ClusterIP. Le service Green est load-balancé sur pod-green-1 et pod-green-2.</div>

---

### 🌐 Service: NodePort

- Extension du `ClusterIP` 🌐
- Expose à l'extérieur du cluster 🌍
- Accès via des ports sur les Nodes du cluster 🌐
- Load balancer interne sur les Pods ⚖️

---

```mermaid
---
title: NodePort sur port 30001 du Node 1
---
flowchart TD

    svcA["Service blue<br/>NodePort 10.0.0.5<br/>port 81<br/>nodePort 30001"]
    svcB["Service green<br/>NodePort 10.0.0.7<br/>port 82<br/>nodePort 30002"]
    class svcA blue
    class svcB green

    subgraph node1 ["Node 1<br/>172.10.10.1<br/>:30001 :30002"]
        pod1_1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
        class pod1_1 blue
    end

    subgraph node2 ["Node 2<br/>172.10.10.2<br/>:30001 :30002"]
        pod2_1["pod-blue-2<br/>10.4.32.5<br/>port 8181"]
        pod2_2["pod-green-1<br/>10.4.32.6<br/>port 8282"]
        class pod2_1 blue
        class pod2_2 green
    end

    subgraph node3 ["Node 3<br/>172.10.10.3<br/>:30001 :30002"]
        pod3_1["pod-green-2<br/>10.4.32.8<br/>port 8282"]
        class pod3_1 green
    end

   %% Connexions services → pods
    svcA -.-> pod1_1
    svcA -.-> pod2_1

    svcB -.-> pod2_2
    svcB -.-> pod3_1

    %% Utilisateur externe
    User(["User"])

    %% Connexions externes
    User e1@--> |"1 - http:// 127.10.10.1:30001"| node1
    User e2@--> |"2 - http:// pod-blue-1:8181"| pod1_1

    e1@{ animate : true }
    e2@{ animate : true }
```

```mermaid
---
title: NodePort sur port 30002 du Node 1
---
flowchart TD

    svcA["Service blue<br/>NodePort 10.0.0.5<br/>port 81<br/>nodePort 30001"]
    svcB["Service green<br/>NodePort 10.0.0.7<br/>port 82<br/>nodePort 30002"]
    class svcA blue
    class svcB green

    subgraph node1 ["Node 1<br/>172.10.10.1<br/>:30001 :30002"]
        pod1_1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
        class pod1_1 blue
    end

    subgraph node2 ["Node 2<br/>172.10.10.2<br/>:30001 :30002"]
        pod2_1["pod-blue-2<br/>10.4.32.5<br/>port 8181"]
        pod2_2["pod-green-1<br/>10.4.32.6<br/>port 8282"]
        class pod2_1 blue
        class pod2_2 green
    end

    subgraph node3 ["Node 3<br/>172.10.10.3<br/>:30001 :30002"]
        pod3_1["pod-green-2<br/>10.4.32.8<br/>port 8282"]
        class pod3_1 green
    end

   %% Connexions services → pods
    svcA -.-> pod1_1
    svcA -.-> pod2_1

    svcB -.-> pod2_2
    svcB -.-> pod3_1

    %% Utilisateur externe
    User(["User"])

    %% Connexions externes
    User e1@--> |"1 - http:// 127.10.10.1:30002"| node1
    User e2@--> |"2 - http:// pod-green-2:8181"| pod3_1

    e1@{ animate : true }
    e2@{ animate : true }
```

<div class="caption">Communication par NodePort. La communication vers l'adresse IP du Node est redirigée vers un Pod du Service.</div>

---

### 🌐 Service: LoadBalancer

- LoadBalancer pour l'accès au `Pod` depuis l'extérieur 🌍
  - Idéalement directement, sinon par un `NodePort` 🌐
- Permet d'avoir un accès unique à plusieurs conteneurs d'un Pod tournant sur plusieurs Nodes 🌐
- Lié au service de _Load Balancing_ **externe** du Cloud Provider (_ELB_, _Azure LB_, _GCLB_, …) ☁️
  - Dans le cluster : idem `ClusterIP` 🌐
  - Programme un _Load Balancer_ Cloud puis ajoute l'IP **externe** au `Service` 🌍
  - On-premise, installer `MetalLB` 🏢

---

### 🌐 Service: ExternalName

- Référence un DNS interne ou externe (alias) 📡
- Exemple : BDD externe au cluster 💾
- Pas de Load balancer ⚖️

---

### 🔗 EndpointSlice

- Lien `Service` <-> `Pod` (ressource interne) 🔗

---

## 🌍 Ingress

- Point d'accès publique HTTP/HTTPS unique pour l'accès aux différentes Pods (différent d'un Service) 🌍
- Agit comme un _Reverse-proxy_ qui redirige la requête vers le `Service` 🔄
- Règles de routage avancées 📜
- En principe, crée un service `LoadBalancer` (point d'entrée de l'Ingress) ⚖️
- Requiert une implémentation d'`Ingress Controller` à installer : 🛠️
  - ~`Nginx Ingress Controller` : Standard, stable, supporte HTTPS et annotations avancées 🌐 (_Déprécié_) ~
  - `HAProxy Ingress` : Performant ⚡
  - `Traefik` : Léger, dynamique (cloud, microservices) ☁️
  - `Consul Ingress / Istio Gateway` : Intégration avec les _service mesh_ Consul / Istio 🌐

---

```mermaid
---
title: Schema d'un Ingress basé path.
---

graph LR;
  client([client])-. Ingress-managed load balancer .->ingress[Ingress, 178.91.123.132];
  ingress-->|/foo|service1[Service service1:4200];
  ingress-->|/bar|service2[Service service2:8080];
  subgraph cluster
  ingress;
  service1-->pod1[Pod];
  service1-->pod2[Pod];
  service2-->pod3[Pod];
  service2-->pod4[Pod];
  end
```

```mermaid
---
title: Schema d'un Ingress basé hostname.
---

graph LR;
  client([client])-. Ingress-managed load balancer .->ingress[Ingress, 178.91.123.132];
  ingress-->|Host: foo.bar.com|service1[Service service1:80];
  ingress-->|Host: bar.foo.com|service2[Service service2:80];
  subgraph cluster
  ingress;
  service1-->pod1[Pod];
  service1-->pod2[Pod];
  service2-->pod3[Pod];
  service2-->pod4[Pod];
  end
```

<div class="caption">Source: <a href="https://kubernetes.io/docs/concepts/services-networking/ingress/">https://kubernetes.io/docs/concepts/services-networking/ingress/</a></div>

---

## 🌐 Gateway API

- Nouvelle API Kubernetes (successeur Ingress) 🌐
  - Orienté rôles, portable, extensible 🔄
  - Routage multi-namespace 🏷️
  - Décorrélé de l'installation de Kubernetes 🛠️
- `GatewayClass` : Ensemble de `Gateway` avec configuration commune et géré par un contrôleur 🏷️
- `Gateway` : Définit une instance d'infrastructure de gestion du trafic : Cloud load-balancing, … ☁️
- `HTTPRoute` : Règles pour mapper le trafic d'une `Gateway` à un endpoint réseau (`Service`) 🌐

```mermaid
---
title: Gateway API
---

graph LR;
  client([client])-. requête HTTP .->gateway[Gateway];
  gateway-->httpRoute[HTTPRoute];
  httpRoute-->|Règle de routage|service[Service];
  service-->pod1[Pod];
  service-->pod2[Pod];
```

---

## Cas d'usage - quels services utiliser ?

---

### Communication interne entre microservices

#### Cas d'usage

- Une API backend consommée par un frontend
- Un service applicatif appelant un service métier
- Un worker consommant une API interne

#### Service **ClusterIP**

- Accessible uniquement **à l'intérieur du cluster**
- Fournit une **IP virtuelle stable** et un **DNS interne**
- Load-balancing natif entre les Pods via DNS : `service-name.namespace.svc.cluster.local`
- Coupler avec des **NetworkPolicies** pour restreindre les flux

---

### Exposition d'une application web vers l'extérieur

- Application web (HTTP/HTTPS)
- API REST publique
- Dashboard applicatif

#### Option A - NodePort

- Accessible via `IP_du_node:NodePort`
- Cluster bare-metal sans load balancer externe
- Peu sécurisé : environnement de test, labo, formation
- Pas de gestion TLS native

#### Option B - LoadBalancer

- IP externe dédiée
- Intégration avec les load balancers cloud public (AWS, GCP, Azure)
- Bare-metal avec MetalLB / kube-vip
- Support natif du trafic externe
- Utilisé en combinaison avec un **Ingress Controller**

---

### Exposition HTTP/HTTPS multi-services (reverse proxy)

- Plusieurs applications derrière un même point d'entrée
- Routage par nom de domaine ou chemin
- Terminaison TLS centralisée
- **ClusterIP** pour les applications
- **LoadBalancer** ou **NodePort** pour l'Ingress Controller

#### Architecture typique

```
Internet
   |
[ LoadBalancer / NodePort ]
   |
[ Ingress Controller ]
   |
[ Services ClusterIP ]
```

- Mutualisation de l'exposition externe
- Gestion centralisée du TLS (cert-manager)
- Scalabilité et flexibilité élevées

---

### Accès à une base de données ou un service stateful

- PostgreSQL, MySQL, MongoDB
- Redis, Kafka, Elasticsearch

#### Option A - ClusterIP

- Accès simple à une base unique
- Load balancing côté client non requis
- exemple : Application → `postgres.default.svc.cluster.local`

#### Option B - Headless Service

- `clusterIP: None`

- StatefulSets
- Réplication, clustering, leader election
- Résolution DNS par Pod
- Contrôle fin du routage (ex : primary / replicas)
- exemple : `postgres-0.postgres`, `postgres-1.postgres`

---

### Services nécessitant une IP fixe par Pod

- Clusters distribués (Kafka, Cassandra)
- Protocoles non HTTP
- Applications sensibles à l'identité réseau

#### Headless Service

- Pas de load balancing
- DNS renvoyant toutes les IP des Pods
- Indispensable avec `StatefulSet`

---

### Accès à un service externe au cluster

- Base de données externe
- API SaaS
- Service legacy hors Kubernetes

#### ExternalName

- Le Service agit comme un alias DNS
- Redirige vers un FQDN externe

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db-external
spec:
  type: ExternalName
  externalName: db.prod.example.com
```

---

### Exposition directe d'un Pod spécifique

- Debug
- Tests réseau
- Accès temporaire à un composant précis

#### Service **NodePort** ou port-forwarding

- Préférer `kubectl port-forward` en production
- Éviter les Services permanents pour le debug

---

### Services internes nécessitant un accès cross-namespace

- Plateforme partagée (auth, logging, metrics)
- Mutualisation de services transverses

#### Service **ClusterIP**

- accès via DNS FQDN complet
- Exemple : `prometheus.monitoring.svc.cluster.local`

---

### Récapitulatif

| Cas d'usage                 | Type de Service         |
| --------------------------- | ----------------------- |
| Communication interne       | ClusterIP               |
| Application web publique    | LoadBalancer / NodePort |
| Reverse proxy HTTP(S)       | Ingress + ClusterIP     |
| Base de données simple      | ClusterIP               |
| Base de données clusterisée | Headless                |
| StatefulSets                | Headless                |
| Service externe             | ExternalName            |
| Debug / tests               | NodePort / port-forward |

---
