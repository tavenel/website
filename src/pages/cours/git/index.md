---
pagetitle: Tom Avenel - Git
updated: 2024-03-06
---

#   Git™

![](/resources/images/cover/git.jpg)

## 💡 Résumé des bases

```
+-----------+    +---------+    +-------------+  +---------------+ 
| Working   |    | Staging |    | Dépôt local |  | Dépôt distant | 
| Directory |    |         |    |   .git      |  | .git          | 
+-----------+    +---------+    +-------------+  +---------------+ 
      |                 |               |                |
      |<=================================================|
      |                          clone                   |
      |                 |               |                |
      |================>|               |                |
      |       add       |               |                |
      |                 |               |                |
      |                 |==============>|                |
      |                 |     commit    |                |
      |                 |               |                |
      |                 |               |===============>|
      |                 |               |      push      |
      |                 |               |                |
      |                 |               |<===============|
      |                 |               |      fetch     |
      |                 |               |                |
      |<================================|                |
      |        checkout / merge         |                |
      |                 |               |                |
      |<=================================================|
      |                          pull                    |
      |                 |               |                |
```

1. `git rev-parse --show-toplevel` : Vérifier le répertoire parent contenant le dossier `.git`
2. `git add -p` : Ajoutez des modifications partie par partie. Idéal pour des commits propres et ciblés.
3. `git commit mon_fichier` : Ignore les changements en staging et crée un commit contenant la version actuelle d'un fichier déjà connu
4. `git commit -a` : Ajoute au staging les états actuels de tous les fichiers déjà connus par Git et en crée un commit.
5. `git commit --amend` : Modifiez votre dernier commit : corriger un message, ajouter un fichier oublié.
6. `git reset --soft HEAD~1` : Annulez le dernier commit en conservant vos modifications. ⚠️  Attention avec l'option `--hard` qui supprime définitivement les modifications
7. `git stash / git stash pop` : Mettez de côté vos modifications temporairement. Idéal pour switcher rapidement de branche.
8. `git cherry-pick <commit-hash>` : Appliquez un commit spécifique d'une autre branche.
9. `git branch -d <branch-name>` : Nettoyez vos branches locales inutilisées.
10. `git log -- <file>` : Visualisez l'historique d'un fichier spécifique (attention à l'espace après `--`).
11. `git blame <filename>` : Identifiez qui a modifié chaque ligne de code.
12. `git bisect` : Trouvez le commit qui a introduit un bug grâce à une recherche dichotomique.
13. `git merge --abort` : Annulez une fusion problématique.
14. `git log --grep="xxx"` : Recherchez dans les messages de commit.
15. `git tag -a v1.0 -m "Version 1.0"` : Marquez les moments importants de votre projet avec des tags.
16. `git clean -fd` : Nettoyez votre espace de travail. ⚠️utilisez d'abord `git clean -n` pour prévisualiser les suppressions
17. `git reflog` : Visualisez l'historique de toutes les opérations Git.
18. `git rebase -i HEAD~<n>` : Réorganisez vos commits. ⚠️ À éviter sur des branches partagées.
19. `git revert <commit-hash>` : Annulez proprement un commit sans réécrire l'historique.
20. `git fetch --all --prune` : Synchronisez et nettoyez votre repo en une commande.
21. `git log --graph --oneline --all` : Visualisez graphiquement l'historique de toutes vos branches.
22. `git log --name-status` : Affiche le nom des fichiers modifiés (et leur status, sinon `--name-only`)
23. `git log --source --all` : Ajoute l'information de branche pour chaque commit
24. `git diff --staged` : Examinez les modifications qui sont dans la staging area avant de commiter.
25. `git show <commit-hash>` : Affichez les détails complets d'un commit spécifique.
26. `git archive` : crée une archive contenant les fichiers d'un commit ou d'une branche sans inclure l'historique Git

## 🤓 Cours

- [html](/cours/git/git-cours.html)
- [pdf](/cours/git/git-cours.pdf)
- [markdown](/cours/git/git-cours.md)

## 🔗 Liens

Voir les [ressources utiles](/cours/git/git-cours.html#64) du cours.

## 💻 TP - Premiers pas

L'objectif de ce TP est d'installer et de configurer git, puis de se familiariser avec ses concepts de base.

- [html](/cours/git/git-tp-commit.html)
- [pdf](/cours/git/git-tp-commit.pdf)
- [markdown](/cours/git/git-tp-commit.md)

## 💻 TP - Le gitignore

Petit TP dont l'objectif est d'utiliser le fichier spécial `.gitignore` pour masquer des fichiers à Git.

- [html](/cours/git/git-tp-gitignore.html)
- [pdf](/cours/git/git-tp-gitignore.pdf)
- [markdown](/cours/git/git-tp-gitignore.md)

## 💻 TP - Utiliser l'historique de Git™

L'objectif de ce TP est d'utiliser les fonctions d'historique de git.

- [html](/cours/git/git-tp-historique.html)
- [pdf](/cours/git/git-tp-historique.pdf)
- [markdown](/cours/git/git-tp-historique.md)

## 💻 TP - Github® et dépôts distants

 L'objectif de ce TP est de créer, configurer et utiliser un dépôt git distant sur la plateforme Github®.

- [html](/cours/git/git-tp-github.html)
- [pdf](/cours/git/git-tp-github.pdf)
- [markdown](/cours/git/git-tp-github.md)

## 💻 TP - Les branches Git™

 L'objectif de ce TP est de manipuler un des concepts les plus puissants de Git™ - la notion de branches.

- [html](/cours/git/git-tp-branches.html)
- [pdf](/cours/git/git-tp-branches.pdf)
- [markdown](/cours/git/git-tp-branches.md)

## 💻 TP - Les tags

Petit TP permettant de découvrir les tags dans Git.

- [html](/cours/git/git-tp-tags.html)
- [pdf](/cours/git/git-tp-tags.pdf)
- [markdown](/cours/git/git-tp-tags.md)

## 💻 TP - Workflows Git™ et Pull Request

 L'objectif de ce TP est de travailler sur un projet en suivant des workflows Git et de s'initier au principe de la pull-request.
 **L'intégralité de ce cas pratique est à réaliser en binôme.**

- [html](/cours/git/git-tp-workflows-pr.html)
- [pdf](/cours/git/git-tp-workflows-pr.pdf)
- [markdown](/cours/git/git-tp-workflows-pr.md)

## 💻 TP - Workflow de Fork

 L'objectif de ce TP est de découvrir le principe du fork pour partager des changements sur un logiciel sans impacter le dépôt officiel.

- [html](/cours/git/git-tp-fork.html)
- [pdf](/cours/git/git-tp-fork.pdf)
- [markdown](/cours/git/git-tp-fork.md)

## 💻 TP - Git™ Bisect

 L'objectif de ce TP est d'utiliser la commande Git Bisect pour trouver un commit par dichotomie.

- [html](/cours/git/git-tp-bisect.html)
- [pdf](/cours/git/git-tp-bisect.pdf)
- [markdown](/cours/git/git-tp-bisect.md)

## 💻 TP Github - Utiliser les Gist

Petit TP dont l'objectif est de découvrir les Gist de GitHub.

- [html](/cours/git/git-tp-github-gist.html)
- [pdf](/cours/git/git-tp-github-gist.pdf)
- [markdown](/cours/git/git-tp-github-gist.md)

## 💻 TP Github - Les actions (introduction à la CI)

Les _Actions_ GitHub permettent très facilement une initiation à un worflow d'intégration continue très limité.

- [html](/cours/git/git-tp-github-actions.html)
- [pdf](/cours/git/git-tp-github-actions.pdf)
- [markdown](/cours/git/git-tp-github-actions.md)

## 💻 TP - Git pour un Projet XAMPP

Configurer un environnement de développement local avec XAMPP et utiliser Git pour versionner une application web stockée dans le dossier `htdocs`.

- [html](/cours/git/git-tp-xampp.html)
- [pdf](/cours/git/git-tp-xampp.pdf)
- [markdown](/cours/git/git-tp-xampp.md)

## 💻 TP Neovim - gérer ses configurations avec Git

L'objectif de ce TP est d'utiliser Git pour gérer les fichiers de configuration d'un programme (ici `Neovim`).

- [html](/cours/git/git-tp-iac-nvim.html)
- [pdf](/cours/git/git-tp-iac-nvim.pdf)
- [markdown](/cours/git/git-tp-iac-nvim.md)

## 💻 TP utiliser Ansible avec Git

L'objectif de ce TP est d'utiliser Ansible et Git pour réaliser de l'Infrastructure-as-Code.

- [html](/cours/git/git-tp-ansible.html)
- [pdf](/cours/git/git-tp-ansible.pdf)
- [markdown](/cours/git/git-tp-ansible.md)

## 💻 TP - Intégrer Git dans un IDE

L'objectif de ce TP est d'utiliser Git directement dans l'IDE et d'y afficher les derniers changements dans le code.

- [html](/cours/git/git-tp-ide.html)
- [pdf](/cours/git/git-tp-ide.pdf)
- [markdown](/cours/git/git-tp-ide.md)

## 💻 TP - Manipulations avancées de la HEAD

Dans ce TP, nous allons voir des commandes avancées pour déplacer le pointeur vers le commit courant (`HEAD`) de Git.

- [html](/cours/git/git-tp-deplacer-head-avance.html)
- [pdf](/cours/git/git-tp-deplacer-head-avance.pdf)
- [markdown](/cours/git/git-tp-deplacer-head-avance.md)

