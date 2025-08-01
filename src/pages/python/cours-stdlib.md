---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CourseLayout.astro'
title: La librairie standard Python (stdlib)
tags:
- python
---

## Introduction aux modules

_fichier mon_module.py_

```python
def fun1():
    print('Hello!')

>>> import mon_module
>>> mon_module.fun1()

>>> from mon_module import fun1
>>> fun1()

>>> from mon_repertoire.mon_sous_repertoire.mon_module import fun1 as ma_fonction
>>> ma_fonction()
```

---

### Fichier `__init__.py`

```
mypkg/
    __init__.py
    module1.py
    module2.py
```

L'instruction python `import mypkg` va exécuter le fichier `__init__.py` (si présent) pour ajouter du code lors du chargement du module.

---

### Aide sur les modules

```python
import os

print( dir(os) ) # Liste des fonctions du module 'os'
```

---

```python
import os

help(os) # Page de manuel du module 'os'
```

---

### Modules utiles

- [Principaux modules de la bibliothèque standard][doc-stdlib]
- [Documentation complète de la bibliothèque standard][doc-full]

---

## OS : interactions avec le système d'exploitation

```python
import os

os.system('uname -a') # Exécute la commande shell 'uname -a'
```

## ShUtil : opérer sur les fichiers

```python
shutil.copyfile('data.db', 'archive.db')
```

---

## Gestion simple des arguments

```python
import sys

print(sys.argv)
#['demo.py', 'one', 'two', 'three']
```

---

### Exercice : récupération des arguments

Écrire un script Python affichant le résultat de la multiplication de tous les nombres passés en paramètres. On utilisera une boucle d'itération sur les arguments du script.

---

## Gestion poussée des arguments

```python
import argparse

parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

---

## Fonction input : récupération des entrées utilisateur

```python
print('Veuillez entrer un nombre positif quelconque : ')
nn = input()
print('Le carré de', nn, 'vaut', nn**2)
```

---

## Random

```python
import random
print( random.choice(['apple', 'pear', 'banana']) )
print( random.sample(range(100), 10) )   # sampling without replacement
print( random.random() )    # random float
print( random.randrange(6) )    # random integer chosen from range(6)
```

---

## Logging

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

---

## Fichiers

```python
with open('mon_fichier', 'r+') as f: # Utiliser un bloc 'with' permet de fermer le fichier automatiquement, sinon f.close()
    """
    Modes d'ouverture : 
    'r'  => lecture seule (défaut)
    'w'  => écriture avec écrasement du fichier existant
    'a'  => ajout en fin de fichier
    'r+' => lecture/écriture
    """

    # Lecture
    fichier_total = f.read()
    une_ligne = f.readline()
    for ligne in f:
        print('Ligne du fichier: ', ligne)

    # Ecriture
    f.write('Nouvelle ligne')
```

---

## (Dé)Sérialisation JSON

```python
import json
mon_objet = {'firstname': 'John', 'lastname': 'Doe'}
my_json = json.dumps(mon_objet, indent=4)

print( mon_objet )
print( type(mon_objet) )
print( my_json )
print( type(my_json) )

mon_objet2 = json.loads( my_json )
print( mon_objet2 )
print( type(mon_objet2) )
```

---

## Stockage d'objets JSON

```python
import json
mon_objet = {'firstname': 'John', 'lastname': 'Doe'}
with open('/tmp/cours-stdlib.json', 'r+') as f:
    # Stockage
    json.dump(mon_objet, f, indent=2)
    # Récupération
    mon_objet2 = json.load(f)
```

---

## Empaquetage et installation d'une bibliothèque Python

`pip` est un programme permettant d'installer une bibliothèque Python depuis le [Python Package Index][site-pypi] :

```sh
$ python -m pip install novas
```

Pour plus d'information : [documentation venv][doc-venv].

---

## Accès aux bases de données

---

### SQLite : inclus dans le langage

#### Connection à la base de données et création d'une table

```python
import sqlite3 as sl

con = sl.connect('my-test.db')
with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)
```

---

#### Insertion d'entrées dans la table

```python
sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]
with con:
    con.executemany(sql, data)
```

---

#### Query sur la table

```python
with con:
    data = con.execute("SELECT * FROM USER WHERE age <= 22")
    for row in data:
        print(row)
```

---

### MySQL

`MySQL` n'est pas disponible directement dans le langage.

Installation du connecteur `MySQL` depuis une librairie externe :

```shell
$ pip install mysql-connector-python
```

---

#### Connexion à la base de données et création d'une base

```python
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
```

---

#### Création d'une table et insertion d'entrées

```python
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        [...]
        database="online_movie_rating",
    ) as connection:
    create_movies_table_query = """CREATE TABLE movies( id INT AUTO_INCREMENT PRIMARY KEY, [...])"""
    insert_movies_query = """ INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES ("Forrest Gump", 1994, "Drama", 330.2), [...]"""

    with connection.cursor() as cursor:
        cursor.execute(create_movies_table_query)
        cursor.execute(insert_movies_query)
        connection.commit()
except Error as e:
    print(e)
```

---

#### Insertion d'entrées en utilisant des objets Python

```python
insert_reviewers_query = """ INSERT INTO reviewers (first_name, last_name) VALUES ( %s, %s ) """
reviewers_records = [
    ("Chaitanya", "Baweja"),
    ("Mary", "Cooper"),
    [...]
]
with connection.cursor() as cursor:
    cursor.executemany(insert_reviewers_query, reviewers_records)
    connection.commit()
```

---

#### Query

```python
select_movies_query = "SELECT * FROM movies LIMIT 5"
with connection.cursor() as cursor:
    cursor.execute(select_movies_query)
    result = cursor.fetchall()
    for row in result:
        print(row)
```


[doc-stdlib]: https://docs.python.org/fr/3/tutorial/stdlib.html
[doc-full]: https://docs.python.org/fr/3/library/index.html#library-index
[doc-venv]: https://docs.python.org/3/tutorial/venv.html
[site-pypi]: https://pypi.org 

---

