---
title: Notes VIM
created: 2022-03-01
checked: 2024-12-17
layout: '@layouts/CourseLayout.astro'
---

## LazyVim

- `<c-o>`, `<c-i>`, `gd`, `[…` : navigate code
- `<leader>ss` : jump function in current buffer
- `<leader>bp` // `<leader>bP` : pin buffers // delete all non pinned buffers

## Move

- `*` // `#` // `g*` // `g#` => (reverse-)search current word (`*` for whole word, `g*` for words containing it)
- `H // M // L` => High // Middle // Low parts of the screen
- `gj` // `gk` // `g0` // `g$` => move in visual line (as breaks in the editor)
- `zj` // `zk` => move between fold(ed) sections
- `(` // `)` => move to begin // end of line
- `{` // `}` => move to begin // end of paragraph
- `[[` / `]]` => move to begin // end of function
- `%` => move to matching char : (), {}, …
- `f-'char' // F-'char'` => move to next // previous 'char' on the line
- `0` // `^` // `$` => start // 1st char // end of line
- `d^` // `d$` …

- `vap` // `dap` => view /delete / … all paragraph
- `vi(` // `vi[` // `ci[` // `ci'` => view in next `()` // `[]` // change in `[]` // `''`
- `va(` // `va[` => view all including  `()` // `[]`

- `V` => visual mode on LINES
- `C-v` => block selection
- `gv` => back to last visual selection
- `gn` // `gN` => visually selects next selection (and `cgn`, `dgn`)

- `C-o` // `C-i` => previous // next moves in jumplist
- `g;` // `g,` => previous // next moves in changelist
- `''` // same with backtick => go before latest jump

### Scroll

- `C-e // C-y` => scroll without moving cursor
- `C-f // C-b` => scroll page

### Fast move

- `C-d // C-u` => move & scroll

### Folding / Unfolding

- `zc` // `zC` // `zo` // `zO` => fold/unfold, capital is recursive

### Text objects

- `i` // `a` => _inside_ : `ci(` to change text inside the next `()` // _around_ : `daw` to delete around the current word
- usage: `d`, `y`, `c` switch to _OPERATOR-PENDING_ mode // _VISUAL_ mode

## Registers

- `"ay // "ap` => copies/paste register 'a'
- `"xp` // `C-r x`=> paste register `x` (normal mode // insert mode)
- `"x` // `"X` => replace register `x` (lowercase) // append to register `x` (uppercase) - `"x` and `"X` same register
- `"1 // .. // "9` => history
- `:reg` => show registers

### Special registers

- `""` => default unnamed delete/yank register (line)
- `"-` => small delete (NO yank) register (\<line)
- `"0` => last (unnamed) yank
- `"1` // .. // `"9` => last to previous unnamed deletes/changes
- `"+y` => system clipboard
- `"*y` => X Window primary selection
- `"~` => drag-and-drop register (GVim only)
- `"%` // `"#` => current file name // alternate (last-edited) file
- `":` => last command
- `".` => last inserted text
- `"=` => expression register
- `"/` => last search
- `"_` => `/dev/null`

## Marks

- `m xxx` // `m XXX` => add a mark within the file // valid between all files
- `\`xxx ` => go to mark or go to first non-blank char of the mark
- `<` // `>` => start / end of last visual
- `[` // `]` => start / end of last edit
- `'` // `\` `  => last jump
- `^` // `gi` => last insert stop mark // insert text after last insert
- `"` => last position in this buffer when closed
- `:marks` => show marks

## Windows and Buffers and Tabs

- `C-w s // C-w v` // `:sp` // `:vsp` => splits (vertically)
- `C-w C-w` // `C-w h,j,k,l` => navigate between splits
- `C-w S-h, S-j, S-k, S-l` => move window (exchange)
- `C-w H` // `C-w K` => change splits horizontal // vertical
- `C-w =` => all windows same size
- `:b` // `:bn` // `:bp` => choose buffer to use // next // previous
- `:ls` => lists buffers
- `:bufdo` => idem `argdo` for buffers
- `C-^` // `C-w ^` // `2C-^` => **Switch current / alternate file in Normal mode** // Edit alternate in split // siwtch to `2nd` or `Nth` alternate file
- `:file <name>` => renames current buffer (and window title)
- `:tabf` // `gt` // `gT` // `1gt` => new tab // next // previous // tab 1
- `:tcd` => `cd` for current tab only

### Argslist (i.e. stable buffer)

