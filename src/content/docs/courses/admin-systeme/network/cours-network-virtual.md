---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Technologies de Réseau Virtuel
type: cours
sidebar:
  order: 2
description: Technologies de Réseau Virtuel
---

## Rappels : NAT, PAT, Bridge

Voir les liens :

- <https://www.it-connect.fr/le-nat-et-le-pat-pour-les-debutants/>
- <https://www.it-connect.fr/comprendre-les-differents-types-de-reseaux-de-vmware-workstation-pro/>
- NAT vs BRIDGE : <https://blog.stephane-robert.info/docs/homelab/bridge-nat/>

---

## VLAN (Virtual Local Area Network) 🌐

- But : Segmenter un réseau physique en plusieurs réseaux logiques (virtuels).
- Fonctionnement : Tags pour identifier et séparer le trafic (Layer 2).
- Avantages 🌟 :
  - **Sécurité :** Isolation des segments de réseau 🔐
  - **Gestion simplifiée :** Regroupe les flux utilisateurs par fonction ou département 🧑‍💼👩‍💼
  - **Efficacité :** Réduit la taille des domaines de diffusion ⚡
- Inconvénients ❌:
  - **Scalabilité limitée :** 4096 Vlan ID 📉
  - **Complexité de gestion** dans des environnements très larges 🧩

---

## IPIP ou IPinIP (IP in IP Encapsulation) 🎁📦

- But : Créer des tunnels virtuels à travers des réseaux IP existants (majoritairement point-à-point) 🕳️➡️📨
- Fonctionnement : Encapsulation de paquet IP dans un autre paquet IP (sans modifier le paquet original) (Layer 3).
- Avantages 🌟 :
  - **Simple :** pas de modifications des paquets originaux 🛠️
  - **Compatibilité :** tout réseau IP, sans matériel spécifique 🖧
- Inconvénients ❌:
  - **Overhead :** taille des paquets => **latence** 📏🐢
  - **Sécurité :** Pas de chiffrement ou d'authentification pour sécuriser les tunnels 🔐

---

## VXLAN (Virtual Extensible LAN) 🧳🌍

- But : Créer des réseaux virtuels (Layer 2) sur des infrastructures IP existantes (Layer 3) 📦➡️📨
- Principe : Encapsule trames Ethernet dans des paquets UDP/IP
- Très utilisé en infra Cloud (multi zones) et multi sites.
- Fonctionnement :
  - _VXLAN Tunnel End Point_ (_VTEP_) : points d'entrée / sortie :
    - Encapsule les trames Ethernet dans des paquets UDP/IP pour les transporter via le réseau IP sous-jacent (overlay -> underlay) ;
    - À la réception, décapsule les paquets VXLAN pour les livrer au réseau local de destination.
  - VTEP software : VMware ESXi, Microsoft Hyper-V, …
  - VTEP hardware : switchs ToR (Top of Rack), …
  - _VTEP IP_ : IP publique unique du VTEP, lien avec le réseau sous-jacent
  - _Virtual Network Identifier (_VNI_) : équivalent VLAN ID (1 VTEP IP -> 1+ VNI)
- Avantages 🌟 :
  - **Scalabilité :** 16 millions de VNI 📈
  - **Flexibilité :** Réseaux virtuels indépendamment de l'infrastructure physique 🛠️
  - **Compatibilité :** Fonctionne sur réseaux IP existants sans modification majeure ✅
  - **Fonctionnalités :** _unicast_, _broadcast_, _multicast_
- Inconvénients ❌:
  - **Complexité :** supplémentaire à la gestion du réseau 🔄
  - **Performance :** Encapsulation = latence supplémentaire (> à IPIP mais assez similaire) et gros overhead au payload 🐢

```sh
ip link show type vxlan
```

:::note
Voir aussi :

- <https://www.techsyncer.com/fr/vxlan-vmware-basics.html>
- <https://vincent.bernat.ch/fr/blog/2017-vxlan-linux>
- <https://networklessons.com/cisco/ccnp-encor-350-401/introduction-to-virtual-extensible-lan-vxlan>
- <https://dryusdan.space/mon-lab-episode-3-isoler-les-reseaux>

:::

---

## eBPF (extended Berkeley Packet Filter) 🧬🐧

- Technologie puissante et flexible intégré au noyau Linux
- **Fonctionnement** : Programmes eBPF écrits en C ou en Rust, puis compilés en bytecode eBPF et chargés directement dans le noyau Linux ⚙️
- **Hooks** : Les programmes sont exécutés suite à des événements noyau : appels système, événements réseau, traces de fonctions, … 🔗
- Avantages 🌟 :
  - **Performance élevée :** Exécution directe dans le noyau avec une latence minimale 🚀
  - **Flexibilité :** Initialement conçu pour le filtrage de paquets réseau, aujourd'hui large gamme d'applications, de la surveillance à la sécurité en passant par le réseau 🔍🛡️
  - **Sécurité :** Vérification des programmes eBPF exécutés par le noyau ✅
- Inconvénients ❌:
  - **Complexité :** Nécessite une bonne compréhension du fonctionnement interne du noyau Linux 🧠
  - **Compatibilité :** Noyau Linux compatible eBPF 📦🔒

### Utilisations Courantes

- 🧐📊 Surveillance et Observabilité : **Tracing** (appels système, événements réseau, …), **Profiling**
- 🔒🛡️ Sécurité : **Détection d'intrusion** (comportements suspects, tentatives d'intrusion en temps réel), **Contrôle d'accès**
- 🌐🛠️ Réseau : **Filtrage de paquets** en fonction de règles complexes (flexible et performant), **Routage et NAT** directement dans le noyau 🔁
- ⚙️⚡ Optimisation des Performances : **Surveillance** et contrôle de l'utilisation des ressources système, **optimisation** mémoire, CPU, I/O 📊🧮

