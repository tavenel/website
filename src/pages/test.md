---
title: Un test
date: 2025
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

:::correction
```console
$ API=$(kubectl get svc kubernetes -o json | jq -r .spec.clusterIP)

$ curl -k https://$API # Connexion anonyme 

{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"system:anonymous\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403
}

$ kubectl get ServiceAccount
NAME      SECRETS   AGE
default   0         7h33m

$ kubectl create token default

eyJhbGciOiJSUzI1NiIsImtpZCI6IjFKVHBxWE1ac0RoVURfVjdWdjNSeEtTMVZsdk5qUFR3Q1U5eldUanlxcWcifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzQzNjE3Nzk2LCJpYXQiOjE3NDM2MTQxOTYsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiMmViMDNjYTYtYWY4MC00YTNjLWI3OTMtYWVkYjZlM2YyYmEyIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRlZmF1bHQiLCJ1aWQiOiJkYTY4ODVhMC1jZGE1LTRhNmUtYThmZC1iZTdjMzZkNzIwMGUifX0sIm5iZiI6MTc0MzYxNDE5Niwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.BjaXxdFx-w5cclykMycsEh-WbgSHwWl5z3fkm-StWkARa2MLRjTwjsT1LM1RGqutmPv4qMy9PXoua1VW4rNs8BeEy0rppG9txDKjMr1utXCgnlYJLnW80B9rTJIl_VfyVWJnvuaBnilZEyrS1_NuT1irC0GVAPexhTd6D7bHyCpB63xq1_3DjSHjoY0pK9R8VYGCa6aYR8ByyqFj5vSs-mJ7EImHEV2RqyyrQBKX3FlezZvt9q9E-ouB0I45oA1galGmOX3v7wHSHUas9qdB1FO7bEaNppud2JHXXKUUzGhkhB57IBSBuIO1sTcDQg9JXbHbaLYbC1DiBd9XL9IOoQ

$ curl -k -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFKVHBxWE1ac0RoVURfVjdWdjNSeEtTMVZsdk5qUFR3Q1U5eldUanlxcWcifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzQzNjE3Nzk2LCJpYXQiOjE3NDM2MTQxOTYsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiMmViMDNjYTYtYWY4MC00YTNjLWI3OTMtYWVkYjZlM2YyYmEyIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRlZmF1bHQiLCJ1aWQiOiJkYTY4ODVhMC1jZGE1LTRhNmUtYThmZC1iZTdjMzZkNzIwMGUifX0sIm5iZiI6MTc0MzYxNDE5Niwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.BjaXxdFx-w5cclykMycsEh-WbgSHwWl5z3fkm-StWkARa2MLRjTwjsT1LM1RGqutmPv4qMy9PXoua1VW4rNs8BeEy0rppG9txDKjMr1utXCgnlYJLnW80B9rTJIl_VfyVWJnvuaBnilZEyrS1_NuT1irC0GVAPexhTd6D7bHyCpB63xq1_3DjSHjoY0pK9R8VYGCa6aYR8ByyqFj5vSs-mJ7EImHEV2RqyyrQBKX3FlezZvt9q9E-ouB0I45oA1galGmOX3v7wHSHUas9qdB1FO7bEaNppud2JHXXKUUzGhkhB57IBSBuIO1sTcDQg9JXbHbaLYbC1DiBd9XL9IOoQ" https://$API

{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"system:serviceaccount:default:default\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403

## Accès encore refusé (authz) mais l'utilisateur est authentifié (authn).
```
:::

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

```mermaid
---
title: Separate Ways
---
classDiagram
    note for ClientPourFacturation "Classe dupliquée contexte Facturation"
    class ClientPourFacturation {
        +addresseDeFacturation
        +récupérerDevis()
    }

    note for ClientPourMarketing "Classe dupliquée contexte Marketing (aucun lien)"
    class ClientPourMarketing {
        +addresseDeContact
        +listerProduitsRécents()
    }
```

```mermaid
---
title: Intégration d'une branche `feature` dans un workflow `fork`
---
flowchart TD
    subgraph Dépôt_Officiel
        OfficialRepo@{ shape: cyl, label: "Dépôt officiel" }
    end

    subgraph Fork_Distant
        ForkA@{ shape: cyl, label: "Fork A\nNouveau dépôt distant" }
    end

    subgraph MachineLocale
        CloneA@{ shape: cyl, label: "Clone A\nDépôt local" }
        Commit
    end

    OfficialRepo -.->|"git clone (entre serveurs)"| ForkA
    CloneA -.-|remote 'origin'| ForkA
    CloneA -.-|remote 'upstream'| OfficialRepo

    CloneA e1@-->|1 - nouvelle branche 'feature'| Commit
    Commit e2@-->|2 - push 'feature' vers origin| ForkA
    ForkA e3@-->|3 - pull request 'feature'| OfficialRepo
    Commit e4@-->|4 - push 'feature' vers upstream| OfficialRepo

    e3@{ animate: true }
    e4@{ animate: true }
```

```mermaid
---
title: CQRS
---
classDiagram

  namespace CommandSide {
    class OrderCommandHandler {
      +handlePlaceOrder(cmd: PlaceOrder)
    }
  }

  namespace QuerySide {
    class OrderQueryService {
      +getOrdersByCustomer(id: UUID): List~OrderDTO~
    }
  }

  OrderCommandHandler --> PlaceOrder
  OrderQueryService --> OrderDTO
```

