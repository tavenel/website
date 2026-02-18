---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Kubernetes
layout: '@layouts/CoursePartLayout.astro'
tags:
- kubernetes
- intro
---

## Introduction

**Kubernetes**, souvent abrégé **K8s**, est une plateforme open-source d'orchestration de conteneurs conçue pour automatiser le déploiement, la mise à l'échelle et la gestion d'applications conteneurisées dans un parc de machines.

---

### Pourquoi Kubernetes ?

Avec la généralisation de **Docker** et des conteneurs, il est devenu simple d'exécuter une application de façon isolée. En revanche, gérer **des dizaines ou centaines de conteneurs** sur plusieurs serveurs pose rapidement des problèmes :

- redémarrage automatique en cas de crash
- répartition de charge
- montée/descente en charge (scaling)
- mises à jour sans interruption de service
- découverte de services et réseau interne
- gestion de la configuration et des secrets

Kubernetes apporte une **couche d'abstraction** au-dessus de l'infrastructure pour résoudre ces problématiques.

---

### Concepts clés

- Un **cluster Kubernetes** est un ensemble de machines (**Nodes**) physiques ou virtuelles qui exécutent des conteneurs. 2 types de Node :
  - **Control Plane** : composants internes de Kubernetes gérant le cluster
  - **Workers** : machines qui exécutent les conteneurs applicatifs
- Un **Pod** est l'unité minimale de déploiement (abstraction autour d'un conteneur).
- Un **Deployment** décrit l'état désiré d'une application :
  - nombre de réplicas
  - version de l'image
  - stratégie de mise à jour
- Un **Service** fournit une **adresse réseau stable** pour accéder aux Pods, même s'ils sont recréés.
- Kubernetes fonctionne sur le principe de **l'état désiré** (_desired state_), par ex _3 instances du backend_, et Kubernetes s'occupe d'y parvenir et de le maintenir (_réconciliation_).

---

### Utilisation

En pratique :

- On décrit les ressources dans un manifest Yaml.
- On interagit avec le cluster principalement via `kubectl`.

```yaml
# my_app.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: demo
  template:
    metadata:
      labels:
        app: demo
    spec:
      containers:
        - name: web
          image: nginx:latest
          ports:
            - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: demo-service
spec:
  type: NodePort
  selector:
    app: demo
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30007
```

```bash
kubectl apply -f my_app.yaml
kubectl get pods
#NAME        READY   STATUS    RESTARTS   AGE   IP            NODE       NOMINATED NODE   READINESS GATES
#demo-app-01 1/1     Running   0          20s   10.244.0.34   minikube   <none>           <none>
kubectl get service demo-service
#NAME          TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
#demo-service  NodePort   10.96.98.162   <none>        80:30007/TCP   6s
kubectl delete -f my_app.yaml
```

---

