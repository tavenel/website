---
title: Cheatsheets Docker®
---

# Cheatsheet Docker®

## Docker run : créer un nouveau conteneur

```sh
docker run nginx
```

***Le conteneur s'arrête une fois le processus principal (`PID=1`, celui lancé par `docker run`) se termine !***

-d : créer un nouveau conteneur en arrière-plan

```sh
docker run -d nginx
```

-name : nommer le conteneur

```sh
docker run --name my_custom_name nginx
```

--restart=always : permet de redémarrer le conteneur en cas d'échec

```sh
docker run --restart=always nginx
```

## Docker exec : exécuter une commande dans un conteneur déjà en activité

```sh
docker exec 12345 /bin/ls
```

`docker exec` revient à créer un conteneur temporaire avec le même contexte (`namespace`, `cgroups`) que le conteneur en cours d'exécution. **Rend la main une fois la commande terminée**

-ti : attacher le terminal pour une commande interactive (ne rend pas la main, par exemple pour un shell)

```sh
docker exec -ti 12345 /bin/bash
```

## Docker ps : lister les conteneurs créés

Lister les csontainers en activité :

```sh
docker ps
```

Lister tous les conteneurs (y compris ceux arrêtés) :

```sh
docker ps -a
```

## Démarrer un conteneur

```sh
docker start 12345
```

## Arrêter un conteneur

### Arrêt propre (SIGTERM)

```sh
docker stop 12345
```

### Terminaison (SIGKILL)

```sh
docker kill 12345
```

## Supprimer un conteneur

```sh
docker rm 12345
```

## Docker images : lister les images récupérées ou créées sur la machine hôte

Lister toutes les images :

```sh
docker images -a
```

## Supprimer une image

```sh
docker rmi 54321
```

## Lister les commandes ayant créé l'image et inspecter les layers

```sh
docker image history [--no-trunc] mon_image
```

## Différence runtime vs image

```sh
docker diff
```

## Docker container

- `docker container ls`
- `docker container attach` : s'attacher à la sortie du PID=1 (commande de lancement du conteneur)
- `docker container cp`
- `docker container prune` : détruit tous les conteneurs arrêtés
- `docker container rename`
- `docker container stats` : monitoring des ressources Docker
- `docker container commit` : crée une image depuis un conteneur existant (à éviter)
- `docker container inspect` : affiche la configuration d'un conteneur en Json. Cette configuration peut être verbeuse, on utilise souvent `jq` pour filtrer l'affichage, par exemple pour afficher uniquement l'état (*healthcheck*) : `docker inspect --format='{{json .State.Health}}'`

## Docker volumes

## Démarrer un conteneur avec un filesystem Read/Only

```sh
docker run --read-only …
```

## Utiliser un filesystem temporaire (tmpfs) dans un répertoire

```sh
docker run --tmpfs /mon_repertoire …
```

### Gérer les volumes

```sh
docker volume create
```

```sh
docker volume ls
```

```sh
docker volume inspect mon_volume
```

### Créer un volume à la création du conteneur

```sh
docker run -v /mon_volume mon_image …
```

### Data volume depuis une baie externe et driver Convoy (NFS, EBS d'AWS)

```sh
docker run --volume-driver=convoy -v mon_volume:/mon_point_de_montage_dans_conteneur …
```

### Data volume en mémoire temporaire (tmpfs)

```sh
docker run --mount type=tmpfs,destination=/tmp …
```

### Bind mount

-v : crée un volume depuis un répertoire visible de la machine hôte et monte ce volume comme répertoire local au conteneur.

```sh
docker run -v mon_repertoire_sur_hote:mon_point_de_montage_dans_conteneur mon_image …

# Par exemple :
docker run -it -v C:\mon_repertoire_partage_windows:/mon_repertoire_dans_le_conteneur …
```

### Utilisation de volume

```sh
docker run -v mon_volume:mon_point_de_montage_dans_conteneur mon_image
```

## Configuration du réseau

### Lister les réseaux

```sh
docker network ls
```

### Créer un réseau

```sh
docker network create --driver <DRIVER TYPE> mon_reseau
```

```sh
docker network create --driver <DRIVER TYPE> mon_reseau --subnet=192.168.0.0/24 --gateway=192.168.0.1
```

