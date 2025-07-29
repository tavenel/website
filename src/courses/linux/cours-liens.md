---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Liens symboliques et réels
layout: '@layouts/CoursePartLayout.astro'
---

## inode

- _Index node_ : structure de données qui stocke les attributs d'un fichier
- permissions, propriétaire, bloc disque de stockage, ...

---

## Liens symboliques

- Type spécial de fichier
- _Lien symbolique_ (ou lien faible, _soft link_) : pointe vers le chemin d'un autre fichier (_target_)
  + `ln -s TARGET NOM_DU_LIEN`
  + Si suppression de la target, pointe vers rien
- _Lien réel_ (_hard link_) : 2e référence vers le même fichier
  + toujours 1 seul inode
  + `ln TARGET NOM_DU_LIEN`

---

```mermaid
---
title: Lien réel vs lien symbolique
---
flowchart LR
    subgraph source
        F1["F1"]
    end

    subgraph hard["Lien réel (hard link)"]
        F2["F2"]
    end

    F3["Lien symbolique (F3)"]

    DATA[("Données sur disque")]

    %% Lien réel (hard link)
    F1 --> DATA
    F2 --> DATA

    %% Lien symbolique
    F3 -.-> F1

```

---

```mermaid
---
title: Suppression du fichier source
---
flowchart TD
    %% Données sur disque
    DATA[("Données sur disque")]

    %% Lien dur (toujours valide)
    subgraph hard["Lien dur (hard link)"]
        F2["F2"]
    end

    %% Fichier source supprimé
    F1["F1 (supprimé)"]:::deleted

    %% Lien symbolique devenu cassé
    F3["Lien symbolique (F3)"] -.-> F1

    %% Connexions
    F2 --> DATA

    class F1 red
```

---

