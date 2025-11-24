---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Outils d'intégration continue
layout: '@layouts/CoursePartLayout.astro'
---

## 🎯 Objectifs

- Comprendre et utiliser les différents outils de l'intégration continue 🧠
- Automatiser les processus de build, de test et de déploiement 🤖
- Améliorer la collaboration entre les équipes de développement et d'exploitation 🤝
- Réduire les erreurs humaines et les temps de feedback ⏳
- Utiliser des gestionnaires de versions pour centraliser le code source 💾

---

## ⚙️ La compilation

- 🏗️ Génère le binaire à livrer en production depuis le code source.
- ✅ Dans le cas d'un langage compilé, la compilation est le premier garant du respect de la norme du langage. Le compilateur permet, au moment de générer le binaire, de vérifier à la fois la syntaxe et (dans une moindre mesure) la sémantique du code, et d'apporter des explications et conseils sur les changements à opérer.

_💡 Par exemple, le respect de la norme Java est garanti par le compilateur qui tourne dans l'IDE._

---

- 🔁 Afin d'être certain de vérifier le même objet, un commit ne devrait au mieux n'être compilé qu'une seule fois et l'artéfact généré ne pas être modifié (architecture immuable).
- 🐳 En principe, cette contrainte est difficile à respecter sans déployer un environnement complet : `Docker`
- ⏱️ On limitera donc au maximum le nombre de compilations du même commit (ex : tests + packaging en 1 seul build)

---

### 🔁 Transpilation et compilation croisée

- 🔐 Pour pallier à un manque d'analyse dynamique dans le binaire de destination on pourra utiliser des langages moins permissifs, transpilés vers le langage de destination.
- 🧠 Ces langages, par une grammaire plus stricte et une analyse statique du code source, garantissent que les problèmes non vérifiés à l'exécution ne peuvent pas survenir (ou moins) au vue de la qualité du code source.

---

_💡 Par exemple, `TypeScript` est transpilé en `EcmaScript` mais garantit la vérification des types sur les variables (ce que `EcmaScript` ne garantit pas)._

_🔄 À l'inverse, il est possible d'exécuter du code directement dans les machines virtuelles en respectant leurs contraintes, mais pas celles du langage de base. Par exemple, `Kotlin™` peut être compilé en bytecode exécutable sur la JVM, même s'il ne respecte pas toutes les contraintes de la norme `Java`._

---

## 🛠️ Les outils de build

`Makefile`, `Apache Maven`, `Gradle`, `npm`, `Webpack®`

- 🏗️ Compilent le code source pour créer les binaires
  - 🔄 Peuvent aussi transpiler le code source vers un autre format : `TypeScript`, ...
  - ⚙️ Peuvent optimiser le code pour la production : obfuscation, minimisation, ...
- 📦 Gèrent éventuellement les dépendances.

---

- ✅ Intègrent souvent la gestion des tests unitaires.
- 🚀 Peuvent parfois déployer les artéfacts produits.
- 📋 Tous les outils de build permettent une utilisation au travers de règles (compiler, déployer, tester, etc.)

---

## 🧪 Les tests unitaires

`Junit`, `phpUnit`, `TestNG`

- 🧩 Ils contrôlent et valident l'implémentation du code au niveau des fonctions ou des classes sans se préoccuper de l'application globale.
- 🛑 Très utiles pour détecter les régressions.
- 🧍‍♂️ Cette isolation minimise les problèmes d'intégration

