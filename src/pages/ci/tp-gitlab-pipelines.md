---
title: TP GitLab CI/CD - introduction aux pipelines
date: 2025 / 2026
---

## Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

## GitLab CI/CD - introduction aux pipelines

GitLab fournit un service d'intégration continue intégré au dépôt : les _GitLab CI/CD pipelines_. Avec l'offre _GitLab SaaS (free tier)_, vous bénéficiez de **400 minutes de calcul par mois** sur des _shared runners_ Linux mis à disposition par GitLab, sans avoir à configurer votre propre infrastructure.

Un pipeline est défini par un fichier `.gitlab-ci.yml` placé à la **racine du dépôt Git**. Ce fichier décrit les étapes (appelées _jobs_) à exécuter dans un environnement Docker, déclenchées lors de certains événements (push, merge request, etc.).

### Structure d'un fichier `.gitlab-ci.yml`

Le fichier CI est un fichier YAML de la structure suivante :

```yaml
# .gitlab-ci.yml

# Étapes séquentielles du pipeline
stages:
  - lint
  - test
  - deploy

# Variables d'environnement à utiliser dans tous les jobs
variables:
  ANSIBLE_VERSION: "9.0.0"

# Job : analyse syntaxique Ansible
ansible-lint:
  stage: lint
  image: python:3.11-slim
  before_script:
    - pip install ansible ansible-lint
  script:
    - ansible-lint site.yml
  rules:
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

# Job : test de syntaxe Ansible (multi-versions)
ansible-syntax-check:
  stage: test
  image: python:3.11-slim
  parallel:
    matrix:
      - ANSIBLE_VERSION: ["7.0.0", "8.0.0", "9.0.0"]
  before_script:
    - pip install ansible==$ANSIBLE_VERSION
  script:
    - ansible-playbook site.yml --syntax-check
  rules:
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

### Prérequis : créer un compte et un projet sur GitLab.com

1. Rendez-vous sur <https://gitlab.com> et créez un compte gratuit _(si ce n'est pas déjà fait)_.
2. Créez un **nouveau projet** (public ou privé) dans lequel vous placerez votre code Ansible.
3. Clonez le dépôt en local et ajoutez vos fichiers de _playbook_ Ansible (par exemple `site.yml`).
4. Créez le fichier `.gitlab-ci.yml` à la racine du projet avec le contenu ci-dessus.

:::tip
GitLab CI/CD s'active automatiquement dès qu'un fichier `.gitlab-ci.yml` est présent dans la branche par défaut. Aucune configuration supplémentaire n'est nécessaire avec l'offre SaaS gratuite.
:::

### Ajout d'un linter Ansible

1. **Créer un pipeline** : Ajoutez le fichier `.gitlab-ci.yml` à la racine de votre dépôt en utilisant l'exemple ci-dessus. Poussez sur la branche principale (`main` ou `master`). Rendez-vous sur **Build > Pipelines** dans l'interface GitLab pour observer l'exécution du pipeline.

2. **Provoquer une erreur** : Modifiez le playbook `site.yml` pour créer un fichier invalide (par exemple en retirant une valeur obligatoire ou en introduisant une syntaxe YAML incorrecte). Poussez le changement sur une branche et ouvrez une _Merge Request_ vers la branche par défaut, ou poussez directement sur la branche par défaut. Vérifiez que le pipeline détecte bien l'erreur dans l'onglet **Build > Pipelines** ou directement dans la Merge Request.

3. **Corriger le problème** : Remédiez aux erreurs signalées par `ansible-lint` ou `ansible-playbook --syntax-check`. Poussez les corrections et vérifiez que le pipeline passe au vert.

:::exo
**Exercice bonus** : Ajoutez un job `ansible-playbook --check` (mode dry-run) dans le stage `test` pour valider le déroulé du playbook sans l'appliquer réellement.
:::

### Ajout d'un badge de pipeline

GitLab fournit un badge de statut pour le pipeline, accessible à l'adresse suivante :

```
https://gitlab.com/<OWNER>/<REPOSITORY>/badges/<BRANCH>/pipeline.svg
```

Par exemple, pour le projet `https://gitlab.com/moncompte/mon-projet` sur la branche `main` :

```markdown
[![Pipeline Status](https://gitlab.com/moncompte/mon-projet/badges/main/pipeline.svg)](https://gitlab.com/moncompte/mon-projet/-/pipelines)
```

_Ajoutez ce badge dans le fichier `README.md` du projet pour afficher l'état du pipeline sur la page d'accueil du dépôt._

:::tip
Pour personnaliser davantage le badge (couleur, texte, etc.), vous pouvez utiliser les _badges personnalisés_ depuis **Settings > CI/CD > General pipelines > Badges** dans l'interface GitLab.
:::

### Documentation

- Documentation GitLab CI/CD : <https://docs.gitlab.com/ee/ci/>
- Syntaxe du fichier `.gitlab-ci.yml` : <https://docs.gitlab.com/ee/ci/yaml/>
- Ansible Lint : <https://ansible-lint.readthedocs.io/>
- Tarifs GitLab SaaS (free tier) : <https://about.gitlab.com/pricing/>

# Legal

- © 2025 Tom Avenel under CC BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITLAB® and the GITLAB® logo design are trademarks of GitLab, Inc., registered in the United States and other countries.
