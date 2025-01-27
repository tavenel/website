---
title: Exercices Tk
correction: false
---

## Fenêtre simple

Créez une fenêtre simple avec un titre et un bouton "Quitter" qui ferme la fenêtre lorsqu'il est cliqué.

On utilisera un `Button` avec une commande `quit` de l'objet `Tk()`.

## Champ de texte

Créez une fenêtre avec deux champs de texte et un bouton "Afficher". Lorsque le bouton est cliqué, affichez le contenu des deux champs de texte dans une boîte de dialogue.

On utilisera :

- Des objets `Entry`
- La fonction `tkinter.messagebox.showinfo()` pour afficher une popup

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

