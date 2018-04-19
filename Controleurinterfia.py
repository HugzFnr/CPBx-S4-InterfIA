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
# en -er (gommer,peindrer -désolé langue française-) qui appellent les fonctions de type boutonclic
# tout cela pour pouvoir assigner aux boutons des fonctions qui ne prennent pas de paramètre event,
# comme un clic de souris par exemple, en argument; et pour pouvoir actualiser le modèle

#les fonctions associés aux boutons sont écrits dans l'ordre de l'interface en lecture de gauche à droite

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
    global Use_peindre
    Use_peindre=Use_peindre+1
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
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",peindreclic)
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.peindre)
    global Clic_peindre
    Clic_peindre=Clic_peindre+1


def ligner1(event):
    Fenetre.ligneclic1(event)

def ligner2(event):
    global Use_ligne
    Use_ligne=Use_ligne+1
    if event.x<=largeur and event.y<=hauteur: #garde-fou de non sortie du canvas
        l2=event.y//cote_PIXEL
        c2=event.x//cote_PIXEL
        if Fenetre.l1<=l2: #ces sens sont utiles pour faire une double boucle for qui fonctionne dans tous les sens de parcours de l'écran
            sensy=1
            deltay=1 
        else :
            sensy=-1
            deltay=-1
        if Fenetre.c1<=c2:
            sensx=1
            deltax=1
        else:
            sensx=-1
            deltax=-1
        if Fenetre.l1==l2:
            for x in range (Fenetre.c1,c2+deltax,sensx):
                Fenetre.colorier_PIXEL(l2,x,Fenetre.couleur_active)
                Dessin.actualiser(l2,x,Fenetre.couleur_active)
        elif Fenetre.c1==c2:
            for y in range (Fenetre.l1,l2+deltay,sensy):
                Fenetre.colorier_PIXEL(y,c2,Fenetre.couleur_active)
                Dessin.actualiser(y,c2,Fenetre.couleur_active)
        else:
            diffx=abs(Fenetre.c1-c2)
            diffy=abs(Fenetre.l1-l2)
            for x in range (Fenetre.c1,c2+deltax,sensx):
                for y in range (Fenetre.l1,l2+deltay,sensy):
                    if ((y-Fenetre.l1)*sensy//(diffy/diffx))==((x-Fenetre.c1)*sensx//(diffx/diffx)): #permet de tracer ce qui ressemble le plus à une ligne diagonale dans n'importe quelle situation différente d'une ligne droite
                        Fenetre.colorier_PIXEL(y,x,Fenetre.couleur_active)
                        Dessin.actualiser(y,x,Fenetre.couleur_active)
                    

def ligne():
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",ligner1)
    Fenetre.dessin.bind("<B1-ButtonRelease>",ligner2)
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.ligne)
    global Clic_ligne
    Clic_ligne=Clic_ligne+1


def crayonner(event):
    global Use_crayon
    Use_crayon=Use_crayon+1
    if event.x<largeur and event.y<hauteur: 
        Fenetre.crayonclic(event)
        Dessin.actualiser(event.y//cote_PIXEL,event.x//cote_PIXEL,Fenetre.couleur_active)

def crayon():
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",crayonner)
    Fenetre.dessin.bind("<B1-Motion>",crayonner)
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.crayon)
    global Clic_crayon
    Clic_crayon=Clic_crayon+1


def gommer(event):
    global Use_gomme
    Use_gomme=Use_gomme+1
    if event.x<largeur and event.y<hauteur:
        Fenetre.gommeclic(event)
        Dessin.actualiser(event.y//cote_PIXEL,event.x//cote_PIXEL,"white")

def gomme():
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",gommer)
    Fenetre.dessin.bind("<B1-Motion>",gommer)
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.gomme)
    global Clic_gomme
    Clic_gomme=Clic_gomme+1


def selecer1(event):
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.selecclic1(event)

def selecer2(event):
    if event.x<=largeur and event.y<=hauteur:
        l2=event.y//cote_PIXEL
        c2=event.x//cote_PIXEL
        Dessin.x1selec=Fenetre.c1
        Dessin.y1selec=Fenetre.l1
        Dessin.x2selec=c2
        Dessin.y2selec=l2
        if Dessin.y1selec<=Dessin.y2selec:
            sensy=1
            deltay=1 #ces delta assurent la correspondance avec le rectangle de sélection visuelle (fichier Vue)
        else :
            sensy=-1
            deltay=-1
        if Dessin.x1selec<=Dessin.x2selec:
            sensx=1
            deltax=1
        else:
            sensx=-1
            deltax=-1
        for x in range (Fenetre.c1,c2,sensx):
            for y in range (Fenetre.l1,l2,sensy):
                Dessin.selectionC[y][x]=Dessin.couleur_PIXEL(y,x)
    Fenetre.selecclic2(event)
                
def selec():
    Fenetre.dessin.bind("<Button-1>",selecer1)
    Fenetre.dessin.bind("<B1-ButtonRelease>",selecer2)
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.selec)
    global Clic_selec
    Clic_selec=Clic_selec+1

def getclic(event):
    l=event.y//cote_PIXEL
    c=event.x//cote_PIXEL
    Dessin.prntcouleur_PIXEL(l,c)

def printPIXEL(): #Getclic, printPIXEL et prntcouleur_PIXEL sont 3 fonctions temporaires pour vérifier la correspondance entre canvas et modèle
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.dessin.bind("<Button-1>",getclic)
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.rotat)

def suppr():
    if Dessin.y1selec<=Dessin.y2selec:
        sensy=1
        deltay=1
    else :
        sensy=-1
        deltay=-1
    if Dessin.x1selec<=Dessin.x2selec:
        sensx=1
        deltax=1
    else:
        sensx=-1
        deltax=-1
    for y in range (Dessin.y1selec,Dessin.y2selec+deltay,sensy):
        for x in range (Dessin.x1selec,Dessin.x2selec+deltax,sensx):
            Fenetre.colorier_PIXEL(y,x,'white')
            Dessin.actualiser(y,x,'white')
    Fenetre.resetselec()
    Dessin.resetselec()
    global Clic_suppr
    Clic_suppr=Clic_suppr+1

##Fenetre.dessin.unbind("<B1-Motion>") #pour enlever un binding
#print(event.widget) le widget sur lequel se passe l'event

Fenetre=Vue()
Fenetre.genicones()
Fenetre.generation() #on génère tout l'interface

Fenetre.crayon.configure(command=crayon) #on assigne les commandes aux boutons ici
Fenetre.gomme.configure(command=gomme)  #pour pouvoir utiliser des fonctions issu du fichier contrôleur                     
Fenetre.peindre.configure(command=peindre)
Fenetre.ligne.configure(command=ligne)
Fenetre.selec.configure(command=selec)
Fenetre.suppr.configure(command=suppr)
Fenetre.rotat.configure(command=printPIXEL) #temporaire, pour tester la correspondance canvas/modèle

Reference=Modele()
Reference_moins_un=Modele() #ce modèle est utilisé par la fonction annuler
Dessin=Modele()


Fenetre.creer_raccourci(Fenetre.crayon,2)

Fenetre.loop()














