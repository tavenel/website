---
title: TP Bash - Gestion des fichiers et des utilisateurs
date: 2024 / 2025
correction: false
---

## Présentation du TP

### Objectifs

- Apprendre à manipuler des fichiers et des répertoires avec Bash.
- Utiliser des boucles et des conditions.
- Créer des scripts interactifs.
- Gérer les utilisateurs et permissions basiques dans un environnement Linux.

### Contexte

Vous êtes administrateur système junior. Vous devez écrire un script pour automatiser certaines tâches courantes, telles que :
  - La création de répertoires.
  - La gestion des utilisateurs fictifs.
  - La vérification et le nettoyage de fichiers.

### Consignes supplémentaires

- Les scripts doivent être commentés pour expliquer chaque étape.
- Gérez les erreurs (ex. : répertoire inexistant, permissions insuffisantes).
- Testez les scripts dans un environnement virtuel ou sur une machine de test.

## Exercice 1 : Créer un script de nettoyage

### But

Créer un script qui :

1. Supprime tous les fichiers d'un répertoire donné dont l'extension est `.tmp`.
2. Affiche combien de fichiers ont été supprimés.
3. Permet à l'utilisateur de confirmer avant chaque suppression.

### Instructions

1. Le script doit prendre en argument un chemin de répertoire.
2. Parcourez les fichiers dans ce répertoire avec une boucle.
3. Pour chaque fichier avec l'extension `.tmp`, affichez une confirmation avant suppression.
4. Affichez un résumé à la fin.

### Exemple de sortie attendue

```bash
$ ./cleanup.sh /home/user/temp
Voulez-vous supprimer /home/user/temp/test1.tmp ? (y/n) y
Voulez-vous supprimer /home/user/temp/test2.tmp ? (y/n) n
2 fichiers .tmp trouvés, 1 supprimé(s).
```

::: {.correction .if correction="true"}
### Corrigé

```bash
#!/bin/bash

# Vérification des arguments
if [ $# -ne 1 ]; then
    echo "Usage : $0 <chemin_du_répertoire>"
    exit 1
fi

# Répertoire à analyser
DIR=$1

# Vérifier si le répertoire existe
if [ ! -d "$DIR" ]; then
    echo "Erreur : Le répertoire $DIR n'existe pas."
    exit 1
fi

# Compteur de fichiers supprimés
count=0

# Parcourir les fichiers .tmp
for file in "$DIR"/*.tmp; do
    echo "Voulez-vous supprimer $file ? (y/n)"
    read -r response
    if [ "$response" = "y" ]; then
        rm "$file"
        echo "$file supprimé."
        count=$((count + 1))
    else
        echo "$file ignoré."
    fi
done

# Résumé final
echo "$count fichiers .tmp supprimé(s)."
```
:::

## Exercice 2 : Gestion d'utilisateurs fictifs

### But

Écrire un script qui :

1. Ajoute un ou plusieurs utilisateurs fictifs à partir d’un fichier texte.
2. Associe à chaque utilisateur un répertoire personnel dans `/home`.
3. Applique des permissions pour que seul cet utilisateur puisse accéder à son répertoire.

### Instructions

1. Le fichier texte d'entrée contient une liste de noms d'utilisateur (un par ligne).
2. Pour chaque utilisateur :
   - Créez un répertoire dans `/home` avec son nom.
   - Appliquez les permissions `700` sur ce répertoire.
3. Affichez un message confirmant la création de chaque utilisateur.

### Exemple de fichier d'entrée

```text
alice
bob
charlie
```

### Exemple de sortie attendue

```bash
$ ./add_users.sh users.txt
Répertoire /home/alice créé avec permissions 700.
Répertoire /home/bob créé avec permissions 700.
Répertoire /home/charlie créé avec permissions 700.
```

::: {.correction .if correction="true"}
### Corrigé

```bash
#!/bin/bash

# Vérification des arguments
if [ $# -ne 1 ]; then
    echo "Usage : $0 <fichier_utilisateurs>"
    exit 1
fi

# Fichier d'entrée
FILE=$1

# Vérifier si le fichier existe
if [ ! -f "$FILE" ]; then
    echo "Erreur : Le fichier $FILE n'existe pas."
    exit 1
fi

# Parcourir les noms d'utilisateur
while IFS= read -r user; do
    # Vérifier si le nom d'utilisateur est vide
    if [ -z "$user" ]; then
        continue
    fi

    # Créer un répertoire personnel
    USER_DIR="/home/$user"
    if [ ! -d "$USER_DIR" ]; then
        mkdir "$USER_DIR"
        chmod 700 "$USER_DIR"
        echo "Répertoire $USER_DIR créé avec permissions 700."
    else
        echo "Le répertoire $USER_DIR existe déjà."
    fi
done < "$FILE"
```
:::

## Exercice 3 : Analyse des fichiers système

### But

Créer un script qui analyse les fichiers dans `/var/log` et extrait les 10 dernières lignes des fichiers contenant des erreurs (`error`).

### Instructions

