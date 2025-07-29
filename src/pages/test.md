---
title: Un test
date: 2025
extra:
- math
---

# H1 title
## H2 title
### H3 title
#### H4 title
##### H5 title

**bold** and _emphasis_.

:::correction
Une correction
:::

:::tip
Un petit tip
:::

:::link
[Un lien](/test) et une url : <https://www.google.fr>
:::

:::warn
Attention ici !
:::

:::strong
Une balise strong
:::

:::exo
Un exercice avec :

1. Première question
   - étape 1
   - étape 2
2. Deuxième question
:::

## Subsection

<kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Delete</kbd>

> Une citation

### 🧩 Emojis

- **Description** : Plateforme open-source pour l'automatisation du déploiement, la mise à l'échelle et la gestion des applications conteneurisées. 🌐
- De loin l'orchestrateur **le plus utilisé avec _Docker®_** 🏆
- **Avantages** 🌟 :
  - Grande communauté et écosystème 👥
  - Hautement extensible avec de nombreux outils et extensions 🛠️
  - Prise en charge de charges de travail complexes 🏋️
- **Inconvénients** ❌:
  - Courbe d'apprentissage abrupte 📚
  - Configuration complexe ⚙️
- Pour les **déploiements complexes et évolutifs** 🌐

-   Docker®
- 󱃾 Kubernetes®
- 🐧 Linux
- 󱃾  Devops - Sysops
- 🔄 CI/CD &  Jenkins
-  Git
- 🧪 Tests
- 󰌠  Python &   Django
- 🧑‍💼 DDD : Domain-Driven Design
- 🏗️ Architecture logicielle
- 📅 Gestion de projet
- 🌐 Cloud & Web
- 📊  Data
- 💚 Green IT
- ☎️  Intégration
- 💬 Management
-   Spring & 󱘻 Hibernate

### Subsubsection

<mark>Highlight</mark> some text

#### h4

$$ \sqrt{3x-1}+(1+x)^2 $$

```python
class A():
	def __init__(self, x):
		self.x = x
		print(x)
		return x

def f(y):
	return y

a = A()
f(2)
```

# gfm

## Autolink literals

www.example.com, https://example.com, and contact@example.com.

## Footnote

A note[^1]

[^1]: Big note.

## Strikethrough

~one~ or ~~two~~ tildes.

## Table

| a | b  |  c |  d  |
| - | :- | -: | :-: |

## Tasklist

* [ ] to do
* [x] done

## Table big

| Critère          | VLAN                          | SDN                           | VXLAN                        | BGP                          | IPinIP                       | eBPF                         |
|-----------------------|-----------------------------------|-----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Couche OSI        | Couche 2 (Liaison de données)     | Couche 3 (Réseau)                | Couche 2 et 3                    | Couche 3 (Réseau)                | Couche 3 (Réseau)                | Couche 3 (Réseau)                |
| Scalabilité       | Limité à 4096 VLANs              | Très élevée                       | Jusqu'à 16 millions de segments  | Très élevée                      | Moyenne                          | Très élevée                      |
| Flexibilité       | Moyenne                           | Très élevée                       | Élevée                           | Élevée                           | Élevée                           | Très élevée                      |
| Complexité        | Moyenne                           | Élevée                            | Élevée                           | Très élevée                      | Faible                           | Élevée                           |
| Utilisation       | Segmentation de réseaux locaux    | Gestion centralisée des réseaux   | Réseaux virtuels extensibles     | Routage inter-AS sur Internet    | Tunnels virtuels sur réseaux IP  | Surveillance, sécurité, réseau, optimisation des performances |
| Sécurité          | Isolation des segments            | Point unique de défaillance       | Isolation des segments           | Politiques de routage complexes  | Nécessite des mécanismes supplémentaires | Vérification rigoureuse des programmes |
| Performance       | Bonne                             | Bonne                             | Potentielle latence supplémentaire| Bonne                            | Overhead supplémentaire          | Très haute                       |
| Compatibilité     | Réseaux Ethernet                  | Réseaux IP                        | Réseaux IP                      | Réseaux IP                       | Réseaux IP                      | Noyau Linux                      |
| Intégration       | Commutateurs et routeurs          | Contrôleurs SDN                   | Commutateurs et routeurs         | Routeurs                          | Routeurs                         | Outils de surveillance et sécurité |
| Résilience        | Moyenne                           | Élevée                            | Élevée                           | Très élevée                      | Moyenne                          | Très élevée                      |
# Math

