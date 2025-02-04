---
title: TP - Envoi de mail en utilisant le protocole SMTP
date: 2023 / 2024
---

## Introduction

`SMTP` a été conçu pour être utilisable directement depuis une interface texte (`telnet`, ...), le protocole est donc optimisé pour être utilisé directement par un humain (et non optimisé pour une machine).

Comme de nombreux fournisseurs de courrier électronique, `Outlook` ne supporte plus `SMTP`, nous allons utiliser sa version sécurisée `SMTPS` (`SMTP` à travers un canal `TLS`)

## Récupération du nom de domaine ou de l'adresse IP du serveur de mails

La norme `DNS` prévoit un enregistrement de type `MX` pour paramétrer un serveur de courriers électroniques.
En l'absence d'enregistrement `MX`, l'enregistrement `A` (enregistrement principal) être utilisé.

Utiliser un client `DNS` pour obtenir l'adresse du serveur de courriers électroniques (enregistrement `MX`) associé à votre adresse mail `Outlook`.

Par exemple :

```
$ nslookup
set type=mx
gmail.com
```

:::tip
La configuration `DNS` reçue est assez complexe : dans la suite du TP, on utilisera le serveur `SMTP` principal `smtp.office365.com:587`
:::


## Ouverture d'un tunnel `TLS`

Pour utiliser `SMTP`, nous pouvons utiliser une interface texte simple tel `telnet`.
Cependant `Outlook` ne supporte que des connexions sécurisées, ce que `telnet` ne supporte pas.

Pour contourner ce problème, nous allons utiliser `SMTPS`, qui est l'usage du protocole `SMTP` standard à travers un tunnel `TLS`. Le tunnel sera ouvert grâce au programme `openssl`.

1. Installer `openssl` : https://wiki.openssl.org/index.php/Binaries 
2. Ouvrir une connexion `TLS` vers le serveur `Outlook` (remplacer `MAIL_SERVEUR` et `PORT` par l'adresse du serveur de mail, et le port `SMTPS`)
3. Vérifier que la connexion est bien établie : le serveur doit répondre `220` ou `250`.

Commande `openssl` pour créer une connexion `SMTPS` :

Sur Windows :

```batch
openssl s_client -starttls smtp -connect MAIL_SERVEUR:PORT
```

Sur Linux (l'option `crlf` permet de transformer les fins de ligne en `CR+LF` lisibles par le serveur) :

```sh
openssl s_client -starttls smtp -connect MAIL_SERVEUR:PORT -crlf
```

## Envoi d'un mail par `SMTP`

Le protocole `SMTP` peut alors être utilisé pour envoyer un mail.

Le protocole `SMTP` est un protocole de dialogue entre le client et le serveur :

### Initiation du protocole

Le protocole est initié par une requête `Extended Hello` :

```
EHLO reseau-cd.net
```

Le serveur répond avec un `250 Hello`.

### Authentification

La deuxième étape est l'identification sur le serveur.

Pour des raisons historiques, `SMTP` requiert un encodage `Base64` : le nom d'utilisateur et le mot de passe doivent donc être passés dans cet encodage.

On peut par exemple utiliser l'utilitaire `base64` :

```
echo MA_CHAINE | base64
```

:::warn
Attention : `Base64` n'est pas un algorithme de chiffrement, uniquement un type d'encodage ! `SMTP` est non sécurisé, l'authentification n'est donc pas chiffrée par le protocole. Cependant, toute la communication est encapsulée dans un tunnel `TLS`, ce qui assure la sécurité des échanges.
:::

Demande d'authentification de type `LOGIN` (username / password) :

```
AUTH LOGIN
```

Le serveur répond `Username` en `Base64` :

```
334 VXNlcm5hbWU6
```

Entrez votre username (adresse mail complète) en `Base64`, par exemple pour `mail@test.com` : `bWFpbEB0ZXN0LmNvbQ==`

Le serveur répond `Password` en `Base64` :

```
334 UGFzc3dvcmQ6
```

Entrez votre mot de passe en `Base64`.

Le serveur répond :

```
235 2.7.0 Authentication successful
```

### Demande d'envoi de mail

Nous allons maintenant pouvoir demander à envoyer un mail :

```
MAIL FROM: adresse@expediteur.com
rcpt to: adresse@destinataire.com
```

Attention, `rcpt to` doit être en minuscule sous `openssl` !

:::warn
Même une fois authentifié, il est nécessaire de fournir une adresse d'émetteur. En effet, l'émetteur peut avoir plusieurs adresses mails ou des alias. Le protocole `SMTP` permet d'entrer n'importe quelle valeur dans ce champ, ce qui pose un gros problème d'usurpation d'identité ! Pour limiter le spam, la plupart des fournisseurs de mails vérifient que ce champ correspond à une adresse autorisée par l'utilisateur authentifié. Cela n'est pas une garantie : le protocole mail est donc par essence **non sûr** (on pourra résoudre ce problème en ajoutant des certificats dans les messages : `GPG`, ...)
:::

### Écriture de l'enveloppe du mail

La dernière étape correspond à l'écriture de l'enveloppe du mail (c'est-à-dire aux informations affichées par le client de messagerie).

La dernière ligne doit être un caractère point `.` seul, ce qui permet de finir le corps du message et d'envoyer le mail.

```
DATA
From: adresse@expediteur.com
To: adresse@destinataire.com
Subject: un mail depuis SMTP

Ceci est un message envoyé directement depuis SMTP

.
```

:::tip
Pourquoi un champ `To:` alors qu'une requête `rcpt to:` a déjà été envoyée ? Le champ `To:` correspond à une information stockée dans l'enveloppe du mail et accessible au destinataire à sa lecture, alors que la requête `rcpt to:` décrit à qui réellement envoyer le message. Cela permet l'utilisation de _blind copies_ `bcc` : le destinataire ne saura pas que le message a également été transmis à d'autres destinataires.
:::


## Exercice attendu :

:::exo
1. Envoyer un ou plusieurs mails de test à sa propre adresse mail. On pourra tester l'usage (et l'absence) des différents champs dans l'enveloppe du mail : `From:`, `To:`, ...
2. Envoyer un mail depuis votre adresse en utilisant `SMTP` vers l'adresse du formateur. Le sujet du mail devra être : _tp-smtp-nom-prénom_
:::

# Legal

- © 2025 Tom Avenel under CC  BY-SA 4.0
