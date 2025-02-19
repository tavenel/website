---
title: Figures colorées
date: 2023 / 2024
correction: false
---

# Figures géométriques

## Classe Rectangle

- Écrire une classe `Rectangle` permettant de construire un rectangle dotée d'attributs `longueur` et `largeur`.
- Créer une méthode `perimetre()` permettant de calculer le périmètre du rectangle et une méthode `surface()` permettant de calculer la surface du rectangle
- Créer 2 instances de `Rectangle` et calculer leurs `perimetre()` et `surface()`.

## Héritage : classe Carre

- Créer une classe `Carre` héritant de `Rectangle` et permettant de créer un carré.
- Créer une instance de `Carre` et calculer son `perimetre()` et `surface()`.

## Classe Cercle

- Créer une classe `Cercle` pour construire un cercle ayant un `rayon`.
- Ajouter des méthodes `perimetre()` et `surface()`. Utiliser `math.pi` (`import math`).
  + On rappelle que le périmètre d'un cercle se calcule par la formule : $2\Pi.r$
  + On rappelle que la surface d'un cercle se calcule par la formule : $\Pi.r^2$
- Que remarque-t-on quand aux méthodes de ces différentes classes ?
  + Quel type d'architecture permet de gérer proprement cette similarité ?
  + Implémenter cette architecture

# Couleurs

## RGB

- Créer une classe `CouleurRGB` permettant de stocker une couleur au format Rouge, Vert, Bleu. Cette classe possède donc 3 attributs (entiers) : `rouge`, `vert`, `bleu`.
- Ajouter une méthode `couleur_rgb()` affichant la couleur RGB sous forme d'un triplet : `(rouge,vert,bleu)`. Par exemple : `(10,20,100)`.
- Ajouter une méthode `couleur_hexa()` permettant de retourner la couleur au format hexadécimal correspondant : on utilisera le code `f"#{r:02x}{g:02x}{b:02x}"` pour convertir 3 variables `r`, `g` et `b`.

## Hexadécimal

- Créer une classe `CouleurHexa` permettant de stocker une couleur au format hexadécimal. Cette classe possède un attribut unique (chaîne de caractères de type : `#aabbcc`) : `hexa`.
- Ajouter une méthode `couleur_hexa()` permettant de retourner la couleur au format hexadécimal.
- Ajouter une méthode `couleur_rgb()` permettant de retourner la couleur RGB correspondante. On utilisera le code : `(int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16))` pour convertir une chaîne de caractères hexadécimale `hx` (de type `#aabbcc`) en triple `R,G,B` correspondant.

# Délégation : figure avec couleur

En utilisant 2 fois un pattern de délégation pour les figures géométriques et pour les couleurs, créer une classe : `FigureColoree` représentant une figure géométrique ayant une couleur.

Les instances de cette classe doivent posséder les méthodes suivantes : `perimetre()`, `surface()`, `couleur_rgb()`, `couleur_hexa()`.

:::correction
# Correction

```python
import zope.interface
from zope.interface.verify import verifyObject, verifyClass

import math

###################################################
# Interfaces par contrat utilisant zope.interface #
###################################################

class FigureGeometrique(zope.interface.Interface):
    def perimetre():
        raise NotImplementedError("A spécialiser")
    def surface():
        raise NotImplementedError("A spécialiser")

@zope.interface.implementer(FigureGeometrique)
class Rectangle():
    def __init__(self, longueur, largeur):
        self.L = longueur
        self.l = largeur
        print(f'Nouvelle instance de rectangle : {self.L} et {self.l}')

    def perimetre(self):
        return 2*(self.l + self.L)

    def surface(self):
        return self.l * self.L

class Carre(Rectangle):
    def __init__(self, cote):
        super().__init__(cote, cote)

@zope.interface.implementer(FigureGeometrique)
class Cercle():
    def __init__(self, rayon):
        self.r = rayon
    
    def perimetre(self):
        return int( 2 * math.pi * self.r )
    
    def surface(self):
        return int( math.pi * (self.r ** 2) )

@zope.interface.implementer(FigureGeometrique)
class Ovale():
    def __init__(self, a, b):
        self.a = a
        self.b = b

verifyClass(FigureGeometrique, Rectangle)
verifyClass(FigureGeometrique, Carre)
verifyClass(FigureGeometrique, Cercle)
#Ovale ne vérifie pas l'interface => ERREUR
#verifyClass(FigureGeometrique, Ovale)

r1 = Rectangle(1,2)
r2 = Rectangle(3,4)

print(r1.perimetre())
print(r1.surface())

print(r2.perimetre())
print(r2.surface())

c = Carre(3)
print( c.perimetre() )
print( c.surface() )

cc = Cercle(5)
print( cc.perimetre() )
print( cc.surface() )

print("###BOUCLE###")
for f in [r1, r2, c, cc]:
    verifyObject(FigureGeometrique, f)
    print( f.perimetre() )
    print( f.surface() )

o = Ovale(2, 3)
#verifyObject(FigureGeometrique, o)



#####################################################
# Interfaces informelles (Duck Typing) - seules les #
# classes respectent le même contrat                #
#####################################################
class CouleurRGB:
    def __init__(self, rouge, vert, bleu):
        self.r = rouge
        self.g = vert
        self.b = bleu
    
    def couleur_rgb(self):
        return ( self.r, self.g, self.b )
    
    def couleur_hexa(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

class CouleurHexa:
    def __init__(self, code_hexa):
        self.hx = code_hexa
    
    def couleur_rgb(self):
        return (int(self.hx[1:3],16),int(self.hx[3:5],16),int(self.hx[5:7],16))
    
    def couleur_hexa(self):
        return self.hx

rgb = CouleurRGB(10, 20, 100)
print( rgb.couleur_rgb() )
print( rgb.couleur_hexa() )
hexa = CouleurHexa('#0a1464')
print( hexa.couleur_rgb() )
print( hexa.couleur_hexa() )

for c in [rgb, hexa]:
    print( c.couleur_rgb() )
    print( c.couleur_hexa() )


#####################################################
# Pattern Délégation - FigureGeométrique et Couleur #
#####################################################
@zope.interface.implementer(FigureGeometrique)
class FigureColoree:
    def __init__(self, forme:FigureGeometrique, couleur): # couleur: CouleurRGB ou CouleurHexa
        self.forme = forme
        self.couleur = couleur
    
    def perimetre(self):
        return self.forme.perimetre()
    
    def surface(self):
        return self.forme.surface()

    def couleur_de_figure(self):
        return self.couleur.couleur_hexa()
    
carre = Carre(4)
coul = CouleurRGB(10,2,1)

fc = FigureColoree( carre, coul )
fc2 = FigureColoree( Carre(3), CouleurHexa('#11aa22') )
fc3 = FigureColoree( Cercle(5), CouleurHexa('#11aa22') )
fc4 = FigureColoree( Ovale(2, 3), CouleurHexa('#11aa22') ) # Ne respecte pas le contrat (Ovale)
print( fc.perimetre() )
# print( fc4.perimetre() ) ## CRASH !!

print("###### Boucle de figures colorées #####")
for fig in [fc, fc2, fc3]:
    print( fig.perimetre() )
    print( fig.surface() )
    print( fig.couleur_de_figure() )
```
:::

