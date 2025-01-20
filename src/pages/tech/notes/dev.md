---
title: Notes dev
date: 2024-09-29
updated: 2024-09-29
---

> Content checked : 2024-09-29

FOSS alternates
===============

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

Tools
=====

## Desktop

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
- `kiwix` => `.zim` browser (offline websites like Wikipedia)
- `grim` => screenshots

## Terminal

- See also : </cours/linux/installation/tp-env-dev.md>
- Terminal emulator : `foot` (Wayland) // `st` (X) // `alacritty` (GPU-accelerated) // `wezterm` (modern) // `zellij`, `tmux` (multiplexers)
  - `bash <(curl -L zellij.dev/launch)` => terminal multiplexer
- File editors and IDEs : `vim` // `neovim` (VIM fork in Lua) // `hellix` => "post-moderm" vim
- File manager : `nnn` // `yazi` // `eza` (better `ls`)
  - `eza` // `eza -T` => `ls` // `tree` replacement // `bat` (`cat` with syntax highliting, very small)
  - `eza --header --long --git --icons --sort=ext --tree --accessed --created --modified --group --links --grid --classify` => full eza options
- `bsdtar` => archive management on Linux, includes `rar` format
- `column -s ',' -t` => better CSV output
- `ntfy send ...` => send notification (can use many backends)
- `tig` // `lazygit` => graphical `git` viewer
- `cmus` // `mocp` => audio player
- Grep with colors => `grep --color=always <pattern> | less -R`
- `plocate` => very efficient locate (far better than `mlocate`)
- `ls file1.py | entr python /_` // `entr -c` // `entr -p` // `entr -r` => execute cmd on file change // clear screen first // postpone 1st cmd before change // reload a non-stopping cmd
- `catimg` (req. `imagemagick`) => show image in terminal
- `glow` => markdown reader
- `termdbms` => SQL queries in TUI
- `dry` => manage Docker containers and Swarm cluster
- `k9s` => k8s management
- `ctop` => like `top` for containers
- `sc-im` => spreadsheet
- `curl ifconfig.me/ip` // `curl ifconfig.me/all.json`
- `curl cheat.sh/<command>` => minimal man page on `<command>`
- `curl wttr.in/Grenoble` => weather at Grenoble, France.
- `fc-list` // `fc-cache -fv` => show available fonts // refresh font cache
- `chvt N` => go to TTY `N` (idem C-A-FN)
- `docker run --rm -it browsh/browsh` // `docker run --rm -ti fathyb/carbonyl https://youtube.com` => terminal-based web browsers
- `fx` // `jq` // `jqp` => json viewers and processors
- `figlet` => ascii-art of text
- `pv` => type-writter effect
- `termshark` => packet sniffer using `wireshark` in terminal
- `atuin` => command history with persistence

## Network

- `aria2` => downloader (HTTP / Magnet)
- `wavemon` => monitor wifi
- `netstat -pultn` => processes with network activity (one shot)
- `nethogs` => processes with network activity (live)
- `iw dev wlp3s0 info` => get wifi info (including power)
- `iw dev wlp3s0 set txpower fixed 700` => limit wifi power (save battery) to 7dBm (default 22)
- `lsof -i -P -n` => opened ports and connexions
- `netscanner` => network scanner

## Disk

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

## Hardware

- `nmon` => hardware monitoring
- `inxi` // `inxi -xxAv6` => description système
- `lstopo -.txt` => vision graphique système - package `hwloc`
- `lspci` // `lsusb` // `lscpu` => liste pci // usb // cpu
- `usbutils` => installs full `lsusb` on Busybox's distribution
- `powerstat`
- Kernel/CPU bugs => `cat /proc/cpuinfo | grep bug`
- Kernel option `SATA_MOBILE_LPM_POLICY` => 3 (seems recommended by Lenovo SSD)
- Kernel firmwares : `iwlwifi-7265D-29.ucode`

## Games

- `1ad` => age of empires-like
- `minetest` // `terasology` => minecraft-like
- `supertux` // `tuxkart` => mario-like // mario kart like
- `pioneers` => "settlers of catan" clone
- `wesnoth` => turned-based strategy

Notes
====

bash
----

- `C-s` // `C-q` => freeze / unfreeze screen display
- `mv file{.json,.yaml}` => rename `file.json` to `file.yaml`
- `ls | xargs -I@ echo @` => idem `for @ in $(ls); do echo $@; done`
- `%` // `%-` => foreground the most recent // second most recent backgrounded job
- `disown %<jobID>` => disowns jobs from the parent - process keeps running if terminal is closed

zsh
----

- `jobs -d` => show jobs with `pwd`
- `for i in {0..255}; do print -Pn "%K{$i}  %k%F{$i}${(l:3::0:)i}%f " ${${(M)$((i%6)):#3}:+$'\n'}; done` => show terminal colors

