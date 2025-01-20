---
pagetitle: Tom Avenel - FAQ
---

## Général

### Que signifie ce terme dans la culture Cloud / Devops ?

::: link
Voir le glossaire de la _Cloud Native Computing Foundation_ : <https://glossary.cncf.io/fr/>
:::

### Quelle est la différence entre un langage compilé, interprété, ou tournant dans une machine virtuelle ?

::: link
Voir la section _"Exécuter du code"_ de cet article : <https://lafor.ge/rust/pourquoi/#executer-du-code>
:::

### Je tape le nom de mon programme dans un terminal et celui-ci ne s'exécute pas, pourquoi ?

Un shell (le programme qui exécute les commandes dans le terminal) utilise la variable PATH pour faire le lien entre le nom d'une commande et le chemin vers le fichier du programme à exécuter. Par exemple, lorsque l'on tape `ls mon_fichier`, le shell cherche le chemin du programme `ls` à exécuter dans les répertoires définis dans la variable PATH. Si le programme n'est pas trouvé, la variable PATH est sûrement mal configurée.

::: tip
Pour apprendre à gérer la variable d'environnement `$PATH` :

- voir [ce tutoriel sous Windows](https://www.malekal.com/comment-modifier-la-variable-path-sous-windows-10-11/)
- sous Linux (ou MacOS), voir le TP sur la ligne de commandes [du cours Linux](/cours/linux/index.html)
:::

### Qu'est-ce qu'un Makefile ?

`make` est un exécuteur de tâches permettant très simplement de gérer les différentes tâches d'un projet : compilation, tests, … C'est le gestionnaire de tâches historique des programmes écrits en `C` et il est encore très utilisé car disponible presque partout. On l'utilise aujourd'hui souvent pour lancer un autre outil plus puissant.

Les tâches sont décrites dans un fichier nommé `Makefile`.

Exemple de `Makefile` :

```Makefile
install :
    npm install
test : install
    npm run test
```

Voir [cet article](https://vinta.ws/code/use-makefile-as-the-task-runner-for-arbitrary-projects.html) pour apprendre à écrire un bon `Makefile`.

:::tip
`make` s'intègre très bien avec `Vim` ! Essayez `:make` dans votre projet : la `quickfix list` est remplie automatiquement
:::

## Programmation

### C'est quoi la programmation fonctionnelle ?

La programmation fonctionnelle utilise des concepts mathématiques permettant, entre autres, d'éviter les erreurs non gérées par l'utilisation de fonctions _pures_ (sans effet de bord).

::: link
Voir ce très bon article pour une introduction (simple) à la programmation fonctionnelle sans concept mathématique.
:::

## Git

### La commande `git commit` échoue

```
Waiting for your editor to close the file... error: cannot run ...
```

`git commit` (sans option `-m`) a besoin d'un éditeur de texte pour ajouter un commentaire au commit à créer. Votre éditeur est mal configuré `git config core.editor` affiche le lien vers le programme de l'éditeur de texte à configurer.

Attention, sous Windows il faut remplacer `C:\...\mon_programme.exe` par des slash `/` en pensant à ajouter devant les caractères spéciaux (par exemple les espaces) un backslash : `\` : `C:\Program Files\mon_programme.exe` devient donc `C:/Program\ Files/mon_programme.exe`.

Par exemple, pour utiliser `vsCode` sous Windows avec le chemin par défaut : `git config --global core.editor "C:/Program\ Files/Microsoft\ VS\ Code/Code.exe --wait"`

::: tip
Si vous souhaitez utiliser `vsCode` comme éditeur, attention à bien ajouter l'option `--wait` à la commande : `git config --global core.editor "C:/.../code.exe --wait`. 
:::

Attention, il est possible d'entrer plusieurs configurations `core.editor`. En cas d'erreur, il faut donc commencer par supprimer toutes les références précédentes à `core.editor` avant d'en déclarer un nouveau : `git config --global --unset-all core.editor`

### La commande `git push` échoue : `no upstream branch`

```
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
```

Git refuse d'envoyer les commits de la branche locale vers un dépôt distant car il ne sait pas vers quelle branche l'envoyer. Pour rappel Git est un modèle distribué, chaque dépôt est indépendant ! Voir [le cours Git](/cours/git/index.html)

Il faut donc expliquer à Git à quelle branche distante lier la branche locale (elle sera créée si besoin sur le dépôt distant). Si le `remote` s'appelle `origin` (cas par défaut après un `clone`) :

```
git push --set-upstream origin ma_branche_distante
```

### Pourquoi git ne voit-il pas mon nouveau répertoire vide ?

Git gère uniquement des fichiers : les répertoires en eux-mêmes sont ignorés. Un répertoire est donc créé uniquement s'il est nécessaire pour accéder au chemin d'un fichier - si `git` supprime le dernier fichier d'un répertoire, il supprime également ce répertoire vide.

## Python

### Je tape python, rien ne s'exécute, pourquoi ?

Voir la question sur le PATH.

### J'ai installé ma dépendance avec `pip install ma_librairie` mais Python me dit qu'il ne trouve pas la librairie, pourquoi ?

Il est courant d'avoir plusieurs installations de Python sur la même machine (versions différentes, `virtualenv`, ...). `pip` est un module Python qui dépend de chaque installation de Python (1 installation de `pip` pour 1 installation de `python`).

En exécutant `pip install ma_librairie` on exécute le programme `pip` trouvé dans le PATH. En exécutant `python mon_fichier.py` on exécute le programme `python` trouvé dans le PATH... pas forcément au même endroit que `pip` !

Pour éviter cette erreur, il est recommandé de toujours lancer `pip` comme un module du programme `python` actuellement utilisé : `python -m pip install ma_librairie`. Ainsi on est certain d'utiliser le module `pip` de la version de `python` actuellement utilisée !

Voir la question sur le PATH pour plus d'information.

### J'ai installé `unittest` mais `python mon_test.py` me dit qu'`unittest` n'est pas installé...

Voir la question sur `pip`.

### J'ai installé `selenium` mais `python mon_test.py` me dit que `selenium` n'est pas installé...

Voir la question sur `pip`.

### J'ai installé `django` mais `python manage.py runserver` me dit que `django` n'est pas installé...

Voir la question sur `pip`.

### Mon IDE affiche des erreurs d'imports alors que j'ai bien installé les dépendances du projet

Vérifiez que votre IDE utilise la bonne version de `Python` (celle avec laquelle vous avez installé les dépendances) ! Il peut s'agir d'une installation globale sur votre système, d'un environnement virtuel, ...

Par exemple dans `VSCode`, attention à bien définir le bon interpréteur à utiliser pour votre projet : <https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter>.

**Attention - dans VSCode, la configuration de l'interpréteur pour le projet n'est pas forcément la même que celle de l'interpréteur exécutant les commandes dans le terminal de VSCode !!**

Voir la question sur le `PATH` pour connaître le chemin vers le "vrai" exécutable lancé lorsque vous tapez `python` ou `py`.

### Comment créer un environnement virtuel (`venv`, `virtualenv`) en Python ?

Pour ne pas impacter le reste du système, il est recommandé d'installer les dépendances d'un projet dans un environnement indépendant du reste du système : c'est le principe des _virtual environments_.

Il existe plusieurs technologies d'environnements virtuels, notamment [venv](https://docs.python.org/fr/3/library/venv.html).

Créer un environment virtuel revient à créer une nouvelle installation de Python : cela crée donc un nouveau répertoire avec un nouveau programme `Python` et `pip` et toutes les librairies Python (installées par `pip install ...`) pour cette installation de Python.

Pour créer un environment virtuel sous Linux :

```sh
$ python -m venv chemin\vers\le\nouveau\repertoire\du\venv
```

Ou sous Windows :

```cmd
C:\>python -m venv C:\chemin\vers\le\nouveau\repertoire\du\venv
```

Cette commande crée une installation locale de Python dans le répertoire spécifié.

Il faut ensuite, **dans chaque terminal ouvert par la suite pour notre projet**, activer cet environnement en sourçant la configuration (voir le [tableau ici](https://docs.python.org/fr/3/library/venv.html#how-venvs-work)).

Par exemple sous Linux / Mac :

```bash
$ source /path/to/new/virtual/environment/bin/activate
```

Ou sous Windows (`cmd`) :

```cmd
C:\> C:\path\to\myenv\Scripts\activate.bat
```

Ou sous Windows (`powershell`) :

```cmd
C:\> C:\path\to\myenv\Scripts\Activate.ps1
```

Il est aussi possible d'utiliser `VSCode` pour générer directement l'environnement virtuel : <https://code.visualstudio.com/docs/python/environments>

## Base de données, mysql

### J'utilise un conteneur `mysql` avec un point de montage direct `bind mount`. Ma base de données n'est pas correctement configurée ?

Il semble que `mysql` ne supporte pas les permissions d'un système de fichiers monté directement par Windows en `bind mount` :

```
$ docker run -v C:/...:/var/lib/mysql ....
```

Préférer utiliser un vrai volume :

```
$ docker volume create ...
$ docker run -v volume_id:/var/lib/mysql ...
```

### J'ai des erreurs `InnoDB`

Par exemple :

```
2023-02-23T12:25:18.105758Z 0 [ERROR] InnoDB: Unable to lock ./ibdata1 error: 11
```

InnoDB n'accepte pas les écritures concurrentes - il y a certainement 2 serveurs de base de données qui tournent en même temps sur la machine et qui utilisent le même répertoire pour les données ( par exemple `/var/lib/mysql` )

## Docker

### Lorsque j'utilise `docker compose` j'ai des erreurs `changes out of order` :

::: link
Utiliser la dernière version de `docker` et `docker-compose`.

Si vous avez installé `docker` via Docker Desktop, il se peut (2024-02) que la version de `docker-compose` installée ne soit pas compatible avec la dernière version de `docker`.

Voir : <https://medium.com/code-kings/docker-changes-out-of-order-error-try-this-b1644edf3169>
:::

## Virtualbox

### J'ai une erreur : "activer la virtualisation VT-x/AMD-V".

1. Vérifier que la virtualisation est bien activée dans le BIOS (voir la documentation de votre PC).
2. `Hyper-V` n'accepte qu'un seul programme à la fois utilisant `VT-x` ce qui peut poser problème. Voir ce lien pour désactiver les services pouvant utiliser `VT-x` : <https://superuser.com/questions/1734650/virtualization-enabled-in-bios-but-intelpiu-not-recognize>.

