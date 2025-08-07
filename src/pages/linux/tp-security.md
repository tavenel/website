---
title: Sécurité sous Linux
date: 2024 / 2025
---

## Définition ou modification des mots de passe utilisateur ainsi que des informations d'expiration du compte.

:::exo
En utilisant les commandes `passwd` et `chage` :

  1. changer le mote de passe de l'utilisateur depuis le compte `root`
  2. mettre au point une politique de sécurité avec une expiration des mots de passe
  3. vérifier que la poliitque est bien implémentée
:::

:::correction
```sh
passwd nom_utilisateur
chage -M 90 nom_utilisateur
chage -l nom_utilisateur
```
:::

## Détermination des connexions utilisateur passées ou actuelles.

:::exo
En utilisant les commandes `who`, `w` et `last`, déterminer les connexions utilisateur actuelles et passées.
:::

## Élévation de privilèges

`sudo` permet une élévation de privilège, c'est-à-dire d'exécuter temporairement la prochaine commande avec les droits d'un autre utilisateur. On utilise en principe `sudo` pour passer `root` pendant l'usage de commandes critiques mais l'option `-u` permet de passer par un autre compte utilisateur (utile par exemple pour tester des configurations).

:::exo
Utiliser le tutoriel : <https://doc.ubuntu-fr.org/sudoers> pour configurer correctement `sudo` sur votre système.
:::

## Définition des limites utilisateur pour les connexions, les processus et l'utilisation de la mémoire.

### `ulimit` : limiter les ressources des processus

La commande `ulimit` est utilisée pour afficher ou modifier les limites des ressources pour les processus en cours d'exécution sur un système Linux. Elle permet de contrôler et de limiter différentes ressources système telles que la quantité de mémoire virtuelle, le nombre de fichiers ouverts, la taille du segment de mémoire partagée, etc., pour chaque processus ou pour l'utilisateur actuel.

`ulimit` peut être utilisé par un utilisateur pour limites les ressources de ses propres processus, mais il existe des limites imposées par le système qui peuvent être modifiées uniquement par l'administrateur système.

:::tip
Les modifications de `ulimit` son temporaires.

Pour les rendre permanentes, il faut éditer le fichier `/etc/security/limits.conf`.
:::

#### Exemples

- Afficher les limites actuelles des ressources pour le shell en cours d'exécution : `ulimit -a`
- Afficher la limite maximale de fichiers ouverts pour le shell en cours d'exécution : `ulimit -n`
- Définir la limite maximale de fichiers ouverts pour le shell en cours d'exécution : `ulimit -n 1000`
- Définir la limite maximale de mémoire virtuelle pour le shell en cours d'exécution (en kilo-octets) : `ulimit -v 1000000`
- Définir la limite maximale de taille de fichier (en kilo-octets) : `ulimit -f 5000`

:::exo
1. Afficher les limites de ressources actuelles du shell courant.
2. Limiter la mémoire virtuelle du shell courant à 200MB.
3. Limiter la taille maximale de fichier depuis le shell courant à 10 KB.
4. Tester cette limite.
5. Rendre les limitations permanentes.
:::

:::correction
1. Afficher les limites de ressources actuelles du shell courant.

```console
$ ulimit -a

real-time non-blocking time  (microseconds, -R) unlimited
core file size              (blocks, -c) 0
data seg size               (kbytes, -d) unlimited
scheduling priority                 (-e) 0
file size                   (blocks, -f) unlimited
pending signals                     (-i) 3529
max locked memory           (kbytes, -l) 8192
max memory size             (kbytes, -m) unlimited
open files                          (-n) 1024
pipe size                (512 bytes, -p) 8
POSIX message queues         (bytes, -q) 819200
real-time priority                  (-r) 0
stack size                  (kbytes, -s) 8192
cpu time                   (seconds, -t) unlimited
max user processes                  (-u) 3529
virtual memory              (kbytes, -v) unlimited
file locks                          (-x) unlimited
```

