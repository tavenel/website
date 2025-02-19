---
title: Jenkins - intégration continue
date: 2023 / 2024
---

## Récupération du code des exemples de cette séance

L'ensemble des projets utilisés dans cette séance est disponible dans le dépôt de code suivant :

```bash
git clone https://git.sr.ht/~toma/jenkins-b3
```

Ce dépôt contient, pour chaque exemple, un répertoire avec l'ensemble des sources à utiliser.

## Installation de Jenkins®

Nous allons utiliser le packaging de Jenkins® s'exécutant dans son propre serveur applicatif. Ce packaging n'est pas recommandé pour une véritable mise en production, mais est très utile pour déployer simplement une version de test.

Jenkins® étant basé sur `Java`, vous devez avoir installé une version récente de la technologie `Java`. La version courante supporte les versions 17 et 21 de `Java`.

### Installation

1. Récupérer le packaging `WAR` de la version `LTS` de Jenkins® depuis la page de téléchargement : <https://www.jenkins.io/download/>
2. Lancer Jenkins® depuis la ligne de commandes :
  + Ouvrir un invité de commandes dans le répertoire où a été téléchargé Jenkins®.
  + Depuis ce répertoire, lancer la commande `java -jar jenkins.war` dans le terminal.

### Configuration

L'installation ne devrait prendre que quelques secondes.

Attendre le message `Jenkins is fully up and running` puis ouvrir le programme en allant à l'URL <http://localhost:8080> dans votre navigateur.

Cela donne accès à une interface Web, que vous allez pouvoir utiliser pour configurer Jenkins®. Mais vous devez d'abord prendre une mesure de sécurité : Jenkins® a généré un mot de passe aléatoire pour vous.

Celui-ci se trouve dans le répertoire `.jenkins`, dans le dossier `Secrets` et enfin dans le fichier `initialAdminPassword`. Ce fichier peut être ouvert avec n'importe quel éditeur de texte. Copiez la chaîne de caractères et collez-la dans la zone dédiée de l'interface Web.

Maintenant, il est temps de configurer Jenkins®. L'assistant de configuration vous demandera si vous souhaitez choisir les plugins à installer ou si vous préférez utiliser le paramétrage par défaut intégrant déjà toutes les améliorations majeures. Nous allons choisir les plugins par défaut et installerons les plugins manquants lorsque nécessaire. Patientez pendant l'installation des plugins classiques, avant de passer à la création du compte utilisateur.

Remplir la configuration du compte utilisateur que vous souhaitez créer et valider. Jenkins® demande de valider l'URL de son serveur : garder la configuration par défaut <http://localhost:8080> et valider pour atteindre la page d'accueil du service.

## Premiers pas dans Jenkins®

Vous démarrez Jenkins® avec un environnement de travail complètement vide.

Pour démarrer un nouveau projet d'intégration continue, vous devez créer un nouveau job. Pour ce faire, utilisez l'icône visible au milieu de la fenêtre `create new jobs` ou l'option de menu `New Item`, que vous trouverez à gauche.

Ensuite, Jenkins® vous demande un nom pour votre projet et de choisir un type de projet : sélectionner `Freestyle project` (il s'agit du type le plus standard d'un job Jenkins®).

La page suivante propose de nombreuses options de paramétrage regroupées en six onglets.

Commençons par la `gestion du code source`. Pour ce projet, nous allons copier les sources à la main : choisir `None`.

À l'étape suivante, sélectionnez le `Build Trigger`. Cela déterminera dans quelles situations Jenkins® devra effectuer un build. Dans cet exemple, nous déclencherons un build manuellement lorsque nécessaire - ne rien sélectionner.

`L'environnement de build`, que Jenkins® vous laissera configurer par la suite, comprend d'autres options liées aux builds : une interruption, par exemple, si le processus se bloque ? Ou l'affichage d'un horodatage (timestamp) dans la console ? Aucune option n'est obligatoire.

Enfin, il s'agit du `Build` lui-même : ici, vous déterminez comment votre programme doit être construit. Comme vous avez déjà intégré les connexions à `Maven` et `Gradle` via la sélection standard de plugins, vous pouvez choisir l'un de ces programmes. Il est toutefois également possible d'utiliser des commandes simples de type ligne de commande. Sélectionnez l'option pour les commandes par `batch` pour ce premier exemple et entrez le script suivant :

```batch
del *.class
javac *.java
java -cp . App "2" "3"
```

