---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: iSCSI
type: cours
sidebar:
  order: 4
description: iSCSI
---
## 🧠 Comprendre iSCSI

**iSCSI** (Internet Small Computer Systems Interface) est un protocole permettant d'envoyer des commandes **SCSI** sur un réseau **TCP/IP**.  
Il permet de connecter un **client (Initiator)** à un **serveur de stockage (Target)** à travers le réseau comme si le disque distant était local.

## Concepts fondamentaux

| Élément | Description |
|----------|--------------|
| **Initiator** | Machine cliente qui accède au stockage distant. |
| **Target** | Serveur qui héberge les volumes partagés (LUNs). |
| **LUN (Logical Unit Number)** | Unité logique de stockage exposée par la target. |
| **Session iSCSI** | Connexion entre l'initiator et la target via TCP (port 3260). |

## Fonctionnement

1. L'administrateur configure un disque ou une partition sur le **serveur target**.  
2. Le **target** publie un service iSCSI et expose un ou plusieurs **LUNs**.  
3. Le **client initiator** découvre les targets disponibles sur le réseau.  
4. Il se connecte à la target et monte le volume distant comme un disque local.  

---

## Avantages et inconvénients

**Avantages :**
- Utilise l'infrastructure réseau existante (TCP/IP).
- Solution économique comparée à la fibre optique (Fibre Channel).
- Compatible avec de nombreux OS.

**Inconvénients :**
- Dépend des performances du réseau.
- Peut introduire de la latence.
- Nécessite une gestion soignée de la sécurité (authentification CHAP, isolation VLAN).

---

