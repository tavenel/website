---
title: Website
layout: '@layouts/CourseLayout.astro'
---

![](@assets/undraw/undraw_static-website_x3tn.svg)

## Accessibility

- This website targets primarily students from my teaching. It is also available for everyone else who has at least some basic computer science skills and wants to improve them.
- This website can be reached on a desktop or mobile device. It aims to be as accessible as possible, and usable on almost all Web client devices, including old smartphones or old computers.
- This website is optimized for a low-bandwith network. If not specified, each downloadable document is under 1M. PDF files are compressed and HTML and Markdown versions are shown first.
- Tested with <https://wave.webaim.org>.
- For more information, have a look to the [Accessibility][cours-rse] course.

## Accessibilité

- Ce site web vise principalement les apprenants de mes formations. Il est aussi disponible pour toute personne ayant des compétences de base en informatique et voulant améliorer ces dernières.
- Ce site web peut être utilisé depuis un PC de bureau ou un téléphone mobile (smartphone). Il est conçu dans le but d'être utilisable sur tout client Web, y compris d'anciens ordinateurs ou téléphones portables.
- Ce site web est optimisé pour une connexion bas débit. En absence d'indication, le document à télécharger fait moins de 1M. Les fichiers PDF sont compressés et les versions HTML et Markdown affichées en premier.
- Pour plus d'information sur l'accessibilité, voir le [cours sur l'accessibilité][cours-rse].

[cours-rse]: /cours/rse/index.html

## PWA

[![PWA Banner](@assets/website/pwa-enabled.svg)](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)

This website can be downloaded and installed on your device for offline use as a Progressive Web App.

To install, look for the "Add to Home Screen" option in the browser's menu or settings. On most mobile devices, this option can be found by visiting the website, then selecting the "Options" or "Menu" button in the browser, and searching for "Add to Home Screen." On some desktop browsers, you can install the PWA by right-clicking on the page and selecting "Install."

To uninstall, remove the PWA from your device's home screen.

The PWA uses the "_network-first, cache-second_" strategy : <https://developer.chrome.com/docs/workbox/caching-strategies-overview/>.

## Technology

This website is a lightweight Astro website : <https://astro.build/>.

It is a static website with very little JavaScript intended to be extremely fast, small and easy to change or copy.

- The whole website pages and deployment scripts are available as a git repo : <https://git.sr.ht/~toma/astro> or <https://github.com/tavenel/website>
- The website is hosted on <https://vercel.com/>.
- PageSpeed Insights (2023-10-13) [Details of analysis](https://pagespeed.web.dev/analysis/https-www-avenel-pro-promotions-esgi-esgi-b3-src-linux-lpic-1-html/g9fuj8pwm7?form_factor=desktop) : <span class="green">Performance:100%, Accessibility:100%, Best Practices:100%,SEO:100% (Mobile & Desktop)</span>
- W3 analysis : <https://validator.w3.org/nu/?doc=https%3A%2F%2Fwww.avenel.pro%2F>
- Covers come from the <https://undraw.co/> project.

## Generative AI

The content of this website is **not** created using a generative AI. Some _beautifying_ is however sometimes applied to the content through a generative AI to make the content more appealing (like adding emoticons or splitting long sentences). The final content is always created manually and fully endorsed by the author.

## Search

A search module is implemented client-side using the <https://pagefind.app/> JS library.
This library is only loaded on the search page.

## Personal data

Anonymous analytics is collected from _Vercel_ : <https://vercel.com/docs/analytics/privacy-policy>. Its only usage is to track the number of views to each page.

## Eco-developped

- This website is developped with ecological principles in mind. It intends to be as frugal as possible and usable on old terminals like old mobile phone or old computers.
- Éco-index (2023-10-13) [Détails sur ecoindex.fr](https://www.ecoindex.fr/resultat/?id=0cba402f-cc0f-4b2d-ad7a-1495a1ccb6d2#score-details) : <span class="green">A (94/100)</span>
- <div id="wcb" class="carbonbadge"></div><script src="/carbonbadge-1.1.3.min.js"  defer></script>
- For more information, have a look to the [Green IT course](/cours/rse).

## Lobbying et partenariats

- Ce site est ouvert à partenariats **uniquement pour des services éthiques**. Les autres sollicitations sont ignorées.
- <https://sr.ht/> : forge de code source et micro hébergeur Web. Héberge ce site Web (service <https://srht.site/>) et la plupart de mes dépôts de code dans la forge `git`. Service éthique proche des philosophies <https://suckless.org/>. Serveurs aux États-Unis, en cours de transfert vers les Pays-Bas.
- <https://www.zaclys.com/> : hébergeur Software-as-a-Service (SaaS) français éthique. J'utilise à titre personnel le déploiement Nextcloud pour y stocker des fichiers, gérer mes agendas personnels et professionnels (y compris ceux référencés sur ce site), leur gestionnaire de flux RSS (synchronisés en local par `newsboat`) et parfois d'autres services. Comme tout client Zaclys, je dispose d'une offre de parrainage (3 mois offerts pour le parrain et 3 mois offerts pour le parrainé) : me contacter depuis la page [about me](/about).
- <https://www.leviia.com/> : autre fournisseur d'hébergement Nextcloud, les données sont stockées chez OVH. Compte OnlyOffice inclus dans l'offre. Utilisé pour les données liées à mon activité professionnelle, y compris les rendus des apprenants.

## License

Unless stated otherwise, the full content of this website is under the [󰵫  License: CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/) : you are free to share and adapt its content but you must credit me and distribute under the same license.

