---
title: Développement d’une application moderne en utilisant les services avancés d’`AWS`
date: 2023 / 2024
---

# Remarques importantes sur l’utilisation des services `AWS` dans ce module de formation :

[Voir la remarque dans le TP précédent](/web/tp_aws-1)

# TP 2 : Développement d’une application moderne en utilisant les services avancés d’`AWS`

Dans ce deuxième TP sur les services `AWS`, nous allons voir comment utiliser des services avancés d’une plateforme Cloud pour créer une application Web moderne, en faisant abstraction au maximum de toutes les contraintes opérationnelles (build, déploiement, équilibrage de charge, …)

- Pour réaliser cette partie pratique, on suivra les cinq modules du [tutoriel Amazon](https://aws.amazon.com/fr/getting-started/hands-on/build-modern-app-fargate-lambda-dynamodb-python/).

## Note sur le langage de programmation

Dans ce TP, les exemples de code sont fournis et seuls l’interconnexion avec les services `AWS` est à réaliser, il y a donc très peu de code à entrer. Cependant, il est possible d’utiliser d’autres langages que la version standard du tutoriel (utilisant le langage Python) : voir les différentes branches du projet pour plus d’information.

## Note sur l'identifiant de compte

Dans tout le TP, l'identifiant du compte à renseigner est l'identifiant du compte `AWS`. Celui-ci est disponible en cliquant sur le nom de l’utilisateur, à côté de la rubrique : Mon Compte.

Pour les apprenants utilisant le compte partagé, cet ID du compte est le même pour tous les utilisateurs (demander l'identifiant au formateur).

## Rappel sur les noms de buckets

Les noms des buckets `S3` sont très sensibles à la casse et aux caractères spéciaux : préférer un nom entièrement en minuscule et sans caractère spécial !

## Note pour les pipelines CI/CD

Si, à partir de la fin de l'étape 2 (*pipeline CI/CD*), les changements dans le backend ne semblent pas s'être mis à jour (*modification manuelle de l'âge d'une créature sans impact, impossibilité de s'authentifier, ...*), il se peut que le processus de déploiement automatique (*CD*) ait échoué.

Pour investiguer cette erreur, on peut aller inspecter le service `CodeBuild` disponible dans la console de management d'`AWS` : c'est ce service qui orchestre ce déploiement automatique.

On pourra notamment aller voir les logs d'erreur de l'étape de Build, depuis le pipeline (*Pipelines Code Pipeline > Pipelines > Sélectionner le pipeline > Build > Détails*). En cas d'erreur interne Docker (*too many pulls*, ...), on pourra relancer manuellement la phase de Build grâce au bouton correspondant.

## Partie 4

Dans la partie 4 du tutoriel, le `Dockerfile` utilisé n’est pas à jour avec la dernière version du container Docker Ubuntu utilisé. Le package Python ne peut pas être installé, l'image Docker ne peut donc pas être générée et la phase de build échoue dans `CodeBuild`.

Pour résoudre ce problème, on modifiera le fichier `Dockerfile` fourni par le tutoriel par la version suivante :

<https://github.com/aws-samples/aws-modern-application-workshop/blob/7ee3074c7de97c8d7eadf8123142ce31573c99af/module-4/app/Dockerfile>


## Partie 5

A l'étape 3.C, si vous avez exactement suivi les instructions de copie précédentes, il y a une légère typo dans le chemin du fichier de configuration dans l'exemple de commande.

Ainsi, au lieu d’exécuter la commande :

```sh
aws cloudformation deploy --template-file /home/ec2-user/environment/MythicalMysfitsStreamingService-Repository/cfn/transformed-streaming.yml --stack-name MythicalMysfitsStreamingStack --capabilities CAPABILITY\_IAM
```

On exécutera à la place la commande :

```sh
aws cloudformation deploy --template-file /home/ec2-user/environment/MythicalMysfitsStreamingService-Repository/transformed-streaming.yml --stack-name MythicalMysfitsStreamingStack --capabilities CAPABILITY\_IAM
```

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- “Amazon Web Services", the “Powered by Amazon Web Services” logo, Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), Amazon Relational Database Service (Amazon RDS) are trademarks of Amazon.com, Inc. or its affiliates in the United States and/or other countries
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
