---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Bonnes pratiques
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
---

## Services avec état

- Vous pouvez parfaitement conserver vos bases de données de production hors de Kubernetes (surtout si 1 serveur BDD !)
- Mettre les BDD de dev et pre-prod dans le cluster
- Migrer les BDD de prod seulement s'il y en a beaucoup (pour profiter de l'automatisation)
- **Gérer des services avec état dans Kubernetes est compliqué !**

---

## Sécurité globale

- Soyez attentif au _RBAC_
- Utiliser l'_Admission Controller_ sur les pods
- Logiciels à jour : Kubernetes, OS Linux hôte, conteneurs
- Collecter et surveiller les journaux de l'_APIServer_
- Ajouter une _NetworkPolicy_

---

## Sécurité des Secrets

- **Utiliser des `Secret` pour remplacer les variables d'environnement sensibles** (`DB_PASSWORD`, …) des `Deployment`, `StatefulSet`, …
- ~**Ne pas stocker de `Secret` en clair**~ dans des fichiers YAML : Utiliser `Kubeseal` pour les chiffrer.
- Limiter l'accès aux `Secret` avec **Role-Based Access Control (RBAC)** : Par défaut, accès à tous les Secrets du Namespace.
- Activer le **chiffrement des Secrets dans `etcd`** : par défaut les Secrets sont en clair. Attention à l'impact sur les performances.
- Utiliser des **solutions de gestion externe des Secrets** : _HashiCorp Vault_, _AWS Secrets Manager_, _Azure Key Vault_, …

---

## Limitation des ressources

- Dans chaque `Namespace`, créer un `LimitRange` :
  - `defaultRequest.cpu` et `defaultLimit.cpu` petits (`100m`, …)
  - `defaultRequest.memory` et `defaultLimit.memory` en lien avec le workflow standard :
    - `Java`, `Ruby` : `1G`
    - `Go`, `Python`, `PHP`, `Node` : `250M`
- Dans chaque `Namespace`, créer un `ResourceQuota` :
  - `limits.cpu` et `limits.memory` élevés (1/2 cluster, …)
  - limite élevée d'objets (seulement si un contrôleur s'emballe)
