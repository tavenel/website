---
title: Notions de protocoles Web
date: 2023 / 2024
keywords:
- cloud
correction: false
---

# TD1. Notions de protocoles Web

## QCM

1. Parmi ces logiciels, lequel/lesquels sont des logiciels clients du web ?
   1. PhotoShop
   1. Excel
   1. **Firefox**
   1. Word
   1. Google Docs
   1. **Google Chrome**

1. http://www.google.fr est :
   1. une adresse e-mail
   1. **une adresse web**
   1. une adresse ftp
   1. une adresse news

1. Quel protocole est dit sécurisé parmi les suivants ?
   1. POP
   1. **SSL**
   1. Telnet

1. Le web est un système hypermédia, fonctionnant en mode client/serveur sur Internet, le mode client permet :
   1. de répondre à la requête du serveur
   1. de payer le service du serveur
   1. d'expédier les fichiers correspondant à une page
   1. **d'émettre une requête vers le serveur**


1. Le nombre binaire 1001 vaut en héxadécimal :
   1. F3
   1. **9**
   1. 1A
   1. F4

## Daemon HTTP

Un daemon est un programme qui se lance au démarrage de la machine et reste opérationnel pendant tout le temps d’exécution de celle-ci.

Sur mon serveur il y a un daemon HTTP. Expliquez.

:::correction
Il s’agit d’un programme tournant en permanence et attendant des requêtes HTTP pour y répondre : c’est donc un serveur Web.
:::

## Protocoles de transport

1. Parmi les protocoles de transport, lequel utiliseriez-vous pour un système de visioconférence ?
:::correction
  + UDP, car les données sont volumineuses et la rapidité de transfert est la priorité (devant l’intégrité des données)
:::
1. Parmi les protocoles de transport, lequel utiliseriez-vous pour qu'une application accepte les cartes de crédit sur le réseau et pour garantir l'arrivée des données ?
:::correction
  + TCP, car il faut absolument garantir l’intégrité des données
:::
1. Parmi les protocoles de transport, lequel utiliseriez-vous pour échanger des nombreux fichiers volumineux et garantir l’arrivée des données ?
:::correction
  + TCP, car il faut encore garantir l’intégrité des données, même si elles sont coûteuses à transporter
:::

## Unicité des adresses IP

1. Deux machines de réseaux IPv4 différents peuvent-elles posséder la même adresse IPv4 ?
:::correction
  + Non, car le NetID est différent
:::correction
1. Dans le même réseau IPv4 deux machines différentes peuvent-elles posséder la même adresse IPv4 au même moment ?
:::correction
  + Non, une adresse IP identifie un hôte de manière unique à un instant donné
:::correction
1. Dans le même réseau IPv4 deux machines différentes peuvent-elles posséder la même adresse IPv4 à deux moments différents ?
:::correction
  + Oui, une adresse IP identifie un hôte de manière unique mais seulement à un instant donné. Ce n’est toutefois pas recommandé, mais souvent nécessaire pour recycler des adresses (par exemple, le Cloud utilise beaucoup de machines temporaires, dont la consommation d’adresses IP serait compliquée sans recyclage de celles-ci)
:::


*L’adresse du réseau local est une adresse cachée par le routeur, ce qui fait que toutes les machines de ce réseau sont cachées derrière le routeur et par la suite invisible sur Internet. Le routeur a donc deux adresses IP, l’une du côté du réseau local (donc même adresse du réseau) et l’autre du côté du réseau internet lui permettant d’être visible à l’extérieur.*

1. Dans ce cas, deux machines de deux réseaux différents connectés tous les deux à Internet peuvent-elles avoir la même adresse ?
:::correction
Oui, car cette adresse est masquée sur l’interconnexion des réseaux : une adresse IP est unique seulement dans son propre réseau (par exemple, les réseaux domestiques utilisent souvent les mêmes plages d’IP 192.168.0.1, 192.168.0.2, …)
:::

# TD2. Gestion de réseaux et sécurité

## Plan d’adressage

Dessinez un réseau local composée d’une box Internet, 3 PC, un téléphone IP, un serveur Web et un serveur d’impression. Ce réseau local est connecté à Internet depuis la box Internet. Supposons que l’adresse du réseau local est 192.168.10, affectez des adresses IP aux différents périphériques.

![](td-schema.png)

## Communications sécurisées avec HTTPS

