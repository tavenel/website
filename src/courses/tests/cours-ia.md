---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/CoursePartLayout.astro'
title: Tester avec et pour l'Intelligence Artificielle
tags:
- tests
- IA
---

## Aider la génération de code

- Avoir une batterie de tests robuste permet d'aider une IA à générer du code plus facilement, en utilisant ces tests comme garde-fou.
- Une approche "test-first" (comme du TDD) permet d'obtenir un code métier de meilleure qualité.

---

## 🖥️ Tester avec l'IA

🎯 Comment utiliser l'IA pour tester du code et des applications ?

### Génération de tests unitaires

- L'IA peut lire une fonction et proposer des **tests unitaires** automatiquement : cas normaux, limites, erreurs.
  - par outil intégré **GitHub Copilot**, … : complète automatiquement des tests
  - par prompt **ChatGPT**, … : en copiant/collant du code et en demandant "génère les tests unitaires manquants".

### Automatisation de tests fonctionnels

- Objectif : au lieu d'écrire manuellement tous les scénarios Selenium/Playwright, décrire le scénario en langage naturel et l'IA génère le script de test automatisé.
  - Exemple : "Teste que l'utilisateur peut se connecter, ajouter un produit au panier et valider la commande."

### Analyse de couverture

- L'IA peut pointer les parties du code **non couvertes** par les tests existants et proposer des scénarios manquants.
  - Exemple : utiliser `coverage.py` ou `JaCoCo`, puis donner le rapport à lIA qui propose de nouveaux tests.

:::tip

- L'IA est particulièrement utile pour imaginer des entrées improbables : valeurs nulles, très grandes, caractères spéciaux, mauvais formats JSON, etc.

:::

### Tests exploratoires

- L'IA simule un utilisateur curieux : elle clique un peu partout, essaie des valeurs étranges, et détecte des bugs ou comportements inattendus. Cette stratégie était auparavant quasiment exclusivement manuelle.
- Des outils émergent dans ce domaine : **Mabl**, **Testim.io**, **AutonomIQ**.

### Vérification par prompt

- Faire interagir l'IA avec l'API ou l'application comme un **QA engineer virtuel**.
- L'IA envoie des requêtes, regarde les réponses et dit si elles sont conformes aux specs.

### Suggestions de correctifs

- L'IA analyse les erreurs de test et propose automatiquement une solution, soit :
  - une solution au problème de mise en place de l'environnement de test
  - un correctif applicatif dans le code

---

## Tester une IA générative (LLM)

Tests spécifiques pour une application utilisant une IA générative :

1. Principe général : séparer les données classifiées

- Une partie des données sert à l'entraînement du modèle
- Le reste des données (en général ~20%) sert à la validation du modèle (on compare les réponses du modèle sur ces données aux réponses attendues, par exemple pour un modèle de classification)

2. Tests de robustesse (input-output)

- Créer des jeux de prompts de référence (scénarios représentatifs, edge cases, inputs adversariaux).
- Évaluer si les réponses générées respectent les contraintes attendues (format, style, présence/absence de certains éléments).

3. Tests de non-régression sur données gelées

- Sauvegarder des paires input & output validés.
- Comparer les générations futures à ces sorties "acceptables" (en tolérant une variabilité, via règles ou scoring).

4. Tests basés sur des métriques automatiques

- Textuelles : BLEU, ROUGE, METEOR, BERTScore, perplexité.
- Images : FID, CLIPScore.
- Attention : ces métriques donnent une tendance mais ne suffisent pas seules.

5. Tests de conformité aux règles

- Absence de contenu interdit (toxicité, biais, hallucinations).
- Respect du format demandé (JSON bien formé, schéma valide, longueur max).
- Cohérence factuelle (via croisement avec bases de vérité ou modèles de vérification).
- Prompt injection attacks : vérifier que l'IA ne fuit pas de données sensibles ou n'exécute pas d'ordres interdits.

6. Évaluation humaine

- Tests manuels exploratoires : vérifier pertinence, créativité, clarté.
- Panels utilisateurs / experts : scorer la qualité sur critères définis (fidélité, utilité, sécurité).
- A/B testing : comparer plusieurs versions de modèle ou de réglages (température, prompt, fine-tuning).

---

## Métriques automatiques

- Les sorties d'une IA générative sont **non-déterministes** (variabilité due à la température, au sampling, etc.).
- On ne peut pas tester avec un simple `assert sortie == attendu`.
- Les métriques donnent un **score de similarité ou de qualité**, qui peut servir de seuil de validation ou d'indicateur de régression.

L'idée est de disposer de critères **quantitatifs et reproductibles** pour évaluer la qualité des générations de l'IA. Ces métriques ne remplacent pas l'évaluation humaine, mais elles permettent d'automatiser une partie des tests et de comparer différentes versions d'un modèle ou de prompts.

---

### Métriques pour le texte généré

1. **Basées sur les n-grammes** (comparaison avec une référence humaine) :

