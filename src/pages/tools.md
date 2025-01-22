---
title: Programmes frameworks et outils
date: 2024-10-17
updated: 2024-10-17
---

## Commandes utiles

### 💻 `entr` : réexécute une commande

- `ls file1.py | entr python /_` : réexécute le fichier `file1.py` à chaque sauvegarde
  - `entr -c` : avec clear d'écran
  - `entr -p` : postpone la 1e exécution au 1e changement
  - `entr -r` : redémarre une commande qui tourne en continu

## 🌍 Utilitaires en ligne

- Afficher son IP publique : `curl ifconfig.me/ip` ou `curl ifconfig.me/all.json`
- Aides sur les commandes : `curl cheat.sh/ma_commande`
- `curl wttr.in/Grenoble` => weather at Grenoble, France.

## Outils utiles Devops (liste non exhaustive)

### 🔗 Landscape Devops (liens externes)

- <https://platformengineering.org/platform-tooling>
- <https://xavki.blog/devops-sources/>
- <https://landscape.cncf.io/>

### 1️⃣  Versioning

- `git`
  - forges logicielles => `github`, `gitlab`, `bitbucket` (Atlassian -> `Jira`), `sourcehut`, …
  - sécurité
    - [git-crypt](https://github.com/AGWA/git-crypt)
    - `gittuf` : utilise The Update Framework (TUF) : gestion des clés des développeurs du dépôt, autorisations par branches, fichiers, …
  - outils
    - [gitmoji](https://github.com/carloscuesta/gitmoji) : ajouter des emojis de contexte aux commits
- sémantique :
  - <https://semver.org/>
  - <https://hub.docker.com/r/gittools/gitversion>
- analyses :
  - <https://github.com/gitleaks/gitleaks> : `docker run -v ${PWD}:/path ghcr.io/gitleaks/gitleaks:latest detect --source="/path" -v`
  - <https://github.com/adamtornhill/code-maat> : data mining dans dépôt Git
  - <https://github.com/smontanari/code-forensics>

### 🐳 Conteneurs

- `docker`
  - sécurité :
    - <https://github.com/docker/docker-bench-security>
    - <https://github.com/aquasecurity/trivy> (inclus k8s)
    - `dive`
		- <https://une-tasse-de.cafe/expresso/cosign/> : signer ses images Docker
- `podman` : idem Docker sans agent, supporte Docker et pods k8s
- `cri-o` : container runtime k8s

#### Dockerfile

- vérification : `hadolint`, <https://falco.org/>, <https://quay.github.io/clair/>
- mise à jour : `renovate`

#### Orchestration de conteneurs

- Kubernetes : LA référence en orchestration
  - `k8s` : implémentation principale de Kubernetes
  - `k0s` : implémentation de Docker Enterprise (single binary)
  - `k3s` (installable par `k3d`), `microk8s` (ubuntu) : implémentations légères
  - `minikube` : version 1 noeud simple pour dev/test uniquement
  - `kind` : déploiement local utilisant Docker : [tuto](https://blog.stephane-robert.info/post/kubernetes-kind/)
	- [`Talos` : OS immuable pour k8s](https://une-tasse-de.cafe/blog/talos/)
  - `openshift` : orchestrateur de RedHat
- `swarm` : orchestrateur inclus dans Docker
- `docker compose` : orchestrateur simple de Docker (dev, test, CI/CD, prod simpliste)
- `nomad` : orchestrateur applicatif conteneurisées ou non, simple pour on-premise
- `mesos` + `dc/os`

#### Kubernetes-specific

- linter (vérification fichiers) => `kubeconform`
- installation => `kubeadm`, `rke`, `kubespray`, `rancher`
- package manager (sur-couche) => `helm`
- `rancher` : manager de cluster(s) k8s (installation, monitoring, tests, …)
- ingress & service mesh :
  - `traefik` : reverse-proxy automatique
  - `Consul` (+DNS, reverse proxy, load balancing, …)
  - `Istio` : [article](https://une-tasse-de.cafe/blog/istio/) et observabilité par `Kiali`
	- `Cilium` : networking, security, observability
- scaling
  - [Keda](https://keda.sh/) : Event-driven autoscaling
- sécurité
  - [Popeye](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/popeye/) : vérification de cluster k8s
  - [Kubescape](https://blog.stephane-robert.info/docs/securiser/conteneurs/kubescape/) : scan de clusters, intégration dev et CI/CD
	- [Sealed Secret](https://une-tasse-de.cafe/blog/sealed-secrets/) : chiffrement de secrets dans k8s
- supervision
  - `k9s` : [tuto](https://blog.stephane-robert.info/docs/outils/indispensables/#k9s)
  - `kubevious` : [tuto](https://blog.stephane-robert.info/post/kubernetes-tableau-bord-kubevious/)
- CD
  - `fluxcd` : GitOps
  - `argoscd`
  - `flagger` : blue/green, A/B, canary deployments
- `kubevirt` : Ajout de la gestion de VMs dans Kubernetes
- Consommation d'énergie :
  - `kepler` : monitor Pod energy consumption
	- `kube-green` : k8s operator for energy-saving actions 
	- `krr` : CLI to compute pod requests / limits from existing Prometheus metrics

### 🔙 Backups

- `bareos`
- `restic`
- `timeshift` (Linux btrfs)

### 🗃️ Infrastructure-as-Code (IaC)

- `ansible` (sans agent)
  - galaxy : grande collection de rôles tout prêts
  - sécurité : voir collection `devsec.hardening` dans ansible galaxy
  - `ansible-vault` (voir `vault`)
	- [ansible-inventory-grapher](https://github.com/willthames/ansible-inventory-grapher) : graph Ansible
- `pulumi` (multi-langages)
- `terraform`, [OpenTofu : fork Terraform open-source](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/canary-demo?view=azure-devops&tabs=yaml), [Burrito : "ArgoCD for Terraform"](https://github.com/padok-team/burrito)
- `chef` (client/serveur)
- `puppet`
- `semaphore` : UI for operating `ansible`, `terraform/OpenTofu`, `pulumi`. <https://semaphoreui.com/>
- diagrammes : `plantuml`, `mermaid`, `ditaa`, `kroki`, <https://diagrams.mingrammer.com/>, `dot`
- `Infracost` : track coût plateformes IaC (`Terraform`, …)

### 🛠️ Build tools et dépendances

- gestion et update de dépendances => `renovate`, `asdf`, [mise](https://mise.jdx.dev/)
- builds généralistes => `make`, `taskfile`, `packer`
- JS => `npm`, `yarn`, `webpack`
- Java => `mvn`, `gradle`
- PHP => `composer`
- Python => `venv` + `pip`, `poetry`, `uv`, `pipx`, `hatch`
- Virtual machines => `packer`, `vagrant` (+TUI : <https://github.com/braheezy/violet>), `incus`

### ➿ CI/CD

#### Serveurs CI

- `jenkins` : la référence, très configurable, simple, cloud/on-premise
- `teamcity` : très puissant, complexe
- intégré forge logicielle => `Github Actions`, `Gitlab CI`, `Bitbucket`, `Sourcehut`
- `woodpecker CI` : léger, intègre Docker
- `tekton`, `drone` : déployer sa CI/CD dans k8s

#### Outils CI

- `dagger` : coder son pipeline en `Go`, `Python`, `Typescript` (indépendant du serveur CI/CD)
- `Trivy` : détection de vulnérabilités [lien de présentation](https://blog.stephane-robert.info/docs/securiser/outils/trivy/)
- <https://r2devops.io/> : auditer le pipeline CI/CD
- [Regula](https://blog.stephane-robert.info/post/infra-as-code-policy-check-regula/) : vérifications de sécurité dans code IaC (Terraform, yaml k8s, …)

#### CD & Gitops

- `flux` (dans cluster k8s)
- `argocd` [tuto](https://une-tasse-de.cafe/blog/argocd/)

#### 📦 Gestionnaires d'artefacts / dépendances

- tous types : `artifactory`, `nexus`
- Docker, Helm : `Harbor`
- tracking dépendances : `Dependency Track` [tuto](https://blog.stephane-robert.info/docs/securiser/analyser-code/dependency-track/)
### 🔐 Administration sécurisée

- `ssh`, `assh` (sur-couche SSH)
  - `wezterm` => terminal tout-en-un (multiplexeur, SSH, …)
- `x-pipe`
- multiplexeurs :
  - `tmux` => la référence, très configurable
    - [MyNav](https://github.com/GianlucaP106/mynav) : gestionnaire de sessions
  - `zellij` => moderne, très simple
  - `wezterm` => terminal tout-en-un (multiplexeur, SSH, …)
  - `screen` => moins utilisé aujourd'hui, support natif de sessions.
- clients HTTP : <https://github.com/darrenburns/posting>
- `wazuh` (intégration Docker)
- IDS (Intrusion Detection System) : Suricata

### Supervision / Monitoring / Observabilité

- `prometheus` (push par `node exporter`, puissant mais lourd) + `grafana` => solution classique
  - `cAdvisor` => sondes Prometheus automatiques pour conteneurs
  - [`grafterm`](https://github.com/slok/grafterm) similaire à grafana mais dans un terminal
	- <https://github.com/robusta-dev/holmesgpt> : Investigate Prometheus with AI
- `loki` + `grafana`
- `VictoriaMetrics` (pull, très efficace) + `VMAlert` (règles compatibles prometheus) + `grafana`
- `zabbix` (plutôt sysadmin que devops)
- `netdata`
- `Datadog` [article](https://blog.wescale.fr/datadog-et-lart-de-lobservabilit%C3%A9)
- [Crowdsec](https://blog.stephane-robert.info/docs/securiser/reseaux/crowdsec/) : outil communautaire
- statuspage : <https://hydrozen.io/>
- API monitoring : `checkly`

### 🤫 Gestion des secrets

- `vault` (HashiCorp), `OpenBAO` (fork open-source)
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

### 🤵 IAM, SSO

- `keycloak`

### Data, Logs

- `ELK` : `logstash` (Extract-Transform-Load) --> `elasticsearch` BDD NoSQL --> `kibana` (visualisation, ~= `grafana`)
- `fluentd` : logs unifiés
- `benthos` : stream processing
- `zipkin`, `jaeger`, `OpenTelemetry` : tracing multi-services de requêtes

### virtualisation

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
- `haproxy`
- `consul`
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
- Tests de charge :
  - `Jmeter`
	- `Gatlin`
	- [Vegeta](https://github.com/tsenart/vegeta)
	- `k6` : [exemple](https://github.com/grafana/quickpizza)
- Tests e2e (interface Web principalement) : `Selenium`, `Selenide`, `Geb`, `Testing library`, `Playwright`, `Cypress`
- BDD : `Cucumber`, `Spock`, `JBehave`
- Tests d'infrastructure : <https://une-tasse-de.cafe/blog/testinfra/>
- <https://testcontainers.com>
- <https://postgresql-anonymizer.readthedocs.io> : anonymiser une BDD Postgresql pour utiliser ses données en tests

## Backend tools

- IA / LLMs :
  - <https://www.langchain.com/>
	- <https://haystack.deepset.ai/>
	- `vLLM`
	- <https://pollinations.ai/>
	- <https://docs.sillytavern.app/>
- Database :
  - [DrawDB](https://github.com/drawdb-io/drawdb) : database designer
  - <https://neon.tech> : Serverless Postgres with branching
	- Backend dans 1 seul fichier : `PocketBase`

## Frontend development

- frameworks :
  - `Angular` : all-in-one, enterprise-ready (heavy, difficult)
  - `React` : most used, heavy, powerfull, quite difficult
  - `Vue` : easy, trending
  - <https://alpinejs.dev/> : minimal, very easy
- Backend : `appwrite`, `firebase`
- animations :
  - Animate text like a typewritter : <https://github.com/mattboldt/typed.js>
  - <https://github.com/julianshapiro/velocity> : speed & performance
- exposer API de dev pour tests :
  - `portr`
- Scanner de technologies de site web : <https://ingredients.work/>
- free icons : <https://tabler.io/icons>
- <https://frontendchecklist.io/>

## Data science, data mining, machine learning

- Dessin de graphes : `matplotlib`
- Librairies Python : data science : `numpy`, `pandas` ; data mining et ML : `scipy`, `sklearn`
- ETL open-source : `airflow`
- Local LLM : `ollama`

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
- clients HTTP : <https://github.com/zaghaghi/openapi-tui>, <https://github.com/Julien-cpsn/ATAC>, <https://posting.sh/>
- bat
- émulateur de terminal : 
  - [alacritty][alacritty] : rapide (utilise le GPU)
  - [foot][foot] : très léger
  - [wezterm][wezterm], [kitty][kitty], [warp][warp] : terminaux avec fonctionnalités supplémentaires
- Multiplexeurs de terminaux :
  - `zellij` : facile pour débuter : `bash <(curl -L zellij.dev/launch)`
  - [tmux][tmux] : le plus populaire
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
	- `ddgr` : recherche Web
	- <https://aider.chat> : AI pair programming
  - `cmus` // `mocp` => audio player
  - `docker run --rm -it browsh/browsh` // `docker run --rm -ti fathyb/carbonyl https://youtube.com` => terminal-based web browsers
- json viewers and processors :
  - `fx`
	- `jq`
	- `jqp`
	- `vim +set ft=json`
- `column -s ',' -t` => better CSV output
- `bsdtar` => archive management on Linux, includes `rar` format
- `ntfy send ...` => send notification (can use many backends)

### Outils poste de travail DevOps

- [Telepresence](https://www.telepresence.io/) : redirige des services k8s distants sur machine locale pour test (staging, …)
- <https://github.com/ekzhang/bore> : expose service local dans un tunnel TCP
- `Terraform` => `terragrunt`, `tfswitch`, `tgswitch`, `terraform-docs`, `tfsec`, `trivy`
- `Kubernetes`
  - `kubectx` : change context
	- `kubens` : change namespace
	- `kube-ps1` : show k8s cluster/context in shell
	- `kubecolor` : colored kubectl output
	- `k9s` : Terminal UI k8s management
	- `k8s lens` : graphical cluster management
	- `kube-capacity` : monitor ressources
  - `dry` => manage Docker containers and Swarm cluster
  - `ctop` => like `top` for containers
	- <https://github.com/sl1pm4t/k2tf> : transforme les Yaml k8s en HCL Terraform
- Gestion de services :
  - TUI `systemd`: <https://isd-project.github.io/isd/>
  - Lecteur `journalctl`: <https://github.com/Lifailon/lazyjournal>
- `termdbms` => SQL queries in TUI

### Outils poste de travail Admin système

#### Network

- `aria2` => downloader (HTTP / Magnet)
- `wavemon` => monitor wifi
- `netstat -pultn` => processes with network activity (one shot)
- `nethogs` => processes with network activity (live)
- `iw dev wlp3s0 info` => get wifi info (including power)
- `iw dev wlp3s0 set txpower fixed 700` => limit wifi power (save battery) to 7dBm (default 22)
- `lsof -i -P -n` => opened ports and connexions
- `netscanner` => network scanner
- `termshark` => packet sniffer using `wireshark` in terminal
- `iftop -i wlan0` => idem `top` mais pour interface réseau
- `iptraf-ng`

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

### FOSS alternates

- `dropbox`, `google drive`, `one drive` => `nextcloud`
- `airtable` => `NocoDB`
- `notion` => `appflowy`
- `salesforce CRM` => `ERPNext`
- `slack` => `mattermost`
- `zoom`, `teams` => `jitsi`
- `jira` => `plane`
- `asana` => `OpenProject`
- `firebase` => `convex`, `supabase`, `appwrite`, `instant`
- `heroku`, `netlify`, `vercel` => `coolify`, `dokku`
- `github` => `gitlab`
- `docusign` => `docuseal`
- `google analytics` => `matomo`

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

