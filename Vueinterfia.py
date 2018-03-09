#Vue interfia

from tkinter import *
from (parametres interfia) import *

fenetre=Tk()
fenetre.title("interfia S") #interfia A = adaptative #S pr statique

#rapport de 5/9 pour hauteur/largeur (pr avoir icônes carrées)
reference=Canvas(fenetre, width=350*echelle, height=630*echelle, bg="grey")
dessin=Canvas(fenetre, width=350*echelle, height=630*echelle, bg="white")
#ces dimensions remplissent convenablement un écran 1280x768
#on espere pouvoir faire un xINT pour remplir de plus grands écrans (x2 CREMI?)


#une colonne et une ligne sont définies par la moitié du plus petit format d'icône
#6 lignes sur 6 colonnes = 1 grosse icone (1)=70x70 pixels
reference.grid(row=6, rowspan=54, column=6, columnspan=30)
dessin.grid(row=6, rowspan=54, column=42, columnspan=30)

#adaptation d'image : prend tout le bouton? serait top
Test=Button(fenetre,text="test")
Test.grid(row=0,column=6,rowspan=6,columnspan=12)
#le bouton s'adapte au texte/à l'image, soucis à régler pour bien définir la grille

fenetre.mainloop()



