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
reference.grid(row=6, rowspan=54, column=6, columnspan=30)
dessin.grid(row=6, rowspan=54, column=42, columnspan=30)

L=[] #on génère le quadrillage de cellules qu'on associe à une matrice( liste de listes )
C=[]
for y in range (0,hauteur,35):
    C.append([0])
    for x in range (0,largeur,35):
        L.append(0)
        L[x//35]=dessin.create_rectangle(x,y,x+35,y+35,fill="white")
        C[y//35].append(L[x//35])
        L[x//35]=reference.create_rectangle(x,y,x+35,y+35,fill="white")
        C[y//35].append(L[x//35])

peindre=Button(fenetre,text="Pot")
peindre.grid(row=0, column=6, rowspan=6, columnspan=6)

ligne=Button(fenetre, text="Ligne")
ligne.grid(row=0, column=12, rowspan=6, columnspan=6)

crayon=Button(fenetre, text="Crayon")
crayon.grid(row=0, column=18, rowspan=6, columnspan=6)

gomme=Button(fenetre, text="Gomme")
gomme.grid(row=0, column=24, rowspan=6, columnspan=6)

ctrlz=Button(fenetre, text="Ctrl+Z")
ctrlz.grid(row=0, column=30, rowspan=6, columnspan=6)

selec=Button(fenetre, text="Sélectionner")
selec.grid(row=0, column=36, rowspan=6, columnspan=6)

ctrlc=Button(fenetre, text="Ctrl+C")
ctrlc.grid(row=0, column=42, rowspan=6, columnspan=6)

ctrlv=Button(fenetre, text="Ctrl+V")
ctrlv.grid(row=0, column=48, rowspan=6, columnspan=6)

rotat=Button(fenetre, text="Rotation")
rotat.grid(row=0, column=54, rowspan=6, columnspan=6)

suppr=Button(fenetre, text="Supprimer")
suppr.grid(row=0, column=60, rowspan=6, columnspan=6)

rouge=Button(fenetre, text="Rouge")
rouge.grid(row=6, column=36, rowspan=2, columnspan=2)

vert=Button(fenetre, text="Vert")
vert.grid(row=6, column=38, rowspan=2, columnspan=2)

bleu=Button(fenetre, text="Bleu")
bleu.grid(row=6, column=40, rowspan=2, columnspan=2)

jaune=Button(fenetre, text="Jaune")
jaune.grid(row=8, column=36, rowspan=2, columnspan=2)

blanc=Button(fenetre, text="Blanc")
blanc.grid(row=8, column=38, rowspan=2, columnspan=2)

noir=Button(fenetre, text="Noir")
noir.grid(row=8, column=40, rowspan=2,columnspan=2)

fenetre.mainloop()




