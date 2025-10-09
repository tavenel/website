---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Clusters de haute disponibilité (HA) et Corosync
layout: '@layouts/CoursePartLayout.astro'
---

## 🎯 Objectifs pédagogiques

- Comprendre les concepts fondamentaux des clusters de haute disponibilité (objectifs, métriques, architectures).
- Expliquer le rôle précis de Corosync dans une pile HA et détailler son fonctionnement interne (Totem, quorum, membership, CPG).
- Installer, configurer et sécuriser Corosync (fichiers de config, authkey, transport multicast vs udpu, multi-ring).
- Intégrer Corosync avec un gestionnaire de ressources (ex. Pacemaker) pour orchestrer des ressources HA.
- Diagnostiquer les incidents courants (split-brain, perte de quorum, réseau malade) et appliquer des mesures correctives.

---

## 📚 Glossaire rapide

- **HA (High Availability)** : Capacité d'un service à rester accessible malgré des pannes matérielles ou logicielles.
- **RTO / RPO** : Recovery Time Objective (temps de rétablissement cible) / Recovery Point Objective (point de reprise des données).
- **Quorum** : Règle de décision majoritaire qui permet d'éviter des états divergents (split-brain).
- **STONITH** : Shoot The Other Node In The Head : mécanisme de fencing/power-off pour garantir l'exclusion d'un nœud fautif.
- **Totem** : Protocole de Corosync assurant la diffusion fiable et l'ordre des messages dans le cluster.
- **CPG** : Closed Process Group : API de messagerie fournissant un canal de communication ordonné.

---

## Théorie des clusters HA

### Pourquoi la HA ? métriques et exigences

- **Disponibilité** : ex. 99.9% → ~8.76h downtime/an. Les exigences déterminent l'architecture.
- **RTO (Recovery Time Objective)** : combien de temps maximal pour rétablir le service.
- **RPO (Recovery Point Objective)** : perte de données tolérable.

Ces contraintes fondent les choix : redondance active/passive ou active/active, réplication synchrone vs asynchrone, etc.

---

### Modèles d'architectures

- **Active–Passive (Primary/Standby)** : un nœud sert, un autre prend la relève (failover). Simple et sûr.
- **Active–Active** : plusieurs nœuds servent simultanément (requiert coordination et ressources partagées ou sharding).
- **Split-brain risk** : augmente quand plusieurs nœuds pensent être primaires : prévention par quorum et fencing.

---

### Composants d’un cluster HA

- **Layer de communication et membership** (ex. Corosync) : maintien de la vue des nœuds et diffusion fiable.
- **Resource manager** (ex. Pacemaker) : définition, démarrage/arrêt et placement des ressources.
- **Agents de ressources** (OCF, LSB) : scripts qui démarrent, arrêtent, monitorent les services.
- **Fencing / STONITH** : isolation irréfutable d'un nœud défaillant (poweroff/reboot via IPMI, PDU, virtualisation).
- **Stockage partagé ou répliqué** : iSCSI, DRBD, NFS, ceph : choisir selon RPO/RTO.

---

### Quorum et décisions distributées

- **Quorum majoritaire** : la majorité des votes doit être présente pour prendre des décisions (prévention du split-brain).
- **Quorum device / qdevice** : entité externe servant d'arbitre lorsqu'on a un nombre pair/insuffisant de nœuds.
- **Two-node clusters** : cas particulier : généralement on active un tie-breaker (Qdevice) ou des règles spécifiques.

---

### Fencing / STONITH

- Sans fencing, on risque la corruption des données : deux nœuds écrivant la même ressource.
- Méthodes : IPMI, iLO, iDRAC, PDU controllable, fence_virt via hyperviseur, fence_xvm, fence_vmware, etc.

:::warn
Toujours configurer un mécanisme STONITH opérationnel avant tout essai en prod.
:::

---

## Vue d'ensemble de Corosync

### Rôle et position dans la pile HA

- **Corosync** fournit la couche de communication fiable, le membership et la gestion du quorum. Il ~ne gère pas directement~ les ressources applicatives.
- Souvent utilisé conjointement avec **Pacemaker** (gestionnaire de ressources) : _Corosync_ gère le cluster membership et transport, _Pacemaker_ orchestre.

### Principaux modules / services

- **Totem** : protocole de diffusion ordonnée (ring/token) qui garantit livraison fiable et ordering.
- **CPG (Closed Process Group)** : API de messagerie pour applications qui ont besoin d’un groupe et d’un ordre (Pacemaker utilise ces API).
- **Quorum** : module qui calcule si le cluster a le droit de voter (majority, expected_votes...).
- **Configuration manager (cmap)** : permet de partager de petites données de configuration/clé-valeur entre nœuds.

### Garanties offertes par Corosync

- **Fiabilité de diffusion** : messages délivrés à tous les nœuds survivants dans le bon ordre.
- **Détection de défaillance et membership** : chaque nœud a une "vue" cohérente du cluster.
- **Quorum** : décision majoritaire pour éviter décisions divergentes.

---

## Architecture et protocole Totem

:::tip
Le Totem protocol fournit la logique sous-jacente de transport et d'ordre. Il utilise un mécanisme de passage de token (token passing) et peut fonctionner via multicast (`mcast`) ou unicast (`UDPU`).
:::

### Token passing

- Un token circule entre nœuds suivant l’ordre de la `nodelist`.
- Le nœud qui possède le token peut émettre des messages ; le token garantit un ordre global.
- Si un nœud ne renvoie pas le token, les autres détectent sa défaillance et mettent à jour la vue.

