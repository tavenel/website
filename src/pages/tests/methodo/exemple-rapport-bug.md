---
title: Rapport de bug
---

# Exemple de rapport de bug

Sommaire: Dans le CTR (taux de clics), le calcul de la ligne 'Total' est incorrect

- Produit: `Exemple de produit`
- Version: `1.0`
- Plate-forme: `PC`

- URL: _(Fournissez l'URL de la page où le bug se produit)_
- OS / Version: `Windows 2000`

- Statut: `NOUVEAU`
- Gravité: `Majeur`
- Priorité: `P1`
- Composant: `Statistiques de l'éditeur`

- Assigné à: <developer@example.com>
- Rapporté par: <tester@example.com>
- DC: <manager@example.com>

## Description du bug

### Reproduisez les étapes

1. Aller à la page: _(Fournissez l'URL de la page où le bug se produit)_
2. Cliquez sur le lien `Statistiques de l'éditeur` pour afficher les statistiques détaillées sur les revenus de l'éditeur par date.
3. Sur la page _(indiquez l'URL de la page où le bug se produit)_, vérifiez la valeur CTR dans la ligne `Total` du tableau des statistiques CTR.

### Résultat réel

- Le calcul de la ligne `Total` dans le tableau CTR est incorrect.
- De plus, le CTR de ligne individuel pour chaque éditeur n'est pas tronqué à 2 chiffres après la virgule décimale.
- Il affiche un CTR comme `0,042556767`.

### Résultat attendu

- CTR total = `(Nombre total de clics / Nombre total de recherches) * 100`

_[Joindre une capture d'écran du bug le cas échéant]_

