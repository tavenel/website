---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Introduction à l'intégration continue
layout: '@layouts/CoursePartLayout.astro'
---

```mermaid
mindmap
  root((Intégration Continue))

    Principes
      Développement itératif
      Intégration fréquente du code
      Tests automatisés à chaque changement

    Objectifs
      Détection rapide des erreurs
      Qualité du code
      Réduction du coût de correction
      Déploiement plus rapide

    Étapes Clés
      Commit du code
      Déclenchement du pipeline
      Compilation
      Exécution des tests
      Analyse statique
      Packaging
      Notification des résultats

    Outils Populaires
      Jenkins
      GitLab CI
      GitHub Actions

    Tests
      Unitaires
      Intégration
      Fonctionnels
      End-to-end

    Qualité du Code
      Analyse statique - SonarQube
      Linting
      Couverture de code
```

---

## ⚠️ Problèmes courants

- Lenteur des déploiements manuels ⏳
- Erreurs humaines fréquentes au déploiement : ❌
  - Configurations incorrectes ⚙️
  - Oublis de fichiers, … 📄
  - Besoin d'interventions d'urgence 🚨
- Modifications difficiles à suivre : 🔄
  - Quelle version en production ? 🏷️
  - Quels changements sur la production ? 🔍
  - Conflits de dépendances 🔄
- Tests non systématiques ❌
- Pas de communication entre dev et ops 📞

---

## 🔄 Intégration continue

> Ensemble de pratiques consistant à vérifier que chaque modification du code source ne produit pas de régression 🔄

---

> Continuous Integration is a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily – leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible. Many teams find that this approach leads to significantly reduced integration problems and allows a team to develop cohesive software more rapidly. Martin Fowler, ThoughtWorks Chief Scientist

---

## 🔄 Shift Left

La CI se positionne dans une stratégie **Shift Left** : 🔄

- Pratique qui consiste à intégrer les tests et la gestion des connaissances dans les étapes initiales du développement logiciel (plutôt que tardivement dans le processus de production). 🔄
- Objectif : détecter et corriger les bugs et les erreurs dès les premières étapes du développement 🐛

---

## 🌟 Avantages

---

### 🔄 Feedback loop réduite

- Spécifications ✅
  - Les spécifications sont validées plus tôt ✅
- Build 🏗️
  - Le build est testé plus tôt ✅
- Erreurs ❌
  - Les erreurs sont détectées plus tôt ❌
- Intégration 🔄
  - L'intégration est testée plus tôt 🔄

---

### 🤝 Facilite le travail collaboratif

Les changements concurrents sont validés contre une éventuelle régression 🔄

---

## ❌Inconvénients de l'intégration continue

---

- Demande de grosses ressources humaines à la mise en place et matérielles à l'usage 💼
  - Mais le gain est souvent vite compensé par les erreurs en moins à corriger ! ✅
- Peut être compliqué sur de gros changements : la CI nécessite d'intégrer souvent les changements sur le serveur… 🔄
  - … ce qui peut aussi être un avantage pour vérifier tôt la compatibilité ! ✅
- Peu adapté à certains environnements où les spécifications changent souvent (Proof of Concept, Recherche, ...) ⚠️

---

- Respecter une méthodologie stricte d'intégration continue demande beaucoup de rigueur 📏
  - Il peut être nécessaire de vérifier le respect de ces méthodes, manuellement ou automatiquement 🔍
- Le principal défaut est souvent humain ! 👥

---

# 🔄 Pipelines d'intégration continue

---

## 📌 Définition

- Un pipeline d'intégration est une définition formelle du **processus** à suivre pour **intégrer** des changements. 📌
- Il est souvent représenté de manière graphique par un **schéma d'enchaînement d'actions**. 📊
- Ces pipelines peuvent être exécutés manuellement, mais ils seront aussi la référence utilisée pour l'automatisation et l'orchestration de l'intégration continue. 🔄

---

### Exemple simpliste de pipeline

