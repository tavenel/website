---
license: © 2026 Tom Avenel under 󰵫  BY-SA 4.0
title: Exercice - Construire et interpréter un diagramme de Kano
tags:
- kano
type: exo
sidebar:
  order: 10
description: Exercice - Construire et interpréter un diagramme de Kano
---
## Une plateforme de services pour les équipes techniques

Une DSI souhaite mettre en place **Forge**, un portail interne en libre-service destiné aux développeurs et aux administrateurs systèmes.

L’objectif est de réduire les demandes manuelles adressées à l’équipe plateforme et de rendre les opérations courantes plus rapides, traçables et reproductibles. Depuis Forge, un utilisateur pourrait notamment demander un environnement, consulter l’état des services ou déclencher certaines opérations autorisées.

Une première phase de cadrage a fait émerger les fonctionnalités suivantes :

| Code | Fonctionnalité envisagée |
|---|---|
| F1 | **Disponibilité du portail** : le portail est accessible pendant les plages de service annoncées. |
| F2 | **Authentification centralisée** : connexion via le SSO de l’organisation. |
| F3 | **Contrôle des droits** : chaque utilisateur ne peut déclencher que les opérations autorisées pour son rôle. |
| F4 | **Journal d’audit** : les opérations sensibles sont horodatées et attribuées à leur auteur. |
| F5 | **Provisionnement automatisé** : création d’un environnement de développement à partir d’un modèle en quelques minutes. |
| F6 | **Retour de progression** : affichage de l’état d’une opération longue (en attente, en cours, terminée, en échec). |
| F7 | **Notifications proactives** : notification lorsqu’une opération se termine ou nécessite une intervention. |
| F8 | **Annulation d’une opération** : possibilité d’annuler une opération encore réversible. |
| F9 | **Tableau de bord personnalisé** : vue synthétique des environnements et services pertinents pour l’utilisateur. |
| F10 | **Suggestions intelligentes** : recommandations de ressources ou de paramètres en fonction du contexte d’utilisation. |

Une enquête exploratoire a été menée auprès de **30 utilisateurs** (développeurs, administrateurs systèmes et membres de l’équipe plateforme). Les réponses ont été agrégées et codées selon la grille Kano présentée ci-dessous.

## Rappel : principe du modèle de Kano

Le modèle de Kano étudie la relation entre la présence d’une caractéristique et la satisfaction de l’utilisateur. Une fonctionnalité n’est donc pas simplement « utile » ou « inutile » : son effet dépend de la manière dont elle répond à une attente.

Les cinq catégories principales sont :

- **M — Must-be / besoin de base** : son absence provoque une forte insatisfaction ; sa présence est considérée comme normale et ne crée pas nécessairement de satisfaction supplémentaire.
- **O — One-dimensional / performance** : plus la fonctionnalité est performante, plus la satisfaction augmente ; son absence ou sa mauvaise qualité insatisfait.
- **A — Attractive / attractivité** : une fonctionnalité inattendue qui augmente la satisfaction lorsqu’elle existe, mais dont l’absence n’est pas pénalisante.
- **I — Indifferent / indifférent** : sa présence ou son absence change peu la satisfaction.
- **R — Reverse / inverse** : une partie des utilisateurs préfère l’absence de la fonctionnalité ou considère sa présence comme gênante.
- **Q — Questionable / douteux** : combinaison de réponses incohérente ou ambiguë ; elle doit être examinée, et non interprétée comme un besoin.

Les catégories M, O et A constituent généralement les résultats les plus directement exploitables. I, R et Q sont également importantes : elles évitent de développer des fonctions qui n’apporteraient pas de valeur à une partie des utilisateurs, voire leur nuiraient.

### Les deux questions à poser

Pour chaque fonctionnalité, le questionnaire Kano comporte deux questions symétriques :

- **Question fonctionnelle : la fonctionnalité est présente :** si Forge proposait la fonctionnalité, comment vous sentiriez-vous ?
- **Question dysfonctionnelle : la fonctionnalité est absente** : si Forge ne proposait pas la fonctionnalité, comment vous sentiriez-vous ?