xonsh
-----

- A mix of a Bash shell and Python interpreter.
- `!()` => executes the command but returns a `CommandPipeline` object
- `a=2` // `$a=2` // `print(a); print($a); print(${a})` => declares and instantiates the 2 different variables `a` and `$a`
- `${...}` => contains all environment variables
- <https://github.com/xonsh/awesome-xontribs>

default applications
--------------------

```
xdg-settings set default-web-browser luakit.desktop
xdg-settings set default-url-scheme-handler http luakit.desktop
xdg-settings set default-url-scheme-handler https luakit.desktop
xdg-mime default luakit.desktop text/markdown
xdg-mime default org.pwmt.zathura-pdf-mupdf.desktop application/pdf
```

git
------------------------------

- `git diff --word-diff`
- `git clone --depth=1` // `git clone --filter=blob:none` => clone only last commit // do not clone blobs (only history)
- `git sparse-checkout set [dir1] [dir2] …` => only checkouts top-level files and dir1 dir2 …
- `git stash --all` // `git stash pop`
- `git log --oneline --decorate --graph` => minimal log
- `git config --global alias.lola "log --graph --decorate --pretty=oneline --abbrev-commit --all"` => crée l'alias `git lola` pour afficher un graphe des commits
- `git log -p` => log with diff
- `git config --global user.signingkey <gpg_key_id>` // `git commit -S` // `git log --show-signature` => sign commit
- Reduce git size => `git gc --aggressive`
- Very aggressive garbage collector => `git -c gc.reflogExpire=0 -c gc.reflogExpireUnreachable=0 -c gc.rerereresolved=0 -c gc.rerereunresolved=0 -c gc.pruneExpire=now gc`
- Retrieve lost commit => `git reflog` && `git checkout` && `git cherry-pick <commit-id>`
- Blame // log only some lines => `git blame -L 20,40 my_file` // `git log -L20,40:my_file`
- Blame a block following `PATTERN` => `git blame :'PATTERN' my_file` // `git blame :'class MyClass' MyClass.java`
- Ignore whitespace => `git blame -w`
- Follow file/blocks around files in _current commit_ => `git blame -C …`
- Follow file/blocks around files in _current commit vs commit that created the file_ => `git blame -C …`
- Follow file/blocks around files in _all commits_ (very useful) => `git blame -C -C -C …`
- `git maintenance` // `git maintenance run` => schedule Git repo optimizations // run now
- `git log --pretty='' --date=short --numstat` => code churn
- `git log --pretty=format:'%s' | tr ' ' '\n' | sed 's/.*/\L&/' | sort | uniq -c | sort -rg | head -n 100` => word cloud from commit messages

nnn
------------------------------

- `~` // `` ` `` // `-` // `@` => go to `~` // `/` // `cd -` // `working_dir`
- `'` => go to file
- `>` => export file list
- `e` => edit file
- `d` => details
- `t` => sort by
- `space` => select file
- `v` // `p` // `x` => move // copy // delete file
- `,` => mark directory (adds a bookmark `,`)
- `b` // `C-/` => go to bookmark
- `Alt-` // `;` => run plugins : `p` => less to show content // `g` => git status
- `]` // `=` => terminal // GUI app
- `nnn -C` => color by context instead of file type
- `nnn -n` // `C-n` => start with type-to-nav // toggle type-to-nav
- `nnn -p <file>` => write end-file or selections to `<file>`
- `n` => use `~/.config/fish/functions/n.fish` to move fish to last `nnn` dir

mupdf
------------------------------

- `W` // `H` => resize to fit screen width // height
- `m` // `t` // `[0-9]m` // `[0-9]t` => mark // go to mark
- `+` // `-` // `z` => zoom +/- // reset zoom
- `P` => page number / total

yazi
------------------------------

- `s` // `S` => search with `fd` // `rg`
- `z` // `Z` => search files with `zoxide` // `fzf`
- `f` => filter
- `O` => open interactive
- `t`, `C-c` => create tab (then `1`, `2`, …) // closes tab
- `cc` // `cd` //`cf` // `cn` => copy absolute path // directory // filename // filename without extension
- `,a` // `,A` // `,n` // `,c` // `,m` // `,e` // `,s` => sort alphabetically // idem (reversed) // naturally // creation // modified // extension // size

zathura
------------------------------

- `a` => best fit
- `s` => width-fit
- `m[a-z] // '[a-z]` => create mark // goto mark
- `d` => dual vs single page
- `f` => follow link
- `r` => rotate
- `C-r` => dark mode
- `F5` => presentation mode

pdfpc
------------------------------

