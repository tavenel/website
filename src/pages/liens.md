---
title: Références et Liens utiles
created: 2024-10-17
checked: 2025-01-27
---

![](@assets/undraw/undraw_link-shortener_9ro5.svg)

## Livres

### Living Documentation

- [Living Documentation (Cyrille Martaire)](https://leanpub.com/livingdocumentation)
- Comment bien écrire de la documentation dans le code ?
- Et un prétexte à des réflexions d'architecture, le DDD, le BDD, …
- **LE** livre qui m'a fait progresser en développement

### Refactoring

- [Refactoring, Improving the Design of Existing Code. (Martin Fowler, with Kent Beck)](https://martinfowler.com/books/refactoring.html)
- Un livre génial sur le refactoring de code : comment restructurer un code existant
- Explique aussi comment gérer le code _legacy_ et s'en protéger pour créer des évolutions stables

### Team Topologies

- <https://teamtopologies.com/book>
- Comment découper et organiser les équipes autour d'un projet informatique
- Comment formaliser les interactions entre sous-équipes (collaboration, relation client / fournisseur …)
- Très utilisé en DDD mais très utile dans tous les contextes de projets !
- Voir aussi le [cours DDD](/ddd/cours#relations-entre-quipes) pour un résumé des topologies d'équipes

### Développement

- [Bootstrapping Microservices, Second Edition With Docker, Kubernetes, GitHub Actions, and Terraform (Ashley Davis)](https://www.manning.com/books/bootstrapping-microservices-second-edition)

### Building a Second Brain

- "_Building a Second Brain_" ([livre](https://www.goodreads.com/book/show/59616977-building-a-second-brain)) est une méthode pratique pour stocker et organiser ses notes efficacement selon la méthode **CODE** :

- **Capturer** les idées 📝
- **Organiser** ces idées par des relations entre elles 🗂️
- **Distiller** : ne garder que l'essentiel du concept ⚗️
- **Exprimer** : donner forme et partager (mail, présentation, article, décision, …) 🎤

### Made to Stick

"_Made to Stick_" ([livre](https://www.goodreads.com/book/show/69242.Made_to_Stick)) : pourquoi certaines idées ont un impact durable et d'autres non? Pour ancrer les idées, utiliser la méthode **SUCCES** :

- **Simple** : "Quand on dit trois choses, on ne dit rien."
- **Inattendu (Unexpected)** : La surprise attire l'attention.
- **Concret**
- **Crédible**
- **Émotions** : faire ressentir les choses
- **Histoire (Story)** : pour faire ressentir quelque chose, utiliser des histoires et le storytelling

### The Mom Test

"_The Mom Test_" ([livre](https://www.goodreads.com/book/show/52283963-the-mom-test)) explore les (anti-)schémas lors des retours avec les clients :

- Présentez une idée à votre mère et elle vous dira qu'elle est excellente, même si ce n'est pas le cas.
  - Idem pour les clients : retours souvent polis plutôt qu'utiles.
- Solution :
  - Pas de question basée sur des opinions : "Pensez-vous que c'est une bonne idée ?" ❌
  - Privilégier : expériences et comportements réels (non simulables) ✔️
- Éviter :
  - "Achèteriez-vous un produit qui ferait … ?" ❌
  - "Combien paieriez-vous pour … ?" ❌
- Privilégier :
  - "Comment vivez-vous cette situation actuellement ?" ✔️
  - "Pourquoi est-ce important pour vous ?" ✔️
  - "Pouvez-vous me raconter la dernière fois où cela s'est produit ?" ✔️

> Merci à [Teiva Harsanyi](https://substack.com/@teivah) pour la découverte de ces livres : <https://www.thecoder.cafe/p/paternity-leave>

## Podcasts

- Cybersécurité : "_True stories from the dark side of the Internet_" : <https://darknetdiaries.com/>
- Développement : "_Developer Voices_" : <https://www.developervoices.com/>

## Mailing lists

- <https://www.thecoder.cafe/>

## Citations

> Ce qui se conçoit bien s'énonce clairement et les mots pour le dire viennent aisément. (Boileau)

> You can only be _pragmatic_ if you know how to be _dogmatic_.

> Toute abstraction visant à simplifier le travail d'un utilisateur transfère la complexité ailleurs, généralement aux équipes techniques. La complexité ne disparaît jamais, elle est déportée vers une application. [Conservation de la Complexité](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

> La vérité, c'est qu'il n'y a pas de vérité. (Y compris celle-ci). (Proverbe Shadok)

> Les ordinateurs, plus on s'en sert moins, moins ça a de chance de mal marcher. (Proverbe Shadok)

> A force de taper dans rien, il finit toujours par en sortir quelque chose. Et réciproquement. (Proverbe Shadok)

> Avec un escalier prévu pour la montée, on réussit souvent à monter plus bas qu'on ne serait descendu avec un escalier prévu pour la descente. (Proverbe Shadok)

> Programs must be written for people to read, and only incidentally for machines to execute. (Abelson & Sussman, SICP, preface to the first edition)

> Dealing with failure is easy: Work hard to improve. Success is also easy to handle: You've solved the wrong problem. Work hard to improve. (Alan Perlis)

> Je crois qu'il y a un marché mondial pour à peu près cinq ordinateurs. Thomas Watson, président d'IBM, 1958

> Toujours laisser le code plus propre que vous l'aviez trouvé. (Règle adaptée des Scouts)

## Liens

### Réseau

- [V2F (Youtube) :  screw it... let's rebuild the ENTIRE Internet](https://www.youtube.com/watch?v=HRa31C7zfzk)
- <https://www.it-connect.fr/le-nat-et-le-pat-pour-les-debutants/>
- <https://www.it-connect.fr/comprendre-les-differents-types-de-reseaux-de-vmware-workstation-pro/>
- NAT vs BRIDGE : <https://blog.stephane-robert.info/docs/homelab/bridge-nat/>
- Types de réseaux virtuels basiques sous Linux : <https://pve.proxmox.com/wiki/Network_Configuration>

### CRDTS

**Conflict-free Replicated Data Types** : comment fusionner des données répliquées ?

- <https://vlcn.io/blog/intro-to-crdts> : Enjeux des CRDTS
- <https://jakelazaroff.com/words/an-interactive-intro-to-crdts/> : Introduction et exemples de CRDTS
- <https://read.thecoder.cafe/p/crdt> : explication des CRDTs
- <https://zknill.io/posts/collaboration-no-crdts/> : comment collaborer sans CRDTS

### Sauvegardes : la règle du 3-2-1-1-0

- 3 = Conservez au moins trois copies de vos données : production, sauvegarde, copie de sauvegarde (en bonus l'archivage compte comme une copie)
- 2 = Utilisez au moins deux types de supports différents pour le stockage (de marque différentes) : disques internes, SAN, NAS (en bonus l'archivage avec les bandes LTO compte comme un support)
- 1 = Conservez au moins une copie hors site : autre site (de production et de sauvegarde) que ce soit une infra de stockage ou dans un coffre-fort par exemple.
- 1 = Conservez au moins une copie hors ligne, isolée ou immuable : c'est surtout pour se prémunir d'une destruction volontaire (ransomware, acte malveillant via accès distant)
- 0 = Zéro erreur après tests de restauration : une sauvegarde non restaurable n'est pas exploitable le jour où on en a besoin.

### High Availability (HA)

- The CAP Theorem : <https://www.thecoder.cafe/p/cap>
- The PACELC Theorem : <https://www.thecoder.cafe/p/pacelc>
- Availability Models : <https://www.thecoder.cafe/p/availability-models>

### E-Mail

- <https://www.mail-tester.com> : test mail spammyness
- <https://www.emailprivacytester.com> : test mail client for privacy
- <https://www.virustotal.com> : scan file for viruses (Google)

### Cybersécurité

- <https://blog.stephane-robert.info/post/google-dorks/> : Les Google Dorks - trouver des informations sensibles depuis Google Search.
- <https://ddosecrets.com/> : Distributed Denial of Secrets : publication des leaks
- <https://en.fofa.info/> : Recherche d'hôtes sur critères
- Check DNS leaks : <https://dnsleaktest.com/>
- <https://blog.humancoders.com/les-pires-failles-de-securite-de-2025-3853/>
- <https://zythom.fr/2025/11/cybersecurite-assistee-par-ia/>

#### Ampleur des attaques

- Presque 80 nouvelles CVE/jour [source 2024](https://www.ninjaone.com/fr/blog/7-statistiques-sur-la-cybersecurite-que-chaque-pme-et-msp-doit-connaitre/)
- 50% des PME ont connu une violation de site web et plus de 40 % signalent des attaques mensuelles ou plus fréquentes [source 2021](https://www.sectigo.com/resource-library/study-finds-50-of-smbs-have-experienced-a-website-breach-and-40-are-being-attacked-monthly?utm_source=chatgpt.com)
- 50% des PME attaquées ont coulé [source 2025](https://www.lemagit.fr/conseil/Combien-de-PME-mettent-la-cle-sous-la-porte-apres-une-cyberattaque?utm_source=chatgpt.com).

### CRA - EU Cyber Resilience Act

- Si publication de logiciel, besoin de publier un SBOM (Software Bill of Materials) des dépendances
- Gérer les vulnérabilités (scan CVE depuis SBOM) -> statement (affecté / non affecté <- à justifier) -> rapport

### Documentation

#### Diagramme C4

Type de diagramme très utilisé en agilité, permettant de décrire l'architecture en "zoomant" des composants au code : <https://c4model.com/>

#### ADR

Un **ADR** (_Architecture Decision Record_) permet de documenter un choix d'architecture, par exemple avec le formalisme suivant :

> In the context of \<use case/user story>, facing \<concern> we decided for \<option> to achieve \<quality>, accepting \<downside>, because \<additional rationale>.

:::link
Voir aussi : <https://adr.github.io/>
:::

#### Liens

- Exemples simplifiés de pages de manuel (+ ligne de commandes et format opensearch pour ajout au navigateur) : <https://cheat.sh/>
- Explication graphique de commandes de terminal : <https://explainshell.com/>
- Documentation technique - fonctionne hors ligne : <https://devdocs.io/>
- [CERISE : Conseils aux Etudiants en Recherche d'InformationS Efficace](https://callisto-formation.fr/course/view.php?id=263)
- Exemples de bons README : <https://github.com/matiassingers/awesome-readme>
- Exemple de page d'aide de CLI : voir la commande `kubectl --help`
- Comment écrire de bons exemples : <https://conventionalcomments.org/>
- Documentation technique - fonctionne hors ligne <https://devdocs.io/>
- Référence pour écrire une bonne documentation technique : <https://diataxis.fr/> et <https://blog.wescale.fr/back-to-basics-pere-castor-dis-moi-comment-ecrire-une-bonne-documentation-technique>

##### LaTeX

- Écrire des maths en LaTeX : <https://zestedesavoir.com/tutoriels/409/outils-pour-lecriture-des-mathematiques-en-latex/>
- Utiliser LaTeX pour créer des sujets d'examen : <https://blog.dorian-depriester.fr/latex/rediger-des-sujets-dexamen-avec-latex>
- Symboles mathématiques et lettres grecques en LaTeX : <https://fr.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols>

### Dev

- Lexique du développeur : <https://zestedesavoir.com/tutoriels/531/les-bases-de-la-programmation/>
- <https://conventionalcomments.org/>
- <https://zestedesavoir.com/tutoriels/299/la-theorie-rest-restful-et-hateoas/>
- <https://zestedesavoir.com/tutoriels/621/algorithmique-pour-lapprenti-programmeur/>
- Histoire de Java : <https://codegym.cc/fr/groups/posts/fr.594.histoire-de-java-une-histoire-complete-du-developpement-java-de-1991-a-2021>
- <https://perso.crans.org/besson/publis/slides/2016_07__Python_demo_at_EPFL/> : cours Python ML/DL/data science
- [Algorithme génétique de déplacement dans l'eau](https://www.youtube.com/watch?v=gVEWaOtEASM)
- [Authentication and authorization in a microservice architecture](https://microservices.io/post/architecture/2025/05/28/microservices-authn-authz-part-2-authentication.html)
- [Pattern CQRS/ES et implémentations](https://romaintrm.github.io/posts/cqrs-es-nos-heuristiques-apres-plusieurs-annees-de-production/)
- [Message Queues vs Pub/Sub : arrêtez de les confondre](https://maxence.maireaux.fr/fr/blog/message-queues-vs-pub-sub/)
- <https://lafor.ge/monad/> : "Les monades sans les maths". Introduction simple aux conteneurs, fonctor & monades
- <https://cloudnativenow.com/contributed-content/you-are-more-likely-to-land-a-lead-level-cloud-native-role-than-a-junior-one/>

### UI et UX

- Cas d'étude d'UX Design : <https://growth.design/>
- UX asynchrone : <https://kyusuf.com/post/fake-it-til-you-make-it-css>
- <https://dev.to/devluc/50-best-websites-for-web-design-inspiration-and-ideas-be6>
- <https://xyris.app/blog/best-svg-animation-tools-in-2025-features-pros-cons/>
- Exemple de pire interface utilisateur : <https://userinyerface.com/>

### Théorie

- Les méta-lois en informatique : <https://github.com/StephaneTrebel/presentations/tree/main/meta-lois>
- Article très complet sur les origines de la console et des terminaux Unix : <https://thevaluable.dev/guide-terminal-shell-console/>
- Excellent article sur le fonctionnement d'un ordinateur : <https://lafor.ge/virtualization-1/>
- Cours sur les optimisations des compilateurs : <https://zestedesavoir.com/tutoriels/427/les-optimisations-des-compilateurs/>
- Cours mémoire cache et optimisation de code : <https://zestedesavoir.com/tutoriels/331/memoire-cache-et-optimisation-de-code/>
- Le paradoxe de la complexité : <https://www.votito.com/methods/togs-paradox/>
- <https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing> : erreurs typiques en programmation & déploiement de systèmes distribués

### Liens transverses Tech

- <https://oracle.com/cloud/free> : free servers
- <https://endoflife.date>
- Gérer la variable d'environnement `$PATH` :
  - voir [ce tutoriel sous Windows](https://www.malekal.com/comment-modifier-la-variable-path-sous-windows-10-11/)
  - sous Linux, voir le TP sur la ligne de commandes [du cours Linux](/linux)
- Tips `Vagrant` : <https://blog.stephane-robert.info/docs/infra-as-code/provisionnement/vagrant/introduction/#quelques-tips>
- Salaires dans la tech : <https://www.silkhom.com/les-salaires-informatique-et-electronique/>
- <https://killercoda.com/> : playgrounds Dev / Ops (Linux, Git, k8s, …)
- [Une architecture open-source qui ne déraille pas (Julien Cognet, Snowcamp 2025)](https://www.slideshare.net/slideshow/snowcamp-2025-une-architecture-qui-ne-deraille-pas/275103626)
- <https://sebsauvage.net/wiki/doku.php?id=android> applications et jeux Android intéressants
- Fiches de réparation de matériels électroniques : <https://fr.ifixit.com/>
- "A series of nonverbal algorithm assembly instructions" : <https://idea-instructions.com/>
- <https://wrongthink.link/posts/all-you-need-is-ssh/>
- Comment réaliser un bon onboarding : <https://blog.wescale.fr/bienvenue-dans-lequipe-voici-ton-onboarding-puisse-le-sort-vous-etre-favorable>
- Histoire du pilotage des serveurs : de l'administration physique aux terminaux à l'infrastructure-as-code : <https://richard-dern.fr/interets/informatique/2025/12/12/piloter-ses-serveurs-avec-un-emulateur-de-terminal-web/>

### Adoption

En 2025 (d'après : <https://www.docker.com/blog/2025-docker-state-of-app-dev/>) :

- CI/CD: GitHub Actions (40%), GitLab (39%), Jenkins (36%)
- Provisioning: Terraform (39%), Ansible (35%), GCP (32%)
- Monitoring: Grafana (40%), Prometheus (38%), Elastic (34%)
- Containers in IT : 92%

### Liens Divers

- Introduction au droit d'auteur et aux licences Creative Commons : <https://zestedesavoir.com/tutoriels/261/le-droit-dauteur-creative-commons-et-les-licences-sur-zeste-de-savoir/>
- [Do Not Erase: Beautiful Collection of Mathematicians' Blackboards](https://abakcus.com/do-not-erase-beautiful-collection-of-mathematicians-blackboards)
- [Le charbon est beaucoup plus dangereux que le nucléaire](https://lehollandaisvolant.net/?d=2022/08/29/18/40/42-le-charbon-est-beaucoup-plus-dangereux-que-le-nucleaire)
- Perma-entreprise : <https://www.permaentreprise.fr/>
- <https://www.librealire.org/bien-gerer-son-projet-libre-que-faire-au-dela-du-code>
- Comics about energy : <https://www.stuartmcmillen.com/comic/energy-slaves/>

## Gamification

### Linux, Vim, Docker, Kubernetes, Git

:::link
Voir les pages de cours :

- [Page Linux et Vim](/linux)
- [Liens Gamification Docker](/docker/cours#exercices-challenges)
- [Liens Kubernetes](/k8s/cours#-liens)
- [Liens Git](/git/cours#ressources)

:::

### Cybersécurité

- Wargames orientés Linux et déploiement Web (démarrer par _bandit_) : <https://overthewire.org/wargames/bandit/>
- CTF populaires :
  - <https://www.hackthebox.com/> : plateforme de gamification permettant d'apprendre la cybersécurité en résolvant des défis.
  - <https://tryhackme.com/> : plateforme d'apprentissage gamifiée avec des laboratoires pratiques et des scénarios réels. Cette plateforme est très accessible
  - <https://www.vulnhub.com/> : plateforme regroupant des machines virtuelles vulnérables à exploiter.
  - <https://www.root-me.org/> : plateforme d'apprentissage immersive permettant de se familiariser avec la cybersécurité en s'entraînant sur des environnements réels.
  - <https://www.securecodewarrior.com/> : apprendre à développer du code robuste
  - <https://hackropole.fr/fr/> : rejouer les épreuves du France Cybersecurity Challenge
- <https://docs.rapid7.com/metasploit/metasploitable-2/> et <https://github.com/rapid7/metasploitable3> : VMs Linux vulnérables
- <https://github.com/apsdehal/awesome-ctf>
- <https://sploitus.com/> : recherche de vulnérabilités
- <https://archive.org/download/HalLinuxForensics> : exercices de forensics

## Exemples de projets

### Docker

- [Exemples de projets Docker](https://github.com/dockersamples)
- [SF Food trucks : application flask, react, elastic search avec 3 conteneurs](https://docker-curriculum.com/#sf-food-trucks)
- [Dockercoins : excellent projet de démonstration de Jérôme Petazzoni](https://github.com/jpetazzo/container.training)
- [Petclinic : version Docker Compose](https://github.com/spring-petclinic/spring-petclinic-microservices)
- [Exemple de microservices en Docker Compose et Kubernetes](https://github.com/microservices-demo/microservices-demo)

### Kubernetes

- [Petclinic : version Kubernetes](https://github.com/spring-petclinic/spring-petclinic-cloud)
- [Kubercoins : excellent projet de démonstration de Jérôme Petazzoni](https://github.com/jpetazzo/kubercoins)
- [Coffee : applications de test pour k8s (kustomize, helm, yaml, …)](https://github.com/QJoly/kubernetes-coffee-image)
- [Exemples de tutoriels GKE](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples)
- [Exemple de microservices en Docker Compose et Kubernetes](https://github.com/microservices-demo/microservices-demo)
- [BookInfo, application de démonstration d'Istio](https://istio.io/latest/docs/examples/bookinfo/)

### Cybersécurité

- <https://owasp.org/www-project-juice-shop/>

### Fullstack

- <https://spring-petclinic.github.io/>
- <https://github.com/gothinkster/realworld>
- <https://github.com/bradtraversy/50projects50days>
