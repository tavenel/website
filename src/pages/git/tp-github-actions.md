---
title: TP Github Actions - introduction à la CI
date: 2023 / 2024
---

## Présentation

Dans la suite du TP, les commandes à entrer en utilisant votre utilisateur standard sont signalées par une ligne commençant par le symbole `$` (convention standard). Ce symbole n'est pas à entrer : par exemple, la ligne `$ ls .git` indique à l'utilisateur courant d'entrer la commande `ls .git` dans son terminal.

De manière similaire, une ligne commençant par le symbole `#` indique une commande à entrer par le super-utilisateur (Linux, MacOS) ou un administrateur du système (Windows).

## Github Actions - introduction à la CI

Les _Actions_ GitHub permettent très facilement une initiation à un worflow d'intégration continue très limité.

Une _Action_ est un fichier `.yml` situé dans le répertoire `.github/workflows`. Ce fichier va décrire un environnement `Docker` permettant de réaliser un ensemble d'étapes, par le biais de configurations prédéfinies, lors de certains événements.

### Structure d'un fichier d'action

Le fichier d'action est un fichier `.yml` de la structure suivante :

```yml
name: nom-de-l-action
on:
  push:
    branches:
      - stable
      - release/v*
  pull_request:

jobs:
  build:
    name: Nom du job
    runs-on: alpine-latest # Image Docker à utiliser
    strategy:
       max-parallel: 4
       matrix:
         python-version: [2.7, 3.5, 3.6, 3.7]
         ansible-version: [2.7.13, 2.8.4]

    steps: # liste des étapes du workflow
    - uses: actions/checkout@v5
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Ansible ${{ matrix.ansible-version }}
      run: |
        python -m pip install --upgrade pip
        pip install ansible-lint ansible==${{ matrix.ansible-version }}
    - name: Lint playbook
      run: |
        ansible-playbook site.yml --syntax-check
        ansible-lint site.yml
```

### Ajout d'un linter Ansible

1. Créer une action GitHub utilisant une action vérifiant la bonne écriture des fichiers `Ansible` (_linter_). On utilisera [Ansible Lint Action][ansible-lint-action] directement (plutôt que d'appeler la commande `ansible-lint` comme dans l'exemple précédent).
2. Modifier le playbook pour créer un fichier invalide - vérifier que la CI détecte bien une erreur.
3. Fixer les problèmes dans les fichiers - vérifier que la CI ne renvoie plus d'erreur.

### Ajout d'un badge

GitHub fournit un badge de statut par action configurée, celui-ci peut être récupéré à l'adresse :

```
https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/<WORKFLOW_FILE>/badge.svg
```

_Ajouter un fichier `README.md` pour afficher le badge de statut sur la page d'accueil du projet._

### Documentation

- Documentation Ansible Lint : <https://ansible-lint.readthedocs.io/>
- [GitHub Action pour Ansible Lint][ansible-lint-action]

[ansible-lint-action]: https://github.com/ansible/ansible-lint

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.

