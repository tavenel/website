---
title: IA
created: 2026-02-12
checked: 2026-02-12
---

## Prompts

### Générer un bon prompt

- Rôle, contexte, résultat attendu, objectif, contraintes, format
  - _"avant de répondre, pose-moi toutes les questions nécessaires pour optimiser ta réponse"_
  - _"si tu ne sais pas, dis-le moi et n'invente rien"_

- <https://blog.shevarezo.fr/post/2025/12/10/astuces-meilleures-reponses-chatgpt>

### Types de prompts IA

- _zero-shot_ => pas de contexte
- _few shots_ => contexte par exemples
- _chain of thought_ => "let's think …" (step-by-step example)
- _RAG_ (retrieval augmented generation) => élévation de contexte par vecteur de contexte
- _agents_ => conscience de l'environnement

## Agents

- <https://cursor.com/blog/agent-best-practices>

### MCP

- MCP best practices from Horacio Gonzalez : [blog](https://lostinbrittany.dev/en/building-smarter-mcp-servers-from-theory-to-practice/) et [slides](https://lostinbrittany.dev/talks/2026/2026-01-16_SnowCamp_MCP-Servers-Good-Practices-Design-Choices-and-Consequences/) :
  - Narrow, named capabilities : each tool should read like a product verb: `getMonsterByName`, `listMonstersByType`, `compareMonsters`.
  - Stable types in/out : explicit schemas (IDs, enums, unions) so the agent can plan reliably.
  - Deterministic behavior : same inputs → same outputs; include `idempotencyKey` when making state changes.
  - Least privilege : tools do one thing; internal queries/side-effects are not exposed.
  - Guardrails at the edge : validate inputs, clamp result sizes, redact PII, enforce authZ inside the server
  - Make the LLM succeed on the first try : types (union, enum), limits, idempotency
  - Always return a **machine part** and a **human part**
- Turn _tasks_ into MCP _tools_/_resources_/_prompts_ :
  - **Tools** (actions) :
    - Read: `getMonsterByName(name) -> Monster`
    - List: `listMonstersByType(type, limit=25, cursor?) -> {items:[Monster], nextCursor}`
    - Search: `searchMonsters(q, limit=10) -> [MonsterSummary]`
  - **Resources** (documents/URIs the client can browse/fetch) :
    - `ragmonsters://schema/Monster` (JSON schema for types)
    - `ragmonsters://docs/query-tips` (compact usage notes)
    - `ragmonsters://images/{monsterId}` (read-only asset stream)
  - **Prompts** (reusable instructions/templates) :
    - `prompt://ragmonsters/answering-style` (tone, do/don't)
    - `prompt://ragmonsters/disambiguation` (ask for missing fields first)

## Utiliser l'IA en formation

Idées d'utilisation de l'IA :

- Générer une réponse par IA, puis l'apprenant fait une critique de la réponse.
- Demander le cheminement : brouillon, suite, …
- Créer un chatbot dédié au cours pour anticiper l'envoi des cours sur chatgpt
- Faire une démo en tant que formateur d'un bon usage de l'IA pour créer le cours
- Moteur d'IA local au campus

Amener la discussion sur l'IA avec les étudiants pour que cela ne soit pas tabou.

### Règles sur l'utilisation de l'IA générative en cours

Objectif : clarifier les règles IA pour les projets et rendus.

- Sauf mention contraire dans le sujet ou pendant les heures de formation, l'utilisation d'IA est à modérer fortement
  - n'hésitez pas à demander au formateur ce qui est intéressant à faire générer par une IA et ce qui mérite réflexion
  - vous pouvez inclure vos interactions pertinentes (prompts, …) avec les outils d'IA dans le rapport afin d'aider à valider vos compétences
- Vous devez toujours être en capacité d'expliquer 100% de vos rendus, y compris les productions éventuelles d'autres apprenants
- Aucun détecteur d'IA n'est utilisé pour la correction car ceux-ci ne sont pas fiables
  - donc protégez votre proriété intellectuelle et ne soumettez pas vos travaux à ces outils (`zeroGPT`, …) !
- Enfin, vous êtes en mission d'apprentissage : il serait dommage de ne pas profiter de ce temps mis à votre disposition pour monter en compétences

## Les différents types d'apprentissage

- **Apprentissage supervisé** : le modèle apprend à partir de données **étiquetées** (avec réponses connues) pour prédire une sortie lors de nouvelles données.
  - en principe : 80% des données pour l'apprentissage
    - parfois : 20% des données d'apprentissage utilisées en données de **validation** utilisées pour le réglage de l'algorithme pendant l'entraînement, mais pas pour ajuster directement les poids du modèle. Servent à ajuster les **hyperparamètres** : profondeur d'un arbre, taux d'apprentissage d'un réseau de neurones, … ; à décider de l'arrêt de l'entraînement (_early stopping_) ; à comparer plusieurs modèles candidats.
  - 20% pour le test (jamais vues pendant l'entraînement ni pendant la validation, mesurent (impartial) la performance réelle du modèle sur des données nouvelles).
- **Apprentissage non supervisé** : le modèle apprend à partir de données **non étiquetées** et cherche à découvrir (seul) des structures cachées (groupes, similarités, réductions de dimensions).

```
Jeu de données complet
        │
        ├── 70-80 % → Données d'entraînement (train set)
        │              - Utilisées pour ajuster les poids/paramètres du modèle
        │
        ├── 10-15 % → Données de validation (validation set)
        │              - Servent à régler les hyperparamètres
        │              - Aident à éviter le surapprentissage (early stopping)
        │
        └── 10-15 % → Données de test (test set)
                       - Jamais vues avant
                       - Utilisées uniquement pour l'évaluation finale
```

:::link

- Voir aussi le cours sur [le data mining](/data/mining/cours)

:::

## Liens

- <https://www.comparia.beta.gouv.fr/>
- <https://tugaleres.com/2025/03/04/est-on-plus-efficace-en-utilisant-une-ia-type-chatgpt/>
- <https://github.com/microsoft/AI-For-Beginners> : Cours gratuits Microsoft
- Impact des IA génératives sur les étudiants :
  - <https://open.devinci.fr/ressource/etude-2024-impact-ia-generatives-etudiants/>
  - <https://www.newcartographies.com/p/the-myth-of-automated-learning>
- [Les sacrifiés de l'IA (Henri Poulain)](https://www.francetvinfo.fr/replay-radio/info-medias/les-sacrifies-de-l-ia-dans-son-documentaire-henri-poulain-revele-les-coulisses-d-une-industrie-qui-exploite-la-misere-humaine_7038260.html)
- [UX : Comment les entreprises de la tech nous forcent à utiliser l'IA](https://limitesnumeriques.fr/travaux-productions/ai-forcing)
- <https://blog.wescale.fr/back-to-basics-pere-castor-raconte-moi-le-prompt-engineering>
- Local AI LLMs : <https://ollama.com/> et <https://docs.openwebui.com/>
  - `tinyllama`, `tinydolphin`, `dolphin-mistral`, `codestral`, …
- Block AI indexing in your website : <https://github.com/ai-robots-txt/ai.robots.txt>
- ["Encadrer l'utilisation de l'IA dans les devoirs à la maison" (Académie de Grenoble, PDF)](https://dane.web.ac-grenoble.fr/sites/default/files/Media/document/IA%20devoirs_Ac-Paris.pdf)
- <https://korben.info/linus-torvalds-ia-vibe-coding-pragmatisme-dev.html>
- <https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing>

