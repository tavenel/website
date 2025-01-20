---
title: TP Mise en place de règles de filtrage sous Debian avec Netfilter
author: Tom Avenel
date: 2024 / 2025
correction: false
---

## Contexte

Vous êtes administrateur système pour une petite entreprise. L'équipe réseau vous demande de sécuriser un serveur Debian en configurant un pare-feu pour :

1. Autoriser uniquement les connexions SSH provenant du réseau local.
2. Bloquer tout autre trafic entrant sauf les réponses aux requêtes sortantes légitimes.
3. Permettre l'accès HTTP/HTTPS (ports 80 et 443) uniquement depuis une plage IP spécifique.
4. Enregistrer dans les logs système les connexions bloquées.

La configuration du pare-feu devra être persistante (et donc ne pas être effacée par un redémarrage).

Vous devez également automatiser cette configuration à l’aide d’un script shell et permettre à un utilisateur **non privilégié** d'exécuter ce script.

Utilisez des outils comme `ping`, `curl`, ou `nmap` depuis différentes sources pour vérifier le comportement du pare-feu.

## Livrables attendus

1. Un fichier `firewall.sh` opérationnel.
2. Une capture d'écran ou un rapport des tests réseau réalisés.
3. Une explication des choix liés aux droits du fichier `firewall.sh`.