:::tip
Paramètres disponibles pour un réseau de type `bridge` :

- `com.docker.network.bridge.enable_icc` : communication inter-conteneurs (`true` / `false`)
- `com.docker.network.bridge.enable_ip_masquerade` : Active le masquage IP pour l'accès au réseau externe.
- `subnet` : Choisir le réseau (CIDR)
- `gateway` : Spécifier la passerelle du réseau.

:::

:::tip
Comment atteindre des services de l'hôte depuis un conteneur isolé par le *bridge* Docker ?

- *Docker Desktop* (dev uniquement) : Utiliser l'adresse IP interne ou le nom DNS `host.docker.internal`
- Linux natif : ajouter `--add-host=host.docker.internal:host-gateway` à la ligne de commande
- *Docker Compose* : ajouter à la configuration du conteneur :

    ```yaml
    extra_hosts:
    - "host.docker.internal:host-gateway"
    ```

:::

### Supprimer un réseau

```sh
docker network rm mon_reseau
```

### Inspecter un réseau

```sh
docker network inspect mon_reseau
# trouver la plage réseau associée :
docker network inspect mon_reseau -f '{{ range $i, $a := .IPAM.Config }}{{ println .Subnet }}{{ end }}'
```

### Créer un conteneur en utilisant un réseau spécifique

```sh
docker run --network mon_reseau mon_image
```

### Connexion / Déconnexion à un réseau existant

```sh
docker network connect mon_reseau mon_conteneur
docker network disconnect mon_reseau mon_conteneur
```

### Mapping de port

-p : lier un port du conteneur (80) à un port de l'hôte (8080)

```sh
docker run -p 8080:80 mon_conteneur
```

### Nettoyer les ressources

```sh
docker container prune # supprime les conteneurs inactifs
docker image prune # supprime les images non utilisées par un conteneur
docker buildx prune # supprime les builds non utilisés

# Supprimer **toutes** les données non utilisées : conteneurs, images, réseaux, volumes.
# Attention à la perte de données !!!
docker system prune 
```

## Limiter les ressources d'un conteneur

Exemple de version simpliste :

```sh
docker run --memory="1g" --cpus=".5" mon_image
```

Voir la documentation : <https://docs.docker.com/config/containers/resource_constraints/>

## Exporter les logs (ELK, …)

```sh
docker --log-driver gelf --log-opt gelf-address=udp://… …
```

## Afficher l'utilisation disque

```sh
docker system df              

TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          16        8         4.008GB   2.07GB (51%)
Containers      15        1         2.906MB   2.278kB (0%)
Local Volumes   13        13        2.764GB   0B (0%)
Build Cache     32        0         246.5MB   246.5MB
```

```sh
docker buildx du

ID      RECLAIMABLE SIZE  LAST ACCESSED
9zfls97m6q210we36khnehxl1*               true   231.8MB    29 hours ago
[…]
Shared:  187.4MB
Private: 246.5MB
Reclaimable: 433.9MB
Total:  433.9MB
```

## Serveur distant

Docker est un modèle client-serveur, il est possible d'exposer publiquement le serveur (qui tourne les conteneurs) et d'utiliser un client distant :

```sh
# Server
dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock
# Client
docker -H tcp://<ip>:2375 ps
```

### Accéder au serveur du host dans un conteneur

```sh
# On monte la socket Docker dans le conteneur
docker run -v var/run/docker.sock:/var/run/docker.sock …`
# Permet de faire des commandes : `docker …` à l'intérieur du conteneur et de voir les autres conteneurs (monitoring, …)
```

## Registry

Il est possible d'installer sa propre registry Docker :

```sh
# Installation d'une registry locale
docker run -d -p 5000:5000 --restart always --name registry registry:2

