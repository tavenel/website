---
title: TP Introduction à l'infrastructure-as-code (IaC)
date: 2023 / 2024
---

## 📋 Prérequis et installation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

`Ansible` est un outil d'automatisation d'opérations sur un parc de machines - il est utilisé principalement pour faire de l'Infrastructure-as-Code, c'est-à-dire la gestion de la configuration d'un parc de machines depuis du code source.

Ansible se connecte à un OS standard principalement en `SSH` - pour ce TP, il est donc nécessaire d'avoir une machine (locale ou distante) tournant un serveur SSH. On pourra utiliser une machine virtuelle type `VirtualBox`.

Une fois le serveur SSH déployé, cloner le dépôt contenant une configuration `Ansible` minimale pour tourner un 1er playbook.

Modifier le fichier `mes_hosts` pour utiliser l'IP du serveur SSH et le paramètre `remoute_user` du fichier `mon_playbook.yml` avec le nom de l'utilisateur qui se connectera en `SSH` sur le système.

Le playbook sera exécuté avec la commande suivante (se placer dans le répertoire du playbook) :

```
ansible-playbook -i ./mes_hosts mon_playbook.yml
```

```ini
#mes_hosts
[mes_machines]
pc_portable ansible_host=127.0.0.1
```

```yaml
#mon_playbook
---
- name: Mon premier playbook
  connection: ssh
  hosts: mes_machines
  remote_user: tom
  tasks:
    - name: Ping the system
      ansible.builtin.ping:
```

## Infrastructure-as-Code

### Nouveau remote

Une fois le playbook minimal testé avec succès, utiliser le gestionnaire de versions `Git` pour gérer différentes versions de la configuration du système. Pour cela :

1. Créer un nouveau dépôt de code en ligne (par exemple sur `GitHub`).
2. Ajouter ce dépôt à la liste des `remote` du dépôt actuel

_Quel est l'intérêt d'une telle configuration ? Comment s'appelle cette architecture de dépôts Git ?_

### Modifications du playbook

Maintenant, toutes les modifications de la machine virtuelle seront réalisées depuis le playbook `Ansible`, 

1. Tester l'ajout d'un nouveau fichier sur la machine cible grâce au module [copy][ansible-copy].
2. Déployer un serveur Web `Apache` depuis le playbook. On pourra notamment utiliser les modules du gestionnaire de paquets de la machine cible.

# Ressources

- documentation Ansible : <https://docs.ansible.com/ansible/latest/index.html>
  + [Module copy][ansible-copy]
- Tutoriel Ansible débutant : <https://alemorvan.frama.io/formatux.fr-support/SupportLinux-Automatismes-DevOPS.pdf>
  + correction du tutoriel : <https://docs.formatux.fr/DEVOPS-021-Ansible-Niveau-2-TD-Corrections.pdf>
- Liste complète de tutoriels Ansible en français : <https://gitlab.com/xavki/presentation-ansible-fr>
- [Ansible : cas pratique (1er partie)](https://blog.levassb.ovh/post/ansible-study-case/)

[ansible-copy]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html#ansible-collections-ansible-builtin-copy-module

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Ansible® is a registered trademark of RED HAT, INC.
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.
- Oracle® VirtualBox is a registered trademark of Oracle and/or its affiliates.

