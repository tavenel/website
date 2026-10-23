---
title: 📬 Introduction à Postman
description: 📬 Introduction à Postman
type: cours
sidebar:
  order: 10
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
---
## ✨ Postman

- Plateforme populaire pour le développement, le test et la gestion des API. 🌐
- Permet de :
  - Travailler en **Collaboration** en temps réel sur les API. 👥
  - Créer des **Tests Automatisés** d'API ✅
  - Écrire la **Documentation** des API 📚
  - Gérer différents **Environnements** pour les API. 🌍

---

## 📝 Créer une Requête

---

### ➕ Créer une Nouvelle Requête

1. Cliquez sur le bouton `+` pour ouvrir un nouvel onglet de requête.
2. Choisissez le type de requête HTTP (_GET_, _POST_, _PUT_, _DELETE_, etc.). 📄
3. Entrez l'URL de l'API que vous souhaitez tester. 🌐

---

### ⚙️ Configurer les Paramètres de la Requête

- Ajoutez des en-têtes, des paramètres de requête, ou le corps de la requête si nécessaire.
- Utilisez l'onglet "_Headers_" pour ajouter des en-têtes HTTP. 🏷️
- Utilisez l'onglet "_Body_" pour ajouter des données au format _JSON_, _XML_, etc. 📦

---

## 🏃‍♂️ Exécuter et Analyser les Requêtes

---

### 📊 Analyser la Réponse

- Cliquez sur le bouton "_Send_" pour envoyer la requête à l'API. ▶️ 
- Examinez le code de statut HTTP de la réponse. 🔢
- Consultez les données de réponse dans le corps de la réponse. 📄
- Utilisez l'onglet "_Tests_" pour écrire et exécuter des tests JavaScript sur la réponse. 🧪

---

## 🔢 Script Postman

- Postman est généralement utilisé via son interface graphique, mais vous pouvez également écrire des scripts pour automatiser les tests.
- 💡 Utile pour la CI/CD !
- Exemple de script en _JavaScript_ pour envoyer une requête _GET_ et tester la réponse :

```js
// Envoyer une requête GET à une API
pm.sendRequest({
    url: 'https://jsonplaceholder.typicode.com/posts/1',
    method: 'GET',
}, function (err, response) {
    if (err) {
        console.log(err);
    } else {
        pm.test("Code de statut est 200", function () {
            pm.response.to.have.status(200);
        });

        pm.test("Réponse a un corps non vide", function () {
            pm.expect(response.json()).to.not.eql({});
        });

        console.log(response.json());
    }
});
```

---

