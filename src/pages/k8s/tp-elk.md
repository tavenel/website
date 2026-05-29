---
title: Logging centralisé d'un cluster Kubernetes
date: 2024 / 2025
---

# Logging centralisé d'un cluster Kubernetes

## Introduction

Le logging centralisé est essentiel dans un environnement `Kubernetes` pour surveiller les applications et diagnostiquer les problèmes. Des solutions comme l'ELK Stack (`Elasticsearch`, `Logstash`, `Kibana`) ou `Fluentd` sont souvent utilisées pour collecter, centraliser, analyser et visualiser les logs des applications et des composants du cluster.

Nous allons voir dans un premier temps comment déployer une stack ELK dans un cluster `Kubernetes`, puis une intégration de `Fluent` et de `Loki` comme systèmes alternatifs de logging.

## Utilisation de l'ELK Stack (`Elasticsearch`, `Logstash`, `Kibana`) pour `Kubernetes`

### Déploiement de l'ELK Stack dans `Kubernetes`

L'ELK Stack est composé de trois principaux composants :

- `Elasticsearch` : Le moteur de recherche et de stockage des logs.
- `Logstash` : L'outil de collecte et de transformation des logs (facultatif).
- `Kibana` : L'interface utilisateur pour visualiser et analyser les logs.

#### Utilisation de `Helm` pour installer l'ELK Stack

`Helm` est souvent la solution la plus simple pour déployer l'ELK Stack.

Ajouter le dépôt `Helm` pour `Elasticsearch` et `Kibana` :

```sh
helm repo add elastic https://helm.elastic.co
helm repo update
```

Installer `Elasticsearch` :

Vous pouvez personnaliser la taille du cluster `Elasticsearch` selon vos besoins.

```sh
helm upgrade --install elasticsearch elastic/elasticsearch --namespace logging --create-namespace
```

Installer `Kibana` :

```sh
helm upgrade --install kibana elastic/kibana --namespace logging
```

Exposer Kibana :

```sh
kubectl port-forward svc/kibana-kibana 5601:5601 -n logging
```

Vous pouvez accéder à `Kibana` en ouvrant un navigateur et en accédant à <http://localhost:5601>.

### Collecte des logs avec Filebeat ou `Logstash`

- `Filebeat` est un outil léger de collecte de logs. Il est souvent utilisé à la place de `Logstash` pour réduire la complexité.
- `Logstash` est un ETL (Extract-Transform-Load) puissant qui peut transformer les logs avant qu'ils soient envoyés à `Elasticsearch`.

#### Installation de Filebeat avec `Helm`

Installer `Filebeat` pour la collecte des logs des pods :

```sh
helm upgrade --install filebeat elastic/filebeat --namespace logging
```

`Filebeat` collecte les logs de tous les pods et les envoie à `Elasticsearch`.

Configurer `Filebeat` pour lire les logs des containers. Ajoutez la configuration suivante dans votre `values.yaml` :

```yaml
filebeatConfig:
  filebeat.yml: |
    filebeat.inputs:
      - type: container
        paths:
          - /var/log/containers/*.log
    output.elasticsearch:
      hosts: ["http://elasticsearch.logging.svc.cluster.local:9200"]
```

Vérifier les logs dans `Kibana` : Une fois que les logs sont envoyés à `Elasticsearch`, vous pourrez les visualiser et les analyser dans `Kibana`.

### Visualisation dans Kibana

Accédez à l'interface `Kibana` à <http://localhost:5601>.

Dans `Kibana`, configurez un `Index Pattern` pour visualiser les logs collectés dans `Elasticsearch` (par exemple, les index `filebeat-*`).

Utilisez `Discover` pour analyser les logs et créer des dashboards de visualisation personnalisés.

## Utilisation de `Fluentd` pour le Logging dans `Kubernetes`

`Fluentd` est un autre collecteur de logs populaire, souvent utilisé en combinaison avec `Elasticsearch` et `Kibana` (ou un autre backend comme `Fluent-bit`).

### Déploiement de `Fluentd` dans `Kubernetes`

`Fluentd` peut être configuré pour lire les logs des pods et les envoyer à `Elasticsearch` (ou à une autre destination).

#### Installer `Fluentd` avec `Helm`

Ajouter le dépôt `Helm` `Fluentd` :

