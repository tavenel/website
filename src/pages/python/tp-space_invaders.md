---
title: TP Space Invaders
---

# TP Space Invaders

## Espace de jeu

Définir en Python une classe `Space` dont le constructeur fournit 2 attributs aux instances de cette classe : `nb_l`, et `nb_c` de type entiers, et signifiant les nombres de lignes et de colonnes de l'espace de jeu.
 
## Affichage de la grille

Ajouter à cette définition de classe un attribut d'objet `grille`: une liste initialement vide. Écrire, dans le constructeur de la classe, à l'aide de deux boucles `for ... in ...` imbriquées, un algorithme permettant d'initialiser la grille comme une tableau de `nb_l` lignes et `nb_c` colonnes. Les cellules du tableau contiennent initialement un unique caractère `" "` (espace).

Par exemple, à l'issue de l'instanciation d'un espace de 4 lignes et 10 colonnes :

```python
>>> s = Space(4, 10)
```

sa grille vaudra :

```python
>>> s.grille
[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
```

## Invaders

Définir en Python une classe `Invader` dont le constructeur déclare l'attribut `c` permettant de spécifier le type d'envahisseur. Ce sera un simple caractère, qui vaudra `#` par défaut.
 

## Affichage d'un invader

Ajouter à cette classe une méthode `__repr__` (méthode automatiquement appelée par la fonction `print()`), et qui renvoie une chaîne de caractères représentant l'envahisseur. Dans un premier temps, ce sera simplement l'unique caractère défini à la question précédente.

Par exemple, à l'issue de l'instanciation d'un envahisseur, on pourra l'afficher ainsi :

```python
>>> i = Invader()
>>> str(i)
#
```
 
## Envahisseurs dans la grille

On souhaite faire apparaitre en haut de l'espace une ligne d'envahisseurs !

Modifier la construction de la grille de l'espace de jeu en remplaçant les espaces de la première ligne par des envahisseurs (ces cellules de la grille ne contiennent alors plus un caractère, mais un objet de type `Invader`).

## Afficher l'espace de jeu

Il est temps d'afficher l'espace de jeu :

Ajouter à la classe `Space` une méthode `__repr__` (cette méthode, automatiquement appelée par la fonction `print()`,  n'attend aucun autre argument que l'objet lui-même, et doit renvoyer une chaîne de caractères).

À présent si l'on crée un espace de jeu de 6 lignes et 10 colonnes :

```python
>>> s = Space(6, 10)
```

On peut l'afficher avec un simple `print` :

```python
>>> print(s)
##########
          
          
          
          
          
>>>
```

## Cadre de jeu

Rajouter un « cadre » autour le l'espace pour qu'il soit mieux visible à l'écran (utiliser les caractères ┌ ┐ └ ┘ ─ |).
L'espace de jeu doit à présent avoir cette apparence :

```python
┌──────────┐
|##########|
|          |
|          |
|          |
|          |
|          |
└──────────┘
```
 
## Tir

Ajouter à la classe `Space` une méthode `tirer` qui permet de lancer un missile depuis le sol, à partir d'une position donnée. Le missile traverse alors l'espace de jeu jusqu'à toucher un envahisseur (On utilisera la fonction `time.sleep` pour ralentir l'affichage au fur et à mesure que le missile monte).

Par exemple, si on déclenche un tir depuis la position 2 :

```python
s.tirer(2)
```

L'espace de jeu prend les apparences successives suivantes :

```python
┌──────────┐
|##########|
|          |
|          |
|          |
|          |
|  ^       |
└──────────┘
┌──────────┐
|##########|
|          |
|          |
|          |
|  ^       |
|          |
└──────────┘
┌──────────┐
|##########|
|          |
|          |
|  ^       |
|          |
|          |
└──────────┘
┌──────────┐
|##########|
|          |
|  ^       |
|          |
|          |
|          |
└──────────┘
┌──────────┐
|##########|
|  ^       |
|          |
|          |
|          |
|          |
└──────────┘
┌──────────┐
|##^#######|
|          |
|          |
|          |
|          |
|          |
└──────────┘
```
 
## Objet canon

1. Créer une classe `Canon`, représentant le canon qui tire les missiles depuis le sol. Le canon possède un attribut `pos`, qui mémorise sa position dans la grille. Ne pas oublier de lui donner une méthode `__repr__` !
2. Instancier un unique canon dans le constructeur de l'espace de jeu.

## Canon dans la grille

1. Modifier la construction de la grille pour y faire figurer le canon.
2. Modifier la méthode tirer pour que le tir parte depuis la position du canon.

## Utilisation du clavier

Utiliser le module `keyboard` pour déplacer le canon de gauche à droite et déclencher les tirs.

Il faudra auparavant installer ce module :

```shell
pip install keyboard
```

