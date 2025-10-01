---
title: 📦 Les cgroups
---

## Introduction

Les **cgroups** (Control Groups) sont un mécanisme du noyau Linux permettant de limiter, comptabiliser et isoler l'utilisation des ressources système (CPU, mémoire, disque, réseau, etc.) par des groupes de processus. Ceux-ci permettent d'améliorer la gestion des ressources dans les environnements multi-utilisateurs ou conteneurisés (comme Docker ou Kubernetes), garantissant une meilleure stabilité et performance du système. En associant des processus à des hiérarchies de cgroups, il devient possible de définir des quotas, des priorités ou même de suspendre des groupes de tâches.

:::tip
Les _cgroup_ sont hiérarchiques et héritent des limites de leurs parents.
:::

## Vérifier le montage des cgroups

```bash
mount -l | grep cgroup2
ls /sys/fs/cgroup/
```

## Créer un cgroup

### Manuellement

1. Création du cgroup
    ```bash
    mkdir /sys/fs/cgroup/new-cgroup
    ```
2. Limiter l'utilisation de la mémoire à 500M
    ```bash
    echo 500M > /sys/fs/cgroup/new-cgroup/memory.max
    ```
3. Limiter l'utilisation CPU à 50%
    ```bash
    echo "50000 100000" > /sys/fs/cgroup/new-cgroup/cpu.max
    ```
4. Affecter le processus courant ($$) au cgroup
    ```bash
    echo $$ >> /sys/fs/cgroup/new-cgroup/cgroup.procs
    ```

### En utilisant _cgroup-tools_

1. Création du cgroup
    ```bash
    cgcreate -g cpu,memory:test
    ```
2. Test du Cgroup en utilisant `stress-ng` :
    ```bash
    cgexec -g cpu:test -g memory:test stress-ng --cpu 4 --vm 10
    ```
3. Limiter l'utilisation de la mémoire à 500M
    ```bash
    cgset -r memory.max=500M test
    ```
4. Affecter le processus courant ($$) au cgroup
    ```bash
    cgclassify -g cpu:test $$
    ```

### En utilisant systemd

Voir le tutoriel : <https://docs.oracle.com/en/operating-systems/oracle-linux/9/systemd/SystemdMngCgroupsV2.html>

## Limiter les ressources d'un groupe de conteneurs

_Docker_ permet de limiter les ressources d'un conteneur (en appliquant pour nous un _cgroup_ par conteneur). Mais comment faire si l'on veut limiter les ressources d'une stack de conteneurs (par exemple l'entièreté de notre application composée d'un backend, d'une BDD et d'un frontend) ?

Il n'est pas possible de démarrer plusieurs conteneurs dans le même _cgroup_ mais on peut jouer sur la hierarchie des cgroups.

```sh
docker run --cgroup-parent cgroup-stack backend
docker run --cgroup-parent cgroup-stack bdd
docker run --cgroup-parent cgroup-stack frontend
```

:::tip
_Docker Compose_ utilise la propriété `cgroup_parent` :

```yaml
cgroup_parent: cgroup-stack
```
:::

:::tip
_Docker_ utilise par défaut _systemd_ pour la gestion des _cgroups_ (et _Kubernetes_ recommande d'utiliser _systemd_ lorsqu'il est disponible).
Dans ce cas, _systemd_ impose que le `cgroup_parent` soit un [slice](https://www.man7.org/linux/man-pages/man5/systemd.slice.5.html) : il suffit d'utiliser directement _systemd_ pour créer le _cgroup_ parent correctement.
:::

## OOMKiller et cgroup

Lorsqu'un processus tente d'utiliser plus que la quantité de mémoire disponible, le noyau tue le processus (`SIGKILL`) et envoie un event `OOM` (_Out of Memory_). Dans le cas d'un _cgroup_, il peut y avoir plusieurs processus dans le groupe : le noyau tente donc de tuer l'un des processus (en principe, celui utilisant le plus de ressources).

Cela peut être problématique (_Pod_ Kubernetes ou _Conteneur_ Docker avec plusieurs processus, serveur web incohérent, …). Dans un cgroup, on peut préférer de tuer l'intégralité du _cgroup_ en cas de dépassement de mémoire.

Dans ce cas, on activera la propriété `memory.oom.group` des cgroups :

```
# memory.oom.group
1
```

Pour plus d'information, voir : <https://lore.kernel.org/all/20180730180100.25079-4-guro@fb.com/>

:::tip
- _Systemd_ possède une option similaire à la création d'un cgroup :
    ```bash
    systemd-run -p OOMPolicy=kill …
    ```
- _Nerdctl_ et _Podman_ permettent de changer cette propriété au démarrage d'un conteneur :
    ```bash
    nerdctl run --cgroup-conf=memory.oom.group=1 ...
    ```
- _Docker_ met toujours `memory.oom.group` à 0 : il faut donc trouver le _cgroup_ du conteneur et changer la propriété manuellement.
- _Kubernetes_ a changé plusieurs fois de comportement : `memory.oom.group=0` si k8s <= v1.28 ; `memory.oom.group=1` si v1.28 < k8s < 1.32 ; `memory.oom.group=1` par défaut mais [modifiable par option Kubelet : `singleProcessOOMKill`](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md) si k8s >= 1.32
:::

