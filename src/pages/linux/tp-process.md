---
title: TP - Les processus
date: 2024 / 2025
---

## Cours

:::tip
Voir le cours de la formation LPIC-1 section _Process Monitoring_, 103.5 Lesson 1 p.295
:::

## Obtenir des informations sur un processus

La commande `ps` permet d'obtenir des informations sur les processus.

1. Listez les processus de tous les utilisateurs du système.
2. Afficher uniquement les processus de votre utilisateur.
3. Afficher l'arborescence de tous les processus.
4. La commande `top` permet d'afficher dynamiquement les informations sur les processus en cours d'exécution.
5. En utilisant les variables du shell `$` et `PPID`, récupérer le `PID` du processus courant et de son parent.

:::correction
La syntaxe de cette commande est très différente d'un système à l'autre (notamment sur système `GNU` vs `BSD`). Lorsque nécessaire, 2 solutions sont données.

1. Listez les processus de tous les utilisateurs du système.

```sh
ps -ef
```

ou

```sh
ps aux
```

2. Afficher uniquement les processus de votre utilisateur.

```sh
ps -u tom
```

ou

```sh
ps u tom
```

3. Afficher l'arborescence de tous les processus.

```sh
ps -ejH
```

ou

```sh
ps axjf
```

5. En utilisant les variables du shell `$` et `PPID`, récupérer le `PID` du processus courant et de son parent.

Pour récupérer le `PID` du processus courant :

```sh
echo $$
```

Pour récupérer le `PID` du processus parent auquel est rattaché le processus courant :

```sh
echo $PPID
```
:::

## Tuer un processus

### kill

- Ouvrez un terminal et utilisez la commande `top` pour afficher la liste des processus en cours d'exécution.
- Notez l'identifiant du processus que vous souhaitez arrêter. Vous pouvez également utiliser la commande `ps` pour trouver l'identifiant du processus.
- Utilisez la commande `kill` suivie de l'identifiant du processus pour arrêter le processus. Par exemple : `kill 12345`, où `12345` est l'identifiant du processus.
- Vérifiez que le processus a été arrêté en utilisant à nouveau la commande `top`. Vous devriez ne plus voir le processus dans la liste.
- Si vous souhaitez arrêter un processus de manière plus brutale, vous pouvez utiliser la commande `kill -9` suivie de l'identifiant du processus. Cette commande envoie le signal `SIGKILL` au processus, qui le termine immédiatement sans donner la possibilité de s'arrêter proprement.

:::tip
La commande `Control-C` permet d'envoyer un signal `SIGINT` au(x) processus d'avant plan, qui se traduit en général par un arrêt du programme. `kill` peut envoyer de nombreux signaux à un processus (pas uniquement pour son arrêt). Pour les signaux de base, voir <https://www.baeldung.com/linux/sigint-and-other-termination-signals>
:::

:::tip
Vous devez être un utilisateur `root` ou avoir les privilèges nécessaires pour arrêter un processus. Il est important d'être prudent lors de l'utilisation de la commande `kill`, car elle peut entraîner des données corrompues ou des erreurs système si elle est utilisée sur des processus importants.
:::

### pkill

Il est aussi possible de tuer un processus depuis son nom (attention, dangereux si plusieurs instances sont en exécution).

1. Lancez le processus `sleep 1000` dans un terminal.
2. Dans un autre terminal, tuer le processus avec la commande `pkill`.
3. `pkill` utilise en fait la commande `pgrep` pour récupérer l'identifiant d'un processus. Comment réécrire facilement la commande `pkill` ?


:::correction
```sh
sleep 1000
pkill 1000
kill `pgrep sleep`
```
:::

### killall

`killall` permet de tuer toutes les instances d'un programme, par exemple : `killall sleep`.

## Jobs

Voir le cours de la formation LPIC-1 section _Job Control_, 103.5 Lesson 1 p.290

1. Lancez le processus `sleep 1000` en arrière-plan. Récupérez son `PID`.
2. Replacez ce processus en avant plan, puis stoppez-le (ne le tuez pas) et replacez-le en arrière-plan.
3. Indiquez les détails de ce processus :
4. Modifiez la priorité de ce processus et passez-la à un facteur 10 :
5. Listez à nouveau le détail de ce processus mais au format long. Regardez la valeur de la colonne `NI` :
6. Envoyez le signal 15 à ce processus. Ceci va le terminer.
7. Dans un environnement graphique, vous pouvez aussi installer et utiliser le programme `oneko` qui affiche un chat qui suit le pointeur de la souris afin de voir graphiquement la différence entre un processus d'avant plan, d'arrière-plan ou en pause.

