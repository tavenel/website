---
title: TP - Utilisation du protocole HTTP avec Telnet
date: 2023 / 2024
---

## Installation de telnet

Suivre les étapes décrites à l'adresse : https://rdr-it.com/windows-10-installation-du-client-telnet/ 

## Utilisation de telnet pour récupérer le contenu d'une page

Pour se connecter à un serveur distant, on utilise l'instruction suivante (remplacer `SERVEUR` et `PORT` par l'adresse du serveur et le port de connexion.

```
telnet SERVEUR PORT
```

Une fois connecté au serveur, on peut envoyer directement des requêtes `HTTP` au serveur.

::: exo
Utiliser `telnet` pour récupérer la page de résultats d'une recherche sur votre moteur de recherche préféré. On pourra récupérer l'URL correspondant à la recherche dans un navigateur.

Vérifier que la page contenant les résultats de la recherche est bien renvoyée par le serveur.
:::

## Utilisation de `telnet` pour effectuer une requête PUT

`telnet` permet d'effectuer toute requête `HTTP` sur le serveur : nous allons l'utiliser pour simuler une requête de type `PUT` sur la page <httpbin.org/put> pour ajouter un nouvel objet sur ce serveur.

Pour cela, nous allons demander à communiquer en version 1.1 du protocole et nous spécifions quelques headers pour recevoir une réponse en `Json`.

Attention à bien modifier le champ `URL` par l'URL de la page sur le serveur.

La requête est envoyée après l'envoi d'une ligne vide à `telnet` en fin d'instructions.

```
telnet httpbin.org 80
PUT URL HTTP/1.1
Host: httpbin.org
accept: application/json

```

_Vérifier que le serveur renvoie bien un code de retour de succès (HTTP 2xx)._

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
