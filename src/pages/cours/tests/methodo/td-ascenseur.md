---
title: Tests d'ascenseur
---

# Tests d'un contrôleur d'ascenseur

## Présentation du contexte

On fait appel à vous pour tester un contrôleur d'ascenseur.

Comme il s'agit du début du projet avec une équipe sans expérience avec ce genre de système, il est décidé de construire une simulation en Java afin de valider la conception du contrôleur.

On vous livre une implémentation du simulateur d'ascenseur en Java et on vous demande d'en effectuer le test.

Une spécification en langue naturelle du contrôleur d'ascenseur est fournie ci-dessous.

## Spécification - comportement local

### Les portes

#### Variables

- `étage` : l'étage de la porte

#### Comportement

- Attendre que l'ascenseur soit à l'arrêt à l'étage de la porte.
- Ouvrir la porte.
- Attendre un certain laps de temps.
- Fermer la porte.
- Signaler à l'ascenseur qu'il peut redémarrer.

### Les usagers

#### Variables

- `étage` : l'étage courant de l'usager
- `direction` : la direction que l'usager veut emprunter
- `destination` : la destination de l'usager

#### Comportement

- Si un appel a été signalé au même étage en direction opposée :
  + Attendre ;
  + Sinon, appeler l'ascenseur.
- Attendre que la porte s'ouvre
- Décider d'entrer ou non (l'usager peut être distrait)
- Si la porte est encore ouverte, entrer dans l'ascenseur
- Entrer la destination
- Attendre que la porte se ferme
- Attendre que l'ascenseur soit à destination
- Attendre que la porte s'ouvre et sortir

### L'ascenseur

#### Variables

- `étage` : l'étage courant de l'ascenseur
- `direction` : la direction courante de l'ascenseur
- `destinations` : un vecteur des destinations entrées par les usagers
- `appels` : un vecteur des appels effectués par les usagers

#### Comportement

- Choisir la direction
  + Selon la direction courante, chercher un appel ou une destination vers le haut ou le bas
    * S'il n'y a aucune direction courante, commencer à chercher vers le haut
  + S'il existe un appel à l'étage courant, indiquer qu'il n'y a pas de direction courante
  + S'il existe un appel ou une destination vers la direction courante et que l'ascenseur n'est pas à l'étage le plus haut (respectivement le plus bas)
    * Maintenir la direction courante
    * Sinon, chercher pour un appel ou une destination dans la direction opposée
  + S'il existe un appel ou une destination dans la direction opposée et que l'ascenseur n'est pas à l'étage le plus bas (respectivement le plus haut)
    * Changer la direction à la direction opposée
    * Sinon, indiquer qu'il n'y a pas de direction courante
- Monter ou descendre d'un étage selon la direction
- Renverser la direction si l'ascenseur atteint l'étage le plus haut (respectivement le plus bas)
- Si le nouvel étage correspond à un appel ou une destination
- Effacer tout appel ou destination pour l'étage courant
- Signaler d'ouvrir la porte
- Attendre la fermeture de la porte

## Spécifications - comportement global

### Système

- Lorsque l'ascenseur est en mouvement, aucune porte n'est ouverte.
- Il est toujours vrai qu'un usager qui demande l'ascenseur y entrera fatalement
- Il n'y a jamais plus d'une porte ouverte à la fois.
- La distance parcourue par un usager est toujours égale à $|source - destination|$.

### Simplification

Exemple de simplification :

- Un seul ascenseur,
- Deux usagers au même étage demandent l'ascenseur : si leurs directions sont différentes, un usager attend.

## Exemple de trace d'exécution

0. # Usager[0]: # effectue l'appel 1-UP
1. # Usager[1]: # effectue l'appel 2-DOWN
2. + Ascenseur: + direction: UP
3. + Ascenseur: + Etage: 1
4. + Ascenseur: + arrêt a l‘étage 1
5. * Porte[1]: * ouverture
6. # Usager[0]: # entre ds l'ascenseur
7. # Usager[0]: # entre la destination 2
8. * Porte[1]: * fermeture
9. + Ascenseur: + fin de l'arrêt
10. + Ascenseur: + direction: UP
11. + Ascenseur: + Etage: 2
12. + Ascenseur: + arrêt à l‘étage 2
13. * Porte[2]: * ouverture
14. # Usager[0]: # destination atteinte
15. # Usager[1]: # entre ds l'ascenseur
16. # Usager[1]: # entre la destination 0
17. * Porte[2]: * fermeture
18. + Ascenseur: + fin de l'arrêt
19. + Ascenseur: + direction: DOWN
20. + Ascenseur: + Etage: 1
21. + Ascenseur: + direction: DOWN
22. + Ascenseur: + Etage: 0
23. + Ascenseur: + arrêt à l‘étage 0
24. * Porte[0]: * ouverture
25. # Usager[1]: # destination atteinte
