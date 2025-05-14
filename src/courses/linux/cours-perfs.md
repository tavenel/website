---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Cours Linux - performances
layout: '@layouts/CoursePartLayout.astro'
---

# performances d'un système Linux

---

## Métriques CPU

- **CPU inactif (%idle)** : Pourcentage de temps où le processeur est inactif et n'exécute aucune tâche.
- **CPU système (%sys)** : Pourcentage de temps où le CPU est occupé à exécuter des tâches du noyau (kernel). Inclut la gestion des processus, du système de fichiers et du réseau.
- **CPU utilisateur (%user)** : Pourcentage de temps passé à exécuter des applications.
- **Attente d’E/S (%iowait)** : Proportion de temps pendant laquelle le CPU attend la fin des opérations d'entrée/sortie (lecture / écriture sur disque dur, …).
  - Une valeur élevée peut indiquer un système qui utilise beaucoup la mémoire d'échange (swap).
- **CPU volé (%steal)** : Pourcentage de temps où le CPU a été alloué à une autre machine virtuelle par l'hyperviseur.
- **Load Average** : moyenne du nombre de processus qui sont en cours ou en attente d’exécution.
  - Généralement présenté par trois valeurs : dernière minute, 5 minutes, 15 minutes (voir `uptime`).
  - Diviser ces valeurs par le nombre de coeurs (ratio 1 == CPU utilisé à 100%, sinon sur- ou sous-exploité).

---

## Types de contention

- **Contention Mémoire** (demandes excédant la capacité ou ralentissements)
  - **OOM-Killer** : Mécanisme du noyau Linux pour libérer de la mémoire vive (RAM) en tuant des processus lorsque celle-ci vient à manquer.
- **Contention CPU** (ralentissements, performances médiocres)
  - `%user` élevé => normal si calcul applicatif important, sinon signe de sous-dimensionnement.
  - `%sys` élevé => le CPU passe beaucoup de temps à gérer les opérations du noyau : système mal configuré, bug de driver, trop de processus système.
- **Contention Réseau** (bande passante saturée, retards dans la communication)
- **Contention I/O** (sollicitation excessive du stockage, délais lecture/écriture, dégradation des performances générales).
  - `%iowait` élevé => le processeur passe beaucoup de temps à attendre que les I/O se terminent (souvent perceptible par l'utilisateur).
  - Mitigations : optimisation des systèmes de fichiers, passer à des disques SSD

---

## Commandes d’analyse

- **top et htop** : Surveillance en temps réel du CPU, de la mémoire et des processus. htop offre une interface améliorée.
- **iotop** : Activité disque, identife les processus gourmands en IO.
- **iostat** : Statistiques détaillées sur l'utilisation du disque
- **vmstat** : Informations sur les processus, la mémoire, le paging, les blocs IO, les interruptions et l'activité du processeur.
- **sar** : Collecte et rapporte des données sur l'activité du système.
- **lsof** : Liste les fichiers ouverts par les processus
- **dstat** : Alternative polyvalente pour visualiser simultanément les statistiques système importantes (CPU, mémoire, disque, réseau).

---

