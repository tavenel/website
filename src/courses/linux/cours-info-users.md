---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Informer les utilisateurs
layout: '@layouts/CoursePartLayout.astro'
---

## 📂 Fichiers et mécanismes d'information

### `/etc/issue`

- Affiché **avant** l'invite de login sur les **consoles locales (tty)**.
- Sert à afficher un **message de bienvenue ou d'avertissement**.

Exemple :

```
Bienvenue sur le serveur de formation LPIC2
Accès réservé aux utilisateurs autorisés.
````

Personnalisation :

```sh
sudo nano /etc/issue
```

Variables dynamiques disponibles :

- `\n` : nom d'hôte
- `\l` : ligne tty
- `\d` : date
- `\t` : heure

Exemple :

```
Bienvenue sur \n, vous êtes sur la console \l - \d à \t
```

---

### `/etc/issue.net`

- Similaire à `/etc/issue`, mais affiché pour les **connexions distantes** (ex. : SSH).
- Nécessite activation via `/etc/ssh/sshd_config` :

```
Banner /etc/issue.net
```

Puis :

```sh
sudo systemctl reload sshd
```

---

### `/etc/motd`

- _Message of the Day_
- Affiché **après** authentification lors d'une session shell.
- Sert à donner des **informations générales** : messages d'administration, annonces, etc.

Contenu fixe :

```sh
sudo nano /etc/motd
```

Systèmes modernes (Debian, Ubuntu...) :

- Génèrent automatiquement `/etc/motd` depuis `/etc/update-motd.d/`
- Pour un _motd_ statique, désactiver ce comportement ou ajouter un script personnalisé.

---

## 📢 Informer les utilisateurs actifs

### `wall` - Envoyer un message à tous les utilisateurs connectés

- Envoie un message **immédiatement** à tous les terminaux utilisateurs connectés.

Exemple :

```sh
echo "Le système sera redémarré dans 5 minutes." | sudo wall
```

---

### `shutdown` - Planifier un arrêt ou un redémarrage avec message

- Permet de prévenir les utilisateurs d'un **arrêt programmé**, avec un **délai** et un **message personnalisé**.

```bash
sudo shutdown -r +10 "Redémarrage pour maintenance. Veuillez sauvegarder votre travail."
```

Autres options :

- `-h` : halt (arrêt)
- `-r` : reboot
- `now` : immédiat

Annuler une planification :

```sh
sudo shutdown -c
```

---

### `systemctl` - Arrêt/redémarrage sans message

Commande moderne (systemd), mais **n'envoie pas de message** aux utilisateurs :

```sh
sudo systemctl reboot
sudo systemctl poweroff
```

---

