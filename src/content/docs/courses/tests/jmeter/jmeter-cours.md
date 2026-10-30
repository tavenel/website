---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Introduction à JMeter
type: cours
sidebar:
  order: 1
description: Introduction à JMeter
---
## 🤔 JMeter

- Outil Java open source conçu pour effectuer des 🏎️ **tests de charge fonctionnels** et mesurer les ⚡ **performances**.
- Initialement développé pour tester les 🌍 **applications web** (_HTTP_, _HTTPS_)
- Support pour les tests de performance des **bases de données** via _JDBC_ 🗃️
- Tests de **services web** : _SOAP_ / _REST_ 🤖
- Hautement extensible grâce aux **plugins** 🧩

---

## 📝 Créer un Plan de Test

---

### ➕ Ajouter des Éléments de Test

1. **Test Plan**: Le nœud racine de votre plan de test. 🌳
2. **Thread Group**: Simule un groupe d'utilisateurs envoyant des requêtes au serveur. 👥
3. **Samplers**: Définissent les types de requêtes à envoyer (HTTP Request, FTP Request, etc.). 📬
4. **Listeners**: Collectent et affichent les résultats des tests (Graph Results, View Results Tree, etc.). 📊

---

### ⚙️ Configurer un Thread Group

- Faites un clic droit sur `Test Plan > Add > Threads (Users) > Thread Group`. ➕
- Configurez le nombre d'utilisateurs (threads), la période de montée en charge (Ramp-Up Period), et le nombre de fois à exécuter le test (Loop Count). ⏱️

---

### 🌐 Ajouter un Sampler HTTP Request

- Faites un clic droit sur `Thread Group > Add > Sampler > HTTP Request`. ➕
- Configurez le serveur, le port, et le chemin de la requête HTTP. 🌐

:::tip
On pourra par exemple utiliser l'API de test : <https://jsonplaceholder.typicode.com/posts/1>
:::

---

## 🏃 Exécuter le Test

- Sauvegardez votre plan de test. 💾
- Cliquez sur le bouton "Start" (triangle vert) pour exécuter le test. ▶️

---

## 📈 Analyser les Résultats

- Utilisez des `Listeners` pour visualiser les résultats. 👂
- Exemples de Listeners:
  - **View Results Tree**: Affiche les détails de chaque requête. 🌳
  - **Summary Report**: Fournit un résumé statistique des résultats. 📄
  - **Graph Results**: Affiche les résultats sous forme graphique. 📊

---

## 💡 Conseils pour des Tests Efficaces

- 🔄 **Paramétrisation**: Utilisez des variables pour simuler différents scénarios de test.
- ✅ **Assertions**: Ajoutez des assertions pour valider les réponses des requêtes.
- ⚠️ Ne pas ~surcharger~ le client JMeter; cela peut fausser les résultats (environnement simple).
  - 🔢 Exporter les tests en scripts **JMX** pour ne pas lancer le client graphique (lourd)
  - 💡 Utile pour la CI/CD !
- 🔍 Surveiller les ressources du serveur pendant les tests pour identifier les goulots d'étranglement.

---

