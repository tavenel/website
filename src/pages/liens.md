---
title: Liens utiles
created: 2024-10-17
checked: 2025-01-27
---

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

### Développement

- [Bootstrapping Microservices, Second Edition With Docker, Kubernetes, GitHub Actions, and Terraform (Ashley Davis)](https://www.manning.com/books/bootstrapping-microservices-second-edition)

## Podcasts

- Cybersécurité : "_True stories from the dark side of the Internet_" : <https://darknetdiaries.com/>
- Développement : "_Developer Voices_" : <https://www.developervoices.com/>

## Informations transverses

### Apprentissage, Métacognition, Organisation

#### Notions d'apprentissage

- **Cessité attentionnelle** : lors d'un focus fort sur une tâche, peu d'attention au reste
  - Voir l'expérience du gorille dans ce podcast : <https://www.radiofrance.fr/franceculture/podcasts/votre-cerveau/l-attention-4589382>
  - Vidéo Youtube : [selective attention test](https://www.youtube.com/watch?v=IGQmdoK_ZfY)
- **Inhibition** : capacité du cortex préfrontal à sortir des routines et automatismes
  - Voir l'expérience de l'effet Stroop : <https://biais-psychologiques.com/biais/effet-stroop/> et podcast : <https://www.radiofrance.fr/franceculture/podcasts/votre-cerveau/l-inhibition-et-la-flexibilite-3735919>
- La **récompense** permet d'appliquer une **motivation extrinsèque** (de l'extérieur) à l'apprentissage à court terme mais **au détriment de la motivation intrinsèque** (interne à l'apprenant) sur le long terme (à minimiser donc).
  - Pour promouvoir la **motivation intrinsèque** : mettre le focus sur l'apprentissage de nouvelles compétences & l'interaction entre apprenants
  - Voir le podcast : <https://www.radiofrance.fr/franceculture/podcasts/votre-cerveau/la-motivation-et-l-esprit-de-changement-1962894>
- L'utilisation des **émotions** permet un engagement fort :
  - Émotion positive : succès de la réalisation, reconnaissance de la réussite, plaisir et bien-être dans le groupe, …
  - Émotion négative : situation future néfaste pouvant être évitée par la réalisation de la tâche ou de l'apprentissage, peur de passer à côté d'une opportunité (bien connu en marketing), …
