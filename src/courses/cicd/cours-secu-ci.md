---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Sécurité de la Supply Chain
layout: '@layouts/CoursePartLayout.astro'
---

## Supply Chain

La "Supply Chain" est devenue ces dernières années un vecteur stratégique en cybersécurité. Les exemples ci-dessous montrent la diversité de ces attaques (open source, cloud, AI/ML) et ont mis en lumière l'importance de sécuriser chaque maillon de la chaîne logicielle (pipelines CI/CD), de renforcer l'authentification multi-facteurs et de surveiller activement les dépendances logicielles.

---

## Exemples d'attaques

---

### Attaque NPM

En 2025, l'écosystème _npm_ a été frappé par une attaque majeure de la chaîne d'approvisionnement (supply chain), liée à une mauvaise configuration de pipeline et à une compromission de comptes de mainteneurs.

---

#### Origine de la vulnérabilité

Le 8 septembre 2025, des attaquants ont compromis les comptes _npm_ de plusieurs mainteneurs de packages populaires (comme `chalk`, `debug`, `ansi-styles`, `strip-ansi`) via une campagne de phishing sophistiquée. Ils ont utilisé une technique d'_Adversary-in-the-Middle_ (_AitM_) pour voler les identifiants, mots de passe et jetons 2FA, puis ont publié des versions malveillantes de 18 packages, totalisant plus de 2 milliards de téléchargements hebdomadaires.

La compromission initiale est survenue à cause d'une mauvaise configuration des workflows GitHub (notamment l'utilisation du déclencheur `pull_request_target`). Ce déclencheur accorde des permissions élevées (écriture via `GITHUB_TOKEN`) aux pull requests externes, permettant à une PR malveillante d’exécuter du code arbitraire et d’injecter du malware dans les packages qui a permis à des pull requests malveillantes d'exécuter du code avec des permissions élevées, facilitant l'injection de malware [source](https://cybercare-nantes.fr/attaque-chaine-npm-identifiants-derobes-nx/).

- Les versions malveillantes contenaient du code JavaScript obfusqué conçu pour intercepter les transactions cryptomonnaies et voler des informations sensibles.
- Le malware était capable de se propager automatiquement : il scannait les environnements compromis, modifiait les fichiers `package.json`, injectait un script malveillant (`bundle.js`), puis republiait les packages infectés. Cela a permis de contaminer les pipelines CI/CD et de créer des portes dérobées persistantes dans les applications déployées. [source](https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2025-093/)
- Les attaquants ont envoyé des e-mails de phishing urgents, les incitant à mettre à jour leurs informations 2FA sur un faux domaine (_npmjs.help_).

---

#### Impact et réponse

- L'attaque a touché des milliers de développeurs et d'entreprises, avec un risque élevé de vol de tokens GitHub, de clés API et de données sensibles :
  - Plus de 2 300 secrets GitHub et cloud ont été dérobés via cette méthode, selon l’équipe Nx [source](https://cybercare-nantes.fr/attaque-chaine-npm-identifiants-derobes-nx/).
  - Plus de 180 packages npm compromis, avec un potentiel d'infection de millions d'utilisateurs et d'applications [source 1](https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2025-093/) [source 2](https://www.mend.io/blog/npm-supply-chain-attack-packages-compromised-by-self-spreading-malware/)
- Les équipes de sécurité ont recommandé de :
  - Mettre à jour les dépendances vers des versions sûres.
  - Auditer les pipelines CI/CD pour détecter tout comportement anormal.
  - Renforcer la surveillance et la protection des comptes mainteneurs.

---

### Porte dérobée XZ Utils (2024)

- **Cible** : La bibliothèque open source _XZ Utils_, utilisée dans de nombreuses distributions Linux.
- **Méthode** : Un développeur malveillant a intégré une porte dérobée dans le code source sur plusieurs années, permettant un accès distant aux systèmes infectés.
- **Impact** : Potentiel de compromission massive des serveurs Linux, détecté juste avant une diffusion large [source](https://xygeni.io/fr/blog/understanding-software-supply-chain-attacks/).

---

### Incident EventStream NPM (2024)

- **Cible** : Le package npm `EventStream`, utilisé par des milliers de projets.
- **Méthode** : Injection d'un code malveillant dans une dépendance peu surveillée, permettant le vol de données sensibles.
- **Impact** : Compromission de nombreuses applications dépendantes, illustrant le risque des dépendances transitives [source](https://xygeni.io/fr/blog/understanding-software-supply-chain-attacks/).

---

### Attaque via Typosquatting sur npm et PyPI (2024-2025)

- **Cible** : Développeurs utilisant des packages open source.
- **Méthode** : Création de faux packages (noms similaires à des bibliothèques populaires) pour tromper les utilisateurs et injecter des malwares comme le stealer _Windows Lumma_.
- **Exemple** : 14 000 faux packages sur npm pour exploiter un système de récompense en cryptomonnaie [source](https://www.cio-online.com/actualites/lire-supply-chain-logicielle-explosion-des-composants-open-source-malveillants-en-2024-15930.html).

---

### SolarWinds (2020)

- Compromission du logiciel _Orion_, touchant plus de 18 000 clients, dont Microsoft et des agences gouvernementales. [source 1](https://guardia.school/boite-a-outils/comprendre-ce-quest-une-supply-chain-attack.html), [source 2](https://xygeni.io/fr/blog/software-supply-chain-attacks-should-i-be-worried/)

---

### Attaques ciblant les modèles AI/ML (2024-2025)

- **Cible** : Plateformes comme _Hugging Face_.
- **Méthode** : Injection de modèles malveillants ou empoisonnement de données pour compromettre les systèmes d'IA.
- **Impact** : Augmentation de 6,5x des modèles malveillants en 2024, selon [JFrog](https://www.globalsecuritymag.fr/le-rapport-jfrog-software-supply-chain-state-of-the-union-2025-est-paru.html).

---

### Attaques Cloud et SaaS (2025)

- **Cible** : Infrastructures cloud et API de prestataires SaaS.
- **Méthode** : Exploitation des intégrations entre partenaires pour propager des malwares ou voler des données. [source](https://0xhack.fr/supply-chain-attack-2026-les-nouvelles-menaces-et-strategies-de-defense-a-connaitre/)

---