```mermaid
---
title: Un pipeline CI/CD
---

graph LR
  subgraph Intégration continue
    Source-->Build-->Test
  end

  subgraph Déploiement continu
    Test-->Deploy
  end
```

---

On pourra utiliser plusieurs profils (_pipelines_) d'intégration suivant les changements à intégrer et les ressources disponibles, par exemple :

- `Daily` pour chaque intégration : tests unitaires uniquement
- `Nightly` chaque soir : tests de fonctionnalités non parallélisables
- `Weekly` chaque semaine : `staging` (copie environnement de production) pour scénarios complexes de tests de performances

---

:::tip

- On pourra répliquer certains éléments de la boucle d'intégration continue sur l'environnement du développeur pour améliorer les temps de réponse.
- Cela ne dispense pas de reproduire ces étapes sur le serveur d'intégration (environnement neutre).

:::

---

## Workflows Git

Les pipelines d'intégration continue sont fortement liés aux workflows de gestion du code source qui conditionnent les process de développement.

:::link
Voir le [cours sur le gestionnaire de versions Git](/git/).
:::

---

### Pull-request

- Popularisé par `GitHub®`, la `pull-request` ou `merge-request` est aujourd'hui largement répandue en gestion de projet.
- En théorie, simple demande de relecture de code avant l'intégration (`merge`) d'une branche dans une autre.
- En pratique : permet de prévenir l'équipe de la fin d'une partie du produit et engage le processus d'intégration, par exemple un pipeline d'intégration continue

---

### Process de pull-request

Étape optionnelle avant d'intégrer la branche de fonctionnalité au `main` du dépôt central :

1. `push` de la branche de `dev` dans le dépôt central
2. Validation des changements avant fusion : `pull-request`
3. Fusion dans `main` dans le dépôt central

---

- C'est généralement le point de départ du pipeline d'intégration continue.
- Sert de discussion avant l'intégration de changements : revue de code, vérification de la qualité, process administratifs, ...
- Approuvée manuellement par les développeurs ou automatiquement en fonction de critères qualité.

---

### Qualité du commit vs qualité de la pull-request

Il existe 2 grands schémas de lancement de pipeline d'intégration continue (et beaucoup de modèles mélangeant un peu de ces deux schémas) :

- Pour chaque commit : à privilégier pour les branches stables du projet, où chaque commit est critique : `master`, ...
- Au moment d'une pull-request : à privilégier pour les branches de travail instables : fonctionnalité, correction de bug, ...

---

### Qualité liée au commit

- Les interfaces de gestion de projets hébergés (`Github®`, `Bitbucket`, `Gitlab`, ...) peuvent parfois laisser croire que l'intégration continue a été réalisée sur la pull-request…
- …mais la référence utilisée est **toujours un commit** (celui qui sera utilisé pour le merge de la branche).
- `qualité de la pull request == qualité du commit de référence de la branche à intégrer`

---

```mermaid
---
title: Le processus de pull-request
---

graph LR
  subgraph Machine personnelle
    A1{{fa:fa-laptop-code Code, exécute, teste}}-->A2{OK?}-->|Oui|A3[fa:fa-code-branch Push branche fonctionnalité]
    A2-->|Non|A1
  end

  subgraph Serveur git distant
    A3-.->B1[(fa:fa-code-pull-request Serveur CI)]--Analyse qualité-->B1
    B1-->B2{{Revue de code}}-->B3{OK?}-->|Oui|B4[fa:fa-code-merge Merge dans main]
    B3-->|Non|A1
  end

```

---

# 📌 Grands principes de l'intégration continue

- Centralisation du code 💾
- Commit réguliers 🔄
- Automatisation des build 🤖
- Compilations auto-testantes 🧪

---

## 💾 Centralisation du code : le gestionnaire de versions

- Segmente les modifications du code source en `commits` et les identifie par des ID de commit. 🏷️
- Garantit l'intégrité : permet le partage fiable des modifications entre tous les développeurs. 🔄
- Référence du contrôle qualité : toute métrique d'intégration continue est faite contre un commit. 🔍

---