# Utilisation de la registry
docker pull ubuntu
docker tag ubuntu localhost:5000/ubuntu
docker push localhost:5000/ubuntu
```

## Sécurité

### Docker scout : analyses de sécurité

Docker Scout est un outil de sécurité pour Docker qui aide à analyser les images de conteneurs pour identifier les vulnérabilités, les dépendances, et les mises à jour de sécurité nécessaires.

```sh
docker scout cves nginx:latest # CVEs (vulnérabilités)
docker scout recommendations nginx:latest # MAJ à effectuer
```

### Capabilities

Docker permet de contrôler les *capabilities* du noyau Linux disponibles dans un conteneur.

```sh
# Retirer des capabilities
docker run --cap-drop=NET_RAW,MKNOD,SYS_ADMIN,SYS_MODULE mon_image
```

```sh
# Retirer TOUTES les capabilities sauf …
docker run --cap-drop=ALL --cap-add=NET_ADMIN,… mon_image
```

Rappel des principales capabilities d'un noyau Linux :

- `AUDIT_WRE` : Audit et accès au file system
- `CHOWN`, `FOWNER` : Changer l'ownership d'un fichier
- `DAC_READ_SEARCH` : Lire des fichiers et répertoires
- `FSETID` : Le process peut changer son `UID`/`GID`
- `KILL` : Process termination
- `MKNOD` : permet de créer des fichiers spéciaux comme les liens symboliques.
- `NET_BIND_SERVICE` : Network binding
- `NET_RAW` : Raw socket usage (permet d'envoyer des paquets réseau bruts)
- `SETPCAP` : Changer les capabilities d'un autre processus
- `SETUID`, `SETGID` : Bits `SUID` et `GID`
- `SYS_ADMIN` : Donne accès à un large éventail d'opérations système, y compris la gestion des montages, des répertoires temporaires et l'accès aux systèmes de fichiers.
- `SYS_BOOT` : (Re)boot
- `SYS_MODULE` : Permet de charger et d'exécuter du code au niveau module du noyau Linux.
- `SYSLOG` : Logging

:::tip
Pour afficher les capabilities courantes, utiliser :

```sh
capsh --print
```

:::

### CIS Benchmarks

**Docker Bench for Security** permet de vérifier la conformité aux benchmarks *Center for Internet Security* (CIS) :

```sh
docker run -it --net host --pid host --cap-add audit_control \
-v /var/lib:/var/lib \
-v /var/run/docker.sock:/var/run/docker.sock \
docker/docker-bench-security
```

### WAF

Un *Pare-feu d'applications Web* (WAF) comme `ModSecurity` permet de protéger vos applications contre les attaques courantes : injections SQL, XSS, …

```sh
docker run -d -p 80:80 -p 443:443 --name my_waf modsecurity/modsecurity
```

## Liens

:::link
Voir aussi :

- <https://spacelift.io/blog/docker-commands-cheat-sheet>
- <https://github.com/wsargent/docker-cheat-sheet>
- <https://blog.stephane-robert.info/docs/conteneurs/moteurs-conteneurs/cheat-sheet/>

:::

---

# Cheatsheet Dockerfile

- `FROM` : permet de définir l'image source
- `ADD <SOURCE> <DESTINATION>` : permet d'ajouter / télécharger des fichiers dans l'image
  - `<SOURCE>` est un chemin sur l'hyperviseur, `<DESTINATION>` est un chemin à l'intérieur de l'image en création.
- `RUN` : permet d'exécuter des commandes dans votre conteneur
- `EXPOSE <PORT>` : permet de documenter l'utilisation d'un port du conteneur.
  - Remplacer `<PORT>` par la valeur du port utilisé dans le conteneur, par exemple `80`.
- `VOLUME <VOL>` : permet de documenter l'utilisation d'un répertoire du conteneur partageant des données avec l'hyperviseur.
  - Remplacer `<VOL>` par le chemin du répertoire dans le conteneur.
- `WORKDIR <DIR>` : définit le nouveau répertoire de travail à utiliser dans le conteneur.
  - Remplacer `<DIR>` par le chemin du répertoire dans le conteneur.
- `ENTRYPOINT <COMMANDE>` : définit le processus principal (PID=1) permettant de lancer le conteneur.
  - Remplacer `<COMMANDE>` par la commande désirée, par exemple `['java','-jar','myapp.jar']`.
  - Préférer un tableau d'arguments à une chaîne de caractères.
  - Non remplacé par la commande `docker run`
- `CMD <COMMANDE>` : (re)définit la commande et ses arguments par défaut à exécuter au démarrage du conteneur.
  - Préférer un tableau d'arguments à une chaîne de caractères.
  - Peut être remplacé par la commande `docker run …`
  - Préférer définir uniquement des arguments par défaut et définir la commande dans l'entrypoint (évite de remplacer le processus par un `docker run …`)
- `HEALTHCHECK` permet d'exécuter une commande dans le conteneur pour vérifier son état : [doc](https://docs.docker.com/reference/dockerfile/#healthcheck). Par exemple : `HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1`

:::link

- [Lien : vidéo CMD vs ENTRYPOINT mais c'est quoi la différence ?](https://www.youtube.com/watch?v=kfyDu5R4VrM)
- D'autres technologies de construction d'images existent : voir la page <https://blog.stephane-robert.info/docs/conteneurs/images-conteneurs/build/introduction/>

:::

## docker init : générer un Dockerfile

```sh
docker init
```

Génère un `Dockerfile` de base pour une application, sans avoir à le créer manuellement.

## Build multistage

- Plusieurs `FROM … AS etapeX`
- Seul le dernier `FROM …` reste dans l'image finale, le reste est détruit…
- …Mais accès aux fichiers d'un autre layer `FROM` précédent par `COPY --from=etapeX …` dans le `Dockerfile`

```dockerfile
FROM npm AS mon-build
RUN npm package