- `:ar` // `:args` => list args list
- `:ar <file1> <file2> …` => redefine the args list
- `:n` // `:p` // `:first` // `:last` => navigate to args list
- `:argdo update` // `:argdo edit!` => apply changes // revert to all files in args list

## Auto-completion

- `C-d` => auto-completes
- `C-n` // `C-p` => auto-complete based on last inputs
- `:e C-d` => lists of files to open
- `C-x C-o` => code auto-complete
- `C-x C-n // C-x C-p // C-x C-`l=> auto-completes word (next/previous) // line
- `C-x C-f` => auto-completes file path (expands environment variables)
- `C-x C-l` => complete a whole line from the content of one buffer
- `C-x s` => complete with spelling suggestions
- `C-x C-v` => complete with the command line history
- `C-x C-i` => complete with the keywords in the current and included files (in option `path`).
- `C-y` // `C-e` => accept / cancel auto-complete (idem for all menus)
- `##` => expands all filepath of each buffer in the arglist, e.g. `:args git ls-files` then `:vimgrep /{pattern}/g ##`

## Goto (and code)

- `gf` // `C-w f` // `C-w gf` => go to file under cursor. Works in Neovim terminal too. // in new window // in new tab
- `gd` // `gD` // `1gd` // `1gD` => goto local (jump to definition) // global variable declaration (`1gd` ignores 1st `{}`)

## Regexp

- Specials :
  - `.` => current line
  - `$` => last line
  - `%` => all lines (substitute for `1,$`)
  - `'a` => mark `a`
  - `'<,'>` => all visual selection (default when `:`)

- `:START,END/re/p` => `grep` mode.
  - `p` => paste
  - `d` => delete
  - `m` // `m$` => move lines // move to end of file
  - `j` => join

To change every occurrence of a character string between two lines,

- Type   `:START,ENDs/old/new/g`    where START,END are the line numbers of the range of lines where the substitution is to be done.
- Type   `:%s/old/new`         to change every occurrence in the current line.
- Type   `:%s/old/new/g`       to change every occurrence in the whole file.
- Type   `:%s/old/new/gc`      to find every occurrence in the whole file, with a prompt whether to substitute or not.
- Type   ``` %s/`\(.*\)`/… ``` to capture all text in the search pattern and re-use it with `\1` in the `/new/` part

**Full expression** : `:START,ENDg/re/s/foo/bar/g` => find and replace

## Spellcheck

- change locale => `:setlocal spell spelllang=en_us`

## Search / Match

- `:highlight` => lists highlights
- `match <highlight> /<search>/` // `2match …` // `3match …` => colored search using highlight pattern (e.g. : `SpellBad`, `Todo`, …)

## Katas and tips

- `:set makeprg=gradle` => change `:make` program
- `ZZ` // `ZQ` => `:wq` if file changed // `:q!`
- Wrap `word` with 1 char `"` => `c i w " " <ESC> P`
- Wrap `word` with multiple chars `<p></p>` => `c i w <p> C-r " </p>`
- Transform tabs to spaces => `:set expandtab` and `:retab!` // inverse with
  `:set noexpandtab` and `:retab!`
- `v + :w` => writes selection to file
- `v + :r` => imports file in current buffer
- `:r + !` => imports output of cmd
- `:vimgrep /<C-r>// %` => search (vimgrep) the last search history (`C-r /`) in current file (`%`) (or in all buffers : `#`) ~> results in the quickfix list
- ``` :vimgrep /pattern/ `git ls-files` ``` => search only in `git ls` results
- `:argdo %s/{pattern}/{replacement}/ge` // then `:argdo update` => applies regexp to everything in the args list, `/e` is to ignore files not matching // then writes files
- `qA` => appends to macro `a`
- `:g/pattern/normal …` => `normal` all lines having `pattern`
  - `:g/pattern/normal @i` => applies macro `i` to lines containing `pattern` (in `normal` mode)
