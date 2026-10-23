---
title: 🧩 TP Packer - Création d'une image Azure et déploiement d'une application web complète
date: 2025 / 2026
type: projet
sidebar:
  order: 201
description: 🧩 TP Packer - Création d'une image Azure et déploiement d'une application web complète
---
## Présentation du TP

### Objectifs pédagogiques

- Comprendre les concepts fondamentaux de _Packer_ (builders, provisioners, variables, artefacts).
- Construire un template Packer complet pour Azure.
- Déboguer un build Packer et valider une image.
- Déployer une instance Azure basée sur l'image générée.
- Tester le fonctionnement d'une application web.
- Améliorer et optimiser un template Packer.

### Pré-requis

- Connaissances de base sur Azure (Ressource Group, VM, réseau, gestion identité).
- Aisance avec Linux (Ubuntu ou Debian).
- Compte Azure via Azure for Students.
- Postes de travail avec Packer et Azure CLI installés.

### Architecture cible

Le TP vise à générer une image Azure contenant :

- Nginx **ou** Apache
- PHP
- Une application web simple (ex. : mini site PHP affichant `phpinfo()` + une page index personnalisée)

Un déploiement final consistera à lancer une VM Azure basée sur l'image Packer.

## Plan du TP

### Découverte, préparation et création du template Packer

#### Configuration Azure + authentification

- Vérification de l'authentification Azure CLI :

  ```
  az login
  az account show
  ```

- Récupération du `subscription_id`, `tenant_id`, `client_id`, `client_secret`.
- Création d'une _App Registration_ si nécessaire.

#### Structure d'un template Packer Azure

Création d'un fichier : `azure-template.json` ou HCL (`azure.pkr.hcl`).

Contenu minimal attendu :

- variables
- source `azure-arm` (ou `azure-arm builder`)
- build block
- provisioner shell : installation OS updates

Produire un premier template valide.

#### Validation du template

Commandes :

```
packer fmt .
packer validate azure.pkr.hcl
```

Analyse des erreurs courantes :

- credentials invalides
- réseau non trouvé
- type de machine incorrect
- syntaxe HCL

#### Premier build

Lancement :

```
packer build azure.pkr.hcl
```

Observation du lifecycle :

- création du resource group temporaire
- création VM temporaire
- provisionnement
- capture image
- destruction ressources intermédiaires

### Provisioning avancé et application web

#### Provisioner shell : installation serveur web + PHP

Exemple (Nginx) :

```
sudo apt update
sudo apt install -y nginx php-fpm php-cli
```

#### Deployment de l'application web

Copie via `file` provisioner, puis configuration :

```
/var/www/html/index.php
```

Objectif : **obtenir une image Azure totalement provisionnée**.

### Déploiement Azure, tests et optimisation

#### Vérification du build Azure

Depuis Azure CLI :

```
az image list -g <RG>
az image show -n <image-name> -g <RG>
```

#### Déploiement d'une VM basée sur l'image

Utilisation de :

```
az vm create \
  --resource-group <RG> \
  --name webvm \
  --image <image-name> \
  --admin-username azureuser \
  --ssh-key-values ~/.ssh/id_rsa.pub \
  --public-ip-sku Standard
```

Test d'accessibilité :

- IP publique récupérée via Azure CLI
- ouverture du port 80
- affichage du site web

### Tests fonctionnels

- vérifier que Nginx/Apache fonctionne au reboot
- vérifier que PHP est actif
- vérifier que les fichiers copiés se trouvent au bon emplacement
- documenter les logs système en cas de défaut

### Optimisation du template

Pistes :

- utilisation de variables
- scripts d'installation idempotents
- réduction du temps de build : nombre de packages, clean apt
- ajout d'un tag versionné sur l'image
- externalisation des credentials via environnement

Objectif final : proposition d'une **v2 du template plus propre et plus modulaire**.

## Livrables

- Template Packer complet
  - Fichier HCL (`*.pkr.hcl`) avec variables, builders, provisioners.
  - Scripts shell utilisé.
- Documentation technique
  - description du workflow Packer
  - explication du provisioning
  - difficultés rencontrées + solutions
  - architecture de l'image générée
  - étapes du déploiement VM dans Azure
  - tests réalisés et résultats
- Preuve de fonctionnement
  - Capture d'écran de l'IP publique + page web affichée
  - Commandes Azure montrant la présence de l'image
- Version optimisée
  - Modifications apportées
  - Justifications techniques

## Bonus

- Ajout de MySQL/MariaDB dans l'image.
- Application PHP complète (Laravel, Symfony) : build chain complète.
- Ajout de tests automatiquement lancés dans l'image.
- Intégration CI (GitLab / GitHub Actions) pour automatiser le build Packer.
- Intégration avec Ansible / Terraform pour automatiser le déploiement VM.