Pour chacune, le répondant choisit une seule réponse :

1. J’aime cela.
2. C’est normal / je m’y attends.
3. Cela m’est égal.
4. Je peux faire avec.
5. Je n’aime pas cela.

Les réponses aux deux questions sont croisées dans une matrice d’évaluation Kano. Le croisement attribue une catégorie A, O, M, I, R ou Q.

### Matrice d’évaluation Kano

Les lignes correspondent à la réponse à la question fonctionnelle (fonctionnalité présente) et les colonnes à la réponse à la question dysfonctionnelle (fonctionnalité absente).

| Présente \\ Absente | J’aime | Attendu | Indifférent | Je peux faire avec | Je n’aime pas |
|---|---:|---:|---:|---:|---:|
| **J’aime** | Q | A | A | A | O |
| **Attendu** | R | I | I | I | M |
| **Indifférent** | R | I | I | I | M |
| **Je peux faire avec** | R | I | I | I | M |
| **Je n’aime pas** | R | R | R | R | Q |

> **Attention :** les libellés de réponse doivent être strictement identiques dans les deux questions et dans la matrice. Une réponse Q peut signaler une incompréhension, une formulation ambiguë ou une réponse inattentive.

## Travail demandé

### Préparer le questionnaire

1. Pour F1 à F10, rédigez les deux questions Kano : une question fonctionnelle et une question dysfonctionnelle.
2. Vérifiez que chaque fonctionnalité est formulée de manière compréhensible et suffisamment indépendante des autres.
3. Identifiez une formulation qui pourrait biaiser les réponses et proposez une reformulation neutre.

### Classer les résultats

Le tableau ci-dessous présente, pour chaque fonctionnalité, le nombre de réponses classées dans chacune des catégories Kano après croisement des réponses individuelles.

**Consigne :** pour chaque fonctionnalité, identifiez la catégorie dominante en retenant celle qui obtient le plus grand nombre de réponses. En cas d’égalité, signalez le résultat comme ambigu et expliquez pourquoi il serait imprudent de trancher sans examiner les réponses individuelles.

| Fonction | A | O | M | I | R | Q |
|---|---:|---:|---:|---:|---:|---:|
| F1 — Disponibilité du portail | 2 | 3 | 21 | 2 | 1 | 1 |
| F2 — Authentification SSO | 3 | 5 | 16 | 4 | 1 | 1 |
| F3 — Contrôle des droits | 2 | 4 | 20 | 2 | 1 | 1 |
| F4 — Journal d’audit | 5 | 9 | 8 | 6 | 1 | 1 |
| F5 — Provisionnement automatisé | 12 | 11 | 2 | 3 | 1 | 1 |
| F6 — Retour de progression | 4 | 18 | 3 | 4 | 1 | 0 |
| F7 — Notifications proactives | 10 | 7 | 2 | 9 | 1 | 1 |
| F8 — Annulation d’une opération | 7 | 13 | 5 | 3 | 1 | 1 |
| F9 — Tableau de bord personnalisé | 8 | 5 | 2 | 13 | 1 | 1 |
| F10 — Suggestions intelligentes | 11 | 3 | 1 | 12 | 2 | 1 |

*Chaque ligne totalise 30 réponses.*

### Construire le diagramme

Construisez un diagramme de Kano à partir de vos classifications.

Pour cet exercice, utilisez une représentation qualitative à deux axes :

- **Axe horizontal :** niveau de satisfaction lorsque la fonctionnalité est présente, de faible à élevé.
- **Axe vertical :** niveau d’insatisfaction lorsque la fonctionnalité est absente, de faible à élevé.

Placez chaque fonctionnalité dans la zone correspondant à sa catégorie dominante :