Exemples : `git`, `mercurial`, `svn` et leurs serveurs hébergés : `github`, `bitbucket`, `gitlab`, ... 🌐
Certains gestionnaires de versions permettent d'isoler du tronc commun les modifications dont la qualité n'est pas encore suffisante : branches `git`, ... 🌿

---

## 🔄 Commit réguliers

- But intégration continue : réduire au maximum le temps de feedback. ⏳
  - Intégrer les plus petits changements possibles. 🔄
  - Intégrer le plus souvent possible. 🔄
- En principe : intégration continue si `> 1 intégration (commit) par jour`. 📅

---

## 🤖 Automatisation des build

- Nécessaire pour une analyse et validation automatique de la qualité : ✅
- Pas d'intervention manuelle sur l'intégration continue. ❌
- Mais processus manuel possible, par exemple si changements critiques et concurrents entre 2 développeurs. 👥
  - Ces intégrations manuelles sont à exécuter **avant** l'intégration continue - qui validera donc l'ensemble de ces changements ✅

---

## 🧪 Compilations auto-testantes

- Les outils de build permettent l'exécution de certains outils d'intégration continue : tests, vérification syntaxique, … directement durant la phase de build 🛠️
- Permet d'exécuter le même outil avec la même configuration à toutes les étapes du pipeline d'intégration : machine personnelle, serveur d'intégration, … 🖥️
- Une modification du code source ne passant pas l'étape de compilation est en général immédiatement rejetée et la boucle d'intégration continue s'arrête. ❌

---

Lancement de l'outil automatiquement par l'outil de build : pas de programme externe et pas d'oubli de lancer l'outil. 🔄
Ex : `gradle build` ou `mvn package` intègrent par défaut l'exécution des tests unitaires. 🧪

---

```mermaid
---
title: Processus d'intégration continue.
---
flowchart TD
    subgraph DevMachine["Machine du développeur"]
        CompileUnitTests["Compilation et tests unitaires"]
        CommitChanges["Intégration des changements dans le dépôt de code"]
        CompileUnitTests --> CommitChanges
    end

    subgraph CI_Server["Serveur d'intégration continue"]
        CompileProdCode["Compilation code de production"]
        DisplayResults["Affichage des résultats"]
        CommitChanges --> CompileProdCode
        CompileProdCode --> DisplayResults
    end
```

<div class="caption">Exemple de processus d'intégration continue</div>

---

## 🏗️ Déploiement continu (_Continuous Deployment_)

- Le mouvement DevOps favorise de plus en plus un processus opérationnel entièrement automatisé. 🏗️
- La CI devient une vérification entièrement automatisée dans le pipeline de déploiement. 🔄
- Si succès : l'artéfact généré est déployé automatiquement en production. 🏗️

---

:::tip
Cette méthode opérationnelle est très efficace car elle est entièrement automatisée. Cependant, il est nécessaire de pouvoir agir très rapidement sur la production pour pouvoir fixer d'éventuels problèmes non détectés par le processus automatique.
:::

---

## 🏗️ Livraison continue (_Continuous Delivery_)

En pratique, on ajoute souvent une étape de validation manuelle avant le déploiement en production : on effectue alors uniquement la livraison dans un environnement d'intégration / pré-production. Ce modèle s'appelle la livraison continue (_continuous delivery_) et est souvent le terme abrégé par `CD` dans la `CI/CD`. 🏗️

---

## 📌 Méthodologies et gestion de projet

---

### 🧩 Découpage en composants

- Permet une exigence qualité différente pour chaque composant. 🛠️
- Facilite la non régression en testant les composants isolément. 🔄
- Permet d'identifier des zones de haute qualité vs des zones à améliorer. 📊

---

### 🔄 Développement itératif

- L'intégration a lieu bien plus tôt dans la phase de développement. 🔄
- Les itérations facilitent l'acceptation ou le rejet des changements. 🔄
- Très compatible avec les méthodes agiles. 🔄

---

### 🤝 Responsabilité partagée

