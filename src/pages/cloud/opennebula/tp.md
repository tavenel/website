---
title: TP Découverte d'OpenNebula via miniONE
date: 2025 / 2026
---

## Objectifs pédagogiques

* Installer une instance de test d'OpenNebula : _miniOne_
* Utiliser l'interface _Sunstone_ et l'interface en ligne de commande d'OpenNebula pour déployer, gérer et surveiller des machines virtuelles.
* Comprendre les concepts clefs d'_OpenNebula_ : images, datastores, templates, VM, réseaux virtuels (VNET), hôtes, clusters, utilisateurs/quotas.
* Créer et gérer des images et templates, contextualiser des VM et manipuler le cycle de vie (`instantiate`, `suspend`, `resume`, `migrate`, `saveas`, `delete`).
* Automatiser des workflows simples avec le CLI (commandes `one*`) et écrire un script d'automatisation basique.
* Diagnostiquer des erreurs courantes et récupérer des métriques / logs via _Sunstone_ et la CLI.

## Prérequis

* Connaissances : virtualisation basique (KVM/Libvirt), notions de réseau (NAT, bridges), notions Linux (ssh, systemctl).
* Accès réseau entre votre poste et la VM miniONE pour utiliser le navigateur (_Sunstone_) et le CLI.
* Environnement : une machine pour installer `miniONE` (front-end OpenNebula + KVM ou LXD) avec accès SSH (user `oneadmin`)

## Installation

> _Remarque : ce TP suppose que miniONE fournit un front-end OpenNebula (utilisateur `oneadmin`) et des hôtes hyperviseurs configurés.

1. Installer _minOne_ avec KVM en suivant ce lien : <https://docs.opennebula.io/7.0/getting_started/try_opennebula/opennebula_sandbox_deployment/deploy_opennebula_onprem_with_minione/>
2. Vérification : se connecter en SSH au front-end miniONE :

   ```bash
   ssh oneadmin@<IP_frontend>

   # vérifier la version
   oned -v || oned --version

   # lister hôtes, images et templates
   onehost list
   oneimage list
   onetemplate list
   onevm list
   ```

3. Ouvrir Sunstone (interface web) en utilisant l'utilisateur `oneadmin` et le mot de passe donné à l'installation : vérifier que le dashboard montre le front-end, les hôtes et le datastore.

**Livrable 0 :** capture d'écran du `onehost list` et du dashboard Sunstone.

:::warn
- miniOne ne sert qu'à installer OpenNebula : une fois installé, le service redémarre avec la VM (donc il ne faut lancer la commande `./minione` qu'une fois).
- Si la symchronisation d'un hôte par SSH n'est plus possible (par exemple changement de clés SSH), penser à autoriser la connexion à l'hôte, dans notre cas il faut accepter notre VM miniOne à se connecter à elle-même : (en oneadmin) : `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`)
- Si besoin de réinstallation par miniOne, il existe une commande `./minione --purge` qui semble ne pas nettoyer correctement le système sur les dernières versions. La procédure recommandée est :

```sh
sudo ./minione --purge
sudo rm -rf /var/lib/one/*
sudo rm -rf /etc/one/*
sudo rm -rf /var/log/one/*
sudo -u oneadmin onehost sync --force
```
:::

## Images et Datastores

**Objectifs :** comprendre l'image comme disque, créer une image et l'enregistrer dans le datastore local.

1. Lister les images existantes : `oneimage list`.

2. Importer une image (exemple) vers le datastore local (commande générale) :

   ```bash
   # depuis le front-end oneadmin, on peut créer une image en local
   oneimage create --name "ubuntu-cloud" --path "/var/lib/one/datastores/0/images/ubuntu-20.04.qcow2" --type OS -d default

   # ou créer depuis une URL
   oneimage create --name "ubuntu-cloud" --path "https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img" --type OS -d default
   ```

3. Vérifier l'image : `oneimage show <ID>` et `oneimage list`.

4. Exercice : copier une image dans le datastore et la déclarer.

**Livrable 1 :** ID de l'image créée et sortie de `oneimage show <ID>`.

## Réseaux virtuels (VNET) et connectivité

**Objectifs :** créer un réseau virtuel, comprendre le plan d'adressage et attribuer des IPs.

1. Lister les VNETs : `onevnet list`.

2. Créer un VNET simple depuis un fichier template (exemple `vnet.tmpl`) :

   ```text
   NAME = "private-net"
   BRIDGE = "virbr1"
   VN_MAD = "bridge"
   
   AR = [
     IP = "192.168.100.1",
     SIZE = "100",
     IP_END = "192.168.100.100",
     TYPE = "IP4"
     ]
   ```

   Puis :

   ```bash
   onevnet create vnet.tmpl
   ```

3. Vérifier : `onevnet show <ID>`.

4. Exercice : instancier une VM et vérifier qu'elle obtient une IP depuis ce réseau (via `onevm show <vmid>` ou `ssh` dans la VM si accessible ou en utilisant la console VNC depuis l'interface web). Utiliser par exemple l'image _alpine_ par défaut qui fournit les credentials : `root`/`opennebula`

**Livrable 2 :** ID du VNET et capture d'écran du `onevnet show` et du `onevm show` montrant l'IP.

## Templates et création de VM

**Objectifs :** créer un template, instancier des VM, contextualiser et paramétrer la VM (CPU, mémoire, disques, NICs).

1. Inspection des templates existants : `onetemplate list` puis `onetemplate show <ID>`.

