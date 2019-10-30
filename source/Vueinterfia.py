#Vue interfia
from tkinter import *
import time

from Parametresinterfia import *

class Vue():
    def __init__(self):
        self.fenetre=Tk()
        self.fenetre.title("Interfia")

        self.progress=StringVar()
        
        self.raccourcis=[0,0,0,0,0,0,0,0,0]
        self.preraccourcis=[0,0,0,0,0,0,0,0,0]

        self.peindreracc=-1
        self.ligneracc=-1
        self.crayonracc=-1
        self.gommeracc=-1
        self.selecracc=-1
        self.collerracc=-1
        self.copierracc=-1
        self.supprracc=-1
        self.suivracc=-1     #marque où sont les fonctions sont en raccourcis pour pouvour mettre à jour leur état désactivé ou activé

        self.horloge()

    def horloge(self):
 
        self.fenetre.after(1000,self.tictac)
    
    def loop(self):
        self.fenetre.mainloop()

    def tictac(self):
        self.time=self.time+1
        self.temps.set("Temps restant:" + str((Timer/(1000)-self.time)//60)+ "min")
        self.horloge()
        
    def genicones(self):
        
        self.temps=StringVar()
        self.time=0
        #on stocke les icônes adéquates dans des variables utilisables en s'adaptant à l'une des deux échelles prévues définies dans le fichier de paramètres
        if echelle == 1:
            self.peindreIMG = PhotoImage(file="peindreIMG1.gif") #Icône 64x64 à l'échelle 1 et 100x100 echelle 1.6
            self.ligneIMG = PhotoImage(file="ligneIMG1.gif")
            self.crayonIMG = PhotoImage(file="crayonIMG1.gif")
            self.gommeIMG = PhotoImage(file="gommeIMG1.gif")
            self.ctrlzIMG = PhotoImage(file="ctrlzIMG1.gif")
            self.selecIMG = PhotoImage(file="selectionnerIMG1.gif")
            self.ctrlcIMG = PhotoImage(file="ctrlcIMG1.gif")
            self.ctrlvIMG = PhotoImage(file="ctrlvIMG1.gif")
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
        #ces dimensions remplissent convenablement un écran 1280x768 en echelle=1, alors qu'1.6 fonctionne bien sur du 20 pouces

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
                self.L1[x//cote_PIXEL]=self.reference.create_rectangle(x,y,x+cote_PIXEL,y+cote_PIXEL,fill="white",outline="grey")
                self.C1[y//cote_PIXEL].append(self.L1[x//cote_PIXEL]) #(C1[ligne])[colonne] correspond à un PIXEL du canvas de référence (gauche)
                self.L2[x//cote_PIXEL]=self.dessin.create_rectangle(x,y,x+cote_PIXEL,y+cote_PIXEL,fill="white",outline="grey")
                self.C2[y//cote_PIXEL].append(self.L2[x//cote_PIXEL]) #(C2[ligne])[colonne] correspond à un PIXEL du canvas de dessin (droite)

        self.selection=0    
        #Boutons principaux
        self.peindre=Button(self.fenetre, image=self.peindreIMG,borderwidth=3)
        self.peindre.grid(row=0, column=0, rowspan=6, columnspan=6)

        self.ligne=Button(self.fenetre, image=self.ligneIMG,borderwidth=3)
        self.ligne.grid(row=0, column=6, rowspan=6, columnspan=6)

        self.crayon=Button(self.fenetre, image=self.crayonIMG,borderwidth=3)
        self.crayon.grid(row=0, column=12, rowspan=6, columnspan=6)

        self.gomme=Button(self.fenetre, image=self.gommeIMG,borderwidth=3)
        self.gomme.grid(row=0, column=18, rowspan=6, columnspan=6)

        self.selec=Button(self.fenetre, image=self.selecIMG,borderwidth=3)
        self.selec.grid(row=0, column=24, rowspan=6, columnspan=6)

        self.copier=Button(self.fenetre, image=self.ctrlcIMG,state='disabled',borderwidth=3) #ces boutons sont désactivés et grisés par défaut, ils auront besoin d'une sélection ou d'un copier
        self.copier.grid(row=0, column=30, rowspan=6, columnspan=6)

        self.coller=Button(self.fenetre, image=self.ctrlvIMG,state='disabled',borderwidth=3)
        self.coller.grid(row=0, column=36, rowspan=6, columnspan=6)

        self.suppr=Button(self.fenetre, image=self.supprIMG,state='disabled',borderwidth=3)
        self.suppr.grid(row=0, column=42, rowspan=6, columnspan=6)

        self.suivant=Button(self.fenetre, image=self.ctrlzIMG,state='disabled',borderwidth=3)
        self.suivant.grid(row=0, column=48, rowspan=6, columnspan=6)


        self.score=Message(self.fenetre,aspect=500,bg='goldenrod',justify='center',relief='sunken')
        self.score.grid(row=0, column=54,rowspan=3,columnspan=9)

        self.timer=Message(self.fenetre,aspect=500,bg='goldenrod',justify='center',relief='sunken',textvariable=((self.temps)))
        self.timer.grid(row=3,column=54,rowspan=3,columnspan=9)        

        self.scoretot=Message(self.fenetre,aspect=150,bg='purple1',justify='center',relief='sunken')
        self.scoretot.grid(row=0,column=63,rowspan=6,columnspan=4)
        
        #Boutons palette
        self.couleur_active="red2" #la valeur par défaut est rouge
        self.rouge=Button(self.fenetre, image=self.rougeIMG,command=self.rouge,relief="sunken",borderwidth=3,background='magenta4')  #donc par défaut, le bouton est de relief appuyé (=sunken)par défaut
        self.rouge.grid(row=6, column=30, rowspan=3, columnspan=2)

        self.vert=Button(self.fenetre, image=self.vertIMG,command=self.vert,borderwidth=3)
        self.vert.grid(row=6, column=32, rowspan=3, columnspan=2)

        self.bleu=Button(self.fenetre, image=self.bleuIMG,command=self.bleu,borderwidth=3)
        self.bleu.grid(row=6, column=34, rowspan=3, columnspan=2)

        self.jaune=Button(self.fenetre, image=self.jauneIMG,command=self.jaune,borderwidth=3)
        self.jaune.grid(row=9, column=30, rowspan=3, columnspan=2)

        self.blanc=Button(self.fenetre, image=self.blancIMG,command=self.blanc,borderwidth=3)
        self.blanc.grid(row=9, column=32, rowspan=3, columnspan=2)

        self.noir=Button(self.fenetre, image=self.noirIMG,command=self.noir,borderwidth=3)
        self.noir.grid(row=9, column=34, rowspan=3,columnspan=2)

    def rouge(self): #les fonctions très simples pour chaque bouton de la palette, qui modifient la valeur de self.couleur_active utilisée pour dessiner
        self.couleur_active="red2"
        self.desactiver_palette()
        self.bouton_actif(self.rouge)
    def vert(self):
        self.couleur_active="lime green"
        self.desactiver_palette()
        self.bouton_actif(self.vert)
    def bleu(self):
        self.couleur_active="blue"
        self.desactiver_palette()
        self.bouton_actif(self.bleu)
    def jaune(self):
        self.couleur_active="yellow2"
        self.desactiver_palette()
        self.bouton_actif(self.jaune)
    def blanc(self):
        self.couleur_active="white"
        self.desactiver_palette()
        self.bouton_actif(self.blanc)
    def noir(self):
        self.couleur_active="black"
        self.desactiver_palette()
        self.bouton_actif(self.noir)

    def creer_raccourci(self,bouton,emplacement): #duplique un bouton dans un des 4 emplacements du milieu : emplacement=0 pour celui en-dessous de la palette, emplacement = 3 pour le dernier
        #ils sont stockés dans une liste et indexés par leur emplacement
        if emplacement==self.peindreracc:
            self.peindreracc=-1
        elif emplacement==self.ligneracc:
            self.ligneracc=-1
        elif emplacement==self.crayonracc:
            self.crayonracc=-1
        elif emplacement==self.gommeracc:
            self.gommeracc=-1
        elif emplacement==self.selecracc:
            self.selecracc=-1
        elif emplacement==self.copierracc:
            self.copierracc=-1
        elif emplacement==self.collerracc:
            self.collerracc=-1
        elif emplacement==self.supprracc:
            self.supprracc=-1
        elif emplacement==self.suivracc:
            self.suivracc=-1 #si un des Vue.boutonracc vaut -1, c'est que ce bouton n'a pas de raccourci,
    #c'est important pour ne pas faire d'appel incohérent (ex : changer la couleur d'un bouton non existant)
        if bouton['command']==self.peindre['command']:
            self.peindreracc=emplacement
        elif bouton['command']==self.ligne['command']:
            self.ligneracc=emplacement
        elif bouton['command']==self.crayon['command']:
            self.crayonracc=emplacement
        elif bouton['command']==self.gomme['command']:
            self.gommeracc=emplacement
        elif bouton['command']==self.selec['command']:
            self.selecracc=emplacement
        elif bouton['command']==self.copier['command']:
            self.copierracc=emplacement
        elif bouton['command']==self.coller['command']:
            self.collerracc=emplacement
        elif bouton['command']==self.suppr['command']:
            self.supprracc=emplacement
        elif bouton['command']==self.suivant['command']: #toutes ces lignes permettent d'identifier quelle est la fonction de chaque raccourci
            self.suivracc=emplacement #c'est uniquement utile pour mettre à jour l'état visuel (relief+bordure) du bouton et de son raccourci en même temps

        self.raccourcis[emplacement]=Button(self.fenetre,image=bouton['image'])
        self.raccourcis[emplacement].configure(command=bouton['command'],state=bouton['state'])
        self.raccourcis[emplacement].grid(column=30, columnspan=6, rowspan=6, row=12+emplacement*6)

    def update_raccourcis(self): #voir fonction  adaptation du modèle
        for p in range (4):
            if self.preraccourcis[p]!=0:
                self.creer_raccourci(self.preraccourcis[p],p)
            elif self.preraccourcis[p]==0:
                q=p
                while q<8 and self.preraccourcis[q]==0:
                    q=q+1
                if self.preraccourcis[q]!=0:
                    self.creer_raccourci(self.preraccourcis[q],p)
                    self.preraccourcis[q]=0
                elif self.raccourcis[p]!=0:
                    self.raccourcis[p].destroy()            
            
    def bouton_actif(self,bouton):
        bouton.configure(relief="sunken",background='blue')

    def bouton_inactif(self,bouton): 
        bouton.configure(relief="raised",background='grey99')

    def desactiver_boutons(self):
        self.bouton_inactif(self.peindre)
        self.bouton_inactif(self.ligne)
        self.bouton_inactif(self.crayon)
        self.bouton_inactif(self.gomme)
        self.bouton_inactif(self.selec)
        self.bouton_inactif(self.coller)
        for i in range (4):
            if self.raccourcis[i]!=0:
                self.bouton_inactif(self.raccourcis[i])
#ces trois fonctions permettent de visualiser quel bouton est actif en le mettant en relief et en enlevant le relief des autres

    def desactiver_palette(self):
        self.bouton_inactif(self.rouge)
        self.bouton_inactif(self.vert)
        self.bouton_inactif(self.bleu)
        self.bouton_inactif(self.jaune)
        self.bouton_inactif(self.blanc)
        self.bouton_inactif(self.noir)

    def colorier_PIXEL(self,l,c,couleur): #fonction de base souvent réutilisée pour colorier un pixel de la zone de dessin
        self.dessin.itemconfigure(self.C2[l][c],fill=couleur)

    def colorier_PIXEL_modele(self,l,c,couleur):
        self.reference.itemconfigure(self.C1[l][c],fill=couleur)

    def effacer(self):
        for y in range (hauteur//cote_PIXEL):
            for x in range (largeur//cote_PIXEL):
                self.colorier_PIXEL(y,x,'white')
    
    def ligneclic1(self,event):
        if event.x<largeur and event.y<hauteur:
            self.l1=event.y//cote_PIXEL 
            self.c1=event.x//cote_PIXEL

    def crayonclic(self,event): 
        l=event.y//cote_PIXEL 
        c=event.x//cote_PIXEL #retourne les cordonnées du PIXEL (l,c)=(ligne,colonne) surlequel la souris est
        self.colorier_PIXEL(l,c,self.couleur_active)

    def gommeclic(self,event):
        l=event.y//cote_PIXEL 
        c=event.x//cote_PIXEL
        self.colorier_PIXEL(l,c,"white")

    def selecclic1(self,event):
        if event.x<largeur and event.y<hauteur:
            self.l1=event.y//cote_PIXEL
            self.c1=event.x//cote_PIXEL
    def selecclic2(self,event):
        l=event.y//cote_PIXEL
        c=event.x//cote_PIXEL
        if event.x<largeur and event.y<hauteur:
            if self.c1<=c:
                deltax2=1
                deltax1=0
            else :
                deltax2=0
                deltax1=1
            if self.l1<=l:
                deltay2=1
                deltay1=0
            else:
                deltay1=1
                deltay2=0 #on compense pour que la sélection prenne une zone équivalente peu importe les 2 directions (haut vers bas, gauche vers droite,etc...)
            self.selection=self.dessin.create_rectangle((self.c1+deltax1)*cote_PIXEL,(self.l1+deltay1)*cote_PIXEL,(c+deltax2)*cote_PIXEL,(l+deltay2)*cote_PIXEL,width=3,outline='darkblue',dash=(20,20))
            self.copier.configure(state='normal')
            self.suppr.configure(state='normal')
            if self.copierracc>=0:
                self.raccourcis[self.copierracc].configure(state='normal')
            if self.supprracc>=0:
                self.raccourcis[self.supprracc].configure(state='normal')

                 
    def resetselec(self):
            self.dessin.delete(self.selection)
            self.copier.configure(state='disabled')
            self.suppr.configure(state='disabled')
            if self.copierracc>=0:
                self.raccourcis[self.copierracc].configure(state='disabled')
            if self.supprracc>=0:
                self.raccourcis[self.supprracc].configure(state='disabled')

    
        
        
        
    
        
