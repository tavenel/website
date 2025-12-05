---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: OpenNebula
layout: '@layouts/CoursePartLayout.astro'
---

## Introduction à OpenNebula

OpenNebula est une plateforme IaaS **open-source de cloud computing** permettant de construire et administrer un **cloud privé, public ou hybride**. Elle fournit :

- un portail d'administration (**Sunstone**),
- un orchestrateur IaaS,
- une gestion avancée des machines virtuelles,
- un système de multi-tenant,
- des fonctionnalités de provisioning automatisé, de réseau virtuel, de stockage distribué,
- des workloads edge,
- et un écosystème complet (OneFlow, OneGate, FireEdge, Marketplace…)

OpenNebula est souvent considéré comme une alternative plus simple à OpenStack ou VMWare Aria, tout en conservant des fonctionnalités avancées.

### Cas d'usage

- Cloud privé dans un datacenter
- Plateforme de provisioning pour DevOps
- Hébergement interne de VM pour plusieurs équipes
- Hybridation avec AWS, Azure ou GCP
- Edge computing (via Firecracker, LXC…)
- Formation et environnements pédagogiques

![Sunstone UI](https://docs.opennebula.io/7.0/images/sunstone_cloud_dash.png)

<div class="caption">Le frontend Sunstone d'OpenNebula (source : docs.opennebula.io)</div>

## Architecture générale

OpenNebula s'articule autour de :

- **Front-end** :

  - Sunstone (GUI)
  - OneFlow (orchestration)
  - OneGate (communication avec VM)
  - FireEdge (API moderne)
- **Hosts** : nœuds de virtualisation (KVM, VMware, Firecracker)
- **Datastores** : stockage des images, VM, systèmes
- **Virtual Networks** : gestion réseau (bridges, VXLAN, Open vSwitch, Edge Clusters)
- **Marketplace** : images prêtes à l'emploi

Schéma simplifié :

```
             +---------------------------+
             |        USERS / ADMINS     |
             +--------------+------------+
                            |
                        Sunstone GUI
                            |
                 +----------+-----------+
                 |   OpenNebula Frontend |
                 |  oned / FireEdge API  |
                 +----------+-----------+
                            |
      ---------------------------------------------------
      |                     |                           |
   Host KVM            Host KVM                  Host Firecracker
(Compute+Storage)   (Compute+Storage)              (Edge/Light VM)
```

![Architecture OpenNebula](https://docs.opennebula.io/7.0/images/overview_key-features.png)

<div class="caption">Architecture OpenNebula (source : docs.opennebula.io)</div>

![Compostants OpenNebula](https://docs.opennebula.io/7.0/images/overview_architecture.png)

<div class="caption">Composants OpenNebula (source : docs.opennebula.io)</div>

---

## Installation et prise en main

### Installation standard (KVM)

Le plus simple : **frontend + node KVM**.

#### Installation du front-end

```bash
sudo apt update && sudo apt install -y opennebula opennebula-sunstone
sudo systemctl enable --now opennebula opennebula-sunstone
```

Sunstone disponible sur :

```
http://<IP_frontend>:9869
```

Login : `oneadmin` / mot de passe généré dans `/var/lib/one/.one/one_auth`.

#### Installation du nœud KVM

```bash
sudo apt install -y qemu-kvm libvirt-daemon-system bridge-utils
sudo systemctl enable --now libvirtd
```

Configurer accès SSH pour oneadmin (obligatoire).

#### Ajouter le nœud à OpenNebula

```bash
onehost create node1 --im kvm --vm kvm
onehost list
```

## Parcourir Sunstone

**Tableau de bord** : état général, hosts, VMs, clusters.

Menus principaux :

- **Instances** : VMs + services OneFlow
- **Templates** : VM Templates, Services
- **Storage** : images, datastores
- **Network** : VNETs, security groups
- **Infrastructure** : hosts, clusters, VNets
- **System** : users, groups, quotas, ACL

:::link
Pour apprendre à utiliser Sunstone, voir la documentation : <https://docs.opennebula.io/7.0/product/control_plane_configuration/graphical_user_interface/cloud_view/>
:::

---

## Gestion du stockage (Images & Datastores)

### Types de datastores

- **Image Datastore** : stockage des images (golden images)
- **System Datastore** : stockage runtime des disques VMs
- **File Datastore** : context, fichiers annexes

### Importer une image

```
oneimage create --name ubuntu22 --path https://cloud-images... --datastore default
```

Ou depuis Sunstone → Storage → Images → +.

### Créer un datastore NFS ou Ceph

OpenNebula supporte :

- NFS,
- Ceph RBD,
- Gluster,
- LVM,
- ZFS.

Exemple Ceph (fichier `ceph_ds.conf`) :

```
NAME = "ceph-system"
DS_MAD = ceph
TM_MAD = ceph
POOL_NAME = "rbd"
```

---

## Gestion réseau (VNETs, IPAM, SDN)

### Types de virtual networks

- **Bridged** (simple, adapté aux labs)
- **VXLAN / Open vSwitch** (multi-tenant avancé)
- **VLAN 802.1q**
- **Edge Network (FireEdge)**

### Créer un réseau simple en bridge

```yaml
NAME="public-net"
BRIDGE="br0"
VN_MAD="dummy"
TYPE="FIXED"
AR=[ IP=192.168.100.100, SIZE=100 ]
```

```
onevnet create public-net.yml
```

### Sécurité réseau

- **Security Groups**
- **Firewall rules** (in/out)
- **Isolation VXLAN**

---

## Gestion des Templates & Contextualisation

### Templates de VM

Un **template** est une description complète d'une VM : CPU, RAM, disques, cartes réseaux, context, cloud-init.

Exemple :

```yaml
NAME="ubuntu-base"
CPU="2"
MEMORY="4096"
DISK=[ IMAGE="ubuntu22" ]
NIC=[ NETWORK="public-net" ]
CONTEXT=[ NETWORK="YES", SSH_PUBLIC_KEY="$USER[SSH_PUBLIC_KEY]" ]
```

### Cloud-init via OpenNebula

Cloud-init est automatiquement injecté via la section `CONTEXT`.

Exemple cloud-init custom :

```yaml
CONTEXT=[
  NETWORK="YES",
  SSH_PUBLIC_KEY="$USER[SSH_PUBLIC_KEY]",
  USER_DATA="#!/bin/bash
  apt update && apt install -y nginx",
]
```

---

## Déploiement et gestion des VMs

### Lancement d'une VM

Depuis Sunstone :

1. Instances → VMs → +
2. Choix du template
3. Lancement

CLI :

```
onevm create ubuntu-base
onevm list
```

### Actions courantes

- Start / Stop / Reboot
- Live migrate
- Snapshot
- Save / Resume
- NIC attach/detach
- Disk attach/detach

### Monitoring des VMs

- CPU, RAM, IO
- Graphiques Sunstone
- Intégration Prometheus (via exporters)

---

## Gestion multi‑tenant : Users, Groups, VDCs

### Users

Types d'utilisateurs :

- oneadmin (super admin)
- utilisateurs simples

### Groups

Chaque groupe peut avoir :

- quotas,
- limitations,
- VDC,
- ACL personnalisées.

### Virtual Data Centers (VDC)

Un VDC regroupe :

- des hosts,
- des datastores,
- des réseaux,
- des utilisateurs.

Permet d'offrir un cloud privé par équipe : Dev, Ops, SecOps…

### ACL

Les ACL permettent un contrôle fin :

```
oneacl create "@dev GROUP/VM+MANAGE" 
```

---

## Marketplace & Services (OneFlow)

### Marketplace

OpenNebula propose des images pré-packagées :

- Ubuntu, AlmaLinux, Debian
- Kubernetes appliances
- Firecracker images
- Load balancers

### Services OneFlow

Déploiement multi‑tier (frontend + backend + DB) avec :

- scaling,
- dépendances,
- policies.

Exemple : déployer un stack LAMP via OneFlow.

---

## Fonctionnalités avancées

### Autoscaling

Basé sur :

- CPU VM,
- métriques externes,
- règles OneFlow.

### FireEdge & Edge Clusters

Permet :

- provisioning bare-metal distant,
- déploiements edge avec Firecracker,
- gestion via API moderne (FireEdge UI).

### Virtualisation légère : Firecracker

OpenNebula supporte :

- MicroVMs,
- ultra‑rapides,
- faible overhead.

---

## Supervision et observabilité

### Exporters Prometheus

- **one-exporter** : métriques OpenNebula
- **node-exporter** : hosts
- **libvirt-exporter**

### Grafana dashboards

Dashboards standards :

- état des VMs
- ressources des hosts
- networks

---

## Bonnes pratiques

### Réseau

- Utiliser VXLAN pour isolation multi-tenant
- Toujours sécuriser Sunstone via HTTPS

### Stockage

- Préférer Ceph pour la résilience
- Séparer datastore système / datastore images

### Provisioning

- Utiliser cloud-init + Ansible
- Grouper les templates par équipes

---

## Annexes

### Commandes CLI essentielles

```
onehost list
onevnet list
onevm create <tmpl>
onevm show <id>
oneimage list
```

### Template Cloud-init

```yaml
#cloud-config
packages:
  - htop
  - curl
ssh_pwauth: false
users:
  - default
runcmd:
  - echo "Hello from OpenNebula" > /root/hello.txt
```

### VDC multi‑équipe

- groupe dev → quotas CPU/RAM
- groupe ops → accès escaladé
- réseau isolé VXLAN

---

### Liens

- Vidéo de présentation d'OpenNebula : "Introduction to Open Nebula" : <https://opennebula.io/screencasts/>
- [MiniOne : Installation simple d'OpenNebula pour test](https://docs.opennebula.io/7.0/getting_started/try_opennebula/opennebula_on-prem_with_minione/deploy_opennebula_onprem_with_minione/)
