---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Sécurité dans Kubernetes
layout: '@layouts/CoursePartLayout.astro'
tags:
- docker
- kubernetes
- devops
- security
---

# 🔐 Authentification et autorisation

---

## 📋 Généralités

- L'authentification (_authn_, vérification de l'identité) s'effectue par _TLS mutuel_ 🔄
  - Le client et le serveur doivent tous deux détenir un certificat valide 📜
- L'autorisation (_authz_, vérification des droits) s'effectue de différentes manières :
  - _api-server_ : **RBAC** 🔑
  - Certains services délèguent l'autorisation à l'_api-server_ (**webhooks**) 🌐
  - Certains services nécessitent un certificat signé par une _autorité de certification_ (_CA_) 📜

---

# 🔐 Authentification (authn)

- Nombreuses méthodes _authn_ lors d'une requête _api-server_ (génère username, identifiant, groupes) 📋
- L'_api-server_ ne les interprète pas : tâche des _autorizers_ (_authz_). 🔄

---

## 🔑 Méthodes authn

- Certificats clients TLS (clusters `kubeadm`) 🔒
- Bearer tokens (header HTTP) 🔑
- Autre proxy authn devant l'_api-server_ 🌐
- Méthodes authn(s) actuelle(s) dans : `~/.kube/config` 📂

---

### 🚫 Requêtes anonymes

- Si **une** méthode authn renvoie `rejects` : requête refusée `401 Unauthorized` ❌
- Requête anonyme (si aucun accept / reject par aucune méthode authn) :
  - _username_ : `system:anonymous` 👤
  - _liste des groupes_ : `system:unauthenticated` 👥
  - Par défaut ne peut rien faire ❌

---

## 🔒 authn par certificats TLS

- Dans presque tous les déploiements 🌐
- _username_ : `CN` du certificat client 👤
- _liste des groupes_ : `O` du certificat client 👥
- L'_api-server_ peut aussi valider les certificats clients par un CA custom. 🔄

---

### 🔐 authn kubelet

- _Kubelet_ s'authentifie souvent par certificats : `O=system:nodes`, `CN=system:node:name-of-the-node` 🔒
- L'API Kubernetes peut agir comme un CA (encapsule une _CSR X509_ dans une `CertificateSigningRequest`) 🔄
- Permet au _Kubelet_ de renouveler son propre certificat 🔄
- Peut émettre des certificats utilisateur 👤
- Pas de révocation de certificat (clé compromise, …) par l'_api-server_ : [issue #18982](https://github.com/kubernetes/kubernetes/issues/18982) ❌
- => **Certificats de courte durée (quelques heures)** ⏳

---

## 🔑 authn par token

