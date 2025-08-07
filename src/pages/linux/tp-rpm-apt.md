---
title: TP - Gestion de paquetages
date: 2024 / 2025
---

## RPM, Yum et DNF

- Voir le cours de la certification LPIC-1 _102.5 Use RPM and YUM package management_ p.122 pour plus de détails.
- Pour plus d'infos :
  + <https://cheat.sh/rpm>
  + <https://cheat.sh/dnf>

### Travaux Pratiques

Le but de ce TP est de travailler sur la base RPM des packages déjà installés sur votre poste et d'en installer de nouveaux. Le poste, ou une machine virtuelle, doit disposer d'une distribution basée sur RPM (Red Hat, Fedora, Mandriva, openSUSE, etc.).

1. Déterminez le nombre de packages RPM actuellement installés sur votre poste de travail.

:::correction
```sh
rpm -qa | wc -l
```
:::

2. Vérifiez que le package `coreutils` est bien présent sur votre système, puis déterminez à quoi il sert à l'aide de sa description. Pouvez-vous faire en sorte de n'obtenir que la description et rien d'autre ? Lisez la page du manuel pour en savoir plus. _Indice : Le paramètre `-q` accepte un format de sortie que vous pouvez formater avec `--queryformat` . Le format se spécifie ainsi : `%{CHAMP}` avec le champ en majuscules._

:::correction
Dans un premier temps interrogez la base `RPM` sur ce package pour en obtenir les informations :

```sh
rpm -qi coreutils
```

En cas d'erreur, le package n'est sûrement pas installé. Sinon, lisez le contenu du champ `Description`. Dans un second temps, lisez la section du manuel de rpm consacrée au format de sortie.

```sh
rpm -q --queryformat=%{DESCRIPTION} coreutils
```
:::

3. Essayez de supprimer le package `coreutils`. Pouvez-vous fournir la liste des dépendances qui vous en empêche ?

:::correction

```sh
rpm -e coreutils
```

Vous obtenez la liste de tous les packages qui empêchent sa désinstallation : plusieurs centaines !

Notez l'existence du paramètre `-R` qui affiche de quoi dépend le package lui-même, et le `--provides` qui fournit le nom des éléments fournis par le package.

```console
$ rpm -q --provides coreutils

fileutils
sh-utils
stat
textutils
coreutils = 6.9-43
```
:::

4. Téléchargez le package `RPM` de `tuxpaint` présent sur <https://src.fedoraproject.org/rpms/tuxpaint>, choisissez la version de Fedora correspondante (`cat /etc/fedora-release`) et le téléchargement pour architecture x86-64.
  - Essayez d'installer ce package directement avec `rpm`. Que remarque-t-on ?

:::correction
Installez le package avec les paramètres `-i`, `-v` et `-h` :

```sh
rpm -ivh tuxpaint.xxxxxxx.rpm
```

`rpm` refuse l'installation car il manque un ensemble de dépendances. Il est possible (mais fastidieux) de télécharger ces dépendances manuellement et des les installer.
:::

5. En utilisant `dnf (uniquement pour cette question)`, installer facilement `tuxpaint` depuis les dépôts.

:::correction
```sh
dnf install tuxpain
```
:::

6. Si le package était déjà installé, comment auriez-vous pu le mettre à jour ? Sachant qu'il est déjà installé maintenant, tentez de mettre à jour ce package de manière inconditionnelle. Dans quel cas cela peut-il être nécessaire ? Enfin, supprimez-le.

:::correction
Vous pouvez mettre à jour le package avec les paramètres `-U` ou `-F`. 

Notez que vous auriez pu installer le package directement avec `-U` :

```sh
rpm -Uvh tuxpaint.xxxxxxx.rpm
```

Si le package est déjà installé dans la même version cela ne marche pas. Vous pourriez avoir besoin de le faire si des fichiers de ce package ont été supprimés : leur suppression, même complète, ne supprime pas le rpm de la base locale. Ajoutez l'option `--force`.

```sh
rpm -Uvh --force tuxpaint.xxxxxxx.rpm
```
:::

### Yum et DNF

