---
title: Introduction à l'usage de conteneurs Docker®
author: Tom Avenel
date: 2023 / 2024
correction: false
---

## Créer et gérer des conteneurs Docker® depuis des images existantes

Nous allons créer un conteneur depuis une image `hello-world` récupérée sur le Docker® Hub.

### Installation du Docker® Engine

Dans un premier temps, nous allons déployer un nœud `Docker®` afin d'être en mesure de configurer une infrastructure `Docker®` par l'installation du `Docker® Engine`, de créer et gérer des images Docker® et enfin de déployer des conteneurs `Docker®`.

Afin d'être au plus proche d'un déploiement réel sur un serveur dédié, il est conseillé d'effectuer les opérations suivantes dans une machine virtuelle Linux dédiée (par exemple : `Oracle® VirtualBox`). Cependant, il est possible d'effectuer l'installation directement sur son poste de travail, dans un environnement Windows®, Mac OS® ou Linux®. 

1. Créer un compte sur le `Docker® Hub` : <https://hub.docker.com/>

2. Installer `Docker® Desktop` (Windows® & Mac OS®) ou `Docker® Community Edition` (Linux®) sur votre poste de travail.

Pour Windows, récupérer la version stable depuis ce lien : <https://hub.docker.com/editions/community/docker-ce-desktop-windows>

Renseigner le compte `Docker® Hub` créé à l’étape 1 lorsque demandé.

3. Tester l’installation : ouvrir un terminal et taper `docker version`, vérifier que la version est affichée sans erreur.

_Il est également possible d'utiliser le `Docker® Lab` pour utiliser un environnement de tests : [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/)_

### Créer un premier conteneur et le démarrer

Une fois le compte `Docker® Hub` configuré, les images sont automatiquement récupérées depuis celui-ci.

```sh
docker run hello-world
```

Vérifier que l'exécution de cette image affiche bien `Hello from Docker!`

Note :

Un conteneur Docker® reste actif tant que son processus n’a pas terminé son exécution.

Ici, ce processus affiche un simple `Hello, World` avant de terminer son exécution, ce qui a pour conséquence d’arrêter le conteneur que nous venons de créer.

### Créer un conteneur depuis une véritable image de production

Nous allons maintenant créer un conteneur depuis une image contenant un serveur `Nginx`, qui tournera en continu.

Nous allons démarrer ce conteneur en arrière-plan (mode “détaché”) pour pouvoir continuer à utiliser notre terminal :

```sh
docker run -d -p 8080:80 nginx
```

L’option `-d` active le mode détaché

L’option `-p` lie un port du conteneur (ici 80) vers un port de l'hôte (ici 8080). Cela permet d’accéder au port 80 du conteneur depuis l’adresse locale 8080

Vérifier que le conteneur a été correctement démarré avec un serveur `Nginx` en joignant l’URL :