- `pdfpc -w both <file>` => opens both screens in windowed mode
- `Tab` => overview
- `f` => freeze : do not move presentation screen (only monitor screen changes)
- `h` => hide presentation screen
- `m` // `<S-m>` => bookmark slide // goto mark

mutt
------------------------------

- `1` // `2` // `3` => account OVH // gmail // epsi
- `C-g` => cancel current action
- `r` // `f` // `b` => reply // forward // bounce (remail)
- `$` => save changes to mailbox
- `^` => get new mails
- `c` => change mailbox
- `F` // `toggle-new` => Flag (mark important) // mark New
- `t` // `;c` // `;d` => Tag // Copy / Delete tagged
- `o` // `O` => sort
- `v m` => view attachments -> action described in mailcap
- `@` => view full sender em@il
- `Alt-b` => search in messages body
- `:exec <cmd>` => executes a command

## Reader

- `T` => show/hide quoted text
- `h` => show/hide headers

## Editor

- `c` // `b` // `r` => `Cc` // `Bcc` // `Reply-to`
- `p` => `PGP`
- `:my_hdr` => adds a custom header : `X-myheader: myvalue`

aerc
------------------------------

- `C-j` // `C-k` => switch between message types
- `C-x` => execute aerc command while in vim
- `:split` // `:vsplit` => open/close message preview

sfeed curses
------------------------------

- `t` => toggle only unread channels / all channels
- `1` // `2` // `3` => switch layouts
- `r` // `u` => read // unread

cmus
------------------------------

- `:colorscheme <scheme>` => `dracula`, `green`
- `:add <path>` // `:update` => add in library
- `:clear` // `:save <playlist.lst>` // `:load <playlist.lst>`
- `5` // `a` => browser view // add to lib
- `1` //  `Space` => artist view // See albums
- `2` => library view
- `b` // `z` // `c` // `v` => next // previous // pause,continue // stop
- `y` // `e` // `D` => add to playlist // add to queue // remove
- `p` // `P` => change order
- `+` // `-` => sound
- `m` => switch play : all / album / artist
- `s` => shuffle (shows : `S` in statusline)
- `C` => continue playing after song (shows : `C` in statusline)
- `f` => follow (select currently playing track in library view)

Thunderbird
------------------------------

- `C-1` // `C-3` => Navigate mail // agenda

## Message

- `F5` // `S-F5` => get messages // for all accounts
- `F7` => select text mode
- `F8` => main view - toggle message content view
- `F9` => show/hide contacts in compose
- `C-r` // `C-S-r` => reply to sender // reply to all recipients
- `C-l` => forward
- `C-n` => new message
- `C-Enter` => send
- `M` => mark (un)read
- `\` // `*` => collapse/expand threads

## Agenda

- `F11` => today tasks in agenda
- `C-i` // `C-d` => new event // task
- `A-end` => today
- `[` // `]` => navigate calendar

foot
------------------------------

- `C-S-n` => new term (in current folder)
- `S-PageUp` // `S-PageDown` => scroll output
- `C-S-r` => search output
- `C-S-z` // `C-S-x` => navigate prompts history in output
- `C-S-o` => open URL
- `S-Insert` => copy primary

TTY
------------------------------

- `tty` => shows TTY device associated with current terminal (`tty` or `pts`). Can be used to redirect cmd input/output from/to other TTY.

lxc
------------------------------

- `lxc-create <name> -t oci -- --url docker://<image>` => create a LXC container from a Docker image (using OCI)

tmux
------------------------------

- `tmux new -s s1` // `tmux attach-session -t s1` => create session and attach to it (possible at the same time for pair programming)
- `<C-b>`` +`:set status off` => hide status bar

Android
=======

- `fdroid` // `aurora` => FOSS store // alternate to Play store app with same content
- `mull` => Firefox version with security included
- `opera mini` => can use Opera proxies to compress data - useful abroad
- `K-9` => mail client (now endorsed by Thunderbird)
- `SimpleLogin` => email aliases
- `DAVx5` => imap sync
- `signal` => very good IM
- `KeyPass` => TOTP and password generator
- `OSMAndPlus` => complex but very complete navigation tool - based on OpenStreetMap and can add other sources (French IGN, ...)
- `StreetComplete` => contribute to OpenStreetMap
- `mupdf` => PDF viewer
- `Phonograph Plus` // `vlc` => music player // video player
- `termux` => android shell - supports a lot of CLI-based Linux apps
- `freshrss` => RSS viewer (can synchronize with a hosted freshrss instance)
- `insular` => isolate some apps in _islands_ and stops them while the island is not running
- `futo` => local keyboard with voice-to-text

Isolation
=========

- <https://hub.docker.com/u/kasmweb> => Linux distribution / application in Docker container with VNC access in browser