:::correction
1. Lancez le processus `sleep 1000` en arrière-plan. Récupérez son `PID`.

```console
$ sleep 1000&
[1] 9168
```

2. Replacez ce processus en avant plan, puis stoppez-le (ne le tuez pas) et replacez-le en arrière-plan.

```console
$ fg
sleep 1000
# [CTRL] + [Z]
[1]+ Stopped sleep 1000 
$ bg 
[1]+ sleep 1000 &
```

3. Indiquez les détails de ce processus :

```console
$ ps p 9168 -f
UID PID PPID C STIME TTY
tom 9168 8096 0 10:46 pts/1 STAT S TIME CMD 0:00 sleep 1000
```

4. Modifiez la priorité de ce processus passez-la à un facteur 10 :

```console
$ renice 10 9168
9168: priorité précédente 0, nouvelle priorité 10
```

5. Listez à nouveau le détail de ce processus mais au format long.
  - Regardez la valeur de la colonne `NI`.
  - À quoi correspond la colonne `PRI` ?
  - Voir aussi : <https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/>

```console
$ ps p 9168 -l 
F S UID PID PPID C PRI NI ADDR SZ WCHAN TTY    TIME  CMD
0 S 1000 9168 8096 0 90 10 - 2324 restar pts/1 0:00  sleep 1000

# NI est la priorité demandée par nice
# PRI est la priorité effective, i.e. la priorité réelle du processus (choisie par le scheduler)
```

6. Envoyez le signal 15 à ce processus. Ceci va le terminer.

```console
$ kill -15 9168 
[1]+ Complété sleep 1000 
```
:::

### nohup

La commande `nohup` est utilisée pour exécuter un processus en arrière-plan sur un système Unix, sans qu'il soit interrompu lorsque l'utilisateur se déconnecte. La commande `nohup` signifie "no hangup", ce qui signifie que le processus ne sera pas interrompu lorsqu'un signal de déconnexion `SIGHUP` est envoyé au terminal.

Lorsqu'un processus est exécuté avec la commande `nohup`, les sorties standard et d'erreur seront redirigées vers un fichier nommé `nohup.out`, ce qui permettra de conserver les résultats de l'exécution du processus même après la déconnexion de l'utilisateur.

La syntaxe de base de la commande `nohup` est la suivante :

```sh
nohup commande &
```

où `commande` est la commande que vous souhaitez exécuter en arrière-plan. Le caractère `&` permet de démarrer le processus en arrière-plan, de sorte que vous puissiez continuer à utiliser votre terminal pendant que le processus est en cours d'exécution.

1. Exécuter une commande `sleep 2000` avec un `nohup`.
2. Se déconnecter du terminal et vérifier que la commande est toujours en cours d'exécution.


## Multiplexeur de terminal : `tmux`

`Tmux`, abréviation de "Terminal Multiplexer" (Multiplexeur de Terminal en français), est une application en ligne de commande qui vous permet de gérer de manière efficace et flexible des sessions de terminal, des fenêtres et des panneaux (split panes) sur une seule instance de terminal. `Tmux` est particulièrement utile pour les administrateurs système, les développeurs et toute personne travaillant fréquemment avec la ligne de commande.

Quelques-unes des fonctionnalités principales de `Tmux` :

