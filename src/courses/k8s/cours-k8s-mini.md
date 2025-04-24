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

```plantuml
@startditaa
+--------------------------------------------------+
|                 Deployment : replicas=2          |
| +---------------------------------------------+  |
| |              ReplicaSet : 2 Pods            |  |
| |  +-----------------+    +-----------------+ |  |
| |  | Pod 1           |    | Pod 2           | |  |
| |  | conteneur nginx |    | conteneur nginx | |  |
| |  +-----------------+    +-----------------+ |  |
| |                                             |  |
| +---------------------------------------------+  |
|                                                  |
+--------------------------------------------------+

@endditaa
```

<div class="caption">Un Deployment gérant un ReplicaSet gérant un Pod</div> 

---

## Service

- Les `Pod` ne communiquent jamais directement mais par les noms DNS de `Service`.
- `Service` == service DNS associé à un Pod ou un Déploiement par un `label` :
  - l'association crée un objet `Endpoint`
  - DNS : `service_name` dans le même namespace (`mon_service`), sinon `service_name.namespace_name` (`mon_service.mon_namespace`).
  - `type=ClusterIP` (defaut) : communication entre `Pod` dans le cluster uniquement
  - `type=NodePort` : ajoute un accès depuis tous les `Node` du cluster
  - autres types : `type=LoadBalancer` (Cloud provider), `type=ExternalName` (alias DNS)


---

```plantuml
@startuml

title "Communication entre Pods par ClusterIP"

!include <kubernetes/k8s-sprites-unlabeled-25pct>

skinparam rectangle {
  RoundCorner 15
}
skinparam defaultFontName "Arial"
skinparam defaultFontSize 14

rectangle Cluster {

  rectangle "<$svc>\nService orange\nclusterIP 10.0.0.7\nport 82" as svcB #Orange

  component "<$node>\nNode 1" as node1 {
    rectangle "<$pod>\npod-blue-1\n10.4.32.2\nport 8181" as pod1 #LightBlue
  }

  component "<$node>\nNode 2" as node2 {
    rectangle "<$pod>\npod-orange-2\n10.4.32.8\nport 8282" as pod2 #Orange
  }

}

' -- Liaisons entre Services et Noeuds --

svcB -[bold,dashed]right-> pod2 #red
pod1 -[bold,dashed]-> svcB #red : <color:red>http://orange:82</color>

@enduml
```

---

```plantuml
@startuml

title "NodePort"

!include <kubernetes/k8s-sprites-unlabeled-25pct>

skinparam rectangle {
  RoundCorner 15
}
skinparam defaultFontName "Arial"
skinparam defaultFontSize 14

rectangle "<$svc>\nService blue\nNodePort 10.0.0.5\nport 81\nnodePort 30001" as svcA #LightBlue

rectangle Cluster {

  component "<$node>\nNode 1\n172.10.10.1\n:30001" as node1
  
  component "<$node>\nNode 2\n172.10.10.2\n:30001" as node2 {
    rectangle "<$pod>\npod-blue-2\n10.4.32.5\nport 8181" as pod #LightBlue
  }

}


' -- Liaisons (flèches) entre Services et Noeuds --
svcA -[dotted]up-> pod

actor User
User -[bold,dashed]-> node1 #red : <color:red>http://127.10.10.1:30001</color>
node1 -[bold,dashed]right-> svcA #red

@enduml

```

---

## Configuration des applications

- `ConfigMap` (`Volume`) pour la configuration des applications
  - autre ressource similaire : `Secret` (mots de passe, …)

---

## Stockage

- `PersistentVolumeClaim` : associe un `PersistentVolume` (disque virtuel géré par une `StorageClass`) à un/des `Pod`

```plantuml
@startuml

title "PV et PVC"

!include <kubernetes/k8s-sprites-unlabeled-25pct>

skinparam rectangle {
  RoundCorner 15
}
skinparam defaultFontName "Arial"
skinparam defaultFontSize 14


rectangle "<$pv>\nPersistentVolume" as pv
rectangle "<$sc>\nStorageClass" as sc #Orange

database "Physical Volume" as db #LightGreen

rectangle "<$pod>\npod" as pod #LightBlue {
  rectangle "<$pvc>\nPersistentVolumeClaim" as pvc {
}

sc -[dotted]-> pv
sc -[dotted]up-> pvc
pv -> db

@enduml
```

---

## Autres ressources

* `Namespace` : espaces de noms isolant des ressources
- `StatefulSet` : composants avec état et ordre à respecter : BDD, … (très différent du reste)
- `Volume` (différent `PersistentVolume`, proche d'un volume _Docker_) : point de montage pour configs, filesystem temporaire, …
- `DaemonSet` : assure que des pods tournent sur tous les noeuds du cluster (ex pour des services techniques)
- `Job` et `CronJob` pour des tâches

