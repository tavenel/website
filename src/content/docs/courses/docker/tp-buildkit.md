---
title: Docker buildx
date: 2025 / 2026
type: tp
sidebar:
  order: 105
description: Docker buildx
---
## 🎯 Objectifs pédagogiques

- Comprendre le rôle de `docker buildx` et du builder multi-plateforme.
- Savoir créer et utiliser un builder personnalisé.
- Construire et publier des images multi-architecture.
- Utiliser le cache de build.
- Intégrer des secrets dans le build sans les exposer.

## Mise en place de `buildx`

:::caution
Vous devez avoir Docker 19.03+ pour `buildx`.
:::

:::exo

1. Vérifier la version de Buildx
2. Créer un builder dédié avec build multi-arch

:::

:::correction

### Vérifier la version de Docker

```sh
docker --version
docker buildx version
```

### Créer un builder dédié

```sh
docker buildx create --name mybuilder --use
docker buildx inspect --bootstrap
```

- `--bootstrap` initialise les workers QEMU pour l'émulation multi-arch.

### Lister les builders existants

```sh
docker buildx ls
```

✅ Vérifier que `mybuilder` est actif (`*` dans la liste).
:::

## Construction multi-architecture

:::exo
Builder le fichier `Dockerfile` ci-dessous en multi-architecture.
:::

```dockerfile
# Dockerfile

FROM alpine:3.19
RUN echo "Hello from $(uname -m)!" > /message.txt
CMD cat /message.txt
```

:::correction

- Commande de build et push :

```sh
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t "<compte_docker>/hello-multi:1.0" \
  --push .
```

- Vérification :

```sh
docker buildx imagetools inspect "<compte_docker>/hello-multi:1.0"
```

✅ Le manifest doit afficher **2 architectures** (`amd64` et `arm64`).
:::

## Utilisation du cache de build

:::exo

1. Ajouter une étape lente dans le Dockerfile (voir ci-dessous)
2. Réaliser un 1er build avec cache exporté
3. Relancer le même build : celui-ci doit être quasi instantané.

:::

```dockerfile
# Dockerfile

FROM alpine:3.19
RUN apk add --no-cache curl
RUN sleep 5 && echo "Cache test"
```

:::correction

```sh
docker buildx build \
  --platform linux/amd64 \
  -t cache-demo:1.0 \
  --cache-to=type=local,dest=.buildxcache \
  --cache-from=type=local,src=.buildxcache \
  --load .
```

:::

## Build avec secrets

Voici un Dockerfile affichant un secret :

```dockerfile
# Dockerfile

FROM alpine:3.19
RUN echo "API Key: $(cat /run/secrets/api_key)"
```

:::exo

1. Créer un fichier secret
2. Builder l'image avec le fichier secret
3. Tester

:::

:::correction

1. Créer un fichier secret :

```sh
echo "super_secret_token_123" > my_api_key.txt
```

1. Builder l'image avec le fichier secret :

```dockerfile
# Dockerfile

FROM alpine:3.19
RUN --mount=type=secret,id=api_key \
    echo "API Key: $(cat /run/secrets/api_key)"
```

```sh
docker buildx build \
  --secret id=api_key,src=my_api_key.txt \
  --platform linux/amd64 \
  -t secret-demo:1.0 \
  --load .
```

1. Tester

```sh
docker run --rm secret-demo:1.0
```

✅ Le secret est affiché à l'exécution mais absent de l'image en inspection et de `docker history`.
:::
