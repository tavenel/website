---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Résumé Kubernetes basique
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

## Kubernetes

- Cluster de `Nodes` (serveurs physiques ou VMs) :
  - _worker_ (exécute des applications)
  - _control plane_ (administre le cluster et stocke l'état dans _etcd_)
- Administration via ligne de commandes `kubectl` et fichiers de manifests en `yaml`
- Ensemble de ressources (`kind: …`), ajout possible de `CRD` (_Custom Ressource Definition_)
- Réconciliation de ressources : les `Controller` adaptent le Cluster en permanence vers l'état attendu

---

## Déploiements applicatifs

- `Pod` : abstraction d'un (normalement) unique _Conteneur_ : backend, frontend, …
- `Deployment` : gère le déploiement d'un `ReplicaSet` (nombre de `Pod`)
  - et la mise à jour du `Pod` (rolling update, rollback, scaling)

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

## Service

- Les `Pod` ne communiquent jamais directement mais par les noms DNS de `Service`.
- `Service` == service DNS associé à un Pod ou un Déploiement par un `label` :
  - l'association crée un objet `EndpointSlices`
  - DNS : `service_name` dans le même namespace (`mon_service`), sinon `service_name.namespace_name` (`mon_service.mon_namespace`).
  - `type=ClusterIP` (defaut) : communication entre `Pod` dans le cluster uniquement
  - `type=NodePort` : ajoute un accès depuis tous les `Node` du cluster
  - autres types : `type=LoadBalancer` (Cloud provider), `type=ExternalName` (alias DNS)


---

```mermaid
---
title: Communication entre Pods par ClusterIP
---
flowchart TD

    subgraph Cluster ["Cluster"]

        svcB["Service green<br/>clusterIP 10.0.0.7<br/>port 82"]
        class svcB green

        subgraph node1 ["Node 1"]
            pod1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
            class pod1 blue
        end

        subgraph node2 ["Node 2"]
            pod2["pod-green-2<br/>10.4.32.8<br/>port 8282"]
            class pod2 green
        end
    end

    svcB e1@--> |forward| pod2
    pod1 e2@--> |"http:// green:82"| svcB
    e1@{ animate : true }
    e2@{ animate : true }
```

<div class="caption">Communication interne dans le cluster par Cluster IP.</div>

---

```mermaid
---
title: NodePort
---
flowchart TD

    subgraph Cluster ["Cluster"]

        svcA["Service blue<br/>NodePort 10.0.0.5<br/>port 81<br/>nodePort 30001"]
        class svcA blue

        subgraph node1 ["Node 1<br/>172.10.10.1<br/>:30001"]
            pod1["pod-green-1<br/>10.4.32.4<br/>port 8282"]
            class pod1 green
        end

        subgraph node2 ["Node 2<br/>172.10.10.2<br/>:30001"]
            pod2["pod-blue-1<br/>10.4.32.5<br/>port 8181"]
            class pod2 blue
        end
    end


    %% Utilisateur externe
    User(["User"])
    class User actor

    %% Accès externe simulé
    User e1@--> |"http:// 127.10.10.1:30001"| node1
    node1 e2@--> |routage NodePort| svcA
    svcA e3@--> pod2

    e1@{ animate : true }
    e2@{ animate : true }
    e3@{ animate : true }
```
<div class="caption">Communication depuis l'extérieur par NodePort.</div>

---

## Configuration des applications

- `ConfigMap` (`Volume`) pour la configuration des applications
  - autre ressource similaire : `Secret` (mots de passe, …)

---

## Stockage

- `PersistentVolumeClaim` : associe un `PersistentVolume` (disque virtuel géré par une `StorageClass`) à un/des `Pod`

```mermaid
---
title: PV et PVC
---
flowchart TD

    %% Composants
    pv["PersistentVolume"]
    sc["StorageClass"]
    db[(Physical Volume)]
    class sc red
    class db green

    %% Pod et PVC imbriqués
    subgraph pod ["pod"]
        pvc["PersistentVolumeClaim"]
    end
    class pod blue

    %% Relations
    sc -.-> pv
    sc -.-> pvc
    pv --> db
```

<div class="caption">StorageClass, PersistentVolume, PersistentVolumeClaim et volume physique.</div>

---

## Autres ressources

* `Namespace` : espaces de noms isolant des ressources
- `StatefulSet` : composants avec état et ordre à respecter : BDD, … (très différent du reste)
- `Volume` (différent `PersistentVolume`, proche d'un volume _Docker_) : point de montage pour configs, filesystem temporaire, …
- `DaemonSet` : assure que des pods tournent sur tous les noeuds du cluster (ex pour des services techniques)
- `Job` et `CronJob` pour des tâches

