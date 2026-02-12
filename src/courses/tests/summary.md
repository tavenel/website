---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Résumé des tests logiciels
tags:
- tests
- minimal
---

## Objectif : qualité & confiance

- Tester ≠ prouver que ça marche
- **Tester = casser**
- Détecter les défauts tôt
- Réduire les risques en production
- Améliorer maintenabilité et compréhension

---

## Vocabulaire essentiel

- **Cas de test** : liste des tests disponibles
- **Scénario de test**
- **Plan de tests** :
  - Organisation globale
  - Qui ? Quand ? Comment ?

---

## Stratégie globale

- Copier le cycle en V
- Découper en composants
- Associer niveaux de tests ↔ spécifications
- Chaque niveau cible un risque différent

---

## Tests unitaires

- **Tester une brique isolée** : fonction, classe
- Rapides et simples
- Automatisables
- Isole la logique
- Ne doit pas appeler une API ou une DB

```js
// JavaScript
function add(a, b) {
  return a + b;
}

test("addition simple", () => {
  expect(add(2, 3)).toBe(5);
});
```

```python
# Python
def is_even(n):
    return n % 2 == 0

def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False
```

---

## Tests d'intégration

- **Tester l'interaction entre composants** :
  - API ↔ Base de données
  - Service ↔ Service
  - Front ↔ Backend
- Plus lents, plus fragiles

```python
# Vérifie DB + API

def test_create_user(client):
    response = client.post("/users", json={"name": "Alice"})
    assert response.status_code == 201
```

---

## Tests End-to-End (E2E)

- **Vision utilisateur** : parcours métier réel
- Produit complet : UI + Backend + Infra
- Coûteux et lents

```js
// Exemple Cypress

it("login utilisateur", () => {
  cy.visit("/login");
  cy.get("#email").type("user@test.com");
  cy.get("#password").type("1234");
  cy.get("button").click();
  cy.contains("Bienvenue");
});
```

---

## Pyramide des tests

- Beaucoup de **unitaires** : tester tous les cas limites
- Moins d'**intégration** : ne pas retester la logique testée unitairement
- Peu de **E2E** : tester 1 cas "normal" et 1 ou quelques cas d'erreur

---

## Black Box vs White Box

- **Black Box** : vision utilisateur final sans connaître le code pour prioriser par fonctionnalités
- **White Box** : vision développeur pour optimiser les points techniques critiques

---

## TDD - Test Driven Development

1. Écrire test **échouant**
2. Implémenter minimum
3. Refactorer

---

## Bonnes pratiques

- Tests = Documentation (exemples d'utilisation réels)
- Shift-Left Testing : tester **le plus tôt possible**

---

## Industrialisation des tests

- Limiter erreur humaine
- Gagner du temps (répétabilité, feedback rapide pour les devs)
- Pattern **AAA** : _arrange_, _act_, _assert_
- Pipeline CI/CD typique :
  - Build
  - Tests unitaires
  - Tests d'intégration
  - Tests fonctionnels
  - Déploiement

---

## Tests de performance

- Règle : **1 paramètre à la fois**
- **Charge** → utilisateurs normaux
- **Stress** → au-delà des limites
- **Endurance** → longue durée
- **Spike** → pic brutal
- Phases :
  - _Warm-up_
  - _Ramp-up_
  - _Plateau_
  - _Ramp-down_

---

## Tests de recette & validation

- But : valider les fonctionnalités avant mise en production (GO / NO GO)
- Plan de test == Cahier de recette
- Rapport final == PV de recette
- **VABF** : Vérification d'Aptitude au Bon Fonctionnement
- **VSR** : Vérification de Service Régulier
- **Alpha** : interne
- **Beta** : utilisateurs réels

---

