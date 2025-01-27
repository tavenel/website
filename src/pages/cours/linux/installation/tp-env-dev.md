---
title: Installation d'outils de développement sous environnement Linux
date: 2024 / 2025
---

## Introduction

Les environnements GNU/Linux sont des écosystèmes très dynamiques et en constante évolution. Il existe souvent des dizaines, voir des centaines d'alternatives permettant de résoudre le même problème.

Voici une liste, bien entendu non exhaustive, de quelques outils et programmes alternatifs qui peuvent s'avérer utiles sur un poste de travail afin d'améliorer l'ergonomie des commandes POSIX standard.

Note : essayez au maximum d'utiliser votre gestionnaire de versions habituel (par exemple `apt` ou `snap` sous Ubuntu) pour installer les programmes.

## Le shell

### Terminal

Le premier programme auquel s'intéresser est l'émulateur de terminal. La plupart des environnements graphiques proposent des émulateurs de terminaux de qualité par défaut (Gnome Terminal, …). On pourra cependant utiliser des alternatives :

- [alacritty][alacritty] pour sa puissance (utilise le GPU)
- [foot][foot] sous `wayland` pour sa rapidité (très léger en ressources)
- [wezterm][wezterm] est un terminal "nouvelle génération" avec beaucoup de fonctionnalités intégrées (notamment un multiplexeur de terminal)
- [kitty][kitty] est un des terminaux les plus populaires pour ses concepts innovants

#### Multiplexeur de terminal

Un multiplexeur de terminal permet d'ouvrir plusieurs sessions shell dans un seul terminal (et simule donc d'avoir plusieurs sessions, très utile par exemple dans une unique session SSH). La plupart des multiplexeurs fonctionnent sur un modèle client/serveur : le serveur de multiplexeur tourne à distance et héberge le shell en cours, ainsi il est possible de se déconnecter du système et de se reconnecter plus tard et de retrouver sa session là où on l'a laissée.

Quelques multiplexeurs de terminaux :

- `zellij` => terminal multiplexer
- [tmux][tmux] : de très loin le plus populaire, l'un des deux multiplexeurs historiques, peut être amélioré avec beaucoup de plugins
- [zellij][zellij] : multiplexeur de terminal récent, très facile d'utilisation. À tester par : `bash <(curl -L zellij.dev/launch)`
- [wezterm][wezterm] : terminal incluant un multiplexeur de terminal
- [screen][screen] : un des 2 multiplexeurs historiques, encore très utilisé aujourd'hui.

:::link
Voir le TP tmux sur le site web.
:::

#### Font

Utiliser une police de caractères supportant les symboles permet d'afficher dans le terminal beaucoup d'informations (types de fichiers, …). Cela permet aussi d'utiliser des ligatures (symbole `->`, …) et d'éviter les erreurs de programmation (différence `0` vs `O` par exemple). On pourra utiliser les [nerd-fonts][nerd-fonts].

:::tip
Utiliser les commandes `fc-list` pour afficher les polices disponibles et `fc-cache -fv` pour raffraichir le cache.
:::

:::tip
Quelques polices recommandées pour coder : `Hack`, `Inconsolata`, `Noto Color Emoji`, `FiraCode`, `VictorMono` (cursif).
:::

### Interpréteur de commandes : le shell

Le shell lui-même peut être modifié.

`bash` est de loin le plus populaire sous Linux, mais d'autres shells (souvent plus puissants mais plus lents) existent :

- Le Z-Shell `zsh` : fonctionnalités supplémentaires, par défaut sous MacOS
  - peut être couplé à [Oh My ZSH][oh-my-zsh] pour installer facilement des extensions
  - voir aussi : [awesome-zsh][awesome-zsh]
- `fish` : très user-friendly, attention non POSIX : les boucles, … sont différentes
  - peut être couplé à [Fisher][fisher] pour les dépendances
- `bash` avec des extensions, par exemple [Oh My Bash][oh-my-bash]

#### Prompt (PS1)

La variable PS1 décrit le _prompt_ du shell (la partie affichée avant les commandes). Modifier son prompt permet de gagner rapidement en efficacité :

- [pure][pure] : prompt très rapide sous ZSH
- [poweline][powerline] : de loin le prompt le plus populaire, disponible pour presque tous les shells
- ou modifier et exporter la variable `PS1` de son shell soi-même !

#### Coloration syntaxique

La variable `LSCOLORS` est une variable utilisée par `ls` et des programmes similaires pour afficher des types ou patterns de fichiers différemment.

```sh
grep --color=always <pattern> | less -R # grep avec couleur
```

Sous `zsh` on pourra par exemple utiliser [zsh-zsh-syntax-highlighting][zsh-zsh-syntax-highlighting]

#### Auto-completion et suggestions

