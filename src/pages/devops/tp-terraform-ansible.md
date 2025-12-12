---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: TP découverte d'Ansible et de Terraform
date: 2025 / 2026
---

## Présentation du TP

### Objectifs

Ce double TP a pour objectif de manipuler la mise en place d'une mini‑infrastructure virtualisée via Terraform, puis l'automatisation de sa configuration via Ansible.

Vous apprendrez à :

- Déployer des VMs clonées depuis un template avec Terraform.
- Paramétrer CPU/RAM/disques et réseau (IP fixe, 2 interfaces).
- Configurer ces VMs automatiquement via Ansible (utilisateurs, SSH, installation de rôles applicatifs).
- Détruire l'infrastructure provisionnée.

### Prérequis

- Terraform installé.
- Ansible installé.
- Accès à un environnement de virtualisation (VMware Workstation, VirtualBox, cluster VMware, Proxmox,).
- Template Debian 12 minimal OU capacité à en générer un via Terraform.
- Accès SSH fonctionnel vers les VMs une fois créées.

## Terraform

### Préparation du template de VM

Créer une VM minimaliste :

- Installation d'OpenSSH Server.
- Ajout d'un utilisateur terraform/ansible avec clé SSH.
- Mise à jour système.
- Clean des données persistentes (machine-id, logs...).
- Conversion en template.

Ce template servira de base pour les clonages.

:::tip
On pourra également utiliser un template tout fait, comme par exemple ubuntu : `bionic-server-cloudimg-amd64-vagrant`.
:::

### Arborescence du projet Terraform

Créer une arborescence simple :

```
terraform/
  main.tf
  variables.tf
  outputs.tf
```

### Configuration Terraform

Définir :

- Le provider selon l'environnement (ex : `vsphere`, `virtualbox`, `vmware` local…).
- Le template _Debian_ comme source pour un clonage.
- Deux ressources `vm` nommées `web01` et `db01`.
- Paramètres :
  - 1 vCPU
  - 1 Go RAM
  - Disque léger (10 Go recommandé)
  - Deux interfaces réseau :
    - NIC1 : réseau interne
    - NIC2 : NAT ou réseau d'accès
  - IP fixe via `cloud-init` ou configuration Terraform/provider (selon architecture)

### Variables recommandées

- `vm_count`
- `vm_cpu`
- `vm_ram`
- `vm_disk`
- `network_1`
- `network_2`
- `ip_base`

### Outputs

Exporter :

- Les IPs des VMs
- Les noms

### Déploiement

Lancer :

```
terraform init
terraform plan -out plan.out
terraform apply plan.out
```

Attendre que les VMs soient accessibles en SSH.

### Ressources

Exemple de code Terraform :

```hcl
# main.tf
terraform {
  required_providers {
    virtualbox = {
      source  = "terra-farm/virtualbox"
      version = "0.2.2-alpha.1"
    }
  }
}

provider "virtualbox" {
  # Configuration options for the VirtualBox provider (if needed)
}

resource "virtualbox_vm" "node" {
  count = var.num_instances

  name      = "${var.instance_name_prefix}-${count.index + 1}"
  image     = var.image_location
  cpus      = var.vm_cpus
  memory    = "2048 MiB"
    
  network_adapter {
    type           = "hostonly"
    host_interface = "vboxnet1"
  }
  

  provisioner "remote-exec" {
    inline = [
      "sudo mkdir -p ~/testfolder",
      "sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config",
      "sudo systemctl restart sshd",
    ]

    connection {
      host        = self.network_adapter[0].ipv4_address
      user        = var.user
      private_key = file(var.ssh_key)
      type        = "ssh"
      agent       = false
    }
  }

  provisioner "local-exec" {
    command = <<-EOT
      sshpass -p "${var.user_password}" ssh-copy-id -o "StrictHostKeyChecking=no" "${var.user}@${self.network_adapter[0].ipv4_address}"
    EOT

    connection {
      host        = self.network_adapter[0].ipv4_address
      user        = var.user
      private_key = file(var.ssh_key)
      type        = "ssh"
      agent       = false
    }
  }
}

# Generate Ansible inventory file content
locals {
  ansible_inventory_content = <<-EOF
    ${join("\n", [for i, vm in virtualbox_vm.node : "${vm.name} ansible_ssh_host=${vm.network_adapter[0].ipv4_address} ip=${vm.network_adapter[0].ipv4_address} ansible_ssh_user=${user} ansible_ssh_private_key_file='${var.ssh_key}' "])}
  EOF
}

# Create Ansible inventory file
resource "local_file" "inventory_file" {
  filename = "/tmp/inventory.ini"
  content  = local.ansible_inventory_content
}

# Run Ansible playbook
resource "null_resource" "run_ansible" {
  triggers = {
    # Map the server names to their corresponding IDs
    for i, vm in virtualbox_vm.node : i => vm.id
  }

  provisioner "local-exec" {
    command     = "ansible-playbook -i inventory.ini -u ${var.user} -e 'variable=value' ${var.playbook} -b -vvv --private-key= ${var.ssh_key}"
    working_dir = path.module

    connection {
      host        = element([for vm in virtualbox_vm.node : vm.network_adapter[0].ipv4_address], 0) # Access the first IP address
      user        = var.user
      private_key = file(var.ssh_key)
      type        = "ssh"
      agent       = false
    }
  }

  depends_on = [local_file.inventory_file]
  
  
}

output "IPAddresses" {
  value = [for vm in virtualbox_vm.node : vm.network_adapter[0].ipv4_address]
}
```