### Multicast vs UDPU (unicast)

- **Multicast** : efficace pour LAN, nécessite que le réseau autorise le multicast.
- **UDPU (User Datagram Protocol Unicast)** : option si multicast indisponible - chaque pair communique en unicast.
- Choix conditionné par l’infrastructure (clouds/hébergeurs qui bloquent multicast → UDPU).

### Paramètres Totem importants

- `token` (ms) : intervalle cible pour la rotation du token - influences latence de détection ; augmenter si réseau lent.
- `token_retransmits_before_loss_const` : nombre de retransmissions avant qu’un nœud soit considéré perdu.
- `join` : délai maximal pour joindre le cluster.
- `consensus` : paramètres internes pour parvenir à un accord.
- `max_messages` : nombre maximal de messages envoyés quand on détient le token.

:::tip
Ces paramètres ont un impact direct sur la sensibilité aux pannes et la réactivité. Les valeurs par défaut conviennent en général, mais doivent être adaptées pour réseaux à latence élevée.
:::

---

## Intégration avec Pacemaker

### Rôle de Pacemaker (orchestration des ressources)

- Pacemaker agit comme **Resource Manager** : placement, dépendances, contraintes et monitors.
- Pacemaker s'appuie sur Corosync pour la messagerie et la vue du cluster.

### Types de ressources

- **Primitive** : ressource simple (IP flottante, service Apache, script OCF).
- **Group** : collection de primitives exécutées sur le même nœud (ex. VIP + daemon).
- **Clone** : ressource répliquée sur plusieurs nœuds (active/active selon agent).

### Exemple

Création d'un IP flottant et d'un service

:::tip
Exemple via **pcs** (RHEL/CentOS/Fedora). Les commandes équivalentes existent pour `crm`/`crmsh`.
:::

```bash
# authentifier les nœuds
sudo pcs cluster auth node1 node2 node3 -u hacluster -p Secr3t
# création et démarrage du cluster
sudo pcs cluster setup --name mycluster node1 node2 node3
sudo pcs cluster start --all

# création d'une ressource IP
sudo pcs resource create VirtualIP ocf:heartbeat:IPaddr2 ip=192.168.100.200 cidr_netmask=24 op monitor interval=30s

# création d'une ressource apache (exemple)
sudo pcs resource create WebServer ocf:heartbeat:apache configfile=/etc/apache2/sites-enabled/000-default.conf op monitor interval=30s

# contrainte pour que WebServer suive VirtualIP
sudo pcs constraint colocation add WebServer VirtualIP INFINITY
sudo pcs constraint order VirtualIP then WebServer
```

:::warn
Avant toute création de ressources en production, configurer le fencing STONITH.
:::

---

## Sécurité et bonnes pratiques

**Réseau** :

- **Séparer** le plan de données et le plan de gestion/heartbeat (interface dédiée pour Corosync).
- **Réserver** des VLANs ou un réseau privé pour la communication Corosync.
- **MTU** identique sur toutes les interfaces utilisées (éviter fragmentation).

**Synchronisation temporelle** :

- NTP/chrony sur tous les nœuds - des horloges très décalées perturbent les protocoles distribués.

**Authentification & chiffrement** :

- `secauth: on` dans `corosync.conf` pour activer l'authentification.
- Protéger `/etc/corosync/authkey` (0400) et utiliser canaux sécurisés pour sa distribution.

**Fencing (obligatoire)** :

- Configurer un dispositif STONITH dès la mise en production (IPMI, PDU, etc.).
- Tester régulièrement les scénarios de fencing dans un environnement contrôlé.

**Tests et monitoring** :

- Scénarios de test : arrêt brutal d’un nœud, perte d’une interface réseau, surcharge CPU/mémoire.
- Metriques à surveiller : latence réseau, perte de paquets, taux de token loss, logs corosync/pacemaker, état STONITH.

**Valeurs recommandées** :

- **Nombre de nœuds** : idéalement impair (3,5,7) pour faciliter quorum majoritaire.
- **Token** : conserver la valeur par défaut sauf si latence réseau élevée - augmentez prudemment.
- **Multi-ring** : 2 réseaux physiques séparés pour la redondance heartbeat.

---

## Troubleshooting et diagnostics

- **Perte de quorum** : exécuter `corosync-quorumtool -l` et vérifier la configuration `expected_votes`.
- **Split-brain** : deux groupes indépendants - vérifier les logs et la présence d’un mécanisme STONITH.
- **Réseau intermittent** : regarder `dmesg`, `ethtool`, `ip -s link` pour collisions, erreurs.

### Exemple de procédure en cas de split-brain

1. Vérifier l’état du réseau et des nœuds (ping, ssh, journalctl).
2. Ne prenez pas de décision hâtive - identifier la tranche de nœuds majoritaire.
3. Si un nœud est isolé, utiliser STONITH pour l'éteindre proprement.
4. Rattacher le nœud éteint et laisser Pacemaker re-répliquer/relancer les ressources.
5. Si impossible de fencing automatique, envisager remise à zéro manuelle sous contrôle (opération risquée).

---

## QCM / questions de réflexion

1. Pourquoi le fencing est-il indispensable dans un cluster HA ?
2. Expliquez le fonctionnement du protocole Totem en 3 phrases.
3. Quels sont les risques d’utiliser multicast sur un réseau non isolé ?
4. Dans un cluster 2 nœuds, quelles options permettent d’éviter le split-brain ?
5. Décrivez une procédure sûre pour remettre en production un nœud isolé.

---

