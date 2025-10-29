---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: 🧩 Packer
layout: '@layouts/CoursePartLayout.astro'
---

## Introduction

Dans un environnement DevOps, l'objectif est de **standardiser et automatiser** le déploiement des environnements.

Problèmes fréquents :

- Environnements non homogènes entre dev/test/prod.
- Longs temps de déploiement.
- Risques d'erreurs manuelles.

---

**HashiCorp Packer** est un outil d'**automatisation de la création d'images** identiques pour différents environnements (VM, conteneurs, Cloud) :

- **Images _Docker_**
- **Machines virtuelles** (_VirtualBox_, _VMware_)
- **Images Cloud** (_AWS AMI_, _Azure_, _GCP_)
- **Templates _Vagrant_**
- …

---

## Objectifs de Packer

- Créer des images préconfigurées à partir d'un modèle.
- Garantir la reproductibilité entre environnements.
- Intégrer la création d'images dans des pipelines CI/CD.
- Simplifier le déploiement avec des outils comme Terraform.

---

## Intégration DevOps

- _Packer_ n'intègre pas d'outil de déploiement : se combine avec Terraform/Ansible.
- Workflow typique : _Packer_ + _Terraform_

1. **Packer** crée une image préconfigurée (ex : AMI Ubuntu avec Nginx)
2. **Terraform** déploie cette image dans un environnement.

```hcl
# Déploiement de l'AMI via Terraform :

resource "aws_instance" "web" {
  ami           = "ami-0abcd1234"
  instance_type = "t2.micro"
}
```

---

## Architecture

Un template Packer se compose de **trois grandes sections** qui s'exécutent l'une après l'autre :

1. **Builders** :
  - Définit **le type d'image à construire** : _Docker_, _VirtualBox_, _AWS AMI_, _Azure Image_, …
  - Lance un **environnement vierge** pour y appliquer une configuration.
2. **Provisioners** :
  - Définit **comment configurer l'image** : installation de paquets (`apt`, `yum`), copie de fichiers (`file`), scripts `shell`, `ansible`, `chef`, `puppet`, …
  - **Installe** et **configure** le système.
  ```hcl
  provisioner "ansible" {
    playbook_file = "site.yml"
  }
  ```
3. **Post-Processors** :
  - Actions à exécuter **après la création de l'image** :
  - Taguer l'image Docker et/ou la pousser vers un registre
  - Générer un manifeste JSON
  - Créer une box Vagrant
  - …

---

## Exemple

Exemple de template minimal : image Docker avec Nginx

```hcl
# ubuntu-nginx.pkr.hcl

packer {
  required_plugins {
    docker = {
      version = ">= 1.0.0"
      source  = "github.com/hashicorp/docker"
    }
  }
}

source "docker" "ubuntu" {
  image  = "ubuntu:22.04"
  commit = true
}

build {
  name    = "nginx-docker"
  sources = ["source.docker.ubuntu"]

  provisioner "shell" {
    inline = [
      "apt-get update",
      "apt-get install -y nginx",
      "echo '<h1>Hello from Packer!</h1>' > /var/www/html/index.html"
    ]
  }

  post-processor "docker-tag" {
    repository = "demo/nginx"
    tag        = "v1.0"
  }
}
```

```bash
packer init .
packer build .
```

Packer télécharge les dépendances, construit l'image, puis applique les provisioners.

---

## Bonnes pratiques

- Utiliser le **format HCL2** plus lisible (au lieu de JSON).
- **Versionner** les templates Packer dans Git.
- Nommer les images avec des **versions** (`v1.0`, `v1.1`…).
- Automatiser le build via un **pipeline CI/CD**.
- **Centraliser les variables** dans un fichier `.pkrvars.hcl`.

Exemple :

```hcl
variable "nginx_version" {
  type    = string
  default = "1.24"
}
```

---

## 🔗 Références

- Documentation officielle : <https://developer.hashicorp.com/packer> et GitHub : <https://github.com/hashicorp/packer>
- Plugin Docker : [https://developer.hashicorp.com/packer/plugins/builders/docker](https://developer.hashicorp.com/packer/plugins/builders/docker)
- <https://blog.stephane-robert.info/docs/virtualiser/outils/packer/>

---

