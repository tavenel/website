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

# Authentification et autorisation

---

## Généralités

- L'authentification (_authn_, vérification de l'identité) s'effectue par _TLS mutuel_
  - Le client et le serveur doivent tous deux détenir un certificat valide

- L'autorisation (_authz_, vérification des droits) s'effectue de différentes manières :
	- _api-server_ : **RBAC**
	- Certains services délèguent l'autorisation à l'_api-server_ (**webhooks**)
	- Certains services nécessitent un certificat signé par une _autorité de certification_ (_CA_)

---

# Authentification (authn)

- Nombreuses méthodes _authn_ lors d'une requête _api-server_ (génère username, identifiant, groupes)
- L'_api-server_ ne les interprète pas : tâche des _autorizers_ (_authz_).

---

## Méthodes authn

- Certificats clients TLS (clusters `kubeadm`)
- Bearer tokens (header HTTP)
- Autre proxy authn devant l'_api-server_
- Méthodes authn(s) actuelle(s) dans : `~/.kube/config`

---

### Requêtes anonymes

- Si une méthode authn renvoie _rejects_ : requête refusée `401 Unauthorized`
- Requête anonyme (si aucun accept / reject par aucune méthode authn) :
  - _username_ : `system:anonymous`
  - _liste des groupes_ : `system:unauthenticated`
  - par défaut ne peut rien faire

---

## authn par certificats TLS

- Dans presque tous les déploiements
- _username_ : `CN` du certificat client
- _liste des groupes_ : `O` du certificat client
- L'_api-server_ peut aussi valider les certificats clients par un CA custom.

---

### authn kubelet

- _Kubelet_ s'authentifie souvent par certificats : `O=system:nodes`, `CN=system:node:name-of-the-node`
- L'API Kubernetes peut agir comme un CA (encapsule une _CSR X509_ dans une `CertificateSigningRequest`)
- Permet au _Kubelet_ de renouveler son propre certificat
- Peut émettre des certificats utilisateur
- Pas de révocation de certificat (clé compromise, …) par l'_api-server_ : [issue #18982](https://github.com/kubernetes/kubernetes/issues/18982))
- => Certificats de courte durée (quelques heures) !

---

## authn par token

- Transmis par en-têtes HTTP : `Authorization: Bearer …`
- Validés de différentes manières :
	- en dur dans un fichier sur l'_api-server_
	- [Bootstrap tokens](https://kubernetes.io/docs/reference/access-authn-authz/bootstrap-tokens/) : création cluster, ajout _Node_
  - [OpenID Connect Token](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#openid-connect-tokens) : _authn_ par fournisseurs externe `OAuth2`
  - `ServiceAccount` : [create-token](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#create-token)

---

## Autres méthodes authn

- Autres types de tokens
- Clés d'API externes : _AWS EKS_, …

---

# Autorisations (authz)

- Plusieurs méthodes appelées [authorizers](https://kubernetes.io/docs/reference/access-authn-authz/authorization/#authorization-modules), notamment :
	- [Webhook](https://kubernetes.io/docs/reference/access-authn-authz/webhook/) (chaque requête API est soumise à un service externe pour approbation)
	- [Role-Base Access System (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) : associe dynamiquement les permissions aux utilisateurs

---

## Pods et ServiceAccount

- Un _Pod_ est associé à un _ServiceAccount_ (par défaut : `default`, sans droits)
- Le token associé est dans le Pod : `/var/run/secrets/kubernetes.io/serviceaccount/token`

---

# Sécurisation du _Control Plane_

---

- De nombreux composants acceptent les connexions (et les requêtes) d'autres composants :

- `api-server`
- `etcd`
- `Kubelet`

- Nous devons sécuriser ces connexions :
	- Pour refuser les requêtes non autorisées
	- Pour empêcher l'interception de secrets, de _tokens_ et d'autres informations sensibles

---

## etcd

- Client : port `2379`
- Coordination / réplication des noeuds : port `2380`
- _authn_ : TLS, sous-CA
- _authz_ : Kubernetes ~~n'utilise pas le RBAC interne de _etcd_~~ => tous les droits
- Voir : [Documentation etcd sur l'authentification](https://etcd.io/docs/current/op-guide/authentication/) et [PKI The Wrong Way](https://www.youtube.com/watch?v=gcOLDEzsVHI) à la KubeCon NA 2020

---

## Kubelet et api-server

- Communication bidirectionnelle _Kubelet_ <-> _api-server_
- Enregistrement _Kubelet_ -> _api-server_ : le Kubelet reçoit les pods à démarrer/arrêter.
- Communication _api-server_ -> _Kubelet_ : pour actions logs, exec, attach

---

## Clients _api-server_

- Depuis le _Control Plane_ :
	- _authn_ : certificats (`subject` ou `CN`)
	- _authz_ : souvent RBAC

- _api-server_ : `--client-ca-file`, `--tls-cert-file`, `--tls-private-key-file`
- Client _api-server_ : `--kubeconfig` contenant le certificat CA, la clé client et le certificat client
  - Certificat _Scheduler_ : `CN=system:kube-scheduler`
	- Certificat _Kubelet_ (-> _api-server_) : `CN=system:node:<nodename>` et groupes `O=system:nodes`.
  - Certificat _Controller Manager_ : `CN=system:kube-controller-manager`

---

## api-server -> Kubelet

- _Kubelet_ démarré avec `--client-ca-file` (généralement même CA que l'_api-server_)
- L'_api-server_ utilise une paire de clés dédiée pour contacter le _Kubelet_ : `--kubelet-client-certificate` et `--kubelet-client-key`
- _authz_ par _webhooks_ activé dans _Kubelet_ par `--authorization-mode=Webhook`
  - Le Kubelet renvoie une requête à l'_api-server_ pour demander si "cette personne peut effectuer cette opération ?"

---

## Controller manager

- Pour utiliser l'API `CertificateSigningRequest` le _Controller Manager_ a besoin du certificat et de la clé du CA (transmis avec `--cluster-signing-cert-file` et `--cluster-signing-key-file`)
- Le _Controller Manager_ génère aussi les tokens pour les `ServiceAccount`

---

### ServiceAccount tokens

- _authn_ à l'_api-server_ : un token _JWT_ par `ServiceAccount`
- Signé par une paire de clés:
	- Privée (signature) transmise au _Controller Manager_ : `--service-account-private-key-file` et `--root-ca-file`
	- Publique (vérification) transmise à l'_api-server_ : `--service-account-key-file`
- Le _kube-proxy_ tourne souvent en `DaemonSet` : propre `ServiceAccount` (=> token _JWT_)

---

## Webhooks

- Ressources (`kind:`) spécifiques pour les autorisations, dont les `SubjectAccessReview`.
- _authz_ par webhooks : envoi d'un `SubjectAccessReview` à l'_api-server_ pour autoriser chaque requête (réponse `allow` ou `deny`).

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

