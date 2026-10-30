---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Les modes de communication entre processus
tags:
- architecture
- client-server
type: cours
sidebar:
  order: 3
---

## Communication entre processus : `IPC`

Dans un système d'exploitation moderne :

- les processus fonctionnent en concurrence
- les processus ont besoin de communiquer entre eux

_Comment gérer ces échanges ?_

Les mécanismes de communication inter-processus peuvent être classés en trois catégories :

- l'échange de données entre les processus ;
- la synchronisation entre les processus (notamment pour gérer le principe de section critique) ;
- l'échange de données et la synchronisation entre les processus.

## Echange de données

Les données peuvent être échangées :

- par lecture/écriture concurrente de fichiers (localement ou à distance : `NFS`)
- par espace mémoire des processus partagé : processus léger `thread`
- par partage de segments de mémoire dédiés sans partager l'espace mémoire des processus : processus lourd `process`

Problème des sections critiques : **non concurrence des modifications** ! (incohérence, inter-blocage, ...)

## Synchronisation

Permet de résoudre les problèmes de sections critiques en bloquant / débloquant les accès :

- _verrous_ pour bloquer tout ou partie d'un fichier : lecture / écriture / les deux
- _sémaphores_ pour gérer des sections critiques : compteur et fonctions `P` (décrémente et blocage si compteur == 0), `V` (incrémente et débloque un des processus bloqués)
- _signaux_ : processus en attente d'un signal (`SIGSEGV`, …) pour se débloquer

Usage difficile : risques d'inter-blocage.

Utiliser des algorithmes éprouvés :

- _exclusion mutuelle_ - 1 processus à la fois : carte bancaire
- _cohorte_ - N processus à la fois : parking de 500 places
- _rendez-vous_ - ressource accessible après l'attente de plusieurs processus : processus devant échanger des informations entre les étapes de l'algorithme.
- _producteurs–consommateurs_ - ressource accessible après la fin d'un autre processus : réception de données puis traitement
- _lecteurs–rédacteurs_ - une seule catégorie de processus à la fois : fichier accessible à tous en lecture si pas de modification

### Échange de données et synchronisation

Meilleur des deux mondes, plus simples à utiliser (mais coûteux).

- Les processus envoient des informations dans une file
- Les informations sont récupérées dans cette même file au besoin : `message queue` (Unix), `socket` Unix ou `TCP/IP`, `pipes`, `message passing`

Les opérations d'écriture et de lecture dans la file sont **bloquantes** et permettent donc la synchronisation.

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

## Les socket `TCP/IP`

Une socket est un flux de communication entre deux objets `Client` et `Serveur`.

Le Client va demander un droit de créer un canal de communication avec le Serveur, puis, si celui ci accepte, le Client et le Serveur pourront communiquer.

La socket permet une communication logique entre des systèmes reliés au réseau internet (ou en local) en s'abstrayant des spécificités de ces systèmes.

C'est le protocole de base pour échanger sur un réseau, les sockets sont omniprésentes utilisées directement ou depuis d'autres protocoles.

Il existe 2 types de socket :

- le mode connecté (`TCP`) établit une connexion durable entre les deux processus : l'adresse de destination n'est pas nécessaire à chaque envoi de données
- le mode non connecté (`UDP`) : nécessite l'adresse de destination à chaque envoi et aucun accusé de réception n'est donné.

Les socket se situent entre la couche réseau (incluse) et les couches applicatives du modèle OSI (protocoles `UDP` ou `TCP` utilisant `IP` / `ARP`).

En `C++`, `C#`, `Java`, `Python`, etc… les fonctions sont quasiment identiques :

- Créer un objet `Socket`
- Le paramétrer (`TCP`, Internet, etc… et le `Host`, le port)
- Lancer la demande pour le client ou se mettre en `Listen` pour le serveur
- Fermer et détruire les Socket

Le mode `Listen` est le mode du Serveur qui consiste à attendre une demande de connexion d'un Client. Celle ci est souvent bloquante bien que certaines alternatives existent (`CallBack`, ...).

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

## Les serveurs multi-protocoles

Un serveur peut fournir le même service sur plusieurs protocoles.

Exemple : service `DAYTIME` sur `13/TCP` et `13/UDP` (2 socket distinctes).

Permet de ne pas rationaliser les ressources du code métier : un seul déploiement pour le même service.

## Les serveurs multi-services

Un serveur peut fournir plusieurs services sur des socket séparées.

- limite les ressources nécessaires :  nombre de processus, ...
- possibilité de désactiver un service
- un programme différent est exécuté par service demandé

Par exemple : serveur mail `POP` + `IMAP`

## Les appels de procédures distantes : `RPC`

`RPC` (remote procedure call) est un protocole réseau permettant de faire des appels de procédures sur un ordinateur distant à l'aide d'un serveur d'applications.

- Un `RPC` est initié par le client qui envoie un message de requête à un serveur distant connu pour exécuter une procédure spécifique avec des paramètres spécifiques
- Le client est bloqué en attente
- Le serveur répond puis l'application continue son déroulement

`RPC` utilise des `stubs` pour simuler dans le code un appel local aux fonctions du serveur chez le client, ou du client chez le serveur. Ces stubs servent d'interfaces pour la procédure.

De nombreuses applications utilisent `(Secure)RPC` : `NFS`, `NIS`, ...

Il existe beaucoup d'implémentations (incompatibles) de `RPC`.