- `'<,'>normal @i` => applies macro `i` to the current selection
- `C-o` => previous cursor position - even in previous buffer (if new file opened in current view)
- `C-^` => switch to previous buffer (see windows)
- `^` => back to previous
- `gi` => insert in last `i` position (goto `^` and insert)
- `<C-v> code` => inserts unicode character (`C-v u…`)
- `:vs#` => re-open last opened buffer (alternate file) in a vertical split
- modify a macro => `put a` then `"a yy" => show macro`a` then send line of instructions into macro `a`

### Modify quickfix list

- check `errorformat` is OK in `vimrc`
- `:set modifiable`
- edit quickfix => `:g/NOT WANTED/d`
- `:cbuffer` => updates the quickfix

### Copy line

- `:9y` => yanks line 9
- `:9t16` // `:9t.` => copy line 9 to line 16 // copy line 9 to current line
- `:-7t.` // `:+5t.` => copy relative line -7 // +5 to current

## Command mode

- `C-f` => search in history => cmds can be changed with Vim syntax !
- `C-r <register>` => copies the content of register (works in insert-mode too)
- `C-r %` => copies current file name
- `C-r C-f` => Copy the filename under the buffer's cursor.
- `C-r C-w` => Copy the word under the buffer's cursor.
- `C-r C-a` => Copy the WORD under the buffer's cursor.
- `C-r C-l` => Copy the line under the buffer's cursor.

## Visual mode

- `:norm <cmd>` => applies _normal-mode_ cmd to selected lines (e.g. to comment lines)
- `:! <cmd>` => executes the selected line(s) using the given cmd
- `<` // `>` => indent selection
- `o` // `O` => go to the other corner // side of the selection (different for visual block, same for visual lines)

## Normal mode

- `#` => search current word
- `:noh` => clear search
- `/\c <pattern>` // `/\C <pattern>` => force insensitive/sensitive search
- `gq` => wrap lines (on context => `}` for paragraph, `gg gq G` for whole file)
- `<<` // `>>` => indent current line
- `S` => insert at correct indentation

## Insert mode

- `S` => insert text at correct indentation
- `C-k 'e` // C-k \`e => é // è
- `C-w` // `C-u` => delete last word // last line

## Externals

- `:r[ead]` => inserts file (or result of `!cmd`)
- `:.!(cmd)` => executes the `cmd` on current line (e.g. : `sh`)

### Computations : special register =

- From Insert mode : `C-r =` -> `C-r "` => expression mode (calculations) // in
  expression-mode : paste and compute
- From Command Mode : `put =`

## Lists

### Changelist

- `:changes` => list changes

### Jumplist

- `:jumps` => list of cursor positions
- `C-O` // `C-I` => jump between positions

### Quickfix list

- `:copen` // `:cw` => open quickfix // only if errors
- `:cn` // `:cp` // `:cnf` => next // previous quickfix entry // first in next file
- `:cdo s/foo/bar/ | update` => exec cmd on each entry (and updates the buffer to disk)
- `:cdo %s/foo/bar/gc` => global replace with confirmation (`c`)
- `:cfdo bd` => exec cmd on each file (here: close all buffers in quickfix)
- `:Telescope diagnostics` -> `C-q` => diagnostics to quickfix
- `:grep` // `:vimgrep` // `:make` => populate the quickfix
- `:colder` // `:cnewer` => navigate to the 10 quickfix lists

### Location list : quickfix local to window

- `:lopen` // `:lnext` // `:lprev` //
- `:lgrep` // `:lvimgrep` // `:lmake` => populate the location list
- `:lolder` // `:lnewer` => navigate to the 10 location lists

## vimdiff

- `vimdiff <file1> <file2>`
- `]c` // `diffget` // `diffput` => next change // //
- `:windo diffthis` // `:windo diffoff` => diff between splits in current window

## Params

- `:set number` => show line numbers
- `:set relativenumber` => show line numbers
- `:set ic // noic` => ignore case
- `:set hls // nohls` => highlight search
- `:set is` => search-as-you-type

## Sessions

- `:mksession [filename]`
- `vim -S Session.vim`
- `:earlier 10m` // `:later 10m` => moves 10mins earlier / later in history
- `g+` // `g-` => move in history by time instead of last modif branch (CONFUSING). Allows to traverse undo tree. See Gundo plugin

## NeoVim

- `:Man` => opens a man page

## CLI

- `vim -o <files>` // `vim -O <files>` // `<vim -p <files>` => open files in split // vsplit // windows
- `C-]` => go to link in help

## Vim commands stored in edited file

- `#vim: set fileencoding=utf8` => start with `#vim:`

## Vimdiff

- `do` // `dp` => Copy other line to current // Copy current line to other
- `]c` // `[c` => Next diff / previous diff
- `zo` // `zf` => Open // close fold

## GitGutter

- `]c` // `[c` => Next diff / previous diff
- `<leader>hp` //  `<leader>hs` // `<leader>hu` => preview // stage // undo hunks

## Tips for the Quickfix

### Make

- Vim use `make` as a default task runner for `:make`.
  - `:make` // `:lmake` fills the quickfix

