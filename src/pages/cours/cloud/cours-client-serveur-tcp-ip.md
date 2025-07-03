---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Architecture client-serveur
tags:
- architecture
- client-server
---

## Compétences à acquérir

- Connaître le modèle Client/Serveur
- Avoir des notions de conception d'applications Client/Serveur
- Connaître les protocoles applicatifs de l'Internet
- Savoir mettre en place les services associés sous Linux et sous Windows

---

## Les modes de communication entre processus

---

### Communication entre processus : `IPC`

Dans un système d'exploitation moderne :

- les processus fonctionnent en concurrence 
- les processus ont besoin de communiquer entre eux

_Comment gérer ces échanges ?_

---

Les mécanismes de communication inter-processus peuvent être classés en trois catégories :

- l'échange de données entre les processus ;
- la synchronisation entre les processus (notamment pour gérer le principe de section critique) ;
- l'échange de données et la synchronisation entre les processus.

---

### Echange de données

Les données peuvent être échangées :

- par lecture/écriture concurrente de fichiers (localement ou à distance : `NFS`)
- par espace mémoire des processus partagé : processus léger `thread`
- par partage de segments de mémoire dédiés sans partager l'espace mémoire des processus : processus lourd `process`

Problème des sections critiques : **non concurrence des modifications** ! (incohérence, inter-blocage, ...)

---

### Exemple d'échange de données père/fils (voir annexe)

---

### Synchronisation

Permet de résoudre les problèmes de sections critiques en bloquant / débloquant les accès :

- _verrous_ pour bloquer tout ou partie d'un fichier : lecture / écriture / les deux
- _sémaphores_ pour gérer des sections critiques : compteur et fonctions `P` (décrémente et blocage si compteur == 0), `V` (incrémente et débloque un des processus bloqués)
- _signaux_ : processus en attente d'un signal (`SIGSEGV`, …) pour se débloquer

---

Usage difficile : risques d'inter-blocage.

Utiliser des algorithmes éprouvés :

- _exclusion mutuelle_ - 1 processus à la fois : carte bancaire
- _cohorte_ - N processus à la fois : parking de 500 places
- _rendez-vous_ - ressource accessible après l'attente de plusieurs processus : processus devant échanger des informations entre les étapes de l'algorithme.
- _producteurs–consommateurs_ - ressource accessible après la fin d'un autre processus : réception de données puis traitement
- _lecteurs–rédacteurs_ - une seule catégorie de processus à la fois : fichier accessible à tous en lecture si pas de modification

---

### Échange de données et synchronisation

Meilleur des deux mondes, plus simples à utiliser (mais coûteux).

- Les processus envoient des informations dans une file
- Les informations sont récupérées dans cette même file au besoin : `message queue` (Unix), `socket` Unix ou `TCP/IP`, `pipes`, `message passing`

Les opérations d'écriture et de lecture dans la file sont **bloquantes** et permettent donc la synchronisation.

---

### Exemple de transfert de valeur père/fils

Exemple de programme qui saisit une valeur x au clavier dans le processus père, et transmet le sinus de ce nombre, en tant que double au processus fils.

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/wait.h>
#include <math.h>

int main(\void)
{
  pid_t pid_fils;
  int tube[2];
  double x, valeurW, valeurR;

  puts("Création d'un tube");
  if (pipe(tube) != 0)   /* pipe */
    {
      fprintf(stderr, "Erreur dans pipe\n");
      exit(1);
    }
  switch(pid_fils = fork())     /* fork */
  {
     case -1 :
        perror("Erreur dans fork\n");
        exit(errno);
     case 0 : /* processus fils */
        close(tube[1]);
        read(tube[0], &valeurR, sizeof(double));
        printf("Le fils (%d) a lu : %.2f\(\backslash\)n", getpid(), valeurR);
        break;
     default :    /* processus père */
      printf("Fermeture sortie dans le père (pid = %d)\n", getpid());
      close(tube[0]);
      puts("Entrez x :");
      scanf("%lf", &x);
      valeurW = sin(x);
      write(tube[1], &valeurW, \sizeof(\double));
      wait(NULL);
      break;
  }
  return 0;
}
```

D'une manière générale, l'adresse d'une variable peut toujours être considérée comme un tableau dont le nombre d'octet est égal à la taille de cette variable. Ceci est dû au fait qu'un tableau est seulement une adresse qui pointe vers une zone mémoire réservée pour le programme (statiquement ou dynamiquement).

---

### Exemple d'utilisation de pipe anonyme

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define BUFFER_SIZE 256

int main(void)
{
  pid_t pid_fils;
  int tube[2];
  unsigned char bufferR[256], bufferW[256];

  puts("Création d'un tube");
  if (pipe(tube) != 0)   {/* pipe */
    {
      fprintf(stderr, "Erreur dans pipe\(\backslash\)n");
      exit(1);
    }
  pid_fils = fork();     {/* fork */
  if (pid_fils == -1)
    {
      fprintf(stderr, "Erreur dans fork\(\backslash\)n");
      exit(1);
    }
  if (pid_fils == 0) {/* processus fils */
    {
      printf("Fermeture entrée dans le fils (pid = %d)\(\backslash\)n", getpid());
      close(tube[1]);
      read(tube[0], bufferR, BUFFER_SIZE);
      printf("Le fils (%d) a lu : %s\(\backslash\)n", getpid(), bufferR);
    }
  else               {/* processus père */
    {
      printf("Fermeture sortie dans le père (pid = %d)\(\backslash\)n", getpid());
      close(tube[0]);
      sprintf(bufferW, "Message du père (%d) au fils", getpid());
      write(tube[1], bufferW, BUFFER_SIZE);
      wait(NULL);
    }
  return 0;
}
```