[http://localhost:8080](http://localhost:8080)

#### Note 1 :

Notre conteneur étant actif en arrière-plan, il peut être intéressant de s’y connecter.

Pour cela, Docker® permet d’exécuter des commandes dans un conteneur actif, on pourra donc lui demander d’exécuter un shell dans notre conteneur :

1. Lister les conteneurs actifs (et récupérer leurs `ID`) :

```sh
docker ps
```

2. Exécuter une commande dans un conteneur actif :

```sh
docker exec -t -i ID_DU_CONTENEUR bash
```

#### Note 2 :

Les images Docker® sont des images de système d’exploitation distribuées sur le réseau, elles peuvent donc être volumineuses et il est important de réduire leur taille au maximum.

Une conséquence est que la plupart des outils utiles à un administrateur système ont souvent été retirés des images pour gagner de la place.

Par exemple, il faudra souvent installer un éditeur de texte dans les conteneurs comme `nano` pour faciliter la modification de fichiers :

```sh
apt-get update -yq && apt-get install -yq nano
```

### Gérer les conteneurs

Utiliser les commandes Docker® pour lister les conteneurs actifs et les arrêter (utiliser la Cheatsheet en annexe).

Supprimer ensuite tous les conteneurs inactifs (il n’est pas possible de supprimer un conteneur actif)

<div style="page-break-after: always"></div>

## Créer des images de conteneurs

Au lieu d’utiliser l'image `Nginx` déjà présente sur le `Docker® Hub`, nous allons recréer notre propre version de cette image.

La création d’une image Docker® passe par **un fichier `Dockerfile`** qui contient la description et les instructions pour créer cette image.

Pour optimiser le transfert des images, Docker® utilise un système de mises à jour : chaque image est une mise à jour d’une autre image (en réalité, du layer d’une image).

Lors de la construction de l’image depuis le `Dockerfile`, chaque instruction va créer, depuis une image de base, un nouveau layer empilé sur le layer précédent.

Afin d’optimiser la taille et les performances de notre image, il faut limiter au maximum le nombre de couches d'images et donc le nombre d’instructions, par exemple en enchaînant les commandes par un `&&` !

:::warning
Les instructions suivantes ne sont pas des commandes Docker ! Il s'agit des instructions à entrer dans un **fichier nommé `Dockerfile`**. Le `Dockerfile` est donc un langage (comme Python par exemple) qui va être interprété par la commande `docker build` et **NON des commandes à taper dans le terminal** !!!
:::

### Création du Dockerfile

Créer un nouveau fichier nommé `Dockerfile` (sans extension de fichier). Dans ce fichier de code, ajouter les lignes suivantes :

#### `FROM`

Un `Dockerfile` démarre par l’instruction `FROM` qui indique quelle est l’image de base utilisée.

Nous allons partir de l’image officielle `debian:12`

```Dockerfile
FROM debian:12
```

#### `RUN`

L'instruction `RUN` permet d’exécuter des commandes dans l’image durant sa création.

Nous allons installer `NginX` dans l'image pour éviter de le faire à chaque création de conteneur :

```Dockerfile
RUN apt-get update -yq && apt-get install -yq nginx
```

:::tip
Chaque instruction `RUN` crée un nouveau _layer_ : limiter leur nombre pour réduire la taille de l'image Docker.
:::

#### `EXPOSE`

Le `Dockerfile` possède un ensemble d’instructions permettant de configurer le conteneur qui sera créé depuis notre image.

Nous allons exposer le port 80 de `NginX` dans chaque conteneur créé depuis notre image :

```Dockerfile
EXPOSE 80
```

#### `CMD`

Le `Dockerfile` se termine par une instruction `CMD` indiquant la commande du processus unique exécuté dans le conteneur.

Cette instruction ne sera pas utilisée lors de la création de l’image et sert uniquement au démarrage des conteneurs créés depuis cette image.

Ici, nous allons exécuter la commande `nginx` qui démarre `NginX` et rend la main. Pour que notre conteneur ne s’arrête pas après l'exécution de la commande `NginX`, on ajoute un `sleep infinity` pour continuer à faire tourner le conteneur :

```Dockerfile
CMD nginx && sleep infinity
```

#### `Dockerfile` complet

Résumé du `Dockerfile` complet :

```Dockerfile
FROM debian:12

RUN apt-get update -yq && apt-get install -yq nginx

EXPOSE 80

CMD nginx && sleep infinity
```

### Création de l'image

Nous allons maintenant créer une image docker (en local) depuis le `Dockerfile` que nous venons de créer :

```sh
docker build -t NOM_DE_MA_NOUVELLE_IMAGE REPERTOIRE_DU_DOCKERFILE
```

On peut tester la validité de cette image en créant un conteneur depuis cette nouvelle image :

```sh
docker run -d -p 8080:80 NOM_DE_MA_NOUVELLE_IMAGE
```

### Publication de l'image

Nous allons maintenant publier notre image locale sur le `Docker Hub` pour pouvoir la partager.

Cette opération nécessite 2 étapes : _tagger_ l'image pour lui donner son nom sur le Hub, puis publication sur le Hub.

1. Tag de l'image :

```sh
docker tag NOM_DE_MON_IMAGE_LOCALE:latest YOUR_USERNAME/NOM_DE_MON_IMAGE_REMOTE:NOM_DU_TAG_REMOTE
```

Par exemple : `docker tag my_nginx:latest epsi/my_nginx:latest`

2. Publication de l'image

```sh
docker push YOUR_USERNAME/NOM_DE_MON_IMAGE_REMOTE:NOM_DU_TAG_REMOTE
```

Par exemple : `docker push epsi/my_nginx:latest`

### Utilisation de l'image publiée sur le Docker Hub

La nouvelle image peut maintenant être utilisée par n’importe qui :

```sh
docker run epsi/my_nginx:latest
```

### Multi-stage build

Il est possible d'utiliser plusieurs `FROM … AS etapeX` dans un `Dockerfile` : seul le dernier `FROM …` reste dans l'image finale (tout ce qui est avant le dernier `FROM` est détruit). L'intérêt de ce build _multi-stage_ est que l'on peut récupérer des fichiers du layer précédent par des instructions `COPY --from=etapeX …` 

Utilisons un multi-stage build pour un `hello-world` de Golang en créant un fichier `main.go` :

```golang
//main.go
package main

import "fmt"

func main() {
    fmt.Println("Salut depuis un multi build!")
}
```

#### Build dans le stage 1

Nous allons d'abord commencer par créer un `Dockerfile` pour builder le fichier dans un environnement `Golang`.

```Dockerfile
# Stage 1: Build Environment (Golang)
FROM golang:alpine AS build-stage
# À faire: Copier le fichier main.go de la machine dans l'image
RUN go build main.go # On build le fichier pour créer /go/main
```

:::warning
**Attention à bien ajouter l'instruction manquante au Dockerfile !**
:::

Créer un conteneur pour vérifier l'état de l'image actuelle :

```sh
docker build . -t multi:v1
docker run --rm multi:v1 /bin/ls
# bin
# main
# main.go
# src
```

#### Multi-stage build

Ajouter un 2e stage dans le `Dockerfile` précédent pour créer un 2e layer sur l'image, servant à exécuter le fichier compilé. Le `golang` étant compilé en langage machine, il n'est plus nécessaire d'avoir une image avec un environnement `golang` complet : on utilisera un simple système `alpine`.

```Dockerfile
# Stage 1: Build Environment (Golang)
FROM golang:alpine AS build-stage
# À faire: Copier le fichier main.go de la machine dans l'image
RUN go build main.go

# Stage 2: Runtime Environment (Alpine)
FROM alpine
# À faire: Copier le fichier /go/main du layer précédent dans le répertoire courant (`.`)
CMD ["./main"] # Exécution du programme compilé
```

Vérifier la bonne exécution de la nouvelle image :

```sh
docker build . -t multi:v2
docker run --rm multi:v2
# Salut depuis un multi build!

# TEST: On remplace la ligne `CMD ["./main"]`
# pour tester l'image en exécutant /bin/ls
# pour lister le contenu du répertoire
docker run --rm multi:v2 /bin/ls
# […]
# main
# […]
```

::: {.correction .if correction="true"}
```Dockerfile
# Stage 1: Build Environment (Golang)
FROM golang:alpine AS build-stage
COPY main.go .
RUN go build main.go

# Stage 2: Runtime Environment (Alpine)
FROM alpine
COPY --from=build-stage /go/main .
CMD ["./main"]
```
:::


## Utilisation de volumes

1. Utiliser un point de montage (`bind mount`) pour monter un répertoire du système hôte à la création d'un conteneur :
  + On utilisera l'image : `bash`.
  + Créer un nouveau conteneur en lui liant un point de montage vers un répertoire du système hôte.
  + Ajouter un fichier dans le répertoire hôte.
  + Vérifier que le fichier est bien accessible au conteneur en se connectant sur celui-ci.
2. Créer un volume dédié pour partager de la donnée entre deux conteneurs applicatifs :
  + On utilisera l'image : `bash`.
  + Créer un nouveau volume nommé grâce à la commande `docker volume create`.
  + Créer deux conteneurs utilisant le volume nommé.
  + Créer un fichier dans le point de montage du volume dans le premier conteneur.
  + Vérifier que ce fichier est accessible dans le deuxième conteneur.
  + Modifier le fichier dans le deuxième conteneur.
  + Accéder au fichier dans le premier conteneur.
  + Que remarquez-vous ?

::: {.correction .if correction="true"}
```
# 1.
# Ajouter un fichier dans C:\mon_repertoire_partage_windows
# Créer le conteneur avec le répertoire partagé. On utilise le mode interactif ( `-it` ) pour rester dans le conteneur
docker run -it -v C:\mon_repertoire_partage_windows:/mon_repertoire_partage_linux bash
# Afficher le fichier dans le conteneur : 
ls /mon_repertoire_partage_linux
```

```
# 2.
docker volume create mon_volume
# Créer les 2 conteneurs utilisant le volume
docker run -it -v mon_volume:/mon_repertoire_partage_1 bash
docker run -it -v mon_volume:/mon_repertoire_partage_2 bash
# Dans le 1er conteneur, création d'un fichier
echo 'salut' >> /mon_repertoire_partage_1/mon_fichier
# Dans le 2e conteneur, affichage du fichier
cat /mon_repertoire_partage_2/mon_fichier
```
:::

## Gestion du réseau

1. Créer un conteneur ne possédant pas d'accès réseau :
  + On utilisera l'image : `bash`.
  + Vérifier que le conteneur ne peut pas atteindre l'extérieur (`ping`)
  + Vérifier que les autres conteneurs ne peuvent pas atteindre ce conteneur (`ping`)
2. Créer un conteneur utilisant directement l'interface réseau de l'hôte :
  + On utilisera l'image : `bash`.
  + Vérifier dans le conteneur l'accès direct à l'interface réseau (`ip addr show`)
  + Vérifier que le conteneur peut atteindre l'extérieur (`ping`)
3. Créer deux conteneurs pouvant communiquer entre eux mais pas avec l'extérieur
  + On utilisera l'image : `bash`.
  + Vérifier que les conteneurs peuvent communiquer entre eux
4. Créer un conteneur exposant son port 80 sur le port 8181 de l'hôte :
  + On utilisera l'image : `nginx`.
  + Vérifier que le service du conteneur est accessible depuis l'hôte à l'adresse : `http://localhost:8181`

::: {.correction .if correction="true"}
```
# 1.
docker run -it --network none bash
ping google.fr # pas de réponse
# depuis Windows :
ping NOM_DU_CONTENEUR (remplacer NOM_DU_CONTENEUR par le nom du conteneur obtenu avec docker ps) # pas de réponse

## Par exemple :
docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS     NAMES
78ea503fc460   bash      "docker-entrypoint.s…"   7 seconds ago   Up 5 seconds             compassionate_neumann

ping compassionate_neumann
```
:::

::: {.correction .if correction="true"}
```
# 2.
docker run -it --network host bash

# On voit toutes les interfaces de la machine physique :

bash-5.2# ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN qlen 1000
    link/ether 50:7b:9d:c8:27:9a brd ff:ff:ff:ff:ff:ff
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP qlen 1000
    link/ether 10:02:b5:c4:1a:d0 brd ff:ff:ff:ff:ff:ff
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN 
    link/ether 02:42:3e:f0:7e:aa brd ff:ff:ff:ff:ff:ff

bash-5.2# ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN qlen 1000
    link/ether 50:7b:9d:c8:27:9a brd ff:ff:ff:ff:ff:ff
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP qlen 1000
    link/ether 10:02:b5:c4:1a:d0 brd ff:ff:ff:ff:ff:ff
    inet 10.132.149.7/22 scope global wlan0
       valid_lft forever preferred_lft forever
    inet6 fe80::1202:b5ff:fec4:1ad0/64 scope link 
       valid_lft forever preferred_lft forever
4: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN 
    link/ether 02:42:3e:f0:7e:aa brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:3eff:fef0:7eaa/64 scope link 
       valid_lft forever preferred_lft forever

# On peut joindre le réseau
bash-5.2# ping google.fr
PING google.fr (172.217.20.163): 56 data bytes
64 bytes from 172.217.20.163: seq=0 ttl=114 time=11.628 ms
64 bytes from 172.217.20.163: seq=1 ttl=114 time=13.752 ms
```
:::

::: {.correction .if correction="true"}
```
# 3. Créer deux conteneurs pouvant communiquer entre eux mais pas avec l'extérieur
# On crée un bridge privé :
docker network create --internal reseau-interne
# Note : `--internal` est optionnel (choix par défaut)

# Dans un 1er terminal
docker run -it --name conteneur1 --network reseau-interne bash

# Dans un 2e terminal
docker run -it --name conteneur2 --network reseau-interne bash

# Terminal 1 :
ping conteneur2 # OK
ping google.fr # KO
# Terminal 2 :
ping conteneur1 # OK
ping google.fr # KO
```
:::

::: {.correction .if correction="true"}
```
# 4. Créer un conteneur exposant son port 80 sur le port 8181 de l'hôte :
docker run -p 8181:80 nginx

# Vérifier http://localhost:8181
```
:::

## Interface utilisateur

Il est possible d'utiliser une interface utilisateur en ligne de commande pour simplifier la gestion des conteneurs.

On peut pour cela installer `lazydocker`, mais puisque nous avons maintenant une stack `Docker` fonctionnelle, autant tourner `lazydocker` en `docker` pour monitorer les conteneurs… depuis un conteneur !

```sh
# -v /var/run/docker.sock:/var/run/docker.sock
# permet de récupérer la socket du dæmon Docker dans le conteneur
# pour faire du Docker dans du Docker.
# Cette pratique est interdite en production ! ("docker in docker")
docker run --name lazydocker -it -v /var/run/docker.sock:/var/run/docker.sock lazyteam/lazydocker
# Ou une autre interface : _Go Manage Docker_ :
docker run -it -v /var/run/docker.sock:/var/run/docker.sock kakshipth/gomanagedocker:latest
```

## Récupération des logs du conteneur 

Les programmes qui tournent dans un conteneur ne sont pas gérés intégralement par le système d’exploitation de l’hôte : il faut donc un système annexe pour, par exemple, récupérer les logs de conteneurs. 

1. Comment les applications exposent-elles ces logs à Docker® ?
2. Utiliser les commandes Docker® pour récupérer dynamiquement les logs des conteneurs en cours d’exécution.

::: {.correction .if correction="true"}
```sh
# Pour récupérer les logs actuels :
docker logs mon_conteneur

# Ou pour suivre dynamiquement (_follow_) les nouveaux logs :
docker logs -f mon_conteneur
```
:::

## Limiter les ressources du conteneur 

Docker® n’est pas un système de machines virtuelles à proprement parler, mais permet d’en simuler l'usage. Un des intérêts de la virtualisation est l’isolation des ressources, afin de ne pas perturber le reste du système. 

1. Utiliser les commandes Docker® pour limiter les ressources disponibles pour un conteneur.
2. Quelle est la bonne pratique pour changer les ressources disponibles d'un conteneur en cours d'exécution ?

::: {.correction .if correction="true"}
```sh
docker run --memory="1g" --cpus=".5" mon_image
```

La bonne pratique pour changer les ressources disponibles d'un conteneur en cours d'exécution est de le détruire et de recréer un conteneur avec les ressources voulues.
:::

## Docker comme outil sur sa machine personnelle

Docker permet aussi d'utiliser des environnements reproductibles sur sa machine personnelle (pour le développement, pour des tests, …).

### Un mini serveur Web

Docker® est très utile pour tester sur sa machine des exécutions proches d'un environnement de production. Comme exemple simpliste, on peut utiliser un mini serveur Web pour charger des pages statiques.

1. Utiliser l'image `nginx` pour servir du contenu Web statique depuis le répertoire courant.

::: {.correction .if correction="true"}
```sh
# $PWD est la variable décrivant le chemin absolu du répertoire courant.
# On peut aussi fournir directement un autre répertoire sur le système hôte (Windows, …)
docker run --rm -d -v "${PWD}:/usr/share/nginx/html" -p 8080:80 nginx
```
:::

### Utiliser la même version des outils partagés par l'équipe à travers Docker® 

Docker® peut être utilisé pour partager un outil à l'ensemble de l’équipe projet, et ainsi garantir d’utiliser exactement le même environnement. Cela est aussi utile pour utiliser des programmes initialement écrits pour un autre système d’exploitation (majoritairement Linux). 

1. Créer une image Docker® depuis un système Alpine et contenant l'utilitaire `tar`.
2. Utiliser l'image créée pour partager la même version de `tar` et créer une archive d'un fichier sur l'hôte. On utilisera la commande : `tar czf mon_archive.tgz mon_fichier_à_archiver.txt`
3. Utiliser cette même image pour lister le contenu de l'archive : `tar tzvf mon_archive.tgz`
4. Utiliser cette même image pour extraire le contenu de l'archive : `tar xzvf mon_archive.tgz`

::: {.correction .if correction="true"}
```sh
# Création de l'image : on crée un Dockerfile (ou avec un éditeur de texte)
cat << EOF > Dockerfile
FROM alpine:edge
RUN apk add --no-cache tar

WORKDIR /archive
ENTRYPOINT ["/usr/bin/tar"]
CMD ["--usage"]
EOF

# Build de l'image
docker build . -t mon-archiver:1.0

# Création d'un fichier à archiver
echo 'le contenu du fichier' > mon_fichier.txt

# Sans commande, par défaut on affiche l'usage de la commande `tar` :
docker run --rm -v ${PWD}:/archive mon-archiver:1.0
# Archivage du fichier : "tar czf mon_archive.tgz mon_fichier.txt"
docker run --rm -v ${PWD}:/archive mon-archiver:1.0 czf mon_archive.tgz mon_fichier.txt
# Affichage du contenu de l'archive : "tar tzvf mon_archive.tgz"
docker run --rm -v ${PWD}:/archive mon-archiver:1.0 tzvf mon_archive.tgz mon_fichier.txt
# Extraction du contenu de l'archive : "tar xzvf mon_archive.tgz"
docker run --rm -v ${PWD}:/archive mon-archiver:1.0 xzvf mon_archive.tgz mon_fichier.txt
```
:::

### Un LLM local avec Ollama

1. Utiliser Docker pour tester différents modèles d'IA sur sa machine en utilisant `ollama`.

::: {.correction .if correction="true"}
Voir : <https://hub.docker.com/r/ollama/ollama>
:::

\newpage{}

## Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Docker and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Oracle and VirtualBox are registered trademarks of Oracle and/or its affiliates.
- Linux is a registered trademark of Linus Torvalds.
- Mac and Mac OS are trademarks of Apple Inc., registered in the U.S. and other countries.
- Windows is a registered trademark of Microsoft Corporation in the United States and other countries.
