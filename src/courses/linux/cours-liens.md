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

```plantuml
title: Lien réel vs lien symbolique

@startuml
folder "source" {
  [F1]
}

folder "Lien réel (hard link)" {
  [F2]
}

[Lien symbolique] as F3

database "Données" as data {
}

[F1] -> data
[F2] -> data
[F3] ..> F1
@enduml
```

---

```plantuml
@startuml
title: Suppression du fichier source

folder "Lien dur (hard link)" {
  [F2]
}

[Lien réel (symbolic)] as F3

database "Données" as data {
}

[F2] -> data
[F1] #red
[F3] ..> F1 #red
@enduml
```

---