---

### Exemple de pipe nommé

Exemple de pipe nommé (passe par un fichier sur disque) pour transmettre le mot `coucou` : les processus n'ont pas besoin de lien de parenté.

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>

int main()
{
   int fd;
   FILE *fp;
   char *nomfich="/tmp/test.txt";   /* nom du fichier */
   if(mkfifo(nomfich, 0644) != 0)  /* création du fichier */
   {
      perror("Problème de création du noeud de tube");
      exit(1);
   }
   fd = open(nomfich, O_WRONLY);  /* ouverture en écriture */
   fp=fdopen(fd, "w");  /* ouverture du flot */
   fprintf(fp, "coucou\(\backslash\)n"); /* écriture dans le flot */
   unlink(nomfich); /* fermeture du tube */
   return 0;
}
```


La fonction mkfifo prend en paramètre, outre le chemin vers le fichier, le masque des permissions (lecture, écriture) sur la structure fifo.

```c
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>

int main()
{
   int fd;
   FILE *fp;
   char *nomfich="/tmp/test.txt", chaine[50];
   fd = open(nomfich, O_RDONLY);  /* ouverture du tube */
   fp=fdopen(fd, "r");  /* ouverture du flot */
   fscanf(fp, "%s", chaine);  /* lecture dans le flot */
   puts(chaine);  /* affichage */
   unlink(nomfich);  /* fermeture du flot */
   return 0;
}
```

---

### Les socket `TCP/IP`

Une socket est un flux de communication entre deux objets `Client` et `Serveur`.

Le Client va demander un droit de créer un canal de communication avec le Serveur, puis, si celui ci accepte, le Client et le Serveur pourront communiquer.

---

La socket permet une communication logique entre des systèmes reliés au réseau internet (ou en local) en s'abstrayant des spécificités de ces systèmes.

C'est le protocole de base pour échanger sur un réseau, les sockets sont omniprésentes utilisées directement ou depuis d'autres protocoles.

---

Il existe 2 types de socket :

- le mode connecté (`TCP`) établit une connexion durable entre les deux processus : l’adresse de destination n’est pas nécessaire à chaque envoi de données
- le mode non connecté (`UDP`) : nécessite l’adresse de destination à chaque envoi et aucun accusé de réception n’est donné.

Les socket se situent entre la couche réseau (incluse) et les couches applicatives du modèle OSI (protocoles `UDP` ou `TCP` utilisant `IP` / `ARP`).

---

En `C++`, `C#`, `Java`, `Python`, etc… les fonctions sont quasiment identiques :

- Créer un objet `Socket`
- Le paramétrer (`TCP`, Internet, etc… et le `Host`, le port)
- Lancer la demande pour le client ou se mettre en `Listen` pour le serveur
- Fermer et détruire les Socket

Le mode `Listen` est le mode du Serveur qui consiste à attendre une demande de connexion d’un Client. Celle ci est souvent bloquante bien que certaines alternatives existent (`CallBack`, ...).

---

Exemple de serveur de socket en Python :

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(5)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
```

---

Exemple de client de socket en Python :

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))
s.sendall('Welcome to WayToLearnX!')
data = s.recv(1024)
s.close()
print repr(data), 'Reçue'
```

---

### Les serveurs multi-protocoles 

Un serveur peut fournir le même service sur plusieurs protocoles.

