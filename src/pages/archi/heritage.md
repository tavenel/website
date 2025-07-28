---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
layout: '@layouts/SlideLayout.astro'
title: Héritage de classes, polymorphisme et délégation
tags:
- architecture
- poo
- heritage
---

## 📋 Prérequis

Le vocabulaire basique de programmation objet doit être maîtrisé : voir le [cours d'introduction aux langages objet][site-perso] si besoin.

---

## Héritage

- Une classe peut hériter d’une autre pour étendre ses fonctionnalités.
  + Permet d’ordonner des objets proches pour s’y retrouver.
- Inversement, cela permet de regrouper plusieurs classes ayant des fonctionnalités communes.
  + Permet de factoriser du code en repérant des comportements génériques utilisés dans plusieurs contextes et en les mettant dans un parent commun.

---

### Exemple

Les cercles, les carrés et les étoiles sont trois types de figures géométriques ayant toutes un centre, une couleur et une épaisseur utilisés pour le dessin. On peut les déplacer et calculer leur aire.

---

## Interface et classe abstraite

En programmation orientée objet, on parle d'interface et de classe abstraite pour différencier des classes particulières dans un modèle d'héritage.

---

### Interface

Classes ne possédant ni donnée (pas d'attribut de classe) ni implémentation de méthode : les méthodes sont présentes mais ne contiennent pas de code.

- Aucun intérêt pour le langage directement : ces classes ne servent à rien...
- ... sauf à décrire un contrat (le prototype de la classe) qui sera implémenté dans l'héritage (classe _concrète_).

En pratique : très utiles pour utiliser un contrat sans connaître l'abstraction.

---

### Classe abstraite

- Classe qui ne va pas pouvoir être instanciée directement.
- Contient des méthodes abstraites (sans implémentation), similaires à une interface...
- ...et des implémentations : attributs, méthodes concrètes, ...

---

- Intérêt : factoriser des parties de l'implémentation communes à **tout** l'héritage en décrivant clairement les parties à spécialiser.
- _Peu évolutif et cachent souvent des problèmes d'architecture, on leur préfère généralement la délégation (voir la suite du cours)_.

---

### Implémentation

- Les langages objet de programmation par contrat (Java) implémentent en général ces notions directement dans le langage : `interface MonInterface`, `abstract class MaClasseAbstraite`.
- Dans les langages suivant un concept de _Duck Typing_ (Python, EcmaScript : c'est au développeur de suivre ou non le contrat) ces types sont généralement implicites : `class MonInterface`, `class MaClasseAbstraite`.

---

### Exemple d'interface en Java

```java
interface FigureGeometrique {

    public double aire();

}

class Cercle implements FigureGeometrique {

    private final int rayon;

    public Cercle(int rayon) {
	    this.rayon = rayon;
	}

    @Override
	public double aire() {
        return Math.PI * this.rayon * this.rayon;
	}

}

class Carre implements FigureGeometrique {

    private final int cote;

    public Carre(int cote) {
	    this.cote = cote;
	}

    @Override
	public double aire() {
        return this.cote * this.cote;
	}

}

FigureGeometrique[] figures = new FigureGeometrique[]{ new Cercle(2), new Carre(3), new Cercle(5), new Carre(2) };

for (FigureGeometrique figure : figures) {
	// Utilisation de l'interface FigureGeometrique
	System.out.println(figure.aire());
}
```

---

### Exemple de classe abstraite en Python

```python
class FigureGeometrique:

    def __init__(self, centre, couleur="black"):
        self.couleur = couleur

    def couleur(self):
        ''' Méthode concrète (avec implémentation) '''
        return self.couleur

    def aire(self):
        ''' Méthode abstraite (sans implémentation) '''
        raise NotImplementedError("La classe fille doit implémenter cette fonction!")

class Cercle(FigureGeometrique):

    def __init__(self, rayon, couleur="black"):
        self.rayon = rayon
        super().__init__(couleur)

    def aire(self):
        return 3.1415 * self.rayon * self.rayon

class Carre(FigureGeometrique):

    def __init__(self, cote, couleur="black"):
        self.cote = cote
        super().__init__(couleur)

    def aire(self):
        return self.cote ** 2

figures = [Cercle(2, "red"), Carre(3, "green"), Cercle(5), Carre(2)]

for figure in figures:
    # Utilisation de la classe FigureGeometrique
    print(figure.couleur())
    print(figure.aire())
```

---

## Polymorphisme

Dans les exemples, on utilise les objets `figure` sans connaître réellement la classe utilisée `Cercle` ou `Carre`.

L'appel à la méthode `aire()` dépendra de la classe de l'objet (`Cercle` ou `Carre`) mais le contrat sera toujours respecté : seul le calcul de l'aire nous intéresse.

_Polymorphisme_ : utilisation uniforme d'objets différents en utilisant leur contrat commun.

---

### Exercice

Réécrire les exemples précédents sans utiliser d'héritage (avec un enchaînement de conditions `if`).

Cet exemple illustre l'intérêt de la factorisation par polymorphisme.

---

### Exercice

Le polymorphisme peut parfois être implicite, comme en Python si l'on sait que des classes sans lien d'héritage suivent quand même le même contrat.

Reprendre le dernier exemple : créer uniquement deux classes `Cercle` et `Carre` sans aucun lien d'héritage et utiliser du polymorphisme pour calculer l'aire des objets.

Quel est l'inconvénient de cette écriture ?

---

## Délégation

- Design pattern qui permet par composition d'objets la même factorisation que l'héritage (sans ses inconvénients).
- Principe : appeler un autre objet qui contient l'implémentation à exécuter

---

```python
class DelegateAffiche:

    def msg(self):
        print('msg in delegate')

class Delegator1:

    def __init__(self, afficheur):
        self.afficheur = afficheur

    def affiche(self):
        return self.afficheur.msg()

class Delegator2:
    pass

afficheur = DelegateAffiche()

# Version 1 : delegate dans la déclaration de classe
main_obj1 = Delegator1(afficheur)
main_obj1.affiche()
'msg in delegate'

# Version 2 : par référence de fonction sur l'instance
main_obj2 = Delegator2()
main_obj2.affiche = afficheur.msg # pas de () !!!
main_obj2.affiche()
'msg in delegate'
```

---

Certains langages (`Kotlin`) supportent nativement la délégation :

```kotlin
interface ClosedShape {
    fun area(): Int
}

class Rectangle(val width: Int, val height: Int) : ClosedShape {
    override fun area() = width * height
}

class Window(private val bounds: ClosedShape) : ClosedShape by bounds
```

---

La délégation est certainement le design pattern le plus utile apporté par les langages objets.

- Avantages 🌟 :
  + Très propre : aucun impact sur l'architecture globale.
  + Aucune dépendance inutile.
  + Factorisation évidente de comportements communs.
- Inconvénients :
  + verbeux si programmation par contrat : `Java`

=> À utiliser massivement !

---

