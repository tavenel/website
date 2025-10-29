---
title: TP Clusters de Haute Disponibilité (HA) et Corosync
date: 2025 / 2026
---

**Niveau :** Avancé / Master Administration Système

## 🎯 Objectif

Monter un cluster 3 nœuds :

- Installer Corosync + Pacemaker sur 3 VMs.
- Configurer corosync.conf (multicast ou udpu selon l'environnement).
- Créer une ressource VirtualIP + service nginx et tester le basculement en stoppant le service sur le nœud actif.

## 🎯 Objectifs pédagogiques

- Comprendre les concepts et les mécanismes des clusters HA.
- Mettre en place un cluster haute disponibilité complet avec **Corosync + Pacemaker**.
- Expérimenter le basculement (failover) de services entre deux nœuds.
- Tester la résilience du cluster en cas de panne.

## Théorie (rappel synthétique)

*(Résumé extrait du cours complet : voir version détaillée du module)*

### Qu'est-ce qu'un cluster de haute disponibilité ?

Un **cluster HA** vise à assurer la **continuité de service** malgré des pannes matérielles ou logicielles. Il s'appuie sur :

- **Corosync** : communication fiable entre les nœuds, quorum, membership.
- **Pacemaker** : orchestration et gestion des ressources (services, IPs, volumes, etc.).
- **Fencing/STONITH** : mécanisme d'exclusion d'un nœud défaillant.

### Types d'architecture

- **Active/Passive** : un nœud actif, l'autre en secours.
- **Active/Active** : services répartis entre plusieurs nœuds (plus complexe).

### Règles de base

- Toujours avoir un **quorum majoritaire**.
- Toujours **activer STONITH**.
- **Tester les scénarios de panne** régulièrement.

## TP Pratique : Cluster HA avec Corosync + Pacemaker

:::tip
Les commandes exactes varient légèrement selon la distribution (Debian/Ubuntu vs RHEL/CentOS). Ci-dessous des exemples génériques.
:::

### Installation

**Debian / Ubuntu**

```bash
sudo apt update
sudo apt install corosync pacemaker crmsh -y
```

**RHEL / CentOS / Alma / Rocky**

```bash
sudo dnf install corosync pacemaker pcs -y
```

### Génération et distribution de la clé d'authentification

Sur `node1` :

```bash
sudo corosync-keygen
# copie du fichier /etc/corosync/authkey vers les autres nœuds (scp) en veillant aux permissions (0400)
sudo scp /etc/corosync/authkey node2:/etc/corosync/
sudo chmod 400 /etc/corosync/authkey
```

### Configuration du cluster

Fichier `/etc/corosync/corosync.conf` identique sur les deux nœuds :

```json
# /etc/corosync/corosync.conf
totem {
  version: 2
  secauth: on
  cluster_name: ha-cluster
  transport: udpu
  interface {
    ringnumber: 0
    bindnetaddr: 192.168.100.0
    mcastport: 5405
  }
}

nodelist {
  node {
    ring0_addr: 192.168.100.10
    nodeid: 1
  }
  node {
    ring0_addr: 192.168.100.20
    nodeid: 2
  }
}

quorum {
  provider: corosync_votequorum
  two_node: 1
}

logging {
  to_syslog: yes
}

service {
  name: pacemaker
}
```

Redémarrez Corosync sur les deux nœuds :

```bash
sudo systemctl restart corosync pacemaker
```

Vérifiez :

```bash
# état Corosync
sudo corosync-cfgtool -s

# état quorum
sudo corosync-quorumtool -l

# logs
journalctl -u corosync -b --no-pager
```

### Configuration Pacemaker

Vérifiez que les deux nœuds sont visibles :

```bash
sudo crm_mon -1
# ou
pcs status --full
```

Les deux nœuds doivent apparaître en ligne (`Online: [ node1 node2 ]`).

### Création d'une ressource IP virtuelle (VIP)

```bash
sudo pcs resource create ClusterIP ocf:heartbeat:IPaddr2 ip=192.168.100.100 cidr_netmask=24 op monitor interval=30s
```

Vérifiez :

```bash
sudo pcs status resources
```

Pinguez la VIP :

```bash
ping 192.168.100.100
```

### Ajout d'une ressource Apache (exemple)

Sur **chaque nœud**, installez Apache :

```bash
sudo apt install apache2 -y
```

Créez la ressource :

```bash
sudo pcs resource create WebServer ocf:heartbeat:apache configfile=/etc/apache2/apache2.conf op monitor interval=30s
```

Ajoutez une contrainte :

```bash
sudo pcs constraint colocation add WebServer ClusterIP INFINITY
sudo pcs constraint order ClusterIP then WebServer
```

Vérifiez :

```bash
sudo pcs status --full
```

### Test du basculement

1. Identifiez le nœud actif :

   ```bash
   sudo crm_mon -1
   ```

2. Stoppez le service Pacemaker sur le nœud actif :

   ```bash
   sudo systemctl stop pacemaker
   ```

3. Observez le basculement automatique sur le second nœud.

4. Redémarrez le service :

   ```bash
   sudo systemctl start pacemaker
   ```

### Test de panne réseau (simulation)

Sur un nœud :

```bash
sudo ip link set eth1 down
```

Sur l'autre : observez la reprise du service.

Restaurez :

```bash
sudo ip link set eth1 up
```

### Nettoyage du cluster

```bash
sudo pcs cluster stop --all
sudo pcs cluster destroy --all
```

## Pour aller plus loin

- Ajouter un **nœud témoin (qdevice)** pour quorum externe.
- Tester un **fencing virtuel** (ex. `fence_virt` sur VirtualBox).
- Utiliser un LUN iSCSI (ou DRBD) pour le stockage partagé des ressources.
- Intégrer une ressource **DRBD** pour la réplication de stockage.
- Observer le comportement via `crm_mon -Af` pour suivi en direct.
- Tester perte d'un anneau réseau (déconnecter une interface).
- Tester ralentissement réseau (tc/netem) et observer les paramètres totem.

## Annexes

### Cheatsheet commandes

- `corosync-cfgtool -s` : statut Corosync.
- `corosync-quorumtool -l` : statut quorum.
- `corosync-keygen` : générer authkey.
- `systemctl status corosync pacemaker` : état des services.
- `crm_mon -1` / `pcs status --full` : état des ressources.

### Commandes utiles de diagnostic

```bash
corosync-cfgtool -s         # affiche l'état des anneaux / token
corosync-quorumtool -l      # état du quorum et votes
journalctl -u corosync -b   # logs du service corosync
journalctl -u pacemaker -b  # logs du gestionnaire de ressources
crm_mon -1, crm_resource    # vue du cluster et ressources (Pacemaker)
pcs status --full           # équivalent pcs
corosync-cmapctl --help     # inspecter cmap (si disponible)
corosync-objctl             # opérations d'administration avancée (selon versions).
```

### Fichier `corosync.conf` : structure et exemples

Le fichier principal de configuration est **/etc/corosync/corosync.conf**. Il contient :

- `totem { ... }` - paramètres du protocole et interfaces réseau.
- `nodelist { node { ... } }` - adresse/identifiant des nœuds.
- `quorum { ... }` - configuration du quorum.
- `logging { ... }` - options de journalisation.
- `service { name: pacemaker }` - déclaration des services utilisateur.

#### Exemple 1 - cluster 3 nœuds (multicast, configuration minimale)

```yaml
totem {
  version: 2
  secauth: on
  cluster_name: mycluster
  token: 3000
  token_retransmits_before_loss_const: 10
  join: 60
  consensus: 3600
  max_messages: 20
  interface {
    ringnumber: 0
    bindnetaddr: 192.168.100.0
    mcastaddr: 226.94.1.1
    mcastport: 5405
  }
}
nodelist {
  node {
    ring0_addr: node1.example.local
    nodeid: 1
  }
  node {
    ring0_addr: node2.example.local
    nodeid: 2
  }
  node {
    ring0_addr: node3.example.local
    nodeid: 3
  }
}
quorum {
  provider: corosync_votequorum
  two_node: 0
}
logging {
  to_syslog: yes
}
service {
  name: pacemaker
}
```

#### Exemple 2 - cluster 2 nœuds (UDPU, binding explicite)

```yaml
totem {
  version: 2
  secauth: on
  cluster_name: mycluster-two-node
  interface {
    ringnumber: 0
    bindnetaddr: 192.168.50.0
    transport: udpu
  }
}
nodelist {
  node { ring0_addr: 192.168.50.10 nodeid: 1 }
  node { ring0_addr: 192.168.50.20 nodeid: 2 }
}
quorum {
  provider: corosync_votequorum
  two_node: 1
}
logging { to_syslog: yes }
service { name: pacemaker }
```

#### Exemple 3 - configuration multi-ring (redondance réseau)

Ajouter plusieurs blocs `interface { ringnumber: 0 }` et `interface { ringnumber: 1 }` pointant vers deux réseaux physiques distincts (ex. `192.168.100.0` et `192.168.101.0`) : ainsi si une interface tombe, l'autre maintient la communication.