2. Limiter la mémoire virtuelle du shell courant à 200MB.

```sh
ulimit -v 204800
```

3. Limiter la taille maximale de fichier à 10 KB.

```sh
ulimit -f 10
```

4. Tester cette limite : vérification des limitations et création (interdite) d'un fichier de 11 KB.

```console
$ ulimit -a   

real-time non-blocking time  (microseconds, -R) unlimited
core file size              (blocks, -c) 0
data seg size               (kbytes, -d) unlimited
scheduling priority                 (-e) 0
file size                   (blocks, -f) 10
pending signals                     (-i) 3529
max locked memory           (kbytes, -l) 8192
max memory size             (kbytes, -m) unlimited
open files                          (-n) 1024
pipe size                (512 bytes, -p) 8
POSIX message queues         (bytes, -q) 819200
real-time priority                  (-r) 0
stack size                  (kbytes, -s) 8192
cpu time                   (seconds, -t) unlimited
max user processes                  (-u) 3529
virtual memory              (kbytes, -v) 204800
file locks                          (-x) unlimited

$ dd if=/dev/zero of=testfile bs=1K count=11
File size limit exceeded
```

5. Rendre les limitations permanentes.

```console
$ cat /etc/security/limits.d/99-tp.conf 

* soft as 204800
* hard as 204800
* soft fsize 10
* hard fsize 10
```
:::

### `fuser` : afficher les processus utilisant un fichier

La commande `fuser` (File User) est utilisée pour afficher les processus qui utilisent les fichiers spécifiés sur un système Linux. Elle permet d'identifier les processus qui ont ouvert ou verrouillé un fichier donné, ce qui peut être utile pour diagnostiquer les problèmes de verrouillage de fichiers, de terminaison de processus, etc. ou simplement pour en savoir plus sur l'utilisation des ressources système.

#### Exemples

- Afficher les processus qui utilisent un fichier : `fuser nom_fichier`
- Afficher les processus qui utilisent un répertoire : `fuser -m chemin_du_répertoire`
- Tuer les processus qui utilisent un fichier spécifique : `fuser -k nom_fichier`
- Afficher les PID des processus qui utilisent un fichier spécifique : `fuser -u nom_fichier`

:::exo
1. Créer un fichier `mon_fichier`
2. Afficher le contenu du fichier en temps réel : `tail -f mon_fichier`
3. Dans un autre terminal, vérifier que le processus `tail` est bien en train d'utiliser le fichier.
4. Tuer le processus `tail`
:::

:::correction
```sh
echo 'une_ligne' > mon_fichier
tail -f mon_fichier
fuser mon_fichier
fuser -k mon_fichier
```
:::

### `lsof` : afficher les fichiers ouverts

`lsof` permet d'afficher les fichiers ouverts par un processus ou un utilisateur (ou globalement).

#### Exemples

