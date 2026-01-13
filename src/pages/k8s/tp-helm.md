---
title: Déploiement applicatif avec Helm
date: 2024 / 2025
---

## Introduction

`Helm` est un outil et une CLI de _gestion de paquets_ pour Kubernetes qui permet de déployer et de gérer des applications Kubernetes de manière _déclarative_.

- Les `charts` Helm sont des packages qui encapsulent des configurations Kubernetes, des `templates`, et d'autres ressources nécessaires pour déployer une application.
- Les `charts` sont distribuées en ligne dans des `repositories` (publics ou privés)
  - un repo a un nom sur la machine locale : `helm repo add mon-repo http://…`
    - cela permet de l'utiliser facilement : `helm install ma-release mon-repo/nginx`
- Une instance de la `chart` déployée dans le cluster est appelée `release`. Une `release` est versionnée : (des)installation, upgrade, rollback
- Il est possible d'ajouter des `hooks` autour des `releases` : avant / après installation, upgrade, …

:::warn
Attention : tout comme les images Docker, une chart Helm permet de récupérer des configurations et un packaging distribués en ligne. Il faut donc toujours bien vérifier les charts que l'on utilise (`repository` officiel, …)
:::

:::link

- Voir la [cheatsheet Kubernetes](/k8s/cheatsheet) pour les commandes.
- Voir aussi le [TP Prometheus & Grafana](/k8s/tp-prometheus-grafana) pour apprendre à déployer Prometheus et Grafana en utilisant Helm.
- Voir le lien suivant pour un tutoriel : <https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/helm/>

:::

:::tip

- _Helm_ a beaucoup changé de modèle en passant de la v2 à la v3, notamment en ~~supprimant le besoin d'un serveur `tiller`~~ : attention à ne pas suivre une doc sur Helm v2 !
- En v3, _Helm_ applique un **Three Way Merge** en comparant trois états avant de modifier un objet :
  - Le nouvel état défini dans le manifeste que l'on souhaite appliquer ;
  - L'état actuel de l'objet (état "live") ;
  - Et la dernière configuration appliquée avec succès, stockée dans un secret (`helm history`).
- En v4, _Helm_ suit la nouvelle logique de l'API Kubernetes (depuis la v1.22) en appliquant un **Server Side Apply (SSA)** : chaque modification apportée sur un champ d'un objet se voit attribuer un propriétaire : `kubectl get --show-managed-fields`

:::

### Structure

Une _Chart Helm_ contient au minimum :

- Un répertoire `templates` : fichiers de manifests Kubernetes qui utilisent le système de _templates Go_.
- Un fichier `values.yaml` qui contient les valeurs par défaut (modifiables) pour les templates de la `chart`.
- Un fichier `Chart.yaml` contenant les metadata de la _Chart_ : nom, version, description, …
- Un fichier `README` est conseillé pour `helm show readme …`
- Un fichier `NOTES.txt` peut être ajouté au répertoire `templates/` : il sera affiché à chaque installation / upgrade et **ses tags `{{ … }}` sont évalués**
- Un répertoire `charts/` (optionnel) contenant les dépendances
- Un fichier `values.schema.json` (optionnel) pour valider les `values` passées à l'exécution

### Templates

Les templates de manifests utilisent le système de templates de _Go_ :

