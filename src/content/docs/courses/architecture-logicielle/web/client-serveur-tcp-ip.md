---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Applications client/serveur sur TCP/IP
tags:
- architecture
- client-server
type: cours
sidebar:
  order: 4
---

## Généralités

La plupart des protocoles applicatifs sur `TCP/IP` sont des protocoles apparus au début d'Internet.
Les besoins de sécurité ayant évolué, beaucoup de ces services sont aujourd'hui disponibles en version sécurisée, la plupart du temps encapsulés dans une connexion `SSL` (Secure Socket Layer) ou `TLS` (Transport Layer Security).

Lorsqu'une version sécurisée est disponible, un `S` est ajouté à la fin du nom du protocole : `HTTPS`, `IMAPS`, ...

## Connexions à distance

### telnet [TCP]

`telnet` (terminal network ou telecommunication network ou teletype network) :

- protocole très généraliste
- communication en mode texte avec un serveur distant
- peu utilisé aujourd'hui : la communication circule en clair sur le réseau
- préférer `ssh`, sauf sur certains matériels réseau.

Permet d'établir une connexion `TCP` interactive avec d'autres services tels que `SMTP`, `HTTP`, `POP`, `IMAP` à des fins de tests.

### rlogin [TCP 513]

- Commande Unix permettant d'ouvrir une session en ligne de commandes sur une machine distante.
- idem `telnet` : préférer `ssh` plus sécurisé et ayant plus de fonctionnalités

```sh
rlogin <machine distante> -l <nom de l'utilisateur>
```

### ssh [TCP 22]

`ssh` (Secure SHell) est un protocole de communication sécurisé conçu pour remplacer les différents protocoles non chiffrés comme `rlogin`, `telnet`, `rcp` et `rsh`.

- Utilisé majoritairement pour ouvrir un shell sur un ordinateur distant Unix.
- Peut aussi transférer des ports `TCP` d'une machine vers une autre afin de sécuriser une connexion qui ne l'est pas (`POP3`, …) dans un tunnel chiffré
- Impose un échange de clés de chiffrement en début de connexion : tous les segments `TCP` sont authentifiés et chiffrés
- Compatible cryptographie asymétrique (`RSA`/`DSA`) avec clef privée/publique
- `sshv2` fournit `scp` et `sftp` avec la même configuration

### X11

`X`, `X Window`, `X11` est un protocole de système de fenêtrage qui permet de tourner des applications graphiques et gère les périphériques d'entrée (clavier, souris, ...).

C'est le système standard sur les UNIX (Linux, BSD, …), optionnel sur MacOS, installable sur Windows.

Fonctionnement client–serveur :

- Le serveur `X` tourne sur un client léger doté d'un écran, d'un clavier et d'une souris
- Un ou des clients `X` (locaux ou distants) se connectent au serveur et lui envoient leurs requêtes d'affichage

Le client est simplement l'application logicielle (jeu, traitement de texte, calculatrice…) qui utilise alors le protocole `X` pour déléguer au serveur `X` les tâches d'interactions homme/machine (ou IHM).

## Transfert de fichiers

### SCP

`scp` (Secure copy) :

- protocole de copie de fichiers similaire à la commande Unix `cp`
- disponible à travers le réseau
- utilise `ssh` pour sécuriser la transaction distante

```sh
scp FichierSource utilisateur@serveur:Repertoire/FichierCible # Upload
scp utilisateur@serveur:Repertoire/FichierSource FichierCible # Download
```

`scp` est normalement toujours disponible dans les implémentations des serveurs `ssh`.

### FTP [TCP commandes:21 / données:20(actif) ou aléatoire (passif)]

FTP (File Transfer Protocol) est un protocole de communication client-serveur destiné au partage de fichiers sur un réseau `TCP/IP`.

Une URI FTP s'écrit sous la forme : `ftp://server/path/to/resource`

Le protocole utilise deux types de connexions `TCP` :

- Une connexion de contrôle initialisée par le client pour transmettre les commandes concernant les fichiers (suppression de fichiers, renommage, liste des fichiers…).
- Une connexion de données initialisée par le client ou le serveur pour transférer les données requises (contenu des fichiers, liste de fichiers).

