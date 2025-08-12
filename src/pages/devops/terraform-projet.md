---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: 🎯 Projet Déploiement d'une infrastructure multi-environnement sur Azure avec Terraform
date: 2025 / 2026
---

## 📋 Présentation du projet

### Contexte professionnel

Vous êtes une équipe DevOps dans l'entreprise **CloudTech Solutions**, une startup en pleine croissance qui développe une application web de gestion de projets. L'entreprise souhaite migrer son infrastructure vers Azure et automatiser complètement le déploiement de ses environnements.

Votre mission : concevoir et déployer une infrastructure cloud moderne, scalable et sécurisée en utilisant Terraform comme outil d'Infrastructure as Code (IaC).

### 🎯 Objectifs pédagogiques

- 🤖 Automatisation de la création, mise à jour et destruction de ressources cloud
- 👥 Mise en place d'un workflow d'équipe avec Git et outils de versioning
- 🧩 Maîtrise des concepts Terraform (State, Modules, Variables)
- ☁️ Intégration avec les services Azure
- ⚡ Optimisation avec dynamic blocks et fonctions ternaires
- 🔐 Sécurisation avec Vault et Sentinel
- 🔄 Intégration CI/CD avec Jenkins/GitLab

## 🏗️ Infrastructure à déployer

L'infrastructure comprendra **3 environnements** (dev, staging, prod) avec les composants suivants :

| Composant | Description | Quantité |
|-----------|-------------|----------|
| **Resource Group** | Conteneur logique des ressources | 1 par environnement |
| **Virtual Network** | Réseau virtuel Azure | 1 avec 2 subnets
| **Virtual Machines** | Serveurs Linux  | 3 (2 web + 1 db) |
| **Load Balancer** | Répartiteur de charge | 1 |
| **Public IP** | Adresse IP publique | 1 |
| **Network Security Group** | Pare-feu réseau (port SSH, HTTP) | 2 (web + db) |
| **Storage Account** | Stockage pour diagnostics | 1 |

## 📋 Mise en place de l'environnement

### Prérequis & Setup

**Comptes nécessaires :**

