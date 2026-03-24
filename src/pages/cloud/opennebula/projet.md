---
title: Projet Montage d'un Virtual Data Center
date: 2025 / 2026
---

## Présentation du projet

### Résumé

Ce projet vise à faire concevoir, déployer et exploiter un **Virtual Data Center** complet sur OpenNebula, automatisé et observable. Les étudiants fourniront une infrastructure documentaire, du code Infrastructure-as-Code (Terraform), des playbooks Ansible, une solution de supervision (Prometheus/Grafana) et de centralisation des logs (Loki) ainse qu'un petit cluster Kubernetes dans OpenNebula et démontreront l'observabilité applicative.

**Technologies** : OpenNebula, Prometheus, Grafana, Loki, Terraform, Ansible, Kubernetes

### Objectifs pédagogiques

À l'issue du projet, les étudiants devront être capables de :

1. Concevoir l'architecture d'un cloud privé simple basé sur OpenNebula.
2. Déployer et configurer OpenNebula dans un environnement virtualisé.
3. Écrire des modules Terraform pour provisionner des VMs dans OpenNebula.
4. Automatiser la configuration et le déploiement des services avec Ansible.
5. Mettre en place une chaîne d'observabilité : Prometheus (métriques), Grafana (dashboards), Loki (logs) et Alertmanager.
6. Documenter l'infrastructure et rédiger un rapport technique professionnel.
7. Déployer et monitorer un cluster Kubernetes provisionné sur OpenNebula.

### Prérequis

- Connaissances de base Linux (CLI, réseau, services)
- Virtualisation (KVM/QEMU) et notions de stockage réseau
- Notions de réseau (VLAN, NAT, routage de base)
- Accès à un hyperviseur (ou VMs) pour le lab : au moins 6 VMs, ou accès à un environnement cloud pour provisionner des VMs

## 🎯 Objectif global du projet

Le projet vise donc à concevoir une **plateforme cloud basée sur OpenNebula** avec une dimension DevOps / Platform Engineering permettant :

- de fournir des **environnements isolés par tenant (multi-tenancy)**
- de **provisionner automatiquement une infrastructure complète**
- de permettre le **déploiement rapide de clusters Kubernetes**
- d'intégrer **observabilité + automatisation (DevOps-ready)**

:::tip
Autrement dit : construire une **offre "VDC-as-a-Service"** orientée onboarding rapide, donc un mini équivalent de AWS/GCP… basé sur OpenNebula
:::

### 🧭 Plateforme

👉 Ce que vous construisez réellement : une **plateforme interne de type cloud provider** avec :

| Niveau        | Rôle                  |
| ------------- | --------------------- |
| OpenNebula    | IaaS                  |
| VDC           | Boundary multi-tenant |
| Automation    | Provisioning          |
| Kubernetes    | PaaS                  |
| Observabilité | Exploitabilité        |

## 🧱 Rôle du VDC

Un **VDC (Virtual Data Center)** est :

- un **environnement isolé**
- regroupant :
  - compute (VMs)
  - réseau(x) isolé(s)
  - stockage
- associé à :
  - un ou plusieurs groupes utilisateurs
  - des quotas et ACL

➡️ Il constitue **l'unité de multi-tenancy principale**

```
VDC Tenant A
├── Groupes utilisateurs
├── Réseaux (privé, public)
├── Templates VM
├── Images
├── Quotas
└── ACL
VDC Tenant B
├── Groupes utilisateurs
├── Réseaux (privé, public)
├── Templates VM
├── Images
├── Quotas
└── ACL
…
```

:::link
Voir aussi : <https://opennebula.io/blog/experiences/managing-virtual-data-centers-with-opennebula-zones/>
:::

### 🧠 Architecture

Le VDC n'est pas juste une feature OpenNebula, c'est **le produit final à industrialiser**

Chaque tenant doit recevoir un VDC prêt à l'emploi avec :

- réseau préconfiguré
- templates VM
- images
- quotas
- droits utilisateurs

## 🚀 Objectif clé : onboarding automatisé d'un tenant

- C'est le cœur du projet : 👉 _Créer un VDC = onboarder un client_
- Un client (tenant) doit pouvoir (en quelques minutes) :
  - **demander un VDC**
  - **déployer un cluster K8s**
  - **consulter ses métriques**

### Exemple de pipeline d’onboarding automatisé

