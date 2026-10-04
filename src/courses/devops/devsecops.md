---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Le DevOps
layout: '@layouts/CoursePartLayout.astro'
---

## 🎯 Objectif

> **Comment construire et exploiter une chaîne de livraison dans laquelle la sécurité est intégrée à l'infrastructure, au CI/CD et aux déploiements ?**

## Fil conducteur

> **DevSecOps consiste à construire une chaîne de livraison dans laquelle les contrôles de sécurité sont automatisés, traçables et proportionnés au risque.**

Une démarche DevSecOps peut être résumée ainsi :

1. **Menace**
2. **Contrôle**
3. **Automatisation**
4. **Finding**
5. **Analyse du risque**
6. **Décision**

Un administrateur DevSecOps doit donc savoir :

- identifier une menace
- choisir un contrôle
- l'automatiser
- interpréter son résultat
- prendre une décision
- mesurer le résultat

Un outil de sécurité n'a de valeur que si l'on sait **quel risque il cherche à réduire, où il intervient et quoi faire de son résultat**.

## Du DevOps au DevSecOps

Une chaîne DevOps classique automatise :

```text
Code → Build → Test → Package → Deploy → Run
```

DevSecOps ajoute des contrôles de sécurité tout au long de cette chaîne. Il s'agit de rendre les équipes capables de :

- prévenir ;
- détecter ;
- corriger ;
- tracer ;
- automatiser les contrôles de sécurité.

| Étape | Contrôles possibles |
| --- | --- |
| Code | SAST, secret scanning |
| Dépendances | SCA |
| Infrastructure | IaC scanning, policy-as-code |
| Image | container scanning |
| Application déployée | DAST |
| Production | runtime security, observabilité |

## Lexique DevSecOps

