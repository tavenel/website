---
title: Exercices Tk
correction: false
---

## Fenêtre simple

Créez une fenêtre simple avec un titre et un bouton "Quitter" qui ferme la fenêtre lorsqu'il est cliqué.

On utilisera un `Button` avec une commande `quit` de l'objet `Tk()`.

:::correction
```python
from tkinter import *

# Créez la fenêtre
fenetre = Tk()
fenetre.title("Bouton quitter")

# Créez le bouton "Quitter"
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()

# Affichez la fenêtre
fenetre.mainloop()
```
:::

## Champ de texte

Créez une fenêtre avec deux champs de texte et un bouton "Afficher". Lorsque le bouton est cliqué, affichez le contenu des deux champs de texte dans une boîte de dialogue.

On utilisera :

- Des objets `Entry`
- La fonction `tkinter.messagebox.showinfo()` pour afficher une popup

:::correction
```python
import tkinter.messagebox

# Créez la fenêtre
fenetre = Tk()
fenetre.title("Champ de texte")

# Créez les champs de texte
texte1 = Entry(fenetre)
texte2 = Entry(fenetre)
texte1.pack()
texte2.pack()

# Créez le bouton "Afficher"
def afficher():
  tkinter.messagebox.showinfo("Afficher", "Texte 1 : " + texte1.get() + "\nTexte 2 : " + texte2.get())
bouton_afficher = Button(fenetre, text="Afficher", command=afficher)
bouton_afficher.pack()

# Affichez la fenêtre
fenetre.mainloop()
```
:::


## Liste déroulante

Créez une fenêtre avec une liste déroulante qui contient plusieurs options. Lorsque l'option sélectionnée est changée, affichez le choix dans une étiquette.

On utilisera :

- Un objet `OptionMenu()` pour la liste déroulante utilisant une `StringVar` : `choix` pour stocker le choix.
- Un objet `Label()` pour afficher le choix
- Un binding d'événement entre le choix et l'affichage : `choix.trace('w', changement)` où `changement` est une fonction faisant le lien entre le choix et le label :

```python
def changement(*args):
  label.configure(text="Vous avez choisi : " + choix.get())
```

:::correction
```python
# Créez la fenêtre
fenetre = Tk()
fenetre.title("Liste déroulante")

# Créez la liste déroulante
choix = StringVar(fenetre)
choix.set("Option 1") # Valeur par défaut
liste_deroulante = OptionMenu(fenetre, choix, "Option 1", "Option 2", "Option 3")
liste_deroulante.pack()

# Créez l'étiquette qui affichera le choix
label = Label(fenetre, text="Vous avez choisi : ")
label.pack()

# Mettez à jour l'étiquette lorsque le choix est changé
def changement(*args):
  label.configure(text="Vous avez choisi : " + choix.get())
choix.trace("w", changement)

# Affichez la fenêtre
fenetre.mainloop()
```
:::

## Dessin

Créez une fenêtre avec un canevas sur lequel vous pouvez dessiner en utilisant la souris. Ajoutez des boutons pour changer la couleur et l'épaisseur du trait. Lorsque vous maintenez le bouton gauche de la souris enfoncé et que vous déplacez la souris sur le canevas, des traits seront dessinés.

On utilisera :

- Une fonction `change_color()` pour changer la couleur : `self.color = tk.colorchooser.askcolor()[1]`
- Une fonction `change_thickness()` pour changer l'épaisseur du trait : `self.thickness = tk.simpledialog.askinteger("Épaisseur", "Choisissez une épaisseur (1-10):", minvalue=1, maxvalue=10)`
- Un binding click gauche <-> dessin utilisant une fonction `draw()` : `self.canvas.bind("<B1-Motion>", self.draw)`

La fonction `draw()` dessine en réalité des cercles à l'écran suivant la position de la souris :

```python
def draw(self, event):
    # Dessiner un trait lorsque la souris est en mouvement
    x1, y1 = (event.x - self.thickness), (event.y - self.thickness)
    x2, y2 = (event.x + self.thickness), (event.y + self.thickness)
    self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
```

:::correction
```python
import tkinter as tk
from tkinter import colorchooser
from tkinter import simpledialog

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dessin")

        # Créer un canevas
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='white')
        self.canvas.pack()

        # Créer des boutons pour changer la couleur et l'épaisseur du trait
        self.color_button = tk.Button(self.root, text="Changer la couleur", command=self.change_color)
        self.color_button.pack()
        self.thickness_button = tk.Button(self.root, text="Changer l'épaisseur", command=self.change_thickness)
        self.thickness_button.pack()

        # Créer un bouton Quitter
        self.quit_button = tk.Button(self.root, text="Quitter", command=self.root.destroy)
        self.quit_button.pack()

        # État du dessin
        self.color = 'black'
        self.thickness = 1

        # Événement de dessin
        self.canvas.bind("<B1-Motion>", self.draw)

    def change_color(self):
        # Ouvrir une boîte de dialogue pour choisir une couleur
        self.color = tk.colorchooser.askcolor()[1]

    def change_thickness(self):
        # Ouvrir une boîte de dialogue pour choisir une épaisseur
        self.thickness = tk.simpledialog.askinteger("Épaisseur", "Choisissez une épaisseur (1-10):", minvalue=1, maxvalue=10)

    def draw(self, event):
        # Dessiner un trait lorsque la souris est en mouvement
        x1, y1 = (event.x - self.thickness), (event.y - self.thickness)
        x2, y2 = (event.x + self.thickness), (event.y + self.thickness)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

app = App()
app.root.mainloop()
```
:::

## Mouvements

On utilisera :

- Un `Canvas()`
- La fonction `canvas.create_rectangle()`
- Un bindind entre n'importe qu'elle touche et une fonction `on_key_press()` : `self.bind_all('<Key>', self.on_key_press)`

La fonction `on_key_press()` peut être la suivante (si `self.square` est le rectangle à déplacer) :

```python
    def on_key_press(self, e):
        if e.keysym == 'Up':
            self.move_item(self.square, 0, -5)
        elif e.keysym == 'Down':
            self.move_item(self.square, 0, 5)
        elif e.keysym == 'Left':
            self.move_item(self.square, -5, 0)
        elif e.keysym == 'Right':
            self.move_item(self.square, 5, 0)
```

Attention à garder en mémoire les coordonnées du rectangle !

:::correction
```python
class Game(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width=self.width,
                                height=self.height)
        self.canvas.pack()
        self.pack()

        self.square = self.canvas.create_rectangle(5, 5, 25, 25, fill='red')
        self.x = 10
        self.y = 10

        self.bind_all('<Key>', self.on_key_press)
        self.focus_set()

    def on_key_press(self, e):
        if e.keysym == 'Up':
            self.move_item(self.square, 0, -5)
        elif e.keysym == 'Down':
            self.move_item(self.square, 0, 5)
        elif e.keysym == 'Left':
            self.move_item(self.square, -5, 0)
        elif e.keysym == 'Right':
            self.move_item(self.square, 5, 0)
    
    def move_item(self, item, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x <= self.width and 0 <= new_y <= self.height:
            self.canvas.move(item, dx, dy)
            self.x = new_x
            self.y = new_y

root = tk.Tk()
root.title('Simple Game')
game = Game(root)
game.mainloop()
```
:::

