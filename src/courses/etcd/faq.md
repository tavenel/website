---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: FAQ etcd
layout: '@layouts/CoursePartLayout.astro'
---

### Les clients doivent-ils envoyer leurs requêtes au leader etcd ?

etcd utilise le protocole _Raft_ basé sur un leader ; le leader gère toutes les requêtes client nécessitant un consensus du cluster (écriture, …). Cependant, le client n'a pas besoin de savoir quel nœud est le leader. Toute requête nécessitant un consensus envoyée à un _follower_ est automatiquement transmise au leader. Les requêtes ne nécessitant pas de consensus (par exemple, les lectures sérialisées) peuvent être traitées par n'importe quel membre du cluster.

### Pourquoi un nombre impair de membres de cluster ?

Un cluster etcd nécessite une majorité de nœuds, un quorum, pour s'accorder sur les mises à jour de son état. Pour un cluster à $n$ membres, le quorum est de $\frac{n}{2}+1$ . Pour tout cluster de taille impaire, l'ajout d'un nœud augmentera toujours le nombre de nœuds nécessaires au quorum. Bien que l'ajout d'un nœud à un cluster de taille impaire semble préférable, car il y a plus de machines, **la tolérance aux pannes est moins bonne** : le même nombre de nœuds peut tomber en panne sans perte de quorum, mais le nombre de nœuds susceptibles de tomber en panne est plus élevé.
Un cluster de taille impaire tolère donc le même nombre de pannes qu'un cluster de taille paire, mais avec moins de nœuds.

:::tip
Si le cluster est dans un état où il ne peut plus tolérer de pannes, **ajouter un nœud avant de supprimer des nœuds est dangereux**, car si le nouveau nœud ne parvient pas à s'enregistrer auprès du cluster (par exemple, en raison d'une mauvaise configuration de l'adresse), **le quorum sera définitivement perdu**.
:::

### Quelle est la tolérance aux pannes ?

Un cluster etcd fonctionne tant qu'un quorum de membres peut être établi. Si le quorum est perdu suite à des pannes réseau temporaires, etcd redémarre automatiquement et en toute sécurité une fois le réseau rétabli ; Raft assure la cohérence du cluster. En cas de coupure de courant, etcd conserve le journal Raft sur le disque ; etcd relit le journal jusqu'au point de panne et reprend la participation au cluster. En cas de panne matérielle permanente, le nœud peut être retiré du cluster via l'exécution d'une reconfiguration du cluster.

### Faut-il déployer etcd en cross-region / cross-datacenter ?

Déployer etcd entre régions améliore sa tolérance aux pannes, car les membres se trouvent dans des domaines de défaillance distincts. Le coût est une latence plus élevée des requêtes de consensus liées au franchissement des limites des datacenters. Comme etcd repose sur un quorum de membres pour le consensus, la latence liée au franchissement des datacenters sera relativement importante, car au moins une majorité des membres du cluster doivent répondre aux requêtes de consensus. De plus, les données du cluster doivent être répliquées sur tous les homologues, ce qui entraîne également un coût en bande passante.

:::warn
Avec des latences plus longues, la configuration par défaut d'etcd peut entraîner des élections fréquentes ou des dépassements de délai d'attente.
:::

### Liens etcd

:::link
Voir aussi la documentation officielle _etcd_, notamment : 
- la FAQ (source des explications ci-dessus) : <https://etcd.io/docs/latest/faq/>
- les problèmes courants : <https://etcd.io/docs/latest/learning/design-learner/>
:::

