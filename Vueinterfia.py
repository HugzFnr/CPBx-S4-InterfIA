#Vue interfia

from tkinter import *
from Parametresinterfia import *

class Vue():
    def __init__(self):
        self.fenetre=Tk()

        self.fenetre.title("Interfia")

        

    def loop(self):
        self.fenetre.mainloop()

    def genicones(self): #on stocke les icônes adéquates dans des variables utilisables en s'adaptant à l'une des deux échelles prévues définies dans le fichier de paramètres
        if echelle == 1:
            self.peindreIMG = PhotoImage(file="peindreIMG1.gif") #Icône 64x64 à l'échelle 1 et 100x100 echelle 1.6
            self.ligneIMG = PhotoImage(file="ligneIMG1.gif")
            self.crayonIMG = PhotoImage(file="crayonIMG1.gif")
            self.gommeIMG = PhotoImage(file="gommeIMG1.gif")
            self.ctrlzIMG = PhotoImage(file="ctrlzIMG1.gif")
            self.selecIMG = PhotoImage(file="selectionnerIMG1.gif")
            self.ctrlcIMG = PhotoImage(file="ctrlcIMG1.gif")
            self.ctrlvIMG = PhotoImage(file="ctrlvIMG1.gif")
            self.rotatIMG = PhotoImage(file="rotatIMG1.gif")
            self.supprIMG = PhotoImage(file="supprIMG1.gif")
            self.rougeIMG = PhotoImage(file="rougeIMG1.gif")  #21x32 à l'échelle 1 et 33x50 echelle 1.6
            self.vertIMG = PhotoImage(file="vertIMG1.gif")
            self.bleuIMG = PhotoImage(file="bleuIMG1.gif")
            self.jauneIMG = PhotoImage(file="jauneIMG1.gif")
            self.blancIMG = PhotoImage(file="blancIMG1.gif")
            self.noirIMG = PhotoImage(file="noirIMG1.gif")

        elif echelle == 1.6:
            self.peindreIMG = PhotoImage(file="peindreIMG1,6.gif")
            self.ligneIMG = PhotoImage(file="ligneIMG1,6.gif")
            self.crayonIMG = PhotoImage(file="crayonIMG1,6.gif")
            self.gommeIMG = PhotoImage(file="gommeIMG1,6.gif")
            self.ctrlzIMG = PhotoImage(file="ctrlzIMG1,6.gif")
            self.selecIMG = PhotoImage(file="selectionnerIMG1,6.gif")
            self.ctrlcIMG = PhotoImage(file="ctrlcIMG1,6.gif")
            self.ctrlvIMG = PhotoImage(file="ctrlvIMG1,6.gif")
            self.rotatIMG = PhotoImage(file="rotatIMG1,6.gif")
            self.supprIMG = PhotoImage(file="supprIMG1,6.gif")
            self.rougeIMG = PhotoImage(file="rougeIMG1,6.gif")
            self.vertIMG = PhotoImage(file="vertIMG1,6.gif")
            self.bleuIMG = PhotoImage(file="bleuIMG1,6.gif")
            self.jauneIMG = PhotoImage(file="jauneIMG1,6.gif")
            self.blancIMG = PhotoImage(file="blancIMG1,6.gif")
            self.noirIMG = PhotoImage(file="noirIMG1,6.gif")

        
    def generation(self):
        self.reference=Canvas(self.fenetre, width=largeur, height=hauteur, bg="grey")
        self.dessin=Canvas(self.fenetre, width=largeur, height=hauteur, bg="white")
        #ces dimensions remplissent convenablement un écran 1280x768 en echelle=1, 1.6 sur les petits CREMI

        #une colonne et une ligne sont définies par la moitié du plus petit format d'icône
        #6 lignes sur 6 colonnes = 1 grosse icone (1)=70x70 pixels
        self.reference.grid(row=6, rowspan=54, column=0, columnspan=30)
        self.dessin.grid(row=6, rowspan=54, column=36, columnspan=30)

        self.L1=[] #on génère le quadrillage de PIXELS (carré de 35*35 pixels en echelle=1)qu'on associe à une matrice ( liste de listes )
        self.C1=[]
        self.L2=[]
        self.C2=[]
        for y in range (0,hauteur,cote_PIXEL):
            self.C1.append([])
            self.C2.append([])
            for x in range (0,largeur,cote_PIXEL):
                self.L1.append(0)
                self.L2.append(0)
                self.L1[x//cote_PIXEL]=self.reference.create_rectangle(x,y,x+cote_PIXEL,y+cote_PIXEL,fill="white")
                self.C1[y//cote_PIXEL].append(self.L1[x//cote_PIXEL]) #(C1[ligne])[colonne] correspond à un PIXEL du canvas de référence
                self.L2[x//cote_PIXEL]=self.dessin.create_rectangle(x,y,x+cote_PIXEL,y+cote_PIXEL,fill="white")
                self.C2[y//cote_PIXEL].append(self.L2[x//cote_PIXEL]) #(C2[ligne])[colonne] correspond à un PIXEL du canvas de dessin
            
        #Boutons principaux
        self.peindre=Button(self.fenetre, image=self.peindreIMG)
        self.peindre.grid(row=0, column=0, rowspan=6, columnspan=6)

        self.ligne=Button(self.fenetre, image=self.ligneIMG)
        self.ligne.grid(row=0, column=6, rowspan=6, columnspan=6)

        self.crayon=Button(self.fenetre, image=self.crayonIMG)
        self.crayon.grid(row=0, column=12, rowspan=6, columnspan=6)

        self.gomme=Button(self.fenetre, image=self.gommeIMG)
        self.gomme.grid(row=0, column=18, rowspan=6, columnspan=6)

        self.ctrlz=Button(self.fenetre, image=self.ctrlzIMG)
        self.ctrlz.grid(row=0, column=24, rowspan=6, columnspan=6)

        self.selec=Button(self.fenetre, image=self.selecIMG)
        self.selec.grid(row=0, column=30, rowspan=6, columnspan=6)

        self.ctrlc=Button(self.fenetre, image=self.ctrlcIMG)
        self.ctrlc.grid(row=0, column=36, rowspan=6, columnspan=6)

        self.ctrlv=Button(self.fenetre, image=self.ctrlvIMG)
        self.ctrlv.grid(row=0, column=42, rowspan=6, columnspan=6)

        self.rotat=Button(self.fenetre, image=self.rotatIMG)
        self.rotat.grid(row=0, column=48, rowspan=6, columnspan=6)

        self.suppr=Button(self.fenetre, image=self.supprIMG)
        self.suppr.grid(row=0, column=54, rowspan=6, columnspan=6)

        #Boutons palette
        self.rouge=Button(self.fenetre, image=self.rougeIMG)
        self.rouge.grid(row=6, column=30, rowspan=3, columnspan=2)

        self.vert=Button(self.fenetre, image=self.vertIMG)
        self.vert.grid(row=6, column=32, rowspan=3, columnspan=2)

        self.bleu=Button(self.fenetre, image=self.bleuIMG)
        self.bleu.grid(row=6, column=34, rowspan=3, columnspan=2)

        self.jaune=Button(self.fenetre, image=self.jauneIMG)
        self.jaune.grid(row=9, column=30, rowspan=3, columnspan=2)

        self.blanc=Button(self.fenetre, image=self.blancIMG)
        self.blanc.grid(row=9, column=32, rowspan=3, columnspan=2)

        self.noir=Button(self.fenetre, image=self.noirIMG)
        self.noir.grid(row=9, column=34, rowspan=3,columnspan=2)

    def colorier(self,event): 
        if event.x<=largeur and event.y<=hauteur: #garde-fou de non sortie du canvas
            l=event.y//cote_PIXEL #retourne les cordonnées du PIXEL (ligne,colonne) surlequel la souris est dans la grille de dessin
            c=event.x//cote_PIXEL
            self.dessin.itemconfigure(self.C2[l][c],fill="yellow")

    def creer_raccourci(self,bouton,emplacement): #duplique un bouton dans un des 5 emplacements du milieu : emplacement=0 pour celui en-dessous de la palette, emplacement = 4 pour le dernier
        self.raccourci=Button(self.fenetre,image=bouton['image'])
        self.raccourci.grid(column=30, columnspan=6, rowspan=6, row=12+emplacement*6)

    