Exemple : service `DAYTIME` sur `13/TCP` et `13/UDP` (2 socket distinctes).

Permet de ne pas rationaliser les ressources du code métier : un seul déploiement pour le même service.

---

### Les serveurs multi-services

Un serveur peut fournir plusieurs services sur des socket séparées.

- limite les ressources nécessaires :  nombre de processus, ...
- possibilité de désactiver un service
- un programme différent est exécuté par service demandé

Par exemple : serveur mail `POP` + `IMAP`

---

### Les appels de procédures distantes : `RPC`

`RPC` (remote procedure call) est un protocole réseau permettant de faire des appels de procédures sur un ordinateur distant à l'aide d'un serveur d'applications.

- Un `RPC` est initié par le client qui envoie un message de requête à un serveur distant connu pour exécuter une procédure spécifique avec des paramètres spécifiques
- Le client est bloqué en attente
- Le serveur répond puis l'application continue son déroulement

---

`RPC` utilise des `stubs` pour simuler dans le code un appel local aux fonctions du serveur chez le client, ou du client chez le serveur. Ces stubs servent d'interfaces pour la procédure.

---

De nombreuses applications utilisent `(Secure)RPC` : `NFS`, `NIS`, ...

Il existe beaucoup d'implémentations (incompatibles) de `RPC`.

---
layout: section
---

## Applications client/serveur sur `TCP/IP`

---

### Généralités

La plupart des protocoles applicatifs sur `TCP/IP` sont des protocoles apparus au début d'Internet.
Les besoins de sécurité ayant évolué, beaucoup de ces services sont aujourd'hui disponibles en version sécurisée, la plupart du temps encapsulés dans une connexion `SSL` (Secure Socket Layer) ou `TLS` (Transport Layer Security).

Lorsqu'une version sécurisée est disponible, un `S` est ajouté à la fin du nom du protocole : `HTTPS`, `IMAPS`, ...

---

### Connexions à distance

---

#### telnet [TCP]

`telnet` (terminal network ou telecommunication network ou teletype network) :

- protocole très généraliste
- communication en mode texte avec un serveur distant
- peu utilisé aujourd'hui : la communication circule en clair sur le réseau
- préférer `ssh`, sauf sur certains matériels réseau.

Permet d'établir une connexion `TCP` interactive avec d'autres services tels que `SMTP`, `HTTP`, `POP`, `IMAP` à des fins de tests.

---

#### rlogin [TCP 513]

- Commande Unix permettant d'ouvrir une session en ligne de commandes sur une machine distante.
- idem `telnet` : préférer `ssh` plus sécurisé et ayant plus de fonctionnalités

```sh
$ rlogin <machine distante> -l <nom de l'utilisateur>
```

---

#### ssh [TCP 22]

`ssh` (Secure SHell) est un protocole de communication sécurisé conçu pour remplacer les différents protocoles non chiffrés comme `rlogin`, `telnet`, `rcp` et `rsh`.

- Utilisé majoritairement pour ouvrir un shell sur un ordinateur distant Unix.
- Peut aussi transférer des ports `TCP` d'une machine vers une autre afin de sécuriser une connexion qui ne l'est pas (`POP3`, …) dans un tunnel chiffré

---

- Impose un échange de clés de chiffrement en début de connexion : tous les segments `TCP` sont authentifiés et chiffrés
- Compatible cryptographie asymétrique (`RSA`/`DSA`) avec clef privée/publique
- `sshv2` fournit `scp` et `sftp` avec la même configuration

---

#### X11

`X`, `X Window`, `X11` est un protocole de système de fenêtrage qui permet de tourner des applications graphiques et gère les périphériques d'entrée (clavier, souris, ...).

C'est le système standard sur les UNIX (Linux, BSD, …), optionnel sur MacOS, installable sur Windows.

---

Fonctionnement client–serveur :

- Le serveur `X` tourne sur un client léger doté d'un écran, d'un clavier et d'une souris
- Un ou des clients `X` (locaux ou distants) se connectent au serveur et lui envoient leurs requêtes d'affichage

Le client est simplement l'application logicielle (jeu, traitement de texte, calculatrice…) qui utilise alors le protocole `X` pour déléguer au serveur `X` les tâches d'interactions homme/machine (ou IHM).

---

### Transfert de fichiers

---

#### SCP

`scp` (Secure copy) :

- protocole de copie de fichiers similaire à la commande Unix `cp`
- disponible à travers le réseau
- utilise `ssh` pour sécuriser la transaction distante

