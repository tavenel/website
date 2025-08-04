---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: λ TP OpenFaaS
---

## Introduction aux Fonctions Serverless

Une fonction _Serverless_ est un morceau de code exécutable à la demande, hébergé sur une plateforme cloud (AWS Lambda, Azure Functions, Google Cloud Functions, …), sans que le développeur n'ait à gérer l'infrastructure sous-jacente (serveurs, mise à l'échelle, maintenance). L'un de ses grands avantages est la simplicité : elle permet de se concentrer sur le code métier, tout en bénéficiant d'une facturation à l'usage (paiement uniquement pour le temps d'exécution) et d'une mise à l'échelle automatique. Cependant, elle présente aussi des inconvénients : la dépendance au fournisseur ("vendor lock-in"), une latence potentielle au démarrage (le _cold start_), et des limites de contrôle sur l'environnement d'exécution.

### OpenFaaS

_OpenFaaS_ (_Open Functions as a Service_) est une plateforme qui permet de déployer facilement des fonctions serverless sur n'importe quelle infrastructure, y compris sur Kubernetes, Docker Swarm, ou même sur une machine unique. Contrairement aux offres serverless propriétaires des grands clouds (AWS Lambda, etc.), OpenFaaS donne aux développeurs un contrôle total sur leur environnement d'exécution tout en offrant la simplicité du modèle serverless : chaque fonction est empaquetée comme un conteneur Docker et exposée via une API HTTP. OpenFaaS facilite aussi l'autoscaling, la gestion des événements, l'authentification, et fournit une interface web simple pour déclencher et superviser les fonctions.

Ses avantages principaux sont la portabilité (pas de verrouillage cloud), la simplicité d'utilisation, et la compatibilité avec n'importe quelle application conteneurisée (pas seulement des petits scripts).

#### Concepts

```mermaid
---
title: OpenFaaS for Kubernetes
---
flowchart TB
  subgraph Template_Store
    Java["Java"]
    Python["Python"]
  end

  subgraph Function_Store
    fdd1["Function Definition"]
    fdd2["Function Definition"]
  end

  subgraph Another_team_software
    inbound_http_request1["Inbound HTTP Request"]
    kafka_topic["Kafka Topic"]
  end

  subgraph Your_team_software
    custom_ui["Custom UI"]
    custom_api["Custom API"]
  end

  subgraph Customer_or_Partner
    inbound_http_request2["Inbound HTTP Request"]
    s3_bucket_put["S3 Bucket PUT"]
  end

  subgraph OpenFaaS_Installation
    fdp1["Function Deployment"]
    fdp2["Function Deployment"]
    fdp3["Function Deployment"]

    openfaas["OpenFaaS"]
    autoscaler["Autoscaler"]
    prometheus["Prometheus"]
    queue_worker["Queue-Worker"]
    cron_connector["Cron-Connector"]
    kafka_connector["Kafka-Connector"]

    fdp1 --> openfaas
    fdp2 --> openfaas
    fdp3 --> openfaas
  end

  Template_Store -.-> OpenFaaS_Installation
  Function_Store -.-> OpenFaaS_Installation
  Another_team_software -.-> OpenFaaS_Installation
  Your_team_software -.-> OpenFaaS_Installation
  Customer_or_Partner -.-> OpenFaaS_Installation

  class fdp1,fdp2,fdp3 green
  class openfaas,autoscaler,prometheus,queue_worker,cron_connector,kafka_connector blue
```

<div class="caption">Concepts OpenFaaS. Source: https://www.openfaas.com/blog/integrate-with-openfaas/</div>

#### Appel de fonction serverless en HTTP

```mermaid
---
title: OpenFaaS for Kubernetes
---
flowchart TB
  subgraph Registry
    registry_content["ghcr.io/openfaas/sleep:0.1.0"]
  end

  subgraph OpenFaaS_Installation
    function_sleep["Function 'sleep'"]
    deployment["Deployment"]
    pod1["Pod"]
    pod2["Pod"]
    openfaas_gateway["OpenFaaS Gateway"]
    service["Service TCP/8080"]
    ingress["Ingress 80, 443"]
  end

  User(("User"))

  User -->|HTTP GET /function/sleep| ingress
  function_sleep -.-> deployment
  function_sleep -.-> service
  deployment -.-> pod1
  deployment -.-> pod2

  openfaas_gateway --- function_sleep
  ingress --> openfaas_gateway
  openfaas_gateway --> service
  service --> pod1
  service --> pod2

  registry_content -.-> function_sleep

  class function_sleep,deployment,service,pod1,pod2 green
  class openfaas_gateway blue
```

<div class="caption">Appel HTTP via Ingress OpenFaaS. Source: https://www.openfaas.com/blog/integrate-with-openfaas/</div>

Les appels de fonctions se font depuis l'Ingress OpenFaaS :

- en synchrone : <http://gateway.openfaas:8080/function/NAME>
- en asynchrone : <http://gateway.openfaas:8080/async-function/NAME>

:::link
Voir aussi : <https://www.openfaas.com/blog/integrate-with-openfaas/>
:::

### Exemples de cas d'utilisation typiques

#### Traitement d'images

Utilisation d'OpenFaaS pour automatiser le traitement d'images, comme le redimensionnement, la conversion de formats, ou l'application de filtres.

- **Déclencheur** : Téléchargement d'une nouvelle image dans un bucket S3.
- **Action** : Une fonction OpenFaaS est déclenchée pour redimensionner l'image et la sauvegarder dans un autre bucket.
- **Avantages** : Évolutivité automatique et traitement rapide des images sans avoir à gérer l'infrastructure sous-jacente. 🌟

#### Analyse de sentiments

Déploiement d'un modèle de machine learning pour analyser les sentiments dans les commentaires des utilisateurs ou les messages sur les réseaux sociaux.

- **Déclencheur** : Nouveau commentaire posté sur une plateforme de médias sociaux.
- **Action** : Une fonction OpenFaaS analyse le texte pour déterminer si le sentiment est positif, négatif ou neutre.
- **Avantages** 🌟 : Réactivité en temps réel et capacité à traiter de grands volumes de données textuelles.

#### Intégration de données

Utilisation d'OpenFaaS pour intégrer des données provenant de différentes sources (API, bases de données, fichiers) et les transformer en un format unifié.

- **Déclencheur** : Nouvelle entrée dans une base de données SQL.
- **Action** : Une fonction OpenFaaS extrait les données, les transforme et les charge dans un entrepôt de données.
- **Avantages** 🌟 : Automatisation des flux de travail ETL (Extract, Transform, Load) et réduction des erreurs manuelles.

#### Notifications en temps réel

Envoi de notifications en temps réel aux utilisateurs en fonction de certains événements ou conditions.

- **Déclencheur** : Changement de statut d'une commande dans un système de gestion des commandes.
- **Action** : Une fonction OpenFaaS envoie une notification par email ou SMS au client.
- **Avantages** 🌟 : Amélioration de l'expérience utilisateur grâce à des mises à jour instantanées.

#### Automatisation des tâches DevOps

Automatisation des tâches répétitives dans le cycle de développement et de déploiement, comme les tests, les builds, ou les déploiements.

- **Déclencheur** : Nouveau commit dans un dépôt Git.
- **Action** : Une fonction OpenFaaS lance une série de tests automatisés et déploie le code si les tests réussissent.
- **Avantages** 🌟 : Accélération du cycle de développement et réduction des erreurs humaines.

## Installation d'OpenFaaS dans Kubernetes

1. Installer OpenFaaS dans votre cluster Kubernetes en suivant la documentation : <https://docs.openfaas.com/cli/install/>

```sh
arkade install openfaas

# Récupération du mot de passe admin
PASSWORD=$(kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)
```

2. Installer la CLI d'OpenFaaS :

```sh
arkade get faas-cli
```

3. Ouvrir un port sur la gateway et s'y connecter

```sh
kubectl port-forward -n openfaas svc/gateway 8080:8080 &
echo -n $PASSWORD | faas-cli login --username admin --password-stdin
```

Le portail OpenFaaS est maintenant accessible sur `http://127.0.0.1:8080`.

## Test de déploiement d'une fonction existante

Déployer la fonction de test _figlet_ (cette fonction crée un Ascii art depuis une chaîne de caractères passée en paramètre) :

```console
$ faas-cli deploy figlet


$ faas-cli list               

Function                      	Invocations    	Replicas
figlet                        	0              	1


$ curl -X POST http://127.0.0.1:8080/function/figlet \
     -H "Content-Type: application/text" \
     -d 'mon texte en asciiart'

                         _            _                    
 _ __ ___   ___  _ __   | |_ _____  _| |_ ___    ___ _ __  
| '_ ` _ \ / _ \| '_ \  | __/ _ \ \/ / __/ _ \  / _ \ '_ \ 
| | | | | | (_) | | | | | ||  __/>  <| ||  __/ |  __/ | | |
|_| |_| |_|\___/|_| |_|  \__\___/_/\_\\__\___|  \___|_| |_|
                                                           
                _ _            _   
  __ _ ___  ___(_|_) __ _ _ __| |_ 
 / _` / __|/ __| | |/ _` | '__| __|
| (_| \__ \ (__| | | (_| | |  | |_ 
 \__,_|___/\___|_|_|\__,_|_|   \__|


$ faas-cli list

Function                      	Invocations    	Replicas
figlet                        	1              	1    
```


## Une première fonction serverless en Python

Exemple de création d'une fonction simple : on utilise pour cela l'un des _templates_ existant (`dockerfile` pour utiliser directement une image Docker ou un langage de programmation pour la génération d'une image automatiquement). 

```sh
faas-cli new hello-openfaas --prefix mon_user_dockerhub --lang python3-http
```

:::tip
L'option `--prefix` permet d'ajouter votre nom d'utilisateur _Docker Hub_ afin d'y publier automatiquement l'image Docker de la fonction créée.
:::

La commande génère deux fichiers principaux :

- `stack.yml` (définition de la fonction)
- `hello-openfaas/handler.py` (code Python de la fonction)

**Exemple de code dans `handler.py`** :

```python
def handle(event, context):
	    return {
        "statusCode": 200,
  			"body": "You said: " + str(event.body)
    }
```

:::link
Pour plus d'information sur le template Python, voir : <https://docs.openfaas.com/languages/python/>
:::

### Déployer la fonction

La commande `faas-cli up` construis, pousse et déploie la fonction. Attention à être connecté au _Docker Hub_ auparavant :

```sh
docker login

faas-cli up -f stack.yaml
```

(*`up` = build + push + deploy en une seule commande*)

:::tip
Attention, la version gratuite d'OpenFaaS n'autorise pas le déploiement d'images privées : l'image créée sur votre compte _Docker Hub_ doit donc rester publique !
:::

:::tip
Pour créer une image multi-plateformes (_ARM_ pour MacOS, …) utiliser l'option `--platform` :

```sh
faas-cli publish -f stack.yaml --platforms linux/arm64,linux/arm/v7,linux/amd64
```
:::

### Appeler la fonction

Via l'interface Web ou bien en ligne de commande :

```console
$ curl -X POST http://127.0.0.1:8080/function/hello-openfaas -d "test"

You said: b'test'%
```

## Timeouts

Pour éviter une saturation des ressources, une bonne pratique est d'ajouter des timeouts sur toutes les fonctions asynchrones exécutées.

Un timeout se définit par des variables d'environnement :

```yaml
provider:
  name: openfaas
  gateway: http://127.0.0.1:8080

functions:
  ma-fonction:
    lang: …
    handler: …
    image: …
    environment:
      read_timeout: "5s" # timeout de lecture de requête HTTP
      write_timeout: "5s" # timeout d'écriture de réponse HTTP
      exec_timeout: "5s" # timeout d'exécution de la fonction
```

:::tip
Un timeout génère une erreur `502`.
:::

:::link
Voir aussi la documentation officielle : <https://docs.openfaas.com/tutorials/expanded-timeouts/>
:::

## Logs et supervision

Vous pouvez visualiser les logs d'une fonction :

- Depuis la ligne de commandes `faas-cli logs`
- Depuis l'interface utilisateur : trouvez la fonction dont vous souhaitez visualiser les logs et cliquez dessus
- En récupérant les logs du _Pod_ associé : `kubectl logs -n openfaas-fn …`
- En utilisant un système de logs centralisés dans le cluster (stack ELK, …).

:::tip
Les _Pods_ sont déployés dans le _Namespace_ `openfaas-fn`. Pour trouver le _Pod_ associé à une fonction, on peut utiliser un sélecteur :

```sh
kubectl get pods -n openfaas-fn --selector=faas_function=…
```
:::

:::tip
Il est possible d'ajouter la variable d'environnement `write_debug=true` pour afficher des informations de debug sur la console (payload, …) :

```yaml
environment:
  write_debug: true
```
:::

### Dashboard OpenFaaS

OpenFaaS inclut un dashboad permettant de suivre les appels d'une fonction :

![Monitoring de fonctions dans le dashboard OpenFaaS](https://docs.openfaas.com/images/dashboard/load-graphs.png)

<div class="caption">Monitoring de fonctions dans le dashboard OpenFaaS. Source: https://docs.openfaas.com/openfaas-pro/dashboard/</div>

:::link
Pour plus d'informations, voir : <https://docs.openfaas.com/openfaas-pro/dashboard/>
:::

### Prometheus & Grafana

OpenFaaS est prévu pour s'intégrer avec _Prometheus_ et _Grafana_ :

![Monitoring de fonctions dans Grafana](https://docs.openfaas.com/images/grafana/overview-dashboard.png)

<div class="caption">Monitoring de fonctions dans Grafana. Source: https://docs.openfaas.com/openfaas-pro/grafana-dashboards/</div>

:::link
Voir aussi :

- Les métriques Prometheus : <https://docs.openfaas.com/architecture/metrics/>
- Le dashboard Grafana : <https://docs.openfaas.com/openfaas-pro/grafana-dashboards/>
:::

## 📜 Gestion des informations sensibles (secrets) et de la configuration (variables d'environnement)

:::link
Voir la documentation officielle :

- https://github.com/openfaas/workshop/blob/master/lab10.md
- https://docs.openfaas.com/cli/secrets/
:::

### 📦 Secrets

OpenFaaS propose une gestion des `secrets` (qui utilise les `Secret` de Kubernetes) :

```sh
echo -n "super-secret-password" | faas-cli secret create mon-password
```

```yaml
functions:
  save-function:
    lang: python3
    handler: ./ma-function
    image: <your-registry>/ma-function:latest
    secrets:
      - mon-password
```

- Dans le code Python, ce secret peut être lu comme un **fichier** :

```python
def get_secret(secret_name):
    path = f"/var/openfaas/secrets/{secret_name}"
    with open(path, "r") as f:
        return f.read().strip()

password = get_secret("mon-password")
```

**Avantage** 🌟 : Le secret **n'est jamais visible** dans le YAML, ni injecté comme variable d’environnement.

### ⚙️ Configurations externes simples

Pour des paramètres non critiques il est possible d'utiliser directement les **variables d'environnement** :

```yaml
functions:
  save-function:
    environment:
      MINIO_URL: "minio.openfaas:9000"
      MINIO_BUCKET: "processed-images"
```

```python
import os

minio_url = os.getenv("MINIO_URL", "default-value")
bucket = os.getenv("MINIO_BUCKET", "default-bucket")
```

### 🛠️ ConfigMaps Kubernetes

Pour des **fichiers de configuration** ou des **blocs volumineux** (ex: listes de serveurs, politiques d'accès, etc.), il est préférable de passer par un `ConfigMap` Kubernetes monté comme un `Volume` dans la fonction OpenFaaS :

```sh
kubectl create configmap my-config --from-file=config.yaml
```

```yaml
functions:
  save-function:
    lang: python3
    handler: ./ma-function
    image: <your-registry>/ma-function:latest
    annotations:
      com.openfaas.volume.mount: "image-config:/var/config"
    environment:
      CONFIG_PATH: "/var/config/config.yaml"
```

```python
import os
import yaml #pyyaml

def handle(event, context):
    config_path = os.getenv("CONFIG_PATH", "/var/config/config.yaml")

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        endpoint = config['storage']['endpoint']
        bucket = config['storage']['bucket']
        region = config['storage']['region']

        return f"Config loaded: endpoint={endpoint}, bucket={bucket}, region={region}"

    except Exception as e:
        return f"Error loading configuration: {str(e)}"
```

## Chaînage de fonctions

Une fonction simple sans contexte n'est pas très représentative d'un vrai programme. Nous allons créer un exemple simple de chaîne de fonctions OpenFaaS en utilisant plusieurs fonctions qui s’enchaînent les unes après les autres via des appels HTTP. Nous allons créer deux fonctions pour cet exemple :

- `uppercase()` : prend un texte en entrée et renvoie le texte en majuscules.
    ```python
    def handle(event, context):
        return {"statusCode": 200, "body": event.body.upper()}
		```
- `reverse()` : prend le texte transformé en majuscules et le renverse.
    ```python
    def handle(event, context):
        return {"statusCode": 200, "body": event.body[::-1]}
		```

Il suffit alors de créer une 3e fonction réalisant la logique métier des appels :

```python
import requests


def handle(event, context):
    gateway_url = "http://gateway.openfaas:8080/function"

    try:
        uppercased = requests.post(f"{gateway_url}/uppercase", data=event.body)
        if uppercased.status_code != 200:
            return f"Unable to uppercase text: {uppercased.text}"
        reversed = requests.post(f"{gateway_url}/reverse", data=uppercased.text)
        if reversed.status_code == 200:
            return reversed.text
        else:
            return f"Unable to reverse text: {reversed.text}"
    except Exception as e:
        return f"Unable to transform text: {e}"

```

:::tip
Pour ajouter une nouvelle fonction dans la stack actuelle (après avoir créé la 1ere fonction), effectuer la commande suivante :

```sh
faas-cli new reversed --prefix mon_user_dockerhub --lang python3-http --append stack.yaml
```
:::

:::tip
Pourquoi ne pas appeler directement `reverse()` depuis `uppercase()` ? Le but est de garder des fonctions _pures_ au maximum (sans effet de bord), ainsi il sera plus facile de débugger un problème dans la fonction, la tester, migrer vers un pattern asynchrone, …
:::

## Scaling automatique

Le **scaling automatique** est un des atouts majeurs d'OpenFaaS. Celui-ci utilise un **AutoScaler** intégré appelé **faas-netes** (qui utilise un `HorizontalPodAutoscaler` de Kubernetes).

:::tip
Il est aussi possible de faire de l'auto-scaling sans Kubernetes en utilisant **faasd**.
:::

- Si **des requêtes arrivent**, OpenFaaS crée **plus d'instances** de la fonction (i.e. plus de _Pod_ Kubernetes).
- Si **plus personne** n'appelle la fonction pendant un certain temps, OpenFaaS **réduit automatiquement** le nombre d'instances
- Le scaling se configure avec des annotations :

```yaml
functions:
  watermark-function:
    lang: python3
    handler: ./ma-function
    image: <your-registry>/ma-function:latest
    annotations:
      com.openfaas.scale.min: "1"
      com.openfaas.scale.max: "10"

```

:::link
Voir aussi :
- La documentation officielle : <https://docs.openfaas.com/architecture/autoscaling/>
- [un lab openfaas](https://github.com/openfaas/workshop/blob/master/lab9.md)
:::

### Tester l'auto-scaling

Pour tester l'auto-scaling, déployer la fonction `go-echo` :

```sh
git clone https://github.com/alexellis/echo-fn \
 && cd echo-fn \
 && faas-cli template store pull golang-http \
 && faas-cli deploy \
  --label com.openfaas.scale.max=5 \
  --label com.openfaas.scale.min=1
```

Puis effectuer un test de charge :

```sh
for i in {0..10000}; do echo -n "Post $i" | faas-cli invoke go-echo && echo; done;
```

### Scale-to-zero

- Si `openfaas-idler` est installé, il est possible de faire du **scale-to-zero** (comme _AWS Lambda_) : la fonction ne consomme plus aucune ressource après X minutes d'inactivité.
- Par défaut, `openfaas-idler` éteint une fonction après 5 minutes d'inactivité.
- Attention au coût du redémarrage : **cold start**.
- La configuration se fait par les variables d'environment :
  - `inactivityDuration` : Temps d'inactivité avant extinction
  - `reconcileInterval` : Fréquence de vérification

```yaml
functions:
  watermark-function:
    lang: python3
    handler: ./ma-function
    image: <your-registry>/ma-function:latest
    annotations:
      com.openfaas.scale.min: "0"
      com.openfaas.scale.max: "10"
    environment:
      inactivityDuration: "2m"
      reconcileInterval: "30s"
```

:::link
Voir faas-idler : <https://github.com/cuulee/faas-idler>
:::

## 🔥 Connecter OpenFaaS à des **événements automatiques** (triggers)

OpenFaaS peut réagir à plusieurs types d'événements externes grâce à un composant appelé **OpenFaaS Event Connector**, ou en utilisant des **triggers** comme :

- des **CronJobs** (*fonction planifiée*)
- des **messages Kafka, NATS, MQTT** (*événements temps réel*)
- ou même **des webhooks GitHub, GitLab** (*CI/CD déclenché par un commit*)

:::link
Voir aussi la doccumentation officielle :
- sur le _triggers_ : <https://docs.openfaas.com/reference/triggers/>
- sur les fonctions asynchrones : <https://docs.openfaas.com/reference/async/>
:::

### Exemple : Planifier une fonction avec **Cron-Connector**

Le **Cron-Connector** est un petit service qui utilise des expressions **cron** pour appeler des fonctions OpenFaaS à intervalle régulier.

#### Installation

Déployer le cron-connector qui crée un Pod `cron-connector` dans le cluster qui écoute les planifications.

```sh
arkade install cron-connector
```

On peut par exemple exécuter la fonction disponible `NodeInfo` dans le store pour avoir des informations sur le _Node_ toutes les 5 minutes :

```sh
faas-cli store deploy nodeinfo \
  --annotation schedule="*/5 * * * *" \
  --annotation topic=cron-function

kubectl logs deploy/cron-connector -n openfaas
```

#### Exécution de la fonction de test toutes les 2 minutes

Modifier le fichier `stack.yml` de la fonction précédente pour y ajouter une annotation de _scheduling_ :

```yaml
functions:
  hello-openfaas:
    lang: python3
    handler: ./hello-openfaas
    image: <dockerhub-username>/hello-openfaas:latest
    annotations:
      com.openfaas.schedule: "*/2 * * * *"
```

Ici, `*/2 * * * *` signifie **toutes les 2 minutes**.

Puis on redéploie la fonction :

```sh
faas-cli up
```

```console
$ kubectl logs deploy/cron-connector -n openfaas

2025/04/28 12:31:15 Version: 43c31dbb873719753cd4bd53e175435d2c6c5274	Commit: 0.7.0
2025/04/28 12:31:15 Gateway URL: http://gateway.openfaas:8080
2025/04/28 12:31:15 Async Invocation: false
2025/04/28 12:31:15 Rebuild interval: 30s	Rebuild timeout: 5s
2025/04/28 12:32:15 Added: nodeinfo.openfaas-fn [*/5 * * * *]
2025/04/28 12:35:00 Invoking: nodeinfo.openfaas-fn [*/5 * * * *]
2025/04/28 12:35:00 Response: nodeinfo [200] (29ms)
2025/04/28 12:38:15 Added: hello-openfaas.openfaas-fn [*/2 * * * *]
2025/04/28 12:40:00 Invoking: nodeinfo.openfaas-fn [*/5 * * * *]
2025/04/28 12:40:00 Invoking: hello-openfaas.openfaas-fn [*/2 * * * *]
2025/04/28 12:40:00 Response: hello-openfaas [200] (8ms)
2025/04/28 12:40:00 Response: nodeinfo [200] (9ms)
```

:::tip
D'autres types de connecteurs plus poussés existent : _Kafka Connector_ pour écouter un _topic_ Kafka, …
:::

:::warn
Attention, certains triggers sont réservés à la licence professionnelle !
:::

## Intégration avec des services externes

### Bonnes pratiques générales

- **Secrets** jamais hardcodés dans le code source.
- **Timeouts** et **retry** dans les appels réseau.
- **Limiter les permissions** de la fonction (ex: RBAC minimal si besoin).
- **Valider toutes les entrées utilisateur**.

### Se connecter à MySQL depuis une fonction Python

**Déployer un secret :**

```sh
echo -n "superpassword" | faas-cli secret create mysql-password
```

**Dans `stack.yml` de la fonction :**

```yaml
functions:
  my-db-function:
    image: my-db-function:latest
    secrets:
      - mysql-password
    environment:
      db_host: "mysql.svc.cluster.local"
      db_user: "admin"
```

**Dans la fonction Python :**

```python
import os
import mysql.connector

def handle(event, context):
    conn = mysql.connector.connect(
        host=os.environ.get('db_host'),
        user=os.environ.get('db_user'),
        password=open('/var/openfaas/secrets/mysql-password').read()
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    results = cursor.fetchall()
    return str(results)
```

### 📨 Intégration avec un **système de messagerie** : envoyer un message RabbitMQ depuis une fonction Node.js

**Même principe** :

- Stocker l'URL, credentials dans secrets/configmaps.
- Utiliser un client de messagerie dans la fonction.

**Secrets** :
```sh
echo -n "amqp://user:password@rabbitmq.svc.cluster.local" | faas-cli secret create rabbitmq-url
```

**stack.yml** :

```yaml
functions:
  send-msg:
    image: send-msg:latest
    secrets:
      - rabbitmq-url
```

**Code Node.js :**

```javascript
const amqp = require('amqplib');

module.exports = async (event, context) => {
    const url = require('fs').readFileSync('/var/openfaas/secrets/rabbitmq-url', 'utf8');
    const conn = await amqp.connect(url);
    const ch = await conn.createChannel();
    await ch.assertQueue('myqueue');
    ch.sendToQueue('myqueue', Buffer.from(event.body));
    await ch.close();
    await conn.close();
    return context.status(200).succeed('Message sent!');
};
```

### 🌎 Appeler une **API externe** OpenWeather en Python

**Secret** :

```sh
echo -n "my_openweather_token" | faas-cli secret create openweather-token
```

**stack.yml** :

```yaml
functions:
  weather:
    image: weather-fn:latest
    secrets:
      - openweather-token
    environment:
      api_url: "http://api.openweathermap.org/data/2.5/weather"
```

**Fonction Python :**

```python
import os
import requests

def handle(event, context):
    token = open('/var/openfaas/secrets/openweather-token').read().strip()
    city = event.body or 'Paris'
    url = f"{os.environ.get('api_url')}?q={city}&appid={token}"
    response = requests.get(url, timeout=5)
    return response.text
```

## 📜 Créer un **template personnalisé**

Créer ou utiliser des **templates personnalisés** dans OpenFaaS est une pratique très puissante pour adapter son environnement de fonctions.

Un **template** OpenFaaS est **l'ossature** d'une fonction :  il fournit tout ce qui est nécessaire pour construire l'image Docker d'une fonction **sans avoir à tout écrire soi-même**.

Un template contient :

- Un **Dockerfile** de base
- Un **handler** préconfiguré
- Un **processus de build** standardisé
- La **manière** d’exécuter le code (Python, Node.js, Go, etc.)

Cas d'usage typiques : ajouter des dépendances systèmes, changer la version du runtime (Python, …) , supporter des frameworks spécifiques (_Django_, _FastAPI_, …), ajouter du monitoring intégré, optimiser les tailles d'images

Un template est un dossier ayant comme structure :

```
template/
  mon-template/
    Dockerfile
    template.yml
    function/ # contenu par défaut des nouvelles fonctions (optionel)
```

```dockerfile
# Dockerfile
FROM python:3.12-slim

RUN pip install --no-cache-dir flask

# Copy function code
COPY function/ /function/

WORKDIR /function/

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

ENV fprocess="python index.py"
CMD ["fwatchdog"]
```

**Explication** :

- `fprocess` ➔ ce que le watchdog (serveur HTTP interne OpenFaaS) exécute.
- `fwatchdog` ➔ petit serveur qui reçoit les appels HTTP et lance la fonction.

```yaml
# template.yml
language: mon-python-custom
fprocess: "python index.py"
```

:::warn
`fprocess` est critique : démarrer directement le serveur ou le script (éviter `ENV fprocess="cd /somewhere && source env/bin/activate && python complicated.py" && …`)
:::

:::tip
Pour **accélérer les cold start**, utiliser des images légères (`slim`, `alpine`, `distroless`) si possible.
:::


## ➡️ Utilisation

```sh
faas-cli new ma-fonction --lang mon-python-custom
```

# 🚀 Exemple de pipeline serverless de Traitement d'Images

## Objectif

1. L'utilisateur **upload** une image.
2. Une fonction **redimensionne** l'image.
3. Une autre fonction **ajoute un filigrane (watermark)**.
4. Enfin, une fonction **enregistre** l'image modifiée dans un stockage (par exemple, MinIO/S3).

## ⚙️ Architecture du flux

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

Chaque étape est totalement découplée et utilise un **appel HTTP** ou un **publish-event** (au choix) pour interconnecter les fonctions.

## 📦 Fonctions du projet

| Fonction            | Rôle                                  | Input                         | Output               |
|---------------------|----------------------------------------|-------------------------------|----------------------|
| `upload-function`    | Reçoit une image (via HTTP POST)       | Image brute                   | Événement "Uploaded" |
| `resize-function`    | Redimensionne l'image (ex: 800px max)  | Image uploadée                | Événement "Resized"  |
| `watermark-function` | Ajoute un filigrane "© MyCompany"      | Image redimensionnée          | Événement "Watermarked" |
| `save-function`      | Sauvegarde l'image finale dans MinIO/S3 | Image watermarked             | Succès/Échec         |

## 🛠️ Mise en œuvre

### Créer les fonctions

Par exemple pour `resize-function` :

```sh
faas-cli new resize-function --lang python3-http
```

**Exemple simplifié de `resize-function/handler.py`** :

```python
from PIL import Image
import io

def handle(event, context):
    img = Image.open(io.BytesIO(event.body))
    img.thumbnail((800, 800))
    
    output = io.BytesIO()
    img.save(output, format='JPEG')
    
    return output.getvalue()
```

:::tip
Penser à ajouter la librairie **Pillow** dans les `requirements.txt` (pour manipuler les images).
:::

**Exemple simplifié de `watermark/handler.py`** :

```python
from PIL import Image, ImageDraw, ImageFont
import io


def handle(event, context):
    """
    Ajoute un watermark à une image reçue en POST.
    """
    try:
        # Charger l'image depuis l'entrée binaire
        image = Image.open(io.BytesIO(event.body)).convert("RGB")

        # Dessiner le watermark
        draw = ImageDraw.Draw(image)
        watermark_text = "© MySuperCompany"
				font = ImageFont.load_default()

        # Position : en bas à droite
        x = image.width - 100
        y = image.height - 10

        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255))

        # Retourner l'image modifiée
        output = io.BytesIO()
        image.save(output, format="JPEG")
        return output.getvalue()

    except Exception as e:
        return f"Error adding watermark: {e}"
```


### Connecter les fonctions

Il est possible de chaîner les appels **manuellement** dans chaque fonction (via HTTP) **ou** d'utiliser des événements + connecteurs (comme Kafka).

**Exemple simple dans `upload-function` :**

Après avoir uploadé l'image, la fonction appelle directement `resize-function` :

```python
import requests


def handle(event, context):
    """
    Upload d'une image et appel de la fonction de redimensionnement.
    """
    # Adresse interne OpenFaaS Gateway (service Kubernetes)
    gateway_url = "http://gateway.openfaas:8080/function"

    # On _forward_ directement l'image brute au resize
    try:
        resized = requests.post(f"{gateway_url}/resize-function", data=event.body)
        if resized.status_code != 200:
            return f"Error forwarding image: {resized.text}"
        watermarked = requests.post(f"{gateway_url}/watermark", data=resized.content)
        if watermarked.status_code != 200:
            return f"Error watermarking image: {watermarked.text}"
        saved = requests.post(f"{gateway_url}/save-minio", data=watermarked.content)
        if saved.status_code != 200:
            return f"Error saving image: {saved.text}"
        return saved.content
    except Exception as e:
        return f"Upload failed: {e}"

```

### Stockage (facultatif)

Pour enregistrer les images transformées, nous allons déployer **MinIO** dans le cluster. MinIO permet de créer un stockage de type _S3_ (compatible avec les _Buckets_ d'Amazon Cloud).

#### Installation de MinIO

```sh
# Installation du serveur
arkade install minio

# Configuration du serveur
MINIO_ROOT_USER=$(kubectl get secret -n default minio -o jsonpath="{.data.root-user}" | base64 -d; echo)
MINIO_ROOT_PASS=$(kubectl get secret -n default minio -o jsonpath="{.data.root-password}" | base64 -d; echo)
arkade get mc

kubectl port-forward svc/minio 9000:9000 & # accès local à minio pour test
mc config host add minio http://127.0.0.1:9000 $MINIO_ROOT_USER $MINIO_ROOT_PASS
```

Et dans `save-function`, utiliser le SDK MinIO pour uploader l'image vers un bucket.

#### Exemple

**Exemple simplifié de `save-minio/handler.py`** :

```python
import io
import os
import uuid
from minio import Minio
from minio.error import S3Error


def handle(event, context):
    """
    Sauvegarde une image reçue dans un bucket MinIO.
    """
    try:
        # Paramètres de connexion MinIO
        minio_url = os.getenv("MINIO_URL", "minio.openfaas:9000")
        minio_access_key = os.getenv("MINIO_ACCESS_KEY", "admin")
        minio_secret_key = os.getenv("MINIO_SECRET_KEY", "password")
        bucket_name = os.getenv("MINIO_BUCKET", "processed-images")

        # Connexion au serveur MinIO
        client = Minio(
            minio_url,
            access_key=minio_access_key,
            secret_key=minio_secret_key,
            secure=False,  # http, pas https dans ce contexte
        )

        # S'assurer que le bucket existe
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)

        # Générer un nom de fichier unique
        object_name = f"{uuid.uuid4()}.jpg"

        # Enregistrer l'image dans MinIO
        client.put_object(
            bucket_name,
            object_name,
            io.BytesIO(event.body),
            length=len(event.body),
            content_type="image/jpeg",
        )

        return f"Image saved as {object_name} in bucket {bucket_name}."

    except S3Error as e:
        return f"S3 Error: {e}"
    except Exception as e:
        return f"Cannot save : {e}"
```

## 🧠 Résultat

- L'utilisateur **upload** une image.
- Les **fonctions serverless** exécutent le travail automatiquement, étape par étape.
- L'**architecture est découplée, évolutive, et maintenable**.

:::note
Il reste cependant encore beaucoup de choses à améliorer :

- Utiliser **Kafka Connector** pour lier les fonctions sans couplage direct (plus propre).
- Ajouter de l'**authentification JWT** au niveau de l'API Gateway OpenFaaS.
- Mettre en place de l'**autoscaling** sur les fonctions selon la charge.
- Faire du **versionning d'images** ou une **file d'attente de traitement**.
:::

:::tip
Pour tester l'application, on pourra envoyer une image entière au format binaire :

```sh
curl --data-binary @/chemin/vers/mon/image.jpg http://127.0.0.1:8080/function/upload
```
:::

## Liens

:::link
- Voir aussi, un podcast sur sur le serverless : _Beyond Kubernetes: Serverless Execution Models for Variable Workloads_ : <https://kube.fm/kubernetes-vs-lambda-marc>
:::