Le protocole HTTPS (HTTP sur SSL/TLS) est couramment utilisé pour sécuriser les communications entre un serveur Web et un navigateur. Pour cela, une session HTTPS s'appuie sur un certificat diffusé par le serveur permettant d'effectuer une session d'authentification initiale et ensuite un chiffrement du canal de communication dans lequel transite l'échange HTTP.

1. Lors de l'authentification, le protocole utilise une clef publique contenue dans un certificat que le serveur détient et diffuse au client à l'établissement de la connexion. Quelles sont les protections offertes par cette utilisation d'un certificat serveur ?

:::correction
Le protocole SSL avec un certificat serveur offre d'abord une authentification du partenaire accédé par une vérification que ce serveur détient bien la clef privée correspondant à la clef publique diffusée. Ensuite, la communication est chiffrée, on a donc des garanties sur la confidentialité des échanges ainsi que sur l'intégrité de la communication pendant toute sa durée.
:::

1. Comment   l'utilisateur   du   navigateur   peut-il   être   assuré   que   cette   clef   publique correspond bien à l'organisme auquel il souhaite accéder ? 

:::correction
Le certificat n'inclut pas seulement la clef publique, mais également une signature de cette   clef   publique   par   un   autre   certificat.   (Celui-ci   pouvant   également   être   un certificat   intermédiaire.)   La   racine   de   cette   chaîne   de   certification   doit   être   un certificat pré­installé sur le navigateur (ou obtenu indépendamment en préalable à la communication).   L'utilisateur   peut   alors   être   sûr   que   le   certificat   diffusé   par   le serveur appartient bien à l'organisme indiqué s'il vérifie la chaine de certification, s'il a confiance dans le certificat racine et s'il a confiance dans les organismes détenteurs des certificats intermédiaires pour avoir fait les vérifications nécessaires avant de signer les certificats dérivés. (Il s'agit alors de tiers de confiance ou d'autorités de certification.)
:::

1. Pourquoi de nombreux services Web, utilisant pourtant HTTPS, demandent-ils en plus à   l'utilisateur   de   fournir   un   nom   de   compte   et   un   mot   de   passe   pour   compléter l'ouverture de session 

:::correction
Le certificat serveur n'offre qu'une authentification du serveur. Si le service accédé gère   une   base   de   comptes   utilisateurs,  ceux-ci   doivent   donc   également   en   plus s'authentifier. Cette authentification du client peut éventuellement s'effectuer via un nom d'utilisateur et un mot de passe. Cette méthode est moins forte qu'une technique faisant appel à des algorithmes de cryptographie asymétriques, mais elle est bénéficie néanmoins via HTTPS de la protection offerte par le canal chiffré et signé de SSL.
:::

1. Il est possible d'utiliser un certificat client stocké sur le navigateur pour l'échange HTTPS. Quel   est   l'effet   de   l'utilisation   d'un   certificat   client   sur   la   protection   de l'ensemble du service (avantages / inconvénients) ?

:::correction
Dans   ce   cas,   l'authentification   du   client,   appuyée   sur   un   certificat   et   une authentification à clef privée/clef publique offre des garanties bien plus importantes en terme de sécurité. Par contre, il faut alors gérer une procédure de délivrance de ces   certificats   clients   (incluant   leur   signature   par   un   tiers   de   confiance,   après vérification de l'identité du demandeur par exemple).
:::

## Masque de sous-réseau 

Une entreprise à succursale multiple utilise l’adresse d’un réseau identifié par l’IP 196.179.110.0. Pour une gestion plus fine de ses sous-réseaux, le responsable informatique désire pouvoir affecter une adresse IP propre à chacune des 10 succursales. 

Attention : La valeur 0 n’est jamais utilisée comme Host ID pour des raisons de compatibilité.

1. Donner et expliquez la valeur du plus petit masque possible pour le réseau principal (196.179.110.0) correspondant à ce besoin ?
:::correction
  + Comme on doit pouvoir adresser 10 machines, il faut donc 10 adresses IP dérivées de l’adresse initiale. La valeur décimale 10 se code par 1010 en binaire, il faut donc disposer de 4 bits au moins pour pouvoir identifier 10 entités en écriture binaire. La part du HostID dans le masque de sous-réseau sera donc de 4 bits (et donc celle du network ID : 32 – 4 = 28 bits).
  + Le masque de sous-réseau à construire est donc : 28 bits à 1 pour le NetID suivis de 4 bits à 0 pour le HostID, soit : 11111111.11111111.11111111.11110000 soit encore en décimal : 255.255.255.240