```sh
$ scp FichierSource utilisateur@serveur:Repertoire/FichierCible # Upload
$ scp utilisateur@serveur:Repertoire/FichierSource FichierCible # Download
```

`scp` est normalement toujours disponible dans les implémentations des serveurs `ssh`.

---

#### FTP [TCP commandes:21 / données:20(actif) ou aléatoire (passif)]

FTP (File Transfer Protocol) est un protocole de communication client-serveur destiné au partage de fichiers sur un réseau `TCP/IP`.

Une URI FTP s'écrit sous la forme : `ftp://server/path/to/resource`

---

Le protocole utilise deux types de connexions `TCP` :
- Une connexion de contrôle initialisée par le client pour transmettre les commandes concernant les fichiers (suppression de fichiers, renommage, liste des fichiers…).
- Une connexion de données initialisée par le client ou le serveur pour transférer les données requises (contenu des fichiers, liste de fichiers).

---

#### FTPS [explicite:21 / implicite:990+989]

`ftps` est la version sécurisée du protocole FTP qui peut utiliser un chiffrement explicite ou implicite :

- chiffrement explicite : connexion port de commande 21 via `ftp://` et demande `SSL/TLS` pour la suite. Compatible `FTP` classique (non chiffré)
- chiffrement implicite (idem `HTTPS`) : connexion SSL/TLS au port de commande 990 via `ftps://` et données chiffrées port 989. Non compatible `FTP` classique. Méthode dépréciée.

 ---

#### SFTP [TCP 22]

`sftp` (SSH FTP ou Secured FTP) est une autre version sécurisée de `FTP` qui utilise une encapsulation `ssh`.

`sftp` propose donc bien plus de fonctionnalités que `scp` et lui est souvent préféré.

---

#### TFTP [UDP 69 (transport)]

`TFTP` (Trivial File Transfer Protocol) est une simplification du protocole `FTP` :

- pas de listage de fichiers
- pas de mécanismes d'authentification ni de chiffrement

Il faut connaître à l'avance le nom du fichier que l'on veut récupérer.

Aucune notion de droits de lecture/écriture n'est disponible en standard. 

---

`TFTP` est très utilisé pour la mise à jour des logiciels embarqués sur les équipements réseaux (routeurs, pare-feu, etc.) ou pour démarrer un PC à partir d'une carte réseau.

---

#### NFS [UDP <= NFSv3 / `TCP` ou autres >= NFSv4]

`NFS` (Network File System) est un protocole qui permet à un ordinateur d'accéder via un réseau à des fichiers distants en montant localement sur un client le système de fichiers distants du serveur.

`NFS` utilise le protocole `RPC` et fonctionne principalement entre systèmes UNIX mais des versions existent pour Mac et Windows.

---

Les dernières versions de `NFS` proposent des opérations puissantes de gestion de système de fichiers distants : chiffrement des communications, délégation (fichier géré en local), migration et réplication du serveur, reprise sur incidents.

---

#### SMB [TCP 445 / NetBIOS 139]

Le protocole `SMB` (Server Message Block), autrefois `CIFS`, est un protocole permettant le partage de ressources (fichiers et imprimantes) sous Windows. Une implémentation libre `Samba` existe pour la plupart des OS.

`SMB` fonctionne via une structure de client/serveur, le client va envoyer des requêtes spécifiques et le serveur de fichiers va y répondre. Le protocole est optimisé pour une utilisation dans un réseau local, mais il peut aussi être utilisé sur Internet.

---

Les ressources partagées sont accessibles à partir d'une adresse utilisant la convention `UNC` de type : 

```
\\serveur\partage\chemin\nom_fichier
```

---

### Gestion d'utilisateurs distants

---

#### NIS

`NIS` (Network Information Service), ou `Yellow Pages` est un protocole client serveur permettant la centralisation d'informations sur un réseau UNIX.