Lift($$L$$) can be determined by Lift Coefficient ($$C_L$$) like the following
equation.

$$
L = \frac{1}{2} \rho v^2 S C_L
$$

```python
class A:
	def __init__(self, x):
		self.x = x
	
	def f(self, y)
			 return self.x + y
```

```plantuml
@startuml

caption
= Design Pattern Page Object
endcaption

title Page Object

interface HomePage
interface LoginPage
class HomePageObject
class LoginPageObject
class Test1
class Test2
class Test3

HomePageObject -up-|> HomePage
LoginPageObject -up-|> LoginPage

Test1 -up-> HomePageObject
Test1 -up-> LoginPageObject
Test2 -up-> HomePageObject
Test2 -up-> LoginPageObject
Test3 -up-> HomePageObject
Test3 -up-> LoginPageObject
@enduml
```

```plantuml
@startdot

digraph supervised {

node [style="filled"]
entrées [color="indianred"]

subgraph clusterSuperviseur {
node [fillcolor="lightskyblue"]
edge [color="royalblue"]
label = "Superviseur"
superviseur -> "sortie désirée" -> erreur
}

subgraph {
node [fillcolor="aquamarine2"]
edge [color="aquamarine4"]
réseau -> "sortie obtenue" -> erreur
}

entrées -> superviseur, réseau
erreur -> réseau [style="dashed", color="royalblue"]

label = "Schéma d'apprentissage supervisé"

@enddot
}
```

```plantuml
@startditaa

+-------------+                                  +----------------+   +--------------+ 
|             |                                  |                |   |              |
|             |                       +--------->|  Construction  |   |              |
|             |                       |          |      50%       |   |              |
|             |                       |          +----------------+   |              |
|             |                       |                               |              |
|             |                       |          +----+ +--+ +----+   |              |
|             |                 +-----+--+------>|    | |  | |    |   |              |
|             |                 |        |       +----+ +--+ +----+   |              |
|             |                 | Design |                            |              |
|             |        +------->|   23%  |       +----------------+   |              |
|             |        |        +--------+------>|                |   |              |
|             |   +----+----+                    +----------------+   |              |
|             |   |         |                                         |              |
| Préparation |   | Cadrage |  Parrallélisation    Sérialisation      | Finalisation |
|             |   |   9%    |                                         |     12%      |
|     6%      |   +----+----+                    +----------------+   |              |
|             |        |        +--------+------>|                |   |              |
|             |        +------->|        |       +----------------+   |              |
|             |                 | Design |                            |              |
|             |                 |        |       +----+ +--+ +----+   |              |
|             |                 +-----+--+------>|    | |  | |    |   |              |
|             |                       |          +----+ +--+ +----+   |              |
|             |                       |                               |              |
|             |                       |          +----------------+   |              |
|             |                       |          |                |   |              |
|             |                       +--------->|  Construction  |   |              |
|             |                                  |                |   |              |
+-------------+                                  +----------------+   +--------------+

@endditaa
```

```plantuml
@startmindmap
* Context Map

  **_ Superposition de contextes
    *** Shared Kernel

  **_ Contextes coopérant fortement
    *** Partnership

  **_ Crée un lien de coopération
    *** Customer/Supplier Teams

  **_ Crée un lien unidirectionnel
    *** Conformist

  **_ Supporte différents clients
    *** Open Host Service
      ****_ Version formelle
        ***** Published Language

  **_ Libère les contraintes entre équipes
    *** Separate Ways

  **_ Traduis et isole unilatéralement
    *** Anticorruption Layer

left side

  **_ Évaluation et examen des relations
    *** Bounded Context

      ****_ nommage
        ***** Ubiquitous Language

      ****_ garde le modèle unifié
        ***** Continuous Integration

@endmindmap
```

```mermaid
---
config:
  theme: 'base'
---
flowchart TD
    A["La solution peut-elle être achetée/intégrée?"] -->|Oui| B["Cela mettra-t-il en péril l’entreprise ?"]
    A -->|Non| C["Complexité de la logique métier?"]
    B -->|Oui| D["Domaine Principal"]
    B -->|Non| E["Sous-domaine Générique"]
    C -->|Complexe| D
    C -->|Simple| F["Sous-domaine Support"]
```

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