:::

1. En utilisant ce masque de réseau, le réseau pourra-t-il supporter des machines en plus des 10 déjà allouées ? Si oui, combien et pourquoi ?
:::correction
  + Compte tenu des bits affectés à l’identification de la machine dans le réseau (HostID), on utilise 4 bits pour identifier les machines. 4 bits permettent d’identifier 16 entités (2^4), mais la valeur 0 représente le réseau lui-même et la valeur tout à 1 représente l’adresse de broadcast : le réseau pourra donc identifier jusqu’à 14 machines. Il reste donc 4 adresses supplémentaires de libres sur le réseau.
:::

1. Quelle est l’adresse de broadcast (ou adresse de diffusion) du réseau ?
:::correction
  + L’adresse de broadcast correspond à tous les bits du champ Host\_ID à 1.
  + Le HostID est ici codé sur 4 bits, on peut donc considérer uniquement le dernier octet (8 bits).
  + Le dernier octet de l’adresse du réseau vaut 0 (196.179.110.0), donc en binaire : 0000 0000 (4 derniers bits du Network ID suivis de 4 bits du Host ID).
  + Le dernier octet de l’adresse de broadcast vaut donc (en mettant le Host\_ID à 1) : 0000 1111
  + Ce qui correspond en décimal à 15, soit l’adresse de diffusion : 196.179.110.15
:::


## Segmentation de réseau TCP/IP

Une entreprise utilise pour ses sites Web la plage d’adresse 10.0.0.0 de la classe A (le NetID est exprimé uniquement et entièrement sur le 1er octet de l’adresse). Considérons quatre serveurs de cette entreprise dont les noms et adresses sont donnés ci- dessous :

|*Nom (DNS)*|*Adresse IP (adresse logique)*|*Adresse MAC (adresse physique)*|
| :- | :- | :- |
|Site1.Entreprise.com|10.99.43.27|00-90-27-55-74-35|
|Site2.Entreprise.com|10.163.12.254|00-90-27-55-74-36|
|Site3.Entreprise.com|10.189.12.27|00-90-27-55-74-38|
|Site4.Entreprise.com|10.126.43.254|00-90-27-55-74-37|

1. Quel est le NetID de ce plan d’adressage ?
:::correction
  + En classe A le NetID est exprimé sur 1 octet, soit 10 (en décimal) pour le premier octet (ou 00001010 en binaire)
:::

1. On souhaite réaliser deux sous-réseaux (SubNetID) tels que Site1 et Site4 appartiennent au même sous réseaux et que Site2 et Site3 appartiennent à un autre sous-réseau.
  - Quel est le nombre de bit nécessaires pour réaliser ces deux sous-réseaux ?
  - Les bits du NetID et du SubNetID doivent être contigus (par exemple les sous-réseaux 192.168.1.0 et 192.168.2.0 sont deux sous-réseaux du réseau 192.168.0.0). Pour répondre à cette question, on cherchera donc le nombre de premiers bits nécessaires et suffisants après le Net ID pour segmenter le réseau en deux sous-réseaux distincts.

:::correction
Pour distinguer le nombre de bits nécessaires il suffit d’examiner la valeur binaire du 1er octet du Host\_ID, si cela est insuffisant du second... jusqu’à trouver la combinaison binaire qui réponde au problème posé.*

|Nom (DNS)|Octet 1 du HostID (décimal)|Octet 1 du HostID (binaire)|
| :- | :- | :- |
|Site1.Entreprise.com|227|11    100011|
|Site2.Entreprise.com|163|10    100011|
|Site3.Entreprise.com|189|10    111101|
|Site4.Entreprise.com|126|01    111110|

L’examen du tableau ci-dessus montre que seuls deux bits du 1er octet du HostID sont nécessaires pour distinguer dans le plan d’adressage donné les 2 sous-réseaux (réseau 1 : 11 ou 0X, réseau 2 : 10).
:::

1. Donnez le masque correspondant aux deux sous-réseaux.
:::correction
  + Le masque de sous réseau correspondant est :
  + NetID (1er octet de l’adresse) : 11111111  +  SubnetID : 11000000 00000000 00000000 00000000*
  + Soit en décimal : 255.192.0.0
:::

1. On souhaite isoler chaque machine dans un sous-réseau distinct.
   1. Quel est le nombre de bits minimum et nécessaire pour qu’aucune des machines n’appartiennent au même sous réseau ?