Après cela, Jenkins® vous donne encore la possibilité d'exécuter des `actions postérieures au build`. Nous n'utiliserons pas ces options dans ce premier exemple : finir la configuration en sauvegardant les informations et créez votre premier job.

Chaque projet a sa propre sous-page dans Jenkins®. Ici, vous pouvez déclencher un build, modifier à nouveau les paramètres et consulter le statut.

Sur la page `Statut`, Jenkins® vous indique également `l'historique des builds`. Le dernier build a-t-il réussi ou non ? Jenkins® indique par des points bleus que le build a réussi. Le rouge représente une erreur qui doit être résolue immédiatement, conformément aux principes de l'intégration continue.

À cet endroit, vous verrez également quand un build est en cours. En cliquant sur le numéro de build, vous accédez à une page de détails où vous pouvez également afficher le contenu de la console.

**Lancez un premier build** du job que nous venons de créer dans Jenkins®. Ce build va échouer car nous n'avons pas encore copié les sources du projet, mais il aura pour effet de créer le répertoire de travail pour le job.

Nous allons maintenant **copier les sources** du 1er exemple : copiez le contenu du répertoire `calculator-java-simple` (sans le répertoire lui-même) dans le répertoire de travail : `.jenkins/workspace/{NomDuJobJenkins}`.

Le répertoire `.jenkins` peut varier d'un environnement à l'autre : c'est le même que celui utilisé lors de la configuration pour récupérer le fichier `initialAdminPassword`.

Relancez le build : celui-ci doit maintenant être valide. Vérifiez dans la console que la sortie du programme affiche bien : `The result is 5`.

![Résultat attendu dans Jenkins](@assets/jenkins/build-success.png)

## Exécution de tests unitaires et rapports de tests

_Le compilateur `javac` fourni par `Java` étant extrêmement limité, les projets `Java` utilisent généralement des outils de build leur permettant de gérer les dépendances.

Dans ce deuxième exemple, nous allons utiliser l'outil de build `Gradle` pour compiler et exécuter les tests unitaires `JUnit` de notre application.

Le build `Gradle` configure également un plugin `Jacoco` (`JavaCodeCoverage`) permettant de reporter la couverture de code des tests – ce rapport sera intégré dans Jenkins®._

Dans le tableau de bord de Jenkins®, vous pouvez voir tous les projets sur lesquels vous travaillez. Ici aussi, le programme matérialise l'état du projet par une couleur. Vous obtenez également des informations sur la Stabilité du build sous la forme d'un bulletin météo. Il s'agit d'une statistique sur la stabilité moyenne des builds du projet. Si plus de 80 % de vos builds réussissent, vous verrez un soleil. En dessous de cette valeur, la météo symbolique se dégrade.

### Installation du plugin de code coverage

