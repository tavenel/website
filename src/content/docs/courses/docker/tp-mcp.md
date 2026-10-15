---
title: Découverte et prise en main de MCP avec Docker
date: 2025 / 2026
type: tp
sidebar:
  order: 250
description: Découverte et prise en main de MCP avec Docker
---
## 🎯 Objectifs pédagogiques

- Définir le rôle du **Model Context Protocol (MCP)**
- Comprendre l'intérêt de **Docker** pour encapsuler un serveur MCP
- Déployer un serveur MCP minimal
- Exposer un **tool MCP simple**
- Interagir avec le serveur MCP via un client LLM
- Identifier les cas d'usage possibles de MCP

## 📌 Contexte

Les modèles de langage (LLM) sont puissants, mais **ne peuvent pas accéder directement** aux systèmes, fichiers ou API internes d'une organisation.

Le **Model Context Protocol (MCP)** permet de résoudre ce problème en standardisant la façon dont un LLM :

- découvre des outils,
- consomme des ressources,
- interagit avec des services externes.

Dans ce TP, vous allez **conteneuriser un serveur MCP** et lui exposer progressivement des capacités simples.

## 🧱 Architecture cible

```
┌─────────────────┐
│ Client LLM      │
│ (Claude / CLI)  │
└────────┬────────┘
         │ MCP
┌────────▼────────┐
│ Serveur MCP     │  ← Docker
│ (Python / Node) │
└────────┬────────┘
         │
 ┌───────▼──────────────┐
 │ Outils & Contextes   │
 │ - Fichiers           │
 │ - API REST           │
 │ - Commandes système  │
 └──────────────────────┘
```

## 🧪 Comprendre MCP

> MCP est un protocole standard permettant à un LLM de découvrir et d'appeler des outils externes de manière structurée et sécurisée.

En utilisant un LLM, répondre aux questions suivantes :

- Quel est le rôle d'un **MCP Server** ?
- Quelle différence entre un **tool** et une **resource** ?
- Pourquoi MCP est-il indépendant du modèle de langage ?

:::correction
**1. Rôle d'un MCP Server**
Un serveur MCP est un **intermédiaire standardisé** entre un modèle de langage et des capacités externes (outils, fichiers, API). Il expose explicitement ce que le LLM a le droit de faire, sous une forme structurée et contrôlée.

**2. Différence entre tool et resource** :

- **Tool** : action exécutable (fonction, appel API, calcul, requête)
- **Resource** : donnée statique ou semi-statique (fichier, documentation, configuration)

**3. Pourquoi MCP est indépendant du LLM**
Le protocole est agnostique du modèle : n'importe quel LLM compatible MCP peut consommer les mêmes outils sans modification côté serveur.
:::

## 🐳 Mise en place du projet Docker

:::exo

1. Créer l'arborescence suivante :

```
mcp-docker-tp/
├─ server/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
└─ docker-compose.yml
```

2. Installer une implémentation MCP en Python
3. Compléter le `Dockerfile` :
   - image de base Python
   - installation des dépendances
   - lancement du serveur MCP
4. Construire et lancer le conteneur

   ```bash
   docker compose up --build
   ```

5. Vérifier les logs

:::

:::correction

### `requirements.txt`

```txt
# requirements.txt
mcp
psutil
```

### `app.py`

```py
# app.py
exit
```

### `Dockerfile`

```dockerfile
# Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
```

### `compose.yml`

```yaml
# compose.yml
services:
  mcp-server:
    build: ./server
    container_name: mcp-server
    volumes:
      - ./data:/data
    ports:
      - "3333:3333"
```

### Lancement

```bash
docker compose up --build
```

:::

## 🔧 Premier serveur MCP minimal

Objectif : Créer un serveur MCP **fonctionnel mais minimal**.

:::exo

1. Implémenter un serveur MCP exposant un _tool_ `hello`
2. Le tool retourne :
   - un message statique
   - le nom du conteneur
3. Tester l'appel depuis le client LLM : `StreamableHTTP`, `Connection Type: via proxy`, `URL:` : <http://localhost:8000/mcp> :

  ```sh
  DANGEROUSLY_OMIT_AUTH=true npx -y @modelcontextprotocol/inspector
  ```

