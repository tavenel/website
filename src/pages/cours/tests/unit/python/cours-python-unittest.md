---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Tests unitaires Python
keywords:
- python
- tests
- unit
---

# Tests unitaires Python avec unittest

---

# Unittest

- Framework de test intégré dans la bibliothèque standard Python.

---

## Structure d'une classe de test

- Tests regroupés dans des _classes de test_ :
  + Regroupe les tests sur le même SUT ou avec le même but.
  + Doit hériter de `unittest.TestCase`
  + 1 test = 1 méthode dont le nom commence par `test`

---

## Exemple d'une classe de test

```python
import unittest

class UneClasseDeTest(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(True)
```

---

# Exécution

---

## Exécution de la classe de test

```python
if __name__ == '__main__':
    unittest.main()
```

---

## Code avant/après chaque test

`setUp()` et `tearDown()` sont exécutés avant / après chaque test

---

```python
import unittest

class UneClasseDeTest(unittest.TestCase):

    def setUp(self):
        print("Avant le test")

    def tearDown(self):
        print("Après le test")

    def test_simple(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
```

---

# Vérifications

- Vérifications par _assertions_ héritées de `unittest.TestCase`
- Acceptent toutes le paramètre optionnel `msg` (message si échec).

---

## Principales assertions

- `assertEqual(a, b)` et `assertNotEqual(a, b)`
- `assertTrue(x)` et `assertFalse(x)`
- `assertIs(a, b)` et `assertIsNot(a, b)`
- `assertIsNone(x)` et `assertIsNotNone(x)`
- `assertIn(a, b)` et `assertNotIn(a, b)`
- `assertIsInstance(a, b)` et `assertNotIsInstance(a, b)`

---

# Exécution des tests

```python
import unittest

class ChaineDeCaractereTest(unittest.TestCase):

    def test_reversed(self):
        resultat = reversed("abcd")
        self.assertEqual("dcba", "".join(resultat))

    def test_sorted(self):
        resultat = sorted("dbca")
        self.assertEqual(['a', 'b', 'c', 'd'], resultat)

    def test_upper(self):
        resultat = "hello".upper()
        self.assertEqual("HELLO", resultat)

if __name__ == '__main__':
    unittest.main()
```

---

## Exécution du fichier de test

```
$ python3 test_str.py

...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

---

## Exécution comme module

```
$ python3 -m unittest test_str

...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

---

# Tester des exceptions : `assertRaises`

```python
import unittest

class AbsTest(unittest.TestCase):

    def test_abs_n_accepte_pas_une_chaine_de_caracteres(self):
        with self.assertRaises(TypeError):
            abs("a")

if __name__ == '__main__':
    unittest.main()
```

---

```sh
$ python3 test_abs.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

---

# Utilisation de doublure

- Substituent des objets réels par de _faux_ objets de test ;
- Permet de contrôler l'environnement du SUT à tester (non changé) en isolation en remplaçant des dépendances d'intégration inutiles par des doublures.

---

## Simulateur

- Implémentation alternative d’un sous-système non disponible pour l'environnement de test.
- ex : BDD en mémoire (`H2`)

---

## Stub

- Remplace une dépendance problématique par une doublure de test au comportement déterministe.
- ex : objet simulant une dépendance à une API Web par une réponse codée en dur et utilisée dans le SUT dans la suite du test.

---

## Mock

- Remplace une dépendance par une doublure de test vérifiant les appels faits à cette dépendance.
- ex : objet simulant une dépendance à une API Web en vérifiant la bonne requête demandée par le SUT à la dépendance.

---

### Utilisation d’un mock

SUT à tester - `is_sourcefile()` utilise la dépendance `path` gérant le chemin d'un fichier sur le système.

```python
from pathlib import Path

def is_sourcefile(path):
    """Retourne True si le fichier est un fichier source Python"""
    if not path.is_file():
        raise Exception("Fichier indisponible")
    return path.suffix == ".py"
```

---

```python
import unittest
from unittest.mock import MagicMock

class FonctionTest(unittest.TestCase):

    def test_is_sourcefile_when_sourcefile(self):
        path = MagicMock()
        path.is_file.return_value = True
        path.suffix = ".py"

        resultat = is_sourcefile(path)

        self.assertTrue(resultat)
        path.is_file.assert_called()

    def test_is_sourcefile_when_file_does_not_exist(self):
        path = MagicMock()
        path.is_file.return_value = False

        with self.assertRaises(Exception):
            is_sourcefile(path)

        path.is_file.assert_called()

    def test_is_sourcefile_when_not_expected_suffix(self):
        path = MagicMock()
        path.is_file.return_value = True
        path.suffix = ".txt"

        resultat = is_sourcefile(path)

        self.assertFalse(resultat)
        path.is_file.assert_called()

if __name__ == '__main__':
    unittest.main()
```

---

### Assertions et méthodes utiles

```python
mon_mock.ma_methode...
...assert_called()
...assert_called_once()
...assert_called_with(param1, param2, ...)
...assert_called_once_with(param1, param2, ...)
...call_count
...call_args # dernier appel
...call_args_list # tous les appels
...method_calls
...return_value = ...
```

Voir aussi les [side effects](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect).

---

### Mock en utilisant des annotations (patch)

Soit le SUT dans le fichier `my_calendar.py` :

```python
import requests
from datetime import datetime

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
```

---

```python
import datetime
import unittest
from requests.exceptions import Timeout
from unittest.mock import patch
import my_calendar

class TestCalendar(unittest.TestCase):

    @patch('my_calendar.datetime')
    def test_monday_is_weekday(self, my_datetime):
        my_datetime.today.return_value = datetime.datetime(2023, 1, 2, 12, 00, 00, 00)

        self.assertTrue(my_calendar.is_weekday())

    @patch('my_calendar.datetime')
    def test_sunday_is_not_weekday(self, my_datetime):
        my_datetime.today.return_value = datetime.datetime(2023, 1, 1, 12, 00, 00, 00)

        self.assertFalse(my_calendar.is_weekday())
```

---

```python
import datetime
import unittest
from requests.exceptions import Timeout
from unittest.mock import patch
import my_calendar

class TestCalendar(unittest.TestCase):

    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):

            mock_requests.get.side_effect = Timeout

            with self.assertRaises(Timeout):
                my_calendar.get_holidays()
                mock_requests.get.assert_called_once()
```

---

<!-- class: liens -->

# Liens

- [Vidéo Python Mock Testing](https://www.youtube.com/watch?v=-F6wVOlsEAM)

---

<!-- class: legal -->

# Legal

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