Le shell peut auto-compléter des commandes :

- avec la touche `<Tab>` (notamment pour les noms de fichiers) mais également pour des arguments de commandes avec les extensions adéquates
- en utilisant la complétion inventée par [fish][fish] : en utilisant l'historique des commandes, une proposition de complétion complète la commande, appuyer sur la flèche de droite `->` pour accepter la complétion.

Sous `zsh` on pourra par exemple utiliser [zsh-autosuggestions][zsh-autosuggestions]

#### Avertissement

:::warning
Le shell est un programme relancé très souvent, voir pour certaines parties (prompt par exemple) après chaque commande. Attention à ne pas surcharger votre shell de plugins et extensions inutiles (notamment concernant les autocomplétions) qui le ralentiraient fortement !
:::

### alias

Utiliser des alias est un bon moyen d'améliorer son shell pour répondre à ses propres besoins.

Quelques exemples d'alias courants :

```bash
alias ..="cd .."
alias l="ls --color"
alias ll="ls -l"
```

On peut aussi utiliser les alias pour redéfinir des commandes de base du système, par exemple `alias ls='ls -l'` ou `alias ls=eza`. Attention aux effects secondaires !!!

## Petits programmes

### Afficher des informations sur les fichiers

`ls` est LA commande de référence pour afficher des informations sur les fichiers. De nombreuses alternatives existent, qui sont souvent fortement compatibles mais ajoutent de petites subtilités (meilleur affichage, …).

- [eza][eza] (anciennement `exa`) est un bon remplaçant de `ls`
- [yazi][yazi], [n3][nnn] et [ranger][ranger] sont des explorateurs de fichiers en mode console

### Outils de recherche

Les programmes `find` et `grep` sont les 2 programmes de référence sous Linux. Ils sont POSIX (donc disponibles presque partout) et très puissants, il faut donc savoir les maîtriser.

Cependant dans un environnement que l'on gère soi-même (par exemple sa machine personnelle) il peut être intéressant d'ajouter d'autres outils un peu plus ergonomiques :

- [fd][fd] est un remplaçant de `find`
- [ripgrep][rg] (`rg`) , le [Silver Searcher][ag] (`ag` ), [ack][ack] sont des remplaçants de `grep`, souvent plus rapides et supportant bien la récursivité.
- [Fuzzy-finder][fzf] (`fzf`) est la référence pour de la recherche en temps réel (avec par exemple : `export FZF_DEFAULT_COMMAND='fd . --hidden'`)
  - exemple : `fzf --preview 'bat --style=numbers --color=always --line-range :500 {}'`
- [plocate][plocate] un remplaçant bien plus efficace que `mlocate` (implémentation standard de `locate`)

### Affichage de fichiers

- [bat][bat] est une alternative à `cat`.
  - `bat --list-themes`

## IDE

Bien sûr, `vi` est l'éditeur POSIX de prédilection sous Linux. Sur sa machine de développement, on pourra lui préférer `neovim` qui a un écosystème très dynamique et supporte la configuration par fichiers `Lua`. Comme pour `Linux`, il existe de nombreuses distributions de `neovim` permettant d'installer directement un écosystème de plugins le transformant en un véritable IDE. On pourra par exemple utiliser [LazyVim][lazyvim] (voir aussi le très bon livre gratuit [LazyVim for Ambitious Developers](https://lazyvim-ambitious-devs.phillips.codes/).

Il existe de nombreuses distributions `neovim` : pour les tester, on pourra utiliser le projet <https://lazyman.dev/> qui permet de tester de nombreuses configurations toutes prêtes pour `neovim`.

À noter également, [helix][helix] est un éditeur moderne très inspiré de `vim` mais en modifiant quelques concepts.

## Interfaces utilisateurs en mode terminal (TUI)

- explorateurs de fichiers
  - [n3][nnn]
  - [ranger][ranger]
  - [yazi][yazi]
- un joli lecteur markdown : [glow][glow]
- git
  - [lazygit][lazygit]
  - [tig][tig]
- docker
  - [lazydocker][lazydocker]
  - [dry][dry]
  - [k9s] (kubernetes)
- tableur : [sc-im][sc-im]
- base de données : [term-dbms][term-dbms]
- musique : [cmus][cmus]

## Utilitaires en ligne

- Afficher son IP publique : `curl ifconfig.me/ip` ou `curl ifconfig.me/all.json`
- Afficher des pages d'aide de commadnes : `curl cheat.sh/ma_commande`

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
[wezterm]: https://wezfurlong.org/wezterm/index.html
[yazi]: https://github.com/sxyazi/yazi
[zellij]: https://zellij.dev/
[zsh-autosuggestions]: https://github.com/zsh-users/zsh-autosuggestions