- Voir [ces slides sur les limitations de ressources](https://2021-05-enix.container.training/4.yml.html#190)

---

## Découpage en sous-clusters :

- Un cluster par application, des `Namespace` différents pour les environnements ?
- Un cluster par environnement, des `Namespace` différents pour les applications ?
- Tout sur un seul cluster ? Un cluster par combinaison ?
- Un cluster intermédiaire :
  - Cluster de production, cluster de base de données, cluster de développement/préproduction/etc.
  - Cluster de production et de base de données par application, cluster de développement/préproduction/etc. partagé

---

# Certifications

- Kubernetes and Cloud Native Associate (KCNA)
- Certified Kubernetes Application Developer (CKAD)
- Certified Kubernetes Administrator (CKA)
- Certified Kubernetes Security Specialist (CKS)

Pour plus d'information, voir [une explication des différentes formations](https://gist.github.com/bakavets/05681473ca617579156de033ba40ee7a)

---

# Liens

## Installation de clusters et environnements de test

- [Fichiers perso de configuration des lignes de commandes : kubectl, helm, …](https://git.sr.ht/~toma/dotfiles/tree/main/item/.config/zsh/k8s.sh)
- Bacs à sable pour tester k8s : [killercoda](https://killercoda.com/playgrounds/scenario/kubernetes) et <https://labs.play-with-k8s.com/> et <https://kodekloud.com/playgrounds/>
- Mini-distributions : <https://blog.palark.com/small-local-kubernetes-comparison/>
- [Administration de cluster via etcd](https://blog.stephane-robert.info/post/kubernetes-etcd/)
- [Un cluster de production en un éclair avec Talos](https://kdrive.infomaniak.com/app/share/834488/21e24b60-ece5-4445-ba1d-c5adc3c170cc)
- [Installer Kubernetes via kubeadm](https://dev.to/abhay_yt_52a8e72b213be229/how-to-set-up-and-install-a-kubernetes-cluster-a-step-by-step-guide-375j)
- <https://learnk8s.io/production-best-practices/>
- <https://kubernetes.io/docs/tasks/administer-cluster/>

## Documentation, Cours et Formations

- [Site web Kubernetes](https://kubernetes.io/)
- [Introduction à k8s](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/introduction/)
- Cours sur kubernetes :
  - [uptime-formation](https://supports.uptime-formation.fr/05-kubernetes/01_cours_presentation_k8s/)
  - [stephane-robert](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/introduction/)
  - [vidéos xavki](https://www.youtube.com/watch?v=37VLg7mlHu8&list=PLn6POgpklwWqfzaosSgX2XEKpse5VY2v5)
	- <https://container.training/> : Les **excellentes formations (complètes) de Jérôme Petazzoni**, notamment :
	  - [Fondamentaux Kubernetes](https://2021-05-enix.container.training/2.yml.html) : cours complet, de l'installation aux usages de kubernetes
		- [Packaging d'applications et CI/CD pour Kubernetes](https://2021-05-enix.container.training/3.yml.html)
		- [Kubernetes Avancé](https://2021-05-enix.container.training/4.yml.html)
		- [Opérer Kubernetes](https://2021-05-enix.container.training/5.yml.html)
		- <https://github.com/jpetazzo/container.training>
		- [Video - Deep Dive into Kubernetes Internals for Builders and Operators](https://www.youtube.com/watch?v=3KtEAa7_duA)
- [Introduction à kubectl](https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/outils/kubectl/)
- [Livre : Bootstrapping Microservices with Docker, Kubernetes, and Terraform](https://www.manning.com/books/bootstrapping-microservices-with-docker-kubernetes-and-terraform)
- Livre "Kubernetes 101" de Jeff Geerling et [playlist Youtube](https://www.youtube.com/watch?v=IcslsH7OoYo&list=PL2_OBreMn7FoYmfx27iSwocotjiikS5BD) et [dépôt Github](https://github.com/geerlingguy/kubernetes-101)
- <https://kubernetes.io/case-studies/>
- [Kubernetes and Reconciliation Patterns](https://hkassaei.com/posts/kubernetes-and-reconciliation-patterns/)

## Scaling et H/A

- Autoscaling : [doc](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) et [pratique](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
- [HPA Autoscaling depuis des métriques custom dans Prometheus](https://blog.zwindler.fr/2024/10/11/optimisation-ressources-kubernetes-autoscaling-horizontal-custom-metrics-prometheus-adapter/)
- [Kubernetes HA : what if kubernetes internal components go down](https://medium.com/@s.atmaramani/what-if-kubernetes-internal-components-goes-down-6f6372ce0838)
- <https://openai.com/index/scaling-kubernetes-to-7500-nodes/>

## Déploiement d'applications

- [Exemple de déploiement d'une application stateless](https://kubernetes.io/docs/tutorials/stateless-application/guestbook/)
- [Exemple de déploiement d'une application stateful](https://kubernetes.io/docs/tutorials/stateful-application/)
  - [Wordpress avec MySQL](https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
  - [Exemple complet : déploiement d'un cluster ZooKeeper stateful, et maintenance des noeuds](https://kubernetes.io/docs/tutorials/stateful-application/zookeeper/)

### Déploiement continu

- [Blue-Green deployment in k8s](https://developer.harness.io/docs/continuous-delivery/deploy-srv-diff-platforms/kubernetes/kubernetes-executions/create-a-kubernetes-blue-green-deployment/)
- [Canary deployment in k8s](https://learn.microsoft.com/en-us/azure/devops/pipelines/ecosystems/kubernetes/canary-demo?view=azure-devops&tabs=yaml)
- <https://blog.wescale.fr/comment-rendre-une-application-haute-disponibilit%C3%A9-avec-kubernetes>

## Réseau et Service

- Tutoriels sur la communication entre pods :
  - [Utiliser un service](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)
  - [Tutoriel complet](https://medium.com/@extio/mastering-kubernetes-pod-to-pod-communication-a-comprehensive-guide-46832b30556b)
	- [Youtube Xavki : Kubernetes 021 - Services : NodePort, LoadBalancer, ExternalName et notions de Endpoints](https://www.youtube.com/watch?v=tF28iwTco9A)
- <https://www.cortex.io/post/understanding-kubernetes-services-ingress-networking>
- [Video: Kubernetes Ingress Explained (2 Types)](https://www.youtube.com/watch?v=1BksUVJ1f5M)
- [Video (Anton Putra) : How to debug Kubernetes Ingress? (TLS - Cert-Manager - HTTP-01 & DNS-01 Challenges)](https://www.youtube.com/watch?v=DJ2sa49iEKo)
- [Blog: comparaison des types de réseau et de CNI dans Kubernetes (publié par le CNI Calico)](https://docs.tigera.io/calico/latest/networking/determine-best-networking)
- [Fonctionnement interne des Service](https://coroot.com/blog/engineering/a-deep-dive-into-service-to-service-communications/)
- <https://kubernetes.io/docs/tutorials/services/source-ip/> : tester et comprendre l'abstraction de service (NAT, source / destination IP)

## Sécurité

- <https://spacelift.io/blog/kubernetes-secrets>
- [Slides sur cert-manager](https://2021-05-enix.container.training/3.yml.html#205)
- [Connexion à l'API Kubernetes par OpenID (Jérôme Petazzoni)](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/openid-connect.md) : Google account, …
- [Managing Kubernetes Users, Groups, and ServiceAccounts: A Deep Dive with Hands-On Scenarios](https://medium.com/careerbytecode/managing-kubernetes-users-groups-and-serviceaccounts-a-deep-dive-with-hands-on-scenarios-e8d1dde38a22)
- Exemples d'attaques par Pods non sécurisés : <https://github.com/BishopFox/badPods> et [tutoriel](https://bishopfox.com/blog/kubernetes-pod-privilege-escalation)
- [Doc officielle: sécurité](https://kubernetes.io/docs/concepts/security/) notamment [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) et [Sécuriser le noyau Linux hôte](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/)
- [Threat Matrix for Kubernetes (Microsoft)](https://www.microsoft.com/en-us/security/blog/2020/04/02/attack-matrix-kubernetes/)

## Test et debug

- <https://kubernetes.io/docs/tasks/debug/debug-cluster/> et <https://kubernetes.io/docs/tasks/debug/debug-application/>
- <https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/>
- [Simuler la génération de certificats HTTPS pour un cluster de test avec Pebble](https://blog.manabie.io/2021/11/simulate-https-certificates-acme-k8s/)
- Images Docker utiles pour lancer des _Pod_ de débug :
  - <https://github.com/InAnimaTe/echo-server> : mini webserveur affichant le contexte courant sur le port 8080 : Pod, Node, …
  - <https://mauilion.dev/posts/etcdclient/> : image statique de Pod pour tester etcd
  - <https://github.com/kubernetes-up-and-running/kuard> qui affiche des détails sur l'exécution du Pod
  - <https://github.com/jpetazzo/shpod> : image de debug complète, incluant un serveur SSH et kubectl

:::tip
L'image `shpod` est très utile pour du débug, on pourra la lancer depuis une _Helm Chart_ :

```sh
helm upgrade --install --repo https://shpod.in/ shpod shpod \
	--namespace default \
	--set service.type=NodePort \
	--set resources.requests.cpu=0.1 \
	--set resources.requests.memory=500M \
	--set resources.limits.cpu=1 \
	--set resources.limits.memory=500M \
	--set persistentVolume.enabled=true \
	--set "rbac.cluster.clusterRoles={cluster-admin}" \
	--set ssh.authorized_keys="$(cat ~/.ssh/*.pub)"
```
:::

## Extensions courantes

- [Helm: package manager pour déployer dans k8s](https://helm.sh/) et [Introduction à Helm](https://www.aukfood.fr/helm-le-meilleur-ami-de-votre-kubernetes/)
- [Exemple de monitoring Prometheus - Grafana dans un cluster Kubernetes](https://blog.octo.com/exemple-dutilisation-de-prometheus-et-grafana-pour-le-monitoring-dun-cluster-kubernetes)

## Autres

- <https://roadmap.sh/kubernetes>
- Awesome Kubernetes: <https://github.com/tomhuang12/awesome-k8s-resources>
- [Dear Friend, you have built a Kubernetes](https://www.macchaffee.com/blog/2024/you-have-built-a-kubernetes/)
- [Learning Kubernetes, Pods & Deployments with Doom](https://www.youtube.com/watch?v=j9DOWkw9-pc)
- [10 Ways to Shoot Yourself in the Foot with Kubernetes, #9 Will Surprise You (Youtube)](https://www.youtube.com/watch?v=QKI-JRs2RIE)
- [Gitpod: We are leaving Kubernetes](https://www.gitpod.io/blog/we-are-leaving-kubernetes)
- [Scheduler Kubernetes (pour démonstration)](https://github.com/kelseyhightower/scheduler)
- Exemples :
  - de projets : voir la [page des liens](/cours/liens#kubernetes)
  - de fichiers de manifest YAML : <https://github.com/kubernetes-up-and-running/examples>
- Multi-cluster : [Interconnecting Clusters (Jérôme Petazzoni)](https://2021-05-enix.container.training/5.yml.html#186) et <https://www.kubecost.com/kubernetes-multi-cloud/kubernetes-multi-cluster/>
- Tutoriels pour 2 solutions de stockage : [Portworx](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/portworx.md) et [OpenEBS](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/openebs.md)
- <https://une-tasse-de.cafe/blog/operator/> : exemple d'écriture d'un opérateur en Go.

---

# Legal

- Docker®, Docker Swarm and the Docker logo are trademarks or registered trademarks of Docker, Inc. in the United States and/or other countries. Docker, Inc. and other parties may also have trademark rights in other terms used herein.
- Kubernetes® is a registered trademark of The Linux Foundation in the United States and/or other countries
- Other names may be trademarks of their respective owners

