---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Les tests statiques
tags:
- tests
- revue
---

## 🧪 Tests statiques vs dynamiques

- 🏃 **Tests dynamiques** : nécessitent l'exécution du logiciel testé ;
- 📜 **Tests statiques** : examen manuel (_revues_) ou évaluation outillée (_analyse statique_) sans exécuter le code.

---

### 📌 Exemples

- 🏥 Systèmes critiques : _aéronautique, médical, ..._
- 🛠️ Très démocratisé : _IDE, CI_
- 📄 Tout type de livrable : _spécifications, code, manuel utilisateur, page Web, ..._

---

## 🌟 Avantages

- 🛡️ **Prévention** des défauts de conception ou de codage ;
  - 🔍 **Difficulté** à trouver les défauts **dynamiquement** ;
  - 🔧 Détection et correction **plus efficace** **avant** les tests dynamiques
- 📈 Meilleure productivité du développement :
  - 🏗️ **Meilleure conception** et **code plus facile à maintenir** ;
  - 💰 **Réduction** des coûts et des délais de **développement** ;
  - 💰 **Réduction** des coûts et des délais des **tests** ;
- 🗣️ Amélioration de la **communication** dans l'équipe : _revues_.

---

## 📜 La revue de code

---

### 📌 Principe

- 👥 Faire relire le code source par une ou plusieurs personnes autres que celles qui l'ont codé ;
- 👨‍💻 Réalisées par des _développeurs_ ;
- 👥 Éventuellement assistés de _testeurs_ des équipes _Qualité_, _Sûreté de Fonctionnement_, ... ;
- 🛡️ Fait partie du **contrôle de la qualité**.
- 📄 Adaptable à d'**autres livrables** : _spécifications, modèles, ..._

---

### 🎯 Objectifs

- 📜 Vérifier le respect de certains **standards** de codage :
  - 📚 Généraux ;
  - 🏢 Propres à l'équipe / l'entreprise ;
  - 🔧 Contraintes sur le système, ... ;
- 🔍 Identifier des pratiques de programmation **suspectes** ;
- 🎯 Si **connaissance du métier**, peut détecter des **erreurs fonctionnelles**.

---

### 📌 Exemples de vérifications

- 📝 _Nombre de commentaires_ ;
- 📜 _Code structuré_ ;
- 📏 _Constantes_ ;
- 📏 _Longueur des fonctions_ ;
- 🔄 _Décision exprimée simplement_ ;
- 🔄 _Boucles lisibles_ : `while i < max` vs `while i != max` ;
- 🔧 _Variable initialisée_ ;
- ⚠️ _Division par zéro_ ;
- ⚠️ _Indice sortant du tableau_ ;
- 📂 _Fichier non fermé_ ;
- 🗑️ _Fuite mémoire_ ;
- ⚠️ _Erreur de précision_ ;
- 🔄 _Effet de bord : modifier les paramètres dans la fonction_ ;

---

## 📌 Conclusion

- 🎯 Bonne idée de la qualité du code source ;
  - 🔄 Bon niveau de **maintenabilité**.
  - ⚠️ Mais NE montre PAS que le code est correct ;
- 🏆 **Efficaces** mais **coûteuses** en RH ;
- 🛠️ Pas besoin d'outillage particulier ;

---