Un serveur `NIS` stocke et distribue les informations administratives du réseau, qui se comporte ainsi comme un ensemble cohérent de comptes utilisateurs (`/etc/passwd`), groupes, machines (fichiers de noms d'hôte `/etc/hosts`), ...

---

Le client récupère les informations en interrogeant le serveur à partir d'appels `RPC` grâce à des commandes d'administration dédiées : `yppasswd,ypwhich,...`

`NIS` est réputé pour être faible en matière de sécurité.
`NIS+` une réécriture complète de `NIS`, également plus sécurisée mais on lui préfère de plus en plus `ldap` ou `kerberos`.

---

### Le courrier électronique

---

#### POP(S) [TCP 110 / S:995]

Le protocole `POP3` (Post Office Protocol), permet de récupérer les mails situés sur un serveur de messagerie électronique.

Le fonctionnement de `POP` est simple : le client se connecte au serveur de messagerie, s'authentifie, récupère le courrier, efface le courrier sur le serveur (optionnel), et se déconnecte.

---

Toute opération supplémentaire est donc réalisée directement sur le client. Pour cette raison, on lui préfère de plus en plus `IMAP` qui permet des opérations complexes directement sur le serveur.

`POP3` est encore disponible sur presque tous les serveurs de messagerie électronique en mode SaaS.

L'envoi de mails se fait en général en utilisant `SMTP`.

---

#### IMAP(S) [TCP 143 / S:993]

`IMAP` (Internet Message Access Protocol), est un protocole qui permet d'accéder à ses courriers électroniques directement sur les serveurs de messagerie.

Les messages étant gérés directement sur le serveur, le multi-client est grandement facilité.

`IMAP` fournit des opérations avancées directement sur le serveur : création de dossiers, tri des emails, ...

---

`IMAP` est aujourd'hui presque toujours disponible sur les serveurs de messagerie électronique en mode SaaS.

L'envoi de mails se fait en général en utilisant `SMTP`.

---

#### SMTP(S) [TCP 25 / implicite:465  / explicite:587]

`SMTP` (Simple Mail Transfer Protocol) est un protocole de communication utilisé pour envoyer un courrier électronique d'un client vers les serveurs de messagerie électronique.

Le protocole assez simple : on commence par spécifier l'expéditeur du message, puis le ou les destinataires d'un message, puis, en général après avoir vérifié leur existence, le corps du message est transféré.

`SMTP` est le protocole ultra majoritaire dans l'envoi de courriers électroniques.

---

#### Webmail

Une messagerie Web (Webmail) est une interface web rendant possible l’émission, la consultation et la manipulation de courriers électroniques directement sur le Web depuis un navigateur.

C'est en fait un client de messagerie qui s'exécute dans un serveur Web.
Le serveur Web effectue alors les requêtes locales ou distantes vers le serveur de messagerie.

---

L'avantage principal d'un Webmail est d'éviter la configuration du client de messagerie et l'ouverture de ports dédiés sur le client.
Cependant, les courriers électroniques ne sont alors plus accessibles en local.

---

### Un annuaire fédérateur

---

#### LDAP(S) [TCP 389 / S:636]

`LDAP` (Lightweight Directory Access Protocol) est une norme pour les systèmes d'annuaires, incluant un modèle de données, un modèle de nommage, un protocole, un modèle de sécurité et un modèle de réplication.

`ldaps` : `ldap` + tunnel `ssl/tls`

---

Le nommage des éléments constituant l'arbre `LDAP` reflète souvent le modèle politique, géographique ou d'organisation de la structure représentée :

- `DNS` pour racine et premières branches (domain components ou `dc=…`)
- pour les branches plus profondes : groupes (organizational units ou `ou=…`) ou personnes (common name ou `cn=…` voir user identifier `uid=…`)

---

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

---

### L'administration de réseaux

---

#### SNMP [UDP 161 / 162]

`SNMP` (Simple Network Management Protocol) est un protocole de communication qui permet de gérer les équipements du réseau, de superviser et de diagnostiquer des problèmes réseaux et matériels à distance : commutateurs, concentrateurs, routeurs, postes de travail, serveurs physiques ou virtuels, ...

`SNMP` est composé de trois types de composants : des `NMS` (network management systems) pour exécuter les requêtes de gestion, des nœuds (équipement géré) et des agents (transmettent les messages `SNMP` entre les nœuds et les `NMS`).

---

Les objets `SNMP` contenus dans les nœuds peuvent être des informations matérielles, des paramètres de configuration, des statistiques de performance et autres objets qui sont directement liés au comportement en cours de l'équipement en question.

`SNMP` est très utilisé et de nombreux outils l'intègrent pour effectuer de la surveillance et maintenance applicative et matérielle : `Zabix`, `Nagios`, ...

---
layout: section
---

## Ressources

- [Programmation de sockets][developpez-sockets]
- [Synchronisation de processus - cours sur les moniteurs (_Samia Bouzefrane, CNAM_)][cours-moniteurs]

[developpez-sockets]: https://laissus.developpez.com/tutoriels/cours-introduction-tcp-ip/?page=page_13
[cours-moniteurs]: http://deptinfo.cnam.fr/new/spip.php?pdoc4762

---

