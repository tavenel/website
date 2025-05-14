---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Cours Linux Interface graphique
layout: '@layouts/CoursePartLayout.astro'
---

# Installation et configuration de X11

---

## X11

- Système graphique historique de Linux
- Modèle client / serveur
- Session X courante dans variable `DISPLAY` (en principe: `:0`)
- `/etc/X11/xorg.conf`
- `~/.xsession-errors`

---

![Architecture de X11](https://learning.lpi.org/en/learning-materials/102-500/106/106.1/106.1_01/images/image_01.png)

<div class="caption">Architecture de X11. Crédits: learning.lpi.org</div>

---

## Wayland

- Successeur de `X11` : adopté par défaut sur `Ubuntu`, `Fedora`, …
- Session courante : variable `WAYLAND_DISPLAY` : (`wayland-0`, …)

---

# Bureaux graphiques

---

## Desktop Environment

- Gestionnaire de fenêtres au-dessus du serveur graphique
- sur-couche à `X11` ou `Wayland`
- [Exemples](https://linux.goffinet.org/administration/introduction-a-linux/environnements-de-bureau/)

---

## Gnome : le bureau intégré

![Le bureau Gnome](https://learning.lpi.org/en/learning-materials/102-500/106/106.2/106.2_01/images/gnome-debian-10.1.0.png)

<div class="caption">Le bureau Gnome</div>

---

## KDE : le bureau configurable

![Le bureau KDE](https://learning.lpi.org/en/learning-materials/102-500/106/106.2/106.2_01/images/kde-opensuse-15.1.png)

<div class="caption">Le bureau KDE</div>

---

## XFCE : le bureau léger

![Le bureau XFCE](https://learning.lpi.org/en/learning-materials/102-500/106/106.2/106.2_01/images/xfce-manjaro-18.1.0.png)

<div class="caption">Le bureau XFCE</div>

---

## Interopérabilité : normes freedesktop.org

- Variables à utiliser dans les applications (valeurs par défaut ci-dessous)
- `XDG_CURRENT_DESKTOP='Wayland'`
- `XDG_CONFIG_HOME=$HOME/.config`
- `XDG_CACHE_HOME=$HOME/.cache`
- `XDG_DATA_HOME=$HOME/.local/share`
- `XDG_RUNTIME_DIR=/run/user/$UID`

---

## VNC et RDP

- Protocoles de connexion à distance pour sessions graphiques

---

# Accessibilité

---

Les bureaux graphiques disposent de nombreux outils d'accessibilité :

- Thèmes du bureau à fort contraste ou grandes polices.
- Lecteur d'écran.
- Lecteur braille.
- Loupe d'écran.
- Clavier virtuel.
- Touches Difficiles/Répétition.
- Touches lentes/rebond/inverser.
- Émulation de la souris au clavier.
- Gestuelles.
- Reconnaissance vocale.

---

<!-- Annexe : liste des TPs -->

[tp-ligne-commande]: tp-ligne-commande.md
[tp-systeme]: tp-systeme.md
[tp-grub]: tp-grub.md
[tp-shared-lib]: tp-shared-lib.md
[tp-sysv-systemd]: tp-sysv-systemd.md
[tp-rpm-apt]: tp-rpm-apt.md
[tp-texte]: tp-texte.md
[tp-fichiers]: tp-fichiers.md
[tp-redirections]: tp-redirections.md
[tp-process]: tp-process.md
[tp-fichiers-avance]: tp-fichiers-avance.md
[tp-partitions]: tp-partitions.md

[tp-ligne-commande]: tp-ligne-commande.md
[tp-systeme]: tp-systeme.md
[tp-grub]: tp-grub.md
[tp-shared-lib]: tp-shared-lib.md
[tp-sysv-systemd]: tp-sysv-systemd.md
[tp-rpm-apt]: tp-rpm-apt.md
[tp-texte]: tp-texte.md
[tp-fichiers]: tp-fichiers.md
[tp-redirections]: tp-redirections.md
[tp-process]: tp-process.md
[tp-fichiers-avance]: tp-fichiers-avance.md
[tp-partitions]: tp-partitions.md
[tp-cron]: tp-cron.md
[tp-lang]: tp-lang.md
[tp-smtp]: /cours/cloud/exo-smtp.md
[tp-syslog]: tp-syslog.md
[tp-network]: tp-network.md
[tp-security]: tp-security.md
[tp-ssh-gpg]: tp-ssh-gpg.md