- L'intégration continue peut être mise en place à tous les niveaux du pipeline d'intégration : 🔄
  - Chez les développeurs (IDE) 💻
  - Chez les opérationnels (serveur d'intégration) 🏗️

---

## Actionnabilité

- Besoin d'**actionnabilité** après erreur dans le pipeline
- Définir la **gouvernance** : qui est responsable de quoi ?
- Sinon : plus de confiance dans la CI/CD

---

| Catégorie            | Fréquence de Déploiement (vitesse) | Délai d'exécution des modifications (vitesse) | Temps moyen pour restorer (stabilité) | Taux d'erreurs lors de changements (stabilité) |
|--------------------|---------------------|---------------------|----------------------|--------------------|
| Elite performers    | > 1/jour (à la demande) | < 1 jour            | < 1 heure           | 0 - 15%            |
| High performers    | 1/jour - 1/semaine  | 1/jour - 1/semaine | < 1 jour            | 0 - 15%            |
| Medium performers  | 1/semaine - 1/mois  | 1/semaine - 1/mois  | < 1 jour            | 0 - 15%            |
| Low performers     | 1/mois - 1/6 mois   | 1/mois - 1/6 mois   | 1 semaine - 1 mois  | 46 - 60%           |

---

## Promotion Pipelines

- _Promotion Pipelines_ : Passage d'un environnement de test -> staging -> … -> prod
- Configuration des **différents environnements** : utiliser des **fichiers / répertoires** dédiés (~pas de branches Git par environnement~)
- Valeurs **par défaut** : **production** (évite d'envoyer des conf de dev en prod)

:::link

- <https://dev.to/codefreshio/how-to-model-your-gitops-environments-and-promote-releases-between-them-1p6i>
- <https://developers.redhat.com/articles/2022/07/20/git-workflows-best-practices-gitops-deployments>
- <https://codefresh.io/blog/stop-using-branches-deploying-different-gitops-environments/>

:::

```mermaid
---
title: Promotion Pipelines
---
flowchart
  %% Actors & repo
  Dev["fa:fa-code-branch Repo Git
  (fichiers IaC: Terraform + app/Dockerfile)"]
  Dev --> CI["fa:fa-gitlab Pipeline CI/CD
  (GitLab CI / GitHub Actions)"]

  %% Build & registry
  subgraph CICD [CI / CD]
    CI --> Build["fa:fa-docker Build image Docker"]
    Build --> Registry["fa:fa-docker Docker Registry
    (image: myapp:123)"]
  end
  
  %% Common IaC code
  CI --> TF_PLAN["fa:fa-file-code Terraform plan
  (même code Terraform)"]

  %% Remote state / vars
  RemoteState["fa:fa-database Backend remote
  (ex: S3 + lock)"]
  TF_PLAN -.-> RemoteState

  %% Integration stage
  subgraph INT [Intégration / Test]
    TF_INT[fa:fa-file-code Terraform apply workspace=integration vars=integration.tfvars]
    TF_PLAN --> TF_INT
    TF_INT --> Deploy_INT["fa:fa-server Déployer infra & app (image: myapp:123)"]
    Registry -.-> Deploy_INT
    Deploy_INT --> Tests_INT["fa:fa-vial-circle-check Tests automatisés
    (unit / intégration)"]
  end

  
  %% Promotion decision
  Tests_INT --> Promote{Promotion : Tests OK ?}
  Promote -.- non[fa:fa-x non] -.-> Fix[fa:fa-code-branch Retour dev
  nouveau commit]
  Fix -.-> Dev
  Promote -.- oui[fa:fa-check oui] -.-> TF_PRE[fa:fa-file-code Terraform apply workspace=preprod vars=preprod.tfvars]

  %% Staging stage
  subgraph STAGING [Staging]
    TF_PRE --> Deploy_PRE["fa:fa-server Déployer infra & app
    (image: myapp:123)"]
    Registry -.-> Deploy_PRE
    Deploy_PRE --> Tests_PRE[fa:fa-vial-circle-check Smoke tests
    e2e]
    Tests_PRE -.-> Approval{Promotion : Approval Gate manuel ou automatisé}
  end

  Approval -.-> TF_PROD[fa:fa-file-code Terraform apply workspace=production vars=prod.tfvars]

  %% Production stage
  subgraph PROD [Production]
    TF_PROD --> Deploy_PROD["fa:fa-server Déployer infra & app (image: myapp:123)"]
    Registry -.-> Deploy_PROD
    Deploy_PROD --> Monitoring[fa:fa-bell Monitoring, Alerts, Rollback]
  end
```

---

## Sécurité de la Supply Chain

La "Supply Chain" est devenue ces dernières années un vecteur stratégique en cybersécurité. Les exemples ci-dessous montrent la diversité de ces attaques (open source, cloud, AI/ML) et ont mis en lumière l'importance de sécuriser chaque maillon de la chaîne logicielle (pipelines CI/CD), de renforcer l'authentification multi-facteurs et de surveiller activement les dépendances logicielles.

---

### Attaque NPM

En 2025, l'écosystème _npm_ a été frappé par une attaque majeure de la chaîne d'approvisionnement (supply chain), liée à une mauvaise configuration de pipeline et à une compromission de comptes de mainteneurs.

---

#### Origine de la vulnérabilité

Le 8 septembre 2025, des attaquants ont compromis les comptes _npm_ de plusieurs mainteneurs de packages populaires (comme `chalk`, `debug`, `ansi-styles`, `strip-ansi`) via une campagne de phishing sophistiquée. Ils ont utilisé une technique d'_Adversary-in-the-Middle_ (_AitM_) pour voler les identifiants, mots de passe et jetons 2FA, puis ont publié des versions malveillantes de 18 packages, totalisant plus de 2 milliards de téléchargements hebdomadaires.

La compromission initiale est survenue à cause d'une mauvaise configuration des workflows GitHub (notamment l'utilisation du déclencheur `pull_request_target`). Ce déclencheur accorde des permissions élevées (écriture via `GITHUB_TOKEN`) aux pull requests externes, permettant à une PR malveillante d’exécuter du code arbitraire et d’injecter du malware dans les packages qui a permis à des pull requests malveillantes d'exécuter du code avec des permissions élevées, facilitant l'injection de malware [source](https://cybercare-nantes.fr/attaque-chaine-npm-identifiants-derobes-nx/).

- Les versions malveillantes contenaient du code JavaScript obfusqué conçu pour intercepter les transactions cryptomonnaies et voler des informations sensibles.
- Le malware était capable de se propager automatiquement : il scannait les environnements compromis, modifiait les fichiers `package.json`, injectait un script malveillant (`bundle.js`), puis republiait les packages infectés. Cela a permis de contaminer les pipelines CI/CD et de créer des portes dérobées persistantes dans les applications déployées. [source](https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2025-093/)
- Les attaquants ont envoyé des e-mails de phishing urgents, les incitant à mettre à jour leurs informations 2FA sur un faux domaine (_npmjs.help_).

---

#### Impact et réponse

- L'attaque a touché des milliers de développeurs et d'entreprises, avec un risque élevé de vol de tokens GitHub, de clés API et de données sensibles :
  - Plus de 2 300 secrets GitHub et cloud ont été dérobés via cette méthode, selon l’équipe Nx [source](https://cybercare-nantes.fr/attaque-chaine-npm-identifiants-derobes-nx/).
  - Plus de 180 packages npm compromis, avec un potentiel d'infection de millions d'utilisateurs et d'applications [source 1](https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2025-093/) [source 2](https://www.mend.io/blog/npm-supply-chain-attack-packages-compromised-by-self-spreading-malware/)
- Les équipes de sécurité ont recommandé de :
  - Mettre à jour les dépendances vers des versions sûres.
  - Auditer les pipelines CI/CD pour détecter tout comportement anormal.
  - Renforcer la surveillance et la protection des comptes mainteneurs.

---

### Porte dérobée XZ Utils (2024)

- **Cible** : La bibliothèque open source _XZ Utils_, utilisée dans de nombreuses distributions Linux.
- **Méthode** : Un développeur malveillant a intégré une porte dérobée dans le code source sur plusieurs années, permettant un accès distant aux systèmes infectés.
- **Impact** : Potentiel de compromission massive des serveurs Linux, détecté juste avant une diffusion large [source](https://xygeni.io/fr/blog/understanding-software-supply-chain-attacks/).

---

### Incident EventStream NPM (2024)

- **Cible** : Le package npm `EventStream`, utilisé par des milliers de projets.
- **Méthode** : Injection d'un code malveillant dans une dépendance peu surveillée, permettant le vol de données sensibles.
- **Impact** : Compromission de nombreuses applications dépendantes, illustrant le risque des dépendances transitives [source](https://xygeni.io/fr/blog/understanding-software-supply-chain-attacks/).

---

### Attaque via Typosquatting sur npm et PyPI (2024-2025)

- **Cible** : Développeurs utilisant des packages open source.
- **Méthode** : Création de faux packages (noms similaires à des bibliothèques populaires) pour tromper les utilisateurs et injecter des malwares comme le stealer _Windows Lumma_.
- **Exemple** : 14 000 faux packages sur npm pour exploiter un système de récompense en cryptomonnaie [source](https://www.cio-online.com/actualites/lire-supply-chain-logicielle-explosion-des-composants-open-source-malveillants-en-2024-15930.html).

---

### SolarWinds (2020)

- Compromission du logiciel _Orion_, touchant plus de 18 000 clients, dont Microsoft et des agences gouvernementales. [source 1](https://guardia.school/boite-a-outils/comprendre-ce-quest-une-supply-chain-attack.html), [source 2](https://xygeni.io/fr/blog/software-supply-chain-attacks-should-i-be-worried/)

---

### Attaques ciblant les modèles AI/ML (2024-2025)

- **Cible** : Plateformes comme _Hugging Face_.
- **Méthode** : Injection de modèles malveillants ou empoisonnement de données pour compromettre les systèmes d'IA.
- **Impact** : Augmentation de 6,5x des modèles malveillants en 2024, selon [JFrog](https://www.globalsecuritymag.fr/le-rapport-jfrog-software-supply-chain-state-of-the-union-2025-est-paru.html).

---

### Attaques Cloud et SaaS (2025)

- **Cible** : Infrastructures cloud et API de prestataires SaaS.
- **Méthode** : Exploitation des intégrations entre partenaires pour propager des malwares ou voler des données. [source](https://0xhack.fr/supply-chain-attack-2026-les-nouvelles-menaces-et-strategies-de-defense-a-connaitre/)

---

# Ressources

- Le site de référence de [Martin Fowler sur l'intégration continue](https://martinfowler.com/delivery.html)
- La [traduction en français du site précédent](https://skalp.developpez.com/traductions/martin-fowler-integration-continue/)
- Le livre sur l'intégration continue : [Continuous Integration](https://martinfowler.com/books/duvall.html)
- Le livre sur le déploiement continu : [Continuous Devilery](https://martinfowler.com/books/continuousDelivery.html)
- Intégration continue avec Gitlab CI : <https://gitlab.com/goffinet/gitlab-ci>
- [Exemple de pipeline Jenkins YAML en Infrastructure-as-Code][gist-jenkins-pipeline-yaml]
- [CD : Gestionnaires d'artéfacts - attaques supply chain](https://blog.wescale.fr/supply-chain-attack-proxies-gestionnaires-dartefacts-et-cartographie)
- [CD : attaques supply chain - livrables de confiance](https://blog.wescale.fr/supply-chain-attack-des-livrables-de-confiance)
- Le pipeline d'Actions Github du site Web du cours (<www.avenel.pro>) : <https://github.com/tavenel/website/actions>
- 🚀 Pour aller plus loin : le [cours sur les pratiques DevOps](/devops).

[gist-jenkins-pipeline-yaml]: https://gist.github.com/jonico/e205b16cf07451b2f475543cf1541e70

---