- **BLEU** (Bilingual Evaluation Understudy) : compare la proportion de n-grammes communs.
- **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation) : très utilisé en résumé automatique, mesure rappel et précision sur des séquences.
- **METEOR** : améliore BLEU en tenant compte de synonymes et de la flexibilité grammaticale.
- Exemple d'usage : comparer une réponse générée à un "gold standard" rédigé par un expert.

2. **Basées sur l'embedding sémantique** :

- **BERTScore** : calcule la similarité sémantique entre référence et génération via embeddings contextualisés (BERT, RoBERTa).
- **Cosine similarity** sur embeddings (par ex. OpenAI Embeddings, Sentence-BERT).
- Utile quand on veut évaluer la fidélité au sens plutôt qu'à la forme exacte.

3. **Basées sur la fluence du texte** :

- **Perplexité** : mesure la probabilité qu'un autre modèle de langage attribue à la génération (texte plus "naturel" = perplexité faible).
- Peut servir à détecter des textes incohérents ou artificiels.

---

### Métriques pour l'image générée

- **FID (Fréchet Inception Distance)** : compare la distribution des features entre images générées et vraies images.
- **IS (Inception Score)** : mesure la qualité et la diversité des images générées.
- **CLIPScore** : utilise CLIP pour mesurer la cohérence entre un texte (prompt) et une image générée.

---

### Stratégie pratique d'utilisation

1. **Définir un corpus de prompts de référence** (scénarios critiques, cas normaux, cas limites).
2. **Générer des sorties avec l'IA** et les comparer à :

- des **références humaines** (si disponibles),
- ou des **critères formels** (schéma, format).

3. **Calculer les métriques** (ex. BLEU, BERTScore, FID selon le type de contenu).

- fonctionnent mieux avec un **ensemble de sorties** (moyenne statistique) qu'au cas par cas.

4. **Fixer des seuils d'acceptabilité** (ex. BLEU ≥ 0.4 pour un résumé, perplexité ≤ 50 pour un texte cohérent).
5. **Surveiller les tendances** : comparer les scores entre versions de modèles ou de prompts pour détecter des régressions.
6. Compléter par :

- **règles de conformité** (format, sécurité),
- **tests humains** pour juger nuance, créativité, pertinence.

:::tip
En pratique, on conseille d'**orchestrer plusieurs métriques** en parallèle (par ex. BLEU + BERTScore + validation de format) pour obtenir une vision plus robuste.
:::

---

## Test de Retrieval-Augmented Generation (RAG)

Un **RAG (Retrieval-Augmented Generation)** combine deux briques :

1. **R (Retrieval)** : aller chercher les bons documents dans une base (vectorielle, index, moteur de recherche).
2. **AG (Augmented Generation)** : générer une réponse avec un LLM en s'appuyant sur ces documents.

Tester un RAG, c'est donc tester **à la fois la recherche et la génération** - et leur intégration.

---

### Retrieval

🎯 Objectif : vérifier que les bons documents sont bien retrouvés.

1. Tests unitaires :

- Vérifier que l'indexation fonctionne (documents bien ingérés, embeddings valides)
- Vérifier que le **schéma** (métadonnées, _chunks_) est respecté

2. Tests de qualité de recherche :

- Créer un **jeu de requêtes de référence** avec leurs documents attendus (_ground truth_).
- Mesurer la qualité avec des métriques de recherche d'information :

  - **Recall@k** (les bons documents apparaissent-ils dans le top-k résultats ?)
  - **Precision@k** (parmi les résultats, combien sont pertinents ?)
  - **MRR (Mean Reciprocal Rank)** (le premier document pertinent est-il bien classé en haut ?)

3. Tests de robustesse :

- Cas "difficiles" : synonymes, paraphrases, fautes de frappe.
- Cas piégés : requêtes ambiguës ou bruitées.

---

### Augmented Generation

🎯 Objectif : vérifier que le LLM produit une réponse correcte **à partir du contexte fourni**.

1. Conformité au format :

- La réponse respecte-t-elle le format attendu (JSON, liste, texte court) ?
- Validation automatique avec un schéma ou un parseur.

2. Pertinence et fidélité :

- **Fact-checking** : la réponse est-elle supportée par les documents fournis ?

  - Métriques possibles : **Faithfulness score** (_LLM-as-a-judge_ : utiliser un autre LLM comme correcteur automatique).
  - Vérification automatique : chaque phrase doit pouvoir être tracée à un _chunk_ (morceau de document).

3. Non-hallucination :

- Détecter les parties de la réponse qui n'ont aucun support dans les documents.
- Tests avec prompts adversariaux (questions hors contexte : le RAG doit répondre "je ne sais pas" ou rester neutre).

---

### Intégration R + AG

🎯 Objectif : vérifier que les deux briques s'assemblent correctement.

1. End-to-end testing : donner une question et observer la réponse.

2. Chaîne de traçabilité :

- Vérifier que la réponse cite ou référence les sources.
- Vérifier que les documents affichés à l'utilisateur correspondent vraiment à ceux utilisés en entrée du LLM.

3. Résilience aux erreurs :

- Que se passe-t-il si aucun document pertinent n'est trouvé ?
- Gestion du bruit (documents partiellement pertinents).
- Tests de charge (latence du retrieval + génération).

---