- **M** : faible gain de satisfaction lorsque la fonction est présente, forte insatisfaction lorsqu’elle est absente ;
- **O** : satisfaction et insatisfaction évoluent toutes deux fortement ;
- **A** : fort gain de satisfaction lorsque la fonction est présente, faible insatisfaction lorsqu’elle est absente ;
- **I** : faible effet dans les deux situations ;
- **R** : effet inverse pour une partie significative des répondants ;
- **Q** : résultat douteux, à isoler plutôt qu’à placer comme une catégorie de besoin.

Vous pouvez réaliser le diagramme à la main ou avec un outil de votre choix. Ajoutez le code et le nom de chaque fonctionnalité.

### Interpréter et décider

En vous appuyant sur vos résultats, répondez aux questions suivantes :

1. Quelles fonctionnalités doivent être considérées comme des prérequis de lancement ?
2. Quelles fonctionnalités pourraient différencier Forge et augmenter la satisfaction ?
3. Quelles fonctionnalités semblent surtout relever de la performance opérationnelle ?
4. Pour quelles fonctionnalités faudrait-il recueillir davantage d’informations ?
5. Faut-il développer F10 (suggestions intelligentes) avant F1 (disponibilité du portail) ? Justifiez votre réponse.
6. Proposez un ordre de priorité pour un premier incrément produit. Votre proposition doit prendre en compte la catégorie Kano, les risques opérationnels et les dépendances techniques.

### Prendre du recul

Citez au moins trois limites du résultat obtenu. Vous pouvez notamment examiner :

- la représentativité de l’échantillon ;
- les différences entre développeurs et administrateurs systèmes ;
- la formulation des questions ;
- le caractère évolutif des attentes ;
- la différence entre importance déclarée et usage réel ;
- les contraintes de sécurité, de conformité et d’exploitation qui ne sont pas mesurées par Kano.

:::correction

## Questionnaire

Exemples de formulations neutres. Il est possible d’améliorer le style, à condition de conserver une question fonctionnelle et une question dysfonctionnelle symétriques.

| Code | Question fonctionnelle | Question dysfonctionnelle |
|---|---|---|
| F1 | Si Forge était accessible pendant les plages de service annoncées, comment vous sentiriez-vous ? | Si Forge n’était pas accessible pendant ces plages, comment vous sentiriez-vous ? |
| F2 | Si vous pouviez vous connecter à Forge avec le SSO de l’organisation, comment vous sentiriez-vous ? | Si vous ne pouviez pas utiliser le SSO et deviez vous authentifier autrement, comment vous sentiriez-vous ? |
| F3 | Si Forge appliquait des droits adaptés à votre rôle pour chaque opération, comment vous sentiriez-vous ? | Si Forge ne contrôlait pas les droits selon votre rôle, comment vous sentiriez-vous ? |
| F4 | Si les opérations sensibles étaient journalisées avec leur auteur et leur horodatage, comment vous sentiriez-vous ? | Si ces opérations n’étaient pas journalisées de cette manière, comment vous sentiriez-vous ? |
| F5 | Si Forge créait automatiquement un environnement à partir d’un modèle en quelques minutes, comment vous sentiriez-vous ? | Si vous deviez créer cet environnement manuellement, comment vous sentiriez-vous ? |
| F6 | Si Forge affichait l’état d’avancement des opérations longues, comment vous sentiriez-vous ? | Si Forge n’affichait pas cet état d’avancement, comment vous sentiriez-vous ? |
| F7 | Si Forge vous notifiait lorsqu’une opération se termine ou nécessite votre intervention, comment vous sentiriez-vous ? | Si Forge ne vous envoyait pas ces notifications, comment vous sentiriez-vous ? |
| F8 | Si vous pouviez annuler une opération tant qu’elle est réversible, comment vous sentiriez-vous ? | Si vous ne pouviez pas annuler une opération encore réversible, comment vous sentiriez-vous ? |
| F9 | Si Forge affichait un tableau de bord adapté à vos environnements et services, comment vous sentiriez-vous ? | Si Forge ne proposait pas de tableau de bord personnalisé, comment vous sentiriez-vous ? |
| F10 | Si Forge suggérait des ressources ou paramètres adaptés à votre contexte, comment vous sentiriez-vous ? | Si Forge ne proposait pas ces suggestions, comment vous sentiriez-vous ? |

