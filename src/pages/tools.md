---
title: Programmes frameworks et outils
created: 2024-10-17
---

## Commandes utiles

### 💻 `entr` : réexécute une commande

- `ls file1.py | entr python /_` : réexécute le fichier `file1.py` à chaque sauvegarde
  - `entr -c` : avec clear d'écran
  - `entr -p` : postpone la 1e exécution au 1e changement
  - `entr -r` : redémarre une commande qui tourne en continu

## 🌍 Utilitaires en ligne

- Afficher son IP publique : `curl ifconfig.me/ip` ou `curl ifconfig.me/all.json`
- ❓ Aides sur les commandes : `curl cheat.sh/ma_commande`
- ⛅ `curl wttr.in/Grenoble` => weather at Grenoble, France.
- [Extension Firefox et Chrome pour alerter sur les sites générés par IA](https://next.ink/164873/outils-next-une-extension-chrome-et-firefox-pour-etre-alerte-des-sites-genai/)

## Outils utiles Devops (liste non exhaustive)

### 🗺️ Landscape Devops (liens externes)

- <https://platformengineering.org/platform-tooling>
- <https://xavki.blog/devops-sources/>
- <https://landscape.cncf.io/>

### 1️⃣  Versioning

-  `git`
  - forges logicielles => `github`, 🦊 `gitlab`, `bitbucket` (Atlassian -> `Jira`), `sourcehut`, `forgejo`, `gitea`, `gitbucket`, …
  - 🔐 sécurité
    - [git-crypt](https://github.com/AGWA/git-crypt)
    - 🔑 `gittuf` : utilise The Update Framework (TUF) : gestion des clés des développeurs du dépôt, autorisations par branches, fichiers, …
		- <https://github.com/gitleaks/gitleaks> : `docker run -v ${PWD}:/path ghcr.io/gitleaks/gitleaks:latest detect --source="/path" -v`
		- <https://github.com/trufflesecurity/trufflehog> : trouver des secrets exposés dans ses dépôts Git
  - outils
    - 🤪 [gitmoji](https://github.com/carloscuesta/gitmoji) : ajouter des emojis de contexte aux commits
    - <https://alchemists.io/projects/git-lint> : linter de commits Git pour une cohérence des messages
- [jujutsu](https://github.com/jj-vcs/jj) : autre gestionnaire de versions basé sur un backend Git. TUI : [lazyjj](https://github.com/Cretezy/lazyjj)
- sémantique :
  - 1️⃣  <https://semver.org/>
  - 2️⃣ <https://hub.docker.com/r/gittools/gitversion>
  - 3 <https://alchemists.io/projects/milestoner> : automatise la génération de release notes, versioning et déploiements.
- analyses :
  - 📊 <https://github.com/adamtornhill/code-maat> : data mining dans dépôt Git
  - 🔎 <https://github.com/smontanari/code-forensics>

### 📦 Conteneurs

-   `docker`
  - 🔒 sécurité :
    - _Docker Scout_ (inclus dans _Docker desktop_) : voir la [cheatsheet Docker](/docker/cheatsheet)
    - <https://github.com/docker/docker-bench-security>
    - <https://github.com/aquasecurity/trivy> (inclus k8s)
    - <https://une-tasse-de.cafe/expresso/cosign/> : signer ses images Docker
    - `grype` : scan de sécurité des images Docker
  - Analyse des images Docker :
    - `dive` : analyse poussée des layers
		- [sou](https://github.com/knqyf263/sou) : analyse simple des layers
    - `Container Structure Test` : tests sur images Docker produites. [tuto](https://blog.stephane-robert.info/docs/conteneurs/outils/container-struct-test/)
  - images légères :
    - Alpine linux : <https://www.alpinelinux.org/>
    - Distroless : <https://blog.garambrogne.net/distroless.html>
- 🚢 `podman` : idem Docker sans agent, supporte Docker et pods k8s
- `cri-o` : container runtime k8s

#### 📄 Dockerfile

- 🧐 vérification : `hadolint`, <https://falco.org/>, <https://quay.github.io/clair/>
- 🔄 mise à jour : `renovate`

#### Registry

- Hubs publics :
  - Docker Hub : <https://hub.docker.com>
  - Hub Github : <https://ghcr.io/>
  - Hub d'images temporaires : <https://ttl.sh/>
- Registry internes :
  - <https://github.com/Joxit/docker-registry-ui>
  - `gitea`
  - <https://hub.docker.com/_/registry> 

#### Orchestration de conteneurs

- 󱃾 Kubernetes : LA référence en orchestration
  - `k8s` : implémentation principale de Kubernetes
  - `k0s` : implémentation de Docker Enterprise (single binary)
  - `k3s` (installable par `k3d`), `microk8s` (ubuntu) : implémentations légères
  - `minikube` : version 1 noeud simple pour dev/test uniquement
  - `kind` : déploiement local utilisant Docker (excellent pour une installation locale) : [tuto](https://blog.stephane-robert.info/post/kubernetes-kind/)
   [`Talos` : OS immuable pour k8s](https://une-tasse-de.cafe/blog/talos/)
  - `openshift` : orchestrateur de RedHat
  - `rancher` : manager de cluster(s) k8s (installation, monitoring, tests, …)
  - `k8s-tew` : k8s the easy way, cluster complet. [tuto](https://blog.zwindler.fr/2025/05/26/test-k8s-tew/)
- `swarm` : orchestrateur inclus dans Docker
- `docker compose` : orchestrateur simple de Docker (dev, test, CI/CD, prod simpliste)
- `nomad` : orchestrateur applicatif conteneurisées ou non, simple pour on-premise
- `mesos` + `dc/os`

#### 󱃾 Kubernetes-specific

- Liste d'opérateurs : <https://operatorhub.io/>
- 🔎 linter (vérification fichiers) => `kubeconform`, `kube-score`
- 📦 package manager (sur-couche) => `helm` (et secrets : <https://github.com/jkroepke/helm-secrets>)
- ingress & service mesh :
  - `traefik` : reverse-proxy automatique
  - amélioration d'Ingress :
    - _Ingress controller_ (ingress avec _CRD_ custom) :
      - `Contour`
      - `Emissary Ingress`
      - `Voyager` 
    - _Application proxy_ avec services : _rate limiting_, …
      - `Kong`
      - `Apisix`
      - `Traefik proxy` 
    - _Service mesh_
      - `Istio` : [article](https://une-tasse-de.cafe/blog/istio/) et observabilité par <https://kiali.io/>
      - `Cilium` : networking, security, observability
      - `Traefik mesh`
      - `NGINX Service Mesh`
      - `Consul` : DNS, reverse proxy, load balancing, …
    - Gateway API : `ingress2gateway`
  - [external DNS](https://github.com/kubernetes-sigs/external-dns) : synchronisation Ingress / Service avec DNS externe (Cloud, …)
- 📦📦 scaling
  - [Keda](https://keda.sh/) : Event-driven autoscaling
  - `Goldilocks` : génération de recommendations de _requests_ et _limits_
- 🔒 sécurité
  - [Popeye](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/popeye/) : vérification de cluster k8s
  - [Kubescape](https://blog.stephane-robert.info/docs/securiser/conteneurs/kubescape/) : scan de clusters, intégration dev et CI/CD
	- `kubeseal` et `Sealed Secret` : [tuto 1](https://une-tasse-de.cafe/blog/sealed-secrets/) et [tuto 2](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/sealed-secrets/) : chiffrement de secrets dans k8s
	- <https://external-secrets.io/> : injection de secrets (Opérateur et CRDs) : [tuto](https://blog.wescale.fr/synchronisation-des-secrets-dans-votre-cluster-kubernetes-avec-external-secrets)
	- `cert-manager` : gestion des certificats SSL/TLS [tuto](https://une-tasse-de.cafe/blog/cert-manager/)
  - `polaris` : détection de problèmes de sécurité dans un cluster
  - <https://chaos-mesh.org/> : chaos computing dans un cluster
  - <https://github.com/kubernetes-sigs/security-profiles-operator> : Opérateur SELinux, Apparmor, Seccomp
  - `Falco`
- 🧐 supervision
  - `k9s` : [tuto](https://blog.stephane-robert.info/docs/outils/indispensables/#k9s)
  - `kubevious` : [tuto](https://blog.stephane-robert.info/post/kubernetes-tableau-bord-kubevious/)
  - <https://k8slens.dev/> : un IDE orienté k8s
  - <https://github.com/stern/stern> : logs multi-pods
  - <https://codeberg.org/hjacobs/kube-web-view> : remplacement R/O du web dashboard, supporte le multi-cluster
  - <https://github.com/kubernetes-sigs/kui> : version graphique de `kubectl`
  - <https://codeberg.org/hjacobs/kube-janitor> : Supprimes des ressources Kubernetes après un certain temps
  - <https://www.tigera.io/> : Unified Network Security & Observability for Kubernetes
  - <https://www.kuboscore.io/> : vérification de clusters
- 🚀 CD
  - `fluxcd` : GitOps
  - `argocd` : <https://une-tasse-de.cafe/blog/argocd/>
    - <https://kargo.io/> : promotion de pipelines (test,staging,prod,…). [tuto](https://piotrminkowski.com/2025/01/14/continuous-promotion-on-kubernetes-with-gitops/)
    - <https://devtron.ai/> : alternative à `Kargo`
  - `flagger` : blue/green, A/B, canary deployments
- `kubevirt` : Ajout de la gestion de VMs dans Kubernetes
- 🪫 Consommation d'énergie et pricing :
  - `kepler` : monitor Pod energy consumption
  - `kube-green` : k8s operator for energy-saving actions. [tuto](https://blog.octo.com/arreter-ses-environnements-avec-kubernetes)
  - [Keda](https://keda.sh/) : Event-driven autoscaling
  - `sablier` scaling depuis requêtes sur _Ingress_
  - `krr` : CLI to compute pod requests / limits from existing Prometheus metrics
  - <https://karpenter.sh/> : démarrage / arrêt automatique de noeuds sur le cluster
  - <https://www.kubecost.com> : gestion des coûts des clusters (on-premise + cloud)
  - `ZeroPod` : snapshot et arrêt de Pod lorsque pas d'usage [tuto](https://blog.zwindler.fr/2025/06/20/zeropod-scale-to-zero-kubernetes-checkpointing/)
- 🔄 Upgrade :
  - `WatchTower`
  - `Keel` (avec triggers)
  - `Pluto` : gestion des dépréciations d'API : [tuto](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/pluto/)
- Administration :
  - [auger](https://github.com/etcd-io/auger?tab=readme-ov-file#use-cases) : décode la data d'`etcd`
  - <https://stash.run/> : backup PV
  - [ReShifter](https://github.com/mhausenblas/reshifter) : cluster state management
  - [Velero](https://github.com/heptio/velero) : full cluster backup
  - [kube-backup](https://github.com/pieterlange/kube-backup) : backup YAML dans répo Git
  - [bivac](https://github.com/camptocamp/bivac) : Backup Interface for Volumes Attached to Containers 
  - [Portworx](https://docs.portworx.com/portworx-install-with-kubernetes/storage-operations/create-snapshots/) : [snapshots par annotations](https://docs.portworx.com/portworx-install-with-kubernetes/storage-operations/create-snapshots/snaps-annotations/#taking-periodic-snapshots-on-a-running-pod)

##### Installation de cluster

- 📥 installation => `kubeadm`, `rke`, `kubespray` (supporte Ansible), `rancher`
	- <https://github.com/kubernetes/node-problem-detector> : Détecter les problèmes sur un Node
- CNI :
  - [Tigera](https://github.com/tigera/operator) : gestion du _CNI_ Calico dans le cluster
- [Exemple de configuration des lignes de commandes : kubectl, helm, …](https://git.sr.ht/~toma/dotfiles/tree/main/item/.config/zsh/k8s.sh)
- Multi-clusters :
  - <https://blog.alterway.fr/k0rdent.html>
  - <https://submariner.io/>
  - <https://liqo.io/>
- [Spegel](https://github.com/spegel-org/spegel) : Miroir qui récupère les images Docker sur les Nodes où elles sont en cache

### 💾 Backups

- `bareos`
- `restic`
- `timeshift` (Linux btrfs)

### 🗃️ Infrastructure-as-Code (IaC)

- 🅰️ `ansible` (sans agent)
  - galaxy : grande collection de rôles tout prêts
  - sécurité : voir collection `devsec.hardening` dans ansible galaxy
  - `ansible-vault` (voir `vault`)
	- [ansible-inventory-grapher](https://github.com/willthames/ansible-inventory-grapher) : graph Ansible
- `pulumi` (multi-langages)
  - `pulumi convert --from kubernetes --language <language> --out <output_dir>` : k8s Yaml => pulumi
  - `pulumi convert --from terraform` : terraform HCL => pulumi
  - `pulumi import --from terraform` : import terraform state from `tfstate`
- `terraform`, [OpenTofu : fork Terraform open-source](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/canary-demo?view=azure-devops&tabs=yaml), [Burrito : "ArgoCD for Terraform"](https://github.com/padok-team/burrito)
- 👨‍🍳 `chef` (client/serveur)
- 🤹 `puppet`
- 📦 `packer` : création d'images de VMs
- `semaphore` : UI for operating `ansible`, `terraform/OpenTofu`, `pulumi`. <https://semaphoreui.com/>
- diagrammes : `plantuml`, `mermaid`, `ditaa`, `kroki`, <https://diagrams.mingrammer.com/>, `dot`
- 💲 `Infracost` : track coût plateformes IaC (`Terraform`, …)
- </> `Typer` : librairie Python pour écrire facilement une CLI
- <https://github.com/Textualize/rich> : Rich library for text-based GUI and advanced text formatting in Python
- [Sake](https://github.com/alajmo/sake) : exécution de tâches à distance (SSH, Docker), micro-ansible

### 🛠️ Build tools et dépendances

- 🔄 gestion et update de dépendances => `renovate`, `asdf`, [mise](https://mise.jdx.dev/)
- builds généralistes => `make`, `taskfile`, `packer`
- JS => `npm`, `yarn`, `webpack`
- ☕ Java => `mvn`, `gradle`
  - <https://docs.openrewrite.org/> : refactoring automatique de code pour mise à jour, …
- 🐘 PHP => `composer`
- 󰌠 Python => `venv` + `pip`, `poetry`, `uv`, `pipx`, `hatch`
- Virtual machines => `packer`, `vagrant` (+TUI : <https://github.com/braheezy/violet>), `incus`

### 🔄 CI/CD

#### Serveurs CI

-  `jenkins` : la référence, très configurable, simple, cloud/on-premise
- `teamcity` : très puissant, complexe
- intégré forge logicielle => `Github Actions`, `Gitlab CI`, `Bitbucket`, `Sourcehut`
- `woodpecker CI` : léger, intègre Docker
- `tekton`, `drone` : déployer sa CI/CD dans k8s
- <https://werf.io/> : lier CI/CD et k8s
- <https://www.shipfox.io/> : GitHub runners rapides et moins cher
- <https://www.usemergeable.dev/> : Inbox pour les Pull Requests depuis GitHub

#### Outils CI

- `dagger` : coder son pipeline en `Go`, `Python`, `Typescript` (indépendant du serveur CI/CD)
- `Trivy` : détection de vulnérabilités [lien de présentation](https://blog.stephane-robert.info/docs/securiser/outils/trivy/)
- <https://r2devops.io/> : auditer le pipeline CI/CD
- [Regula](https://blog.stephane-robert.info/post/infra-as-code-policy-check-regula/) : vérifications de sécurité dans code IaC (Terraform, yaml k8s, …)
- `Lynis` : sécurité des configs Linux [tuto](https://blog.stephane-robert.info/docs/securiser/durcissement/lynis/)
- <https://github.com/woodruffw/zizmor> : analyse statique des actions GitHub.

#### CD & Gitops

- `flux` (dans cluster k8s)
- `argocd` [tuto](https://une-tasse-de.cafe/blog/argocd/)

#### 📦 Gestionnaires d'artefacts / dépendances

- tous types : `artifactory`, `nexus`
- Docker, Helm : `Harbor`
  - images Docker avec packages générées à la volée : <https://nixery.dev/>
- tracking dépendances : `Dependency Track` [tuto](https://blog.stephane-robert.info/docs/securiser/analyser-code/dependency-track/)

### 🔐 Administration sécurisée

- `ssh`, `assh` (sur-couche SSH)
  - `wezterm` => terminal tout-en-un (multiplexeur, SSH, …)
- `x-pipe`
- multiplexeurs :
  - `tmux` => la référence, très configurable.
    - [MyNav](https://github.com/GianlucaP106/mynav) : gestionnaire de sessions tmux
    - <https://tmate.io/> : fork de tmux permettant le partage de session.
  - `zellij` => moderne, très simple
  - `wezterm` => terminal tout-en-un (multiplexeur, SSH, …)
  - `screen` => moins utilisé aujourd'hui, support natif de sessions.
- `wazuh` (intégration Docker)
- IDS (Intrusion Detection System) :
  - `Suricata`
  - `Falco` : comportement des conteneurs et des applications : <https://une-tasse-de.cafe/blog/falco/>
- `rkhunter` : détection de rootkits

### 📈 Supervision / Monitoring / Observabilité

- monitoring :
  - `prometheus` (push par `node exporter`, puissant mais lourd) : [tuto](https://blog.stephane-robert.info/docs/observer/metriques/prometheus/) et <https://une-tasse-de.cafe/blog/prometheus/>
    - Liste d'exporters disponibles : <https://prometheus.io/docs/instrumenting/exporters/>
    - Scaling par `thanos`
  - `cAdvisor` => sondes Prometheus automatiques pour conteneurs
	- <https://github.com/robusta-dev/holmesgpt> : Investigate Prometheus with AI
  - `zabbix` (plutôt sysadmin que devops)
  - `hertzbeat` (compatible `prometheus`) : [tuto](https://blog.stephane-robert.info/docs/observer/metriques/hertzbeat/)
- stacks de logging :
  - `ELK` : _Elastricsearch_, _Logstash_, _Kibana_
  - `loki` + `grafana` (pour tester : <https://github.com/grafana/docker-otel-lgtm>) : <https://une-tasse-de.cafe/blog/loki/>
  - `VictoriaMetrics` (pull, très efficace) + `VMAlert` (règles compatibles prometheus) + `grafana`
	- <https://github.com/openobserve/openobserve> : léger
- tracing :
  - `zipkin`
  - `OpenTelemetry`
  - `Jaeger`
- dashboards :
  - `grafana`
  - [`grafterm`](https://github.com/slok/grafterm) similaire à grafana mais dans un terminal
- `netdata`
- `Datadog` [article](https://blog.wescale.fr/datadog-et-lart-de-lobservabilit%C3%A9)
- [Crowdsec](https://blog.stephane-robert.info/docs/securiser/reseaux/crowdsec/) : outil communautaire
- statuspage : <https://hydrozen.io/>
- API monitoring : `checkly`

### 🤫 Gestion des secrets

- `vault` (HashiCorp) : [tuto](https://blog.stephane-robert.info/docs/securiser/secrets/hashicorp-vault/) et <https://une-tasse-de.cafe/blog/vault/>, `OpenBAO` (fork open-source)
- `Sops` (Mozilla, directement dans le fichier)
- `novops` (en mémoire)

### Tâches automatisées

- `cron`
- `dkron`

### 📔 Documentation

- `markdown` : support natif pour beaucoup d'outils
- `asciidoc` : proche markdown, documentations poussées
  - `asciidoctor` : websites from asciidoc
- `pandoc` : transformation de documents d'un format à un autre : md, html, docx, …
- `docusaurus` : wiki
- `MarkItDown`: PDF, PPT, Word vers Markdown
- <https://github.com/getomni-ai/zerox> : PDF, PPT, Word vers Markdown using AI for OCR
- `asciinema` : enregistrement de sessions de terminal

### 🤵 IAM, SSO

- `keycloak`

### 📊 Data, Logs

- `ELK` : `logstash` (Extract-Transform-Load) --> `elasticsearch` BDD NoSQL --> `kibana` (visualisation, ~= `grafana`)
- `fluentd` : logs unifiés
- `benthos` : stream processing
- `zipkin`, `jaeger`, `OpenTelemetry` : tracing multi-services de requêtes
- <https://github.com/cbos/observability-toolkit>

### virtualisation

- `VMWare ESX`
- `kvm`
- `qemu`
- `xen`
- `OpenVZ`
- `lxc`,`lxd` (conteneurs), `incus`

### Débug & instances de test

- Buckets S3 locaux : <https://github.com/minio/minio> : `docker run -p 9000:9000 -p 9001:9001 quay.io/minio/minio server /data --console-address ":9001"`
- Image générant de faux logs : <https://github.com/chentex/random-logger>

## async : queues de messages, brokers

- `kafka`
- `rabbitmq`

## (reverse) proxy, load balancing, service registry

- `nginx`
- `haproxy`
- `consul` : <https://une-tasse-de.cafe/blog/consul/>
- `traefik`

## 🧪 Tests

- 🔗 Voir la [🧪 page de cours sur les tests](/tests)
- Tests unitaires :
  - Java : `Junit`, `TestNG`, `Mockito` (mocks)
  - Python : `Pyunit`, `Pytest`
  - JS : `Jasmine`, `Jest`, `Mocha`, `Vitest`
  - PHP : `PHPUnit`
- <https://argos-ci.com/> : tests visuels (offre gratuite 5000 tests / mois)
- Tests HTTP / API :
  - <https://hurl.dev/>
  - Wiremock (mock API)
  - [ATAC](https://github.com/Julien-cpsn/ATAC)
  - `Swagger`
  - `resto`
  - <https://proxymock.io/> : générateur de Mock HTTP (analyse le payload des requêtes)
- Tests de charge :
  - `Jmeter`
	- `Gatlin`
	- [Vegeta](https://github.com/tsenart/vegeta)
	- `k6` : [exemple](https://github.com/grafana/quickpizza)
- Tests e2e (interface Web principalement) : `Selenium`, `Selenide`, `Geb`, `Testing library`, `Playwright`, `Cypress`
  - [Outil d'automatisation de tests d'acceptance FitNesse et intégration avec Junit](https://fitnesse.org/FitNesse/UserGuide/WritingAcceptanceTests/RunningFromJunit.html)
- BDD : `Cucumber`, `Spock`, `JBehave`
- Tests d'infrastructure : <https://une-tasse-de.cafe/blog/testinfra/>
- <https://testcontainers.com>
- [Outils de test open-source](https://www.guru99.com/best-open-source-testing-tools.html)
- Mutation Testing :
  - <https://stryker-mutator.io/>
  - <https://github.com/loicknuchel/mutation-testing-sample/>
  - <https://pitest.org/>
  - <https://www.arcmutate.com/>
- Données de test :
  - <https://postgresql-anonymizer.readthedocs.io> : anonymiser une BDD Postgresql pour utiliser ses données en tests
  - Génération de fausses données : <https://fakerjs.dev/>

## Backend tools

- IA / LLMs :
  - <https://www.langchain.com/>
	- <https://haystack.deepset.ai/>
	- `vLLM`
	- <https://pollinations.ai/>
	- <https://docs.sillytavern.app/>
- Database :
  - `Postgresql` : `replication manager` pour failover / réplication
  - [DrawDB](https://github.com/drawdb-io/drawdb) : database designer
  - <https://neon.tech> : Serverless Postgres with branching
	- Backend dans 1 seul fichier : `PocketBase`, <https://manifest.build/>
  - <https://kottster.app/> : UI sur la database
- Gestion d'erreurs : `Sentry`
- APIs : `OpenAPI`
- Paiement en ligne : `Stripe`
- Liste et algos d'e-mails jetables : <https://github.com/disposable-email-domains/disposable-email-domains>
- SSO : `GoAuthentik` et [tutoriel SSO et GoAuthentik complet](https://une-tasse-de.cafe/blog/goauthentik/)

## Frontend development

- frameworks :
  - `Angular` : all-in-one, enterprise-ready (heavy, difficult)
  - `React` : most used, heavy, powerfull, quite difficult
  - `Vue` : easy, trending
  - <https://alpinejs.dev/> : minimal, very easy
	- <https://astro.build/> : framework statique / SSR multi-composants (`React`, …). 0 JS par défaut
- Backend : `appwrite`, `firebase`, `nitric`
- animations :
  - Animate text like a typewritter : <https://github.com/mattboldt/typed.js>
  - <https://github.com/julianshapiro/velocity> : speed & performance
- exposer API de dev pour tests :
  - `portr`
- Scanner de technologies de site web : <https://ingredients.work/>
- free icons : <https://tabler.io/icons>
- free images : <https://undraw.co/>
- SVG background patterns : <https://heropatterns.com/>
- <https://frontendchecklist.io/>
- Client-side search : <https://pagefind.app/>
- Système de commentaires utilisant Github : <https://giscus.app/>
- Layouts et composants tout faits : <https://pagedone.io/>, <https://www.preline.co/>, <https://flowbite.com/>
- Affichage de messages et d'alertes : <https://alertifyjs.com/>
- <https://www.happyhues.co/> : palettes de couleurs
- Tables complexes : <https://www.ag-grid.com/>

## 📊 Data science, data mining, machine learning

- Dessin de graphes : `matplotlib`
- Librairies Python : data science : `numpy`, `pandas` ; data mining et ML : `scipy`, `sklearn`
- ETL open-source : `airflow`
- Local LLM : `ollama`, <https://terminaltrove.com/parllama/> (TUI)
- SQL queries on a CSV, Json, Excel file : <https://terminaltrove.com/sqly/>
- MCP : `FastMCP` (idem FastAPI pour MCP)

## Project management

- `projectlibre` : FOSS, gère Gantt, compatible `MS Project`
- `JIRA` : free forever < 10 / team
- Github Pull-request in terminal : <https://github.com/dlvhdr/gh-dash>

## 💻 Outils Poste de travail

- IDE
	- (Neo)vim et [LazyVim][LazyVim].
		- [Kulala](https://www.lazyvim.org/keymaps#kulalanvim) : HTTP requests from Neovim
	- <https://lazyman.dev/> : test de configurations pour `neovim`.
	- Voir le guide : [LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/)
	- [helix][helix] : très inspiré de `vim`.
- clients HTTP :
  - <https://github.com/zaghaghi/openapi-tui>
  - <https://github.com/Julien-cpsn/ATAC>
  - <https://posting.sh/>
  - <https://github.com/ffuf/ffuf> (ressource discovery)
  - <https://github.com/asciimoo/wuzz>
  - <https://github.com/lucaspickering/slumber>
  - <https://github.com/reorx/httpstat> : `cURL` statistics
  - <https://github.com/rs/curlie> : `curl` frontend
  - <https://github.com/ducaale/xh> : focus performance
- bat
- émulateur de terminal : 
  - [alacritty][alacritty] : rapide (utilise le GPU)
  - [foot][foot] : très léger
  - [wezterm][wezterm], [kitty][kitty], [warp][warp] : terminaux avec fonctionnalités supplémentaires
- Multiplexeurs de terminaux :
  - `zellij` : facile pour débuter : `bash <(curl -L zellij.dev/launch)`
  - [tmux][tmux] : le plus populaire
  - <https://mosh.org> : terminal remote (similaire SSH) avec support roaming, déconnexion, …
- shell :
	- `bash`, disponible partout (avec [Oh My Bash][oh-my-bash])
  - `zsh`, plus puissant avec [Oh My ZSH][oh-my-zsh] (voir aussi [awesome-zsh][awesome-zsh])
	- exotiques : `fish` (avec [Fisher][fisher]), [nu][nushell]
- prompt shell (`PS1`) :
	- [pure][pure] : prompt très rapide sous ZSH
	- [poweline][powerline] : très populaire
- Police de caractères (font) : utiliser les versions [nerd-fonts][nerd-fonts], polices recommandées pour coder : `Hack`, `Inconsolata`, `Noto Color Emoji`, `FiraCode`, `VictorMono` (cursif)
  - `fc-list` // `fc-cache -fv` => show available fonts // refresh font cache
- `atuin` => command history with persistence
- lister / explorer des fichiers :
  - [eza][eza] (anciennement `exa`) : alternative à `ls`
    - `eza --header --long --git --icons --sort=ext --tree --accessed --created --modified --group --links --grid --classify` => full eza options
	- [bat][bat] : alternative à `cat`. `bat --list-themes`
	- [yazi][yazi], [n3][nnn] et [ranger][ranger] : explorateurs de fichiers en mode console
	- [fd][fd] : alternative à `find`
	- [ripgrep][rg] (`rg`), [Silver Searcher][ag] (`ag` ), [ack][ack] : alternatives à `grep`
	- [plocate][plocate] : implémentation rapide pour `locate` (plus rapide que `mlocate`)
  - Grep with colors => `grep --color=always <pattern> | less -R`
  - `ls file1.py | entr python /_` => execute cmd on file change
    - `entr -c` => clear screen first
    - `entr -p` => postpone 1st cmd before change
    - `entr -r` => reload a non-stopping cmd
- fuzzy-finder :
	- [fzf][fzf] : `export FZF_DEFAULT_COMMAND='fd . --hidden'`, `docker ps -a | fzf`, `fzf --preview 'bat --style=numbers --color=always --line-range :500 {}'`
- interfaces utilisateurs en mode terminal (TUI):
	- [glow][glow] : lecteur markdown
	- [lazygit][lazygit]
	- `lazysql`
	- [systemctl-tui](https://github.com/rgwood/systemctl-tui)
	- [pipeform](https://github.com/magodo/pipeform) : TUI pour Terraform
	- `ddgr` : recherche Web
	- <https://aider.chat> : AI pair programming
  - `cmus` // `mocp` => audio player
  - `docker run --rm -it browsh/browsh` // `docker run --rm -ti fathyb/carbonyl https://yewtu.be` => terminal-based web browsers
- json viewers and processors :
  - `fx`
	- `jq`
	- `jqp`
	- `vim +set ft=json`
- `column -s ',' -t` => better CSV output
- `bsdtar` => archive management on Linux, includes `rar` format
- `ntfy send ...` => send notification (can use many backends)
- Environnements de développement sous Kubernetes : <https://skaffold.dev/>, <https://tilt.dev/>

### Outils poste de travail DevOps

- [Telepresence](https://www.telepresence.io/) : redirige des services k8s distants sur machine locale pour test (staging, …)
- <https://github.com/ekzhang/bore> : expose service local dans un tunnel TCP
- `Terraform` => `terragrunt`, `tfswitch`, `tgswitch`, `terraform-docs`, `tfsec`, `trivy`
- `Docker` :
  - `lazydocker` => TUI pour gérer des conteneurs Docker
  - `dry` => manage Docker containers and Swarm cluster
  - `ctop`, [dtop](https://github.com/StakeSquid/dtop) => like `top` for containers
- `Kubernetes` :
  - `kubectx` : change context
  - `kubens` : change namespace
  - `kubie` : change context / namespace temporairement
  - `kube-ps1` : show k8s cluster/context in shell
  - `kubecolor` : colored kubectl output
  - `k9s` : Terminal UI k8s management
  - `k8s lens` : graphical cluster management
  - `kube-capacity` : monitor ressources
  - <https://github.com/sl1pm4t/k2tf> : transforme les Yaml k8s en HCL Terraform
	- <https://k8slens.dev/> : IDE dédié à Kubernetes
  - <https://github.com/philippemerle/KubeDiagrams> : génération de diagrammes d'infra d'un cluster
  - Plugins `kubectl` :
    - upgrade : <https://github.com/kubepug/kubepug>
    - sécurité :
      - `kubectl who-can` / [kubectl-who-can](https://github.com/aquasecurity/kubectl-who-can) by Aqua Security
      - `kubectl access-matrix` / [Rakkess (Review Access)](https://github.com/corneliusweig/rakkess) by Cornelius Weig
      - `kubectl rbac-lookup` / [RBAC Lookup](https://github.com/FairwindsOps/rbac-lookup) by FairwindsOps
      - `kubectl rbac-tool` / [RBAC Tool](https://github.com/alcideio/rbac-tool) by insightCloudSec

- Gestion de services :
  - TUI `systemd`: <https://isd-project.github.io/isd/>
  - Lecteur `journalctl`: <https://github.com/Lifailon/lazyjournal>
- `termdbms` : SQL queries in TUI
- <https://github.com/Macmod/godap> : LDAP in TUI
- `otel-tui` : TUI `OpenTelemetry`, `Zipkin`, `Prometheus` : <https://github.com/ymtdzzz/otel-tui>
- `loggo` : TUI for logs : <https://github.com/aurc/loggo>

### Outils poste de travail Admin système

- `systemd-analyze` : analyse du temps de démarrage des services

#### Network

- `aria2` => downloader (HTTP / Magnet)
- `wavemon` => monitor wifi
- `netstat -pultn` => processes with network activity (one shot, listening only)
- `netstat -puatn` => processes with network activity (one shot, including connected)
- `nethogs` => processes with network activity (live)
- `iw dev wlp3s0 info` => get wifi info (including power)
- `iw dev wlp3s0 set txpower fixed 700` => limit wifi power (save battery) to 7dBm (default 22)
- `lsof -i -P -n` => opened ports and connexions
- `netscanner` => network scanner
- `termshark` => packet sniffer using `wireshark` in terminal
- `iftop -i wlan0` => idem `top` mais pour interface réseau
- `iptraf-ng`
- [netshow](https://github.com/taylorwilsdon/netshow) : TUI de monitoring réseau

#### Disk

- `shake` => defragment Ext4
- `lsblk -f` => list software (partitions) with topology
- `blkid` => partitions IDs
- `smartctl -a /dev/sda` => infos on HDD
- `hdparm`
  - `hdparm -C /dev/sda` => current disk state (active vs standby)
  - `hdparm -T /dev/sda` => test RAM reading speed
  - RC service `hdparm` => spin down disk when idle (/etc/conf.d/hdparm)
- Change root mount => `pivot_root`
- `davfs2` => WebDAV mount
- `rmlint` => find duplicates

#### Hardware

- `nmon` => hardware monitoring
- `inxi` // `inxi -xxAv6` => description système
- `lstopo -.txt` => vision graphique système - package `hwloc`
- `lspci` // `lsusb` // `lscpu` => liste pci // usb // cpu
- `usbutils` => installs full `lsusb` on Busybox's distribution
- `powerstat`
- Kernel/CPU bugs => `cat /proc/cpuinfo | grep bug`
- Kernel option `SATA_MOBILE_LPM_POLICY` => 3 (seems recommended by Lenovo SSD)
- Kernel firmwares : `iwlwifi-7265D-29.ucode`

### Desktop

- `mpv` // `mpv --profile=fast` // `mpv --profile=high-quality` => video player
- `geany` => small IDE (alpine)
- `picard` => update mp3 tags graphically and automatically
- `jpegoptim` => optim jpg size
- Zero-loss jpg/png
  - `$ find . -regextype posix-extended -iregex '.*(jpeg|jpg)' -print0 | xargs -0 -n 1 -P $((`nproc`/ 2)) jpegoptim -pt`
  - `$ find . -name \*.png -print0 | xargs -0 -n 1 -P $((`nproc`/ 2)) -I {} zopflipng -m --lossy_8bit --lossy_transparent -y {} {}`
- `wdisplays` // `wlr-randr` => manage displays (`Wayland`) : graphical // textual
- `chattr +i /mnt/backup` => Immutable directory / file
- packages `gst-plugins-good` && `gst-plugins/libav` : req for YouTube videos
  - `gst-plugins-vaadi` for hardware acceleration
- `grim` => screenshots

## Self-hosting

- <https://anubis.techaro.lol/> : proxy pour bloquer les bots (AI, …)
- <https://github.com/Flomp/wanderer> : catalogue de sorties trail

### FOSS alternates

- `dropbox`, `google drive`, `one drive` => `nextcloud`
- `airtable` => `NocoDB`
- `notion` => `appflowy`, <https://affine.pro/>
- `salesforce CRM` => `ERPNext`
- `slack` => `mattermost`
- `zoom`, `teams` => `jitsi`
- `jira` => `plane`
- `asana` => `OpenProject`
- `firebase` => `convex`, `supabase`, `appwrite`, `instant`
- `heroku`, `netlify`, `vercel` => `coolify`, `dokku`, `dokploy`
- `github` => `gitlab`, `forgejo`, `gitea`
- `docusign` => `docuseal`
- `google analytics` => `matomo`
- _google translate_ => <https://libretranslate.com/>
- <https://silex.me/> => création de site web no-code
- <https://capjs.js.org/> : proof-of-work alternatif aux CAPTCHA

## 🔗 Awesome lists

- <<https://www.trackawesomelist.com/ansible-community/awesome-ansible/rss.xml> : awesome Ansible
- <<https://www.trackawesomelist.com/awesome-lists/awesome-bash/rss.xml> : awesome Bash
- <<https://github.com/f/awesome-chatgpt-prompts/commits/main.atom> : awesome ChatGPT prompts
- <https://github.com/cicdops/awesome-ciandcd> : awesome CI/CD
- <<https://www.trackawesomelist.com/agarrharr/awesome-cli-apps/rss.xml> : awesome CLI apps
- <<https://www.trackawesomelist.com/moimikey/awesome-devtools/rss.xml> : awesome Devtools
- <<https://www.trackawesomelist.com/agamm/awesome-developer-first/rss.xml> : awesome Developer-first resources
- <<https://www.trackawesomelist.com/ripienaar/free-for-dev/rss.xml> : awesome Free for Dev
- <https://github.com/veggiemonk/awesome-docker> : awesome Docker
- <https://github.com/docker/awesome-compose> : awesome Docker Compose
- <<https://www.trackawesomelist.com/mendel5/alternative-front-ends/rss.xml> : awesome Front-ends alternative
- <<https://www.trackawesomelist.com/stevemao/awesome-git-addons/rss.xml> : awesome Git addons
- <<https://www.trackawesomelist.com/rockerBOO/awesome-neovim/rss.xml> : awesome Neovim
- <<https://www.trackawesomelist.com/zudochkin/awesome-newsletters/rss.xml> : awesome Newsletters
- <<https://www.trackawesomelist.com/tvvocold/FOSS-for-Dev/rss.xml> : awesome Open-source for Dev
- <<https://www.trackawesomelist.com/jyguyomarch/awesome-productivity/rss.xml> : awesome Productivity
- <<https://www.trackawesomelist.com/ProductivityDirectory/awesome-productivity-tools/rss.xml> : awesome Productivity tools
- <https://www.trackawesomelist.com/public-apis/public-apis/rss.xml> : awesome Public APIs
- <https://www.trackawesomelist.com/vinta/awesome-python/rss.xml> : awesome Python
- <<https://www.trackawesomelist.com/matiassingers/awesome-readme/rss.xml> : awesome Readmes
- <https://github.com/cjbarber/ToolsOfTheTrade> : awesome SaaS
- <<https://www.trackawesomelist.com/awesome-selfhosted/awesome-selfhosted/rss.xml> : awesome Self-hosted
- <<https://www.trackawesomelist.com/alebcay/awesome-shell/rss.xml> : awesome Shell programs
- <<https://www.trackawesomelist.com/awesome-foss/awesome-sysadmin/rss.xml> : awesome Sysadmin
- <<https://github.com/rothgar/awesome-tuis/commits/master.atom> : awesome Terminal UIs
- <<https://www.trackawesomelist.com/shuaibiyy/awesome-terraform/rss.xml> : awesome Terraform
- <https://www.trackawesomelist.com/TheJambo/awesome-testing/rss.xml> : awesome Testing
- <<https://www.trackawesomelist.com/markodenic/web-development-resources/rss.xml> : awesome Web development resources
- <<https://www.trackawesomelist.com/aviaryan/awesome-no-login-web-apps/rss.xml> : awesome No-login Web apps
- <<https://www.trackawesomelist.com/unixorn/awesome-zsh-plugins/rss.xml> : awesome ZSH Plugins



[ack]: https://github.com/beyondgrep/ack3
[ag]: https://github.com/ggreer/the_silver_searcher
[alacritty]: https://alacritty.org/
[awesome-zsh]: https://github.com/unixorn/awesome-zsh-plugins
[bat]: https://github.com/sharkdp/bat
[cmus]: https://cmus.github.io/
[dry]: https://github.com/moncho/dry
[eza]: https://github.com/eza-community/eza
[fd]: https://github.com/sharkdp/fd
[fisher]: https://github.com/jorgebucaran/fisher
[foot]: https://codeberg.org/dnkl/foot
[fzf]: https://github.com/junegunn/fzf
[glow]: https://github.com/charmbracelet/glow
[helix]: https://helix-editor.com/
[k9s]: https://k9scli.io/
[kitty]: https://sw.kovidgoyal.net/kitty/
[lazydocker]: https://github.com/jesseduffield/lazydocker
[lazygit]: https://github.com/jesseduffield/lazygit
[lazyvim]: https://www.lazyvim.org/
[nerd-fonts]: https://www.nerdfonts.com/
[nnn]: https://github.com/jarun/nnn
[nushell]: https://www.nushell.sh/
[oh-my-bash]: https://ohmybash.nntoan.com/
[oh-my-zsh]: https://ohmyz.sh/
[plocate]: https://plocate.sesse.net/
[powerline]: https://github.com/b-ryan/powerline-shell
[pure]: https://github.com/sindresorhus/pure
[ranger]: https://github.com/ranger/ranger
[rg]: https://github.com/BurntSushi/ripgrep
[sc-im]: https://github.com/andmarti1424/sc-im
[screen]: https://www.gnu.org/software/screen/
[term-dbms]: https://github.com/mathaou/termdbms
[tig]: https://jonas.github.io/tig/
[tmux]: https://github.com/tmux/tmux/wiki
[warp]: https://www.warp.dev/
[wezterm]: https://wezfurlong.org/wezterm/index.html
[yazi]: https://github.com/sxyazi/yazi
[zellij]: https://zellij.dev/
[zsh-autosuggestions]: https://github.com/zsh-users/zsh-autosuggestions