| Terme | Definition | Question |
| --- | --- | --- |
| **SAST (Static Application Security Testing)** | Analyse du code source (pas d'exécution) | Le code contient-il des patterns dangereux ? |
| **DAST (Dynamic Application Security Testing)** | Analyse de l'application en cours d'exécution | L'application déployée présente-t-elle des vulnérabilités ? |
| **SBOM (Software Bill of Materials)** | Nomenclature ou inventaire complet de tous les composants, bibliothèques et logiciels tiers utilisés dans une application. | Quels sont tous les composants installés ? |
| **SCA (Software Composition Analysis)** | Analyse des dépendances | Les dépendances sont-elles vulnérables ? |
| **Secret scanning** | Recherche dans le code des mots de passe, clés API ou jetons d'accès écrits par erreur | Des credentials sont-ils présents ? |
| **IaC (Infrastructure-as-Code)** | Gestion et configuration des infrastructures (serveurs, réseaux) via des fichiers de code | L'infrastructure contient-elle une configuration dangereuse ? |
| **Container scanning** | Inspecter le contenu des images de conteneurs | L'image contient-elle des vulnérabilités ? |
| **Fuzzing** | Test automatisé qui envoie des données inattendues pour détecter fuites mémoire, plantages, buffer overflows, ... | Le logiciel résiste-t-il à des entrées massives, aléatoires, invalides ou inattendues ? |

## Chaîne logicielle

La chaîne logicielle est une surface d'attaque. Une chaîne moderne ressemble à ceci :

1. **Developer**
2. **Git repository**
3. **CI runner**
4. **Build**
5. **Artifact registry**
6. **Deployment**
7. **Production**

Chaque étape peut donner accès à :

- du code ;
- des credentials ;
- des artefacts ;
- du cloud ;
- des réseaux internes ;
- des données de production.

## Menaces côté Git

Le dépôt source peut être attaqué ou utilisé comme vecteur d'attaque :

- secret commité ;
- compte développeur compromis ;
- branche protégée contournée ;
- pull request malveillante ;
- modification non revue ;
- dépendance ou fichier de pipeline modifié.

Un dépôt Git n'est pas seulement un stockage de code : il contient potentiellement **les instructions qui vont être exécutées par l'infrastructure CI**.

## Menaces côté CI/CD

Un runner peut avoir accès à :

- tokens ;
- secrets ;
- registries ;
- credentials cloud ;
- réseau interne ;
- environnements de production.

Risques :

- runner compromis ;
- permissions excessives ;
- secret accessible à une PR ;
- injection dans le pipeline ;
- action ou plugin compromis ;
- artefact empoisonné.

> **Compromettre la CI peut permettre de compromettre la production.**

## Supply chain logicielle

L'application n'est qu'une partie de la chaîne de confiance :

- **dépendances**
- **outils de build**
- **CI**
- **base images**
- **environnement de build**
- **registry**
- **mécanisme de déploiement**

Quelques menaces :

- dépendance vulnérable ;
- package malveillant ;
- dependency confusion ;
- typosquatting ;
- base image compromise ;
- artefact remplacé ;
- outil de build compromis.

La question devient :

> **De quoi mon logiciel dépend-il, et puis-je faire confiance à ce qui a produit l'artefact ?**

## Secure SDLC

La sécurité doit être prise en compte avant le déploiement :

1. **Requirements**
2. **Architecture**
3. **Threat modeling**
4. **Security controls**
5. **Implementation**
6. **Testing**
7. **Deployment**

Plus un problème est découvert tard, plus sa correction peut être coûteuse (**shift left**).

Mais le déplacement vers la gauche ne signifie pas que les contrôles runtime deviennent inutiles.

## Threat modeling

Le threat modeling permet de raisonner avant de choisir les outils.

Identifier :

1. les **assets** ;
2. les acteurs ;
3. les frontières de confiance ;
4. les flux ;
5. les menaces ;
6. les contrôles.

La question n'est pas "_quel scanner devons-nous installer ?_" mais "_quelle menace devons-nous réduire ?_"

### STRIDE

Une méthode simple pour structurer l'analyse :

| Catégorie | Exemple |
| --- | --- |
| **Spoofing** | usurpation d'identité |
| **Tampering** | modification d'un artefact |
| **Repudiation** | absence de traçabilité |
| **Information Disclosure** | fuite de données |
| **Denial of Service** | épuisement d'une ressource |
| **Elevation of Privilege** | accès administrateur obtenu |

**STRIDE** est un cadre de réflexion, pas une checklist exhaustive.

### Exemple de threat model

Une application web accède à une API qui accède à une base de données.

```text
Internet
   ↓
Frontend
   ↓
API
   ↓
Database
```

#### Assets

- données ;
- credentials ;
- disponibilité du service.

#### Menaces

- accès non autorisé ;
- vol de credentials ;
- injection ;
- exfiltration.

#### Contrôles

- authentification ;
- autorisation ;
- secret management ;
- segmentation réseau ;
- validation des entrées ;
- logs ;
- alerting.

## Secret scanning

Un secret découvert dans Git doit être considéré comme **potentiellement compromis** :

1. Détection
1. Blocage
1. Identification
1. Révocation
1. Rotation
1. Recherche d'une compromission passée

**Supprimer le secret du dernier commit ne suffit pas si le credential reste valide ou apparaît encore dans l'historique.**

## SCA - Software Composition Analysis

Une application moderne dépend souvent d'un grand nombre de composants : il faut donc considérer les dépendances **transitives**.

Pour une vulnérabilité donnée :

- quelle version est installée ?
- quelle version est corrigée ?
- le composant est-il réellement utilisé ?
- l'application est-elle exposée ?
- existe-t-il une mesure compensatoire ?

### SBOM

- Un Software Bill of Materials décrit tous les composants présents dans un logiciel.
- Il permet notamment de rechercher rapidement où une bibliothèque vulnérable est utilisée.
- Un SBOM décrit la composition ; il ne prouve ni l'absence de vulnérabilité ni l'intégrité de l'artefact.
- Formats courants : _CycloneDX_, _SPDX_.

## SAST

- Le Static Application Security Testing analyse le code sans exécuter l'application pour identifier certains patterns dangereux directement dans le code : _Semgrep_, _CodeQL_
- Un résultat SAST est un **signal à analyser**, pas automatiquement une preuve de vulnérabilité exploitable (faux positifs ou négatifs, contexte métier incomplet, problèmes d'architecture difficiles à détecter).

## DAST

- Le Dynamic Application Security Testing teste une application en fonctionnement (par exemple depuis la CI/CD).
- Le DAST est particulièrement utile pour observer le comportement réel de l'application déployée.

## Sécuriser le pipeline CI/CD

Le pipeline doit être considéré comme une infrastructure à protéger :

- moindre privilège ;
- isolation ;
- credentials temporaires ;
- runners éphémères lorsque possible ;
- secrets non persistants ;
- séparation des environnements ;
- traçabilité ;
- contrôle des modifications du pipeline.

Le fichier de pipeline est lui-même du **code exécutable** attaquable.

### Pull requests et forks

Une pull request provenant d'une source externe doit être considérée comme du code potentiellement hostile.

Attention à un pipeline qui :

- exécute automatiquement du code de PR ;
- expose des secrets ;
- fournit un token avec permissions d'écriture ;
- utilise un runner privilégié ;
- donne accès au réseau interne.

**Le contexte d'exécution compte autant que le code analysé.**

### Self-hosted runners

Un runner auto-hébergé peut devenir un point de persistance.

Risques :

- état résiduel entre jobs ;
- credentials oubliés ;
- accès au réseau interne ;
- Docker socket ;
- privilèges root.

Mesures :

- runners éphémères ;
- isolation ;
- nettoyage ;
- segmentation réseau ;
- absence de credentials persistants ;
- permissions minimales.

## Secrets

Un secret doit être :

- difficile à exfiltrer ;
- limité dans ses permissions ;
- traçable ;
- rotatable ;
- idéalement limité dans le temps.

## Workload identity

- Toutes les identités ne doivent pas être équivalentes : Human ≠ CI pipeline ≠ Application ≠ Kubernetes controller
- Chaque workload doit obtenir une identité adaptée à son rôle.
- Le principe de moindre privilège s'applique également aux **machines et workloads**, pas uniquement aux utilisateurs.

## OIDC et credentials temporaires

Ancien modèle :

```text
CI
 ↓
clé cloud statique
```

Modèle préférable :

```text
CI
 ↓
OIDC
 ↓
Cloud identity
 ↓
Temporary credentials
```

Avantages :

- pas de clé statique longue durée à stocker ;
- durée de vie limitée ;
- meilleure traçabilité ;
- réduction de la surface d'attaque.

## Provenance

- La provenance répond à une autre question : "Comment cet artefact a-t-il été produit ?"
- La provenance permet de documenter la chaîne de production d'un artefact et d'établir une relation de confiance entre source, build et résultat.

Exemple :

```text
Source commit
     ↓
Build system
     ↓
Build parameters
     ↓
Artifact digest
```

### Signature des artefacts

Une chaîne de confiance peut être construite ainsi :

```text
Build
  ↓
Image
  ↓
Signature
  ↓
Registry
  ↓
Verification
  ↓
Deployment
```

L'objectif est de vérifier que l'artefact déployé correspond bien à celui produit par une chaîne de confiance autorisée.

La signature apporte une garantie **l'intégrité et l'origine** de l'artefact selon le modèle de confiance choisi.

### Tags vs digests

- Un tag (mutable) peut être déplacé vers un autre artefact : `image: app:latest`
- Un digest (immuable) identifie le contenu correspondant : `image: app@sha256:...`
- Pour les déploiements reproductibles, l'identification par digest permet de réduire l'ambiguïté sur ce qui est réellement exécuté.

## Sécurité des conteneurs

**Un conteneur n'est pas une frontière de sécurité magique.** Sa configuration et les privilèges accordés au processus sont déterminants.

Principe : réduire la surface d'attaque :

- image minimale ;
- dépendances minimales ;
- utilisateur non-root ;
- filesystem read-only lorsque possible ;
- capabilities minimales ;
- pas de `--privileged` sans justification.

### SecurityContext Kubernetes

Exemple de contraintes :

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
```

Selon le workload, compléter avec :

- `capabilities.drop` ;
- seccomp ;
- AppArmor ;
- contraintes réseau.

La configuration exacte dépend des besoins de l'application.

### Container scanning

Un outil comme Trivy peut rechercher :

- CVE système ;
- CVE applicatives ;
- secrets ;
- mauvaises configurations.

Il faut également considérer :

- la provenance ;
- les permissions ;
- la configuration ;
- les dépendances ;
- le runtime ;
- le processus de build.

## IaC

- Une configuration Terraform ou Kubernetes peut créer directement une vulnérabilité.
- L'IaC permet de détecter ces problèmes **avant qu'ils deviennent de la configuration déployée**.

Exemples :

```text
Security Group → 0.0.0.0/0
Storage bucket → public
Container → privileged
ServiceAccount → trop puissant
Réseau → trop permissif
```

### IaC security dans le pipeline

Une chaîne possible :

```text
Terraform / manifests
        ↓
      Lint
        ↓
  Security scan
        ↓
     Policy
        ↓
      Plan
        ↓
     Review
        ↓
      Apply
```

Outils possibles selon l'environnement :

- Checkov ;
- Trivy ;
- Conftest ;
- OPA ;
- Kyverno côté Kubernetes.

### Policy as Code

Une politique de sécurité peut devenir du code :

```text
INTERDIRE :
- base de données publique
- container privileged
- image sans contrôle d'intégrité
- stockage sans chiffrement
```

Avantages :

- versionnée ;
- testable ;
- reproductible ;
- automatisable ;
- auditable.

Le contrôle devient une propriété de la plateforme, plutôt qu'une consigne uniquement documentaire.

## Analyser une CVE

Questions :

1. La version est-elle réellement affectée ?
2. Le composant est-il utilisé ?
3. La vulnérabilité est-elle exploitable ?
4. L'application est-elle exposée ?
5. Existe-t-il un exploit connu ?
6. Existe-t-il un correctif ?
7. Une mesure compensatoire est-elle possible ?
8. Quel est le délai acceptable de correction ?

Une stratégie possible :

```text
Critical + exploitable → block
High → remediation SLA
Medium → backlog
Accepted risk → exception documentée
```

Les seuils doivent être adaptés au contexte de l'organisation.

## Architecture DevSecOps cible

```text
Developer
   ↓
Git
   ↓
CI
 ├── Secret scan
 ├── SAST
 ├── SCA
 ├── Tests
 └── IaC scan
   ↓
Build
   ↓
Container image
 ├── Container scan
 ├── SBOM
 └── Signature
   ↓
Registry
   ↓
Deployment
   ↓
Kubernetes
 ├── RBAC
 ├── Pod Security
 ├── NetworkPolicy
 └── Admission policy
   ↓
Production
   ↓
Runtime + Observability
```

## Outils

| Domaine DevSecOps             | Objectif                                    | Outils courants                                             | Quand ?              |
| ----------------------------- | ------------------------------------------- | ----------------------------------------------------------- | -------------------- |
| **SAST**                      | Analyser le code source                     | SonarQube, Semgrep, CodeQL, Snyk Code                       | À chaque commit / PR |
| **SCA**                       | Détecter les vulnérabilités des dépendances | Snyk Open Source, OWASP Dependency-Check, Trivy, Dependabot | Commit / PR          |
| **Secret scanning**           | Détecter clés/API tokens/mots de passe      | Gitleaks, TruffleHog, GitHub Secret Scanning                | Commit / PR          |
| **DAST**                      | Tester l'application en fonctionnement      | OWASP ZAP, Burp Suite                                       | Après déploiement    |
| **Container scanning**        | Scanner les images Docker/OCI               | Trivy, Grype, Snyk Container, Docker Scout                  | Après `docker build` |
| **IaC scanning**              | Sécuriser Terraform/Kubernetes/etc.         | Checkov, KICS, tfsec, Trivy                                 | PR / commit          |
| **Kubernetes security**       | Vérifier manifests/configuration K8s        | Kubescape, Trivy, Kube-score                                | Avant déploiement    |
| **SBOM**                      | Inventorier composants et dépendances       | Syft, Trivy, CycloneDX                                      | Build/release        |
| **Image signing**             | Garantir l'intégrité/provenance             | Cosign, Sigstore                                            | Après build          |
| **Provenance / Supply Chain** | Prouver comment l'artefact a été construit  | SLSA, GitHub Attestations, Cosign                           | Build/release        |
| **License scanning**          | Vérifier les licences des dépendances       | FOSSA, Snyk, ScanCode Toolkit                               | PR / build           |
| **Dependency update**         | Maintenir les dépendances à jour            | Renovate, Dependabot                                        | Automatique          |
| **Linting**                   | Détecter erreurs et mauvaises pratiques     | ESLint, Ruff, golangci-lint, hadolint                       | Commit / PR          |
| **Code quality**              | Mesurer dette technique / qualité           | SonarQube, SonarCloud                                       | PR / build           |
| **IaC policy**                | Imposer des règles de sécurité              | Open Policy Agent, Conftest, Kyverno                        | PR + déploiement     |
| **Runtime security**          | Détecter comportements suspects             | Falco, Tetragon                                             | Runtime              |
| **DAST/API security**         | Tester API et endpoints                     | OWASP ZAP, StackHawk                                        | Staging              |
| **Monitoring / SIEM**         | Détecter incidents                          | Grafana, Prometheus, Loki, ELK, Wazuh                       | Runtime              |
| **Vulnerability management**  | Centraliser et suivre les vulnérabilités    | DefectDojo, Snyk, Dependency-Track                          | Continu              |
