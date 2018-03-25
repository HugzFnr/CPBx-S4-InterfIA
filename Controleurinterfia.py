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

#les fonctions avec le nom du bouton (gomme,peindre,...) appellent les fonctions
# en -er (gommer,peindrer -RIP langue française-) qui appellent les fonctions de type boutonclic
# tout cela pour pouvoir assigner aux boutons des fonctions qui ne prennent pas de paramètre event,
# comme un clic de souris par exemple, en argument; et pour pouvoir actualiser le modèle

def crayonner(event):
    Fenetre.crayonclic(event)
    Dessin.actualiser(event.y//cote_PIXEL,event.x//cote_PIXEL,Fenetre.couleur_active)
    Dessin.couleur_PIXEL(event.y//cote_PIXEL,event.x//cote_PIXEL)

def crayon():
    Fenetre.dessin.bind("<Button-1>",crayonner)
    Fenetre.dessin.bind("<B1-Motion>",crayonner)
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.crayon)
    global Clic_crayon
    Clic_crayon=Clic_crayon+1

def gommer(event):
    Fenetre.gommeclic(event)
    Dessin.actualiser(event.y//cote_PIXEL,event.x//cote_PIXEL,"white")

def gomme():
    Fenetre.dessin.bind("<Button-1>",gommer)
    Fenetre.dessin.bind("<B1-Motion>",gommer)
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.gomme)
    global Clic_gomme
    Clic_gomme=Clic_gomme+1

def marque(ligne,colonne,A): #utile pour que la fonction peindre_recursif ne revienne pas sur des pixels déjà traités
    A[ligne][colonne]=1
            
def peindre_recursif(li,co,couleur,A):

    if (couleur==Dessin.couleur_PIXEL(li,co)) and (A[li][co]!=1):
        Fenetre.colorier_PIXEL(li,co,Fenetre.couleur_active)
        Dessin.actualiser(li,co,Fenetre.couleur_active)
        marque(li,co,A)
        
        l=li
        c=co
        bas=li+1
        haut=li-1
        droite=co+1
        gauche=co-1
        
        if l<17:
             #gestion de tous les cas bordures
            peindre_recursif(bas,c,couleur,A)
        if l>0:
            peindre_recursif(haut,c,couleur,A)
            
        if c<9:
            peindre_recursif(l,droite,couleur,A)
            
        if c>0:
            peindre_recursif(l,gauche,couleur,A)
            
        
def peindreclic(event):
    l=event.y//cote_PIXEL
    c=event.x//cote_PIXEL
    coul=Dessin.couleur_PIXEL(l,c)
    A=[]
    B=[]
    for y in range (0,hauteur//cote_PIXEL):
        A.append([])
        for x in range (0,largeur//cote_PIXEL):
            B.append(0)
            A[y].append(B[x])
    peindre_recursif(l,c,coul,A)

def peindre():
    Fenetre.dessin.bind("<Button-1>",peindreclic)
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.peindre)
    global Clic_peindre
    Clic_peindre=Clic_peindre+1
    
def getclic(event):
    l=event.y//cote_PIXEL
    c=event.x//cote_PIXEL
    Dessin.prntcouleur_PIXEL(l,c)

def printPIXEL(): #Getclic, printPIXEL et prntcouleur_PIXEL sont 3 fonctions temporaires pour vérifier la correspondance entre canvas et modèle
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.dessin.bind("<Button-1>",getclic)
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.rotat)
    

##Fenetre.dessin.unbind("<B1-Motion>") #pour enlever un binding
#print(event.widget) le widget sur lequel se passe l'event

   
Fenetre=Vue()
Fenetre.genicones()
Fenetre.generation() #on génère tout l'interface

Fenetre.crayon.configure(command=crayon) #on assigne les commandes aux boutons ici
Fenetre.gomme.configure(command=gomme)  #pour pouvoir utiliser des fonctions du contrôleur                     
Fenetre.peindre.configure(command=peindre)

Fenetre.rotat.configure(command=printPIXEL) #temporaire, pour tester la correspondance canvas/modèle

Reference=Modele()
Reference_moins_un=Modele() #ce modèle est utilisé par la fonction annuler
Dessin=Modele()


Fenetre.creer_raccourci(Fenetre.crayon,2)

Fenetre.loop()














