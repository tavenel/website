---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Modèles de déploiements continus
keywords:
- ci
---

<!-- _class: titre lead -->

# Modèles de déploiements continus

_Tom Avenel_

<https://www.avenel.pro/>

---

# Différents modèles

Bug détecté en production :

- Attendre la livraison d'un correctif ?
- Faire un rollback vers la version précédente ?
- Quelle stratégie de déploiement pour adresser ces problèmes ?

---

# Blue-Green Deployment

- Déploiement _zero-downtime_
- 2 productions identiques
- Un routeur aiguille les utilisateurs vers l'un des 2 sites
- Mise à jour d'un site puis l'autre

---

## Avantages

\+ Implémentation est facile et rapide (Cloud)
\+ Rollback possible en utilisant le second site
\+ Tests dans environnement identique à la production

## Inconvénients

\- Coûts et maintenance supérieurs : 2 sites

---

# Canary Release

- Similaire _Blue-Green_
- Seule un petit pourcentage aléatoire des utilisateurs migre sur la nouvelle version
- Utile si peu de confiance sur la nouvelle version
  * surveiller le panel d'utilisateurs sur le nouveau site
  * migrer petit à petit tous les utilisateurs

---

# Ring Based Deployment

- Similaire _Canary Release_ mais le public test est un public ciblé :
  * experts du domaine
  * public impacté par le changement
  * ...

---

# Feature Flags

- Le code est modifié pour (dés)activer les fonctionnalités au déploiement ou dynamiquement :
  * difficile en dev si non prévu dès le début du projet
  * grande liberté de déploiement : morceaux de fonctionnalités non terminées

---

# Dark Launch

- _Ring-Based Deployment_ et _Feature Flags_ combinés :
- nouvelle fonctionnalité activée uniquement pour panel précis
- ajustement des déploiements suite aux retours du panel
- migration des autres utilisateurs

---

# Test A/B

- 2 versions concurrentes sont déployées
- chaque utilisateur est aiguillé aléatoirement sur l'un des sites
- seule la version la "meilleure" (moins de bug, meilleurs retours clients, ...) est gardée

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
