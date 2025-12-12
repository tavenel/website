---
title: Programmes et outils utiles DevOps et poste de travail
created: 2024-10-17
---

## Commandes utiles

### 💻 `entr` : réexécuter une commande

- `ls file1.py | entr python /_` : réexécute le fichier `file1.py` à chaque nouvel enregistrement du fichier
  - `entr -c` : avec clear d'écran
  - `entr -p` : postpone la 1e exécution au 1e changement
  - `entr -r` : redémarre une commande qui tourne en continu

## 🌍 Utilitaires en ligne

- Afficher son IP publique :
  - `curl ifconfig.me/ip`
  - `curl ifconfig.me/all.json`
  - <https://www.monip.org/>
- DNS :
  - `9.9.9.9` (Quad9)
  - [liste standard](https://download.dnscrypt.info/resolvers-list/v3/public-resolvers.md) `dnscrypt`
  - Check website DNS : <https://www.whatsmydns.net/>
  - <https://nip.io/> : DNS résolvant toute IP vers un hostname : `10.0.0.1.nip.io` résoud vers `10.0.0.1`
- ❓ Aides sur les commandes : `curl cheat.sh/ma_commande`
- ⛅ `curl wttr.in/Grenoble` : météo à Grenoble, France.
- <https://bugmenot.com/> : partage de logins
- <https://www.trackawesomelist.com/aviaryan/awesome-no-login-web-apps/rss.xml> : awesome No-login Web apps
- <https://github.com/cjbarber/ToolsOfTheTrade> : awesome SaaS
- <https://www.trackawesomelist.com/zudochkin/awesome-newsletters/rss.xml> : awesome Newsletters
- <https://www.trackawesomelist.com/jyguyomarch/awesome-productivity/rss.xml> : awesome Productivity
- <https://www.trackawesomelist.com/ProductivityDirectory/awesome-productivity-tools/rss.xml> : awesome Productivity tools

## 1️⃣  Versioning

-  Forges logicielles `git`: `github`, 🦊 `gitlab`, `bitbucket` (Atlassian -> `Jira`), `sourcehut`, `forgejo`, `gitea`, `gitbucket`, …
- [jujutsu](https://github.com/jj-vcs/jj) : autre gestionnaire de versions basé sur un backend Git. TUI : [lazyjj](https://github.com/Cretezy/lazyjj)
- Outils Git :
  - 🤪 [gitmoji](https://github.com/carloscuesta/gitmoji) : ajouter des emojis de contexte aux commits
  - <https://alchemists.io/projects/git-lint> : linter de commits Git pour une cohérence des messages
  - <https://github.com/jesseduffield/lazygit> : **formidable TUI git**
  - <https://www.trackawesomelist.com/stevemao/awesome-git-addons/rss.xml> : awesome Git addons
- 🔐 Sécurité :
  - [git-crypt](https://github.com/AGWA/git-crypt)
  - 🔑 `gittuf` : utilise The Update Framework (TUF) : gestion des clés des développeurs du dépôt, autorisations par branches, fichiers, …
  - <https://github.com/gitleaks/gitleaks> : `docker run -v ${PWD}:/path ghcr.io/gitleaks/gitleaks:latest detect --source="/path" -v`
  - <https://github.com/trufflesecurity/trufflehog> : trouver des secrets exposés dans ses dépôts Git
- Versioning sémantique :
  - 1️⃣  <https://semver.org/>
  - 2️⃣ <https://hub.docker.com/r/gittools/gitversion>
  - 3 <https://alchemists.io/projects/milestoner> : automatise la génération de release notes, versioning et déploiements.
- Analyses de dépôt Git :
  - 📊 <https://github.com/adamtornhill/code-maat> : data mining dans dépôt Git
  - 🔎 <https://github.com/smontanari/code-forensics>

## 📦 Conteneurs

###   Docker

- <https://github.com/veggiemonk/awesome-docker> : awesome Docker
- <https://github.com/docker/awesome-compose> : awesome Docker Compose
- 🔒 Sécurité :
  - _Docker Scout_ (inclus dans _Docker desktop_) : voir la [cheatsheet Docker](/docker/cheatsheet)
  - <https://github.com/docker/docker-bench-security>
  - <https://github.com/aquasecurity/trivy> (inclus k8s)
  - <https://une-tasse-de.cafe/expresso/cosign/> : signer ses images Docker
  - `grype` : scan de sécurité des images Docker
- Analyse des images Docker :
  - `dive` : analyse poussée des layers
  - [sou](https://github.com/knqyf263/sou) : analyse simple des layers
  - `Container Structure Test` : tests sur images Docker produites. [tuto](https://blog.stephane-robert.info/docs/conteneurs/outils/container-struct-test/)
  - `dfimage` : recrée (approximativement) un Dockerfile depuis une image Docker : <https://github.com/LanikSJ/dfimage>
- Images légères :
  - Alpine linux : <https://www.alpinelinux.org/>
  - Distroless : <https://blog.garambrogne.net/distroless.html>
  - _Docker Slim_ : réduction drastique de la taille des images déjà buildées
- Images Docker avec packages générées à la volée : <https://nixery.dev/>

### 📄 Dockerfile

- 🧐 Vérification : `hadolint`, <https://falco.org/>, <https://quay.github.io/clair/>
- 🔄 Mise à jour : `renovate`

### Registry

- Hubs publics :
  - Docker Hub : <https://hub.docker.com>
  - Hub Github : <https://ghcr.io/>
  - Hub d'images temporaires : <https://ttl.sh/>
- Registry internes :
  - <https://github.com/Joxit/docker-registry-ui>
  - `gitea`
  - <https://hub.docker.com/_/registry>

### Alternatives à docker

- 🚢 `podman` : idem Docker sans agent, supporte Docker et pods k8s
- `cri-o` : container runtime k8s

### Orchestration de conteneurs

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

## 󱃾 Kubernetes

- Liste d'opérateurs : <https://operatorhub.io/>
- 📦 Package manager (sur-couche) => `helm` (et secrets : <https://github.com/jkroepke/helm-secrets>)
- 🔎 Linter (vérification fichiers) => `kubeconform`, `kube-score`
- [external DNS](https://github.com/kubernetes-sigs/external-dns) : synchronisation Ingress / Service avec DNS externe (Cloud, …)
- <https://chaos-mesh.org/> : chaos computing dans un cluster
- `kubevirt` : Ajout de la gestion de VMs dans Kubernetes
- [auger](https://github.com/etcd-io/auger?tab=readme-ov-file#use-cases) : Décode la data d'`etcd`

### Ingress & service mesh

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

### 🔒 Sécurité

- `kubeseal` et `Sealed Secret` : [tuto 1](https://une-tasse-de.cafe/blog/sealed-secrets/) et [tuto 2](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/sealed-secrets/) : chiffrement de secrets dans k8s
- <https://external-secrets.io/> : injection de secrets (Opérateur et CRDs) : [tuto](https://blog.wescale.fr/synchronisation-des-secrets-dans-votre-cluster-kubernetes-avec-external-secrets)
- `cert-manager` : gestion des certificats SSL/TLS [tuto](https://une-tasse-de.cafe/blog/cert-manager/)
- <https://github.com/kubernetes-sigs/security-profiles-operator> : Opérateur SELinux, Apparmor, Seccomp

#### Analyse de clusters

- `polaris` : détection de problèmes de sécurité dans un cluster
- Benchmark CIS : <https://github.com/aquasecurity/kube-bench>
- [Popeye](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/popeye/) : recherche de problèmes de sécurité dans un cluster k8s
- [Kubescape](https://blog.stephane-robert.info/docs/securiser/conteneurs/kubescape/) : scan de clusters, intégration dev et CI/CD
- <https://www.kuboscore.io/> : vérification de clusters
- <https://github.com/topiaruss/kogaro> : vérification d'erreurs classiques de configuration, intégration CI/CD

### 🧐 Supervision

- <https://github.com/stern/stern> : logs multi-pods
- <https://codeberg.org/hjacobs/kube-janitor> : Supprimes des ressources Kubernetes après un certain temps
- <https://www.tigera.io/> : Unified Network Security & Observability for Kubernetes
- <https://github.com/gianlucam76/k8s-cleaner> : détection et notification de ressources non utilisées

### 🚀 CD

- `fluxcd` : GitOps
- `argocd` : <https://une-tasse-de.cafe/blog/argocd/>
  - <https://kargo.io/> : promotion de pipelines (test,staging,prod,…). [tuto](https://piotrminkowski.com/2025/01/14/continuous-promotion-on-kubernetes-with-gitops/)
  - <https://devtron.ai/> : alternative à `Kargo`
- `flagger` : blue/green, A/B, canary deployments

### 🪫 FinOps

- But : réduire la consommation d'énergie et le pricing
- `kepler` : monitor Pod energy consumption : <https://sustainable-computing.io/>
- `kube-green` : k8s operator for energy-saving actions. [tuto](https://blog.octo.com/arreter-ses-environnements-avec-kubernetes)
- [Keda](https://keda.sh/) : Event-driven autoscaling
- `sablier` scaling depuis requêtes sur _Ingress_
- `krr` : CLI to compute pod requests / limits from existing Prometheus metrics
- <https://karpenter.sh/> : démarrage / arrêt automatique de noeuds sur le cluster
- <https://www.kubecost.com> : gestion des coûts des clusters (on-premise + cloud)
- `ZeroPod` : snapshot et arrêt de Pod lorsque pas d'usage [tuto](https://blog.zwindler.fr/2025/06/20/zeropod-scale-to-zero-kubernetes-checkpointing/)

### 📦📦 Scaling

- [Keda](https://keda.sh/) : Event-driven autoscaling
- `Goldilocks` : génération de recommendations de _requests_ et _limits_
- <https://github.com/jthomperoo/predictive-horizontal-pod-autoscaler> : modèles prédictifs pour auto-scaling (HPA)

### Installation de cluster

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

### 🔄 Upgrade de cluster

- `WatchTower`
- `Keel` (avec triggers)
- Gestion des dépréciations d'API :
  - `Pluto` : [tuto](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/pluto/)
  - <https://github.com/doitintl/kube-no-trouble>

### Backup de cluster

- <https://stash.run/> : backup PV
- [Velero](https://github.com/heptio/velero) : full cluster backup
- [kube-backup](https://github.com/pieterlange/kube-backup) : backup YAML dans répo Git
- [bivac](https://github.com/camptocamp/bivac) : Backup Interface for Volumes Attached to Containers
- [Portworx](https://docs.portworx.com/portworx-install-with-kubernetes/storage-operations/create-snapshots/) : [snapshots par annotations](https://docs.portworx.com/portworx-install-with-kubernetes/storage-operations/create-snapshots/snaps-annotations/#taking-periodic-snapshots-on-a-running-pod)

## 🗃️ Infrastructure-as-Code (IaC)

- `ansible` : sans agent ni état, configuration fine d'une ou plusieurs ressources
  - <https://www.trackawesomelist.com/ansible-community/awesome-ansible/rss.xml> : awesome Ansible
- `terraform` : avec état, CRUD de ressources similaires
- `pulumi` (multi-langages)
  - `pulumi convert --from kubernetes --language <language> --out <output_dir>` : k8s Yaml => pulumi
  - `pulumi convert --from terraform` : terraform HCL => pulumi
  - `pulumi import --from terraform` : import terraform state from `tfstate`
- 👨‍🍳 `chef` (client/serveur)
- 🤹 `puppet`
- 📦 `packer` : création d'images de VMs
- `semaphore` : UI for operating `ansible`, `terraform/OpenTofu`, `pulumi`. <https://semaphoreui.com/>
- 💲 `Infracost` : track coût plateformes IaC (`Terraform`, …)
- [Sake](https://github.com/alajmo/sake) : exécution de tâches à distance (SSH, Docker), micro-ansible

### 🅰️ Ansible

- galaxy : grande collection de rôles tout prêts
- sécurité : voir collection `devsec.hardening` dans ansible galaxy
- `ansible-vault` (voir `vault`)
- [ansible-inventory-grapher](https://github.com/willthames/ansible-inventory-grapher) : graph Ansible

### Terraform

- `terraform`, [OpenTofu : fork Terraform open-source](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/canary-demo?view=azure-devops&tabs=yaml), [Burrito : "ArgoCD for Terraform"](https://github.com/padok-team/burrito)
- Linter :`terragrunt`, `trivy`, `tflint`
- `Terraform Compliance` / `Checkov` : Analyse IaC pour conformité et sécurité.
- `terraform-docs` : outil pour documenter ses modules Terraform
- <https://github.com/sl1pm4t/k2tf> : transforme les Yaml k8s en HCL Terraform
- <https://github.com/magodo/pipeform> : TUI pour Terraform
- <https://www.trackawesomelist.com/shuaibiyy/awesome-terraform/rss.xml> : awesome Terraform

## 🛠️ Build tools et dépendances

- 🔄 gestion et update de dépendances => `renovate`, `asdf`, [mise](https://mise.jdx.dev/)
- builds généralistes => `make`, `taskfile`, `packer`
- JS => `npm`, `yarn`, `webpack`
- ☕ Java => `mvn`, `gradle`
  - <https://docs.openrewrite.org/> : refactoring automatique de code pour mise à jour, …
- 🐘 PHP => `composer`
- 󰌠 Python => `venv` + `pip`, `poetry`, `uv`, `pipx`, `hatch`
- Virtual machines => `packer`, `vagrant` (+TUI : <https://github.com/braheezy/violet>), `incus`

## 🔄 CI/CD

### Serveurs CI

-  `jenkins` : la référence, très configurable, simple, cloud/on-premise
- `teamcity` : très puissant, complexe
- intégré forge logicielle => `Github Actions`, `Gitlab CI`, `Bitbucket`, `Sourcehut`
- `woodpecker CI` : léger, intègre Docker
- `tekton`, `drone` : déployer sa CI/CD dans k8s
- <https://werf.io/> : lier CI/CD et k8s
- <https://www.shipfox.io/> : GitHub runners rapides et moins cher
- <https://www.usemergeable.dev/> : Inbox pour les Pull Requests depuis GitHub

### Outils CI

- `dagger` : coder son pipeline en `Go`, `Python`, `Typescript` (indépendant du serveur CI/CD)
- <https://github.com/woodruffw/zizmor> : analyse statique des actions GitHub.
- <https://github.com/cicdops/awesome-ciandcd> : awesome CI/CD

#### 🛡️ Sécurité

- <https://r2devops.io/> : auditer le pipeline CI/CD
- [Regula](https://blog.stephane-robert.info/post/infra-as-code-policy-check-regula/) : vérifications de sécurité dans code IaC (Terraform, yaml k8s, …)
- `Lynis` : sécurité des configs Linux [tuto](https://blog.stephane-robert.info/docs/securiser/durcissement/lynis/)
- `dependabot` : mise à jour des dépendances (Github Actions)
- `CodeQL` (GitHub) ou `Semgrep` : Analyse statique orientée sécurité.
- `Hadolint` : Analyse des Dockerfiles pour bonnes pratiques et sécurité.
- `gitleaks` recherche des vulnérabilités dans un dépôt Git (mots de passe en clair, …)
- `Trivy` : détection de vulnérabilités [lien de présentation](https://blog.stephane-robert.info/docs/securiser/outils/trivy/) : Scan d'images Docker, dépendances, dépôts Git pour vulnérabilités (CVE).
- `r2devops` / `regula` permettent d'auditer le code à la recherche de CVE
- `Snyk` : Analyse de dépendances + suggestions de correction.
- `Gitleaks` : Détection de secrets/API keys dans le code.
- `OWASP ZAP` : Test d'intrusion automatisé des APIs/web apps.
- _Open Policy Agent_ (`OPA`) : Validation de règles (policies) dans le pipeline.
- `Conftest` : Contrôle d'infra-as-code (Terraform, K8s YAML) contre des règles internes.

### CD & Gitops

- `flux` (dans cluster k8s)
- `argocd` [tuto](https://une-tasse-de.cafe/blog/argocd/)

### 📦 Gestionnaires d'artefacts / dépendances

- tous types : `artifactory`, `nexus`
- Docker, Helm : `Harbor`
- tracking dépendances : `Dependency Track` : Gestion du _SBOM_ (_Software Bill of Materials_).

## 📈 Supervision / Monitoring / Observabilité

- `netdata`
- `Datadog` [article](https://blog.wescale.fr/datadog-et-lart-de-lobservabilit%C3%A9)
- [Crowdsec](https://blog.stephane-robert.info/docs/securiser/reseaux/crowdsec/) : outil communautaire
- API monitoring : `checkly`
- OCSInventory => inventaire automatique et gestion de parc de machines
- GLPI => gestion de parc, ticketing, …

### Monitoring

- `prometheus` (push par `node exporter`, puissant mais lourd) : [tuto](https://blog.stephane-robert.info/docs/observer/metriques/prometheus/) et <https://une-tasse-de.cafe/blog/prometheus/>
  - Liste d'exporters disponibles : <https://prometheus.io/docs/instrumenting/exporters/>
- Scaling par `thanos`
- `cAdvisor` => sondes Prometheus automatiques pour conteneurs
  - <https://github.com/robusta-dev/holmesgpt> : Investigate Prometheus with AI
- `zabbix` (plutôt sysadmin que devops)
- `hertzbeat` (compatible `prometheus`) : [tuto](https://blog.stephane-robert.info/docs/observer/metriques/hertzbeat/)
- <https://github.com/coroot/coroot> : monitoring eBPF

### Logging

- `ELK` : _Elastricsearch_, _Logstash_, _Kibana_
- `loki` + `grafana` (pour tester : <https://github.com/grafana/docker-otel-lgtm>) : <https://une-tasse-de.cafe/blog/loki/>
- `VictoriaMetrics` (pull, très efficace) + `VMAlert` (règles compatibles prometheus) + `grafana`
  - <https://github.com/openobserve/openobserve> : léger

### Tracing

- `zipkin`
- `OpenTelemetry`
- `Jaeger`

### Dashboards

- `grafana`
- [`grafterm`](https://github.com/slok/grafterm) similaire à grafana mais dans un terminal

## 🤫 Gestion des secrets

- `vault` (HashiCorp) : [tuto](https://blog.stephane-robert.info/docs/securiser/secrets/hashicorp-vault/) et <https://une-tasse-de.cafe/blog/vault/>, `OpenBAO` (fork open-source)
- `Sops` (Mozilla, directement dans le fichier)
- `novops` (en mémoire)

## Tâches automatisées

- `cron`
- `dkron`

## 📔 Documentation

- `markdown` : support natif pour beaucoup d'outils
- `asciidoc` : proche markdown, documentations poussées
  - `asciidoctor` : websites from asciidoc
- `pandoc` : transformation de documents d'un format à un autre : md, html, docx, …
- `docusaurus` : wiki
- `MarkItDown`: PDF, PPT, Word vers Markdown
- <https://github.com/getomni-ai/zerox> : PDF, PPT, Word vers Markdown using AI for OCR
- <https://typst.app/> : écriture proche de markdown puis génération automatique de documents, slides, … en utilisant des templates
- `asciinema` : enregistrement de sessions de terminal
- Diagrammes : `plantuml`, `mermaid`, `ditaa`, `kroki`, <https://diagrams.mingrammer.com/>, `dot`
  - Comparaison de librairies générant des diagrammes depuis Markdown : <https://support.typora.io/Draw-Diagrams-With-Markdown/>
- <https://www.trackawesomelist.com/matiassingers/awesome-readme/rss.xml> : awesome Readmes

## 🤵 IAM, SSO

- `keycloak`
- `GoAuthentik` et [tutoriel SSO et GoAuthentik complet](https://une-tasse-de.cafe/blog/goauthentik/)

## VPN

- Wireguard
  - Dashboard : <https://wgdashboard.dev/>

## 💾 Sauvegarde

- `bareos`
- `restic`
- `timeshift` (Linux btrfs)

## 📊 Data, Logs

- `ELK` : `logstash` (Extract-Transform-Load) --> `elasticsearch` BDD NoSQL --> `kibana` (visualisation, ~= `grafana`)
- `fluentd` : logs unifiés
- `benthos` : stream processing
- `zipkin`, `jaeger`, `OpenTelemetry` : tracing multi-services de requêtes
- <https://github.com/cbos/observability-toolkit>

## virtualisation

- `VMWare ESX`
- `kvm`
- `qemu`
- `xen`
- `OpenVZ`
- `lxc`,`lxd` (conteneurs), `incus`

## async : queues de messages, brokers

- `kafka`
- `rabbitmq`

## (reverse) proxy, load balancing, service registry

- `nginx`
  - <https://nginxui.com/> : statistics, logs, tests, …
- `haproxy`
- `consul` : <https://une-tasse-de.cafe/blog/consul/>
- `traefik`

## 🧪 Tests

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
- Tests de charge et stress tests :
  - `Jmeter`
  - `Gatlin`
  - [Vegeta](https://github.com/tsenart/vegeta)
  - `k6` : [exemple](https://github.com/grafana/quickpizza)
  - stress-ng (charge CPU et mémoire d'un système Linux) : <https://github.com/ColinIanKing/stress-ng/>
- Tests e2e (interface Web principalement) :
  - `Testing library` : utilisation de sélecteurs indépendants des frameworks de test
  - `Selenium`
    - et variations : `Selenide`, `Geb`
  - `Playwright` et son serveur MCP : <https://github.com/microsoft/playwright-mcp>
  - `Cypress`
  - [Outil d'automatisation de tests d'acceptance FitNesse et intégration avec Junit](https://fitnesse.org/FitNesse/UserGuide/WritingAcceptanceTests/RunningFromJunit.html)
- BDD : `Cucumber`, `Spock`, `JBehave`
- Tests d'infrastructure : <https://une-tasse-de.cafe/blog/testinfra/>
- [Outils de test open-source](https://www.guru99.com/best-open-source-testing-tools.html)
- Mutation Testing :
  - <https://stryker-mutator.io/>
  - <https://github.com/loicknuchel/mutation-testing-sample/>
  - <https://pitest.org/>
  - <https://www.arcmutate.com/>
- Données de test :
  - <https://postgresql-anonymizer.readthedocs.io> : anonymiser une BDD Postgresql pour utiliser ses données en tests
  - Génération de fausses données : <https://fakerjs.dev/> et <https://generatedata.com/>
- <https://testcontainers.com>
- Image générant de faux logs : <https://github.com/chentex/random-logger>
- <https://www.trackawesomelist.com/TheJambo/awesome-testing/rss.xml> : awesome Testing

## Backend tools

- Gestion d'erreurs : `Sentry`
- APIs : `OpenAPI`
- Paiement en ligne : `Stripe`
- Liste et algos d'e-mails jetables : <https://github.com/disposable-email-domains/disposable-email-domains>
- <https://github.com/Textualize/rich> : Rich library for text-based GUI and advanced text formatting in Python
- </> `Typer` : librairie Python pour écrire facilement une CLI
- <https://www.trackawesomelist.com/public-apis/public-apis/rss.xml> : awesome Public APIs
- <https://www.trackawesomelist.com/vinta/awesome-python/rss.xml> : awesome Python

### IA / LLMs

- <https://www.langchain.com/>
  - <https://haystack.deepset.ai/>
  - `vLLM`
  - <https://pollinations.ai/>
  - <https://docs.sillytavern.app/>
- `litLLM` : aggreggation de LLMs : <https://docs.litellm.ai/docs/>
  - [À la découverte de liteLLM, une plateforme pour les gouverner tous](https://www.youtube.com/watch?v=L8CeGZ0Pf5o)
- <https://github.com/f/awesome-chatgpt-prompts/commits/main.atom> : awesome ChatGPT prompts

### Database

- `Postgresql` : `replication manager` pour failover / réplication
- [DrawDB](https://github.com/drawdb-io/drawdb) : database designer
- <https://neon.tech> : Serverless Postgres with branching
  - Backend dans 1 seul fichier : `PocketBase`, <https://manifest.build/>
- <https://kottster.app/> : UI sur la database

## Frontend development

- Backend : `appwrite`, `firebase`, `nitric`
- Scanner de technologies de site web : <https://ingredients.work/>
- `Wappalyzer` : extension détectant les technologies utilisées par un site Web
- Fonds de cartes Open-Street Map : <http://maps.stamen.com>
- <https://www.trackawesomelist.com/mendel5/alternative-front-ends/rss.xml> : awesome Front-ends alternative
- <https://www.trackawesomelist.com/markodenic/web-development-resources/rss.xml> : awesome Web development resources

### Validation

- <https://frontendchecklist.io/>

### Frameworks

- `Angular` : all-in-one, enterprise-ready (heavy, difficult)
- `React` : most used, heavy, powerfull, quite difficult
- `Vue` : easy, trending
- <https://alpinejs.dev/> : minimal, very easy
- <https://astro.build/> : framework statique / SSR multi-composants (`React`, …). 0 JS par défaut

### CSS

- Minimal CSS Framework for Semantic HTML : <https://picocss.com/>
- Diagnostic CSS (highlight issues) :
  - <https://meyerweb.com/eric/tools/css/diagnostics/index.html>
  - <https://meyerweb.com/eric/tools/favelets/>

### Composants

- Layouts et composants tout faits : <https://pagedone.io/>, <https://www.preline.co/>, <https://flowbite.com/>
- Tables complexes : <https://www.ag-grid.com/>

### Librairies JS

- Système de commentaires utilisant Github : <https://giscus.app/>
- Affichage de messages et d'alertes : <https://alertifyjs.com/>
- Client-side search : <https://pagefind.app/>
- Animations :
  - Animate text like a typewritter : <https://github.com/mattboldt/typed.js>
  - <https://github.com/julianshapiro/velocity> : speed & performance

### UI

- <https://www.happyhues.co/> : palettes de couleurs
- Générateur de couleurs accessibles : <https://randoma11y.com>
- free icons : <https://tabler.io/icons>
- free images : <https://undraw.co/>
- SVG background patterns : <https://heropatterns.com/>

## 📊 Data science, data mining

- Dessin de graphes : `matplotlib`
- Librairies Python : data science : `numpy`, `pandas` ; data mining et ML : `scipy`, `sklearn`
- ETL open-source : `airflow`
- SQL queries on a CSV, Json, Excel file : <https://terminaltrove.com/sqly/>

## Project management

- `JIRA` : free forever < 10 / team

## Cybersécurité

### Outils généraux

- Outil brute-foce pour Répertoire/fichier, DNS & virtual host : <https://github.com/OJ/gobuster>
- Collection de listes de mots, données, … à utiliser en analyses : <https://github.com/danielmiessler/SecLists>
- Vérification de leak de crédentials (Git, CI, Docker, …) : <https://github.com/trufflesecurity/trufflehog>
- `rkhunter` : détection de rootkits

### 🔐 Administration sécurisée

- `ssh`, `assh` (sur-couche SSH)
  - blocage connexions : `fail2ban`, `SSHGuard` ([tuto](https://loud-technology.com/insight/sshguard-protection-ssh-alternative-fail2ban/))
- `x-pipe`
- `wazuh` (intégration Docker)
- IDS (Intrusion Detection System) :
  - `Suricata`
  - `Falco` : comportement des conteneurs et des applications : <https://une-tasse-de.cafe/blog/falco/>, <https://falco.org/>
  - <https://tetragon.io/> : eBPF-based Security Observability and Runtime Enforcement
- <https://localcert.net/> : certificats gratuits en `.localcert.net` pour réseau privé

## IA

- <https://aider.chat> : AI pair programming (TUI in terminal)
- Local LLM : `ollama`, <https://terminaltrove.com/parllama/> (TUI)
- [Extension Firefox et Chrome pour alerter sur les sites générés par IA](https://next.ink/164873/outils-next-une-extension-chrome-et-firefox-pour-etre-alerte-des-sites-genai/)

### MCP

- Liste de serveurs MCP : <https://github.com/modelcontextprotocol/servers>
- `FastMCP` (idem FastAPI pour MCP)

### Free IAs

- <https://chatgpt.com/>
- <https://chat.mistral.ai/chat>
- <https://gemini-free.com/>

## 💻 Outils Poste de travail

### CLI

- `column -s ',' -t` => better CSV output
- `bsdtar` => archive management on Linux, includes `rar` format
- <https://github.com/charmbracelet/glow> : lecteur markdown
- `ddgr` : recherche Web
- `cmus` // `mocp` => audio player
- `docker run --rm -it browsh/browsh` // `docker run --rm -ti fathyb/carbonyl https://yewtu.be` => terminal-based web browsers
- fuzzy-finder : <https://github.com/junegunn/fzf> : `export FZF_DEFAULT_COMMAND='fd . --hidden'`, `docker ps -a | fzf`, `fzf --preview 'bat --style=numbers --color=always --line-range :500 {}'`
- Grep avec couleurs : `grep --color=always <pattern> | less -R`
- `atuin` => command history with persistence
- <https://github.com/sharkdp/bat> : cat amélioré (coloration syntaxique, …)
  - `bat --list-themes`
- <https://www.trackawesomelist.com/agarrharr/awesome-cli-apps/rss.xml> : awesome CLI apps
- <https://github.com/rothgar/awesome-tuis/commits/master.atom> : awesome Terminal UIs

#### json viewers and processors

- `fx`
- `jq`
- `jqp`
- `vim +set ft=json`
- <https://github.com/tomnomnom/gron> : greppable json

#### Explorateurs de fichiers

- <https://github.com/eza-community/eza> (anciennement `exa`) : alternative à `ls`
  - `eza --header --long --git --icons --sort=ext --tree --accessed --created --modified --group --links --grid --classify` => full eza options
  - <https://github.com/sxyazi/yazi>, <https://github.com/jarun/nnn>, et <https://github.com/ranger/ranger> : explorateurs de fichiers en mode console
  - <https://github.com/sharkdp/fd> : alternative à `find`
  - [ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`), [Silver Searcher](https://github.com/ggreer/the_silver_searcher) (`ag` ), [ack](https://github.com/beyondgrep/ack3) : alternatives à `grep`
  - <https://plocate.sesse.net/> : implémentation rapide pour `locate` (plus rapide que `mlocate`)
- `ls file1.py | entr python /_` => execute cmd on file change
  - `entr -c` => clear screen first
  - `entr -p` => postpone 1st cmd before change
  - `entr -r` => reload a non-stopping cmd

#### Terminal

##### Émulateur de terminal

- <https://alacritty.org/> : rapide (utilise le GPU)
- <https://codeberg.org/dnkl/foot> : très léger
- Terminaux avec fonctionnalités supplémentaires :
  - <https://wezfurlong.org/wezterm/> : terminal, multiplexer, SSH
  - <https://sw.kovidgoyal.net/kitty/>
  - <https://www.warp.dev/>

##### Multiplexeurs de terminaux

- `zellij` : facile pour débuter, moderne : `bash <(curl -L zellij.dev/launch)`
- <https://github.com/tmux/tmux/wiki> : la référence, très configurable.
  - <https://github.com/GianlucaP106/mynav> : gestionnaire de sessions tmux
  - <https://tmate.io/> : fork de tmux permettant le partage de session.
- <https://mosh.org> : terminal remote (similaire SSH) avec support roaming, déconnexion, …
- `wezterm`
- `screen` => moins utilisé aujourd'hui, support natif de sessions.

##### Shell

- `bash`, disponible partout
  - plugins : [Oh My Bash](https://ohmybash.nntoan.com/)
  - <https://www.trackawesomelist.com/awesome-lists/awesome-bash/rss.xml> : awesome Bash
- `zsh`, plus puissant
  - plugins : [Oh My ZSH](https://ohmyz.sh/)
  - ZSH expert features : <https://thevaluable.dev/zsh-expansion-guide-example/>
  - <https://github.com/unixorn/awesome-zsh-plugins>
- exotiques :
  - `fish` (avec <https://github.com/jorgebucaran/fisher>)
  - <https://www.nushell.sh/>
- prompt shell (`PS1`) :
  - [pure](https://github.com/sindresorhus/pure) : prompt très rapide sous ZSH
  - [powerline](https://github.com/b-ryan/powerline-shell) : très populaire
- Police de caractères (font) : utiliser les versions <https://www.nerdfonts.com/>, polices recommandées pour coder : `Hack`, `Inconsolata`, `Noto Color Emoji`, `FiraCode`, `VictorMono` (cursif)
  - `fc-list` // `fc-cache -fv` => show available fonts // refresh font cache
- <https://www.trackawesomelist.com/alebcay/awesome-shell/rss.xml> : awesome Shell programs

### Environnement graphique

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
- `ntfy send ...` => send notification (can use many backends)

### Outils poste de travail Développeur

- `ngrok` : rendre les applications locales accessibles sur Internet (Ingress)
- `portr` : expose API de dev pour tests
- <https://github.com/sectordistrict/intentrace> : trace les appels système (similaire `strace`) mais avec une explication sur leur sens
- Github Pull-request in terminal : <https://github.com/dlvhdr/gh-dash>
- <https://www.trackawesomelist.com/moimikey/awesome-devtools/rss.xml> : awesome Devtools
- <https://www.trackawesomelist.com/agamm/awesome-developer-first/rss.xml> : awesome Developer-first resources
- <https://www.trackawesomelist.com/ripienaar/free-for-dev/rss.xml> : awesome Free for Dev
- <https://www.trackawesomelist.com/tvvocold/FOSS-for-Dev/rss.xml> : awesome Open-source for Dev

#### IDE

- (Neo)vim et <https://www.lazyvim.org/>
  - [Kulala](https://www.lazyvim.org/keymaps#kulalanvim) : HTTP requests from Neovim
  - <https://www.trackawesomelist.com/rockerBOO/awesome-neovim/rss.xml> : awesome Neovim
  - <https://lazyman.dev/> : test de configurations pour `neovim`.
  - Voir le guide : [LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/)
- <https://helix-editor.com/> : très inspiré de `vim`.

#### Clients HTTP

- Alternatives à Postman : <https://blog.shevarezo.fr/post/2025/10/22/alternatives-postman-local-first-sans-compte>
- <https://github.com/zaghaghi/openapi-tui>
- <https://github.com/Julien-cpsn/ATAC>
- <https://posting.sh/>
- <https://github.com/ffuf/ffuf> (ressource discovery)
- <https://github.com/asciimoo/wuzz>
- <https://github.com/lucaspickering/slumber>
- <https://github.com/reorx/httpstat> : `cURL` statistics
- <https://github.com/rs/curlie> : `curl` frontend
- <https://github.com/ducaale/xh> : focus performance

### Poste de travail DevOps

- <https://github.com/ekzhang/bore> : expose service local dans un tunnel TCP
- `otel-tui` : TUI `OpenTelemetry`, `Zipkin`, `Prometheus` : <https://github.com/ymtdzzz/otel-tui>
- <https://www.localstack.cloud/> et <https://azure.localstack.cloud/> : déploiements locaux simulant les services cloud AWS et Azure (payant mais version d'essai et version gratuite GitHub students)

#### Docker

- `lazydocker` => TUI pour gérer des conteneurs Docker
- `dry` => manage Docker containers and Swarm cluster
- `ctop`, [dtop](https://github.com/StakeSquid/dtop) => like `top` for containers
- `dcv` (_Docker Container Viewer_) : TUI Docker et Docker Compose <https://github.com/tokuhirom/dcv>

#### Kubernetes

- <https://github.com/philippemerle/KubeDiagrams> : génération de diagrammes d'infra d'un cluster
- Environnements de développement sous Kubernetes : <https://skaffold.dev/>, <https://tilt.dev/>
- Scan de cluster et diagnostics par IA : <https://github.com/k8sgpt-ai/k8sgpt>

##### Outils et extensions kubectl

- `kubectx` : change context
- `kubens` : change namespace
- `kubie` : change context / namespace temporairement
- `kube-ps1` : show k8s cluster/context in shell
- `kubecolor` : colored kubectl output
- <https://github.com/keisku/kubectl-explore> : kubectl extension pour chercher dans la doc avec un "fuzzy finder"
- Plugins `kubectl` :
  - upgrade : <https://github.com/kubepug/kubepug>
  - sécurité :
    - `kubectl who-can` / [kubectl-who-can](https://github.com/aquasecurity/kubectl-who-can) by Aqua Security
    - `kubectl access-matrix` / [Rakkess (Review Access)](https://github.com/corneliusweig/rakkess) by Cornelius Weig
    - `kubectl rbac-lookup` / [RBAC Lookup](https://github.com/FairwindsOps/rbac-lookup) by FairwindsOps
    - `kubectl rbac-tool` / [RBAC Tool](https://github.com/alcideio/rbac-tool) by insightCloudSec

##### Dashboard

- `k9s` : Terminal UI k8s management
  - [tuto](https://blog.stephane-robert.info/docs/outils/indispensables/#k9s)
- `kubevious` : [tuto](https://blog.stephane-robert.info/post/kubernetes-tableau-bord-kubevious/)
- `k8s lens` : graphical cluster management
- `kube-capacity` : monitor ressources
- <https://codeberg.org/hjacobs/kube-web-view> : remplacement R/O du web dashboard, supporte le multi-cluster
- <https://grogg.app/> : dashboard de gestion k8s (app native ou extension vscode)
- <https://github.com/kubernetes-sigs/kui> : version graphique de `kubectl`
- <https://k8slens.dev/> : IDE dédié à Kubernetes avec vision des ressources
- <https://github.com/kbterm/kubeterm> : application de dashboard k8s (desktop et mobile)

##### Génération de Yaml

- <https://kube-composer.com/>
- <https://k8syaml.com/>

##### Exposition de services pour test

- <https://www.telepresence.io/> : redirige des services k8s distants sur machine locale pour test (staging, …)
- <https://github.com/hcavarsan/kftray> : dashboard kubectl forward et reverse tunnel (similaire ngrok) pour k8s

### Poste de travail Admin système

- `loggo` : TUI for logs : <https://github.com/aurc/loggo>
- <https://github.com/Macmod/godap> : LDAP in TUI
- Buckets S3 locaux : <https://github.com/minio/minio> : `docker run -p 9000:9000 -p 9001:9001 quay.io/minio/minio server /data --console-address ":9001"`
- <https://www.trackawesomelist.com/awesome-foss/awesome-sysadmin/rss.xml> : awesome Sysadmin

#### Services

- `systemd-analyze` : analyse du temps de démarrage des services
- [systemctl-tui](https://github.com/rgwood/systemctl-tui)
- Lecteur `journalctl`: <https://github.com/Lifailon/lazyjournal>
- TUI `systemd`: <https://isd-project.github.io/isd/>
- TUI `sysctl` : <https://github.com/orhun/systeroid>

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
- <https://github.com/taylorwilsdon/netshow> : TUI de monitoring réseau

#### Disk

- `ncdu`, `gdu` : espace disque
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

#### Database

- `termdbms` : SQL queries in TUI
- `lazysql`

## Self-hosting

- <https://anubis.techaro.lol/> : proxy pour bloquer les bots (AI, …)
- <https://github.com/Flomp/wanderer> : catalogue de sorties trail
- statuspage : <https://hydrozen.io/>
- <https://www.trackawesomelist.com/awesome-selfhosted/awesome-selfhosted/rss.xml> : awesome Self-hosted

### FOSS alternates

- `dropbox`, `google drive`, `one drive` => `nextcloud`
- `airtable` => `NocoDB`
- `notion` => `appflowy`, <https://affine.pro/>
- `salesforce CRM` => `ERPNext`
- `slack` => `mattermost`
- `zoom`, `teams` => `jitsi`
- `jira` => `plane`
- `asana` => `OpenProject`
- `MS Project` => `projectlibre` : gère Gantt, compatible `MS Project`
- `firebase` => `convex`, `supabase`, `appwrite`, `instant`
- `heroku`, `netlify`, `vercel` => `coolify`, `dokku`, `dokploy`
- `github` => `gitlab`, `forgejo`, `gitea`
- `docusign` => `docuseal`
- `google analytics` => `matomo`
- _google translate_ => <https://libretranslate.com/>
- <https://silex.me/> => création de site web no-code
- <https://capjs.js.org/> : proof-of-work alternatif aux CAPTCHA
- <https://framatalk.org> : video conference without account
- <http://framadate.org/> et <https://polls.fr/> (anonyme et liens directs vers choix - utile pour chat) : sondages
- <https://openfeedback.io/> : Get feedback (free)
- <https://github.com/ether/etherpad-lite/wiki/Sites-That-Run-Etherpad> etherpads : éditions collaboratives
- <https://cijoint.org/> envoi de fichier (<100MB), chiffré côté client
- <https://tlk.io/> instant chatrooms
- remote clipboards :
  - <https://pastebin.com> : share code lines
  - <http://www.olissea.com/PP/PP.php> : also sends mail
- [QR code](https://lehollandaisvolant.net/tout/tools/qrcode/) generator
- <https://yewtu.be> frontend alternatif pour YouTube
- Proxy YouTube : <https://www.proxfree.com/youtube-proxy.php>

### Hébergeurs

- <https://www.zaclys.com> _chaton_ français (hébergeur indépendant) : `nextcloud` (presque tous les plugins), `searx`, `rssfeed`, mail, ....
- <https://www.chapril.org/> _chaton_ de l'April : nombreux services
- <https://leviia.com> hébergeur indépendant français : `nextcloud` et `OnlyOffice` sur stockage OVH.
