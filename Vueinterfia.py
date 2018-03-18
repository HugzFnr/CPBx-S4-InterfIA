#Vue interfia

from tkinter import *

from Parametresinterfia import *
from Controleurinterfia import *
from Modeleinterfia import *


fenetre=Tk()
fenetre.title("interfia S") #interfia A = adaptative #S pr statique

#rapport de 5/9 pour hauteur/largeur (pr avoir icônes carrées)
reference=Canvas(fenetre, width=largeur, height=hauteur, bg="grey")
dessin=Canvas(fenetre, width=largeur, height=hauteur, bg="white")
#ces dimensions remplissent convenablement un écran 1280x768 en echelle=1, 1.6 sur les petits CREMI

#une colonne et une ligne sont définies par la moitié du plus petit format d'icône
#6 lignes sur 6 colonnes = 1 grosse icone (1)=70x70 pixels
reference.grid(row=6, rowspan=54, column=0, columnspan=30)
dessin.grid(row=6, rowspan=54, column=36, columnspan=30)

L1=[] #on génère le quadrillage de cellules qu'on associe à une matrice( liste de listes )
C1=[]
L2=[]
C2=[]
for y in range (0,hauteur,cote_PIXEL):
    C1.append([0])
    C2.append([0])
    for x in range (0,largeur,cote_PIXEL):
        L1.append(0)
        L2.append(0)
        L1[x//cote_PIXEL]=reference.create_rectangle(x,y,x+cote_PIXEL,y+cote_PIXEL,fill="lightgrey")
        C1[y//cote_PIXEL].append(L1[x//cote_PIXEL]) #(C1[ligne])[colonne] correspond à un PIXEL du canvas de référence
        L2[x//cote_PIXEL]=dessin.create_rectangle(x,y,x+cote_PIXEL,y+cote_PIXEL,fill="white")
        C2[y//cote_PIXEL].append(L2[x//cote_PIXEL]) #(C2[ligne])[colonne] correspond à un PIXEL du canvas de dessin
        
if echelle == 1:
    icone = PhotoImage(file="PHicon1.gif") #Icône 64x64 à l'échelle 1 et 100x100 echelle 1.6
    palette = PhotoImage(file="PHcouleur1.gif") #21x32 à l'échelle 1 et 33x50 echelle 1.6

elif echelle == 1.6:
    icone = PhotoImage(file="PHicon1,6.gif")
    palette = PhotoImage(file="PHcouleur1,6.gif")

reference.itemconfigure(C1[0][0],fill="red") #ce test révèle que la colonne 0 n'existe pas, ça commence à 1, alors que la ligne 0 existe

#Menu principal
peindre=Button(fenetre, image=icone)
peindre.grid(row=0, column=0, rowspan=6, columnspan=6)

ligne=Button(fenetre, image=icone)
ligne.grid(row=0, column=6, rowspan=6, columnspan=6)

crayon=Button(fenetre, image=icone)
crayon.grid(row=0, column=12, rowspan=6, columnspan=6)

gomme=Button(fenetre, image=icone)
gomme.grid(row=0, column=18, rowspan=6, columnspan=6)

ctrlz=Button(fenetre, image=icone)
ctrlz.grid(row=0, column=24, rowspan=6, columnspan=6)

selec=Button(fenetre, image=icone)
selec.grid(row=0, column=30, rowspan=6, columnspan=6)

ctrlc=Button(fenetre, image=icone)
ctrlc.grid(row=0, column=36, rowspan=6, columnspan=6)

ctrlv=Button(fenetre, image=icone)
ctrlv.grid(row=0, column=42, rowspan=6, columnspan=6)

rotat=Button(fenetre, image=icone)
rotat.grid(row=0, column=48, rowspan=6, columnspan=6)

suppr=Button(fenetre, image=icone)
suppr.grid(row=0, column=54, rowspan=6, columnspan=6)

#Couleurs
rouge=Button(fenetre, image=palette)
rouge.grid(row=6, column=30, rowspan=3, columnspan=2)

vert=Button(fenetre, image=palette)
vert.grid(row=6, column=32, rowspan=3, columnspan=2)

bleu=Button(fenetre, image=palette)
bleu.grid(row=6, column=34, rowspan=3, columnspan=2)

jaune=Button(fenetre, image=palette)
jaune.grid(row=9, column=30, rowspan=3, columnspan=2)

blanc=Button(fenetre, image=palette)
blanc.grid(row=9, column=32, rowspan=3, columnspan=2)

noir=Button(fenetre, image=palette)
noir.grid(row=9, column=34, rowspan=3,columnspan=2)

fenetre.mainloop()




