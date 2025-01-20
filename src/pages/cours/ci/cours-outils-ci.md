---
marp: true
paginate: true
#footer: _© 2024 Tom Avenel under 󰵫  BY-SA 4.0_
title: Outils d'intégration continue
keywords:
- ci
---

<!-- _class: titre lead -->

# Les outils de l'intégration continue

_Tom Avenel_

<https://www.avenel.pro/>

---

# La compilation

- Génère le binaire à livrer en production depuis le code source.
- Dans le cas d'un langage compilé, la compilation est le premier garant du respect de la norme du langage. Le compilateur permet, au moment de générer le binaire, de vérifier à la fois la syntaxe et (dans une moindre mesure) la sémantique du code, et d'apporter des explications et conseils sur les changements à opérer.

_Par exemple, le respect de la norme Java est garanti par le compilateur qui tourne dans l'IDE._

---

- Afin d’être certain de vérifier le même objet, un commit ne devrait au mieux n’être compilé qu'une seule fois et l'artéfact généré ne pas être modifié (architecture immuable).
- En principe, cette contrainte est difficile à respecter sans déployer un environnement complet : `Docker`
- On limitera donc au maximum le nombre de compilations du même commit (ex : tests + packaging en 1 seul build)

---

## Transpilation et compilation croisée

- Pour pallier à un manque d'analyse dynamique dans le binaire de destination on pourra utiliser des langages moins permissifs, transpilés vers le langage de destination.
- Ces langages, par une grammaire plus stricte et une analyse statique du code source, garantissent que les problèmes non vérifiés à l'exécution ne peuvent pas survenir (ou moins) au vue de la qualité du code source.

---

_Par exemple, `TypeScript` est transpilé en `EcmaScript` mais garantit la vérification des types sur les variables (ce que `EcmaScript` ne garantit pas)._

_A l'inverse, il est possible d'exécuter du code directement dans les machines virtuelles en respectant leurs contraintes, mais pas celles du langage de base. Par exemple, `Kotlin™` peut être compilé en bytecode exécutable sur la JVM, même s'il ne respecte pas toutes les contraintes de la norme `Java`._

---

# Les outils de build

`Makefile`, `Apache Maven`, `Gradle`, `npm`, `Webpack®`

- Compilent le code source pour créer les binaires
  + Peuvent aussi transpiler le code source vers un autre format : `TypeScript`, ...
  + Peuvent optimiser le code pour la production : obfuscation, minimisation, ...
- Gèrent éventuellement les dépendances.

---

- Intègrent souvent la gestion des tests unitaires.
- Peuvent parfois déployer les artéfacts produits.
- Tous les outils de build permettent une utilisation au travers de règles (compiler, déployer, tester, etc.)

---

# Les tests unitaires

`Junit`, `phpUnit`, `TestNG`

- Ils contrôlent et valident l'implémentation du code au niveau des fonctions ou des classes sans se préoccuper de l'application globale.
- Très utiles pour détecter les régressions.
- Cette isolation minimise les problèmes d'intégration

Voir le [cours sur les tests unitaires][site-perso].

---

- Ils doivent être le plus rapide possible car ils vont tourner souvent !
- Exemple : `< 1 min` pour tous les tests unitaires.
- On essaiera de paralléliser les tests au maximum.

---

# Les outils de versionning

Versionner son code source permet :

- D'identifier, isoler et documenter les changements apportés dans le code
- De visualiser l'historique des changements et opérer un retour arrière
- D'intégrer des changements, y compris de manière concurrente et non linéaire

---

`Git` (très majoritaire), `SVN`, `Mercurial` 

Voir le [cours sur le gestionnaire de versions Git][site-perso].

---

# Les outils d'inspection du code

- Génèrent des rapports sur la qualité du code et les points à revoir : couverture de tests, anti-pattern, ...
- Peuvent proposer des corrections de code : bugs, erreur classiques
- Permettent de tester la généricité du code, sa documentation, les performances (profiling), le code obsolète, les mauvaises habitudes, le code mort, ...

---

- Utiles au développeur pour améliorer sa technique et ses habitudes de programmation
- Utiles pour la recette qualité d'un projet grâce au reporting.

---

## Vérification de style

`Checkstyle`

- Garanti le respect de bonnes pratiques et l'utilisation d'une grammaire commune.
- Le code source devient cohérent et lisible facilement par tous.
- Limite les opérations de merge inutiles : sauts de ligne non cohérents, ...
- Facilite la revue de code.

---

Un outil de contrôle du style ne vérifie que la syntaxe (i.e. si le style du code est correct), pas la sémantique. Le sens du code écrit n'est donc pas validé (la variable existe-t-elle, ...)

---

### Exemple 1

_En `Java`, il est d'usage d'écrire les constantes en majuscule, même si ce n'est pas une contrainte de la norme (le code compile quand même)._

Les 2 lignes suivantes sont équivalentes, mais il est beaucoup plus simple de maintenir un code qui suit des pratiques communes :

```java
public static int COEFF_ADDITION = 2; // OK
```

```java
public static int coeffAddition = 2; // KO
```

---

### Exemple 2

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

### Utilisation dans un IDE

_Il peut être très utile de mettre en place un outil de vérification de style dans l'IDE. On pourra par exemple utiliser le plugin Checkstyle de QAPlug et utiliser le coding-style de Google qui est l'un des plus utilisés dans la communauté._

_On pourra également utiliser les fonctions de formatage de code de l'IDE pour appliquer automatiquement ces contraintes de style dans la suite du développement._

---

## Analyse sémantique

`Linter`, `Spotbugs`, `PMD`