Exemple de variables :

```hcl
# variables.tf

variable "server_names" {
  type    = list(string)
  default = ["vm1","vm2"]
}

variable "public_key_location" {
  description = "public key location"
  default = "~/.ssh/id_rsa.pub"
}

variable "ssh_key_private" {
  description = "private key location"
  default = "~/.ssh/id_rsa"
}

variable "image_location" {
  description = "virtualbox image location - can be downloaded or remote location"
  default = "/tmp/bionic-server-cloudimg-amd64.box"
}

variable "ssh_key" {
  description = "default ssh key location - not secure"
  default = "/tmp/insecure_private_key"
}

variable "user" {
  description = "user to use the vm"
  default = "test"
}

variable "user_password" {
  description = "user password to use the vm"
  default = "test"
}

# variable "network_adapter_type" {
#   description = "network adapter type, others are NAT, NAT network, Bridged, internal network etc"
#   default = "bridged"
# }

variable "hostonly_ipv4_subnet" {
  description = "The private IPv4 subnet of the VirtualBox hostonly network (default is 192.168.56.0/16)"
  type        = string
  default     = "192.168.59.0/16"

  validation {
    condition     = can(cidrnetmask(var.hostonly_ipv4_subnet)) && split("/", var.hostonly_ipv4_subnet)[1] == "16"
    error_message = "The specified hostonly IPv4 CIDR is invalid."
  }
}

variable "internet_gateway" {
  description = "internet network gateway"
  default = "nat"
}

variable "instance_name_prefix" {
  description = "Prefix for instance names"
  type        = string
  default     = "vm-from-terraform"
}

variable "vm_cpus" {
  description = "Number of CPUs for VM instances"
  type        = number
  default     = 2
}

variable "num_instances" {
  description = "Number of VM instances to create"
  type        = number
  default     = 3
}

variable "override_disk_size" {
  description = "Whether to override disk size"
  type        = bool
  default     = false
}

variable "disk_size" {
  description = "Disk size for VM instances"
  type        = string
  default     = "20GB"
}

variable "local_path_provisioner_enabled" {
  description = "Enable local path provisioner"
  type        = bool
  default     = false
}

variable "local_path_provisioner_claim_root" {
  description = "Local path provisioner claim root directory"
  type        = string
  default     = "/opt/local-path-provisioner/"
}

variable "libvirt_nested" {
  description = "Enable libvirt nested virtualization"
  type        = bool
  default     = false
}

variable "ansible_verbosity" {
  description = "Ansible verbosity level"
  type        = string
  default     = false
}

variable "ansible_tags" {
  description = "Ansible tags"
  type        = string
  default     = ""
}

variable "playbook" {
  description = "Name of the Ansible playbook to execute"
  type        = string
  default     = "cluster.yml"
}
```

## Ansible

