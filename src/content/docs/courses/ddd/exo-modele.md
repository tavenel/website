---
title: 🧪 Refactoring d'un modèle anémique vers un modèle riche
type: exo
sidebar:
  order: 600
description: 🧪 Refactoring d'un modèle anémique vers un modèle riche
---
## 🎯 Objectif pédagogique

- Identifier les faiblesses d'un modèle anémique (pure structure de données sans comportement).
- Refactorer vers un modèle orienté métier (DDD) en encapsulant la logique métier dans les entités, VO, etc.
- Respecter l'encapsulation et la responsabilité des objets.

## 📝 Contexte - Gestion de commande e-commerce

Voici une implémentation initiale du modèle de commande d'un site e-commerce. On souhaite la **refactorer selon les principes du Domain-Driven Design**.

### Code initial (modèle anémique)

```python
class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items  # liste de dictionnaires {'name': str, 'price': float, 'qty': int}
        self.total = 0.0
        self.status = "pending"  # ou 'paid'

    def compute_total(self):
        self.total = 0
        for item in self.items:
            self.total += item['price'] * item['qty']
        return self.total
```

## 💬 Travail demandé

1. Quels sont les **problèmes** de conception dans cette classe `Order` ?
2. Refactorez ce code pour appliquer les patterns tactiques de DDD :
   - Créez une entité `Order` avec comportement métier.
   - Créez une entité `OrderItem` (ou un _Value Object_ si pertinent).
   - Encapsulez la logique métier : ajout d'articles, calcul du total, paiement.
   - Ajoutez des validations métier (ex. : pas de paiement sans article).

:::correction
## ✅ Correction

### Problèmes identifiés :

* `items` est une liste de dictionnaires : structure fragile, non typée.
* `total` est un champ redondant, sujet à incohérence.
* `Order` est une **structure de données passive** (pas de logique métier).
* Aucune **encapsulation** ni validation métier.

### Refactoring proposé

```python
from uuid import uuid4

class OrderItem:
    def __init__(self, name, price, quantity):
        if quantity <= 0:
            raise ValueError("La quantité doit être positive.")
        if price < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer_name):
        self.order_id = str(uuid4())
        self.customer_name = customer_name
        self.items = []
        self.status = "pending"  # ou 'paid'

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def pay(self):
        if not self.items:
            raise Exception("Impossible de payer une commande vide.")
        self.status = "paid"
```

:::

