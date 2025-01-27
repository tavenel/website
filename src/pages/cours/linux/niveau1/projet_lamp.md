---
title: Installation d'un serveur LAMP sous Linux
author: Tom Avenel
date: 2024 / 2025
---

## Installation du serveur Web : Apache

Dans cette partie, nous allons installer et configurer un serveur web Apache dans notre système.

- Installer le package `apache2`.
- Vérifiez l’état du service.
- Connectez-vous au serveur Web installé dans la machine Linux depuis votre système Windows :
  + Ouvrir votre navigateur Web préféré et entrez l'URL: <http://IP_DE_LA_MACHINE_LINUX:8080>.
  + On remplacera `IP_DE_LA_MACHINE_LINUX` par l’adresse IP de la machine.
  + Attention, cette adresse IP peut avoir changé en cas de redémarrage du système Linux ! Dans ce cas, la commande `ip addr show` permet de récupérer cette nouvelle adresse.

## Installation du plugin PHP

Dans cette partie, nous allons installer et configurer les paquets php pour le serveur web Apache. Cela va nous permettre d’exécuter du code PHP dans notre serveur.

- Installer les paquets : `php libapache2-mod-php php-mysql`
- Supprimer la page d'index servie actuellement par le serveur apache : `/var/www/html/index.html`.
- Créer une nouvelle page de test PHP : `/var/www/html/index.php`.

On pourra utiliser le contenu suivant dans le fichier `index.php` :

```php
<?php phpinfo(); ?>
```

**Attention : depuis php 7, l’extension php `mysql.so` n'existe plus. Cette extension peut encore être référencée dans certaines documentations - nous utiliserons à la place l’extension `mysqli.so`.**

## Installation de la base de données : MySQL

Dans cette partie, nous allons installer et configurer une base de données MySQL dans notre système.

- Installer les paquets du serveur et du client MySQL. Cela va installer l’implémentation par défaut de la base de données MySQL. Sur Debian, cette implémentation s’appelle `mariadb` et il faut donc remplacer le nom du **service** par `mariadb`, pas le paquet à installer. Sur Ubuntu, il s'agit bien de `mysql` :
  + `$ sudo apt install default-mysql-server default-mysql-client`
- Vérifier que le service de la base de données fonctionne correctement :
  + `$ sudo systemctl status mysql`
- Configurer le mot de passe root de la base de données.
- Arrêter le service de la base de données :
  + `# systemctl stop mysql`
- Démarrer la base de données en mode restreint :
  + `$ sudo mysqld_safe --skip-grant-tables --skip-networking &`
  + Si vous obtenez une erreur : `Directory var/run/mysqld for UNIX socket file don't exist` il s'agit d'un bug lors de l'installation, il faut créer le répertoire manuellement et le donner à l'utilisateur `mysql:mysql` :
    + `$ sudo mkdir /var/run/mysqld`
    + `$ sudo chown mysql:mysql /var/run/mysqld`
    + `$ sudo mysqld_safe --skip-grant-tables --skip-networking &`
- Se connecter à la base de données :
  + `$ mysql -u root`
- Dans l’invité MySQL, taper en remplaçant `mon_password` par le mot de passe de votre choix :

  ```sh
  mysql> FLUSH PRIVILEGES;
  
  mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mon_password'; # Remplacer mon_password par son mot de passe désiré
  
  mysql> exit
  ```

- Redémarrer la base de données :
  + Tuer le processus `mysqld_safe`, par exemple :

    ```sh
    # kill 20982
    ```

  + On pensera à récupérer au préalable son identifiant de processus (PID) grâce à la commande `ps`.

- Redémarrer le vrai service MySQL :
  + `$ sudo systemctl start mysql`
- Tester la connexion à la base de données avec le nouvel utilisateur root :
  + `$ mysql -u root -p`
- Créer et configurer un compte mysql dédié (attention : il s’agit ici d’un compte de la base de données, qui n’a aucun lien avec les utilisateurs du système d’exploitation Linux !)
  + `mysql> CREATE USER 'mon_utilisateur'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mon_password';`

