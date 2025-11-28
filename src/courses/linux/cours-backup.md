---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Sauvegarde
layout: '@layouts/CoursePartLayout.astro'
---

## Règle 3-2-1-1-0

- 3 = Conservez au moins trois copies de vos données : production, sauvegarde, copie de sauvegarde (en bonus l'archivage compte comme une copie)
- 2 = Utilisez au moins deux types de supports différents pour le stockage (de marque différentes) : disques internes, SAN, NAS (en bonus l'archivage avec les bandes LTO compte comme un support)
- 1 = Conservez au moins une copie hors site : autre site (de production et de sauvegarde) que ce soit une infra de stockage ou dans un coffre-fort par exemple.
- 1 = Conservez au moins une copie hors ligne, isolée ou immuable pour se prémunir d'une destruction volontaire (ransomware, acte malveillant via accès distant)
- 0 = Zéro erreur après tests de restauration : une sauvegarde non restaurable n'est pas exploitable le jour où on en a besoin.

---

## Utilitaires

| Outil | Type | Utilisation | Avantages 🌟 |
|-------|------|-------------|-----------|
| `tar` | Archivage | Créer des archives de fichiers | Simple, combinable avec compression |
| `rsync` | Synchronisation | Synchroniser des fichiers localement ou à distance | Efficace pour les sauvegardes incrémentielles |
| `dump/restore` | Sauvegarde de système de fichiers | Sauvegarder et restaurer des systèmes de fichiers | Sauvegarde complète et incrémentielle |

---

### Tape Archive (tar)

- Utilitaire pour créer des archives de fichiers.
- Simple et largement utilisé.
- Peut être combiné avec des outils de compression comme gzip ou bzip2.
  - Créer une archive : `tar -cvf archive.tar /chemin/vers/dossier`
  - Extraire une archive : `tar -xvf archive.tar`
  - Compresser une archive avec gzip : `tar -czvf archive.tar.gz /chemin/vers/dossier`

---

### Rsync

- Outil de synchronisation de fichiers
- Efficace pour les sauvegardes incrémentielles : ne transfère que les différences
- Prend en charge la compression et le chiffrement.
  - Synchroniser des fichiers localement : `rsync -av /source/ /destination/`
  - Synchroniser des fichiers sur un serveur distant : `rsync -av -e ssh /source/ user@remote:/destination/`

---

### Dump et Restore

- Utilitaires de sauvegarde / restauration complète du système de fichiers.
- Peut être utilisé pour des sauvegardes incrémentielles.
  - Sauvegarder un système de fichiers : `dump -0u -f /chemin/vers/sauvegarde.dump /dev/sdXn`
  - Restaurer une sauvegarde : `restore -rf /chemin/vers/sauvegarde.dump`

---

## Produits dédiés à la sauvegarde

| Outil | Type | Interface | Fonctionalités | Cas d'utilisation |
|-------|------|-----------|----------------|-------------------|
| Partimage | Sauvegarde de partitions | Ligne de commande | Nombreux systèmes de fichiers supportés | Sauvegarde de systèmes |
| MondoRescue | Sauvegarde complète | Graphique et CLI | Sauvegardes incrémentielles | Récupération après sinistre |
| BackupPC | Sauvegarde centralisée | Web | Compression et déduplication des données | Environnements multi-machines |

---

## Continuité de service et SLA

**SLA** (Service Level Agreement) : engagement contractuel de disponibilité (en %) de service sur un an.

| Taux de disponibilité | 99 %                      | 99,9 %                         | 99,99 %                             | 99,999 %                                     |
| ---------------------------- | ------------------------- | ------------------------------ | ----------------------------------- | -------------------------------------------- |
| **Durée d'indisponibilité sur 1 an**       | 3 jours 15 heures     | 8 heures 48 minutes          | 53 minutes              | 5 minutes |
| **Redondance compute**       | N                         | N+1                            | N+2                                 | Active/Active (minimum 3 sites)              |
| **Redondance stockage**      | RAID local                | Stockage distribué single zone | Multi-AZ storage                    | Multi-région ou cross-provider               |
| **Base de données**          | Single instance + backups | Cluster 2 nœuds + failover     | Cluster multi-AZ + replication sync | Multi-région avec commit quasi-sync + quorum |
| **Load balancer**            | Optionnel                 | Obligatoire                    | HA cross-zone                       | HA multi-région + anycast                    |
| **Single Points of Failure** | Plusieurs                 | Élimination de la majorité     | Aucun toléré                        | Aucun toléré + tests proactifs               |
| **Backups**                  | Quotidiens                | Horaires                       | Continus (PITR)                     | Multi-régions + tests automatisés            |
| **Déploiement**              | Downtime acceptable       | Rolling updates obligatoires   | Blue/Green ou Canary                | Zero-downtime + auto-rollback                |
| **Faillite d'un nœud**       | Service indisponible      | Service ralenti                | Impact minimal                      | Aucun impact perceptible                     |
| **Implications RH** | Part-time On-call (dev & ops) | On-call structuré, personnel dédié à fiabilité | Équipe SRE temps plein | Équipes importantes d'ingénierie de fiabilité, On-call hautement spécialisé 24/7, plans d'escalade internationaux. Recrutement de compétences avancées (réseaux, stockage distribué, DB répliquées) |

Pour augmenter la disponibilité d'un service, on utilise généralement **la redondance de tous les éléments** afin d'éviter les **SPOF** (_Single Point of Failure_) : si un élément est défaillant, un autre prend le relai pour assurer une continuité de service (_failover_).

![Tout élément non redondé est un SPOF](https://user.oc-static.com/upload/2018/06/08/15284524666409_SPOF.png)

<div class="caption">Chaque élément unique de l'architecture est un SPOF (Source: https://openclassrooms.com/fr/courses/2356316-montez-un-serveur-linux-et-ses-services/5173591-construisez-une-solution-adaptee-a-vos-besoins)</div>

:::warn
Plus on pousse la disponibilité, plus l'architecture devient complexe et plus la surface d'erreur (et le coût de conception) augmente. Paradoxalement la redondance peut donc créer de nouveaux modes de défaillance si elle est mal gérée.
:::

:::link
Voir aussi :

- <https://www.nobl9.com/resources/do-you-really-need-five-nines>
- <https://thenewstack.io/the-hidden-costs-of-chasing-five-nines-in-availability/>

:::

---
