---
title: Exemple de Github Actions
---

Pour créer un pipeline d'intégration continue (appelé _GitHub Actions_), il faut créer dans le dépôt Git un fichier `.github/<NOM_DE_MON_WORKFLOW>.yml` 

Voici un exemple simple de pipeline :

```yml
#.github/mon-workflow.yml
name: mon-workflow # nom du pipeline (peut être différent du nom de fichier)

on: # quand tourner le pipeline
# https://docs.github.com/fr/actions/writing-workflows/workflow-syntax-for-github-actions#on
  pull_request:
    branches:
      - 'features/**'
  push:
    branches:
      - main

env: # variables d'environnement à injecter
  php_version: 8.3

# Le pipeline
jobs:

  test: # nom choisi pour le job
    runs-on: ubuntu-latest # environnement 
    concurrency: # limite le nombre de workflows en concurrence
      group: mon-workflow-${{ github.workflow }}-${{ github.ref }} # groupe les exécutions du pipeline courant
      cancel-in-progress: true # annule les précédents workflows en cours : utile si un nouveau commit annule le besoin de la CI actuelle

    steps:

    # Liste des "steps" à exécuter dans le job.
    # Voir <https://github.com/marketplace?type=actions> pour une liste d'actions pré-définies (`uses: `) 

      # récupération du code source
      - name: Checkout project
        uses: actions/checkout@v5

      # initialisation de l'environnement
      - name: Initialize PHP ${{ env.php_version }}
        uses: shivammathur/setup-php@v2
        with:
          php-version: ${{ env.php_version }}
          coverage: pcov

      # installation des dépendances
      - name: Composer install
        run: |
          composer validate --strict
          composer install --optimize-autoloader --no-interaction --prefer-dist

      # test de l'application
      - name: Test
        run: php artisan test
```

