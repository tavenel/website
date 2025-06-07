---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Problèmes courants
layout: '@layouts/CoursePartLayout.astro'
---

# Types de pannes courantes sous Linux

---

🔴 Pannes système :
- Boot bloqué (erreur `init`, `grub`, kernel panic)
- Services critiques non démarrés
- Permissions système corrompues

---

🟠 Pannes liées à l'utilisateur :
- Mot de passe root oublié
- Clé SSH manquante ou mauvaise configuration
- Suppression accidentelle de fichiers de conf

---

🟡 Pannes réseau :
- DNS injoignable
- IP incorrecte / conflit d’adresse
- Pare-feu trop restrictif

---

# Méthode de diagnostic

1. 🧭 **Observer** : messages d'erreur à l'écran, LED, bruit disque
2. 📜 **Lire les logs** : `journalctl -xe`, `/var/log/syslog`, `dmesg`
3. ⚙️ **Tester les services** : `systemctl status`, `ping`, `netstat`
4. 🔧 **Isoler le problème** : matériel, réseau, config, utilisateur
5. 💡 **Corriger** : fichier de conf, redémarrage, réparation
6. 🧪 **Vérifier** : logs après correction, tests utilisateurs

---

# ⚠️ Crash Recovery

- Problème de démarrage, mot de passe root oublié :
  - Accéder au mode "recovery" (`single-user`)
  - Voir le [TP Grub](tp-grub.md)
- Si besoin, démarrer un système avec un Live CD
  - Voir le [TP Rescue](tp-rescue.md)