- `:set makeprg` to change the `:make` program.
- `%<` // `#<` to insert the current // alternate file name without extension
  - `:set makeprg=npm\ run\ test\ %<.test.js`
- `$*` populates all the arguments from `:make …`
  - `:set makeprg=latex\ \\\\nonstopmode\ \\\\input\\{$*}`

### Grep / Vimgrep

- `:vimgrep /<pattern>/ <files>` calls the internal Vim grep with a pattern, for example :
  - `:vim /^#/ %` prints all lines starting with `#` in the current buffer (i.e. the TOC of a Markdown file)
  - ``` :vim #sysops# `git ls-files` ```
- `:grep` calls the external Grep program (using `grepprg`)
  - `set grepprg=rg\ --vimgrep\ --smart-case\ --follow`
  - ```:grep -ri sysops `git ls-files` ```

### Quickfix history

- `:colder` / `:cnewer` // `:lolder` … // `:chistory` to jump between quickfix / location lists

### Actions on quickfix list

- `:set modifiable` and `:cgetbuffer` in the quickfix window to edit and reload the QF with changes (e.g. delete lines)
- `:cdo s/foo/bar/ | update` executes a command in the QF list (`:cfdo bd` iterates only on files in the QF)

### Populate QF

- `:cexpr system('grep …')` => Execute a system cmd and move results to the quickfix
- Add grep results to location list : `:g/mypattern/laddexpr expand("%") .. ":" .. line(".") ..  ":" .. getline(".")`
- `:packadd cfilter` // `:Cfilter` … // `:Cfilter!` … (reverse)
- `:botright cwindow` => occupy full width (else if vertical splits, at the bottom of the rightmost column of windows).
- `set errorformat+=%f\|%l\ col\ %c\|%m` : Teach Vim to read its own Quickfix lists. Seems OK in Neovim

## Filter

- `:filter /<pattern>/ <cmd>` => filter `<cmd>` according to `<pattern>`
- `:filter /content/ buffers` => Only output the buffers with part of the filepath matching content.
- `:filter /archives/ oldfiles` => Only output the marked files with part of the filepath matching archives.
- `:filter!` => reverse filter

## Cheatsheet

- ![Cheat Sheet Vim](@assets/vim/vi-cheatsheet.jpg)
- ![Vim Quickfix commands](@assets/vim/vim-quickfix.png)

## Links

- `:help index` => all shortcuts
- `curl -s -m 3 https://vtip.43z.one` => random Vim tip
- Another Vim cheatsheet : <https://quickref.me/vim>
- [Neovim - Getting started](https://www.reddit.com/r/neovim/wiki/index/getting-started/)
- [Demo Vim expert](https://youtube.com/watch?v=MquaityA1SM)
- [Vimcasts - Special registers & advanced C-r paste](http://vimcasts.org/episodes/pasting-from-insert-mode/)
- [Vimcasts - Ugly registers behaviors](http://vimcasts.org/blog/2013/11/registers-the-good-the-bad-and-the-ugly-parts/)
- [Vimcasts - Vim profiling](http://vimcasts.org/episodes/profiling-vimscript-performance/)
- [Vimcasts - buffers, windows, tabs](http://vimcasts.org/categories/managing-your-workspace)
- [Vimcasts - Replace in many files (expert)](http://vimcasts.org/episodes/project-wide-find-and-replace/)
- [Vimcasts - Folding](http://vimcasts.org/episodes/how-to-fold/)
- [Doc Vim](https://github.com/mhinz/vim-galore)
- [Wiki Golf (challenges)](http://www.vimgolf.com/)
- [Vim intro](https://www.barbarianmeetscoding.com/blog/boost-your-coding-fu-with-vscode-and-vim/)
- [Error format for java/ant/junit/cygwin](https://vim.fandom.com/wiki/Errorformat_for_java/ant/junit/cygwin/bash)
- [Vim UI concepts : buffers, windows, tabs](https://stackoverflow.com/questions/26708822/why-do-vim-experts-prefer-buffers-over-tabs#26710166)
- <https://thevaluable.dev/vim-commands-beginner/>
- <https://thevaluable.dev/vim-intermediate/>
- <https://thevaluable.dev/vim-advanced/>
- <https://thevaluable.dev/vim-adept/>
- <https://thevaluable.dev/vim-veteran/>
- <https://thevaluable.dev/vim-expert/>
- <https://thevaluable.dev/regular-expression-basics-vim-grep/>
- <https://thevaluable.dev/vim-regular-expressions-in-depth/>
