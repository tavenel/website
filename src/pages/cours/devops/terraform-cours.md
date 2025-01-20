---
marp: true
paginate: true
#footer: _© 2024 Tom Avenel under 󰵫  BY-SA 4.0_
title: Terraform
keywords:
- devops
- iac
---

# Terraform

_Tom Avenel_

<https://www.avenel.pro/>

---

<!-- _class: intro -->

# Objectifs
 
- Gérer des ressources dans un cluster Cloud avec une notion d'état grâce à Terraform.

---

# Présentation de Terraform

- Outil IaC de déploiement et mise à jour d'infrastructures hétérogènes
- Déclaratif
- Statefull (vs Ansible : stateless)
- Majoritairement pour le Cloud (multi-provider)
  - fournisseur CRUD de _ressources_ (modifiables) et _data source_ (immuable) par API <https://registry.terraform.io>
- Séparation plan vs application : `refresh`, `plan`, `apply`, `destroy`, …
- Modules partagés pour les infrastructures courantes

---

# Fonctionnement

1. Fichiers IaC pour lancer Terraform : `*.tf`
1. Compare l'état actuel (`terraform.tfstate` ou remote state) au plan => changements / créations
1. Utilise les API des providers pour effectuer les changements
1. Stocke l'état des changements

---

# Étapes

1. `terraform init` => Initialise Terraform et installe les plugins
1. `terraform plan` => Plannifie l'exécution des changements (`terraform graph`)
1. `terraform apply` => Exécute le plan
1. `terraform destroy` => Détruit les ressources

---

# Fichiers

- `main.tf` : configuration de l'infrastructure
- `variables.tf` : déclaration des variables
- `terraform.tfvars` : valeurs des variables
- `modules` : groupes logiques de ressources dans fichiers `.tf` dédiés (~= _role_ Ansible)

---

# Exemple de fichier Terraform

```tf
provider "kubernetes" {
    version = "~> 1.10"
}

resource "aws_instance" "ma_ressource_web" {
    ami = "mon_id"
    instance_type = "t2.micro"
    subnet_id = var.environnement == "production" ? aws_subnet.prod_subnet.id : aws_subnet.dev_subnet.id
}

# data => données extraites de l'infrastructure
data "aws_ami" "ubuntu" {
    most_recent = true
}
```

---

# Variables

---

## Variable string

```tf
# accès par `var.mon_ip`
variable "mon_ip" {
    type = string
    default = "192.168.1.1"
}

output "affiche_mon_ip" {
    value = var.mon_ip
}
```

---

## Variable list

```tf
# pour les types multiples : `count` et `for-each`
variable "mes_ips" {
    default = ["127.0.0.1 localhost","192.168.1.1 mon_ip"]
}

resource "null_resource" "mes_hosts" {
    count = "${length(var.mes_ips)}"
    triggers = { foo = element(var.mes_ips, count.index } # déclenché si mes_ips change
    provisioner "local_exec" {
        command = "echo '${element(var.mes_ips, count.index)}' >> hosts.txt"
    }
```

---

## Variable map (objet)

```tf
variable "mes_distributions" {
    type = "map"
    default = {
        clef1 = "ubuntu"
        clef2 = "rhel"
        clef3 = "alpine"
    }
}

resource "aws_instance" "mes_serveurs" {
    for_each = var.mes_distributions
    triggers = { foo = each.value } # déclenché si mes_distributions change
    tags = { Name = each.key }
}
```

---

# Secrets

1. Marquer la variable "sensible" (pas d'historique)
1. Utiliser `Vault` pour sécuriser le fichier de variables
1. Déplacer l'état `terraform.tfstate` vers un état sécurisé par un Cloud provider

---

## Variable sensible

```tf
# variables.tf
variable "mon_password" {
    type = string
    sensitive = true
```

```tf
# terraform.tfvars
mon_password = "P@ssw0rd"
```

---

<!-- class: liens -->
# Liens

- [Documentation Terraform](https://developer.hashicorp.com/terraform?product_intent=terraform)
- <https://lafor.ge/blue-green/>
- <https://blog.stephane-robert.info/post/ansible-vs-terraform/>
- Livre : "_L'infrastructure as code avec Terraform_ (Julien Wittouck, éditions eni)"
- Voir aussi le cours DevOps sur le [site web][site-perso]

---

<!-- class: legal -->

# Legal 

- Terraform is a trademark and brand of HashiCorp, Inc.
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
