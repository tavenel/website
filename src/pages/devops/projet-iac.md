---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: TP Infrastructure as Code avec Packer, Ansible et Terraform
date: 2025 / 2026
---

## Contexte métier

La société **Novalys Hosting** (entreprise fictive) est un hébergeur d'applications pour des PME locales. Elle souhaite industrialiser la création, le déploiement et la configuration d'une petite infrastructure réplicable sur ses environnements de test et de production afin d'améliorer la reproductibilité, la traçabilité et la sécurité. Le service DevOps doit livrer un blueprint IaC qui permette de :

- Créer des images/VM "_template_" prêtes à l'emploi (Linux et Windows) ;
- Provisionner automatiquement les machines virtuelles nécessaires ;
- Configurer les services d'infrastructure (LB haute disponibilité, DNS/DHCP, annuaire, bases de données, stockage) à l'aide d'Ansible ;
- Utiliser `ansible-vault` pour protéger les secrets ;

Trois scénarios sont proposés (l'apprenant choisit un scénario principal) :

1. **Infrastructure Web haute disponibilité** (par défaut) :

   - Front : `HAProxy` en pair avec `keepalived` (VIP), reverse-proxy + certificat auto-signé;
   - Back : 2 à 3 VMs Web (`Nginx`/`Apache`) derrière `HAProxy` ;
   - BDD : `MariaDB Galera` (cluster 2-3 noeuds) ;
   - Storage : _NFS_ pour partages persistants ;
   - Option avancée : déployer un cluster `Kubernetes` (si connaissances préalables).

2. **Infrastructure IT classique** :

   - DNS + DHCP ;
   - Active Directory (contrôleur `Windows Server`) + un poste client `Windows` (Sysprep) ;
   - Services de base (partage `Samba`, imprimante partagée simulée, etc.).

3. **Reproduction d'un projet de formation antérieur** :

   - L'apprenant reproduit une petite infra déjà réalisée (ex : plateforme CI/CD, monitoring, ou autre) pour montrer la réutilisabilité des modules IaC.

## Objectifs pédagogiques

- Concevoir et automatiser la création d'une image VM "template" (Debian/Alpine/Rocky Linux) et/ou image Windows (Sysprep) via `Packer` ;
- Écrire des configurations Terraform pour provisionner des VMs (sur hyperviseur local type `VirtualBox` / `VMware`, ou cloud provider simulé) ;
- Définir des rôles et playbooks `Ansible` idempotents pour configurer les services demandés ;
- Utiliser `ansible-vault` pour stocker les secrets (mots de passe, clés privées) ;
- Organiser le dépôt Git (répertoires Terraform / Ansible / docs) et documenter le processus ;
- Produire un plan de tests et valider la conformité (checks basic : services actifs, VIP reachable, DB cluster synced, DNS resolution...).

Ce TP est conçu pour être modulable : le but n'est pas d'achever un déploiement industriel en production mais d'apprendre à concevoir une infrastructure reproductible, sécurisée et documentée en IaC.

## Matériel virtuel recommandé (exemples de tailles)

> Les configurations sont volontairement modestes pour un usage pédagogique.

- LB, DNS, DHCP : **256–512 MiB RAM**, 1 vCPU
- VMs Web : **512 MiB–1 GiB RAM**, 1 vCPU (si Kubernetes : **2 GiB et 2 vCPU** par worker)
- Base de données : **512 MiB RAM**, 1 vCPU
- VM NFS : **384 MiB RAM**, 1 vCPU
- VM Windows (client/serveur) : **min 2 GiB RAM**, 1–2 vCPU

## Livrables

- Livrables attendus :

  1. Dépôt Git (ou archive) structuré contenant : `terraform/`, `ansible/`, `packer/`, `docs/` et `vault/` (fichiers chiffrés ou instructions) ;
  2. Fichier `README.md` décrivant l'architecture, prérequis, commandes pour reproduire ;
  3. Inventaire Ansible, roles, playbooks principaux ;
  4. Plan de tests et captures (commande `curl`, `ss`, `systemctl status`, `mysql -e 'SHOW STATUS'`, etc.) ;
  5. Rapport court (2–4 pages) : architecture, choix techniques, problèmes rencontrés, correctifs.

## Structure du dépôt (suggestion)

```
TP-iac-novalys/
├─ terraform/
│  ├─ main.tf
│  ├─ variables.tf
│  ├─ outputs.tf
│  └─ modules/
│     ├─ vm/
│     └─ network/
├─ packer/
│  └─ debian-template.json
├─ ansible/
│  ├─ inventories/
│  │  ├─ dev/
│  │  └─ prod/
│  ├─ roles/
│  │  ├─ common/
│  │  ├─ haproxy_keepalived/
│  │  ├─ web/
│  │  ├─ mariadb_galera/
│  │  ├─ nfs/
│  │  └─ windows_ad/  # documentation + examples
│  ├─ playbooks/
│  │  ├─ site.yml
│  │  ├─ web.yml
│  │  ├─ db.yml
│  │  └─ infra.yml
│  ├─ group_vars/
│  └─ host_vars/
├─ docs/
└─ README.md
```

## Étapes détaillées

### Préparation

- Initialiser un dépôt ;
- Installer les versions requises de Terraform / Ansible / Packer ;
- Vérifier accès à l'hyperviseur (VirtualBox / cloud).

### Création de la VM "template" (Packer)

- Rédiger un template Packer pour générer une image Debian minimalisée (ou l'ISO cloud-friendly) :

  - Préinstall : `openssh-server`, `python3` (pour Ansible), `cloud-init` ou configuration pour compte `ansible` ;
  - Ajout d'un utilisateur `ansible` avec clé publique (provisioner) ;
  - Nettoyage et shutdown pour générer l'image.

### Provisionnement des VM (Terraform)

- Écrire un module Terraform `vm` réutilisable qui prend en entrée : image/template, ressources (RAM, CPUs), réseau, clés SSH, nom ;
- Définir la topologie selon le scénario choisi (ex : 1xLB pair, 2xweb, 3xdb, 1xstorage) ;
- Outputs importants : adresses IP des machines, nom hôte, chemin clé privée (si générée) ;
- Exemples de providers : `libvirt`, `virtualbox`, `vsphere`, `azurerm`, `aws`. Pour le TP local, `libvirt` ou `virtualbox` recommandés.

### Configuration (Ansible)

- Créer le rôle `common` :

  - Création des utilisateurs, groupes ;
  - Distribution des clefs publiques SSH ;
  - Hardening léger (désactiver SSH root, configures `sshd_config`) ;
- Rôle `haproxy_keepalived` :

  - Installer HAProxy, keepalived ;
  - Générer configuration HAProxy pour backend web ;
  - Configurer keepalived pour VIP (tests de bascule) ;
- Rôle `web` :

  - Installer Nginx/Apache, déployer une page sample avec l'hostname/IP ;
  - Configurations idempotentes et tests (ex: `systemctl is-active nginx`) ;
- Rôle `mariadb_galera` :

  - Installer MariaDB, configurer cluster Galera (`wsrep`) ;
  - Scripts d'initialisation pour bootstrap du cluster ;
  - Vérifier état du cluster (`mysql -e 'SHOW STATUS LIKE "wsrep_%"'`) ;
- Rôle `nfs` :

  - Installer `nfs-kernel-server`, exporter un répertoire ;
  - Configurer client NFS sur les web pour monter un dossier (pour tests) ;
- Rôles pour Windows/AD : fournir playbooks d'exemple et documentation (Ansible Windows modules ou PowerShell DSC).

**Sécurité des secrets :**

- Utiliser `ansible-vault` pour chiffrer mots de passe DB, secrets keepalived, clefs privées ;
- Documenter le workflow (création d'un vault password file sécurisé, utilisation dans CI si nécessaire).

### Tests de validation

- Vérifier que le VIP répond (`ping`/`curl`), que HAProxy renvoie les pages web ;
- Vérifier réplication MariaDB Galera (`wsrep_cluster_size` attendu) ;
- Vérifier montages NFS présents et permissions ;
- Vérifier résolution DNS (si déployé), bail DHCP sur client test ;
- Produire un petit script `check.sh` qui exécute les contrôles et sort un code d'état.

## Exemples de commandes (extraits)

### Terraform

```bash
terraform init
terraform apply -var-file=env/dev.tfvars
# récupère les outputs :
terraform output -json > ../ansible/inventories/dev/terraform_outputs.json
```

### Ansible

```bash
# chiffrer un secret
ansible-vault create group_vars/all/vault.yml
# lancer playbook site
ANSIBLE_VAULT_PASSWORD_FILE=~/.vault_pass ansible-playbook -i ansible/inventories/dev site.yml --ask-become-pass
```

## Bonus

- Intégrer un pipeline GitLab CI pour : packer -> terraform plan/apply -> ansible-playbook ;
- Ajouter monitoring : exporter métriques (`node_exporter`), Prometheus & Grafana pour collecter disponibilité HAProxy et MariaDB ;
- Déployer le cluster Kubernetes (`kubeadm` / `k3s`) en remplacement des VMs Web, avec provisionnement via Terraform/Ansible.

## Conseils pratiques & pièges fréquents

- Toujours vérifier l'idempotence (relancer un playbook deux fois doit donner le même état) ;
- Gérer correctement les dépendances (ex : MariaDB doit être bien configurée avant de joindre Galera) ;
- Documenter la façon de récupérer les logs et outputs Terraform/Ansible ;
- Ne pas laisser de mots de passe en clair dans le dépôt ;
- Prévoir une procédure de rollback (ex : détruire les VMs via Terraform).