- L'analyse **statique** de code (parfois appelée _linter_) permet de vérifier la sémantique, c'est-à-dire la cohérence du modèle décrit, dans le code source et/ou les binaires.
- L'analyse **dynamique** (sur le code exécuté) et l'analyse statique (sur le code source ou le binaire avant exécution) n'ont donc rien à voir, même si les vérifications peuvent parfois être redondantes (mais nécessaires).

---

### Analyse statique de code source : `PMD`

Pour s'assurer de la qualité du code produit, on peut procéder à une analyse statique directement sur le code source pour vérifier certains paramètres :

- le code respecte-t-il la norme du langage ?
- y a-t-il des duplications de code ? du code mort ?

---

Cette analyse est possible sur tous les langages, qu'ils soient compilés ou interprétés, y compris les framework frontend et les pseudo langages descriptifs tels `HTML` ou `YAML`.

- `PMD` est un ensemble d'outils d'analyse statique du code source (principalement pour Java) vérifiant le bon respect de la norme ainsi que des bonnes pratiques de développement pour minimiser la dette technique du projet.
- Le [Validateur W3C](http://validator.w3.org/) est un outil d'analyse statique du code `HTML` d'un site.
- [Mozilla Observatory](http://observatory.mozilla.org/) est un site d'analyse statique qui va vous donner beaucoup d'information sur les headers de sécurité de votre site internet.

---

### Analyse statique de bytecode (binaire) : `SpotBugs`

- Certains langages étant compilés avant leur exécution, il peut être intéressant de s'intéresser directement à la qualité du livrable (binaire) qui sera lancé.
- Il est possible pour cela de réaliser une analyse statique sur le bytecode généré avant son exécution.
- L'analyse du bytecode à exécuter permet une analyse très fine des problèmes dans le code.

---

- Cependant, il peut être difficile de corréler ces problèmes avec le code source, ou de détecter de mauvaises pratiques comme le copier-coller car le bytecode généré peut être différent.
- `SpotBugs` est un outil d'analyse statique de bytecode `Java`.
- Son but est de trouver des éventuels problèmes dans les fichiers `.class` `Java` en identifiant des ensembles d'instructions connus comme étant des patterns de bugs.

---

# Analyse dynamique de binaire : les interpréteurs, la JVM

- Certains langages ne sont pas exécutés directement en langage machine (assembleur), mais sont interprétés (ou compilés puis exécutés) dans des machines virtuelles.
- Par exemple, `Python` ou `EcmaScript` sont interprétés dans des machines virtuelles exécutant les instructions du code source directement, alors que le code source `Java` est compilé en bytecode, ensuite exécuté dans une machine virtuelle (`JVM`).

---

- Permet de vérifier la cohérence du modèle du code en cours d'exécution :
  + Les variables et fonctions appelées sont-elles bien définies ?
  + Les types des variables sont-ils correctes ?
- Garanti la sécurité du code exécuté contre :
  + Les attaques basées sur une incohérence dans le code exécuté : `buffer overflow`, ...
  + Les accès inapropriés (accès aux champs privés d'une classe) détectés par la machine virtuelle et refusés.

---

- Les analyses dynamiques de code sont beaucoup plus poussées sur certains framework backend, qui sont les seuls à bénéficier d'une machine virtuelle puissante.
  + Il serait beaucoup trop couteux (en terme de ressources) à déployer sur un client léger.

---

- L'analyse dynamique est rarement configurable : elle est soit incluse dans l'interpréteur ou la machine virtuelle du langage, soit absente (notamment pour un langage compilé directement en langage machine).
  + Le choix du langage de programmation est donc déterminant à cette étape.

---

- Dans un cadre d'intégration continue, le code est exécuté pendant la phase de test : c'est donc elle qui sera la garante de cette étape, d'où l'importance de tester **toutes** les classes du projet !

---

# Les autres outils : quelques exemples

- Documentation du code
- Revue de code
- Serveurs d'intégration continue
- Serveurs d'analyse de la qualité

---

## Documentation du code

La documentation du code (`Javadoc`, ...) permet de décrire les contrats utilisés dans le code.

---

## Revue de code

Les outils de revue de code (`Reviewboard`, outils natifs des hébergeurs de code source `Bitbucket`, `Gitlab`, `Github`, ...) permettent aux développeurs de partager leurs modifications et d'en discuter ensemble, avant leur intégration dans le tronc commun

---

## Serveurs d'intégration continue

Les serveurs d'intégration continue permettant le respect de pipelines d'intégration : `Bitbucket`, ...

---

## Serveurs d'analyse de la qualité

Les serveurs d'analyse continue de qualité (`SonarQube`, `Jenkins`, ...) permettant l'analyse et le suivi de la qualité globale d'un projet.

---

# Déploiements

Ces outils sont le noyau dur de l’intégration continue, et ceux que l’on essaiera de déployer au maximum dans les différents environnements :

- Serveur d’intégration continue
- Environnement de développement
- `staging` / `pre-production` / (rarement) `production` 

---

<!-- class: legal -->

# Legal 

- Oracle and Java are registered trademarks of Oracle and/or its affiliates
- Git and the Git logo are either registered trademarks or trademarks of Software Freedom Conservancy, Inc., corporate home of the Git Project, in the United States and/or other countries
- Apache, Apache Subversion, and the Apache feather logo are trademarks of The Apache Software Foundation.
- GITHUB®, the GITHUB® logo design, the INVERTOCAT logo design, OCTOCAT®, and the OCTOCAT® logo design are trademarks of GitHub, Inc., registered in the United States and other countries.
- Bitbucket is a registered trademark of Atlassian Pty Ltd.
- GitLab is a registered trademark of GitLab Inc.
- Jenkins® and the Jenkins logo are registered trademarks of LF Charities Inc.
- SONARQUBE is a trademark of SonarSource SA.
- The name SpotBugs and the SpotBugs logo are trademarked by the University of Maryland.
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
