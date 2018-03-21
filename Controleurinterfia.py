#Contrôleur interfia
from tkinter import *

from Vueinterfia import *
from Modeleinterfia import *
from Parametresinterfia import *

def dessiner(event):
    Fenetre.colorier(event)
    Dessin.actualiser(event.y//hauteur,event.x//largeur,"yellow")

Fenetre=Vue()
Fenetre.genicones()
Fenetre.generation()

Reference=Modele(Fenetre.reference)
Dessin=Modele(Fenetre.dessin)

Fenetre.dessin.bind("<Button-1>",dessiner)
Fenetre.dessin.bind("<B1-Motion>",dessiner)

Fenetre.creer_raccourci(Fenetre.peindre,0) #test

Fenetre.loop()














