---
title: Jenkins - intégration continue
date: 2024 / 2025
---

## Objectif

L’objectif de ce TP est d’installer le serveur d’intégration continue Jenkins et de tester l’intégration d’un ensemble d’outils de l’intégration continue dans des jobs dédiés.

## Récupération du code des exemples de cette séance

L'ensemble des projets utilisés dans cette séance est disponible dans le dépôt de code suivant :

```bash
git clone https://git.sr.ht/~toma/jenkins_exemples
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

## Exemple 1. Premiers pas dans Jenkins®

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

## Exemple 2. Exécution de tests unitaires et rapports de tests

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

## Exemple 3. Utilisation d’un gestionnaire de versions (Git)

Dans cet exemple, nous allons utiliser le gestionnaire de versions Git pour récupérer et valider automatiquement les changements dans le code de notre projet.

1. **Créez un nouveau dépôt de code git**
    1. Ce dépôt peut être créé localement sur la machine de travail, ou en utilisant un hébergement en ligne de type Github, Bitbucket, Gitlab, …
    2. Copiez les sources données dans cet exemple dans le nouveau dépôt git
2. **Créez un nouveau job** dans Jenkins en utilisant, et configurez l’accès au dépôt git :
    1. Dans la section **Gestion du code source**, sélectionner git et renseignez l’accès à votre dépôt

- 1. Dans la section _Ce qui déclenche le build_, sélectionnez _Scrutation de l’outil de gestion de version_. Cela permet d’analyser le dépôt git suivant une horloge configurée pour chercher d’éventuels changements à analyser, et de lancer un nouveau build dans le cas où des changements seraient détectés.

On pourra per exemple utiliser le planning H/5 \* \* \* \* pour vérifier toutes les 5 minutes l’arrivée de changements.

1. Dans la section **Build**, ajouter une cible Maven **compile** afin de compiler les sources récupérées.

## Exemple 4. Intégration des tests dans Jenkins

Dans ce nouvel exemple, nous allons utiliser les cibles Maven orientées tests pour exécuter les tests unitaires présents dans le répertoire et afficher leurs résultats.

**Créez un nouveau job** en utilisant les sources de cet exemple, et créez :

- Une étape de **Build** invoquant des cibles Maven : verify
- Dans la section **Actions à la suite du build,** ajouter une nouvelle étape **Publier le rapport des résultats des tests JUnit**

Lancer un build et vérifier que les résultats de tests sont affichés dans le sommaire du projet Jenkins :

Notez au passage que l’utilisation de cibles Maven nous a permis d’exécuter automatiquement les tests unitaires à chaque build, sans aucune configuration supplémentaire.

## Exemple 5. Développement piloté par les tests

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

## Exemple 6. Intégration avec Gradle

Dans cet exemple, nous allons utiliser l’outil de build Gradle pour construire et tester un projet. Gradle est très similaire à Maven (et utilise le même système de dépendances) mais utilise un fichier \`build.gradle\` de configuration du build au format Groovy ou Kotlin.

1. Créez un nouveau job dans Jenkins en utilisant le code source de cet exemple.
2. Ajoutez une étape de **Build** en choisissant **Invoke Gradle Script**.
    1. Sélectionner **Use Gradle Wrapper** pour utiliser le programme gradle fourni dans le projet.
    2. Dans le champ **Tasks**, choisissez d’exécuter la tâche **clean test**.
3. Ajoutez une **Action à la suite du Build** en choisissant de **Publier le rapport des résultats des tests JUnit**.
    1. Spécifier le chemin vers les rapports de test générés par Gradle : **build/test-results/test/TEST-\*.xml**
4. Lancez un nouveau build. Vérifier que les résultats de tests sont reportés dans la page du projet.
5. Afficher la sortie de la console enregistrés durant le build. Vérifier que les différentes tâches Gradle ont bien été extraites dans l’arbre de gauche.

## Exemple 7. Mise en place de jobs chaînés

Dans cet exemple, nous allons voir un aperçu d’une des fonctionnalités les plus puissantes de Jenkins : celle de créer des liens logiques de dépendances entre les jobs.

1. Créez un premier job dans Jenkins (on gardera la configuration par défaut pour créer un job vide). Ce job sera exécuté automatiquement après un job gérant ses pré-requis.
2. Créez un second job. Ce job sera le pré-requis à l’exécution du job précédent :
    1. Ajouter une **Action à la suite du Build** pour **Construire d’autres projets en aval**.
    2. Renseigner le projet précédent dans les **Projets à constuire**
    3. Sélectionner l'exécution du premier job seulement si la construction est stable.
3. Lancer un nouveau build du second job. Vérifier qu’à la fin de ce build, une exécution du premier job est lancée automatiquement.

Dans la pratique, les dépendances entre jobs sont utilisées :

- Pour appeler des jobs de publication de résultats ou tout autre process qui peuvent être communs à un ensemble de builds d’intégration continue
- Pour gérer des opérations de nettoyage du système en cas d’échec lors d’un build
- Pour séparer les différentes étapes d’un process d’intégration continue : compilation des sources, exécution des tests, analyse statique, ...

## Exemple 8. Les plugins "Warnings Next Generation" et "Git Forensics"

Dans cet exemple, nous allons installer et utiliser deux plugins dans Jenkins :

Le plugin “Warnings Next Generation” qui permet de répertorier les erreurs et avertissements renvoyés par différents outils de compilation et d’analyse statique

Le plugin “Git Forensics” qui permet d’identifier le commit et le développeur ayant créé les modifications à la base des erreurs reportées

### Installation d’un plugin dans Jenkins

Dans le tableau de bord Jenkins, choisir “Administrer Jenkins” puis “Gestion des plugins”. Cliquer sur l’onglet “Disponibles” et rechercher le plugin à installer. Jenkins supporte mal l’installation à chaud de plugins : choisir l’option “Télécharger maintenant et installer après redémarrage”

Redémarrer Jenkins pour prendre en compte les changements.

Note : il est recommandé d’installer les plugins l'un après l’autre et de redémarrer Jenkins entre chaque installation, pour éviter des problèmes d’interdépendances.

1. Installez les plugins “Warnings Next Generation” et “Git Forensics”.
2. Créez un nouveau job dans Jenkins, en utilisant le dépôt git des exemples fournis.
    1. Configurer l’étape de **Build** avec une unique étape exécutant la compilation du programme en affichant tous les avertissements :

javac -Xlint:all App.java

- 1. Ajouter une **Action à la suite du Build** de type **Record compiler warnings and static analysis results**. Sélectionner l’outil **Java**.

1. Lancez un nouveau build. Vérifiez que les avertissements du compilateur sont bien affichés et que le commit contenant les changements incriminés est bien reporté.

## Exemple 9. Création de pipelines

Dans cet exemple, nous allons utiliser la fonctionnalité de pipeline de Jenkins. Les pipelines offrent la possibilité d’ordonnancer simplement des jobs complexes, permettant la construction de projets aux dépendances multiples.

Créez un nouveau Job dans Jenkins, mais cette fois choisissez le type de job Pipeline.

Dans la section 'Build Triggers', cocher 'Poll SCM' pour scruter régulièrement le gestionnaire de versions (on pourra utiliser `* * * * *` en test pour une vérification toutes les minutes).

Note: lorsque c'est possible, il est préférable d'utiliser un \_webhook_ pour pusher les changements depuis l'hébergeur Git (\`Github\`, \`Gitlab cloud\`, \`Bitbucket\`, …) et déclencher le build. Cependant \`Jenkins\` n'est pas toujours accessible publiquement, il faut alors utiliser un pull et du polling pour scruter périodiquement si de nouveaux commits sont arrivés.

Sélectionner le template “Pipeline Script” et, en utilisant les exemples fournis par Jenkins générer un pipeline en cinq étapes :

- Une étape de préparation récupérant les sources du projet sur un dépôt distant (Bitbucket, Github, Gitlab, …). On pourra s'inspirer de la configuration de l’exemple 3 (Utilisation d’un gestionnaire de versions Git)
- Une étape compilant les sources du projet (on utilisera la cible Maven compile)
- Une étape exécutant les tests (mvn test)
- Une étape réalisant le packaging de l’application (mvn package -DskipTests)
- Une étape agrégeant les résultats de tests et archivant le jar créé à l’étape précédente

Pour s'aider à l'écriture du script, on pourra utiliser le bouton \`Pipeline Syntax\` qui permet de générer le script du pipeline depuis les interfaces graphiques des différentes étapes.

Exemple de pipeline :

```groovy
pipeline {

  // Utiliser n'importe quel agent (worker) disponible
  agent any
  
  stages {
    // Liste des étapes
    
    // Découpage logique en `stage {}` (correspond aux grandes étapes du pipeline)
    stage('Checkout') {
      steps {
        // Liste des étapes - une étape par ligne
        git 'https://…'
      }
    }
    
    stage('Build') {
      steps {
        sh mon_script.sh
      }
      post {
        success {
          archiveArtifacts 'mon_build.zip'
        }
      }
    }

}
```

Lancez un nouveau build et vérifiez le bon déroulement du pipeline.


Les pipelines sont une fonctionnalité puissante de Jenkins, mais leur utilisation dans l’interface classique n’est pas très adaptée. On pourra utiliser les plugins Blue Ocean qui fournissent une interface plus optimisée pour les pipelines.


## Exemple 10. Réutilisation d’artéfacts

Dans cet exemple, nous verrons comment réutiliser dans un job des objets déjà créés dans un build précédent.

1. Installez le plugin “Copy Artifact”. Ce plugin va nous permettre de transférer un objet créé pendant un build dans un second build.
2. Créez un premier job artefactA utilisant les sources de l’exemple avec les configurations suivantes :
    1. Le **Build** exécute une unique tâche Gradle : **build**
    2. Accorder la permission d’accéder aux artéfacts à un futur job artefactB
    3. A la suite du build, archiver l’artefact : build/distributions/\*.zip
3. Créez un second job artefactB avec les configurations suivantes :
    1. Construire après le build d’artefactA
    2. Dans la section Build :
        1. La première tâche sera de type **Copy artifacts from another project**. Choisir le projet artefactA, le build **Upstream build that triggered this job** (afin de récupérer l’artéfact du build précédent), et cocher **Flatten directories**
        2. La deuxième tâche sera une commande batch permettant de dézipper l’artéfact :

**tar.exe -x -f .\\artefactA.zip**

- - 1. La dernière tâche sera l’exécution du programme dans une commande batch :

**.\\artefactA\\artefactA\\bin\\artefactA 3 5**

1. Lancez un build du projet artefactA. Vérifiez que le build d’artefactB est lancé et que le résultat de l’addition est affiché.

En pratique, cette réutilisation d’artéfacts est très utile dans des process d’intégration continue de projets contenant de nombreux composants n’ayant pas tous le même cycle de vie (ce qui est typique d’une architecture microservices). Dans ce cas, on sépare au maximum les fonctionnalités du projet dans des jobs Jenkins dédiés. Cela permet de ne pas avoir à tester de nouveau le reste du projet en cas de changement dans une fonctionnalité isolée (on utilisera uniquement les objets déjà testés). Par exemple : si le service de login n’a pas évolué, on pourra directement intégrer le dernier build de ce service à la construction du projet.

## Exemple 11. Administration de Jenkins

### Sauvegarde et restauration

#### Sauvegarde manuelle

Jenkins enregistre toutes ses données dans le répertoire JENKINS_HOME. La forme de sauvegarde la plus simple consiste donc à sauvegarder l’ensemble de ce répertoire. Celui-ci pouvant cependant être très volumineux, on pourra choisir d’omettre certains sous-répertoires : historique des jobs, artéfacts, binaires des plugins, …

De même qu'il est sage de réaliser des sauvegardes fréquentes, il est également sage de tester régulièrement cette procédure. Jenkins permet cela très facilement : il suffit de changer la variable JENKINS_HOME pour pointer vers le répertoire de sauvegarde :

$**exportJENKINS_HOME=/tmp/jenkins-backup**

**$ java -jar jenkins.war --httpPort=8888**

1. Réalisez une sauvegarde manuelle du répertoire JENKINS_HOME (par défaut : .jenkins dans le répertoire utilisateur)
2. Testez la sauvegarde en démarrant une nouvelle instance de Jenkins utilisant cette sauvegarde

#### Le plugin Backup

Une solution de facilité pour gérer les sauvegardes est de déléguer ce procédé à un plugin dédié.

1. Installez le plugin Backup
2. Configurez la sauvegarde depuis la page d’administration de Jenkins
3. Testez la restauration depuis la sauvegarde effectuée

### Gestion de la sécurité

1. Créez un nouvel utilisateur depuis la page d’administration de Jenkins. Cet utilisateur sera dédié à l’exécution d’un job.
2. Ouvrez les options de sécurité depuis la page d’administration.
    1. Jenkins permet de déléguer la gestion des comptes utilisateurs à des services de login dédiés (LDAP, …). C’est généralement cette option qui est utilisée, mais pour éviter le déploiement d’un annuaire LDAP nous continuerons d’utiliser des comptes locaux dans nos exemples.
    2. Changer le mode d’autorisations par défaut (“Les utilisateurs connectés peuvent tout faire”) pour **Stratégie d'authorisation matricielle basée sur les projets**. Cette stratégie permet une gestion fine des autorisations, en ajoutant de nouvelles options dans chaque job définissant quel utilisateur peut accéder à ce job.
        1. On pensera à ajouter les droits d’administration à l’utilisateur courant pour pouvoir continuer à configurer des jobs dans Jenkins !
        2. Donner le droit **Global:Read** à l’utilisateur créé à la première étape
    3. Ouvrir la configuration du job de l’exemple 1. Sélectionner **Activer la sécurité basée projet** et ajouter l’utilisateur créé à la première étape en lui accordant uniquement les droits **Job:Read** et **Job:Build**
3. Connectez-vous avec l’utilisateur créé à la première étape. Vérifiez que cet utilisateur a uniquement accès au job précédent et que cet utilisateur peut lancer un nouveau build.

### Exécution des jobs dans des nœuds distants

1. Déployez une machine virtuelle Debian qui fournira un environnement d’exécution Linux :
    1. Installer VirtualBox <https://www.virtualbox.org/wiki/Downloads>
    2. Créer une machine virtuelle de type Linux (debian, ubuntu)
    3. Dans les paramètres réseau de la machine virtuelle, choisir de configurer la carte réseau en ‘Pont’ (et non en NAT par défaut) pour que la machine hôte et la machine virtuelle puissent communiquer entre eux
    4. Démarrer la machine virtuelle
    5. Installer Java dans la machine virtuelle (requis pour installer un agent Jenkins)
2. Depuis la page d’administration de Jenkins, cliquez sur **Créer un nœud**
    1. Utiliser **/home/osboxes/jenkins** comme répertoire de travail distant
    2. Choisir **Launch agents via SSH comme** méthode de lancement
        1. Entrer l’adresse IP du la machine virtuelle
        2. Entrer le nom d’utilisateur / mot de passe de la machine virtuelle

- 1. Valider, sélectionner l’agent et afficher les logs pour vérifier que l’installation se déroule correctement

1. Créez un nouveau job à exécuter sur ce nouvel agent :
    1. Créer un nouveau job dans Jenkins
    2. Choisir **Restreindre où le projet peut être exécuté** et entrer le nom du nouvel agent
    3. Ajouter une étape de **Build** de type **script shell :**

**uname –a**

1. Lancez un nouveau build : vérifier que le build tourne bien sur le nouvel agent


## Exemple 12. Intégration avec SonarQube

Dans cet exemple, nous allons installer un serveur d’analyse SonarQube. Nous intégrerons ensuite les rapports de SonarQube dans Jenkins pour afficher une vue centralisée du projet.

1. **Installer le serveur SonarQube**
    1. Télécharger le serveur SonarQube (choisir la version community) : <https://www.sonarsource.com/products/sonarqube/downloads/>
    2. Démarrer le serveur SonarQube, par exemple : C:\\Program Files\\sonarqube-9.6.1\\sonarqube-9.6.1\\bin\\windows-x86-64\\StartSonar.bat
    3. Vérifier le bon démarrage du serveur : [http://localhost:9000](http://localhost:9000/) (admin/admin)
2. **Installer et configurer le scanner SonarQube pour Jenkins**
    1. Installer le plugin **“SonarQube Scanner”**
    2. Configurer le scanner :

Dans le panel “Administrer Jenkins”, choisir “Configuration Globale des Outils”. Dans la section “SonarQube Scanner”, cliquer sur le bouton **“Ajouter SonarQube Scanner”**. Vérifier que l’installation automatique depuis le Maven Central est bien sélectionnée :

1. **Configurer le serveur SonarQube dans Jenkins**

Dans le panel “Administrer Jenkins”, choisir “Configurer le système”. Remplir la section “SonarQube servers" (spécifier notamment **l’injection de variables SonarQube dans le build**) :

1. **Configurer SonarQube dans le job Jenkins**. Créer un nouveau job dans Jenkins utilisant les sources de l’exemple SonarQube, avec la configuration suivante :
    1. Dans la section “Environnements de Build”, cocher l’option **“préparer l'environnement pour SonarQube Scanner”**
    2. Dans la section “Build” :
        1. Ajouter une étape de build Maven lançant la cible **verify**
        2. Ajouter une étape de build Maven lançant la cible **sonar:sonar**
2. **Lancer le build**, vérifier que celui-ci n’échoue pas et que la page du projet dans Jenkins affiche un succès d’analyse dans Sonar. Afficher les résultats de l’analyse dans Sonar.

1. **Analyser le fichier pom.xml dans les sources fournies**. Pour réaliser la couverture des tests, le plugin **jacoco** a été ajouté au projet. L’intégration du projet dans Sonar est réalisée par le biais du plugin **sonar** pour Maven.

Pour plus d’information sur l’utilisation des scanners SonarQube, on pourra visiter : <https://docs.sonarqube.org/latest/analysis/overview/>

## Exemple13. Intégration avec TestLink

Dans cet exemple, nous allons intégrer Jenkins avec l’outil TestLink pour enregistrer les résultats des tests exécutés dans Jenkins à l’intérieur de TestLink.

1. **Installer une instance de TestLink.** Testlink est une application PHP - On pourra utiliser ce tutoriel pour l’installer : <https://www.tutorialspoint.com/testlink/testlink_installation.htm>
2. **Configurer l’instance de TestLink :**
    1. Se connecter sur l’instance de TestLink. Créer un nouveau projet (cocher **Enable Test Automation, Active et Public)**
    2. Créer une clé pour utiliser l’API de TestLink : dans les paramètres de TestLink (bouton MySettings tout en haut), créer une nouvelle clé permettant d’accéder à l’API


- 1. Nous allons maintenant définir un champ personnalisé afin de faire le lien entre un test dans TestLink et la classe d’un test unitaire exécuté dans Jenkins. Pour cela :
        1. Depuis la page principale, cliquer sur “Define Custom Fields”
        2. Créer un nouveau champ, choisir un nom (par exemple : java_class) et un label pour l’affichage, garder les autres paramètres par défaut.


- - 1. Choisir “Add and assign (to current test project)”

    1. La prochaine étape est l’ajout d’un scénario de test dans TestLink. Ce scénario sera utilisé pour la mise à jour des résultats d’exécution depuis Jenkins. Pour ajouter ce scénario :
        1. Dans la page d’accueil, cliquer sur **Test Specification**
        2. Nous allons commencer par créer une suite de tests qui contiendra le scénario de test. Dans la page qui s’affiche, cliquer sur la roue pour afficher les options de création, cliquer sur le bouton “+” et choisir un nom pour la nouvelle suite de tests.

- - 1. Une fois la nouvelle suite de tests créée, sélectionnez-la dans le menu de gauche
        2.  Nous allons maintenant créer un scénario de test dans cette suite de tests. De la même manière que précédemment, cliquer sur la roue puis sur le bouton “+” à la suite de **Test Case Operations**.
            1.  Choisir un titre pour le scénario de test
            2.  Changer le type d’exécution à **Automatique**
            3.  Le nouveau champ personnalisé (par exemple : java_class) ayant été associé au projet, un nouveau champ est disponible à la création du scénario. Remplir ce champ avec le nom de la classe de test que nous utiliserons dans ce projet : **epsi.AppTest**
            4.  Valider la création du scénario de test

    1. Dernière étape : TestLink utilise des plans de tests pour décrire et reporter l’exécution de tests.
        1. Créez un nouveau plan de test dans TestLink (**Test Plan Management / Create**) Sélectionner **Active** et **Public**.
        2. Nous allons maintenant ajouter le scénario de test créé précédemment dans le plan de test.
            1. Depuis la page d’accueil, choisir **Add / Remove Test Cases**
            2. Sélectionner le scénario de test créé précédemment
            3. Cliquer sur **Add / Remove selected**
        3. Il n’est pas nécessaire de créer un nouveau build dans TestLink pour chaque exécution de test : Jenkins s’en chargera pour nous à chaque fois qu’un build sera lancé

1. **Installer et configurer le plugin TestLink dans Jenkins.**
    1. Installer le plugin **TestLink** dans Jenkins.
    2. Configurer le plugin : aller dans la **Configuration du système** de Jenkins et configurer la section TestLink.
        1. On prendra soin de bien remplir la clé d’accès à l’API de TestLink définie à l’étape précédente


1. **Créer un nouveau job dans Jenkins** utilisant les sources de l’exemple. Dans la phase de **Build**, on ajoutera un unique step **“Invoke Test Link”** avec la configuration suivante :
    1. Test Project Name : utiliser le nom du projet créé dans TestLink
    2. Test Plan Name : utiliser le nom du plan créé dans TestLink
    3. Build Name : choisir un nom de build. Pour garder un historique des exécutions, on pourra utiliser un nom de build paramétré, par exemple : **build-$BUILD_NUMBER**
    4. Dans les champs **Custom Fields** et **Test Plan Custom Fields**, ajouter le champ personnalisé créé dans TestLink (par exemple : java_class)
    5. Sans quitter la configuration du step TestLink, ajouter un sous-step Maven dans la section Test Execution. Exécuter les cibles **clean test**
    6. Ajouter une extraction des résultats de tests JUnit : dans la section **Result Seeking Strategy**, ajouter une stratégie **JUnit Class name** avec la configuration suivante :
        1. Dans **Include Pattern**, ajouter : **target/\*\*/TEST-\*.xml**
        2. Dans **Key Custom Field**, ajouter le champ personnalisé créé dans TestLink (par exemple : java_class)
2. **Lancer un build du job Jenkins**. Vérifier que les résultats de TestLink sont bien intégrés dans la page du projet dans Jenkins :


1. **Ajouter l'intégration des autres tests du projet dans TestLink.**

Pour plus d’information sur l’intégration de TestLink dans Jenkins : <https://plugins.jenkins.io/testlink/>

## Exemple 14. Tests d’interface utilisateur

Dans cet exemple, nous allons utiliser Jenkins pour réaliser des tests d’interface utilisateur sur une application existante. Nous utiliserons Sélénium pour réaliser les tests et TestLink pour les rapports de tests.

1. Choisir une application Web à tester (par exemple : [https://fr.wikipedia.org](https://fr.wikipedia.org/) ).
2. Créer des tests d’interface utilisateur en utilisant l’outil de test d’interface graphique Sélénium. On pourra :
    1. Intégrer directement Sélénium dans le framework de tests JUnit
    2. Ou bien : utiliser un framework procurant une abstraction au-dessus de Sélénium (par exemple : Geb <https://gebish.org/> )
3. Intégrer l’exécution des tests Sélénium dans Jenkins. On utilisera une matrice de tests pour réaliser des tests sur différents navigateurs : Edge, Firefox, Google Chrome
4. Intégrer les rapports de tests dans TestLink

:::tip
Dans la pratique, il est courant d’utiliser un dépôt de code dédié et séparé des sources pour les tests d'interface graphique (et/ou tous les tests d’intégration)
:::

## Exemple 15. Intégration des outils d’analyse statique

Dans cet exemple, nous allons intégrer dans Jenkins les rapports des outils d’analyse statique générés par des tâches dédiées des outils de build, par exemple Maven, Gradle, NPM.

1. Vérifier que l’exemple de code intègre bien les outils d’analyse statique directement dans l’outils de build Gradle (ficher build.gradle ) pour y ajouter les plugins d’intégration continue spotbugs, pmd, cpd et checkstyle.
2. Créer un nouveau job dans Jenkins exécutant les tâches Gradle correspondant à ces outils
3. A l’aide des plugins correspondants dans Jenkins, intégrer les rapports de qualité (par exemple : spotbugs, pmd, cpd, checkstyle) dans le job du projet

On pourra utiliser la documentation : <https://jenkins-le-guide-complet.github.io/html/sect-code-quality-tools.html>