**Point de vigilance :** F3 ne doit pas être formulée comme « si Forge était sécurisé », car le terme est trop large et peut déclencher des réponses émotionnelles ou socialement attendues. Il faut décrire le comportement observable : contrôle des autorisations selon le rôle.

## Classification

La catégorie dominante est celle dont l’effectif est le plus élevé sur la ligne.

| Fonction | Catégorie dominante | Lecture |
|---|---|---|
| F1 — Disponibilité du portail | **M** | La disponibilité est un prérequis : son absence est fortement pénalisante. |
| F2 — Authentification SSO | **M** | Les utilisateurs s’attendent à une authentification intégrée et cohérente avec le SI. |
| F3 — Contrôle des droits | **M** | Le contrôle d’accès est un besoin de base et une exigence de sécurité. |
| F4 — Journal d’audit | **O** | La traçabilité apporte une valeur croissante et son insuffisance peut être pénalisante. |
| F5 — Provisionnement automatisé | **A** | L’automatisation rapide constitue un facteur d’attractivité dans ce contexte. |
| F6 — Retour de progression | **O** | La qualité du suivi influe directement sur l’expérience d’utilisation. |
| F7 — Notifications proactives | **A** | Elles apportent un bénéfice appréciable, sans être indispensables à tous. |
| F8 — Annulation d’une opération | **O** | La capacité à reprendre le contrôle d’une opération améliore la satisfaction. |
| F9 — Tableau de bord personnalisé | **I** | La personnalisation n’apporte pas de valeur nette à la majorité de l’échantillon. |
| F10 — Suggestions intelligentes | **I** | Le résultat est partagé entre attractivité et indifférence ; la catégorie dominante est I, de peu. |

**Vérification des cas particuliers :**

- F10 obtient 12 réponses I et 11 réponses A. I est bien la catégorie dominante, mais l’écart est faible : il ne faut pas conclure que les suggestions sont inutiles pour tous.
- Les réponses R et Q sont minoritaires dans cet échantillon. Elles ne doivent pas être ignorées : elles peuvent révéler des profils d’utilisateurs pour lesquels une fonction est gênante, ou des questions mal comprises.
- Une catégorie dominante ne signifie pas que tous les répondants partagent le même avis. Il faut conserver la distribution complète pour interpréter le résultat.

## Diagramme attendu

Représentation qualitative attendue :

```text
Insatisfaction si la fonctionnalité est absente
Élevée
  ^
  |
  |   M : F1, F2, F3       O : F4, F6, F8
  |
  |
  |                         A : F5, F7
  |
  |   I : F9, F10
  +--------------------------------------------> Satisfaction si la fonctionnalité est présente
      Faible                                  Élevée

R : réponses inverses minoritaires, à analyser par segment
Q : réponses douteuses minoritaires, à vérifier
```

Ce schéma est une **carte qualitative des catégories**, pas un graphique statistique calculé à partir de mesures continues. Il sert à visualiser la logique du modèle. Les positions exactes à l’intérieur des zones ne peuvent pas être déduites des seuls effectifs catégoriels fournis.

## Interprétation et priorisation

### Prérequis de lancement

F1 (disponibilité), F2 (SSO) et F3 (contrôle des droits) sont classées M.

Elles doivent être traitées comme des conditions de crédibilité et de fonctionnement du service, avant de rechercher des effets différenciants. Pour F3, la sécurité ne doit pas être arbitrée uniquement sur la satisfaction : le contrôle des autorisations relève également de la maîtrise du risque et des exigences de sécurité du SI.

### Facteurs d’attractivité

F5 (provisionnement automatisé) et F7 (notifications proactives) sont classées A.

F5 peut réduire sensiblement les délais de mise à disposition et la charge de l’équipe plateforme. F7 peut améliorer le confort d’usage et éviter aux utilisateurs de surveiller manuellement une opération. Ces fonctions peuvent différencier Forge, mais leur absence n’est pas nécessairement rédhibitoire au lancement.