- Afficher tous les fichiers ouverts sur le système : `lsof`
- Afficher les fichiers ouverts par un processus spécifique (en remplaçant PID par l'identifiant du processus) : `lsof -p PID`
- Afficher les fichiers ouverts par un utilisateur spécifique (en remplaçant username par le nom de l'utilisateur) : `lsof -u username`
- Afficher les fichiers ouverts par un processus spécifique sur un répertoire particulier : `lsof -p PID | grep /chemin/du/répertoire`
- Afficher les fichiers ouverts par un programme exécutable spécifique : `lsof /chemin/vers/programme`

:::exo
1. Forcer l'ouverture d'un I/O sur un fichier (par exemple avec la commande `tail -f …`).
2. Utiliser `lsof` pour afficher tous les fichiers ouverts.
:::

## Introduction aux Namespace

Le noyau Linux permet de séparer des espaces de noms pour plusieurs types de ressources (c'est une des technologies à la base de Docker !). Ces espaces de noms sont totalement isolés par le noyau et ne peuvent pas échanger de données.

:::exo
Utiliser la commande `ip netns` pour créer un namespace. En utilisant la commande `python3 -m http.webserver`, démarrer un serveur web dans le network namespace créé et vérifier que seul le namespace a accès au réseau.
:::

:::correction
```sh
ip netns add net1
ip netns exec net1 ip a
ip netns exec net1 ip link set lo up
ip netns exec net1 python3 -m http.webserver
curl localhost:8000 # erreur
ip netns exec net1 curl localhost:8000 # OK
```
:::

## Arrêt des services inutiles.

:::exo
Une bonne pratique de sécurité est d'utiliser les gestionnaires de services pour arrêter tous les services inutiles.

1. Utiliser et configurer `systemd` pour désactiver de manière permanente tout service inutile.
:::

## Démarrage dynamique de service depuis une socket

Le but de cet exercice est de démarrer le service `SSH` uniquement lorsqu'une connexion est demandée.

### xinetd

Le fichier de configuration de `xinetd` ressemblerait à :

```
service ssh {
        socket_type = stream
        protocol = tcp
        wait = no
        user = root
        server = /usr/sbin/sshd
        server_args = -i
}
```

:::tip
Le port 22 n'est pas mentionné ici - `xinetd` va trouver ce port en cherchant le service `ssh` dans `/etc/services`.
:::

### systemd.socket

Pour `systemd.socket`, le fichier de configuration `/etc/systemd/system/sshd.socket` ressemblerait à :

```ini
[Unit]
Description=SSH Socket for Per-Connection Servers

[Socket]
ListenStream=22
Accept=yes

[Install]
WantedBy=sockets.target
```

Ce ficher fait référence au service `SSH` configuré dans : `/etc/systemd/system/sshd.service`.

```ini
[Unit]
Description=SSH Per-Connection Server

[Service]
ExecStart=-/usr/sbin/sshd -i
StandardInput=socket
```

:::exo
1. Créer les fichiers de configuration.
2. Pour activer la socket, exécuter les commandes suivantes :
```sh
systemctl enable sshd.socket
systemctl start sshd.socket
systemctl status sshd.socket
```
3. Tester la connexion à la VM par un client SSH.
:::

:::correction
```console
$ systemctl enable sshd.socket
ln -s '/etc/systemd/system/sshd.socket' '/etc/systemd/system/sockets.target.wants/sshd.socket'

$ systemctl start sshd.socket
$ systemctl status sshd.socket
sshd.socket - SSH Socket for Per-Connection Servers
 	  Loaded: loaded (/etc/systemd/system/sshd.socket; enabled)
 	  Active: active (listening) since Mon, 26 Sep 2023 20:24:31 +0200; 14s ago
 	Accepted: 0; Connected: 0
 	  CGroup: name=systemd:/system/sshd.socket

$ ssh root@10.170.16.201
root@10.170.16.201's password: 
Linux debian 6.12.25-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.12.25-1 (2025-04-25) x86_64
```
:::

## Utilisation de `nmap` et `ss` pour connaître les ports ouverts sur une machine

### `ss`

La commande `ss` est un utilitaire de ligne de commande utilisé pour afficher des informations détaillées sur les sockets réseau sur les systèmes Unix et Linux. Elle est utilisée pour inspecter l'état des connexions réseau, des sockets et des interfaces réseau sur une machine. Elle remplace la commande `netstat` historique.

#### Exemples

- `ss -t` : Affiche les sockets TCP
- `ss -u` : Affiche les sockets UDP
- `ss -l` : Affiche les sockets en écoute
- `ss -s` : Affiche les statistiques réseau
- `ss -n` : ne pas résoudre les noms d'hôtes ou de services en adresses IP ou numéros de port (affiche les adresses IP et les numéros de port sous leur forme brute)

`ss` prend en charge de nombreux autres paramètres pour filtrer et afficher des informations spécifiques sur les sockets réseau.

### `nmap`

`Nmap` (_Network Mapper_) est un scanner de réseau open-source largement utilisé pour découvrir et auditer les hôtes sur un réseau, ainsi que pour analyser les services réseau et les pare-feu. Il est conçu pour être un outil polyvalent pour la découverte, l'audit de sécurité, la cartographie réseau et la gestion de la sécurité des réseaux.

Ce n'est pas un utilitaire Linux standard (il n'est donc souvent pas installé par défaut). Nmap est d'ailleurs compatible Windows et MacOS.

#### Exemples

- Balayage des ports sur une machine spécifique : `nmap adresse_ip_machine`
- Balayage des ports TCP spécifiques sur une plage d'adresses IP : `nmap -p port1,port2,port3 plage_ip`
- Balayage des ports UDP sur une plage d'adresses IP : `nmap -sU plage_ip`
- Découverte des hôtes actifs sur un réseau : `nmap -sP réseau`
- Détection des systèmes d'exploitation des hôtes : `nmap -O adresse_ip_machine`
- Balayage des ports et des services les plus courants sur une machine : `nmap -A adresse_ip_machine`
- Balayage des ports et affichage des informations détaillées : `nmap -v adresse_ip_machine`
- Balayage rapide sans résolution DNS : `nmap -T4 -F -n adresse_ip_machine`
- Balayage à partir d'un fichier contenant une liste d'adresses IP : `nmap -iL fichier_adresses`

### Exercice

:::exo
1. Utiliser la commande `nmap` pour scanner une machine distante (par exemple celle de votre binôme, s'il est d'accord) et découvrir les ports ouverts.
2. Utilisez la commande `ss` pour afficher les sockets actives sur la machine, en filtrant les connexions établies et les sockets en écoute.
3. Comparez les numéros de port trouvés avec nmap avec ceux affichés par `ss`. Vérifiez s'il y a des correspondances.
4. Quels sont les avantages de l'utilisation de `nmap` par rapport à `ss` pour scanner les ports ouverts ?
5. Pourquoi est-il important de connaître les ports ouverts sur une machine ?
:::

:::warn
Remarque : Assurez-vous d'avoir les autorisations nécessaires pour scanner des machines distantes et de respecter les politiques de sécurité en vigueur.
:::

:::correction
```sh
nmap -p- <addresse IP>
ss -tuln
```

À l'inverse de `nmap`, `ss` ne peut pas scanner de ports distants mais uniquement afficher les ports ouverts sur la machine locale. `nmap` permet donc de scanner tout un parc de machines pour faire un audit de sécurité depuis un poste central.

Il est important de connaître les ports ouverts car ce sont des sources d'intrusion sur les systèmes. Cela permet aussi de détecter d'éventuels programmes non attendus (soit parce qu'ils n'ont pas été correctement arrêtés, soit parce que la machine a été piratée).
:::

## Analyse de trafic réseau avec `tcpdump`

TCPdump permet de :

- Filtrer le trafic réseau pour des protocoles spécifiques (HTTP, DNS, etc.).
- Sauvegarder les captures pour des analyses ultérieures.

### Capture de trafic réseau

Commencez par capturer tout le trafic réseau sur votre interface par défaut (remplacez `enp0s3` par l'interface réseau de votre machine obtenue par ip addr).

1. Que remarquez-vous dans la sortie ? Quelle information est affichée ?
2. Identifiez un type de paquet (TCP, UDP, ICMP, etc.).

```sh
sudo tcpdump -i enp0s3
```

### Sauvegarder une capture dans un fichier

Pour analyser le trafic plus tard, vous pouvez sauvegarder les paquets dans un fichier :

```sh
sudo tcpdump -i enp0s3 -w capture.pcap
```

Vous pouvez ensuite ouvrir ce fichier dans `Wireshark` pour l'analyser graphiquement.

### Filtrage du trafic

#### Filtrage par adresse IP

Capturez uniquement le trafic provenant ou à destination d'une adresse IP spécifique (par exemple, `8.8.8.8` pour un serveur DNS de Google) :

1. Quelle est la différence dans la sortie par rapport à la capture précédente ?
2. Pourquoi ce type de filtrage est-il utile ?

```sh
sudo tcpdump -i enp0s3 host 8.8.8.8
```

#### Filtrage par port

Capturez uniquement le trafic HTTP (port 80) puis pour le traffic HTTPS (port 443).

1. Quels types de paquets observez-vous ?

```sh
sudo tcpdump -i enp0s3 port 80
```

### Analyse de trafic

#### Capture de requêtes DNS

Capturez uniquement les paquets DNS :

```sh
sudo tcpdump -i enp0s3 port 53
```

1. Quelles informations sur les requêtes DNS sont visibles ?
2. Quelle est l'importance de surveiller le trafic DNS dans un réseau ?

#### Capture de paquets ICMP (Ping)

Capturez uniquement les paquets ICMP pour analyser un ping :

```sh
sudo tcpdump -i enp0s3 icmp
```

1. Que remarquez-vous dans les paquets ICMP ? Identifiez un ping envoyé et une réponse reçue.
1. Pourquoi le protocole ICMP est-il crucial pour le diagnostic réseau ?

#### Bonus - Capture avec des expressions avancées : Filtrage des paquets TCP avec un SYN

Capturez uniquement les paquets TCP avec le flag SYN activé (qui initient une connexion) :

```sh
sudo tcpdump -i enp0s3 'tcp[tcpflags] & tcp-syn != 0'
```

1. Pourquoi ce type de capture est-il utile pour surveiller les tentatives de connexion ?
2. Comment pourriez-vous utiliser ce type de filtrage pour détecter des tentatives d'attaques (ex. : scan de ports) ?

## 🧭 Outil de diagnostic réseau : `mtr`

`mtr` (My Traceroute) est un outil de diagnostic réseau combinant les fonctionnalités de `traceroute` et de `ping`.

- Il affiche la route réseau vers une destination (IP ou nom DNS)
- Il mesure les statistiques de latence et de perte de paquets pour chaque routeur (ou "saut")
- Il permet une analyse continue, utile pour détecter les problèmes intermittents

### ⚙️ Fonctionnement

```console
$ mtr google.com

HOST: myserver             Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. 192.168.0.1             0.0%    10    1.0   1.2   0.9   1.5   0.2
 2. 10.0.0.1                0.0%    10    5.4   5.5   5.2   6.0   0.3
 3. 172.217.22.14           0.0%    10   20.1  20.0  19.7  20.5   0.3
```

| Colonne     | Signification                          |
|-------------|----------------------------------------|
| `Loss%`     | Pourcentage de paquets perdus          |
| `Snt`       | Nombre de paquets envoyés              |
| `Last`      | Dernier temps de réponse mesuré        |
| `Avg`       | Moyenne des temps de réponse           |
| `Best`      | Meilleur temps de réponse              |
| `Wrst`      | Pire temps de réponse                  |
| `StDev`     | Écart-type des réponses (variabilité)  |


### 📋 Options utiles

| Commande                      | Description                               |
|-------------------------------|-------------------------------------------|
| `mtr -rw google.com`         | Mode rapport (non interactif)             |
| `mtr -c 20 google.com`       | Envoie 20 paquets par saut                |
| `mtr -n google.com`          | Pas de résolution DNS (plus rapide)       |
| `mtr -b google.com`          | Affiche adresses IP + noms DNS            |
| `mtr --tcp google.com`       | Utilise TCP au lieu d'ICMP                |


### 📤 Export d'un rapport

```sh
mtr -rw -c 100 -o "LSDNBAW" google.com > rapport.txt
```

- `-rw` : mode rapport écrit
- `-c` : nombre de paquets à envoyer
- `-o` : colonnes personnalisées

:::exo
1. Utilise `mtr` pour générer un rapport de la latence des différents sauts ;
2. Analyser le rapport.
:::
