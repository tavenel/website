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
+---------------------+
| TESTS D'ACCEPTATION |
+---------------------+
           ^
           |
+---------------------+
| TESTS SYSTÈME       |
+---------------------+
           ^
           |
+---------------------+
| TESTS D'INTÉGRATION |
+---------------------+
           ^
           |
+---------------------+
| TESTS UNITAIRES     |
+---------------------+
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
%%{init: { 'theme': 'default', 'gitGraph': {'mainBranchName': 'dev-v2'}} }%%
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


