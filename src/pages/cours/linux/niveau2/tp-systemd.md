---
title: Systemd init
date: 2024 / 2025
correction: false
---

## Terminologie

`systemd` est un programme assez générique de gestion de ressources système. La terminologie est donc un peu différente de la terminologie "classique" d'un système Linux :

- Les ressources et services gérés sont appelés `unit` et groupées en `target`.
- Les `service` sont les `unit` les plus courants (programmes à démarrer, arrêter, redémarrer).
- Un `device` est un périphérique géré par `udev` (utile pour charger des ressources à l'insertion d'un périphérique).

:::tip
- Voir le cours _systemd_, 101.3 Lesson 1 p.40 pour plus de détails
- Pour plus de détails sur la commande `systemctl`, voir le cours _systemd_, 101.3 Lesson 1 p.41
:::

:::link
Voir aussi : <https://blog.stephane-robert.info/docs/admin-serveurs/linux/systemd/> et <https://blog.stephane-robert.info/docs/admin-serveurs/linux/services/>
:::

## systemctl

`systemctl` est une commande système de gestion de services et d'unités sur les systèmes Linux utilisant le gestionnaire d'init `systemd`. Elle permet aux administrateurs système de contrôler et de surveiller les services, les socket, les périphériques et d'autres unités système.

### Gestion des services