1. Parcourez tous les fichiers de `/var/log`.
2. Pour chaque fichier texte :
   - Cherchez les occurrences du mot `error` (insensible à la casse).
   - Affichez les 10 dernières lignes contenant ce mot.
3. Sauvegardez le résultat dans un fichier nommé `error_report.txt`.

### Exemple de sortie attendue

```bash
$ ./analyze_logs.sh
Analyse des logs dans /var/log...
Logs contenant des erreurs sauvegardés dans error_report.txt.
```

::: {.correction .if correction="true"}
### Corrigé

```bash
#!/bin/bash

# Répertoire des logs
LOG_DIR="/var/log"
OUTPUT_FILE="error_report.txt"

# Vérifier si le répertoire existe
if [ ! -d "$LOG_DIR" ]; then
    echo "Erreur : Le répertoire $LOG_DIR n'existe pas."
    exit 1
fi

# Nettoyer ou créer le fichier de sortie
> "$OUTPUT_FILE"

echo "Analyse des logs dans $LOG_DIR..."

# Parcourir les fichiers logs
for log_file in "$LOG_DIR"/*; do
    # Vérifier si c'est un fichier
    if [ -f "$log_file" ]; then
        # Chercher les lignes contenant "error"
        grep -i "error" "$log_file" | tail -n 10 >> "$OUTPUT_FILE"
    fi
done

echo "Logs contenant des erreurs sauvegardés dans $OUTPUT_FILE."
```
:::

## Exercices supplémentaires

### 1. Sauvegarde et restauration automatisées

#### But

Ajouter une fonctionnalité de sauvegarde et de restauration pour les répertoires.  

#### Description

- Le script demande à l'utilisateur de sélectionner un répertoire à sauvegarder.  
- La sauvegarde crée une archive compressée (`.tar.gz`) et la stocke dans un dossier spécifique (ex. : `/backup`).  
- Une option permet également de restaurer une sauvegarde en décompressant l'archive dans un chemin spécifié.  

#### Exemple de menu interactif

```bash
1. Sauvegarder un répertoire
2. Restaurer une sauvegarde
3. Quitter
```

### 2. Surveillance de l'espace disque

#### But

Créer un script qui surveille l'espace disque et alerte si l'utilisation dépasse un seuil défini (ex. : 80 %).  

#### Description

- Utilisez la commande `df` pour analyser l'espace disque.  
- Si le seuil est atteint, le script envoie une notification (via `mail` ou `echo`).  
- Ajoutez une option pour afficher un résumé de l’utilisation par partition.  

#### Exemple de sortie

```bash
Alerte : La partition /dev/sda1 utilise 85 % de l'espace disque.
```

### 3. Gestion des processus

#### But

Écrire un script pour surveiller et gérer les processus en cours.  

#### Description

- Lister tous les processus actifs (`ps` ou `top`).  
- Filtrer les processus par utilisateur ou par mot-clé.  
- Permettre à l'utilisateur de terminer un processus en entrant son PID.  

#### Exemple de menu

```bash
1. Lister les processus actifs
2. Rechercher un processus par nom
3. Terminer un processus (par PID)
4. Quitter
```

### 4. Journalisation avancée

#### But

Ajouter un système de journalisation dans tous les scripts.  

#### Description

- Tous les événements importants (fichiers supprimés, utilisateurs créés, erreurs rencontrées, etc.) sont enregistrés dans un fichier de log avec un timestamp.  
- Exemple : `/var/log/custom_script.log`.  
- Utilisez la commande `logger` ou redirigez explicitement les sorties.  

#### Exemple d'entrée dans le journal

```text
[2024-11-19 10:30:45] Fichier /home/user/temp/test1.tmp supprimé.
[2024-11-19 10:32:10] Erreur : Impossible de créer l'utilisateur "bob".
```

### 5. Interface graphique simple (Zenity ou Whiptail)

#### But

Remplacer les interactions en ligne de commande par des interfaces graphiques simples.  

#### Description

- Utilisez **Zenity** (pour GNOME) ou **Whiptail** (interface dialoguée en mode texte) pour afficher des fenêtres interactives.  
- Par exemple, affichez des boîtes de dialogue pour demander confirmation avant de supprimer des fichiers ou pour sélectionner des options dans un menu.  

#### Exemple avec Zenity

```bash
zenity --question --text="Voulez-vous supprimer /home/user/temp/test1.tmp ?"
```

---

### 6. Gestion des sauvegardes incrémentales

#### But

Implémenter un système de sauvegardes incrémentales.  

#### Description

- Comparez les fichiers d'un répertoire avec leur dernière sauvegarde et copiez uniquement les fichiers modifiés.  
- Utilisez des outils comme `rsync` ou des commandes Bash natives (comparaison avec `diff` ou `find -mtime`).  

### 7. Notification via Slack, Telegram ou e-mail

#### But

Envoyer des notifications pour des événements critiques (espace disque, erreurs, sauvegarde réussie).  

#### Description

- Configurez un webhook pour Slack ou Telegram pour envoyer des messages automatiquement.  
- Ajoutez une option pour envoyer des rapports par e-mail à l'utilisateur.  

