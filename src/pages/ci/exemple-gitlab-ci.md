---
title: Exemple de Gitlab CI
---

Pour créer un pipeline d'intégration continue, il faut commencer par créer un fichier `.gitlab-ci.yml` à la racine du projet.

```yaml
#.gitlab-ci.yml

# Étapes séquentielles du pipeline
stages:
 - build # Les jobs d'un même stage tournent en parrallèle.
 - test
 - deploy

# Variables d'environnement à utiliser
variables:
 NODE_VERSION: "14.x"

# Description des Jobs du pipeline
build:
 stage: build # Lie le `job` avec un `stage`
 script:
    # Installation des dépendances & build de l'application
    - npm install
    - npm run build
 artifacts: # stockage des artéfacts produits
    paths:
      - build/

# Jobs de test
test-npm:
 stage: test
 script:
    - npm test
 only:
    - main # seulement sur les push de la branche `main`

test-job2:
 stage: test # groupe les 2 jobs `test-*` dans le même `stage`
 script:
    - sleep 20
 rules:
    # Exécuté seulement sur une merge-request, un tag, ou un push sur la branche principale
    - if: $CI_PIPELINE_SOURCE == 'merge_request_event'
    - if: $CI_COMMIT_TAG
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH

# Jobs de déploiement
deploy:
 stage: deploy
 script:
    - echo "Déployer sur le serveur"
 when: manual # uniquement manuellement depuis l'interface web
 needs:
    - job: build # dépendance sur le job `build`
      artifacts: true # récupère les artéfacts du job
```