- `systemctl start nom-du-service` : Démarre un service.
- `systemctl stop nom-du-service` : Arrête un service.
- `systemctl restart nom-du-service` : Redémarre un service.
- `systemctl reload nom-du-service` : Recharge la configuration d'un service sans le redémarrer.
- `systemctl status nom-du-service` : Affiche l'état d'un service, y compris s'il est en cours d'exécution ou s'il a rencontré des erreurs.
- `systemctl enable nom-du-service` : Active un service pour qu'il démarre au démarrage du système.
- `systemctl disable nom-du-service` : Désactive un service pour qu'il ne démarre pas au démarrage du système.
- `systemctl is-active nom-du-service` : Vérifie si un service est actif (en cours d'exécution).
- `systemctl is-enabled nom-du-service` : Vérifie si un service est activé pour le démarrage.

### Gestion des unités

- `systemctl list-units` : Liste toutes les unités (services, cibles, montages, etc.) actuellement chargées.
- `systemctl list-unit-files` : Liste toutes les unités disponibles, qu'elles soient activées ou désactivées.
- `systemctl show nom-de-l-unite` : Affiche des informations détaillées sur une unité spécifique, y compris ses dépendances et ses propriétés.

### Gestion des cibles (targets)

- `systemctl get-default` : Affiche la cible (`target`) par défaut du système, qui détermine le niveau d'exécution au démarrage.
- `systemctl set-default nom-de-la-cible` : Définit la cible par défaut du système au démarrage.

### Gestion des sessions utilisateur

- `systemctl --user` : Permet de gérer les services et les cibles spécifiques à la session utilisateur.

### Gestion des journaux (logs)

- `systemctl status nom-du-service` : Affiche les messages de journal liés à un service.
- `journalctl` : Permet de consulter les messages de journal du système.

### Contrôle de la sécurité

- `systemctl list-timers` : Affiche les minuteries système, qui sont utilisées pour planifier des tâches périodiques (`cron-like`).
- `systemctl list-sockets` : Affiche les socket système en cours d'utilisation.
- `systemctl list-machines` : Affiche les machines virtuelles `systemd` en cours d'exécution (nécessite `systemd-machined`).

### Gestion des instantanés de système

- `systemctl snapshot` : Crée un instantané du système pour sauvegarder l'état actuel.
- `systemctl list-snapshots` : Liste les instantanés système disponibles.

## journalctl

`journalctl` est une commande utilisée pour interagir avec le système de journalisation, appelé `journal systemd`, présent sur les systèmes Linux utilisant le gestionnaire d'init `systemd`. Le `journal systemd` est responsable de la collecte et du stockage des journaux système, ce qui inclut des informations sur les événements système, les erreurs, les démarrages, les arrêts, ...

Par défaut, `journalctl` lit les journaux dans `/var/log/journal` (option `-D` ou `--directory`).

- `journalctl` : affiche les derniers journaux.
- `journalctl -u apache2` : affiche les journaux de l'unité (service) `apache2`.
- `journalctl -fu apache2` : affiche les journaux en temps réel de l'unité (service) `apache2`.
- `journalctl -p err` : affiche uniquement les erreurs.
- `journalctl -n 50` : limiter aux 50 dernières lignes
- `journalctl -S "2023-01-01"` : afficher les journaux depuis le 01/01/2023.
- `journalctl -U "2023-01-01"` : afficher les journaux jusqu'au 01/01/2023.
- `journalctl -g mon_terme_de_recherche` : cherche un terme spécifique dans les logs.
- `journalctl -r` : affichage inverse
- `journalctl --dmesg` : affiche les messages du noyau
- `journalctl --list-boots` : affiche les derniers démarrages du système.
- `journalctl -b` : informations du boot
- `journalctl -k` : informations du noyau

### Fichiers de logs

Les fichiers de logs de `journalctl` sont stockés **au format binaire** (ce qui est très rare sous Linux) dans le répertoire `/var/log/journal/`.

## Travaux pratiques systemd

1. Vérifiez l'état actuel du service `SSH`.
1. Démarrer le service `SSH`.
1. Arrêter le service `SSH`.
1. Activer le service `SSH` pour qu'il démarre automatiquement au démarrage du système.
1. Désactiver le service `SSH` pour qu'il ne démarre pas automatiquement au démarrage.
1. Affichez les journaux du service `SSH`.
1. Utilisez `journalctl` pour rechercher tous les messages contenant le terme `error`.
1. Affichez la cible (`target`) par défaut du système.
1. Changez la cible par défaut du système pour une cible différente (par exemple, `multi-user.target`).

:::link
Voir aussi : <https://blog.stephane-robert.info/docs/admin-serveurs/linux/journalisation/>
:::

:::correction
1. Vérifiez l'état actuel du service `SSH` avec `systemctl status ssh.service`.
1. Démarrer le service `SSH` en utilisant `systemctl start ssh.service`.
1. Arrêter le service `SSH` en utilisant `systemctl stop ssh.service`.
1. Activer le service `SSH` pour qu'il démarre automatiquement au démarrage du système avec `systemctl enable ssh.service`.
1. Désactiver le service `SSH` pour qu'il ne démarre pas automatiquement au démarrage avec `systemctl disable ssh.service`.
1. Affichez les journaux du service `SSH` avec `journalctl -u ssh.service`.
1. Utilisez `journalctl` pour rechercher tous les messages contenant le terme `error` avec `journalctl -g error`.
1. Affichez la cible (`target`) par défaut du système avec `systemctl get-default`.
1. Changez la cible par défaut du système pour une cible différente (par exemple, `multi-user.target`) en utilisant `systemctl set-default`.
:::

### Création d'un service personnalisé

1. Création d'un script de service :
  - Créez un script de service simple qui affiche un message à l'écran. Par exemple, créez un fichier `/etc/systemd/system/mon-service.service` avec un contenu tel que :

   ```ini
   [Unit]
   Description=Mon service personnalisé

   [Service]
   ExecStart=/usr/bin/echo "Bonjour depuis mon service"

   [Install]
   WantedBy=multi-user.target
   ```

2. Rechargement des unités `systemd` :
   - Après avoir créé le fichier de service, exécutez `systemctl daemon-reload` pour recharger les unités systemd.
3. Démarrage et vérification du service :
   - Démarrez votre service personnalisé avec `systemctl start mon-service.service`.
   - Vérifiez l'état du service avec `systemctl status mon-service.service`.