### Arborescence recommandée

```
ansible/
  inventory.ini
  site.yml
  roles/
    common/
      tasks/main.yml
    web/
      tasks/main.yml
    db/
      tasks/main.yml
```

### Inventaire

Construire un fichier `inventory.ini` basé sur les IPs Terraform :

```
[web]
web01 ansible_host=IP_WEB ansible_user=terraform

[db]
db01 ansible_host=IP_DB ansible_user=terraform
```

### Rôle "common" : utilisateurs et SSH

Tâches :

- Créer un utilisateur applicatif (`appuser`).
- Déployer une clé SSH dans `~appuser/.ssh/authorized_keys`.
- Configurer `/etc/ssh/sshd_config` (désactiver root login, forcer clés SSH...).
- Redémarrer SSH.

Exemple :

```yaml
- name: Create appuser
  user:
    name: appuser
    shell: /bin/bash
    create_home: yes

- name: Create .ssh directory for appuser
  file:
    path: /home/appuser/.ssh
    state: directory
    mode: '0700'
    owner: appuser
    group: appuser

- name: Deploy authorized SSH key
  copy:
    src: authorized_keys
    dest: /home/appuser/.ssh/authorized_keys
    owner: appuser
    group: appuser
    mode: '0600'

- name: Disable SSH root login
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?PermitRootLogin'
    line: 'PermitRootLogin no'

- name: Enforce public key authentication
  lineinfile:
    path: /etc/ssh/sshd_config
    regexp: '^#?PasswordAuthentication'
    line: 'PasswordAuthentication no'

- name: Restart SSH service
  service:
    name: ssh
    state: restarted
```

### Rôle "web" : installation Apache2

Tâches :

- Installer `apache2`.
- Activer et démarrer le service.
- Déployer une page HTML simple.

Exemple :

```yaml
- name: Install Apache
  apt:
    name: apache2
    state: present
    update_cache: yes

- name: Enable and start Apache
  service:
    name: apache2
    enabled: yes
    state: started

- name: Deploy index.html
  copy:
    dest: /var/www/html/index.html
    content: |
      <html>
      <h1>Serveur Web Apache déployé via Ansible</h1>
      <p>Host: {{ inventory_hostname }}</p>
      </html>
```

### Rôle "db" : installation MariaDB

Tâches :

- Installer `mariadb-server`.
- Sécuriser l'installation via `mysql_secure_installation` automatisé.
- Créer une base de test.

Exemple :

```yaml
---
- name: Install MariaDB server
  apt:
    name: mariadb-server
    state: present
    update_cache: yes

- name: Enable and start MariaDB
  service:
    name: mariadb
    enabled: yes
    state: started

# Exemple simple de sécurisation automatisée
- name: Remove anonymous users
  mysql_user:
    name: ''
    host_all: yes
    state: absent

- name: Remove test database
  mysql_db:
    name: test
    state: absent

- name: Create example database
  mysql_db:
    name: appdb
    state: present

- name: Create an application DB user
  mysql_user:
    name: appuser
    password: "password123"
    priv: "appdb.*:ALL"
    state: present
```

### Déploiement du playbook

Exemple de playbook :

```yaml
- name: Configuration commune sur toutes les VMs
  hosts: all
  become: yes
  roles:
    - common

- name: Configuration du serveur web
  hosts: web
  become: yes
  roles:
    - web

- name: Configuration du serveur MariaDB
  hosts: db
  become: yes
  roles:
    - db
```

Lancer :

```
ansible-playbook -i inventory.ini site.yml
```

Vérifier :

- `curl http://IP_WEB` -> page Apache.
- Accès MariaDB -> `mysql -u root`.

## Destruction de l'infrastructure

Pour terminer le TP, détruire l'infrastructure via Terraform :

```
terraform plan -destroy -out destroy.out
terraform apply destroy.out
```

Vérifier qu'aucune VM n'est encore présente dans l'environnement de virtualisation.

## Livrables attendus

- Code Terraform complet.
- Code Ansible complet.
- Une courte note expliquant :
  - Comment sont gérées les variables.
  - Comment l'inventaire Ansible est alimenté.
  - Comment est effectuée la configuration SSH.