- [x] **Azure** : Inscription gratuite ([https://azure.microsoft.com](https://azure.microsoft.com))
- [x] **HashiCorp** : Compte sur [Terraform Cloud](https://app.terraform.io)
- [x] **Git** : Repository sur GitHub/GitLab

**Configuration locale :**

:::exo
1. Installer `terraform` et la ligne de commande azure : `az`
2. Configurer un Workspace Terraform Cloud et le lier au repository
3. Créer un Service Principal Azure avec les permissions appropriées
4. Initialiser terraform :
    ```bash
    terraform init
    ```
:::

### ⚠️ Coûts Azure

- Utilisez les tailles de VM les plus petites (Standard_B1s, Standard_B2s)
- Arrêtez les ressources après les tests
- Surveillez votre crédit Azure gratuit

## 🏗️ Architecture et conception

### Structure du projet Terraform

```
terraform-project/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── prod/
├── modules/
│   ├── network/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── compute/
│   └── security/
├── scripts/
└── docs/
```

### Diagramme d'Architecture Technique (DAT)

:::exo
1. Réfléchir à un [workflow Git](/git/cours#workflows-git-travailler-en-quipe) cohérent par rapport aux environnements à déployer.
2. Créez un diagramme représentant :
  - Les dépendances entre composants Azure
  - Les correspondances entre ressources Azure et ressources Terraform
  - Les flux de données et de communication
:::

### 💻 Développement Terraform

:::exo
1. Développer le projet Terraform permettant de déployer l'infrastructure sur Azure.
2. Créez un module `network` permettant de :
  - Créer un _Virtual Network_
  - Créer un ou plusieurs _Subnets_ dynamiquement
  - Retourner les IDs des sous-réseaux
3. Optimiser le code Terraform :
  - Blocs dynamiques (ex : règles NSG)
  - Fonctions ternaires et count
  -  Variables + fichier `terraform.tfvars`
4. Utiliser le module `network` pour déployer deux VMs dans deux subnets différents.
:::

### 🔄 CI/CD et automatisation

:::exo
1. Créer un pipeline d'intégration continue (Gitlab CI, Github, Jenkins) cohérent avec les environnements déployés / à déployer.
2. Ajouter des outils dédiés à Terraform dans le pipeline, par exemple : linter _Terragrunt_, _Trivy_ pour la sécurité, …
:::

### 🔐 Sécurisation avancée

:::exo
1. Intégrer Vault pour la gestion des secrets : aucun secret ne doit être stocké en clair.
2. Si ce n'est pas déjà fait, intégrer le _state_ de Terraform dans un backend sécurisé
3. Ajouter des politiques _Sentinel_ (_Terraform Cloud_), par exemple pour interdire des VMs trop puissantes en environnement _dev_ ou pour bloquer certaines régions.
:::

### 🏆 Bonus

- **Monitoring** : Intégration Azure Monitor, alertes
- **Multi-cloud** : Déploiement hybride Azure/AWS/GCP/…
- **Innovation** : Utilisation d'outils avancés (Atlantis, Spacelift)
- **Monitoring** : Dashboard Grafana/Prometheus sur une VM
- **Post-provisioning** : Interconnexion avec Ansible

## 📊 Validation et tests

### Tests à effectuer

1. **Déploiement complet** : `terraform plan` puis `terraform apply`
2. **Visualisation Azure** : Vérification via Azure Portal
3. **Azure Network Watcher** : Analyse topologique du réseau
4. **Tests de connectivité** : SSH vers les VMs, test du Load Balancer
5. **Destruction** : `terraform destroy` pour valider la suppression

### Vérification des ressources via les CLI

```bash
# Vérification de l'état Terraform
terraform state list
terraform state show azurerm_virtual_machine.web[0]

# Validation Azure CLI
az vm list --resource-group myapp-dev-rg --output table
az network lb list --resource-group myapp-dev-rg --output table
```

## 📋 Livrable final - 📁 Repository Git

Structure attendue :

```
terraform-azure-project/
├── README.md                # Documentation complète
├── .gitignore               # Exclusions (*.tfstate, *.tfvars)
├── .gitlab-ci.yml           # Pipeline CI/CD
├── environments/            # Configurations par environnement
├── modules/                 # Modules Terraform réutilisables
├── scripts/                 # Scripts d'automatisation
├── docs/                    # Documentation technique
│   ├── architecture.md      # DAT et explications
│   ├── deployment.md        # Procédures de déploiement
│   └── security.md          # Mesures de sécurité
└── tests/                   # Tests automatisés
```

## 🔗 Ressources utiles

### Documentation officielle

- [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/)
- [Terraform Best Practices](https://www.terraform-best-practices.com/)

### Exemples et templates

- [Terraform Azure Examples](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples)
- [Azure Quickstart Templates](https://github.com/Azure/azure-quickstart-templates)

### Outils complémentaires

- [Trivy](https://trivy.dev/latest/) - Analyse de sécurité
- [Terragrunt](https://terragrunt.gruntwork.io/) - Wrapper Terraform
- [Atlantis](https://www.runatlantis.io/) - Terraform Pull Request Automation

### Tests et validation

- Tests Terraform sur Azure :
  - [Compliance Testing](https://learn.microsoft.com/fr-fr/azure/developer/terraform/best-practices-compliance-testing)
  - [e2e Testing](https://learn.microsoft.com/fr-fr/azure/developer/terraform/best-practices-end-to-end-testing)
  - [Integration Testing](https://learn.microsoft.com/fr-fr/azure/developer/terraform/best-practices-integration-testing)
- [Terratest](https://terratest.gruntwork.io/) - Framework de tests