Voir le [🧪 cours sur les tests unitaires](/tests#tests-unitaires)

---

- ⚡ Ils doivent être le plus rapide possible car ils vont tourner souvent !
- ⏱️ Exemple : `< 1 min` pour tous les tests unitaires.
- 🔀 On essaiera de paralléliser les tests au maximum.

---

## 🗂️ Les outils de versionning

Versionner son code source permet :

- 🧭 D'identifier, isoler et documenter les changements apportés dans le code
- 🔁 De visualiser l'historique des changements et opérer un retour arrière
- 🤝 D'intégrer des changements, y compris de manière concurrente et non linéaire

---

`Git` (très majoritaire), `SVN`, `Mercurial`

Voir le [📘 cours sur le gestionnaire de versions Git](/git)

---

## 🧹 Les outils d'inspection du code

- 📊 Génèrent des rapports sur la qualité du code et les points à revoir : couverture de tests, anti-pattern, ...
- 🛠️ Peuvent proposer des corrections de code : bugs, erreur classiques
- 🔍 Permettent de tester la généricité du code, sa documentation, les performances (profiling), le code obsolète, les mauvaises habitudes, le code mort, ...

---

- 🧑‍💻 Utiles au développeur pour améliorer sa technique et ses habitudes de programmation
- ✅ Utiles pour la recette qualité d'un projet grâce au reporting.

---

### ✨ Vérification de style

`Checkstyle`

- 📐 Garanti le respect de bonnes pratiques et l'utilisation d'une grammaire commune.
- 👀 Le code source devient cohérent et lisible facilement par tous.
- 🧩 Limite les opérations de merge inutiles : sauts de ligne non cohérents, ...
- 🔍 Facilite la revue de code.

---

⚠️ Un outil de contrôle du style ne vérifie que la syntaxe (i.e. si le style du code est correct), pas la sémantique. Le sens du code écrit n'est donc pas validé (la variable existe-t-elle, ...)

---

#### 🧾 Exemple 1

_En `Java`, il est d'usage d'écrire les constantes en majuscule, même si ce n'est pas une contrainte de la norme (le code compile quand même)._

Les 2 lignes suivantes sont équivalentes, mais il est beaucoup plus simple de maintenir un code qui suit des pratiques communes :

```java
public static int COEFF_ADDITION = 2; // ✅
```

```java
public static int coeffAddition = 2; // ❌
```

---

#### 🧾 Exemple 2

Les 2 extraits de code suivants sont équivalents, mais si les développeurs n'utilisent pas le même standard de code, le merge du code source risque d'être beaucoup plus compliqué :

```java
int addition(int i) {
 return i + COEFF_ADDITION;
}
```

```java
int addition( int i )
{
 return i+coeffAddition;
}
```

---

#### 💡 Utilisation dans un IDE

_Il peut être très utile de mettre en place un outil de vérification de style dans l'IDE. On pourra par exemple utiliser le plugin Checkstyle de QAPlug et utiliser le coding-style de Google qui est l'un des plus utilisés dans la communauté._

_On pourra également utiliser les fonctions de formatage de code de l'IDE pour appliquer automatiquement ces contraintes de style dans la suite du développement._

---

## 🧠 Analyse sémantique

`Linter`, `Spotbugs`, `PMD`

- 🔍 L'analyse **statique** de code (parfois appelée _linter_) permet de vérifier la sémantique, c'est-à-dire la cohérence du modèle décrit, dans le code source et/ou les binaires.
- ⚙️ L'analyse **dynamique** (sur le code exécuté) et l'analyse statique (sur le code source ou le binaire avant exécution) n'ont donc rien à voir, même si les vérifications peuvent parfois être redondantes (mais nécessaires).

---

### 🔎 Analyse statique de code source : `PMD`

Pour s'assurer de la qualité du code produit, on peut procéder à une analyse statique directement sur le code source pour vérifier certains paramètres :

- ✅ le code respecte-t-il la norme du langage ?
- 🔁 y a-t-il des duplications de code ? du code mort ?

---

- 💡 Cette analyse est possible sur tous les langages, qu'ils soient compilés ou interprétés, y compris les framework frontend et les pseudo langages descriptifs tels `HTML` ou `YAML`.
- 🛠️ `PMD` est un ensemble d'outils d'analyse statique du code source (principalement pour Java) vérifiant le bon respect de la norme ainsi que des bonnes pratiques de développement pour minimiser la dette technique du projet.
- 🌐 Le [Validateur W3C](http://validator.w3.org/) est un outil d'analyse statique du code `HTML` d'un site.
- 🧪 [Mozilla Observatory](http://observatory.mozilla.org/) est un site d'analyse statique qui va vous donner beaucoup d'information sur les headers de sécurité de votre site internet.

---

### 🧬 Analyse statique de bytecode (binaire) : `SpotBugs`

- Certains langages étant compilés avant leur exécution, il peut être intéressant de s'intéresser directement à la qualité du livrable (binaire) qui sera lancé.
- 🧐 Il est possible pour cela de réaliser une analyse statique sur le bytecode généré avant son exécution.
- 🎯 L'analyse du bytecode à exécuter permet une analyse très fine des problèmes dans le code.

---

- 😕 Cependant, il peut être difficile de corréler ces problèmes avec le code source, ou de détecter de mauvaises pratiques comme le copier-coller car le bytecode généré peut être différent.
- 🛠️ `SpotBugs` est un outil d'analyse statique de bytecode `Java`.
- 🎯 Son but est de trouver des éventuels problèmes dans les fichiers `.class` `Java` en identifiant des ensembles d'instructions connus comme étant des patterns de bugs.

---

## 🚦 Analyse dynamique de binaire : les interpréteurs, la JVM

- 💻 Certains langages ne sont pas exécutés directement en langage machine (assembleur), mais sont interprétés (ou compilés puis exécutés) dans des machines virtuelles.
- 🔁 Par exemple, `Python` ou `EcmaScript` sont interprétés dans des machines virtuelles exécutant les instructions du code source directement, alors que le code source `Java` est compilé en bytecode, ensuite exécuté dans une machine virtuelle (`JVM`).

---

- ✅ Permet de vérifier la cohérence du modèle du code en cours d'exécution :
  - 🧮 Les variables et fonctions appelées sont-elles bien définies ?
  - 🔢 Les types des variables sont-ils corrects ?
- 🛡️ Garanti la sécurité du code exécuté contre :
  - 🚫 Les attaques basées sur une incohérence dans le code exécuté : `buffer overflow`, ...
  - 🔒 Les accès inapropriés (accès aux champs privés d'une classe) détectés par la machine virtuelle et refusés.

---

- 📈 Les analyses dynamiques de code sont beaucoup plus poussées sur certains framework backend, qui sont les seuls à bénéficier d'une machine virtuelle puissante.
- 💡 Il serait beaucoup trop couteux (en terme de ressources) à déployer sur un client léger.

---

- 🔧 L'analyse dynamique est rarement configurable : elle est soit incluse dans l'interpréteur ou la machine virtuelle du langage, soit absente (notamment pour un langage compilé directement en langage machine).
- 💬 Le choix du langage de programmation est donc déterminant à cette étape.

---

- 🧪 Dans un cadre d'intégration continue, le code est exécuté pendant la phase de test : c'est donc elle qui sera la garante de cette étape, d'où l'importance de tester **toutes** les classes du projet !

---

## 🧰 Les autres outils : quelques exemples

---

### 📚 Documentation du code

La documentation du code (`Javadoc`, ...) permet de décrire les contrats utilisés dans le code.

---

### 🔍 Revue de code

Les outils de revue de code (`Reviewboard`, outils natifs des hébergeurs de code source `Bitbucket`, `Gitlab`, `Github`, ...) permettent aux développeurs de partager leurs modifications et d'en discuter ensemble, avant leur intégration dans le tronc commun

---

### 🛠️ Serveurs d'intégration continue

Les serveurs d'intégration continue permettant le respect de pipelines d'intégration : `Bitbucket`, ...

---

### 📈 Serveurs d'analyse de la qualité

Les serveurs d'analyse continue de qualité (`SonarQube`, `Jenkins`, ...) permettant l'analyse et le suivi de la qualité globale d'un projet.

---

### 🔄 Mise à jour des dépendances

Des outils comme `dependabot` (pour _Github Actions_) permettent de créer une pull request automatiquement avec la mise à jour des dépendances

---

### 🛡️ Détection de vulnérabilités

- `gitleaks` recherche des vulnérabilités dans un dépôt Git (mots de passe en clair, …)
- `Trivy` / `Grype` : Scan d'images Docker, dépendances, dépôts Git pour vulnérabilités (CVE).
- `r2devops` / `regula` permettent d'auditer le code à la recherche de CVE
- `Snyk` : Analyse de dépendances + suggestions de correction.
- `Gitleaks` : Détection de secrets/API keys dans le code.
- `OWASP ZAP` : Test d'intrusion automatisé des APIs/web apps.
- `Dependency-Track` : Gestion du _SBOM_ (_Software Bill of Materials_).

---

### 🧪 Tests et validation avancée

- `Testcontainers` : Tests d'intégration avec environnements temporaires (BDD, services).
- `k6` / `JMeter` : Tests de charge et de performance.
- `Selenium` / `Cypress` / `Playwright` : Tests end-to-end pour front et API.
- Mutation Testing (`PIT`, `Stryker`) : Vérifie la robustesse des tests unitaires.

---

### 📜 Conformité et gouvernance

- _Open Policy Agent_ (`OPA`) : Validation de règles (policies) dans le pipeline.
- `Conftest` : Contrôle d'infra-as-code (Terraform, K8s YAML) contre des règles internes.
- `Terraform Compliance` / `Checkov` : Analyse IaC pour conformité et sécurité.

---

### 🚀 Optimisation de l'artefact et déploiement

- `Docker Slim` : Minification des images Docker.
- `Kaniko` / `BuildKit` : Builds plus rapides et sécurisés.
- `Helm` + `chart-testing` : Validation des chartes Helm avant déploiement.
- `Argo CD` / `FluxCD` : Déploiement GitOps.

---

### 🔍 Autres linters / analyse statique

- `CodeQL` (GitHub) ou `Semgrep` : Analyse statique orientée sécurité.
- `Hadolint` : Analyse des Dockerfiles pour bonnes pratiques et sécurité.

---

:::link
Voir aussi [la liste des outils CI/CD sur le site web](/tools#-cicd)
:::

---

## 🚀 Déploiement des outils

Ces outils sont le noyau dur de l'intégration continue, et ceux que l'on essaiera de déployer au maximum dans les différents environnements :

- 🛠️ Serveur d'intégration continue
- 💻 Environnement de développement
- 🧪 `staging` / `pre-production` / (rarement) `production`

---

## Bonnes pratiques & Optimisations

---

### 🎯 Objectifs

- Augmenter la **fiabilité** des livraisons
- Réduire le **temps de cycle**
- Détecter les erreurs **tôt**
- Assurer la **traçabilité** et la **reproductibilité**

---

### 🏗️ Structuration des pipelines

- **Diviser par étapes** (build, test, analyse, déploiement)
- **Utiliser des jobs parallèles** pour les tests ou validations
- **Séparer CI et CD** : pipelines distincts ou étapes conditionnelles

---

### 🧹 Qualité et sécurité du code

- Lancer automatiquement :
  - ✅ **Analyse statique** (SonarQube, eslint, etc.)
  - ✅ **Tests unitaires et d'intégration**
  - ✅ **Scan de vulnérabilités** (Snyk, Trivy, etc.)
  - ✅ **Lint / Formatage**
- Bloquer les fusions Git (`merge`, `rebase`) si les tests échouent
- Garder le code dans un **état toujours déployable**

---

### ⚡ Performance des pipelines

- Utiliser des **stratégies de cache**
- Réutiliser les artefacts entre jobs
- Ne pas reconstruire ce qui n'a pas changé
- Utiliser des runners dédiés pour les projets gourmands

---

### 📦 Gestion des artefacts

- Versionner les artefacts de build
- Publier dans des registres privés/publics :
  . _Docker Registry_
  . _NuGet_, _npm_, _PyPI_, etc.
- Stocker les artefacts dans un système compatible CI/CD (ex : _GitLab_, _GitHub Releases_, _Nexus_, _Artifactory_)

---

### 🔒 Sécurité de la chaîne CI/CD

- Ne **jamais stocker de secrets en clair**
  - Utiliser des secrets managers (_Vault_, GitHub/GitLab secrets, etc.)
- Restreindre les droits sur les runners et pipelines
- Exécuter dans des environnements isolés
- Utiliser des **signatures d'artefacts** (ex : _Sigstore_)

---

### 🧪 Tests et validation

- Tester **toutes les branches** de travail si possible
- Intégrer des **tests end-to-end (E2E)** si pertinent
- Utiliser des **environnements éphémères** pour le **staging**
- Mettre en place des **revues de code obligatoires**

---

### 🚀 Déploiement

- Déployer automatiquement sur :
  - un environnement de staging
  - un environnement de production, après validation manuelle
- Suivre les modèles de CD :
  - **Blue/Green**, **Canary**, **Rolling Update**
  - Voir le cours associé aux modèles de déploiements continus
- Utiliser l'**Infrastructure as Code** pour les déploiements

---

### 🧭 Observabilité & suivi

- Intégrer des outils de monitoring/logging :
  - _Prometheus_ / _Grafana_ / _Loki_
  - _Elastic_ / _Kibana_
- Envoyer les métriques de pipeline (temps de build, erreurs)
- Activer des alertes sur échec de pipeline :
  - Mail, _Slack_, …

---

### 📘 Documentation et maintenance

- Documenter la structure du pipeline CI/CD :
  - Schéma global si le pipeline cumule plusieurs outils (_Github_ + _Jenkins_, …)
  - Workflow de travail _Git_ associé
- Garder les fichiers `.gitlab-ci.yml`, `.github/workflows/*.yml` ou `Jenkinsfile` **clairs et modulaires**
- Mettre à jour régulièrement les versions d'outils (runners, langages, actions)
- Mettre en place des **tests de pipeline** sur branches temporaires

---

### Focus sur le caching

#### 🎯 Objectifs

- 🚀 Réduction du temps des builds
- 📦 Éviter le téléchargement répétitif des dépendances
- 🔁 Réutilisation de résultats intermédiaires
- 🌍 Moins de requêtes vers des dépôts distants

---

#### Exemple: Caching NuGet

```yaml
#.github/pipeline.yml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Cache NuGet packages
        uses: actions/cache@v3
        with:
          path: ~/.nuget/packages
          key: nuget-${{ hashFiles('**/*.csproj') }} # change si les dépendances changent
          restore-keys: | # fallback
            nuget-

      - name: Restore dependencies
        run: dotnet restore
```

```yaml
#.gitlab-ci.yml
cache:
  key: "$CI_COMMIT_REF_SLUG"
  paths:
    - .nuget/packages/

before_script:
  - dotnet restore
```

---

## Framework SLSA

- Objectif : Garantir l'intégrité des artefacts logiciels pour éviter les attaques sur la chaîne d'approvisionnement (_supply chain_) logicielle.
- SLSA 1 : CI/CD entièrement automatisé et metadata de provenance.
- SLSA 2 : Gestionnaire de version, CI/CD hébergée en ligne et provenance authentifiée.
- SLSA 3 : Normes spécifiques pour auditabilité de la source et intégrité de la provenance.
- SLSA 4: Revue de toutes les modifications par deux personnes, CI/CD hermétique et reproductible.

Pour plus d'information, voir : <https://blog.stephane-robert.info/docs/securiser/supply-chain/slsa/>

---