- Transmis par en-têtes HTTP : `Authorization: Bearer …` 🔑
- Validés de différentes manières :
  - En dur dans un fichier sur l'_api-server_ 📂
  - [Bootstrap tokens](https://kubernetes.io/docs/reference/access-authn-authz/bootstrap-tokens/) : création cluster, ajout _Node_ 🌐
  - [OpenID Connect Token](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) : _authn_ par fournisseurs externe `OAuth2` 🌐
  - `ServiceAccount` : [create-token](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#create-token) 🔑

---

## 🔑 Autres méthodes authn

- Autres types de tokens 🔑
- Clés d'API externes : _AWS EKS_, … 🔑

---

# 🔐 Autorisations (authz)

- Plusieurs méthodes appelées [authorizers](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#authorization-modules), notamment :
  - [Webhook](https://kubernetes.io/docs/reference/access-authn-authz/webhook/) (chaque requête API est soumise à un service externe pour approbation) 🌐
  - [Role-Base Access System (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) : associe dynamiquement les permissions aux utilisateurs 🔑

---

## 🔄 Pods et ServiceAccount

- Un _Pod_ est associé à un _ServiceAccount_ (par défaut : `default`, sans droits) 🔄
- Le token associé est dans le Pod : `/var/run/secrets/kubernetes.io/serviceaccount/token` 🔑

---

# 🛡️ Sécurisation du _Control Plane_

---

- De nombreux composants acceptent les connexions (et les requêtes) d'autres composants :
  - `api-server` 🌐
  - `etcd` 📂
  - `Kubelet` 🔄
- Nous devons sécuriser ces connexions :
  - Pour refuser les requêtes non autorisées ❌
  - Pour empêcher l'interception de secrets, de _tokens_ et d'autres informations sensibles 🔒

---

## 📂 etcd

- Stocke toute l'information du Cluster (`Secret`, …) et souvent **non chiffrée** (performances) 📂
- Client : port `2379` 🌐
- Coordination / réplication des noeuds : port `2380` 🌐
- _authn_ : TLS, sous-CA 🔒
- _authz_ : Kubernetes ~~n'utilise pas le RBAC interne de _etcd_~~ => tous les droits 🔑
- Voir : [Documentation etcd sur l'authentification](https://etcd.io/docs/current/op-guide/authentication/) et [PKI The Wrong Way](https://www.youtube.com/watch?v=gcOLDEzsVHI) à la KubeCon NA 2020 📚

---

## 🔄 Kubelet et api-server

- Communication bidirectionnelle _Kubelet_ <-> _api-server_ 🔄
- Enregistrement _Kubelet_ -> _api-server_ : le Kubelet demande les pods à démarrer/arrêter. 🔄
- Communication _api-server_ -> _Kubelet_ : pour actions logs, exec, attach 🔄

---

## 🌐 Clients _api-server_

- Depuis le _Control Plane_ :
  - _authn_ : certificats (`subject` ou `CN`) 🔒
  - _authz_ : souvent RBAC 🔑
- _api-server_ : `--client-ca-file`, `--tls-cert-file`, `--tls-private-key-file` 📂
- Client _api-server_ : `--kubeconfig` contenant le certificat CA, la clé client et le certificat client 📂
  - Certificat _Scheduler_ : `CN=system:kube-scheduler` 🔒
  - Certificat _Kubelet_ (-> _api-server_) : `CN=system:node:<nodename>` et groupes `O=system:nodes`. 🔒
  - Certificat _Controller Manager_ : `CN=system:kube-controller-manager` 🔒

---

## 🔄 api-server -> Kubelet

- _Kubelet_ démarré avec `--client-ca-file` (généralement même CA que l'_api-server_) 🔒
- L'_api-server_ utilise une paire de clés dédiée pour contacter le _Kubelet_ : `--kubelet-client-certificate` et `--kubelet-client-key` 🔑
- _authz_ par _webhooks_ activé dans _Kubelet_ par `--authorization-mode=Webhook` 🌐
  - Le Kubelet renvoie une requête à l'_api-server_ pour demander si "cette personne peut effectuer cette opération ?" 🔄

---

## 🔄 Controller manager

- Pour utiliser l'API `CertificateSigningRequest` le _Controller Manager_ a besoin du certificat et de la clé du CA (transmis avec `--cluster-signing-cert-file` et `--cluster-signing-key-file`) 🔒
- Le _Controller Manager_ génère aussi les tokens pour les `ServiceAccount` 🔑

---

### 🔑 ServiceAccount tokens

- _authn_ à l'_api-server_ : un token _JWT_ par `ServiceAccount` 🔑
- Signé par une paire de clés:
  - Privée (signature) transmise au _Controller Manager_ : `--service-account-private-key-file` et `--root-ca-file` 🔑
  - Publique (vérification) transmise à l'_api-server_ : `--service-account-key-file` 🔑
- Le _kube-proxy_ tourne souvent en `DaemonSet` : propre `ServiceAccount` (=> token _JWT_) 🔄

---

## 🔐 Authentification par jeton en pratique

```console
$ API=$(kubectl get svc kubernetes -o json | jq -r .spec.clusterIP)

$ curl -k https://$API # Connexion anonyme 

{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"system:anonymous\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403
}

$ kubectl get ServiceAccount
NAME      SECRETS   AGE
default   0         7h33m

$ kubectl create token default

eyJhbGciOiJSUzI1NiIsImtpZCI6IjFKVHBxWE1ac0RoVURfVjdWdjNSeEtTMVZsdk5qUFR3Q1U5eldUanlxcWcifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzQzNjE3Nzk2LCJpYXQiOjE3NDM2MTQxOTYsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiMmViMDNjYTYtYWY4MC00YTNjLWI3OTMtYWVkYjZlM2YyYmEyIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRlZmF1bHQiLCJ1aWQiOiJkYTY4ODVhMC1jZGE1LTRhNmUtYThmZC1iZTdjMzZkNzIwMGUifX0sIm5iZiI6MTc0MzYxNDE5Niwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.BjaXxdFx-w5cclykMycsEh-WbgSHwWl5z3fkm-StWkARa2MLRjTwjsT1LM1RGqutmPv4qMy9PXoua1VW4rNs8BeEy0rppG9txDKjMr1utXCgnlYJLnW80B9rTJIl_VfyVWJnvuaBnilZEyrS1_NuT1irC0GVAPexhTd6D7bHyCpB63xq1_3DjSHjoY0pK9R8VYGCa6aYR8ByyqFj5vSs-mJ7EImHEV2RqyyrQBKX3FlezZvt9q9E-ouB0I45oA1galGmOX3v7wHSHUas9qdB1FO7bEaNppud2JHXXKUUzGhkhB57IBSBuIO1sTcDQg9JXbHbaLYbC1DiBd9XL9IOoQ

$ curl -k -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFKVHBxWE1ac0RoVURfVjdWdjNSeEtTMVZsdk5qUFR3Q1U5eldUanlxcWcifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzQzNjE3Nzk2LCJpYXQiOjE3NDM2MTQxOTYsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiMmViMDNjYTYtYWY4MC00YTNjLWI3OTMtYWVkYjZlM2YyYmEyIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRlZmF1bHQiLCJ1aWQiOiJkYTY4ODVhMC1jZGE1LTRhNmUtYThmZC1iZTdjMzZkNzIwMGUifX0sIm5iZiI6MTc0MzYxNDE5Niwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.BjaXxdFx-w5cclykMycsEh-WbgSHwWl5z3fkm-StWkARa2MLRjTwjsT1LM1RGqutmPv4qMy9PXoua1VW4rNs8BeEy0rppG9txDKjMr1utXCgnlYJLnW80B9rTJIl_VfyVWJnvuaBnilZEyrS1_NuT1irC0GVAPexhTd6D7bHyCpB63xq1_3DjSHjoY0pK9R8VYGCa6aYR8ByyqFj5vSs-mJ7EImHEV2RqyyrQBKX3FlezZvt9q9E-ouB0I45oA1galGmOX3v7wHSHUas9qdB1FO7bEaNppud2JHXXKUUzGhkhB57IBSBuIO1sTcDQg9JXbHbaLYbC1DiBd9XL9IOoQ" https://$API

{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {},
  "status": "Failure",
  "message": "forbidden: User \"system:serviceaccount:default:default\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {},
  "code": 403

## Accès encore refusé (authz) mais l'utilisateur est authentifié (authn).
```

---

## 🌐 Webhooks
- Ressources (`kind:`) spécifiques pour les autorisations, dont les `SubjectAccessReview`. 📋
- _authz_ par webhooks : envoi d'un `SubjectAccessReview` à l'_api-server_ pour autoriser chaque requête (réponse `allow` ou `deny`). 🔄

---

### SubjectAccessReview

Ex: vérifier si `jean.doe` peut `get pods -n kube-system`:

```bash
kubectl -v9 create -f- <<EOF
apiVersion: authorization.k8s.io/v1
kind: SubjectAccessReview
spec:
  user: jean.doe
  groups:
  - foo
  - bar
  resourceAttributes:
    #group: blah.k8s.io
    namespace: kube-system
    resource: pods
    verb: get
    #name: web-xyz1234567-pqr89
EOF
```

---

# 🔒 Sécurité dans le Cluster

---

## 🔐 Role-Based Access Control (RBAC)

- _authz_ par règles d'autorisation : [verbes](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#determine-the-request-verb) (`create`, `get`, `list`, `update`, `delete`, …) / [ressources](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources) (`Pod`, `Service`, …) / nom de ressource 📋
- `Role` : profil permettant des accès / actions / ressources dans un namespace (`ClusterRole` : dans tout le cluster) 🔑
- `ServiceAccount` : user applicatif 🔑
  - Génère des token (secrets) : à monter par exemple dans un `Pod` pour permettre l'accès 🔑
  - Utilisés pour accorder des autorisations aux applications, services, … 🔑
- `RoleBinding` (`ClusterRoleBinding`) : association `ServiceAccount` <-> `Role` (`ClusterRole`) 🔄

---

### 🔑 `ClusterRoles` par défaut

- `cluster-admin` peut *tout faire* (pensez à `root` sous UNIX) 🔑
- `admin` peut faire *presque tout* (sauf, par exemple, modifier les quotas et les limites de ressources). 🔑
- `edit` est similaire à `admin`, mais ne permet pas d'afficher ni de modifier les permissions. 🔑
- `view` a un accès en lecture seule à la plupart des ressources, à l'exception des permissions et des secrets. 🔑
- Par défaut, les CRD ne sont pas inclus dans `view` / `edit` / etc. ❌

:::tip
*Dans de nombreux cas, ces rôles suffisent.* ✅
:::

---

### 📋 Verbes `list` vs. `get`

- ⚠️ `list` accorde (aussi) des droits de lecture aux ressources ! 📋
:::warn
- **Si un contrôleur doit pouvoir lister les secrets, il pourra aussi les lire** 📋
:::

---

## 🌐 NetworkPolicies

- Par défaut :
  - Un `Pod` peut communiquer avec tout autre `Pod`, y compris d'autres `Namespace` 🔄
  - Un `Service` est accessible partout, y compris depuis d'autres `Namespace` 🌐
- Une `NetworkPolicy` permet d'**ajouter** de l'isolation :
  - Si un `Pod` n'est _sélectionné_ par **aucune `NetworkPolicy`** : **aucune isolation** 🔄
  - Si un `Pod` **est _sélectionné_** par au moins une `NetworkPolicy` : **isolation totale par défaut** (sauf règles acceptées par la `NetworkPolicy`) 🔒
  - **Stateful** : isolation à la **connexion**, et ~non par paquet~ 🔄
  - Pour communication Pod A -> Pod B : accepter A vers B (`egress`) **et** B depuis A (`ingress`) 🔄
:::warn
Certains CNI ne supportent pas (totalement) les _NetworkPolicies_ : la ressource est appliquée mais sans effet ! ⚠️
:::

---

## 🔄 AdmissionController Statiques

- **Acceptent / refusent** ou **modifient** la création de ressources 🔄
- Ex : valeurs par défaut (image pull secret, sidecars, env var), interdire les tag `latest`, exiger `request` et `limits`, … 🔄
- Intégrés à l'_API Server_ : `kube-apiserver -h | grep enable-admission-plugins` 🔄
- Voir [la liste des AdmissionController](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/), notamment le [PodSecurityAdmission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) et [comment l'utiliser dans un Namespace](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/#requiring-the-baseline-pod-security-standard-with-namespace-labels) 📚

---

## 🌐 AdmissionController Dynamiques

- _Webhooks_ **dynamiques** (ajoutables/supprimables à la volée) 🌐
- **Dans** (`service.name` & `service.namespace`) ou **en-dehors** (`https://…`) du cluster 🌐
- L'_API Server_ et le _webhook_ s'échangent des `AdmissionReview` 🔄
- Voir [les extensions des AdmissionController](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/), le [contenu d'une requête](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#request), les [Admission Webhooks : `ValidatingWebhookConfiguration` & `MutatingWebhookConfiguration`](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#admission-webhooks) 📚
- Voir aussi [les slides de formation : Dynamic Admission Control (Jérôme Petazzoni)](https://github.com/jpetazzo/container.training/blob/main/slides/k8s/admission.md) 📚

---

```plantuml
@startuml
left to right direction
' skinparam linetype ortho

title: Kubernetes API request lifecycle

rectangle {
  rectangle "API Handler" as API
  rectangle "Auth" as Auth
  rectangle "Mutating\nAdmission" as Mutate
  rectangle "Object Schema\nValidation" as Schema
  rectangle "Validating\nAdmission" as Validate
  rectangle "ETCD\nPersistence" as ETCD
}

' Webhooks with different color
rectangle "Webhook Code\nImplementation" as MutatingWebhook #cyan
rectangle "Webhook Code\nImplementation" as ValidatingWebhook #cyan

' Main flow
API --> Auth
Auth --> Mutate
Mutate --> Schema
Schema --> Validate
Validate --> ETCD

' Webhook interactions
Mutate --> MutatingWebhook #blue : <color:blue>Registered Webhook</color>
MutatingWebhook --> Mutate #blue : <color:blue>ModifiedRequest</color>

Validate --> ValidatingWebhook #blue : <color:blue>Registered Webhook</color>
ValidatingWebhook --> Validate #blue : <color:blue>Validation Decision</color>

@enduml
```

---

## 🔍 ValidatingAdmissionPolicy

- Nouvelle alternative simple aux _Validating Admission Webhook_ 🌐
- Utilisent le _Common Expression Language_ (`CEL`) 📜
- Voir la [documentation officielle](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) 📚

---

