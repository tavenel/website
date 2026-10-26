---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Arrêt et redémarrage d'un cluster complet
type: cours
sidebar:
  order: 20
description: Arrêt et redémarrage d'un cluster complet
---

## 🎯 Objectifs

- éviter corruption d'`etcd`
- éviter pods orphelins
- préserver état du control-plane
- éviter split-brain

:::caution
Attention : kubeadm ne supporte pas officiellement l'arrêt d'un cluster complet.
:::

Ordre logique global :

1. **Phase Applicative**
2. **Phase Kubernetes**
3. **Phase Services système**
4. **Extinction machines**

## Backup ETCD

Fortement recommandé !

```bash
ETCDCTL_API=3 etcdctl snapshot save /root/etcd-snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

:::tip
À copier hors machine.
:::

## Arrêter les workflows critiques

Downscaler manuellement les services, démonter les stockages critiques

Objectif : éviter corruption de données, verrous, transactions incomplètes, caches incohérents.

### Downscale des Deployments et StatefulSets critiques

Cas typiques :

- API métiers
- Batchs
- Jobs planifiés
- Outils d'import/export
- Workers Kafka / RabbitMQ
- Applications écrivant en base

```bash
kubectl scale deployment api-prod --replicas=0 -n prod
kubectl scale deployment batch-worker --replicas=0 -n prod
kubectl scale statefulset postgres --replicas=0
```

Option plus propre :
Labeler les workloads critiques :

```bash
kubectl label deploy api-prod shutdown=graceful
kubectl scale deploy -l shutdown=graceful --replicas=0 -A
```

### Suspendre les CronJobs

Objectif : éviter le redémarrage des pods pendant l'arrêt.

```bash
kubectl patch cronjob myjob -p '{"spec":{"suspend":true}}'
```

## Démonter Storage Critique

- NFS
- iSCSI
- CephFS
- Gluster
- SAN

1. Vérifier volumes montés

```bash
mount | grep kubelet
```

2. Démonter proprement

```bash
umount /var/lib/kubelet/pods/*
```

## Cordon + Drain des workers

Sur **chaque worker** :

```bash
kubectl cordon <node>
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
```

Ordre :

1. Workers
2. Puis control-planes secondaires (si High Availability)
3. Control-plane principal en dernier

## Arrêt des services

Sur **chaque node** :

```bash
systemctl stop kubelet
systemctl stop containerd
shutdown -h now
```

- Ordre conseillé :
  1. Workers
  2. Control-planes secondaires
  3. Control-plane principal
- Ne pas stopper `etcd` seul si stacked etcd : kubelet gère le pod statique (sinon arrêter (les) etcd distant(s)).

## Redémarrage

1. Ordre inverse.
2. Uncordon
3. Vérifications sur control-plane principal :

   ```bash
   kubectl get nodes
   kubectl get pods -A
   ```

Si node `NotReady` :

```bash
journalctl -u kubelet -xe
```

## Cluster de test

Voir la [cheatsheet](/k8s/cheatsheet) pour une procédure d'arrêt / redémarrage simple pour un cluster de test sur sa machine personnelle.