1. Création du VDC
2. Création des groupes utilisateurs
3. Allocation des ressources :
   - clusters
   - datastores
   - réseaux
4. Déploiement des templates :
   - VM Linux
   - images cloud-init ou Packer
5. Configuration réseau
6. Injection des accès (SSH / credentials) avec credentials isolés par tenant

## Exemple de produit final

Exemple de produit final : modules Terraform personnalisés permettant l'onboarding d'un tenant : création d'un VDC et d'un cluster k8s

```hcl
module "tenant_vdc" {
  name        = "tenant-a"
  cpu_quota   = 100
  ram_quota   = 256GB
  networks    = ["private", "public"]
}

module "k8s_vdc" {
  vdc = "vdc-a"
  workers = 2
}
```

:::tip
Ceci est la vision finale du projet : on pourra dans un premier temps se limiter à un exemple de code Terraform à modifier pour chaque tenant.
:::

### Exemple de découpage

1. Terraform : 1 VM
   - accès API OpenNebula
   - création d'une VM
   - utilisation d'un template existant ou créé simplement
2. Terraform : N VMs + réseau
   - `count` ou `for_each`
3. Ansible : exécution de playbook dans les VMs créées par terraform
   - provisioning (Terraform) et inventaire dynamique (Terraform output)
   - configuration (Ansible) : users, packages, Docker / container runtime, sécurité de base, …
4. Observabilité : monitoring/logs(/traces) :
   - Monitoring des VMs : Prometheus + Grafana (node exporter sur chaque VM)
   - Logs centralisés avec Loki + Promtail + Grafana (agent Loki / promtail)
5. Kubernetes : cluster automatisé
   - déploiement des nodes : VMs terraform
   - configuration des nodes : Ansible
   - `kubeadm init` (master)
   - `kubeadm join` (workers)
6. Assembler toutes les briques : VDC complet + onboarding
   - module Terraform pour créer un VDC
   - module Terraform pour déployer un cluster k8s dans un VDC
   - dahsboard par tenant

## 🚀 Critères de notation

- ✅ **Industrialisation** :
  - VDC reproductible
  - templates standardisés
- ⚡ **Rapidité** : onboarding < 10 min
- 🔁 **Idempotence** : relancer sans casser
- 📈 **Scalabilité** : N tenants sans redesign
- 🔍 **Observabilité** : visibilité complète par tenant

### Livrables finaux

1. **Dépôt Git** (structure propre) contenant :

   - `terraform/` : modules + exemples d'usage
   - `ansible/` : roles, playbooks, inventories
   - `grafana/` : dashboards JSON
   - `prometheus/` : config, rules
   - `loki/` : pipeline config
   - `docs/` : architecture, guide d'installation, procédure de reprise, rapport final
   - `k8s/` : ressources Kubernetes
2. **Rapport technique** : architecture, choix techniques, difficulté rencontrées, résultats
3. **Screencast / Démo / Slides** pour la soutenance : 20 minutes montrant provisioning, monitoring et logs

### Conseils & pièges courants

- **Itérer rapidement** : encouragez de petites boucles (terraform apply + ansible) plutôt que des changements massifs.
- **Gestion des secrets** : ne stocker aucun secret en clair dans le repo (utiliser Ansible Vault / HashiCorp Vault / variables CI chiffrées).
- **State Terraform** : pour un TP, un backend local est acceptable ; pour les groupes avancés proposer un "remote state" (consul/s3).
- **Timeboxing** : respecter les jalons ; fournir des rendus intermédiaires.

### Étapes optionnelles pour aller plus loin (pour groupes avancés)

- Mettre en place un catalogue d'images automatisé (Packer)
- Déployer Grafana Alertmanager avec notification (email / slack)

## ⚙️ Enjeux techniques liés au VDC

### Isolation stricte

- isolation réseau
- isolation compute
- isolation IAM (groupes / ACL)

:::warn
➡️ Le tenant **ne voit jamais l'infrastructure physique**
:::

### Allocation dynamique des ressources

- un VDC = mapping vers :

  - clusters
  - datastores
  - réseaux

➡️ Possibilité de :

- partager des ressources
- ou dédier des pools

### Modèle "self-service"

- ➡️ Un VDC est proche d'un modèle **mini cloud public interne** avec :
- admin VDC :
  - crée réseaux, templates
  - gère utilisateurs
- utilisateurs :
  - déploient leurs VMs / services

## ☸️ Déploiement simplifié de Kubernetes