- `rpm` est très puissant mais manque de convivialité. `yum` (_Yellowdog Updater, Modified_) a été inventé pour pallier à ce manque : il peut automatiquement télécharger les packages, résoudre les dépendances, ...
- La certification LPIC-1 se focalise encore sur `yum` mais `dnf` (_Dandified Yum_, son successeur) doit lui être préféré car il est plus puissant et plus rapide (mais reste très proche d'usage).

## Gestion de DPKG et APT

- Voir le cours de la certification LPIC-1 102.4 _Use Debian package management_ p.100 pour plus de détails
- Voir aussi :
  + <https://cheat.sh/dpkg>
  + <https://cheat.sh/apt>

### Travaux Pratiques

Le but de ce TP est de travailler sur la base `dpkg` des packages déjà installés sur votre poste, d'en installer de nouveaux et d'utiliser `APT`.

Le poste, ou une machine virtuelle, doit disposer d'une distribution de type Debian ou Ubuntu.

1. Répondez aux questions 1 à 4 du TP rpm, mais avec les commandes et packages `DPKG` équivalents : `coreutils` est présent sous le même nom et `tuxpaint` dispose de packages Debian sur <https://pkgs.org/search/?q=tuxpaint> (pour la version d'Ubuntu : `cat /etc/issue`). En cas de problèmes de dépendances, on ne cherchera pas à les résoudre (voir `apt` ci-dessous).

:::correction
1. La liste des packages installés doit être filtrée. Par défaut `dpkg` fournit la liste de tous les paquets connus, dont ceux installés. Ils commencent par `ii` :

```sh
dpkg -l| grep ^ii | wc -l
```

2. L'option `-l` de `dpkg` peut prendre un filtre comme paramètre :

```sh
dpkg -l "*coreutils*"
```

Il est possible que vous trouviez deux packages de ce nom, aussi vous devrez soit lire les résultats, soit rechercher une correspondance exacte :

```sh
dpkg -l coreutils
```

Pour obtenir les détails du package déjà installé, il vous faut aller dans le manuel qui vous informe qu'il est possible d'utiliser la commande `dpkg-query` et le paramètre `-W` :

```sh
dpkg-query -W coreutils
```

Mais il manque la description. Le manuel de `dpkg-query` fournit une information supplémentaire : vous pouvez modifier le format de sortie avec le `-f` :

```sh
dpkg-query -W -f='${Description}' coreutils
```

3. Pour supprimer un package Debian, utilisez l'option `-r` :

```sh
dpkg -r coreutils
```

Vous allez obtenir des erreurs :

```
dpkg: error processing package coreutils (--remove):
 this is an essential package; it should not be removed
Errors were encountered while processing:
 coreutils
```

C'est un paquet indispensable - il ne doit pas être supprimé.

4. Pour installer un package Debian, utilisez le paramètre `-i` :
 
```sh
dpkg -i tuxpaint.xxxxxxx.dpkg
```

Il n'y a pas de méthode directe équivalente à `rpm` pour la mise à jour d'un package. Si le package est déjà installé le `-i` va le mettre à jour. C'est à vous de vérifier avant si celui-ci est vraiment installé (voyez pour cela la réponse à la première question).
:::

2. `APT` est un gestionnaire de meta-packages : il gère les dépendances à votre place et travaille sur des dépôts et non plus sur des packages individuels. `Tuxpaint` est présent dans le dépôt des paquets Debian, notamment dans le dépôt `Universe`. Le but est d'ajouter (si besoins) ce dépôt, mettre à jour le système vers `Universe` puis d'installer le package `tuxpaint`. 

:::correction
Ajout du dépôt `universe` :

```sh
add-apt-repository universe
```

Mettez à jour la base locale `APT` avec la commande suivante :

```sh
apt update
```

Mettez à jour votre système avec :

```sh
apt upgrade
```

Installez `tuxpaint`. Remarquez que contrairement à la première question, `APT` gère les dépendances et va installer `tuxpaint` ainsi que les dépendances associées.

```sh
apt install tuxpaint
```
:::

### apt vs apt-get

Tout comme `dnf` est une réécriture de `yum`, `apt` est une réécriture récente de `apt-get`. À la différence de `yum` qui est déprécié, `apt` a été écrit pour être beaucoup plus simple que `apt-get` - il est donc plus limité et `apt-get` est encore disponible pour de rares besoins.

Sauf contrainte spéciale, on privilégiera donc `apt`.

## Le futur : `ostree`, OS immuable, conteneurs, AppImage, flatpak...

`rpm` et `dpkg` sont les deux principaux formats de packages sur Linux. Il existe beaucoup d'autres gestionnaires de packages ayant chacun leur propre format (et c'est l'une des  principales différences entre les distributions Linux, avec le système d'`init`) : `apk` sur `Alpine`, `pacman` sur `Arch`, `portage` sur `Gentoo`, ...

Au-delà de ces gestionnaires de packages "classiques", il existe depuis quelques années de nouvelles solutions dérivées des pratiques DevOps : `ostree` (notamment sur Fedora) permet de facilement isoler des applications et de gérer des OS immuables (aucun changement, état du système garanti), `AppImage` permet de facilement partager une application et toutes ses dépendances indépendamment de la distribution, `flatpak` permet d'isoler les applications de la communauté des applications officielles sur Ubuntu...

Les systèmes Linux sont des systèmes globalement très rétro-compatibles (beaucoup de conventions datent des 1ères versions du noyau) mais les révolutions du packaging applicatif ont de fortes répercussions sur l'ensemble du système : remise en cause de la `FHS`, ...

On observe une tendance à la diversité des solutions :

- architectures immuables définies par des fichiers de contrats pour OS légers (conteneurs, ...)
- systèmes hybrides cumulant packaging officiel (`rpm`, `apt`) et packaging communautaire (`flatpak`, `AppImage`) pour les machines personnelles.

