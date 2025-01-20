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
