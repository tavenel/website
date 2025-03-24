---
title: Exemple de fichier Jenkinsfile
---

Pour créer un pipeline d'intégration continue (appelé _Job Jenkins_), il faut créer dans le dépôt Git un fichier _Jenkinsfile_, par exemple : `jenkinsfile.yml`. Dans Jenkins, on crée ensuite un projet de type _Pipeline_ avec une étape _"Pipeline script from SCM"_ et on spécifie le chemin du fichier _Jenkinsfile_ créé.

:::link
- Pour créer le Job Jenkins associé, voir [ce tutoriel](https://medium.com/@sangeetv09/create-a-jenkins-pipeline-using-a-jenkinsfile-f67b11e3f0b3)
- Pour apprendre à écrire le pipeline, voir la documentation officielle : <https://www.jenkins.io/doc/book/pipeline/jenkinsfile/>
- Pour des exemples d'utilisation de plugins Jenkins en Infrastructure-as-Code, voir le dépôt officiel : <https://github.com/jenkinsci/configuration-as-code-plugin>
- Pour des exemples de `Jenkinsfile` plus poussés, voir : <https://gist.github.com/merikan/228cdb1893fca91f0663bab7b095757c> et <https://github.com/hoto/jenkinsfile-examples>
:::

## Declarative pipeline

Le 1e mode (simple) d'écriture d'un pipeline Jenkins est le mode **déclaratif**.


```groovy
pipeline {
    agent any // peut s'exécuter sur n'importe quel agent

    parameters {
        string(name: 'DEPLOY_ENV', defaultValue: 'staging', description: 'The environment to deploy to')
    }

    stages { // le pipeline à exécuter

       stage('Build') { // une étape du pipeline
            steps { // les commandes de l'étape
                sh 'make'
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
       }

       stage('Test') {
            steps {
                sh 'echo "Running tests"'
                junit '**/target/*.xml'
            }
       }

       stage('Deploy') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS' 
              }
            }
            when {
              environment name: 'DEPLOY_ENV', value: 'prod'
            }
            steps {
                sh 'make publish'
            }
       }
    }
    post { // exécuté après le pipeline
        always {
            echo "Hello after Jenkinsfile pipeline"
        }
				success {
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
```

### Parrallélisme

Pour parralléliser l'exécution de certains _steps_, il faut le déclarer explicitement :

```groovy
pipeline {
    agent any
    stages {
        stage('Tests') {
            steps {
                parallel {
                    stage('Unit Test') {
                        steps {
                            echo 'Running unit tests...'
                        }
                    }
                    stage('Integration Test') {
                        steps {
                            echo 'Running integration tests...'
                        }
                    }
                }
            }
        }
    }
}
```

## Scripted pipeline

Jenkins supporte également un 2e mode (avancé) d'écriture des pipelines appelé **Scripted pipeline**. Dans ce mode, il s'agit d'utiliser toute la puissance du langage _Groovy_ plutôt qu'une _DSL_ Jenkins. On utilise ici un exemple simple avec un Noeud d'exécution unique et peu de dépendances donc l'écriture est assez similaire :

```groovy
node { // exécution sur un `node` générique (peut recevoir des arguments)

  stage('Checkout'){ // une étape du pipeline
     checkout scm // récupération du code (plugin Jenkins)
  }

  stage('Build') {
  	  // Script Shell
      sh 'make' 
      archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
  }

  stage('Test') {
  	  sh npm run test
  }

  stage('Build Docker'){
       sh './dockerBuild.sh'
  }

  stage('Deploy'){

      if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
          sh './dockerPushToRepo.sh'

          echo 'ssh to web server and tell it to pull new image'
          sh 'ssh deploy@xxxxx.xxxxx.com running/xxxxxxx/dockerRun.sh'
      }

  }
}
```

:::tip
Voir aussi : <https://www.baeldung.com/ops/jenkins-agent-vs-node>
:::