# On repart d'une image vierge
FROM nginx AS ma-prod
# Mais on peut copier des fichiers du build précédent
COPY --from=mon-build dist/ build/
…
```

## Créer une image depuis un fichier nommé `Dockerfile`

```sh
docker build -t NOM_DE_MA_NOUVELLE_IMAGE REPERTOIRE_DU_DOCKERFILE
```

## Créer une image depuis un fichier ayant un nom personnalisé

```sh
docker build -t NOM_DE_MA_NOUVELLE_IMAGE -f NOM_DU_FICHIER_DOCKERFILE REPERTOIRE_DU_DOCKERFILE
```

## Tagger une image

Tag d'une image locale pour préparer un tag distant :

```sh
docker tag <NOM_DE_MON_IMAGE_LOCALE:latest> <YOUR_USERNAME/NOM_DE_MON_IMAGE_REMOTE:NOM_DU_TAG_REMOTE>
```

## Publier une image

```sh
docker push YOUR_USERNAME/NOM_DE_MON_IMAGE_REMOTE:NOM_DU_TAG_REMOTE
```

## Chercher une image

```sh
docker search
```

## Ignorer des fichiers lors d'un `ADD` : `.dockerignore`

Le fichier `.dockerignore` fonctionne comme un fichier `.gitignore` pour ignorer des fichiers lors d'une opération `ADD` dans le `Dockerfile`.

Ce fichier contient une liste de patterns de fichiers à ignorer, par exemple :

```
.git
node_modules
build
```

## Buildx et BuildKit

`BuildKit` (activé par défaut depuis la version 23.0) est un nouveau moteur de build plus performant, sécurisé et flexible voué à remplacer la commande `docker build` :

- Amélioration des performances de build grâce à la construction en parallèle et une meilleure gestion des caches.
- Utilisation optimisée des ressources (CPU, mémoire).
- Fonctionnalités avancées comme le support des builds multi-plateformes et des caches de builds distribués.
- Meilleure sécurité avec des fonctionnalités comme le build *rootless* (sans accès root).

:::link
Pour plus d'information, voir les liens suivants :

- <https://blog.stephane-robert.info/docs/conteneurs/images-conteneurs/build/buildkit/>
- <https://blog.stephane-robert.info/post/docker-build-multiarch/>
- <https://blog.stephane-robert.info/docs/conteneurs/moteurs-conteneurs/secrets-docker/>

:::

### Activer BuildKit

```sh
DOCKER_BUILDKIT=1 docker build .
```

### Créer un nouveau builder

```sh
docker buildx create --name mybuilder --use
docker buildx inspect --bootstrap
```

### Lister les builders existants

```sh
docker buildx ls
```

### Construction et push multi-arch avec cache

```sh
docker buildx build \
  --cache-to=type=local,dest=.buildxcache \
  --cache-from=type=local,src=.buildxcache \
  --platform linux/amd64,linux/arm64 \
  -t moncompteDocker/nginx-custom:latest \
  --push .