2. Créer un template minimal (fichier `template_ubuntu.tmpl`) en remplaçant la clé publique SSH la clé souhaitée :

   ```text
   NAME = "ubuntu-basic"
   MEMORY = 1024
   CPU = 1

   DISK = [
     IMAGE = "ubuntu-cloud"
   ]

   NIC = [
     NETWORK = "private-net"
   ]

   CONTEXT = [
     SSH_PUBLIC_KEY = "<SSH PUBLIC KEY>",
     NETWORK = "YES",
     SET_HOSTNAME = "YES"
   ]
   ```

   Déclarer le template :

   ```bash
   onetemplate create template_ubuntu.tmpl
   ```

3. Instancier une VM depuis le template :

   ```bash
   onetemplate instantiate <TEMPLATE_ID> --name "tp-vm-01"
   # ou via la GUI Sunstone -> Templates -> Instantiate
   ```

4. Vérifier la VM : `onevm list` puis `onevm show <VM_ID>`.

5. Connexion via SSH en utilisant l'utilisateur `ubuntu` et la clé SSH configurée dans le template.

6. Exercice : modifier la template pour ajouter un second disque et redéployer.

**Livrable 3 :** ID du template, ID de la VM, preuve de connexion SSH ou capture VNC.

:::tip
En cas d'erreur, les logs des VMs sont stockées dans `/var/log/one/<vm_id>.log`. Par exemple : `/var/log/one/1.log` pour la VM d'ID 1.
:::

## Cycle de vie et opérations avancées (sauvegarde/snapshots/migration)

**Objectifs :** pratiquer les actions courantes sur une VM.

1. Suspendre / reprendre :

   ```bash
   onevm suspend <VM_ID>
   onevm resume <VM_ID>
   ```

2. Migrer (live ou cold) vers un autre hôte (si multi-hôte présent) :

   ```bash
   onevm migrate <VM_ID> <HOST_ID>
   ```

3. Sauvegarder le disque d'une VM : `onevm disk-saveas <VM_ID> <DISK_ID> <image_name>` (crée une image à partir d'un disque).

4. Créer un snapshot (selon support) : `oneimage snapshot` / `onevm snapshot-create` _selon version_ (vérifier la disponibilité).

5. Exercice : faire un `disk-saveas`, créer une nouvelle template à partir de cette image et déployer une VM identique.

**Livrable 4 :** log des commandes et vérification de la nouvelle VM créée à partir de l'image sauvegardée.

## Gestion des utilisateurs, groupes et quotas

**Objectifs :** comprendre contrôle d'accès et quotas.

1. Lister les utilisateurs : `oneuser list`.

2. Créer un utilisateur de test :

   ```bash
   oneuser create tp_student password
   ```

3. Affecter un groupe et quotas :

   ```bash
   onegroup create tp_group
   oneuser chgrp <USER_ID> <GROUP_ID>
   oneuser quota <GROUP_ID>
   ```

4. Ajout un quota : max 2 CPU, 512MB Memory et 3 VMs

5. Exercice : connecter vous à Sunstone en tant que l'utilisateur créé et tenter d'instancier une VM. Observer les limites.

**Livrable 5 :** capture Sunstone en tant que `tp_student` et description des quotas appliqués.

## Supervision, logs et dépannage

**Objectifs :** apprendre à récupérer informations opérationnelles et logs.

1. Consulter l'historique et l'état d'une VM : `onevm show <VM_ID> --all` et `onevm top <VM_ID>`.

2. Vérifier les logs OpenNebula :

   * Front-end : `/var/log/one/oned.log`
   * FireEdge Sunstone : `/var/log/one/fireedge.log`
   * Hypervisor (libvirt) sur l'hôte : `/var/log/libvirt/*` (ou systemctl journalctl)

3. Exercice : provoquer une erreur volontaire (par ex. retirer l'image du datastore sans mettre à jour la template) et diagnostiquer la cause via `oned.log` et `onevm show`.

**Livrable 6 :** extrait de logs et explication du diagnostic et de la résolution proposée.

:::link
Voir aussi : <https://docs.opennebula.io/7.0/product/operation_references/opennebula_services_configuration/troubleshooting/>
:::

## Automatisation basique

**Objectifs :** créer un script shell ou Python simple pour automatiser le déploiement d'un nombre N de VM et récupérer leurs IPs.

1. Exemple en shell (bash) :

   ```bash
   #!/bin/bash
   TPL_ID=<TEMPLATE_ID>
   for i in $(seq 1 3); do
     VM_NAME="auto-vm-$i"
     VID=$(onetemplate instantiate $TPL_ID --name "$VM_NAME" --multiple 1)
     echo "La VM $VM_NAME -> ID $VID"
     sleep 5
     onevm show $VID | grep -i ip || true
   done
   ```

2. Exercice : écrire un script qui :

   * instancie 5 VM
   * attend qu'elles soient en état `RUNNING`
   * récupère leurs IPs et les enregistre dans un fichier CSV

**Livrable 7 :** script complet + CSV produit.

## Challenges / Bonus (facultatif)

1. Intégrer un datastore externe (NFS) et migrer des images dessus.
2. Mettre en place un hook qui exécute une action lors de l'instanciation d'une VM (ex : envoi d'un message à un webhook ou exécution d'un script de tagging).
3. Tester l'export/import dans le marketplace (`onemarket`), ou explorer l'intégration Ceph (si disponible dans l'environnement).

## Rappel rapide des commandes CLI utiles

* `onehost list | show` : gestion des hôtes
* `oneimage list` / `oneimage show <ID>` / `oneimage create ...` : images
* `onevnet list` / `onevnet create file` / `onevnet show` : réseaux virtuels
* `onetemplate list` / `onetemplate create file` / `onetemplate instantiate <ID>` : templates
* `onevm list` / `onevm show <ID>` / `onevm migrate <ID> <HOST_ID>` / `onevm suspend <ID>` etc. : VM
* `oneuser create` / `onegroup create` / `onequota` : utilisateurs et quotas
* `oned.log` et `sunstone.log` : logs principaux

---