### Facteurs de performance

F4 (journal d’audit), F6 (retour de progression) et F8 (annulation) sont classées O.

Leur niveau de qualité compte : une journalisation incomplète, un suivi peu fiable ou une annulation qui ne fonctionne que dans de rares cas peut dégrader l’expérience. Pour F4, la valeur dépend aussi des besoins d’exploitation, d’investigation et de conformité.

### Fonctions à investiguer

F9 et F10 sont classées I dans l’échantillon. Il serait raisonnable de différer leur développement, ou de tester des prototypes avant d’investir.

F10 mérite une attention particulière : les réponses A (11) sont presque aussi nombreuses que les réponses I (12). Une segmentation par métier ou par fréquence d’utilisation pourrait révéler un intérêt réel chez certains profils. Il faut donc éviter une conclusion générale trop forte.

### Faut-il développer F10 avant F1 ?

Non, pas sur la base de ces résultats. F1 est un besoin de base : une indisponibilité du portail compromet l’ensemble du service. F10 est majoritairement indifférente dans l’échantillon. En outre, une fonction de suggestion ne compense ni une plateforme indisponible ni un contrôle d’accès insuffisant.

### Exemple d’ordre de priorité pour un premier incrément

| Priorité | Fonctionnalités | Justification |
|---|---|---|
| **P0 — Socle de lancement** | F1, F2, F3 | Besoins de base, disponibilité et sécurité. |
| **P1 — Exploitabilité et expérience fiable** | F4, F6 | Traçabilité et visibilité sur les opérations ; importantes pour l’exploitation quotidienne. |
| **P2 — Valeur opérationnelle** | F5, F8 | Automatisation et contrôle des opérations ; forte valeur, avec des dépendances techniques et des exigences de sûreté. |
| **P3 — Confort et différenciation** | F7 | Amélioration de l’expérience, potentiellement livrable après le socle. |
| **À réévaluer** | F9, F10 | Valeur incertaine dans l’échantillon ; prototype, expérimentation ou report. |

Cet ordre est une proposition argumentée, pas une conséquence mécanique de Kano. Par exemple, F5 peut remonter en priorité si le provisionnement manuel constitue le principal goulot d’étranglement de la DSI. À l’inverse, F8 exige une conception prudente : toutes les opérations ne sont pas annulables sans risque, et l’annulation doit être explicitement limitée aux étapes réversibles.

## Limites et précautions

Plusieurs limites doivent être mentionnées :

1. **Taille et représentativité de l’échantillon.** Trente répondants permettent une première exploration, mais ne garantissent pas une représentation fiable de toutes les équipes, pratiques et contraintes.
2. **Agrégation des profils.** Développeurs, administrateurs systèmes et équipe plateforme n’ont pas nécessairement les mêmes priorités. Une moyenne globale peut masquer des besoins opposés.
3. **Biais de formulation.** Une fonctionnalité décrite comme « intelligente », « rapide » ou « sécurisée » peut orienter les réponses. Il faut décrire un comportement concret et éviter les formulations valorisantes.
4. **Déclaration versus comportement.** Une préférence déclarée ne prédit pas parfaitement l’usage réel. Des tests de prototype, des mesures d’usage et des entretiens sont nécessaires.
5. **Évolution des attentes.** Une fonction attractive aujourd’hui peut devenir un besoin de base après sa généralisation chez les concurrents ou dans l’organisation.
6. **Contraintes non couvertes.** Kano ne mesure pas directement le coût, la complexité, la dette technique, les risques de sécurité, la maintenabilité, les dépendances d’architecture ou les exigences réglementaires.
7. **Perte d’information par la catégorie dominante.** Retenir uniquement la catégorie la plus fréquente masque la dispersion des réponses. F10 illustre ce problème.
8. **Réponses douteuses et inverses.** Les réponses Q et R doivent être examinées. Elles peuvent signaler une incompréhension, une préférence minoritaire réelle ou une fonctionnalité mal conçue.

:::
