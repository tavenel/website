---
pagetitle: Tom Avenel - Git
---

#   Git™

_Modifié le: 2024-03-06_

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

1. `git add -p` : Ajoutez des modifications partie par partie. Idéal pour des commits propres et ciblés.
2. `git reset --soft HEAD~1` : Annulez le dernier commit en conservant vos modifications. Attention avec l'option --hard qui supprime définitivement les modifications 😉  
3. `git commit --amend` : Modifiez votre dernier commit. Parfait pour corriger un message ou ajouter un fichier oublié.
4. `git stash / git stash pop` : Mettez de côté vos modifications temporairement. Idéal pour switcher rapidement de branche.
5. `git cherry-pick <commit-hash>` : Appliquez un commit spécifique d'une autre branche.
6. `git branch -d <branch-name>` : Nettoyez vos branches locales inutilisées.
7. `git log -- <file>` : Visualisez l'historique d'un fichier spécifique.
8. `git blame <filename>` : Identifiez qui a modifié chaque ligne de code.
9. `git bisect` : Trouvez le commit qui a introduit un bug grâce à une recherche dichotomique.
10. `git merge --abort` : Annulez une fusion problématique. La sortie de secours parfaite !
11. `git log --grep="xxx"` : Recherchez dans les messages de commit. Retrouvez rapidement ce que vous cherchez.
12. `git tag -a v1.0 -m "Version 1.0"` : Marquez les moments importants de votre projet avec des tags.
13. `git clean -fd` : Nettoyez votre espace de travail. ⚠️utilisez d'abord `git clean -n` pour prévisualiser les suppressions
14. `git reflog` : Visualisez l'historique de toutes les opérations Git. Votre filet de sécurité !
15. `git rebase -i HEAD~<n>` : Réorganisez vos commits. ⚠️ À éviter sur des branches partagées.
16. `git revert <commit-hash>` : Annulez proprement un commit sans réécrire l'historique.
17. `git fetch --all --prune` : Synchronisez et nettoyez votre repo en une commande.
18. `git log --graph --oneline --all` : Visualisez graphiquement l'historique de vos branches.
19. `git diff --staged` : Examinez les modifications qui sont dans la staging area avant de commiter.
20. `git show <commit-hash>` : Affichez les détails complets d'un commit spécifique.

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

