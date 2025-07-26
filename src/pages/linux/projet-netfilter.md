---
title: TP Mise en place de règles de filtrage sous Debian avec Netfilter
date: 2024 / 2025
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

La syntaxe principale d'une commande `iptables` est la suivante :

```sh
iptables -A chaîne \
	-i interface_source (ou -o interface_destination) \
	-p protocole \
	-s adresse_source --sport port_source \
	-d adresse_destination --dport port_destination \
	-j politique
```

:::tip
Exemple de structure du fichier de script :

```sh
#!/usr/bin/env bash

# 1. Installation des packages : `iptables` et `iptables-persistent`

# 2. Suppression de toutes les règles actuelles
# Flush All Iptables Chains/Firewall rules
iptables -F
# Delete all Iptables Chains
iptables -X
# Flush all counters too
iptables -Z

# 3. CAS GENERAL : application des policy (option `-P`)

# 4. CAS PARTICULIERS : mise en place des règles (option `-A`)

# 5. Persister les règles

# 6. Installation du script : documentation sur le propriétaire et les droits
```
:::

:::tip
Pour logger les paquets, on pourra utiliser la cible `-j LOG` et le `--log-level 4` et ajouter un `--log-prefix` (par exemple, "IPTABLES-DROP: ").
:::

:::tip
Pour autoriser les connexions entrantes **(déjà) établies**, on pourra :

- charger le module qui gère la persistance des connexions (avec l'option `-m`)
- utiliser le matcher d'état : `--ctstate` sur les états `ESTABLISHED` et `RELATED`
:::

## Livrables attendus

1. Un fichier `firewall.sh` opérationnel.
2. Une capture d'écran ou un rapport des tests réseau réalisés.
3. Une explication des choix liés aux droits du fichier `firewall.sh`.