Installer le plugin de code coverage : dans la page d'accueil de Jenkins® `Tableau de bord`, choisir `Administrer Jenkins`. Cliquer sur `Gestion des plugins` et dans l'onglet `Disponibles` choisir et installer le plugin [Code Coverage API Plugin](https://plugins.jenkins.io/code-coverage-api).

### Création du job

- Créez un nouveau job dans Jenkins®.
- Ajoutez une étape de `Build` en choisissant `Invoke Gradle Script`.
  + Sélectionner `Use Gradle Wrapper` pour utiliser le programme `gradle` fourni dans le projet.
  + Dans le champ `Tasks`, choisissez d'exécuter les tâches de test et de code coverage :
    - `clean test jacocoTestReport`
- Ajoutez une `Action à la suite du Build` en choisissant :
  + `Publier le rapport des résultats des tests JUnit`
  + Spécifier le chemin vers les rapports de test générés par `Gradle` :
    - `build/test-results/test/TEST-*.xml`
- Ajoutez une nouvelle `Action à la suite du Build` en choisissant de `Publier le rapport de Coverage`
  + Spécifier le chemin vers les rapports `Jacoco` générés par `Gradle` :
    - `build/reports/jacoco/test/jacocoTestReport.xml`
- Lancez un premier build pour créer le répertoire du projet.
- Copiez le contenu de l'exemple `calculator-java-gradle` dans le nouveau job. Attention à bien copier le contenu du répertoire directement dans le nouveau job (et pas dans un sous-répertoire `calculator-java-gradle`), sinon Jenkins ne trouvera pas le fichier `build.gradle` et le wrapper de `Gradle`.
- Lancez un nouveau build. Vérifier que les résultats de tests sont reportés dans la page du projet et que la couverture de code est affichée.

![Couverture des tests dans Jenkins](@assets/jenkins/code-coverage.png)

## Développement piloté par les tests

Nous allons maintenant réaliser le développement d'une nouvelle fonctionnalité en pilotant ce développement par les tests. Cette méthode de développement permet une augmentation significative de la qualité et de la rapidité de développement.

### Premier exemple

- Créez un nouveau job dans Jenkins. Récupérer les sources de l'exemple `calculator-java-gradle` et configurer l'exécution des tests et des rapports de tests dans Jenkins, de manière similaire aux exemples précédents.
- Ajoutez les tests correspondant à une nouvelle fonctionnalité permettant la multiplication de 2 entiers. Vérifiez que les tests sont lancés automatiquement dans Jenkins® mais échouent puisque l'implémentation n'est pas encore écrite.
  + En `Java` (programmation par contrat), les tests doivent s'appuyer sur un squelette de code sans implémentation dans le produit pour pouvoir compiler et exécuter le test :
  + Utiliser au maximum des interfaces
  + Lorsque nécessaire, on créera les classes concrètes avec des méthodes vides : `return null`
- Ajoutez l'implémentation de la fonctionnalité et vérifiez que les tests ne retournent plus d'erreur.
- Refactorez l'implémentation de la fonctionnalité.

### Second exemple

Récupérer le projet `calculator-kotlin`.

Ce projet en `Kotlin` permet d'exécuter une application réalisant des opérations simples sur deux `vecteurs` de même taille (les vecteurs utilisés ici sont simplement une suite de nombres).

Les opérations à supporter sont les suivantes :

- Opérations `+` et `-` => additionne / soustrait les éléments des vecteurs deux à deux.
  + Par exemple : `[ 1, 2, 3 ] + [ 2, 3, 4 ] = [ 3, 5, 7 ]`
- Opérations `*` et `/` => multiplie / divise les éléments des vecteurs deux à deux.
  + Par exemple : `[ 1, 2, 3 ] * [ 2, 3, 4 ] = [ 2, 6, 12 ]`
- La multiplication (et la division) sont prioritaires sur l'addition (et la soustraction) :
  + `[ 3, 4 ] + [ 1, 2 ] * [ 2, 3 ] = [ 3, 4 ] + [ 2, 6 ] = [ 5, 10 ]`

L'application peut être lancée de différentes manières :

- `./gradlew runTest`
  + Permet de lancer l'application et d'exécuter toujours la même opération (dans le but de tester le développement)
- `./gradlew run`
  + Exécute l'application en mode interactif : les éléments du premier vecteur, puis l'opérateur, puis les éléments du 2nd vecteur sont entrés séparés par un espace. Le caractère `;` permet de lancer l'opération.
- `./gradlew run –args='<operation>'`
  + Exécute l'application en mode non interactif : l'opération fournie en argument est directement exécutée.
  + Par exemple : `/gradlew run --args='1 2 + 3 4'`

- L'opération d'addition est déjà implémentée dans l'application. En s'inspirant du test unitaire de l'addition, ajouter les opérations manquantes en suivant la méthodologie TDD.
- L'application ne permet pour l'instant de réaliser qu'une unique opération sur deux vecteurs, mais les algorithmes de calcul sur les vecteurs (classe `VectorCal`) doivent supporter des opérations complexes. On vérifiera donc également dans les tests unitaires que les opérations complexes et la priorité des opérateurs sont bien supportés.

### Optimiser les temps d'exécution des tests

Le TDD crée vite beaucoup de tests unitaires, qui vont tourner souvent.

On sera donc particulièrement vigilant à optimiser la performance de ces tests :

- Séparer au maximum les tests par classe de test et package (et donc également le code du produit) pour ne pas devoir relancer tous les tests à chaque fois.
- Paralléliser les tests unitaires (ceux-ci ne doivent pas avoir d'état).
- Exclure toute dépendance externe dans les tests unitaires.
- Ajouter des étapes de **refactoring, y compris dans les tests**, pour :
  + Fusionner des tests semblables ou obsolètes.
  + Optimiser l'implémentation des tests.

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Apache, Apache Maven, and Maven are trademarks of the Apache Software Foundation.
- Jenkins® is a registered trademark of LF Charities Inc.
- GRADLE is a trademark of GRADLE, INC.
- Oracle and Java are registered trademarks of Oracle and/or its affiliates.
- Kotlin(TM) is a trademark or registered trademarks of JetBrains, s.r.o.