:::

### Exemple attendu

```json
{
  "message": "Hello from MCP",
  "container": "mcp-server"
}
```

:::correction

### `app.py`

[TODO]

```python
# app.py
from mcp.server import Server
from mcp.types import Tool, TextContent
import socket

server = Server("demo-mcp-server")

@server.tool(
    name="hello",
    description="Retourne un message de bienvenue depuis le serveur MCP"
)
def hello():
    return [
        TextContent(
            type="text",
            text=f"Hello from MCP running in container {socket.gethostname()}"
        )
    ]

if __name__ == "__main__":
    server.run(port=3333)
```

:::

## 🖥️ Exposer un tool système

Objectif : Permettre au LLM d'interroger des informations système simples.

:::exo

1. Ajouter un tool MCP `system_info`
2. Le tool retourne :
   - nom de l'OS
   - version Python
   - uptime du conteneur
3. Vérifier que :
   - aucune commande arbitraire n'est possible
   - les sorties sont structurées (JSON)

:::

:::tip
Pourquoi est-il dangereux d'exposer directement une commande shell au LLM ?
:::

:::correction

### Réponse à la question guidée

**Pourquoi ne pas exposer un shell directement ?**
Parce qu'un LLM pourrait :

- exécuter des commandes destructrices
- exfiltrer des données
- compromettre l'hôte ou le cluster

MCP impose une **surface d'attaque minimale**.
:::

## 📄 Exposer une resource MCP

Objectif : Permettre au LLM de lire un fichier local.

:::exo

1. Créer un fichier `data/info.txt`
2. Monter ce fichier comme volume Docker
3. Exposer une **resource MCP** : `info_file`
4. Permettre au LLM de :
   - lire le contenu
   - le résumer

## 🔐 Sécurité et isolation

:::exo
Répondre aux questions suivantes :

1. Quel est l'intérêt de Docker dans ce TP ?
2. Que se passerait-il si MCP tournait directement sur l'hôte ?
3. Quels types de tools ne devraient jamais être exposés ?
4. Comment limiter les risques (permissions, sandbox, RBAC) ?

:::

:::correction
**1. Rôle de Docker**

- Isolation du runtime
- Contrôle des volumes
- Limitation de l'impact en cas de compromission

**2. MCP sans Docker**

- Accès direct au système hôte
- Risque majeur d'escalade de privilèges

**3. Tools à ne jamais exposer**

- Shell générique
- Accès réseau arbitraire
- Accès aux secrets bruts

**4. Bonnes pratiques**

- Principe du moindre privilège
- Tools très spécifiques
- Validation stricte des entrées
- Logs et audit

:::

## 🚀 Pour aller plus loin (facultatif)

- Ajouter un second service via `docker-compose`
- Ajouter une authentification simple
- Exposer une API REST externe
- Déployer le serveur MCP sur Kubernetes

[TODO]
===

## 🖥️ Étape 4 – Tool système `system_info`

### Implémentation

```python
import platform
import time
import psutil
from datetime import timedelta

@server.tool(
    name="system_info",
    description="Retourne des informations système basiques du conteneur"
)
def system_info():
    uptime_seconds = time.time() - psutil.boot_time()

    return [
        TextContent(
            type="text",
            text=f"""
OS: {platform.system()} {platform.release()}
Python: {platform.python_version()}
Uptime: {timedelta(seconds=int(uptime_seconds))}
"""
        )
    ]
```

---

## 📄 Étape 5 – Resource MCP (fichier local)

:::correction

### Fichier local

`data/info.txt`

```txt
Ce projet démontre l'utilisation de MCP avec Docker.
Il permet à un LLM d'interagir avec des outils et des fichiers locaux
de manière sécurisée et contrôlée.
```

### Ajout de la resource

```python
from mcp.types import Resource

@server.resource(
    name="info_file",
    description="Fichier d'information du projet"
)
def info_file():
    with open("/data/info.txt", "r") as f:
        content = f.read()

    return [
        TextContent(
            type="text",
            text=content
        )
    ]
```

:::

### Résultat attendu

Le LLM peut :

- lire le fichier
- le résumer
- répondre à des questions basées sur son contenu
