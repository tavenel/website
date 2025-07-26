---
title: Tests unitaires frontend avec Jest
---

## Récupération des exemples

:::tip
Le code des exemples est disponible dans le dépôt :

```
git clone https://git.sr.ht/~toma/unit-jest
```
:::

Le projet ajoute les dépendances vers la librairie de test `Jest` dans le fichier `package.json`.

Pour installer ces dépendances, exécuter :

```
npm install
```

## Jest

Pour ce TP, nous utiliserons le framework de tests unitaires `Jest` : <https://jestjs.io/>

`Jest` est un framework "Facebook Open Source" qui permet de tester une application en EcmaScript et une grande majorité de framework frontend : `Angular`, `React`, `Vue`, ...

### Fichier de test

Pour écrire un test `Jest`, on crée un fichier `mon_fichier.test.js` qui :

- importe les fonctions du module (fichier `js`) à tester
- regroupe les tests similaires dans une fonction `describe()`
- ajoute une fonction `it()` par test
- utilise la `DSL` de vérification `Jest` : `expect()...`

Exemple de test :

```js
import { sayHello } from './unit1'

describe('Hello test', () => {
    it('should return "Hello, World"', () => {
        expect(sayHello()).toBe("Hello, World")
    })
})
```

:::link
Pour la liste des `matcher` (fonctions de vérification de Jest), voir : <https://jestjs.io/docs/expect>
:::

:::tip
De manière similaire aux fonctions `setUp()` et `tearDown()` de JUnit, Jest supporte les fonctions suivantes :

- `beforeEach()` va exécuter ce bloc de code avant chaque test.
- `afterEach()` va exécuter ce bloc de code après chaque test.
- `beforeAll()` va exécuter ce bloc de code au début de la phase de test, et non avant chaque test.
- `afterAll()` va exécuter ce bloc de code à la fin de la phase de test.

Voir aussi : <https://jestjs.io/docs/setup-teardown>
:::

### Exécution

Pour exécuter les tests, on utilise les scripts `test` et `testCoverage` décrits dans le fichier `package.json` :

```
npm run test
npm run testCoverage
```

:::tip
Ces scripts lancent en fait les modules `NodeJS` : `jest` et `jest --coverage`.
:::

:::tip
Il est possible d'intégrer `Jest` dans votre IDE pour pouvoir lancer directement les tests depuis celui-ci.

On pourra par exemple utiliser [l'extension Jest pour VSCode](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest).
:::

### Premier test unitaire

:::exo
Compléter le `FIXME` du fichier `js/unit/unit1.test.js` pour écrire un premier test unitaire.
:::