:::correction
|Nom (DNS)|Octet 1 du HostID (décimal)|Octet 1 du HostID (binaire)|
| :- | :- | :- |
|Site1.Entreprise.com|227|1110  0011|
|Site2.Entreprise.com|163|1010  0011|
|Site3.Entreprise.com|189|1011  1101|
|Site4.Entreprise.com|126|0111  1110|

L’examen du tableau ci-dessus montre que la plus petite combinaison binaire pour distinguer 4 sous-réseaux distincts dans les adresses données est de 4 (réseau 4 : 0XXX, réseau 1 : 11XX, réseau 2 : 1010, réseau 3 : 1011).
:::

1. Donnez le masque correspondant.
:::correction
  - Le masque de sous-réseau est alors : 
  - NetID (1er octet de l’adresse) : 11111111  +  SubnetID : 11110000 00000000 00000000 00000000
  - Soit en décimal : 255.240.0.0
:::


## Calculs d'adresses IP

1. Quelle est l’adresse machine (HostID) et l’adresse réseau (NetID) associée ?
  - Adresse IP : 113.47.91.75
  - Masque réseau : 255.0.0.0
:::correction
  - HostID = 0.47.91.75 et  NetID = 113.0.0.0
:::


1. Quelle est l’adresse IP associée ?
  - adresse réseau : 195.183.34.0
  - adresse machine : 0.0.0.27
  - masque réseau : 255.255.255.0
:::correction
  - Réponse : Adresse IP : 195.183.34.27
:::

1. Quel est le masque réseau pour l’adresse IP et l’adresse machine suivante ??
  - adresse IP : 99.47.91.75
  - adresse réseau : 99.0.0.0
  - adresse machine : 0.47.91.75
:::correction
  - Réponse : masque réseau : 255.0.0.0
:::

1. Quelles sont la première et dernière adresse IP disponibles sur le réseau 192.168.10.0/20 ?
  - La notation xxxx/20 représente un masque avec les 20 bits de gauche à 1.

:::correction
Le NetID étant codé sur les 20 bits de gauche, le HostID est codé sur les 32-20=12 bits restants de droite.
Rappel : les adresses où tous les bits du HostID sont à 0 et tous à 1 sont réservées.
Les identifiants des machines vont donc de : HostID = 0000 00000001 à HostID = 1111 11111110
Dans notre cas : les deux premiers octets (192.168) sont donc réservés au réseau.
Le dernier octet est réservé au HostID.
Le troisième octet est partagé : les 4 premiers bits appartiennent au réseau, les 4 suivants au HostID. Le 3e octet de l’adresse IP 192.168.10.0 vaut 10 en décimal, soit 0000 1010 en binaire. Les 4 premiers bits correspondent à la partie réseau, soit 0000.
Le troisième octet de la première adresse IP est donc : 0000 0000 = 0 et le troisième octet de la dernière adresse IP est : 0000 1111 = 15
La première adresse IP du réseau est donc : 192.168.0.1
La dernière adresse IP du réseau est donc : 192.168.15.254

http://jodies.de/ipcalc?host=192.168.10.0&mask1=20
:::


Proposer une structuration du réseau 147.56.0.0 (masque de réseau : 255.255.0.0) en 5 sous-réseaux. Donner les masques de chaque sous-réseau et donner l’adresse IP d’une machine de chaque sous-réseau.

:::correction
Réponse : Pour diviser en 5 sous-réseaux, il faut utiliser 3 bits de l’adresse machine. (2^2=4<5 et 2^3=8>=5).

Le masque du réseau est 255.255.0.0 : on utilisera donc les 3 premiers bits sur le 3ieme octet. Le 3e octet du masque vaut donc : 11100000 (3 bits pour le réseau, le reste pour l’identifiant de la machine), soit 224 en décimal.

La nouvelle valeur du masque est : 255.255.224.0

Maintenant on utilise un codage pour les 5 sr, en fonction du codage choisit on déterminera les plages d’adresse IP pour chaque sous-réseau

- SR 1 : 000 => 147.56.0.1 – 147.56.31.254
- SR 2 : 001 => 147.56.32.1 – 147.56.63.254
- SR 3 : 010 => 147.56.64.1 – 147.56.95.254
- SR 4 : 011 => 147.56.96.1 – 147.56.127.254
- SR 5 : 100 => 147.56.128.1 – 147.56.159.254
:::

