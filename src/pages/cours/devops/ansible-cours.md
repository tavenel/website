---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Ansible
tags:
- devops
- iac
---

# Objectifs
 
- Gérer un parc de machine simplement par Infrastructure-as-Code grâce à Ansible.

---

# Présentation d'Ansible

- Automatise des opérations sur un parc de machines
- **Agentless** : SSH depuis un poste de travail
  - autres protocoles disponibles
- **Stateless** : pas d'état du cluster
- **Idempotent** : décrit un but (et non l'action à effectuer)
- Outil d'IaC très populaire
  - fichiers `playbook` en `yaml`
- Simple d'utilisation dans un cadre standard
- Très nombreux plugins et rôles : <https://galaxy.ansible.com>

---

# Architecture

---

# Playbook

- Fichier `yaml` décrivant les opérations à effectuer
- Liste de `task`
- Supporte quelques opérateurs logiques et paramètres

---

# Inventory

- Collection de machines et de paramètres à fournir au(x) playbook(s) pour gérer les cibles d'exécution
- Possibilité d'inventaire dynamique par des plugins : `aws`, `VirtualBox`, …

---

# Exemple d'inventaire

```ini
#Fichier hosts

[web]
webserver-1 ansible_user=user1
webserver-2
webserver-3 ansible_user=user3

[web:vars]
ansible_connection=ssh

[all:vars]
test_file=/tmp/test
```

```sh
ansible-inventory --graph # affiche l'inventaire
ansible web -m ping -i hosts # exécute ping sur le groupe web de l'inventaire hosts
```

---

# Exemple de playbook

Inspiré de : [ansible documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)

```yaml
---
- name: Update web servers
  hosts: webservers
  remote_user: ansible
  become: yes

  tasks:
  - name: Ensure apache is at the latest version
    ansible.builtin.yum:
      name: httpd
      state: latest

  - name: Write the apache config file
    ansible.builtin.template:
      src: /srv/httpd.j2
      dest: /etc/httpd.conf

  - name: Start the service
    service:
      name: httpd
      state: started

- name: Update db servers
  hosts: databases
  remote_user: root

  tasks:
  - name: Execute a direct Unix command
    command: /sbin/update_db --confirm
```

---

```sh
ansible-playbook <mon_playbook.yml>
ansible-playbook -i <mon_inventaire> <mon_playbook.yml>
ansible-playbook --check […]
ansible-playbook -v […]
```

---

# Tags

Permet d'exécuter (ou ignorer) seulement certaines parties du playbook.

```yaml
[…]
  tasks:
  - name: Task avec tag
    file:
      dest: /etc/hosts
      state: absent
    tags:
      - suppression
  […]
```

```sh
ansible-playbook […] --tags suppression
ansible-playbook […] --skip-tags suppression
```

---

# Variables

Ansible peut utiliser une variable définie (inventaire, playbook, ligne de commande) et créer une variable dynamiquement dans le playbook.

---

```yaml
# Fichier playbook

---
- hosts: web
  vars:
    playbook_var_addr_list: ['::1', '192.168.32.0/24']
  tasks:
  - name: Create a file
    file:
      dest: '{{test_file}}'
      state: '{{file_state}}'
    when: test_file is defined

  - name: Create a new variable
    set_fact: dynamic_var="{{playboook_var_addr_list | ipv4('address') }}"
  - debug:
    msg: "Les adresses ipv4 sont : {{ dynamic_var }}"

  - shell: /usr/bin/uptime
    register: result_uptime
  - debug:
    msg: "L'uptime est {{ result_uptime }}"
```

---

# Rôles

- Collection de playbooks, variables, … pouvant être importés (idem plugin)
- 1 répertoire dédié par rôle et fichier `main.yml`

```sh
ansible-galaxy init mon_role
```

```yaml
---
- name: "Playbook with role"
  hosts: web
  become: yes
  roles:
    role: "mon_role"
```

---

# Secrets : Vault

- `Vault` : Stocke les informations sensibles : mot de passe, variables, (fichiers sensibles)
- Local ou Cloud provider : `AWS Key Management`, `Azure Key Vault`, …

---

```yaml
#Fichier group_vars/web/vars
---
password: '{{vault_mon_password}}'
```

```yaml
#Fichier group_vars/web/vault
---
vault_mon_password: SuperSecretP@ssw0rd
```

```yaml
#Fichier vault_playbook.yml
---
- hosts: web
  tasks:
  - name: print password
    debug:
      msg: 'Mon mot de passe est : {{password}}'
```

```sh
ansible-vault encrypt group_vars/web/vault
ansible-playbook --ask-vault-pass vault_playbook.yml
```

---

# Ansible linter

[ansible-lint](https://docs.ansible.com/ansible-lint/index.html) est un _linter_ permettant de trouver des erreurs dans les fichiers playbook.

---

<!-- class: liens -->
# Liens

- Documentation Ansible : <https://docs.ansible.com/ansible/latest/index.html>
- Tutoriel Ansible débutant : <https://alemorvan.frama.io/formatux.fr-support/SupportLinux-Automatismes-DevOPS.pdf>
  - correction du tutoriel : <https://docs.formatux.fr/DEVOPS-021-Ansible-Niveau-2-TD-Corrections.pdf>
- Liste complète de tutoriels Ansible en français : <https://gitlab.com/xavki/presentation-ansible-fr>
- [Ansible : cas pratique (1er partie)](https://blog.levassb.ovh/post/ansible-study-case/)
- [Cours et TPs Ansible](https://supports.uptime-formation.fr/06-ansible/cours1/)
- [AWX : interface Web de gestion d'ansible](https://github.com/ansible/awx)
- <https://blog.stephane-robert.info/post/ansible-vs-terraform/>
- <https://blog.microlinux.fr/formation-ansible/>
- Voir aussi le cours DevOps sur le [site web][site-perso]

---

# Legal 

- Ansible® is a registered trademark of RED HAT, INC.
- Vault is a trademark and brand of HashiCorp, Inc.
- Other names may be trademarks of their respective owners

