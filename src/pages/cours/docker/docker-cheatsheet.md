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

## Supprimer une image :

```sh
docker rmi 54321
```

## Lister les commandes ayant créé l'image et inspecter les layers

```sh
docker image history mon_image
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
- `docker container inspect` : affiche la configuration d'un conteneur en Json. Cette configuration peut être verbeuse, on utilise souvent `jq` pour filtrer l'affichage, par exemple pour afficher uniquement l'état (_healthcheck_) : `docker inspect --format='{{json .State.Health}}'`

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

### Data volume depuis une baie externe et driver Convoy (NFS, EBS d’AWS)

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

-p : lier un port du conteneur (80) à un port de l’hôte (8080)

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

ID						RECLAIMABLE	SIZE		LAST ACCESSED
9zfls97m6q210we36khnehxl1*              	true 		231.8MB   	29 hours ago
[…]
Shared:		187.4MB
Private:	246.5MB
Reclaimable:	433.9MB
Total:		433.9MB
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

## docker init : générer un Dockerfile

`docker init` : génère un `Dockerfile` de base pour une application, sans avoir à le créer manuellement.

## Liens

:::link
Voir aussi : 

- <https://spacelift.io/blog/docker-commands-cheat-sheet>
- <https://github.com/wsargent/docker-cheat-sheet>
- <https://blog.stephane-robert.info/docs/conteneurs/moteurs-conteneurs/cheat-sheet/>
:::

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

Docker permet de contrôler les _capabilities_ du noyau Linux disponibles dans un conteneur.

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

### CIS Benchmarks

**Docker Bench for Security** permet de vérifier la conformité aux benchmarks _Center for Internet Security_ (CIS) :

```sh
docker run -it --net host --pid host --cap-add audit_control \
-v /var/lib:/var/lib \
-v /var/run/docker.sock:/var/run/docker.sock \
docker/docker-bench-security
```

### WAF

Un _Pare-feu d’applications Web_ (WAF) comme `ModSecurity` permet de protéger vos applications contre les attaques courantes : injections SQL, XSS, …

```sh
docker run -d -p 80:80 -p 443:443 --name my_waf modsecurity/modsecurity
```

---

# Cheatsheet Dockerfile

- `FROM` : permet de définir l'image source
- `ADD <SOURCE> <DESTINATION>` : permet d'ajouter / télécharger des fichiers dans l'image
  + `<SOURCE>` est un chemin sur l'hyperviseur, `<DESTINATION>` est un chemin à l'intérieur de l'image en création.
- `RUN` : permet d’exécuter des commandes dans votre conteneur
- `EXPOSE <PORT>` : permet de documenter l'utilisation d'un port du conteneur.
  + Remplacer `<PORT>` par la valeur du port utilisé dans le conteneur, par exemple `80`.
- `VOLUME <VOL>` : permet de documenter l'utilisation d'un répertoire du conteneur partageant des données avec l'hyperviseur.
  + Remplacer `<VOL>` par le chemin du répertoire dans le conteneur.
- `WORKDIR <DIR>` : définit le nouveau répertoire de travail à utiliser dans le conteneur.
  + Remplacer `<DIR>` par le chemin du répertoire dans le conteneur.
- `ENTRYPOINT <COMMANDE>` : définit le processus principal (PID=1) permettant de lancer le conteneur.
  + Remplacer `<COMMANDE>` par la commande désirée, par exemple `['java','-jar','myapp.jar']`.
  + Préférer un tableau d'arguments à une chaîne de caractères.
  + Non remplacé par la commande `docker run`
- `CMD <COMMANDE>` : (re)définit la commande et ses arguments par défaut à exécuter au démarrage du conteneur.
  + Préférer un tableau d'arguments à une chaîne de caractères.
  + Peut être remplacé par la commande `docker run …`
  + Préférer définir uniquement des arguments par défaut et définir la commande dans l'entrypoint (évite de remplacer le processus par un `docker run …`)
- `HEALTHCHECK` permet d'exécuter une commande dans le conteneur pour vérifier son état : [doc](https://docs.docker.com/reference/dockerfile/#healthcheck). Par exemple : `HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1`

- [Lien : vidéo CMD vs ENTRYPOINT mais c'est quoi la différence ?](https://www.youtube.com/watch?v=kfyDu5R4VrM)
- D'autres technologies de construction d'images existent : voir la page <https://blog.stephane-robert.info/docs/conteneurs/images-conteneurs/build/introduction/>

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
COPY --fromt=mon-build dist/ build/
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

## BuildKit

`BuildKit` (activé par défaut depuis la version 23.0) est un nouveau moteur de build plus performant, sécurisé et flexible voué à remplacer la commande `docker build` :

- Amélioration des performances de build grâce à la construction en parallèle et une meilleure gestion des caches.
- Utilisation optimisée des ressources (CPU, mémoire).
- Fonctionnalités avancées comme le support des builds multi-plateformes et des caches de builds distribués.
- Meilleure sécurité avec des fonctionnalités comme le build _rootless_ (sans accès root).

Pour plus d'information, voir les liens suivants :

- <https://blog.stephane-robert.info/docs/conteneurs/images-conteneurs/build/buildkit/>
- <https://blog.stephane-robert.info/post/docker-build-multiarch/>
- <https://blog.stephane-robert.info/docs/conteneurs/moteurs-conteneurs/secrets-docker/>

## Tagger une image

`docker tag <NOM_DE_MON_IMAGE_LOCALE:latest> <YOUR_USERNAME/NOM_DE_MON_IMAGE_REMOTE:NOM_DU_TAG_REMOTE>` : tag d'une image locale pour préparer un tag distant.

## Publier une image

`docker push YOUR_USERNAME/NOM_DE_MON_IMAGE_REMOTE:NOM_DU_TAG_REMOTE`

## Chercher une image

`docker search`

## Ignorer des fichiers lors d'un `ADD` : `.dockerignore`

Le fichier `.dockerignore` fonctionne comme un fichier `.gitignore` pour ignorer des fichiers lors d'une opération `ADD` dans le `Dockerfile`.

Ce fichier contient une liste de patterns de fichiers à ignorer, par exemple :

```
.git
node_modules
build
```

---

# Cheatsheet docker compose

## Démarrer la stack :

```sh
docker compose up
```

## Détruire la stack :

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

## Attributs d’un service décrit dans un `docker compose.yml` :

- `image` : permet de spécifier l'image source pour le conteneur
- `build` : permet de spécifier le `Dockerfile` source pour créer l'image du conteneur
- `volume` : permet de spécifier les points de montage entre le système hôte et les conteneurs
- `restart` : permet de définir le comportement du conteneur en cas d'arrêt du processus
- `environment` : permet de définir les variables d’environnement
- `depends_on ` permet de dire que le conteneur dépend d'un autre conteneur
- `ports` : permet de définir les ports disponibles entre la machine host et le conteneur

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries.