- **Mémorisation** :
  - Tout le monde apprend à peu près pareil (pas de "visuels", "auditifs", …). Le meilleur apprentissage est croisé (visuel + auditif + …)
  - Éviter le _"par coeur"_ peu efficace. Privilégier un **traitement profond** (basé sur le **sens** des informations)
  - Travailler par associations. Excellent podcast (10') : <https://www.radiofrance.fr/franceculture/podcasts/votre-cerveau/comment-fonctionne-votre-memoire-1-6-non-apprendre-par-coeur-n-est-pas-tres-efficace-2431233>
  - S'impliquer **personnellement** et utiliser des références à **soi-même**
  - Apprentissage basé sur l'**action** : il est beaucoup plus simple de se rappeler ce que l'on a fait que d'apprendre théoriquement

#### Inbox 0

- Objectif : Minimiser le temps passé à la gestion des mails
- Principes :
  - Vérifier ses mail à heure fixe et non toute la journée (pas de notification)
  - Catégoriser ses mails dans des répertoires
  - Appliquer un arbre de décision à chaque mail reçu :
    - Faire directement si < 2 min
    - Sinon Différer
    - Déléguer si possible
    - Supprimer si l'e-mail est uniquement informatif
- <http://www.43folders.com/43-folders-series-inbox-zero>
- <https://asana.com/resources/inbox-zero>
- <https://www.microsoft.com/en-us/microsoft-365-life-hacks/organization/inbox-zero-six-tips-for-living-outside-the-box>

#### Méthode des J

- Principe : "raffraichir" la mémoire à dates régulières afin d'éviter la courbe de l'oubli en révisant par exemple à :
  - J0, J1, J3, J7, J14, J30
  - J0, J1, J3, J10, J20, J35
  - J0, J2, J5, J14
- En Pratique : QCMs, exercices, … aux dates prévues. L'apprentissage se fait à J0, les autres dates sont de courtes sessions de remémorisation.
- <https://www.adobe.com/fr/acrobat/resources/studying/spaced-repetition-method.html>
- <https://hermione.co/methode-des-j-pass/>

#### Prise de notes et rédaction efficaces

- Noter et écrire le fond en _temps réel_
- Avoir une collection d'abbréviations pour gagner du temps
- Séparer d'une colonne : notes objectives "résumé" et notes subjectives "questions / actions à prendre / …"
- Retravailler la forme et la mise en page plus tard
- <https://apprendre5minutes.wordpress.com/2025/03/08/techniques-prise-de-notes-efficaces/>
- <https://kevindetem.com/12-methodes-prise-de-notes-efficace>

#### Sketchnote

- Principe : Représenter graphiquement en dessinant et annotant une prise de notes
- Très utile en cours magistral / conférence technique /  … pour résumer un concept complexe
- Voir aussi : <https://www.mindmapping.com/>
- <https://www.insuffle.com/cest-quoi-le-sketchnoting/>
- <https://www.bienenseigner.com/sketchnote/>
- <https://www.optimike.net/sketchnoting/>

### Sauvegardes : la règle du 3-2-1-1-0

- 3 = Conservez au moins trois copies de vos données : production, sauvegarde, copie de sauvegarde (en bonus l'archivage compte comme une copie)
- 2 = Utilisez au moins deux types de supports différents pour le stockage (de marque différentes) : disques internes, SAN, NAS (en bonus l'archivage avec les bandes LTO compte comme un support)
- 1 = Conservez au moins une copie hors site : autre site (de production et de sauvegarde) que ce soit une infra de stockage ou dans un coffre-fort par exemple.
- 1 = Conservez au moins une copie hors ligne, isolée ou immuable : c'est surtout pour se prémunir d'une destruction volontaire (ransomware, acte malveillant via accès distant)
- 0 = Zéro erreur après tests de restauration : une sauvegarde non restaurable n'est pas exploitable le jour où on en a besoin.

### CRDTS

**Conflict Free Replicated Data types** : comment fusionner des données répliquées ?

- <https://vlcn.io/blog/intro-to-crdts> : Enjeux des CRDTS
- <https://jakelazaroff.com/words/an-interactive-intro-to-crdts/> : Introduction et exemples de CRDTS
- <https://zknill.io/posts/collaboration-no-crdts/> : comment collaborer sans CRDTS

### High Availability (HA)

- The CAP Theorem : <https://www.thecoder.cafe/p/cap>
- The PACELC Theorem : <https://www.thecoder.cafe/p/pacelc>
- Availability Models : <https://www.thecoder.cafe/p/availability-models>

### Cybersécurité (2020)

- 50% des applications Web ont une faille critique
- 50 nouvelles CVE découvertes chaque jour
- 50% des PME attaquées ont coulé

### IA

#### Types de prompts IA

- _zero-shot_ => pas de contexte
- _few shots_ => contexte par exemples
- _chain of thought_ => "let's think …" (step-by-step example)
- _RAG_ (retrieval augmented generation) => élévation de contexte par vecteur de contexte
- _agents_ => conscience de l'environnement

#### Liens IA

- <https://www.comparia.beta.gouv.fr/>
- <https://tugaleres.com/2025/03/04/est-on-plus-efficace-en-utilisant-une-ia-type-chatgpt/>
- <https://github.com/microsoft/AI-For-Beginners> : Cours gratuits Microsoft
- Impact des IA génératives sur les étudiants :
  - <https://open.devinci.fr/ressource/etude-2024-impact-ia-generatives-etudiants/>
  - <https://www.newcartographies.com/p/the-myth-of-automated-learning>
- [Les sacrifiés de l'IA (Henri Poulain)](https://www.francetvinfo.fr/replay-radio/info-medias/les-sacrifies-de-l-ia-dans-son-documentaire-henri-poulain-revele-les-coulisses-d-une-industrie-qui-exploite-la-misere-humaine_7038260.html)
- [UX : Comment les entreprises de la tech nous forcent à utiliser l'IA](https://limitesnumeriques.fr/travaux-productions/ai-forcing)
- <https://blog.wescale.fr/back-to-basics-pere-castor-raconte-moi-le-prompt-engineering>

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

## Liens transverses

- Les méta-lois en informatique : <https://github.com/StephaneTrebel/presentations/tree/main/meta-lois>
- [CERISE : Conseils aux Etudiants en Recherche d'InformationS Efficace](https://callisto-formation.fr/course/view.php?id=263)
- Documentation technique - fonctionne hors ligne : <https://devdocs.io/>
- Gérer la variable d'environnement `$PATH` :
  - voir [ce tutoriel sous Windows](https://www.malekal.com/comment-modifier-la-variable-path-sous-windows-10-11/)
  - sous Linux, voir le TP sur la ligne de commandes [du cours Linux](/linux)
- Article très complet sur les origines de la console et des terminaux Unix : <https://thevaluable.dev/guide-terminal-shell-console/>
- <https://conventionalcomments.org/>
- <https://zestedesavoir.com/tutoriels/299/la-theorie-rest-restful-et-hateoas/>
- <https://zestedesavoir.com/tutoriels/621/algorithmique-pour-lapprenti-programmeur/>
- Excellent article sur le fonctionnement d'un ordinateur : <https://lafor.ge/virtualization-1/>
- Lexique du développeur : <https://zestedesavoir.com/tutoriels/531/les-bases-de-la-programmation/>
- Cours sur les optimisations des compilateurs : <https://zestedesavoir.com/tutoriels/427/les-optimisations-des-compilateurs/>
- Cours mémoire cache et optimisation de code : <https://zestedesavoir.com/tutoriels/331/memoire-cache-et-optimisation-de-code/>
- Introduction au droit d'auteur et aux licences Creative Commons : <https://zestedesavoir.com/tutoriels/261/le-droit-dauteur-creative-commons-et-les-licences-sur-zeste-de-savoir/>
- Exemples de bons README : <https://github.com/matiassingers/awesome-readme>
- UX asynchrone : <https://kyusuf.com/post/fake-it-til-you-make-it-css>
- <https://dev.to/devluc/50-best-websites-for-web-design-inspiration-and-ideas-be6>
- Tips `Vagrant` : <https://blog.stephane-robert.info/docs/infra-as-code/provisionnement/vagrant/introduction/#quelques-tips>
- Salaires dans la tech : <https://www.silkhom.com/les-salaires-informatique-et-electronique/>
- <https://killercoda.com/> : playgrounds Dev / Ops (Linux, Git, k8s, …)
- <https://perso.crans.org/besson/publis/slides/2016_07__Python_demo_at_EPFL/> : cours Python ML/DL/data science
- Le paradoxe de la complexité : <https://www.votito.com/methods/togs-paradox/>
- Exemple de page d'aide de CLI : voir la commande `kubectl --help`
- [Algorithme génétique de déplacement dans l'eau](https://www.youtube.com/watch?v=gVEWaOtEASM)
- <https://xyris.app/blog/best-svg-animation-tools-in-2025-features-pros-cons/>
- [NAT vs BRIDGE](https://blog.stephane-robert.info/docs/homelab/bridge-nat/)
- <https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing> : erreurs typiques en programmation & déploiement de systèmes distribués
- <https://nip.io/> : DNS résolvant toute IP vers un hostname : `10.0.0.1.nip.io` résoud vers `10.0.0.1`
- Cas d'étude d'UX Design : <https://growth.design/>
- [Pattern CQRS/ES et implémentations](https://romaintrm.github.io/posts/cqrs-es-nos-heuristiques-apres-plusieurs-annees-de-production/)
- <https://lafor.ge/monad/> : "Les monades sans les maths". Introduction simple aux conteneurs, fonctor & monades
- [Une architecture open-source qui ne déraille pas (Julien Cognet, Snowcamp 2025)](https://www.slideshare.net/slideshow/snowcamp-2025-une-architecture-qui-ne-deraille-pas/275103626)
- [Authentication and authorization in a microservice architecture](https://microservices.io/post/architecture/2025/05/28/microservices-authn-authz-part-2-authentication.html)
- Histoire de Java : <https://codegym.cc/fr/groups/posts/fr.594.histoire-de-java-une-histoire-complete-du-developpement-java-de-1991-a-2021>
- [Do Not Erase: Beautiful Collection of Mathematicians' Blackboards](https://abakcus.com/do-not-erase-beautiful-collection-of-mathematicians-blackboards)

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
- <https://github.com/apsdehal/awesome-ctf>
- <https://sploitus.com/> : recherche de vulnérabilités

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

