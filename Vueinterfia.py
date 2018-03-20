#Vue interfia

from tkinter import *

from Parametresinterfia import *

class Vue():
    def __init__(self):
        self.fenetre=Tk()

        self.fenetre.title("interfia S") #interfia A = adaptative #S pr statique

        #rapport de 5/9 pour hauteur/largeur (pr avoir icônes carrées)
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
                        
        if echelle == 1:
            peindreIMG = PhotoImage(file="peindreIMG1.gif") #Icône 64x64 à l'échelle 1 et 100x100 echelle 1.6
            ligneIMG = PhotoImage(file="ligneIMG1.gif")
            crayonIMG = PhotoImage(file="crayonIMG1.gif")
            gommeIMG = PhotoImage(file="gommeIMG1.gif")
            ctrlzIMG = PhotoImage(file="ctrlzIMG1.gif")
            selecIMG = PhotoImage(file="selectionnerIMG1.gif")
            ctrlcIMG = PhotoImage(file="ctrlcIMG1.gif")
            ctrlvIMG = PhotoImage(file="ctrlvIMG1.gif")
            rotatIMG = PhotoImage(file="rotatIMG1.gif")
            supprIMG = PhotoImage(file="supprIMG1.gif")
            
            icone = PhotoImage(file="PHicon1.gif")

            rougeIMG = PhotoImage(file="rougeIMG1.gif")  #21x32 à l'échelle 1 et 33x50 echelle 1.6
            vertIMG = PhotoImage(file="vertIMG1.gif")
            bleuIMG = PhotoImage(file="bleuIMG1.gif")
            jauneIMG = PhotoImage(file="jauneIMG1.gif")
            blancIMG = PhotoImage(file="blancIMG1.gif")
            noirIMG = PhotoImage(file="noirIMG1.gif")

        elif echelle == 1.6:
            peindreIMG = PhotoImage(file="peindreIMG1,6.gif")
            ligneIMG = PhotoImage(file="ligneIMG1,6.gif")
            crayonIMG = PhotoImage(file="crayonIMG1,6.gif")
            gommeIMG = PhotoImage(file="gommeIMG1,6.gif")
            ctrlzIMG = PhotoImage(file="ctrlzIMG1,6.gif")
            selecIMG = PhotoImage(file="selectionnerIMG1,6.gif")
            ctrlcIMG = PhotoImage(file="ctrlcIMG1,6.gif")
            ctrlvIMG = PhotoImage(file="ctrlvIMG1,6.gif")
            rotatIMG = PhotoImage(file="rotatIMG1,6.gif")
            supprIMG = PhotoImage(file="supprIMG1,6.gif")
            
            icone = PhotoImage(file="PHicon1,6.gif")

            rougeIMG = PhotoImage(file="rougeIMG1,6.gif")
            vertIMG = PhotoImage(file="vertIMG1,6.gif")
            bleuIMG = PhotoImage(file="bleuIMG1,6.gif")
            jauneIMG = PhotoImage(file="jauneIMG1,6.gif")
            blancIMG = PhotoImage(file="blancIMG1,6.gif")
            noirIMG = PhotoImage(file="noirIMG1,6.gif")
            
        #Boutons principaux
        self.peindre=Button(self.fenetre, image=peindreIMG)
        self.peindre.grid(row=0, column=0, rowspan=6, columnspan=6)

        self.ligne=Button(self.fenetre, image=ligneIMG)
        self.ligne.grid(row=0, column=6, rowspan=6, columnspan=6)

        self.crayon=Button(self.fenetre, image=crayonIMG)
        self.crayon.grid(row=0, column=12, rowspan=6, columnspan=6)

        self.gomme=Button(self.fenetre, image=gommeIMG)
        self.gomme.grid(row=0, column=18, rowspan=6, columnspan=6)

        self.ctrlz=Button(self.fenetre, image=ctrlzIMG)
        self.ctrlz.grid(row=0, column=24, rowspan=6, columnspan=6)

        self.selec=Button(self.fenetre, image=selecIMG)
        self.selec.grid(row=0, column=30, rowspan=6, columnspan=6)

        self.ctrlc=Button(self.fenetre, image=ctrlcIMG)
        self.ctrlc.grid(row=0, column=36, rowspan=6, columnspan=6)

        self.ctrlv=Button(self.fenetre, image=ctrlvIMG)
        self.ctrlv.grid(row=0, column=42, rowspan=6, columnspan=6)

        self.rotat=Button(self.fenetre, image=rotatIMG)
        self.rotat.grid(row=0, column=48, rowspan=6, columnspan=6)

        self.suppr=Button(self.fenetre, image=supprIMG)
        self.suppr.grid(row=0, column=54, rowspan=6, columnspan=6)

        #Boutons palette
        self.rouge=Button(self.fenetre, image=rougeIMG)
        self.rouge.grid(row=6, column=30, rowspan=3, columnspan=2)

        self.vert=Button(self.fenetre, image=vertIMG)
        self.vert.grid(row=6, column=32, rowspan=3, columnspan=2)

        self.bleu=Button(self.fenetre, image=bleuIMG)
        self.bleu.grid(row=6, column=34, rowspan=3, columnspan=2)

        self.jaune=Button(self.fenetre, image=jauneIMG)
        self.jaune.grid(row=9, column=30, rowspan=3, columnspan=2)

        self.blanc=Button(self.fenetre, image=blancIMG)
        self.blanc.grid(row=9, column=32, rowspan=3, columnspan=2)

        self.noir=Button(self.fenetre, image=noirIMG)
        self.noir.grid(row=9, column=34, rowspan=3,columnspan=2)

        self.loop()
        
    def colorier(self,l,c,couleur):
        self.dessin.itemconfigure(self.C2[l][c],fill=couleur)
##        actualiser(l,c,couleur)

    def loop(self):
        self.fenetre.mainloop()