### Outils et Projets Basés sur eBPF 🛠️📦

- _BCC (BPF Compiler Collection) :_ Collection d'outils et d'exemples pour écrire, compiler, et exécuter des programmes eBPF 📚
- _bpftrace :_ Langage de script haut niveau 📝
- _Cilium :_ CNI (Container Network Interface) pour Kubernetes qui utilise eBPF pour fournir des politiques de réseau et de sécurité à haute performance ☸️🛡️
- _Falco :_ Outil de détection d'intrusion en temps réel (IDS) basé sur eBPF, conçu pour surveiller les comportements suspects dans les environnements cloud-native ☁️🔍

### Exemple de Service k8s avec Cilium

La `ServiceHashMap` (informations de routage) eBPF de Cilium joue le rôle de Load Balancer. Le `Service IP` est l'IP publique (virtuelle) du service. Les "Endpoint IP" sont les IPs des conteneurs des Pods.

| Service IP | Port | Service ID | Endpoint ID | Endpoint IP | Port |
| ---------- | ---- | ---------- | ----------- | ----------- | ---- |
| 1.2.3.4    | 8080 | 1          | 4           | 4.3.2.1     | 8080 |
| 1.2.3.4    | 8080 | 1          | 5           | 4.3.2.2     | 8080 |

Exemple de `ConnTrackMap` (tracking des connexions) :

| Service IP | Source Port | Destination IP | Destination Port | Type   | EndpointID | Service ID |
| ---------- | ----------- | -------------- | ---------------- | ------ | ---------- | ---------- |
| 4.3.2.3    | 80          | 1.2.3.4        | 8080             | SVC    | 4          | X          |
| 4.3.2.3    | 80          | 4.3.2.1        | 8080             | Egress | X          | 1          |

:::note
Voir : <https://medium.com/@rickijen/how-to-use-ebpf-to-capture-traffic-over-cilium-vtep-integration-fcb70cef0fc1>
:::

---

## BGP (Border Gateway Protocol) 🌍📡

- Définition : Protocole de routage externe (gateway extérieures) utilisé pour échanger des informations de routage entre différents _systèmes autonomes_ (AS) sur Internet.
- Fonctionnement : Utilise des tables de routage pour déterminer les meilleurs chemins pour acheminer le trafic entre les réseaux.
- Avantages 🌟 :
  - **Scalabilité :** Conçu pour gérer des réseaux de grande taille comme Internet 🌐
  - **Flexibilité :** Permet des politiques de routage complexes et personnalisées 🎛️
  - **Robustesse :** Capable de gérer des pannes et des changements de topologie réseau 🛠️
- Inconvénients ❌:
  - **Complexité :** Configuration et gestion complexes, nécessitant une expertise approfondie 🧠
  - **Convergence lente :** Peut prendre du temps pour converger en cas de changements importants dans le réseau 🕒

### Outils et Projets Basés sur BGP 🧪

- `Bird` & `FRRRouting` : simulateurs BGP

:::note
Voir aussi : <https://une-tasse-de.cafe/blog/bgp-kubernetes/>
:::

---

## Comparaison 📊

| Critère           | VLAN                           | VXLAN                              | BGP                             | IPinIP                                   | eBPF                                                          |
| ----------------- | ------------------------------ | ---------------------------------- | ------------------------------- | ---------------------------------------- | ------------------------------------------------------------- |
| **Couche OSI**    | Couche 2 (Liaison de données)  | Couche 2 et 3                      | Couche 3 (Réseau)               | Couche 3 (Réseau)                        | Couche 3 (Réseau)                                             |
| **Scalabilité**   | Limité à 4096 VLANs            | Jusqu'à 16 millions de segments    | Très élevée                     | Moyenne                                  | Très élevée                                                   |
| **Flexibilité**   | Moyenne                        | Élevée                             | Élevée                          | Élevée                                   | Très élevée                                                   |
| **Complexité**    | Moyenne                        | Élevée                             | Très élevée                     | Faible                                   | Élevée                                                        |
| **Utilisation**   | Segmentation de réseaux locaux | Réseaux virtuels extensibles       | Routage inter-AS sur Internet   | Tunnels virtuels sur réseaux IP          | Surveillance, sécurité, réseau, optimisation des performances |
| **Sécurité**      | Isolation des segments         | Isolation des segments             | Politiques de routage complexes | Nécessite des mécanismes supplémentaires | Vérification rigoureuse des programmes                        |
| **Performance**   | Bonne                          | Potentielle latence supplémentaire | Bonne                           | Overhead supplémentaire                  | Très haute                                                    |
| **Compatibilité** | Réseaux Ethernet               | Réseaux IP                         | Réseaux IP                      | Réseaux IP                               | Noyau Linux                                                   |
| **Intégration**   | Commutateurs et routeurs       | Commutateurs et routeurs           | Routeurs                        | Routeurs                                 | Outils de surveillance et sécurité                            |
| **Résilience**    | Moyenne                        | Élevée                             | Très élevée                     | Moyenne                                  | Très élevée                                                   |

---

### Conclusion 🧭

- **VLAN** : segmentation simple et efficace des réseaux locaux 🧱
- **IPIP** : tunnels virtuels simples et compatibles sur des réseaux IP existants 🕳️
- **VXLAN** : réseaux virtuels extensibles sur des infrastructures IP existantes 🌉
- **eBPF** : technologie puissante et polyvalente offrant des capacités avancées avec une performance inégalée 🚀
- **BGP** : routage inter-AS sur Internet et les grands réseaux 🌐

---