### FTPS [explicite:21 / implicite:990+989]

`ftps` est la version sécurisée du protocole FTP qui peut utiliser un chiffrement explicite ou implicite :

- chiffrement explicite : connexion port de commande 21 via `ftp://` et demande `SSL/TLS` pour la suite. Compatible `FTP` classique (non chiffré)
- chiffrement implicite (idem `HTTPS`) : connexion SSL/TLS au port de commande 990 via `ftps://` et données chiffrées port 989. Non compatible `FTP` classique. Méthode dépréciée.

### SFTP [TCP 22]

`sftp` (SSH FTP ou Secured FTP) est une autre version sécurisée de `FTP` qui utilise une encapsulation `ssh`.

`sftp` propose donc bien plus de fonctionnalités que `scp` et lui est souvent préféré.

### TFTP [UDP 69 (transport)]

`TFTP` (Trivial File Transfer Protocol) est une simplification du protocole `FTP` :

- pas de listage de fichiers
- pas de mécanismes d'authentification ni de chiffrement

Il faut connaître à l'avance le nom du fichier que l'on veut récupérer.

Aucune notion de droits de lecture/écriture n'est disponible en standard.

`TFTP` est très utilisé pour la mise à jour des logiciels embarqués sur les équipements réseaux (routeurs, pare-feu, etc.) ou pour démarrer un PC à partir d'une carte réseau.

### NFS [UDP <= NFSv3 / `TCP` ou autres >= NFSv4]

`NFS` (Network File System) est un protocole qui permet à un ordinateur d'accéder via un réseau à des fichiers distants en montant localement sur un client le système de fichiers distants du serveur.

`NFS` utilise le protocole `RPC` et fonctionne principalement entre systèmes UNIX mais des versions existent pour Mac et Windows.

Les dernières versions de `NFS` proposent des opérations puissantes de gestion de système de fichiers distants : chiffrement des communications, délégation (fichier géré en local), migration et réplication du serveur, reprise sur incidents.

### SMB [TCP 445 / NetBIOS 139]

Le protocole `SMB` (Server Message Block), autrefois `CIFS`, est un protocole permettant le partage de ressources (fichiers et imprimantes) sous Windows. Une implémentation libre `Samba` existe pour la plupart des OS.

`SMB` fonctionne via une structure de client/serveur, le client va envoyer des requêtes spécifiques et le serveur de fichiers va y répondre. Le protocole est optimisé pour une utilisation dans un réseau local, mais il peut aussi être utilisé sur Internet.

Les ressources partagées sont accessibles à partir d'une adresse utilisant la convention `UNC` de type :

```
\\serveur\partage\chemin\nom_fichier
```

## Gestion d'utilisateurs distants

### NIS

`NIS` (Network Information Service), ou `Yellow Pages` est un protocole client serveur permettant la centralisation d'informations sur un réseau UNIX.

