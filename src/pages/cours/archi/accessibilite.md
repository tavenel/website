---
marp: true
paginate: true
#footer: _© 2025 Tom Avenel under 󰵫  BY-SA 4.0_
title: Accessibilité
tags:
- accessibility
- rse
---

<!-- _class: titre lead -->

# Accessibilité

---

# Format texte

- Utiliser un format texte (pas de formats propriétaires type `Microsoft Word` ou `PDF`).

---

<!-- _class: titre lead -->

# Web

---

## CSS

- Utiliser des polices d'écriture standards
- Voir [le lien W3schools sur les Web Safe Fonts](https://www.w3schools.com/cssref/css_websafe_fonts.php)
- Limiter les ombres et dégradés (peu lisibles, coûteux en ressources).
- Limiter les animations

---

## Navigation

- Toute interface utilisateur doit être navigable au clavier
- Ajouter un feedback sur le focus actif
- Ajouter des attributs `aria-label` sur les boutons (screen reader).
- Faire de gros boutons et séparer les liens cliquables (utile également sur mobile).
- Souligner les liens hypertexte

---

## Semantic Web

- Utiliser du Web sémantique : `<header>`, `<main>`, `<footer>`, `<h1>`, ...
- Les `<div>` et `<span>` ne servent qu'à la mise en page (pas à donner du sens au contenu) !
- Pas de `<table>` sauf pour un vrai tableau de données
- Utiliser des `<button>` pour cliquer et des `<a>` pour les liens.
  - Décrire le bouton ou le lien avec précision

---

## Contraste

- Utiliser un contraste élevé
- Dupliquer les changements de contexte : par exemple, texte important en gras et couleur.

---

## Images

- Compresser les images et réduire leur taille
- Images lourdes : utiliser des [images responsive (developer.mozilla.org)](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
- Utiliser des `sprites` pour envoyer plusieurs images en une requête (moins utile en `HTTP/2`). [Voir la page developer mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Images/Implementing_image_sprites_in_CSS)
- Ajouter un champ de description alternatif `alt` et/ou un `role`.
- <https://kurtextrem.de/posts/modern-way-of-img>
- Voir [la page des développeurs Mozilla sur les rôles](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/img_role)


---

## Limiter JS

- Limiter la complexité du code JS (généralement peu accessible).
- Pour les sites très simples, utiliser un framework de site statique comme <https://gohugo.io/>
- [Lien Anybrowser : make your website work for everyone](https://anybrowser.org/campaign/)

---

<!-- _class: titre lead -->

# Application mobile

---

## Mobile-first

- Faire un site responsive en visant en priorité les interfaces les plus limitées

---

## Gestes complexes

- Prévoir une alternative aux gestes complexes (swipe, zoom à 2 doigts, ...)
- Laisser assez d'espace entre les différents éléments cliquables : [voir la norme WCAG](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html)

---

## Portrait vs paysage

- Supporter les interfaces **portrait** et paysage

---

<!-- _class: titre lead -->

# Tests

---

## Navigateur Web

- Utiliser les `devtools` pour simuler des situations de handicap :
  - liées aux couleurs;
  - liées à des réseaux instables et/ou bas débit.

---

## Outils CI

- Ajouter un outil de test automatique (`a11y`) dans le pipeline d'intégration continue
- Reprendre tests end-to-end (exemple : `Selenium`) et automatiser en utilisant le clavier plutôt que les sélecteurs CSS.

---

## Tests manuels

- Ajouter des tests manuels :
  - revues des balises `alt`, `role`, `aria-*`, ...
  - "vrai" test utilisateur

---

<!-- class: liens -->

# Liens

- Outil de vérification d'accessibilité (permet aussi d'enlever le CSS) : <https://wave.webaim.org>
- <https://www.a11yproject.com/>
- <https://testingaccessibility.com/>
- <https://www.w3.org/WAI/standards-guidelines/wcag/>
- <https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/>
- <https://github.com/marcysutton/testing-accessibility-demos>
- [aXe extension](https://www.deque.com/axe/)
- [aXe API pour Selenium](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/webdriverjs)
- [Liste de ressources](https://ideance.net/blog/467/accessibilite-ux-ui-design/)
- [Conférence de Sébastien DELORME : comprendre pourquoi et comment intégrer l’accessibilité numérique (Youtube)](https://www.youtube.com/watch?v=UA_kfsvi_dg)
- <https://drewdevault.com/2019/01/23/Why-I-use-old-hardware.html>
- Bon exemple : application mobile "Uber Drive" [App Store](https://apps.apple.com/fr/app/uber-commander-une-course/id368677368) et [Google Store](https://play.google.com/store/apps/details?id=com.ubercab&hl=fr&gl=US)
- Exemple de pire interface utilisateur (compilation de mauvaises pratiques) : <https://userinyerface.com/>

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
