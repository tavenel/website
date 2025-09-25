---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: YAML & Jinja2 & Go templates
layout: '@layouts/CoursePartLayout.astro'
---

## YAML

- Format de sérialisation de données lisible par l'humain.
- Très utilisé en _Infrastructure-as-Code_ : _Kubernetes_ (`.yaml`), _Ansible_ (`playbooks`), CI/CD (_GitLab CI_), …
- Linter pour valider un YAML : `yamllint`

### Principes de base

1. **Indentation obligatoire** :
  - espaces (généralement 2), pas de tabulations
  - sensible aux espaces : chaque niveau d’imbrication doit avoir la même indentation

2. **Clés-valeurs** simples :

```yaml
nom: Alice
age: 30
admin: true
```

3. **Listes** :

```yaml
fruits:
  - pomme
  - banane
  - fraise
```

4. **Objets imbriqués** :

```yaml
utilisateur:
  nom: Alice
  roles:
    - admin
    - dev
```

5. **Valeurs spéciales**

* `true/false` (booléen)
* `null` (valeur vide)
* `123` (entier), `1.23` (flottant)

## Jinja2

- **Moteur de templates** en Python.
- Permet de générer dynamiquement du texte (HTML, YAML, configs).
- Utilisé par _Ansible_, _SaltStack_, _Flask_, _Django_, …
- Syntaxe basée sur des **délimiteurs `{{ ... }}`**.

### Syntaxe de base

1. **Variables**

```jinja
Bonjour, {{ utilisateur.nom }} !
```

2. **Conditions**

```jinja
{% if admin %}
Utilisateur avec droits admin
{% else %}
Utilisateur standard
{% endif %}
```

3. **Boucles**

```jinja
{% for fruit in fruits %}
- {{ fruit }}
{% endfor %}
```

4. **Filtres** (pour transformer les données)

```jinja
Nom en majuscules : {{ utilisateur.nom | upper }}
```

## 🐹 Templates Go

- Inclus dans la bibliothèque standard (`text/template` et `html/template`).
- Utilisés pour générer du texte dynamique (fichiers de config, emails, pages HTML, YAML/JSON dynamiques, etc.).
- Syntaxe basée sur des **délimiteurs `{{ ... }}`**.

En DevOps, les Go templates sont partout :

- _Helm_ : génération des `Charts`
- _Prometheus_ / _Alertmanager_ : alertes dynamiques
- _Grafana_ : dashboards dynamiques
- _Vault_ / _Consul_ : injection de secrets et de config
- _ArgoCD_ : pipelines dynamiques
- _Kubernetes_ avec _Kustomize_

### Syntaxe de base

1. **Variables**

```go
Bonjour {{ .Nom }} !
```

:::tip
Le `.` représente l'objet courant (ex: une _structure_ Go ou une _map_).
:::

2. **Boucles**

```go
Liste des fruits :
{{ range .Fruits }}
- {{ . }}
{{ end }}
```

3. **Conditions**

```go
{{ if .Admin }}
Utilisateur avec droits admin
{{ else }}
Utilisateur standard
{{ end }}
```

4. **Filtres** et **Fonctions**

- `len` : longueur d’une liste
- `printf` : formatage

Exemple :

```go
Il y a {{ len .Fruits }} fruits.
```

5. **Inclusion** de sous-templates

```go
{{ define "header" }}<h1>{{ .Titre }}</h1>{{ end }}

{{ template "header" . }}
<p>Contenu principal...</p>
```

### Exemple

```go
package main

import (
    "os"
    "text/template"
)

type Utilisateur struct {
    Nom   string
    Admin bool
}

func main() {
    tmpl := `Bonjour {{ .Nom }}
{{ if .Admin }}Vous êtes administrateur{{ else }}Vous êtes utilisateur{{ end }}`

    data := Utilisateur{"Alice", true}

    t := template.Must(template.New("test").Parse(tmpl))
    t.Execute(os.Stdout, data)
}
```