- Les _Tags_ sont représentés par : `{{ ... }}`. Ils seront remplacés par leur valeur à l'exécution.
- `{{ .Release.xyz }}` fait référence aux [variables built-in](https://helm.sh/docs/chart_template_guide/builtin_objects/) initialisées par Helm : nom, version, install vs upgrade, …
- `{{ .Values.xyz }}` fait référence aux [values](https://helm.sh/docs/chart_template_guide/values_files/) modifiables
  - `values.yaml` contient leurs valeurs par défaut
  - modifiables à l'installation par `--set xyz=…` ou `--values fichier.yaml`
- `{{ if x }} y {{ end }}`
- `{{ range x }} y {{ end }}` (`.` contient les éléments de l'itération de `x` en cours)
- `{{- x }}`/`{{ x -}}` supprime les espaces à gauche/droite
- `{{ template "x.y" }}` fait référence à un [template nommé](https://helm.sh/docs/chart_template_guide/named_templates/#declaring-and-using-templates-with-define-and-template)
  - `{{ template "x.y" . }}` : Le `.` est le _contexte_ pour ce template (pour transmettre au template les variables du contexte local)

:::link

- Et aussi : toute la bibliothèque [Sprig](http://masterminds.github.io/sprig/) et des ajouts : `lower` `upper` `quote` `trim` `default` `b64enc` `b64dec` `sha256sum` `indent` `toYaml` …
- Pour plus d'information voir [la documentation sur les template Go](https://golang.org/pkg/text/template/).

:::

:::tip
Il est possible d'ajouter des fichiers à la _chart_ (en dehors du répertoire `templates`) accessibles avec `.Files` qui peuvent être transformés en `ConfigMap` ou en `Secrets` avec `AsConfig` et `AsSecrets` : voir [cet exemple dans la doc Helm](https://helm.sh/docs/chart_template_guide/accessing_files/#configmap-and-secrets-utility-functions)
:::

#### Pipelines

- `{{ quote blah }}` peut également être exprimé comme `{{ blah | quote }}`
- Avec plusieurs arguments, `{{ x y z }}` peut être exprimé comme `{{ z | x y }}`)
- Exemple : `{{ .Values.annotations | toYaml | indent 4 }}` : transforme la _map_ `annotations` en _string_ YAML et l'indente avec 4 espaces pour correspondre au contexte

#### Hooks et tests

- _hooks_ : ressources annotées avec `helm.sh/hook : NOM-DU-HOOK` : `pre-install`, `post-install`, `test` [et beaucoup d'autres](https://helm.sh/docs/topics/charts_hooks/#the-available-hooks)
  - `helm.sh/hook: test` => exécuté seulement par `helm test "<ma-release>"`
- Exécution _synchrone_ : attente de la fin d'un _Job_ ou _Pod_
- Utilisation : migrations BDD, backup, notifs, smoke tests, …

### Dépendances

Une _Chart_ peut avoir des dépendances sur d'autres _Chart_ pour éviter de réécrire le même code en utilisant la section `dependencies` de `Chart.yml` :

```yaml
dependencies:
  - name: redis
    version: 11.0.5 # ou version: ">=11, <12"
    repository: https://charts.bitnami.com/bitnami
    condition: redis.enabled # helm install --set redis.enabled=false …
```

:::warn
Les dépendances doivent être mises à jour par : `helm dependency update` : crée un fichier `Chart.lock` et télécharge les dépendances dans le répertoire `charts/`
:::

:::tip
Comment faire si l'on veut récupérer mais modifier la _Chart_ d'une dépendance (et que le `--set …` ne suffit pas) ? Il suffit de :

1. Décompresser la _Chart_ en dépendance dans le répertoire `charts/`
2. Modifier le(s) fichier(s) de la dépendance : `cd charts && tar zxf redis-*.tgz && cd ..`
3. Relancer `helm dependency update`

:::

:::tip
`.Chart.IsRoot` indique si l'on est dans une dépendance (sous-chart) ou dans la _Chart_ principale, par exemple pour rendre le nom de la _Chart_ générique : `{{- if .Chart.IsRoot}}{{ .Release.Name }}{{ else }}{{ .Chart.Name }}{{ end }}`
:::

### Schema

Pour éviter les erreurs de paramètres passés par `--set` ou un fichier `values.yaml` (typos, …) on peut ajouter un fichier [JSON Schema](https://json-schema.org/) à la racine nommé `values.schema.json`.

Par exemple, pour vérifier que `image.repository` est bien un nom d'image valide et que `image.pullPolicy` vaut `Always`, `Never`, ou `IfNotPresent`.

```json
{
  "$schema": "http://json-schema.org/schema#",
  "type": "object",
  "additionalProperties": false, /* protection contre les variables en trop (typos) */
  "properties": {
    "image": {
      "type": "object",
      "additionalProperties": false, /* à ajouter à chaque niveau ! */
      "properties": {
        "repository": {
          "type": "string",
          "pattern": "^[a-z0-9-_]+$"
        },
        "pullPolicy": {
          "type": "string",
          "pattern": "^(Always|Never|IfNotPresent)$"
        }
      } 
    } 
  } 
}
```

## Installer Helm

Exécuter le script suivant pour installer _Helm_. _Helm_ doit être en mesure de communiquer avec l'`APIServer` : le plus simple est donc de l'installer au même endroit que la machine exécutant les commandes `kubectl`.

```sh
curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get-helm-3 | bash
```

## Déployer une chart Helm

1. Ajouter le dépôt.

```sh
helm repo add kubernetes https://kubernetes.github.io/dashboard
# "kubernetes" has been added to your repositories
```

2. Chercher la chart.

```sh
helm search repo kubernetes-dashboard
# NAME                            CHART VERSION APP VERSION DESCRIPTION                                   
# kubernetes/kubernetes-dashboard 7.14.0                    General-purpose web UI for Kubernetes clusters
```

3. Installation de la chart :

- `helm upgrade --install` installe ou met à jour la chart.

```sh
helm upgrade -i my-dashboard kubernetes/kubernetes-dashboard

# Release "my-dashboard" does not exist. Installing it now.
# I0113 13:47:46.289080   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.289108   52883 warnings.go:110] "Warning: unrecognized format \"int32\""
# I0113 13:47:46.289076   52883 warnings.go:110] "Warning: unrecognized format \"int32\""
# I0113 13:47:46.295739   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.296583   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.311456   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.319156   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.323256   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.323876   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.338284   52883 warnings.go:110] "Warning: unrecognized format \"int64\""
# I0113 13:47:46.338305   52883 warnings.go:110] "Warning: unrecognized format \"int32\""
# NAME: my-dashboard
# LAST DEPLOYED: Tue Jan 13 13:47:48 2026
# NAMESPACE: default
# STATUS: deployed
# REVISION: 1
# TEST SUITE: None
# NOTES:
# *************************************************************************************************
# *** PLEASE BE PATIENT: Kubernetes Dashboard may need a few minutes to get up and become ready ***
# *************************************************************************************************
# 
# Congratulations! You have just installed Kubernetes Dashboard in your cluster.
# 
# To access Dashboard run:
#   kubectl -n default port-forward svc/my-dashboard-kong-proxy 8443:443
# 
# NOTE: In case port-forward command does not work, make sure that kong service name is correct.
#       Check the services in Kubernetes Dashboard namespace using:
#         kubectl -n default get svc
# 
# Dashboard will be available at:
#   https://localhost:8443
```

4. Vérifier l'installation

```sh
helm list
# NAME         NAMESPACE REVISION UPDATED                                 STATUS   CHART                       APP VERSION
# my-dashboard default   1        2026-01-13 13:47:48.412406821 +0100 CET deployed kubernetes-dashboard-7.14.0

# Exposition du dashboard sur la machine personnelle
kubectl -n default port-forward svc/my-dashboard-kong-proxy 8443:443
```

Vérifier l'accès au dashboard : <https://localhost:8443>

## Upgrade et rollback

Helm supporte les upgrade et rollback de _Chart_. Pour cela, l'entièreté de la stack est stockée sur le cluster via des `Secret` Kubernetes de `TYPE: helm.sh/release.v1`.

```sh
kubectl get secrets
kubectl describe secret sh.helm.release.v1.ma-release.v1
kubectl get secret sh.helm.release.v1.ma-release.v1 \
      -o go-template='{{ .data.release | base64decode | base64decode }}' \
      | gunzip -c > release-info.json
helm history ma-release
helm upgrade ma-release
helm rollback ma-release
```

## Créer sa propre Helm Chart

Pour créer un template de _Helm Chart_, utiliser la commande :

```sh
helm create "<chart-name>"
# Par exemple :
helm create chart-perso
```

Pour tester la _Chart_ :

```sh
helm install "<ma-release>" "<chart-name>"
# Par exemple :
helm install test1 chart-perso --namespace chart1-v1
```

Pour supprimer la release :

```sh
helm delete test1 --namespace chart1-v1
# Ou idem :
helm uninstall test1 --namespace chart1-v1
```

## Helmfile

Les _Helm Chart_ sont puissantes mais l'on se retrouve vite avec beaucoup de _Chart_ différentes à appliquer, des `values` à passer en paramètres, …
[Helmfile](https://github.com/helmfile/helmfile) permet de gérer tout ceci : _Helm Chart_ locales & distantes (git + hub), _Kustomization_, manifests `yaml`

:::link
Examples: [install essentials on a cluster, Jérôme Petazzoni][helmfile-ex-1], [run a Bento stack, Jérôme Petazzo][helmfile-ex-2]

[helmfile-ex-1]: https://github.com/jpetazzo/beyond-load-balancers/blob/main/helmfile.yaml
[helmfile-ex-2]: https://github.com/jpetazzo/beyond-load-balancers/blob/main/bento/helmfile.yaml
:::

### Structure

- Fichier principal `helmfile.yaml` définissant :
- `repositories` (dépôts Helm distants)
- `releases` (éléments à installer : charts, YAML, etc.)
- `environments` (facultatif : pour différencier production, staging, etc.) : par `values.yaml`

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Helm® is a registered trademark of The Linux Foundation in the United States and/or other countries.
