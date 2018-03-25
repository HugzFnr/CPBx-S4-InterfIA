#Contrôleur interfia
from tkinter import *

from Vueinterfia import *
from Modeleinterfia import *
from Parametresinterfia import *

#Données qu'on recupère sous forme de logs
Clic_peindre=0 #le nombre de clics pour chaque bouton
Clic_ligne=0
Clic_crayon=0
Clic_gomme=0
Clic_annuler=0
Clic_selec=0
Clic_copier=0
Clic_coller=0
Clic_rotat=0
Clic_suppr=0

Use_peindre=0 #le nombre d'utilisations des fonctions qui modifient le clic
Use_ligne=0
Use_crayon=0
Use_gomme=0



def dessiner(event):
    Fenetre.crayonclic(event)
    #print(event.widget) le widget sur lequel se passe l'event
    Dessin.actualiser(event.y//hauteur,event.x//largeur,Fenetre.couleur_active)

def crayon():
    Fenetre.dessin.bind("<Button-1>",dessiner)
    Fenetre.dessin.bind("<B1-Motion>",dessiner)
    Fenetre.bouton_actif(Fenetre.crayon)
    global Clic_crayon
    Clic_crayon=Clic_crayon+1

    
Fenetre=Vue()
Fenetre.genicones()
Fenetre.generation()

Fenetre.crayon.configure(command=crayon)

Reference=Modele(Fenetre.reference)
Dessin=Modele(Fenetre.dessin)

Fenetre.creer_raccourci(Fenetre.crayon,2)

Fenetre.loop()