- Le VDC sert de **substrat pour K8s**
- Il est attendu dans chaque VDC :
  - templates pour _master nodes_ et _worker nodes_
  - automatisation : (cloud-init / Packer) / Ansible / Terraform
  - provisioning rapide d'un cluster

## 📊 Observabilité obligatoire

- 👉 Objectif : donner au tenant une **vision complète de son VDC** ➡️ sans fuite inter-tenant :

- **Infrastructure** :
  - métriques VM / hyperviseur
  - capacité (CPU, RAM, storage)
- **Kubernetes** :
  - métriques cluster
  - logs
  - events
- **Tenant** :
  - visibilité isolée par VDC

## Conception & préparation

- Formation des équipes, répartition des rôles
- Atelier conception : diagramme d'architecture du Virtual DC
- Préparation des machines et images (création d'une image Linux de référence, cloud-init/ssh)
- Mise en place du dépôt Git (structure initiale)

**Livrable** : diagramme d'archi + repo git initial (README)

## Installation d'OpenNebula

### Objectifs

- Comprendre les composants d'OpenNebula
- Installer et configurer une plateforme OpenNebula minimaliste (Front-end Sunstone + KVM Node)
- Vérifier la communication et configurer les réseaux de base
- Configuration base de données, utilisateurs, authentification (ssh, bonus LDAP)

### Étapes

#### Installation du Front-End OpenNebula

```bash
sudo apt update && sudo apt -y install gnupg
wget -q -O- https://downloads.opennebula.io/repo/repo.key | sudo apt-key add -
echo "deb https://downloads.opennebula.io/repo/6.8/Ubuntu/22.04 stable opennebula" | sudo tee /etc/apt/sources.list.d/opennebula.list
sudo apt update
sudo apt install opennebula opennebula-sunstone opennebula-gate opennebula-flow -y
```

Activer et démarrer les services :

```bash
sudo systemctl enable --now opennebula opennebula-sunstone
```

#### Configuration du nœud KVM

```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y
sudo systemctl enable --now libvirtd
```

Ajouter l'utilisateur `oneadmin` sur le nœud :

```bash
sudo useradd -m oneadmin
sudo passwd oneadmin
sudo usermod -aG libvirt oneadmin
```

Copier la clé SSH du front-end vers le nœud :

```bash
sudo -u oneadmin ssh-copy-id oneadmin@opennebula-compute-1
```

#### Ajouter le nœud à OpenNebula

Depuis le front-end :

```bash
sudo -u oneadmin onehost create kvm-opennebula-compute-1 --im kvm --vm kvm
```

Vérifier :

```bash
sudo -u oneadmin onehost list
```

#### Configuration réseau de base

Créer un réseau virtuel :

```bash
cat <<EOF > network.yml
name: public-net
bridge: br0
vn_mad: dummy
phydev: br0
ip_ranges:
  - start: 192.168.100.100
    end: 192.168.100.200
EOF
onevnet create network.yml
```

### Livrables

- Capture d'écran de Sunstone opérationnel
- `onehost list`
- `onevnet list`

## Création d'images & VM Templates

### Objectifs

- Créer une image _cloud-init_
- Importer dans l'_Image Datastore_
- Construire un template complet prêt au déploiement automatisé
- Ajout du datastore/images et tests de création VM manuelle via Sunstone

### Étapes

#### Importer une image cloud officielle

```bash
sudo -u oneadmin oneimage create \
--name "ubuntu2204-cloud" \
--path https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img \
--datastore default
```

#### Préparation du cloud-init context

Créer un fichier `cloud-init.tpl` :

```yaml
#cloud-config
hostname: vm-$(NAME)
manage_etc_hosts: true
users:
  - name: ubuntu
    groups: sudo
    shell: /bin/bash
    ssh_authorized_keys:
      - $(SSH_KEY)
```

#### Création du template

```bash
cat <<EOF > template.yml
NAME="ubuntu22-base"
CPU="1"
MEMORY="2048"
DISK=[ IMAGE="ubuntu2204-cloud" ]
NIC=[ NETWORK="public-net" ]
CONTEXT=[
  NETWORK="YES",
  SSH_PUBLIC_KEY="\$USER[SSH_PUBLIC_KEY]",
]
EOF
one template create template.yml
```

#### Déploiement d'une VM

```bash
onevm create template.yml
onevm list
```

### Livrables

- Template final (.yml)
- Capture écran de la VM active

## Construction d'images Cloud avec HashiCorp Packer

### Objectifs

- Comprendre l'utilité du _baking d'images_ dans un Virtual Data Center.
- Concevoir une image personnalisée pour OpenNebula via Packer.
- Automatiser la génération d'images compatibles KVM/Firecracker.
- Intégrer Packer dans une pipeline IaC (Terraform + OpenNebula).

### Installation de Packer

- Installation sur le bastion :

  ```bash
  curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
  sudo apt-add-repository "deb https://apt.releases.hashicorp.com $(lsb_release -cs) main"
  sudo apt-get update && sudo apt-get install packer
  ```

### Création d'un template Packer OpenNebula

```
packer/
 ├── http/
 │    └── preseed.cfg
 ├── scripts/
 │    ├── harden.sh
 │    └── install-tools.sh
 └── template.json
```

**Builder OpenNebula KVM**

Fichier : `template.json`

```json
{
  "builders": [
    {
      "type": "qemu",
      "iso_url": "https://releases.ubuntu.com/22.04/ubuntu-22.04-live-server-amd64.iso",
      "iso_checksum": "sha256:xxxxxxxx",
      "output_directory": "output-ubuntu",
      "vm_name": "ubuntu-2204-base",
      "disk_size": 8192,
      "format": "qcow2",
      "headless": true,
      "ssh_username": "packer",
      "ssh_password": "packer",
      "ssh_timeout": "20m",
      "boot_command": [
        "<esc><wait>",
        "auto url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/preseed.cfg ",
        "<enter>"
      ],
      "http_directory": "http"
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "script": "scripts/install-tools.sh"
    },
    {
      "type": "shell",
      "script": "scripts/harden.sh"
    }
  ],
  "post-processors": [
    {
      "type": "shell-local",
      "inline": [
        "mv output-ubuntu/ubuntu-2204-base qcow2-image/ubuntu-2204.qcow2"
      ]
    }
  ]
}
```

### Provisioning de l'image

```bash
apt update
apt install -y qemu-guest-agent curl vim

# hardening
sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart ssh
```

### Production de l'image

```bash
packer init .
packer validate template.json
packer build template.json
```

Résultat attendu :

- Une image QCOW2 optimisée pour OpenNebula
- Données de provisioning appliquées
- SSH sécurisé
- Agent QEMU présent (affichage IP dans Sunstone)

### Import de l'image dans OpenNebula

Via Sunstone :
**Storage → Images → + Create → OS → QCOW2 → Upload**

ou en CLI :

```bash
oneimage create --name ubuntu-2204-base \
  --path qcow2-image/ubuntu-2204.qcow2 \
  --datastore default \
  --type OS
```

### Intégration Packer + Terraform

- Utiliser Packer pour créer une _source_image_id_ dans un module Terraform :

```hcl
resource "opennebula_image" "base" {
  name = "ubuntu-base"
  path = "qcow2-image/ubuntu-2204.qcow2"
  datastore_id = 1
}
```

### 💡 Livrables attendus

- Projet Packer complet (template.json + scripts + preseed).
- Image QCOW2 fonctionnelle dans OpenNebula.

## Terraform pour OpenNebula

### Objectifs

- Installer Terraform
- Initialiser un provider OpenNebula
- Déployer une VM via Terraform

### Étapes

#### Installer Terraform

```bash
sudo apt install unzip -y
wget https://releases.hashicorp.com/terraform/1.9.0/terraform_1.9.0_linux_amd64.zip
sudo unzip terraform_* -d /usr/local/bin/
```

#### Provider OpenNebula

Créer `main.tf` :

```hcl
provider "opennebula" {
  endpoint = "http://opennebula-master:2633/RPC2"
  username = "oneadmin"
  password = "votre_password"
}

resource "opennebula_virtual_machine" "vm1" {
  name = "terraform-vm"
  template_id = 10
}
```

#### Déploiement

```bash
terraform init
terraform plan
terraform apply
```

### Livrables

- Répertoire Terraform
- `terraform plan` (capture)

## Automatisation Ansible pour OpenNebula

### Objectifs

- Installer Ansible
- Créer un playbook déployant un service sur une VM OpenNebula
- Intégration Terraform → Ansible (provisionner avec Terraform, configurer avec Ansible via inventory dynamique)

### Étapes

#### Inventaire dynamique basé sur Terraform Output

Ajouter dans `outputs.tf` :

```hcl
output "vm_ip" {
  value = opennebula_virtual_machine.vm1.ip
}
```

Export :

```bash
terraform output -json > inventory.json
```

#### Playbook d'installation NGINX

Créer `site.yml` :

```yaml
---
- hosts: all
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
    - name: Enable and start nginx
      service:
        name: nginx
        state: started
```

Lancer :

```bash
ansible-playbook -i inventory.json site.yml
```

### Livrables

- Playbook Ansible complet testé sur VMs provisionnées

## Monitoring avec Prometheus

### Objectifs

- Installer Prometheus
- Collecter les métriques OpenNebula (exporters)

### Étapes

#### Installer Prometheus

```bash
sudo useradd --system --no-create-home prometheus
sudo mkdir -p /etc/prometheus /var/lib/prometheus
sudo apt install prometheus -y
```

#### Ajouter node_exporter

```bash
sudo apt install prometheus-node-exporter -y
```

#### Config Prometheus

`/etc/prometheus/prometheus.yml` :

```yaml
scrape_configs:
  - job_name: node_exporter
    static_configs:
      - targets: ["opennebula-master:9100", "opennebula-compute-1:9100"]
```

Restart :

```bash
sudo systemctl restart prometheus
```

### Livrables

- Dashboard des métriques _node_exporter_

## Observabilité avec Grafana & Loki

### Objectifs

- Installation de Grafana
- Installation de Loki + Promtail
- Dashboard logs + métriques combinés

### Étapes

#### Installation de Grafana

```bash
sudo apt install -y apt-transport-https
sudo apt install grafana -y
sudo systemctl enable --now grafana-server
```

#### Installer Loki

Créer `/etc/loki/local-config.yaml` puis :

```bash
sudo systemctl enable --now loki
```

#### Installer Promtail

```bash
sudo systemctl enable --now promtail
```

#### Configurer Grafana

- Ajouter source Prometheus
- Ajouter source Loki
- Importer les dashboard `1860` et `15141`

### Livrables

- Screenshots du dashboard intégrant logs et métriques

## Kubernetes dans OpenNebula

### Objectifs

- Déployer un petit cluster Kubernetes (1 master, 2 workers) provisionné dans OpenNebula via Terraform
- Automatiser l'installation et la configuration du cluster avec Ansible (`kubeadm`)
- Intégrer la supervision Kubernetes : `kube-state-metrics`, `node-exporter`, `metrics-server`, `Prometheus/Grafana`
- Déployer une application de test (nginx) et démontrer HPA (Horizontal Pod Autoscaler)

### Provisionnement Terraform (exemple)

- **Fichier `terraform/k8s/main.tf` (extrait)**

```hcl
# terraform/k8s/main.tf

provider "opennebula" {
  endpoint = "http://opennebula-master:2633/RPC2"
  username = var.one_user
  password = var.one_pass
}

module "k8s_vms" {
  source = "../modules/vdc-vm"
  count = 3
  name  = "k8s-${count.index+1}"
  cpu   = 2
  memory = 4096
  image = "ubuntu2204-cloud"
  network = "public-net"
}

output "k8s_ips" {
  value = module.k8s_vms.*.ip
}
```

- Réseau : `public-net` configuré dans OpenNebula
- `terraform apply` doit produire 3 adresses IP (master + workers)
- Exporter les IPs :

```bash
terraform output -json k8s_ips > k8s_inventory.json
```

### Inventaire Ansible généré depuis Terraform

Transformer `k8s_inventory.json` en inventory Ansible (script simple ou template). Exemple minimal `inventory.ini` :

```
[k8s-master]
<IP_MASTER>

[k8s-workers]
<IP_WORKER1>
<IP_WORKER2>
```

### Playbooks / rôles Ansible

Proposer 3 rôles : `k8s-prereqs`, `kubeadm-init` (master), `kubeadm-join` (workers).

**Rôle `k8s-prereqs` (tâches principales)**

- Désactiver swap
- Installer containerd
- Installer kubeadm, kubelet, kubectl
- Activer et démarrer services

Extrait `roles/k8s-prereqs/tasks/main.yml` :

```yaml
# roles/k8s-prereqs/tasks/main.yml

- name: Disable swap
  ansible.builtin.command: swapoff -a
  become: true

- name: Ensure containerd installed
  ansible.builtin.package:
    name: containerd
    state: present
  become: true

- name: Configure sysctl for Kubernetes
  ansible.builtin.sysctl:
    name: net.ipv4.ip_forward
    value: '1'
    state: present
    reload: yes
  become: true

- name: Add Kubernetes apt repo
  ansible.builtin.apt_key:
    url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
    state: present
  become: true

- name: Install kubeadm kubelet kubectl
  ansible.builtin.apt:
    name: ["kubelet","kubeadm","kubectl"]
    state: present
    update_cache: yes
  become: true
```

**Rôle `kubeadm-init` (sur master)**

- Exécuter `kubeadm init --pod-network-cidr=10.244.0.0/16 --upload-certs`
- Copier le `kubeconfig` vers `/home/ubuntu/.kube/config`
- Générer token de `join` & certificat (via `kubeadm token create --print-join-command --ttl 24h` ou stash des outputs)

Extrait `roles/kubeadm-init/tasks/main.yml` :

```yaml
# roles/kubeadm-init/tasks/main.yml

- name: Initialize Kubernetes master
  become: true
  command: >-
    kubeadm init --pod-network-cidr=10.244.0.0/16 --upload-certs
  args:
    creates: /etc/kubernetes/admin.conf

- name: Save kubeconfig for ubuntu user
  become: true
  copy:
    src: /etc/kubernetes/admin.conf
    dest: /home/ubuntu/.kube/config
    remote_src: yes
    owner: ubuntu
    mode: '0644'
```

Après l'init, on récupère la commande `kubeadm join` (avec token) pour l'appliquer sur les workers.

**Rôle `kubeadm-join` (sur workers)**

- Exécuter la commande `kubeadm join <MASTER:PORT> --token ... --discovery-token-ca-cert-hash ...`

Extrait `roles/kubeadm-join/tasks/main.yml` :

```yaml
# roles/kubeadm-join/tasks/main.yml

- name: Join worker to cluster
  become: true
  command: "{{ join_command }}"
  args:
    warn: false
```

> Remarque : La playbook contrôleur devra récupérer la commande de `join` depuis le master (module `slurp` ou `shell` pour `kubeadm token create --print-join-command`).

### Installer un CNI : Calico

Sur le master (après `kubeadm init`) :

```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

Vérifier `kubectl get pods -n kube-system` jusqu'à ce que Calico soit `Running`.

### Installer components de monitoring pour Kubernetes

**Metrics Server** (nécessaire pour HPA) :

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

**kube-state-metrics** :

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/kube-state-metrics/master/examples/standard/deployment.yaml
```

**node-exporter** :

- Déployer node-exporter en DaemonSet (exemple officiel Prometheus)

**Prometheus** :

- Option 1 : installer `kube-prometheus-stack` via Helm (si Helm dispo)
- Option 2 : déployer un Prometheus Standalone et ajouter scrapes pour `kube-state-metrics`, `node-exporter`, et `kubelet` endpoints

**Exemple de job scrape (prometheus.yml)**

```yaml
- job_name: 'kubernetes'
  kubernetes_sd_configs:
    - role: pod
  relabel_configs:
    - source_labels: [__meta_kubernetes_pod_label_app]
      action: keep
      regex: node-exporter|kube-state-metrics
```

### Déployer une application de test + HPA

**Déployer un déploiement nginx**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-sample
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-sample
  template:
    metadata:
      labels:
        app: nginx-sample
    spec:
      containers:
      - name: nginx
        image: nginx:stable
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 200m
            memory: 256Mi
```

**Exposer le service**

```bash
kubectl expose deployment/nginx-sample --type=NodePort --port=80
```

**Activer HPA** (exemple basé sur CPU)

```bash
kubectl autoscale deployment nginx-sample --cpu-percent=50 --min=1 --max=5
```

Tester le HPA en générant une charge (par ex. `hey`, `ab`, ou un pod stress) et observer `kubectl get hpa`.

### Supervision & Dashboards

- Importer dashboards Grafana pour Kubernetes (node, kube-state-metrics, kubelet, HPA)
- Créer un dashboard d'état global (nodes, pods, cpu/memory, HPA)
- Configurer alertes (pod restarts hauts, node NotReady, HPA scaling failures)

### Livrables

- Playbooks Ansible et roles (prérequis, init, join)
- Modules Terraform et inventory généré
- Démo : `kubectl get nodes`, `kubectl get pods -A`, dashboard Grafana montrant HPA