```sh
helm repo add fluent https://fluent.github.io/helm-charts
helm repo update
```

Installer `Fluentd` avec une configuration pour envoyer les logs à `Elasticsearch` :

```sh
helm upgrade --install fluentd fluent/fluentd --namespace logging
```

Configurer `Fluentd` pour envoyer les logs vers `Elasticsearch` :

Créez ou modifiez le fichier de configuration `Fluentd` pour spécifier la destination `Elasticsearch` :

```yaml
fluentdConfig:
  fluent.conf: |
    <source>
      @type tail
      path /var/log/containers/*.log
      pos_file /var/log/fluentd-containers.log.pos
      tag kubernetes.*
      <parse>
        @type json
      </parse>
    </source>

    <match kubernetes.**>
      @type elasticsearch
      host elasticsearch.logging.svc.cluster.local
      port 9200
      logstash_format true
      include_tag_key true
      tag_key @log_name
      flush_interval 5s
    </match>
```

Vérifier les logs dans `Elasticsearch`/`Kibana` : Une fois `Fluentd` configuré, les logs des pods seront envoyés à `Elasticsearch` et visualisés dans `Kibana` comme précédemment.

### Utilisation de Fluent-bit pour une Collecte Légère

`Fluent-bit` est une version allégée de `Fluentd`, souvent utilisée pour collecter les logs dans des environnements à ressources limitées.

#### Installer `Fluent-bit` avec Helm :

```sh
helm upgrade --install fluent-bit stable/fluent-bit --namespace logging
```

Configurer `Fluent-bit` pour lire les logs des containers et les envoyer à `Elasticsearch` :

```yaml
outputs:
  - name: es
    match: "*"
    host: elasticsearch.logging.svc.cluster.local
    port: 9200
    index: fluent-bit
```

## Comparaison ELK Stack vs Fluentd

ELK Stack est une solution complète et robuste pour le logging, avec de puissantes capacités d'analyse des logs via `Kibana`.
`Fluentd` ou `Fluent-bit` sont des alternatives plus légères pour collecter et envoyer les logs, souvent utilisées pour des configurations à plus faible consommation de ressources.
Le choix entre ces deux solutions dépend de vos besoins en termes de performance, de flexibilité, et de ressources disponibles dans votre cluster `Kubernetes`.

| Critère                      | **ELK Stack (Elastic + Logstash + Kibana)**                              | **Fluentd/Fluent-bit**                                        |
|------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------|
| **Performance**               | Puissant mais gourmand en ressources (surtout Logstash).                | Fluentd/Fluent-bit sont plus légers, particulièrement Fluent-bit. |
| **Complexité**                | Plus complexe à configurer (surtout avec Logstash).                     | Fluent-bit est plus simple et léger à configurer.              |
| **Visualisation**             | Utilise Kibana pour des dashboards sophistiqués.                        | Peut être utilisé avec Kibana, mais il existe aussi d'autres options. |
| **Transformation des Logs**   | Logstash permet une transformation des logs très poussée.               | Fluentd peut transformer les logs, mais Fluent-bit est plus limité. |
| **Popularité**                | Très populaire, utilisé dans de nombreux environnements de production.  | Utilisé souvent dans des environnements à faible consommation de ressources. |
| **Utilisation de la Mémoire** | Utilisation mémoire plus élevée.                                        | Utilisation mémoire plus faible.                              |

## Loki

`Loki` est un système de gestion et d'agrégation de logs développé par Grafana Labs, conçu pour collecter, stocker et analyser les journaux d'applications. Contrairement à d'autres systèmes de gestion de logs comme ELK (`Elasticsearch`, `Logstash`, `Kibana`), `Loki` est beaucoup plus léger et est particulièrement adapté pour une intégration native avec `Prometheus` et `Grafana`.

### Installation de Loki dans Kubernetes

Une façon courante d'installer `Loki` est d'utiliser `Helm` : voir <https://grafana.com/docs/loki/latest/setup/install/helm/install-monolithic/> pour un déploiement de test (utilisant comme stockage le filesystem, un mode scalable requiert du stockage S3).

:::link
Pour tester Loki facilement, on pourra s'inspirer de : <https://linuxblog.xyz/posts/grafana-loki/>
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Prometheus® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Helm® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Grafana® is a registered trademark of Raintank, Inc. dba Grafana Labs ("Grafana Labs").


