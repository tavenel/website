---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: SMART - Surveillance des disques
layout: '@layouts/CoursePartLayout.astro'
---

## S.M.A.R.T.

- Self-Monitoring, Analysis and Reporting Technology (**S.M.A.R.T.**) : technologie intégrée dans la plupart des disques durs (HDD) & SSD & NVMe.
- Permet de :
  - Détecter les signes de défaillance imminente
  - Accéder à des statistiques précises sur le fonctionnement du disque
  - Recevoir des alertes en cas de dégradation
- `smartd` : Daemon qui surveille en continu l'état S.M.A.R.T. des disques et peut envoyer des alertes par email ou syslog.
- `smartctl` : Utilitaire en ligne de commande fourni par le paquet `smartmontools`.

---

## `smartctl`

### Vérifier si S.M.A.R.T. est supporté

```console
$ sudo smartctl -i /dev/sda

SMART support is: Enabled
```

### Activer S.M.A.R.T.

```sh
sudo smartctl -s on /dev/sda
```

---

### Lire les attributs S.M.A.R.T.

```sh
sudo smartctl -A /dev/sda
```

Attributs clés :

| ID  | Nom                      | Interprétation                  |
| --- | ------------------------ | ------------------------------- |
| 5   | `Reallocated_SectorCt`    | Signe d’usure / erreur physique |
| 9   | `Power_On_Hours`         | Durée de fonctionnement         |
| 194 | `Temperature_Celsius`     | Température interne du disque   |
| 197 | `Current_Pending_Sector` | Secteurs instables              |


---

### Auto-test S.M.A.R.T.

```sh
# Test court (2 minutes)
sudo smartctl -t short /dev/sda

# Test long (minutes/heures)
sudo smartctl -t long /dev/sda

# Diagnostic complet
sudo smartctl -a /dev/sda

# Vérification
sudo smartctl -l selftest /dev/sda
```

---