Un serveur `NIS` stocke et distribue les informations administratives du réseau, qui se comporte ainsi comme un ensemble cohérent de comptes utilisateurs (`/etc/passwd`), groupes, machines (fichiers de noms d'hôte `/etc/hosts`), ...

Le client récupère les informations en interrogeant le serveur à partir d'appels `RPC` grâce à des commandes d'administration dédiées : `yppasswd,ypwhich,...`

`NIS` est réputé pour être faible en matière de sécurité.
`NIS+` une réécriture complète de `NIS`, également plus sécurisée mais on lui préfère de plus en plus `ldap` ou `kerberos`.

## Le courrier électronique

### POP(S) [TCP 110 / S:995]

Le protocole `POP3` (Post Office Protocol), permet de récupérer les mails situés sur un serveur de messagerie électronique.

Le fonctionnement de `POP` est simple : le client se connecte au serveur de messagerie, s'authentifie, récupère le courrier, efface le courrier sur le serveur (optionnel), et se déconnecte.

Toute opération supplémentaire est donc réalisée directement sur le client. Pour cette raison, on lui préfère de plus en plus `IMAP` qui permet des opérations complexes directement sur le serveur.

`POP3` est encore disponible sur presque tous les serveurs de messagerie électronique en mode SaaS.

L'envoi de mails se fait en général en utilisant `SMTP`.

### IMAP(S) [TCP 143 / S:993]

`IMAP` (Internet Message Access Protocol), est un protocole qui permet d'accéder à ses courriers électroniques directement sur les serveurs de messagerie.

Les messages étant gérés directement sur le serveur, le multi-client est grandement facilité.

`IMAP` fournit des opérations avancées directement sur le serveur : création de dossiers, tri des emails, ...

`IMAP` est aujourd'hui presque toujours disponible sur les serveurs de messagerie électronique en mode SaaS.

L'envoi de mails se fait en général en utilisant `SMTP`.

### SMTP(S) [TCP 25 / implicite:465  / explicite:587]

`SMTP` (Simple Mail Transfer Protocol) est un protocole de communication utilisé pour envoyer un courrier électronique d'un client vers les serveurs de messagerie électronique.

Le protocole assez simple : on commence par spécifier l'expéditeur du message, puis le ou les destinataires d'un message, puis, en général après avoir vérifié leur existence, le corps du message est transféré.

`SMTP` est le protocole ultra majoritaire dans l'envoi de courriers électroniques.

### Webmail

Une messagerie Web (Webmail) est une interface web rendant possible l'émission, la consultation et la manipulation de courriers électroniques directement sur le Web depuis un navigateur.

C'est en fait un client de messagerie qui s'exécute dans un serveur Web.
Le serveur Web effectue alors les requêtes locales ou distantes vers le serveur de messagerie.

L'avantage principal d'un Webmail est d'éviter la configuration du client de messagerie et l'ouverture de ports dédiés sur le client. 🌟
Cependant, les courriers électroniques ne sont alors plus accessibles en local.

## Un annuaire fédérateur

### LDAP(S) [TCP 389 / S:636]

`LDAP` (Lightweight Directory Access Protocol) est une norme pour les systèmes d'annuaires, incluant un modèle de données, un modèle de nommage, un protocole, un modèle de sécurité et un modèle de réplication.

`ldaps` : `ldap` + tunnel `ssl/tls`

Le nommage des éléments constituant l'arbre `LDAP` reflète souvent le modèle politique, géographique ou d'organisation de la structure représentée :

- `DNS` pour racine et premières branches (domain components ou `dc=…`)
- pour les branches plus profondes : groupes (organizational units ou `ou=…`) ou personnes (common name ou `cn=…` voir user identifier `uid=…`)

L'assemblage de tous les composants (du plus précis au plus général) d'un nom forme son `distinguished name` :

- `cn=ordinateur, ou=machines, dc=EXEMPLE, dc=FR`
- `cn=Jean, ou=personnes, dc=EXEMPLE, dc=FR`

```
            dc=FR
              |
          dc=EXEMPLE
         /          \
   ou=machines    ou=personnes
       /              \
cn=ordinateur       cn=Jean
```

## L'administration de réseaux

### SNMP [UDP 161 / 162]

`SNMP` (Simple Network Management Protocol) est un protocole de communication qui permet de gérer les équipements du réseau, de superviser et de diagnostiquer des problèmes réseaux et matériels à distance : commutateurs, concentrateurs, routeurs, postes de travail, serveurs physiques ou virtuels, ...

`SNMP` est composé de trois types de composants : des `NMS` (network management systems) pour exécuter les requêtes de gestion, des nœuds (équipement géré) et des agents (transmettent les messages `SNMP` entre les nœuds et les `NMS`).

Les objets `SNMP` contenus dans les nœuds peuvent être des informations matérielles, des paramètres de configuration, des statistiques de performance et autres objets qui sont directement liés au comportement en cours de l'équipement en question.

`SNMP` est très utilisé et de nombreux outils l'intègrent pour effectuer de la surveillance et maintenance applicative et matérielle : `Zabix`, `Nagios`, ...

## Ressources

- [Programmation de sockets][developpez-sockets]
- [Synchronisation de processus - cours sur les moniteurs (_Samia Bouzefrane, CNAM_)][cours-moniteurs]

[developpez-sockets]: https://laissus.developpez.com/tutoriels/cours-introduction-tcp-ip/?page=page_13
[cours-moniteurs]: http://deptinfo.cnam.fr/new/spip.php?pdoc4762