```

:::tip

- `--push` : envoie directement l'image vers le registre
- Peut être remplacé par `--load` pour un test local (pour 1 architecture uniquement).

:::

### Vérifier l'image sur Docker Hub

```sh
docker buildx imagetools inspect moncompteDocker/nginx-custom:latest
```

### Montage de secrets

Permet de passer des secrets au moment du build sans les stocker dans l'image (invisible dans `docker history`).

```dockerfile
# Dockerfile

FROM alpine
RUN --mount=type=secret,id=mytoken \
    curl -H "Authorization: Bearer $(cat /run/secrets/mytoken)" https://api.example.com/data
```

```sh
docker buildx build --secret id=mytoken,src=token.txt .
```

### Montage temporaire

`--mount=type=tmpfs` ou `--mount=type=bind` : Crée un filesystem temporaire ou accède à un fichier externe (les fichiers ne restent pas dans l'image).

```dockerfile
# Dockerfile

RUN --mount=type=tmpfs,target=/tmp \
    make
```

### Montage de cache

```dockerfile
# Dockerfile

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

### Contextes multiples

```dockerfile
# Dockerfile

FROM alpine
COPY --from=repo1 /src /app/src
COPY --from=repo2 /lib /app/lib
```

```sh
docker buildx build \
  --build-context repo1=git://github.com/user/repo1.git \
  --build-context repo2=git://github.com/user/repo2.git .
```

## IA

### Model runner

Permet d'exécuter facilement un modèle d'IA.

```sh
docker model run …
```

:::link
Voir :

- la documentation : <https://docs.docker.com/ai/model-runner/>
- le catalogue : <https://hub.docker.com/catalogs/models>

:::

### Model-Connected-Pipeline (MCP)

Permet de gérer l'intégration avec des MCPs.

```sh
docker mcp …
```

Démarrer la passerelle (point d'accès unique pour le client) :

```sh
docker mcp gateway run
```

:::link
Voir :

- la documentation : <https://docs.docker.com/ai/mcp-catalog-and-toolkit/>
- le catalogue : <https://hub.docker.com/mcp>

:::

## Offload

Permet de builder et d'exécuter les conteneurs dans le Cloud.

:::link
Voir la documentation : <https://docs.docker.com/offload/>
:::

### Création d'un environnement Cloud

```sh
docker offload start
```

### Exécution d'un conteneur

```sh
docker run --rm hello-world

# Si besoin de GPU :
docker run --rm --gpus all hello-world
```

---

# Cheatsheet docker compose

## Démarrer la stack

```sh
docker compose up
```

## Détruire la stack

```sh
docker compose down
```

## Afficher la configuration finale après vérification

```sh
docker compose config
```

## Reconstruire la stack en cas de changement dans le code

```sh
docker compose watch
```

:::link

- Voir la documentation : <https://docs.docker.com/compose/how-tos/file-watch/>
- Pour un exemple, voir : <https://github.com/dockersamples/avatars>

:::

## Attributs d'un service décrit dans un docker `compose.yml`

- `image` : permet de spécifier l'image source pour le conteneur
- `build` : permet de spécifier le `Dockerfile` source pour créer l'image du conteneur
- `volume` : permet de spécifier les points de montage entre le système hôte et les conteneurs
- `restart` : permet de définir le comportement du conteneur en cas d'arrêt du processus
- `environment` : permet de définir les variables d'environnement
- `depends_on` permet de dire que le conteneur dépend d'un autre conteneur
- `ports` : permet de définir les ports disponibles entre la machine host et le conteneur
- `provider` : utilise un *Provider* et non une image Docker pour ce service. Voir : <https://docs.docker.com/compose/how-tos/provider-services/>

## Models

Champ `models:` : permet de lancer des modèles d'IA depuis Docker Compose (très similaire aux `services:`).

:::link
Voir la documentation : <https://docs.docker.com/ai/compose/models-and-compose/>
:::

## Convertir un Docker Compose en manifest Kubernetes

```sh
docker compose bridge convert
```

:::link
Voir : <https://docs.docker.com/compose/bridge/usage/>
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.