```mermaid
---
title: Saga
---
classDiagram
  class OrderService
  class PaymentService
  class ShippingService
  class SagaManager

  OrderService --> SagaManager : placeOrder()
  SagaManager --> PaymentService : initiatePayment()
  SagaManager --> ShippingService : prepareShipping()

  note for SagaManager "Coordonne une série d'étapes distribuées"
```

```mermaid
---
title: Process Manager
---
classDiagram
  class OrderFulfillmentProcessManager {
    +handleOrderPlaced(OrderPlacedEvent event)
    +handlePaymentConfirmed(PaymentConfirmedEvent event)
    +handleShippingStarted(ShippingStartedEvent event)
    -ProcessStateEnum state
  }

  class OrderPlacedEvent
  class PaymentConfirmedEvent
  class ShippingStartedEvent

  OrderFulfillmentProcessManager --> OrderPlacedEvent
  OrderFulfillmentProcessManager --> PaymentConfirmedEvent
  OrderFulfillmentProcessManager --> ShippingStartedEvent

  enumeration ProcessStateEnum
  class ProcessStateEnum {
    AWAITING_PAYMENT
    PAYMENT_CONFIRMED
    SHIPPING_IN_PROGRESS
    COMPLETED
  }
```

```mermaid
---
title: ClusterIP Multi-Nodes
---
flowchart TD

  subgraph Cluster ["Cluster"]

    svcA["Service blue<br/>clusterIP 10.0.0.5<br/>port 81"]
    svcB["Service green<br/>clusterIP 10.0.0.7<br/>port 82"]
    class svcA blue
    class svcB green

    subgraph node1 ["Node 1"]
        pod1_1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
        class pod1_1 blue
    end

    subgraph node2 ["Node 2"]
        pod2_1["pod-blue-2<br/>10.4.32.5<br/>port 8181"]
        pod2_2["pod-green-1<br/>10.4.32.6<br/>port 8282"]
        class pod2_1 blue
        class pod2_2 green
    end

    subgraph node3 ["Node 3"]
        pod3_1["pod-green-2<br/>10.4.32.8<br/>port 8282"]
        class pod3_1 green
    end

    svcA -.-> pod1_1
    svcA -.-> pod2_1

    svcB -.-> pod2_2
    svcB -.-> pod3_1

  end
```

```mermaid
---
title: Communication entre Pods par ClusterIP - par Pod 2
---
flowchart TD

    svcB["Service green<br/>clusterIP 10.0.0.7<br/>port 82"]
    class svcB green

    subgraph Cluster ["Cluster"]

        subgraph node1 ["Node 1"]
            pod1_1["pod-blue-1<br/>10.4.32.2<br/>port 8181"]
            class pod1_1 blue
        end

        subgraph node2 ["Node 2"]
            pod2_1["pod-blue-2<br/>10.4.32.5<br/>port 8181"]
            pod2_2["pod-green-1<br/>10.4.32.6<br/>port 8282"]
            class pod2_1 blue
            class pod2_2 green
        end

        subgraph node3 ["Node 3"]
            pod3_1["pod-green-2<br/>10.4.32.8<br/>port 8282"]
            class pod3_1 green
        end
    end

    %% Connexions services → pods
    svcB -.-> pod2_2
    svcB -.-> pod3_1

    %% Communication entre pod et service
    pod1_1 e1@-->|"1 - http:// green:82"| svcB
    svcB e2@-->|"2 - http:// 10.4.32.8:8282"| pod3_1

    e1@{ animate : true }
    e2@{ animate : true }
```

```mermaid
---
title: PV et PVC
---
flowchart TD

    %% Composants
    pv["PersistentVolume"]
    sc["StorageClass"]
    db[(Physical Volume)]
    class sc red
    class db green

    %% Pod et PVC imbriqués
    subgraph pod ["pod"]
        pvc["PersistentVolumeClaim"]
    end
    class pod blue

    %% Relations
    sc -.-> pv
    sc -.-> pvc
    pv --> db
```

```mermaid
---
title: Suppression du fichier source
---
flowchart TD
    %% Données sur disque
    DATA[("Données sur disque")]

    %% Lien dur (toujours valide)
    subgraph hard["Lien dur (hard link)"]
        F2["F2"]
    end

    %% Fichier source supprimé
    F1["F1 (supprimé)"]:::deleted

    %% Lien symbolique devenu cassé
    F3["Lien symbolique (F3)"] -.-> F1

    %% Connexions
    F2 --> DATA

    class F1 red
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

```mermaid
---
title: Carte de contexte
---
flowchart TD

  UP["UserProfile(Supporting)"]
  CB["CourseBooking(Core)"]
  P["Payment(Supporting)"]
  PF["PedagogicalFollowup(Supporting)"]
  S["Support(Generic)"]

  UP -->|fournit profils et disponibilités| CB
  CB -->|déclenche paiement| P
  CB -->|déclenche compte-rendu| PF
  CB -->|signale problèmes| S
  P -->|permet remboursement| S
```

:::

![An alt text](@assets/apps/lamp.png "An image caption")