- Sessions : `Tmux` vous permet de créer et de gérer plusieurs sessions de terminal. Chaque session est un environnement de terminal indépendant, ce qui signifie que vous pouvez travailler sur plusieurs tâches ou projets en parallèle.
- Fenêtres : À l'intérieur de chaque session, vous pouvez créer plusieurs fenêtres. Chaque fenêtre peut contenir un ensemble différent de panneaux, ce qui vous permet de basculer rapidement entre différents contextes de travail. Par exemple, vous pouvez avoir une fenêtre pour l'édition de code, une autre pour le débogage et une troisième pour l'administration système. Ou bien, plusieurs terminaux ouverts sur une machine distante dans une unique connexion `SSH`.
- Panneaux : Les panneaux vous permettent de diviser une fenêtre en plusieurs sections horizontales ou verticales. Vous pouvez ainsi exécuter plusieurs commandes ou voir différentes parties de la sortie de la même commande en même temps.
- Séances persistantes : L'un des avantages majeurs de `Tmux` est la possibilité de détacher une session en cours et de la reconnecter ultérieurement. Cela signifie que vous pouvez déconnecter votre session, quitter le terminal ou même fermer votre ordinateur, puis vous reconnecter à la session exacte où vous l'avez laissée. Cela est particulièrement utile pour les longues tâches de compilation, les transferts de fichiers, ou lorsque vous travaillez sur un serveur distant où la connexion peut être aléatoire.
- Personnalisation : `Tmux` est hautement personnalisable. Vous pouvez configurer des raccourcis clavier, des couleurs, des thèmes et d'autres aspects de son comportement pour l'adapter à vos besoins spécifiques.
- Collaboration : `Tmux` permet également de partager des sessions avec d'autres utilisateurs, ce qui facilite la collaboration en temps réel sur des projets via un terminal partagé.

1. Installer et lancer `tmux`.
2. Lancer le programme `top`
3. Dans `Tmux`, ouvrir une nouvelle fenêtre pour y ouvrir le fichier `~/.tmux.conf` dans `nano`.
4. Séparer la fenêtre verticalement et réduire la taille du nouvel onglet.
5. Changer le nom de la fenêtre courante.
6. Lister les sessions de `tmux`.
7. Se déplacer vers la fenêtre qui tourne `top` puis revenir à la fenêtre courante.
8. Détacher la session courante, en créer une nouvelle qui s'appelle `session2` et dont le nom de la fenêtre est `session2 window`.
9. Détacher la session `session2` et afficher la liste des sessions.
10. Partage de session :
  - En utilisant l'invité de commandes (`[CTRL]` + `[b]` puis `[:]` et la commande `setw -g permit-attach on` activer le partage de session
  - Dans un autre terminal, s'attacher à la session
  - Déconnecter le nouvel utilisateur pour laisser un unique utilisateur de session
11. [Optionel] Utiliser `tmux` pour gérer un ensemble de sessions de terminaux via une seule session `ssh`. Couper la connexion `ssh` et récupérer la session.

:::tip
`tmux` est certainement le multiplexeur de terminal le plus connu, mais il en existe d'autres. `screen` est une autre alternative très utilisée, et des versions plus "modernes" existent aussi : `wezterm`, `zellij`, …

Par exemple, pour tester `zellij` sans avoir besoin de l'installer : `bash <(curl -L zellij.dev/launch)`
:::

:::correction
1. Installer et lancer `tmux`.
2. Lancer le programme `top`
3. Dans `Tmux`, ouvrir une nouvelle fenêtre pour y ouvrir le fichier `~/.tmux.conf` dans `nano`.
`[CTRL]` + `[b]` puis `[c]`

```sh
nano ~/.tmux.conf
```

4. Séparer la fenêtre verticalement et réduire la taille du nouvel onglet.
`[CTRL]` + `[b]` puis `["]`
`[CTRL]` + `[b]` puis `Ctrl` + `[↓]`
5. Changer le nom de la fenêtre courante.
6. Lister les sessions de `tmux`.
`[CTRL]` + `[b]` puis `[,]`. Entrer un nouveau nom et valider avec `[Entrée]`.
`[CTRL]` + `[b]` puis `[s]`  ou `tmux ls`.
7. Se déplacer vers la fenêtre qui tourne `top` puis revenir à la fenêtre courante.
`[CTRL]` + `[b]` puis `[n]`  ou `[CTRL]` + `[b]` puis `[p]`
8. Détacher la session courante, en créer une nouvelle qui s'appelle `session2` et dont le nom de la fenêtre est `session2 window`.
`[CTRL]` + `[b]` puis `[d]` 
    ```sh
    tmux new -s "session2" -n "session2 window"
    tmux ls
    ```
9. Détacher la session `session2` et afficher la liste des sessions.
`[CTRL]` + `[b]` puis `[d]`
10. Partage de session
    ```sh
    tmux attach-session -t nom-de-session
    tmux lsc
    tmux detach-client -t nom-du-client
    ```
11. Idem dans une connexion `SSH`.
:::