```mermaid
%%{init: { 'theme': 'base', 'gitGraph': {'mainBranchName': 'dev-v2'}} }%%
gitGraph
commit
commit
branch stable-1
commit
checkout dev-v2
commit
checkout stable-1
commit
```


```mermaid
graph TD
  subgraph Machine personnelle
    A1{{fa:fa-laptop-code Modification code backend}}-->A2{make dev : OK?}-->|Oui|A3[fa:fa-code-branch Push répo backend]
    A2-->|Non|A1

    C1{{fa:fa-laptop-code Modification code frontend}}-->C2{make dev : OK?}-->|Oui|C3[fa:fa-code-branch Push répo frontend]
    C2-->|Non|C1
  end

  subgraph Serveur CI distant
    A3-.->B1[tests du backend en isolation]-->|make dev|B1-->|OK|E1
    C3-.->D1[tests du frontend en isolation]-->|make dev|D1-->|OK|E1
    E1[Intégration backend + frontend]-->|make prod|E1-->|tests système|E2{{FTP de test}}
  end

  E2-->|OK|E3[(Livraison sur Artifactory)]-->E4[Production]
```


```mermaid
---
title: Le workflow Gitflow.
---

%%{init: { 'theme': 'base', 'gitGraph': {'showCommitLabel': false}} }%%
gitGraph
commit
commit tag: "v0.1"
branch hotfix
 commit
 commit
checkout main
branch dev
 commit
 commit
 branch fonctionnalite-A
  commit
  commit
  commit
  commit
checkout main
merge hotfix tag:"v0.2"
checkout dev
 merge hotfix
 merge fonctionnalite-A
 commit
 commit
 branch livraison-1.0
  commit
  commit
checkout main
merge livraison-1.0 tag:"v1.0"
```


```mermaid
graph LR
  subgraph ReservationContext["RÉSERVATION"]
    subgraph selection[«Sélection»]
      getter("getSelection() : SPI")
    end
  end

  subgraph RechercheContext["RECHERCHE"]
    subgraph selection2[«Sélection»]
      getter2("getSelection() : API")
    end
  end

  getter2 -->|Conformiste| getter

  class selection2,getter,getter2 blue
```

```mermaid
---
config:
  theme: redux-color
---
mindmap
  root((Context Map))

    Superposition de contextes
      Shared Kernel

    Contextes coopérant fortement
      Partnership

    Crée un lien de coopération
      Customer/Supplier Teams

    Crée un lien unidirectionnel
      Conformist

    Supporte différents clients
      Open Host Service
        Version formelle
          Published Language

    Libère les contraintes entre équipes
      Separate Ways

    Traduis et isole unilatéralement
      Anticorruption Layer

    Évaluation et examen des relations
      Bounded Context
        nommage
          Ubiquitous Language
        garde le modèle unifié
          Continuous Integration
```

```mermaid
---
title: Le processus TDD
---
stateDiagram-v2
    
    Test : test en échec
    Implementation : écriture du code
    Refactoring

    Test --> Implementation : test en échec
    Implementation --> Refactoring : succès du test
    Refactoring --> Test : problème suivant
```


```mermaid
---
title: Diagramme de séquence
---
sequenceDiagram
    actor Client
    participant "Upload Image"
    participant "Resize Image"
    participant "Add Watermark"
    participant "Save Image"

    Client->>"Upload Image": Upload
    "Upload Image"->>"Resize Image": Event: Uploaded
    "Resize Image"->>"Add Watermark": Event: Resized
    "Add Watermark"->>"Save Image": Event: Watermarked
```

:::correction
```mermaid
---
title: Plan d'adressage IP
---
flowchart TD

    internet["Internet<br/>IP publique<br/>202.60.23.2"]
    router["Passerelle / Routeur<br/>Adresse locale<br/>192.168.10.1"]
    printer["Printer<br/>192.168.10.3"]
    mobile["Mobile<br/>192.168.10.7"]
    serveur["Serveur Web<br/>192.168.10.2"]
    pcs["3x PC<br/>192.168.10.4<br/>192.168.10.5<br/>192.168.10.6"]

    internet --- router
    mobile --- router
    printer --- router
    serveur --- router
    pcs --- router
```
:::