## Créer un véritable site Web en PHP pour ajouter/supprimer des entrées dans une table SQL

Dans cette partie, nous allons déployer le site PHP donnée en exemple et créer une base de données pour supporter l’utilisation de ce site web.

- Créer une nouvelle base de données `test` qui sera utilisée par notre site Web et ajouter les droits à notre utilisateur de base de données :

  ```sh
  mysql> CREATE DATABASE test;
  
  mysql> GRANT ALL PRIVILEGES ON test.* TO 'mon_utilisateur_bd'@'localhost';
  ```

- Copier les fichiers php `minichat.php` et `minichat_post.php` fournis en exemple dans le répertoire : `/var/www/html`.
- Modifier la connexion à la base de données dans les fichiers `minichat.php` et `minichat_post.php` pour utiliser votre utilisateur créé précédemment.
  + Pour cela, on modifiera les deux derniers paramètres de la ligne suivante dans ces fichiers pour remplacer root par notre utilisateur et ajouter le mot de passe dans les derniers guillemets :

    ```sh
    $bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', 'mot_de_passe');
    ```

- Créer la table de l’application dans notre base de données test, **en se connectant avec notre nouvel utilisateur :
  + `$ mysql -u mon_utilisateur -p`

  ```sh
  mysql> use test;
  
  mysql> CREATE TABLE minichat(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, pseudo VARCHAR(100), message VARCHAR(255));
  ```

- Tester le déploiement de notre site web : depuis votre navigateur Web préféré sur votre machine de travail, atteindre l’URL de notre site : http://adresse_ip/minichat.php. On utilisera pour cela l’adresse IP de notre machine virtuelle.

*En cas d’erreur, on pourra inspecter les logs Apache situés dans le répertoire : `/var/log/apache2*`.

# Annexe : fichiers php

## `minichat.php`

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Mini-chat</title>
    </head>
    <style>
    form
    {
        text-align:center;
    }
    </style>
    <body>
    
    <form action="minichat_post.php" method="post">
        <p>
        <label for="pseudo">Pseudo</label> : <input type="text" name="pseudo" id="pseudo" /><br />
        <label for="message">Message</label> :  <input type="text" name="message" id="message" /><br />

        <input type="submit" value="Envoyer" />
	</p>
    </form>

<?php
// Connexion à la base de données
try
{
	$bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', '');
}
catch(Exception $e)
{
        die('Erreur : '.$e->getMessage());
}

// Récupération des 10 derniers messages
$reponse = $bdd->query('SELECT pseudo, message FROM minichat ORDER BY ID DESC LIMIT 0, 10');

// Affichage de chaque message (toutes les données sont protégées par htmlspecialchars)
while ($donnees = $reponse->fetch())
{
	echo '<p><strong>' . htmlspecialchars($donnees['pseudo']) . '</strong> : ' . htmlspecialchars($donnees['message']) . '</p>';
}

$reponse->closeCursor();

?>
    </body>
</html>
```

## `minichat_post.php`

```html
<?php
// Connexion à la base de données
try
{
	$bdd = new PDO('mysql:host=localhost;dbname=test;charset=utf8', 'root', '');
}
catch(Exception $e)
{
        die('Erreur : '.$e->getMessage());
}

// Insertion du message à l'aide d'une requête préparée
$req = $bdd->prepare('INSERT INTO minichat (pseudo, message) VALUES(?, ?)');
$req->execute(array($_POST['pseudo'], $_POST['message']));

// Redirection du visiteur vers la page du minichat
header('Location: minichat.php');
?>
```

# Legal

- © 2024 Tom Avenel under CC  BY-SA 4.0
- Linux is a registered trademark of The Linux Foundation in the United States and/or other countries.
- Apache is a trademark of the Apache Software Foundation.
- Oracle and MySQL are registered trademarks of Oracle and/or its affiliates.