[Documentation complète](https://github.com/boppreh/keyboard#api)

Nous n'utiliserons que la fonction `keyboard.read_key()` de la manière suivante :

```python
keyboard.read_key(suppress=True)
time.sleep(0.2) # permet d'éviter de détecter plusieurs appuis sur la touche
```

Grâce à cette fonction, le programme s'interrompt jusqu'à ce que l'utilisateur appuie sur une touche, puis la valeur de la touche est renvoyée.

## Score et animation

Ajouter un attribut `score` à la classe `Space`, l'incrémenter à chaque destruction d'envahisseur et l'afficher en dessous de l'espace de jeu.
Faire descendre les envahisseurs progressivement au cours de la partie (un à un ou en bloc) : le jeu doit rester jouable !!

:::correction
# Correction

```python
import time, sys
import keyboard

class Space:
    def __init__(self, nb_l, nb_c, empty_cell=' ', invader='#', missile='^', pos_canon=None):
        self.nb_l = nb_l
        self.nb_c = nb_c

        self.empty_cell = empty_cell
        self.invader = invader
        self.missile = missile

        self.grille = [ [ empty_cell for _ in range(nb_c) ] for _ in range(nb_l) ]
        # Ou algorithmiquement :
        #self.grille = []
        #for i in range(nb_l):
        #    ligne = []
        #    self.grille.append(ligne)
        #    for j in range(nb_c):
        #        ligne.append(empty_cell)

        # Add invaders
        self.grille[0] = [invader for _ in range(self.nb_c)]

        # Add canon
        if pos_canon is None:
            pos_canon = int(self.nb_c /2) # center
        self.canon = Canon(pos_canon)
        self.grille[-1][pos_canon] = self.canon

        # Add score
        self.score = 0

    def __repr__(self) -> str:

        # 1st line
        # ''.join(list) is a shortcut to concatenate all characters in a list
        screen = '┌' + ''.join( ['─' for _ in range(self.nb_c)] ) + '┐\n'

        # iterate on lines
        for i in self.grille:

            # start line with a '|'
            screen += '|'

            # print each cell
            for j in i:
                screen += j.__str__() # transform j in type 'str' if j were a complex type
            
            # end line with a '|' and go to next line
            screen += '|\n'

        # last line
        screen += '└' + ''.join( ['─' for _ in range(self.nb_c)]) + '┘\n'

        # score
        screen += 'Score : ' + str(self.score) + '\n'

        return screen
    
    def tirer(self):

        for x in range(self.nb_l-2, -1, -1):

            # missile goes up
            if self.grille[x][self.canon.pos] == self.invader:
                self.score += 1
            self.grille[x][self.canon.pos] = self.missile
            # clean last position
            if x < self.nb_l-2:
                self.grille[x+1][self.canon.pos] = self.empty_cell

            print(self)
            time.sleep(0.5)

        # missile disappears
        self.grille[0][self.canon.pos] = self.empty_cell
        print(self)
    
    def tirer_avec_animation(self):
        self.grille[-2][self.canon.pos] = self.missile

    def move_canon(self, mvt):
        # Check if still moving in the grid
        if self.canon.pos + mvt >= 0 and self.canon.pos + mvt < self.nb_c:
            # clean last position
            self.grille[-1][self.canon.pos] = self.empty_cell
    
            # move
            self.canon.pos = self.canon.pos + mvt
            self.grille[-1][self.canon.pos] = self.canon

    def move_missiles(self):
        # last line : cleanup missiles from last run
        self.grille[0] = [ self.empty_cell if cell == self.missile else cell for cell in self.grille[0] ]

        # before last line : move missile
        for i in range(self.nb_l-1):
            for j in range(self.nb_c):
                if self.grille[i+1][j] == self.missile:
                    self.score += 1 if self.grille[i-1][j] == self.invader else 0
                    self.grille[i][j] = self.missile
                    self.grille[i+1][j] = self.empty_cell

    def move_invaders(self, invaders_speed):

        # move existing invaders
        for l in range(self.nb_l-1, -1, -1): # iterate on lines (reverse to avoid recursion)
            newl = l + invaders_speed
            for c in range(self.nb_c): # iterate on columns to inspect cells
                if self.grille[l][c] == self.invader: # only care about invaders
                    if newl >= self.nb_l -1: # overflow - an invader reached the floor
                        print('Game over ! Your score : ', self.score)
                        sys.exit(0)
                    else: # move the cell
                        previous_content = self.grille[newl][c]
                        self.grille[newl][c] = self.invader if previous_content == self.empty_cell else previous_content
                        self.grille[l][c] = self.empty_cell

        # add new invaders to fill the first lines
        for l in range(invaders_speed):
            self.grille[l] = [self.invader if previous_content == self.empty_cell else previous_content for _ in range(self.nb_c)]
                       

class Invader:
    def __init__(self, c='#'):
        self.c = c 
    
    def __str__(self) -> str:
        # On appelle la méthode __str__ de l'objet représentant l'envahisseur
        # pour permettre d'utiliser un type plus complexe qu'un simple caractère.
        # Ici, retourner simplement self.c aurait suffit
        return self.c.__str__()

class Canon:
    def __init__(self, pos):
        self.pos = pos
    
    def __repr__(self) -> str:
        return '_'

class GameEngine:
    def __init__(self, space:Space, invaders_speed=1, invaders_timer=1):
        self.space = space

        # Move invaders
        self.invaders_speed = invaders_speed
        self.invaders_timer = invaders_timer # a dedicated timer to slow the game (invaders move only every invaders_timer)
        self.timer = 0

    def play(self):
        print(self.space)
        while True:
            self._onkeypress(keyboard.read_key(suppress=True))
            time.sleep(0.1)
    
    def _onkeypress(self, key):
        if key == 'left' or key == 'q' or key == 'h':
            self.space.move_canon(-1)
            self._inc_timer()
        elif key == 'right' or key == 'd' or key == 'l':
            self.space.move_canon(+1)
            self._inc_timer()
        elif key == 'return' or key == 'space':
            self.space.tirer_avec_animation()
            self._inc_timer()
    
    def _inc_timer(self):
        self.timer += 1
        self.space.move_missiles()
        if (self.timer % self.invaders_timer == 0): # only move invaders every `invaders_timer`
            self.space.move_invaders(self.invaders_speed)
        print('\n',self.space) # add line break to partially fix keyboard bug printing key output on 1st line
    

if __name__ == '__main__':

    #space = Space(4, 10)
    #print(space.grille)
    #i = Invader()
    #print(i)
    #print(space)
    #space.tirer()       

    GameEngine(
        Space(20,10, missile='|', invader=Invader('"')),
        invaders_speed=2,
        invaders_timer=8
        ).play()
```
:::

