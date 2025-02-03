---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Tests statiques
keywords:
- tests
- revue
---

<!-- _backgroundColor: "#000" -->
<!-- _color: "red" -->

# Présentation des tests statiques

_Tom Avenel_

<https://www.avenel.pro/>

---

<!-- _class: titre -->
# Les tests statiques

---

## Tests statiques vs dynamiques

- **Tests dynamiques** : nécessitent l'exécution du logiciel testé ;
- **Tests statiques** : examen manuel (_revues_) ou évaluation outillée (_analyse statique_) sans exécuter le code.

---

### Exemples

- Systèmes critiques : _aéronautique, médical, ..._
- Très démocratisé : _IDE, CI_
- Tout type de livrable : _spécifications, code, manuel utilisateur, page Web, ..._

---

## Avantages

- **Prévention** des défauts de conception ou de codage ;
  + **Difficulté** à trouver les défauts **dynamiquement** ;
  + Détection et correction **plus efficace** **avant** les tests dynamiques

---

## Avantages

- Meilleure productivité du développement :
  + **Meilleure conception** et **code plus facile à maintenir** ;
  + **Réduction** des coûts et des délais de **développement** ;
  + **Réduction** des coûts et des délais des **tests** ;

---

## Avantages

- Amélioration de la **communication** dans l'équipe : _revues_.

---

<!-- _class: titre -->
# La revue de code

---

# Principe

- Faire relire le code source par une ou plusieurs personnes autres que celles qui l’ont codé ;
- Réalisées par des _développeurs_ ;
- Éventuellement assistés de _testeurs_ des équipes _Qualité_, _Sûreté de Fonctionnement_, ... ;

---

- Fait partie du **contrôle de la qualité**.
- Adaptable à d'**autres livrables** : _spécifications, modèles, ..._

---

# Objectifs

- Vérifier le respect de certains **standards** de codage :
  + Généraux ;
  + Propres à l'équipe / l'entreprise ;
  + Contraintes sur le système, ... ;
- Identifier des pratiques de programmation **suspectes** ;
- Si **connaissance du métier**, peut détecter des **erreurs fonctionnelles**.

---

# Exemples de vérifications

- _Nombre de commentaires_ ;
- _Code structuré_ ;
- _Constantes_ ;
- _Longueur des fonctions_ ;
- _Décision exprimée simplement_ ;

---

- _Boucles lisibles_ : `while i < max` vs `while i != max` ;
- _Variable initialisée_ ;
- _Division par zéro_ ;
- _Indice sortant du tableau_ ;
- _Fichier non fermé_ ;
- _Fuite mémoire_ ;
- _Erreur de précision_ ;
- _Effet de bord : modifier les paramètres dans la fonction_ ;

---

# Conclusion 

- Bonne idée de la qualité du code source ;
  + Bon niveau de **maintenabilité**.
  + Mais NE montre PAS que le code est correct ;
- **Efficaces** mais **coûteuses** en RH ;
- Pas besoin d'outillage particulier ;

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
