#Contrôleur interfia
from tkinter import *
import time
import copy


from Vueinterfia import *
from Modeleinterfia import *
from Parametresinterfia import *

#Données qu'on recupère sous forme de logs
Clic_peindre=0 #le nombre de clics pour chaque bouton
Clic_ligne=0
Clic_crayon=0
Clic_gomme=0
Clic_selec=0
Clic_copier=0
Clic_coller=0
Clic_suppr=0
Clic_suivant=0 #celui là est présent juste pour détecter si il y a eu peu avoir une faille

Use_peindre=0 #le nombre d'utilisations des fonctions qui modifient le clic
Use_ligne=0
Use_crayon=0
Use_gomme=0
Use_selec=0
Use_coller=0


Score=0 #1 point pour chaque dessin + le pourcentage de progression du dernier dessin
Hésitation=0
hésit=0

#les fonctions avec le nom du bouton (gomme,peindre,...) appellent les fonctions
# en -er (gommer,peindrer -désolé langue française-) qui appellent les fonctions de type boutonclic
# tout cela pour pouvoir assigner aux boutons des fonctions qui ne prennent pas de paramètre event,
# comme un clic de souris par exemple, en argument; et pour pouvoir actualiser le modèle
#enfin un peu près
#les fonctions associés aux boutons sont écrits dans l'ordre de l'interface en lecture de gauche à droite


def temps_ecoule():
    Fenetre.fenetre.after(Timer-2000,Data)               #on minute la session de test pour préciser les données
    Fenetre.fenetre.after(Timer,lafin)

def Data():
    if Adaptative==1:
        with open('logstesta.txt','w+') as donnees:
            donnees.write('données test : ' +'Interface : ' + ' adaptative' + '; '+ 'Score total : ' + str(Score)+','+ str(progresser())
                      +'; Hésitation : '+str(Hésitation)+'; Clic_peindre :' + str(Clic_peindre)+'; Use_peindre :' + str(Use_peindre)
                      +'; Clic_ligne :' + str(Clic_ligne)+'; Use_ligne :' + str(Use_ligne)+'; Clic_crayon :' + str(Clic_crayon)
                      +'; Use_crayon :' + str(Clic_crayon)+'; Clic_gomme :' + str(Clic_gomme)+'; Use_gomme :' + str(Use_gomme)
                      +'; Clic_selec :' + str(Clic_selec)+'; Use_selec :' + str(Use_selec)+'; Clic_copier :' + str(Clic_copier)
                      +'; Clic_coller :' + str(Clic_coller)+'; Clic_suppr :' + str(Clic_suppr)
                      +'; Use_coller :' + str(Use_coller)   +'; Clic_suivant :' + str(Clic_suivant))
    elif Adaptative==0:
        with open('logstestb.txt','w+') as donnees:
            donnees.write('données test : ' +'Interface : ' + ' statique' + '; '+ 'Score total : ' + str(Score)+','+ str(progresser())
                      +'; Hésitation : '+str(Hésitation)+'; Clic_peindre :' + str(Clic_peindre)+'; Use_peindre :' + str(Use_peindre)
                      +'; Clic_ligne :' + str(Clic_ligne)+'; Use_ligne :' + str(Use_ligne)+'; Clic_crayon :' + str(Clic_crayon)
                      +'; Use_crayon :' + str(Clic_crayon)+'; Clic_gomme :' + str(Clic_gomme)+'; Use_gomme :' + str(Use_gomme)
                      +'; Clic_selec :' + str(Clic_selec)+'; Use_selec :' + str(Use_selec)+'; Clic_copier :' + str(Clic_copier)
                      +'; Clic_coller :' + str(Clic_coller)+'; Clic_suppr :' + str(Clic_suppr)
                      +'; Use_coller :' + str(Use_coller)   +'; Clic_suivant :' + str(Clic_suivant))


def lafin():
  Fenetre.fenetre.destroy()

def hesiter():
    if hésit==1:
        global Hésitation
        Hésitation=Hésitation+1

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
    global hésit
    hésit=0
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
    progresser() #à chaque modification de pixels de l'utilisateur, on met à jour le score de progression affiché

def peindre():
    hesiter()
    global hésit
    hésit=1
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",peindreclic)
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.peindre)
    global Clic_peindre
    Clic_peindre=Clic_peindre+1
    adaptation(Fenetre.peindre)

def ligner1(event):
    Fenetre.ligneclic1(event)

def ligner2(event):
    global Use_ligne
    Use_ligne=Use_ligne+1
    global hésit    
    hésit=0
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
            if diffy>=diffx:
                for x in range (Fenetre.c1,c2+deltax,sensx):
                    for y in range (Fenetre.l1,l2+deltay,sensy):
                        if ((y-Fenetre.l1)*sensy//(diffy/diffx))==((x-Fenetre.c1)*sensx): #permet de tracer ce qui ressemble le plus à une ligne diagonale dans n'importe quelle situation différente d'une ligne droite
                            Fenetre.colorier_PIXEL(y,x,Fenetre.couleur_active)
                            Dessin.actualiser(y,x,Fenetre.couleur_active)
            elif diffx>diffy:
                for y in range (Fenetre.l1,l2+deltay,sensy):
                    for x in range (Fenetre.c1,c2+deltax,sensx):
                        if ((x-Fenetre.c1)*sensx//(diffx/diffy))==((y-Fenetre.l1)*sensy):
                            Fenetre.colorier_PIXEL(y,x,Fenetre.couleur_active)
                            Dessin.actualiser(y,x,Fenetre.couleur_active)
    progresser()
                    

def ligne():
    hesiter()
    global hésit
    hésit=1
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",ligner1)
    Fenetre.dessin.bind("<B1-ButtonRelease>",ligner2)
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.ligne)
    global Clic_ligne
    Clic_ligne=Clic_ligne+1
    adaptation(Fenetre.ligne)

def crayonner(event):
    global hésit
    hésit=0
    global Use_crayon
    Use_crayon=Use_crayon+1
    if event.x<largeur and event.y<hauteur: 
        Fenetre.crayonclic(event)
        Dessin.actualiser(event.y//cote_PIXEL,event.x//cote_PIXEL,Fenetre.couleur_active)
    progresser()
    
def crayon():
    hesiter()
    global hésit
    hésit=1
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",crayonner)
    Fenetre.dessin.bind("<B1-Motion>",crayonner)
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.crayon)
    global Clic_crayon
    Clic_crayon=Clic_crayon+1
    adaptation(Fenetre.crayon)

def gommer(event):
    global hésit
    hésit=0
    global Use_gomme
    Use_gomme=Use_gomme+1
    if event.x<largeur and event.y<hauteur:
        Fenetre.gommeclic(event)
        Dessin.actualiser(event.y//cote_PIXEL,event.x//cote_PIXEL,"white")
    progresser()

def gomme():
    hesiter()
    global hésit
    hésit=1
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",gommer)
    Fenetre.dessin.bind("<B1-Motion>",gommer)
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.gomme)
    global Clic_gomme
    Clic_gomme=Clic_gomme+1
    adaptation(Fenetre.gomme)


def selecer1(event):
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.selecclic1(event)

def selecer2(event):
    global hésit
    hésit=0
    global Use_selec
    Use_selec=Use_selec+1
    if event.x<=largeur and event.y<=hauteur:
        l2=event.y//cote_PIXEL
        c2=event.x//cote_PIXEL
        Dessin.x1selec=Fenetre.c1
        Dessin.y1selec=Fenetre.l1
        Dessin.x2selec=c2
        Dessin.y2selec=l2
        if Dessin.y1selec<=Dessin.y2selec:
            sensy=1 #les sens ont la même utilité que pour la fonction ligne
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
        for y in range (Fenetre.l1,l2+deltay,sensy):
            for x in range (Fenetre.c1,c2+deltax,sensx):
                Dessin.selectionC[y][x]=Dessin.couleur_PIXEL(y,x)
    Fenetre.selecclic2(event)
                
def selec():
    hesiter()
    global hésit
    hésit=1
    Fenetre.dessin.bind("<Button-1>",selecer1)
    Fenetre.dessin.bind("<B1-ButtonRelease>",selecer2)
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.selec)
    global Clic_selec
    Clic_selec=Clic_selec+1
    adaptation(Fenetre.selec)

def copier():
    hesiter()
    Fenetre.coller.configure(state='normal')   
    Dessin.copieC.clear()
    Dessin.copieL.clear()

    Dessin.copieC=copy.deepcopy(Dessin.selectionC) #cette méthode, importé en début de programme permet de cloner la matrice de sélection

    for k in range(len(Dessin.copieC)-1,-1,-1): #je peux ensuite enlever tous les -1 de la matrice de sélection pour la réduire à ce qui a vraiment été sélectionné
        long=len(Dessin.copieC[k])
        for i in range(len(Dessin.copieC[k])-1,-1,-1):
            if (Dessin.copieC[k][i])==(-1):
                del (Dessin.copieC[k][i])
        if (Dessin.copieC[k])==[]:
            del (Dessin.copieC[k])
    global Clic_copier
    Clic_copier=Clic_copier+1
    adaptation(Fenetre.copier)


def collerclic(event):
    global hésit
    hésit=0
    h=event.y//cote_PIXEL
    l=event.x//cote_PIXEL
    for y in range (h,h+len(Dessin.copieC)):
        for x in range (l,l+len(Dessin.copieC[0])):
            if ((x<largeur//cote_PIXEL) and (y<hauteur//cote_PIXEL) and (x>=0) and (y>=0)):
                    Fenetre.colorier_PIXEL(y,x,Dessin.copieC[y-h][x-l])
                    Dessin.actualiser(y,x,Dessin.copieC[y-h][x-l])
    progresser()
    global Use_coller
    Use_coller=Use_coller+1

def coller():
    hesiter()
    global hésit
    hésit=1
    Fenetre.resetselec()
    Dessin.resetselec()
    Fenetre.dessin.bind("<Button-1>",collerclic)
    Fenetre.dessin.unbind("<B1-ButtonRelease>")
    Fenetre.dessin.unbind("<B1-Motion>")
    Fenetre.desactiver_boutons()
    Fenetre.bouton_actif(Fenetre.coller)
    global Clic_coller
    Clic_coller=Clic_coller+1
    adaptation(Fenetre.coller)

def suppr():
    hesiter()
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
    progresser()
    global Clic_suppr
    Clic_suppr=Clic_suppr+1
    adaptation(Fenetre.suppr)

def progresser():
    prog=0
    for y in range (hauteur//cote_PIXEL):
        for x in range ((largeur//cote_PIXEL)):
            if Dessin.couleur_PIXEL(y,x)==Reference.couleur_PIXEL(y,x):
                prog=prog+(5/9)
    Fenetre.score.configure(text="Progression : " + str(int(prog)) + "%")
    if int(prog)==100:
        Fenetre.suivant.configure(state='normal')
        if Fenetre.suivracc>=0:
            Fenetre.raccourcis[Fenetre.suivracc].configure(state='normal')
    else:
        Fenetre.suivant.configure(state='disabled')
        if Fenetre.suivracc>=0:
            Fenetre.raccourcis[Fenetre.suivracc].configure(state='disabled')
    return(prog)

def suivanter():
    Fenetre.effacer()
    Dessin.effacer()
    progresser()
    global Score
    Score=Score+1
    Fenetre.scoretot.configure(text="Score:"+ str(Score))


def suivant():
   #cette fonction définit la séquence de modèles de référence : les mod impairs pour la statique, les mod pairs pour l'adaptative
    global Clic_suivant
    Clic_suivant=Clic_suivant+1
    adaptation(Fenetre.suivant)
    if Adaptative==1:
        if Score==0:
            mod4()
            suivanter()
        elif Score==1:
            mod6()
            suivanter()
        elif Score==2:
            mod8()
            suivanter()
        elif Score==3:
            mod10()
            suivanter()
        elif Score==4:
            mod12()
            suivanter()
        elif Score==5:
            mod14()
            suivanter()
        elif Score==6:
            mod16()
            suivanter()
        elif Score==7:
            mod18()
            suivanter()
        elif Score==8:
            mod20()
            suivanter()
        elif Score==9:
            mod22()
            suivanter()
        elif Score==10:
            mod24()
            suivanter()
        elif Score==11:
            mod26()
            suivanter()
        elif Score==12:
            mod28()
            suivanter()
        elif Score==13:
            mod30()
            suivanter()
        elif Score==14:
            fin()
            suivanter()
 
    elif Adaptative==0:
        if Score==0:
            mod3()
            suivanter()
        elif Score==1:
            mod5()
            suivanter()
        elif Score==2:
            mod7()
            suivanter()
        elif Score==3:
            mod9()
            suivanter()
        elif Score==4:
            mod11()
            suivanter()
        elif Score==5:
            mod13()
            suivanter()
        elif Score==6:
            mod15()
            suivanter()
        elif Score==7:
            mod17()
            suivanter()
        elif Score==8:
            mod19()
            suivanter()
        elif Score==9:
            mod21()
            suivanter()
        elif Score==10:
            mod23()
            suivanter()
        elif Score==11:
            mod25()
            suivanter()
        elif Score==12:
            mod27()
            suivanter()
        elif Score==13:
            mod29()
            suivanter()
        elif Score==14:
            fin()
            suivanter()

def Copier_dessin():
    for y in range (hauteur//cote_PIXEL):
        for x in range (largeur//cote_PIXEL):
            print(str(Dessin.valeur[Dessin.couleur_PIXEL(y,x)]+2)+ ",",end="")
#J'ai codé les modèles en faisant des appels à la fonction mod ci-dessous avec un copier-coller de ce que la console me donnait grâce à la fonction Copier_dessin après copie des dessins avec le jeu

Fenetre=Vue()
Fenetre.genicones()
Fenetre.generation() #on génère tout l'interface

boutons={} #on crée un dictionnaire pour pouvoir associer les boutons à leur variable Clic_bouton, pour pouvoir les classer et proposer les raccourcis en adéquation
def adaptation(bouton):
    if Adaptative==1:
        Classement=[Clic_peindre,Clic_ligne,Clic_crayon,Clic_gomme,Clic_selec,Clic_copier,Clic_coller,Clic_suppr,Clic_suivant]
        Classement.sort() #cette ligne classe les nb d'utilisations de Clic dans la liste Classement par ordre croissant
        boutons[Fenetre.peindre]=Clic_peindre
        boutons[Fenetre.ligne]=Clic_ligne
        boutons[Fenetre.crayon]=Clic_crayon
        boutons[Fenetre.gomme]=Clic_gomme
        boutons[Fenetre.selec]=Clic_selec
        boutons[Fenetre.copier]=Clic_copier
        boutons[Fenetre.coller]=Clic_coller
        boutons[Fenetre.suppr]=Clic_suppr
        boutons[Fenetre.suivant]=Clic_suivant
 
        k=8
        while (boutons[bouton]<Classement[k]) and (k>4):
            k=k-1

        Fenetre.preraccourcis=Fenetre.raccourcis
        save=[0,0,0,0,0,0,0,0,0]
        i=0
        while(i<9) and (Fenetre.raccourcis[i]!=0):
            save[i]=Fenetre.raccourcis[i]['command']
            i=i+1
        boutonsave=[0,0,0,0,0,0,0,0,0]
        for p in range (len(save)):
            if (save[p])==(Fenetre.peindre['command']):
                boutonsave[p]=Fenetre.peindre
            elif (save[p]==Fenetre.ligne['command']):
                boutonsave[p]=Fenetre.ligne
            elif (save[p]==Fenetre.crayon['command']):
                boutonsave[p]=Fenetre.crayon
            elif (save[p]==Fenetre.gomme['command']):
                boutonsave[p]=Fenetre.gomme
            elif (save[p]==Fenetre.selec['command']):
                boutonsave[p]=Fenetre.selec
            elif (save[p]==Fenetre.copier['command']):
                boutonsave[p]=Fenetre.copier
            elif (save[p]==Fenetre.coller['command']):
                boutonsave[p]=Fenetre.coller
            elif (save[p]==Fenetre.suppr['command']):
                boutonsave[p]=Fenetre.suppr
            elif (save[p]==Fenetre.suivant['command']):
                boutonsave[p]=Fenetre.suivant

        if (k>=5) and (boutonsave[8-k]!=bouton): #grâce à la liste triée je peux voir si le nb de clics de la fonction du bouton cliqué est dans le top 4 (et donc devient un raccourci)
            for r in range(len(Fenetre.preraccourcis)):
                if (Fenetre.preraccourcis[r]!=0) and((Fenetre.preraccourcis[r]['command'])==(bouton['command'])): 
                    Fenetre.preraccourcis[r]=0 #on élimine dans la liste des raccourcis les boutons semblables à celui qui vient d'être cliqué pour ne pas avoir de doublons

            for u in range (8,(8-k),-1):
                if (Fenetre.preraccourcis[u-1]!=bouton):
                    Fenetre.preraccourcis[u]=Fenetre.preraccourcis[u-1]

            Fenetre.creer_raccourci(bouton,8-k)
            Fenetre.update_raccourcis()

def data():
    print("peindre",Clic_peindre,"ligne",Clic_ligne,"crayon",Clic_crayon,"gomme",Clic_gomme,"selec",Clic_selec,"copier",Clic_copier,"coller",Clic_coller,"suppr",Clic_suppr,"suivant",Clic_suivant)
        
Fenetre.peindre.configure(command=peindre)
Fenetre.ligne.configure(command=ligne)
Fenetre.crayon.configure(command=crayon) #on assigne les commandes aux boutons ici pour pouvoir utiliser des fonctions issues du fichier contrôleur     
Fenetre.gomme.configure(command=gomme)                  
Fenetre.selec.configure(command=selec)
Fenetre.copier.configure(command=copier)
Fenetre.coller.configure(command=coller)
Fenetre.suppr.configure(command=suppr)
Fenetre.suivant.configure(command=suivant)

Reference=Modele()
Dessin=Modele() #on génère les deux modèles : celui correspondant à la référence (parfois appelé modèle -de dessin- également) et le modèle du dessin, mis à jour par l'utilisateur et son crayon virtuel

def PIX(l,c,codecouleur):
    coul=Dessin.inv_valeur[codecouleur]
    Fenetre.colorier_PIXEL_modele(l,c,coul)
    Reference.actualiser(l,c,coul)

def mod(p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40,p41,p42,p43,p44,p45,p46,p47,p48,p49,p50
        ,p51,p52,p53,p54,p55,p56,p57,p58,p59,p60,p61,p62,p63,p64,p65,p66,p67,p68,p69,p70,p71,p72,p73,p74,p75,p76,p77,p78,p79,p80,p81,p82,p83,p84,p85,p86,p87,p88,p891,p892,p90,p91,p92,p93,p94,p95,p96,p97,p98,p99,p100,
        p101,p102,p103,p104,p105,p106,p107,p108,p109,p110,p111,p112,p113,p114,p115,p116,p117,p118,p119,p120,p121,p122,p123,p124,p125,p126,p127,p128,p129,p130,p131,p132,p133,p134,p135,p136,p137,p138,p139,p140,
        p141,p142,p143,p144,p145,p146,p147,p148,p149,p150,p151,p152,p153,p154,p155,p156,p157,p158,p159,p160,p161,p162,p163,p164,p165,p166,p167,p168,p169,p170,p171,p172,p173,p174,p175,p176,p177,p178,p179):
    PIX(0,0,p1 ) #p1 représente le pixel en haut à gauche de l'écran, p1 est celui à sa droite, p11 est sur la colonne 0 ligne 1, etc.... p0 est inutile mais je m'en suis rendu compte trop tard, l'enlever aurait demandé à refaire les premiers modèles
    PIX(0,1,p2 ) #ça aurait pu prendre beaucoup moins de lignes en format des lignes d'appels de fonction mais ça aurait été encore plus pénible à remplir
    PIX(0,2,p3 )
    PIX(0,3,p4 )
    PIX(0,4,p5 )
    PIX(0,5,p6)
    PIX(0,6,p7 )
    PIX(0,7,p8 )
    PIX(0,8,p9)
    PIX(0,9,p10)
    PIX(1,0,p11 )
    PIX(1,1,p12 )
    PIX(1,2,p13 )
    PIX(1,3,p14 )
    PIX(1,4,p15 )
    PIX(1,5,p16 )
    PIX(1,6,p17 )
    PIX(1,7,p18 )
    PIX(1,8,p19 )
    PIX(1,9,p20 )    
    PIX(2,0,p21 )
    PIX(2,1,p22 )
    PIX(2,2,p23 )
    PIX(2,3,p24 )
    PIX(2,4,p25)
    PIX(2,5,p26 )
    PIX(2,6,p27 )
    PIX(2,7,p28 )
    PIX(2,8,p29 )
    PIX(2,9,p30 )
    PIX(3,0,p31 )
    PIX(3,1,p32 )
    PIX(3,2,p33 )
    PIX(3,3,p34 )
    PIX(3,4,p35 )
    PIX(3,5,p36 )
    PIX(3,6,p37 )
    PIX(3,7,p38 )
    PIX(3,8,p39 )
    PIX(3,9,p40 )    
    PIX(4,0,p41 )
    PIX(4,1,p42 )
    PIX(4,2,p43 )
    PIX(4,3,p44 )
    PIX(4,4,p45 )
    PIX(4,5,p46)
    PIX(4,6,p47)
    PIX(4,7,p48 )
    PIX(4,8,p49) 
    PIX(4,9,p50)
    PIX(5,0,p51 )
    PIX(5,1,p52 )
    PIX(5,2,p53 )
    PIX(5,3,p54 )
    PIX(5,4,p55 )
    PIX(5,5,p56 )
    PIX(5,6,p57 )
    PIX(5,7,p58 )
    PIX(5,8,p59 )
    PIX(5,9,p60 )    
    PIX(6,0,p61 )
    PIX(6,1,p62 )
    PIX(6,2,p63 )
    PIX(6,3,p64 )
    PIX(6,4,p65 )
    PIX(6,5,p66 )
    PIX(6,6,p67 )
    PIX(6,7,p68 )
    PIX(6,8,p69)
    PIX(6,9,p70 )
    PIX(7,0,p71 )
    PIX(7,1,p72 )
    PIX(7,2,p73 )
    PIX(7,3,p74 )
    PIX(7,4,p75 )
    PIX(7,5,p76 )
    PIX(7,6,p77 )
    PIX(7,7,p78 )
    PIX(7,8,p79 )
    PIX(7,9,p80)
    PIX(8,0,p81 )
    PIX(8,1,p82)
    PIX(8,2,p83)
    PIX(8,3,p84)
    PIX(8,4,p85)
    PIX(8,5,p86)
    PIX(8,6,p87)
    PIX(8,7,p88)
    PIX(8,8,p891)
    PIX(8,9,p892)
    PIX(9,0,p90)
    PIX(9,1,p91)
    PIX(9,2,p92)
    PIX(9,3,p93)
    PIX(9,4,p94)
    PIX(9,5,p95)
    PIX(9,6,p96)
    PIX(9,7,p97)
    PIX(9,8,p98)
    PIX(9,9,p99)
    PIX(10,0,p100)    
    PIX(10,1,p101)
    PIX(10,2,p102)
    PIX(10,3,p103)
    PIX(10,4,p104 )
    PIX(10,5,p105)
    PIX(10,6,p106 )
    PIX(10,7,p107)
    PIX(10,8,p108)
    PIX(10,9,p109)
    PIX(11,0,p110)
    PIX(11,1,p111)
    PIX(11,2,p112)
    PIX(11,3,p113)
    PIX(11,4,p114)
    PIX(11,5,p115)
    PIX(11,6,p116)
    PIX(11,7,p117)
    PIX(11,8,p118)
    PIX(11,9,p119)
    PIX(12,0,p120)    
    PIX(12,1,p121)
    PIX(12,2,p122)
    PIX(12,3,p123)
    PIX(12,4,p124)
    PIX(12,5,p125)
    PIX(12,6,p126)
    PIX(12,7,p127)
    PIX(12,8,p128)
    PIX(12,9,p129)
    PIX(13,0,p130)
    PIX(13,1,p131)
    PIX(13,2,p132)
    PIX(13,3,p133)
    PIX(13,4,p134)
    PIX(13,5,p135)
    PIX(13,6,p136)
    PIX(13,7,p137)
    PIX(13,8,p138)
    PIX(13,9,p139)
    PIX(14,0,p140)    
    PIX(14,1,p141)
    PIX(14,2,p142)
    PIX(14,3,p143)
    PIX(14,4,p144)
    PIX(14,5,p145)
    PIX(14,6,p146)
    PIX(14,7,p147)
    PIX(14,8,p148)
    PIX(14,9,p149)
    PIX(15,0,p150)
    PIX(15,1,p151)
    PIX(15,2,p152)
    PIX(15,3,p153)
    PIX(15,4,p154 )
    PIX(15,5,p155)
    PIX(15,6,p156)
    PIX(15,7,p157)
    PIX(15,8,p158)
    PIX(15,9,p159)
    PIX(16,0,p160)
    PIX(16,1,p161 )    
    PIX(16,2,p162)
    PIX(16,3,p163)
    PIX(16,4,p164 )
    PIX(16,5,p165)
    PIX(16,6,p166)
    PIX(16,7,p167)
    PIX(16,8,p168)
    PIX(16,9,p169)
    PIX(17,0,p170)
    PIX(17,1,p171)
    PIX(17,2,p172)
    PIX(17,3,p173)
    PIX(17,4,p174)
    PIX(17,5,p175)
    PIX(17,6,p176)
    PIX(17,7,p177)
    PIX(17,8,p178)
    PIX(17,9,p179)

#le code des 30 modèles, PIXEL par PIXEL avec le code couleur défini au début du modèle
def exemple():
    mod(99,3,4,4,3,4,4,4,4,4,4,4,3,3,4,4,4,4,4,4,4,4,3,3,4,4,4,4,4,4,4,3,4,4,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
        4,5,5,5,5,4,5,5,5,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,
        2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,4,5,2,2,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

def fin():
    mod(99,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
        6,6,6,6,6,6,6,6,6,6,6,5,5,6,6,6,6,6,6,6,6,5,6,6,5,6,5,6,6,5,6,5,5,6,6,6,5,5,6,5,6,5,6,6,5,6,5,6,5,5,6,5,
        6,6,5,6,5,6,6,5,6,6,6,6,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
        6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6)
def mod1():
    mod(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
    1,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,
    1,2,1,2,1,2,2,2,2,2,2,1,1,2,1,2,1,2,2,2,2,2,1,2,1,2,1,2,2,2,3,3,1,1,1,1,1,2,2,3,3,3,3,2,1,2,3,3,3,1,3,3,3,
    3,1,3,3,3,1,1,3,1,3,3,1,3,3,3,1,1,3,1,3,3,3,3,3,3,1,1,1,1,3,3,3,3,3,3,3,1,3,3,3,3,3,3,3,3,3,1,3,3,3,
    3,3,3,3,3,3,3,3,3,3)

def mod2():
    mod(3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,3,3,2,0,3,3,3,3,3,0,2,3,2,
        3,0,0,0,0,0,3,2,3,2,0,3,3,3,3,0,0,2,3,3,2,0,0,0,0,3,2,3,3,3,3,2,3,3,3,2,3,3,3,3,3,3,2,2,2,2,3,3,3,3,
        3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
        3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3)

def mod3():
    mod(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,2,0,2,2,
        0,2,0,2,2,0,2,2,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,0,0,0,3,3,0,3,3,3,0,3,3,3,0,3,3,3,3,0,3,3,3,
        3,3,0,3,3,3,0,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
        3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3)

def mod4():
    mod(2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,1,2,1,1,2,1,2,2,2,2,1,1,1,1,1,1,2,2,2,2,
        2,2,2,2,2,2,2,2,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,2,1,1,
        1,1,1,1,2,1,2,2,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,1,2,2,1,2,2,2,2,2,2,2,2,
        2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)

def mod5():
    mod(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,2,2,2,0,3,0,0,0,3,0,2,2,2,
        0,3,5,3,5,3,0,2,2,2,0,3,3,3,3,3,0,2,2,2,2,0,3,3,3,0,2,2,2,0,0,0,0,5,0,0,0,0,2,0,3,0,3,0,3,0,3,0,2,2,2,0,
        0,0,0,0,2,2,2,2,2,0,0,0,0,0,2,2,2,2,2,3,3,0,3,3,2,2,2,2,2,0,0,2,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
        2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)

def mod6():
    mod(99,3,2,2,2,2,3,2,2,2,2,2,3,2,2,2,3,2,2,2,3,2,2,3,2,2,3,2,2,3,2,2,2,2,5,5,3,5,5,2,2,3,3,5,0,0,5,0,0,5,3,2,5,0,4,
        0,0,0,0,0,5,3,5,0,0,0,0,0,0,0,5,2,5,0,0,0,0,0,0,0,5,2,3,5,0,0,0,0,0,5,3,3,2,3,5,0,0,0,5,3,2,2,3,2,3,5,0,5,3,
        2,3,3,2,2,3,2,5,2,3,2,2,2,2,3,2,2,3,2,2,3,2,2,2,3,2,2,3,2,2,3,2,2,3,2,2,2,3,2,2,2,3,3,2,2,2,2,3,2,2,2,2,2,2,
        2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,2)
    
def mod7():
    mod(99,1,1,1,1,1,1,1,1,1,1,1,1,5,5,5,5,5,1,1,1,1,5,5,4,5,5,5,5,1,1,1,5,3,3,3,3,3,5,1,1,1,3,0,0,0,0,0,3,1,1,1,2,3,
        3,3,3,3,2,1,1,1,2,4,4,4,4,4,2,1,1,2,2,2,2,3,2,2,2,2,1,2,2,2,3,2,3,2,2,2,1,1,1,3,3,3,3,3,1,1,1,1,1,2,2,3,2,2,1,
        1,1,1,1,2,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

def mod8():
    mod(99,3,2,2,2,2,2,2,2,3,3,2,1,1,1,1,1,1,1,2,3,1,1,5,5,5,5,5,1,1,2,1,5,5,0,4,4,5,5,1,1,5,4,0,0,4,0,0,4,5,1,5,4,0,
        4,4,4,0,4,5,1,5,0,5,5,5,5,5,0,5,1,5,5,4,5,4,5,4,5,5,1,1,5,4,4,4,4,4,5,1,1,1,1,5,5,5,5,5,1,1,2,2,1,1,1,1,1,1,1,
        2,3,3,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
        3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3)
    
def mod9():
    mod(99,5,0,2,2,3,2,2,2,0,5,0,5,0,2,2,3,2,0,5,0,2,0,5,0,2,2,0,5,0,2,2,2,0,5,0,0,5,0,2,2,2,3,2,0,5,5,0,2,3,2,3,2,2,
        0,5,5,0,2,2,3,2,2,0,5,0,0,5,0,2,2,0,0,5,0,1,1,0,5,0,0,5,5,0,1,3,2,1,0,5,5,5,5,0,1,2,3,1,0,5,5,0,0,5,0,1,1,0,5,
        0,0,2,2,0,5,0,0,5,0,2,2,3,2,2,0,5,5,0,2,2,3,2,3,2,0,5,5,0,2,3,2,2,2,0,5,0,0,5,0,2,2,2,0,5,0,2,2,0,5,0,2,0,5,0,
        2,2,3,2,0,5,0,5,0,2,2,3,2,2,2,0,5)

def mod10():
    mod(99,3,5,5,5,5,5,5,5,3,5,5,5,5,5,5,5,3,5,5,5,5,5,5,4,4,4,4,4,4,5,5,5,4,2,2,2,2,2,2,4,5,4,2,2,2,4,4,2,2,2,4,2,2,1,2,
          4,4,4,2,2,4,2,1,1,2,2,2,2,2,1,4,2,1,1,2,2,2,1,2,2,4,2,1,1,1,2,2,1,2,4,4,2,2,1,4,4,1,2,1,1,5,4,2,4,4,2,2,2,1,2,
          5,5,4,2,2,2,2,2,2,4,5,3,5,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,3,5,5,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,5,5,5,5,5,5,3,
          5,5,5,5,5,5,3,5,5,5,5,5,5,5,3)

def mod11():
    mod(99,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,
        5,5,5,5,3,5,5,5,5,5,5,5,5,3,5,3,5,5,5,5,5,5,5,5,3,5,5,5,5,5,5,3,3,5,3,5,3,3,5,5,3,0,0,3,0,3,0,0,3,5,3,0,0,3,
      0,3,0,0,3,5,5,3,0,3,0,3,0,3,5,5,5,5,3,3,3,3,3,5,5,5,5,2,2,2,2,2,2,2,5,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)

def mod12():
    mod(99,4,4,4,4,2,2,2,2,3,3,2,4,4,4,4,4,2,2,3,3,2,2,4,4,4,4,2,2,2,2,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,4,1,1,1,1,1,1,1,1,2,2,4,4,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,
        2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

def mod13():
    mod(99,4,2,4,2,4,2,4,2,4,2,2,0,2,0,2,2,0,2,0,4,4,2,0,0,0,0,0,0,2,2,2,0,0,0,3,3,0,0,0,4,4,2,0,0,3,3,0,0,2,2,2,0,0,0,0,0,0,0,0,
        4,4,2,0,0,0,0,0,0,2,2,2,0,2,0,1,1,0,2,0,4,4,2,2,2,1,1,2,1,1,2,2,2,2,2,1,1,1,1,1,4,4,2,2,2,1,1,1,1,2,2,1,2,2,2,1,1,2,2,2,4,
        1,1,1,2,1,1,2,2,2,2,1,1,1,2,1,1,2,2,2,4,1,1,1,2,1,1,2,2,2,2,4,1,1,1,1,1,2,2,2,4,2,2,1,1,1,1,2,2,2,2,4,2,4,1,1,1,2,4,2,4)

def mod14():
    mod(99,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,3,3,3,3,1,3,3,3,3,3,1,3,3,1,3,3,
        3,3,3,1,1,1,1,1,1,3,3,3,1,1,3,1,1,3,1,1,3,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,3,1,1,3,1,3,3,3,3,1,3,1,3,3,3,1,3,3,1,3,3,
        3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,3,3,3,3,3,3,1,3,3,3,1,3,3,3,3,3,1,3,1,3,1,3,3,3,3,3,3,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3)

def mod15():
    mod(99,4,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,0,0,0,0,4,4,0,0,0,0,0,0,3,3,3,3,3,0,0,0,0,3,4,3,3,3,3,3,0,
        0,3,3,3,4,3,3,3,3,3,0,3,3,3,3,4,3,3,3,4,0,3,3,3,3,4,3,3,4,3,0,3,3,3,3,4,3,3,4,3,0,0,3,3,4,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,
        0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,4,0,0,0,0,0)

def mod16():
    mod(99,1,1,4,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,5,4,4,4,1,1,1,1,1,5,5,4,4,4,5,1,1,1,4,4,4,4,4,4,5,5,1,
        1,4,4,4,4,4,4,4,4,1,1,4,5,5,4,4,4,4,4,1,1,4,5,5,4,4,5,5,4,1,1,1,4,4,4,4,5,5,1,1,1,1,1,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,4,1,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

def mod17():
    mod(99,4,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,0,5,5,5,5,5,5,5,5,0,3,0,5,5,4,5,5,5,5,5,0,5,5,5,5,5,5,5,5,5,5,5,5,
        5,5,5,0,5,5,0,5,4,5,4,5,0,3,0,5,0,5,5,5,5,5,0,3,0,5,3,0,5,5,5,5,5,0,3,0,3,0,0,5,5,5,5,0,3,3,3,0,5,5,5,5,0,0,3,3,3,0,5,5,5,
        0,0,3,3,3,3,0,0,5,5,0,0,3,3,3,3,0,0,5,5,5,0,0,3,3,0,0,5,5,5,5,5,0,0,0,0,5,5,4,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5)

def mod18():
    mod(99,4,2,2,2,2,2,2,2,2,2,2,2,4,2,2,2,4,2,2,4,2,2,2,2,2,2,2,2,2,2,4,2,2,2,2,2,4,2,2,2,2,2,4,2,2,2,2,2,2,2,2,3,2,2,2,3,2,2,2,3,
        2,3,3,2,3,3,3,2,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,5,3,3,3,3,5,5,5,5,1,0,5,5,5,5,0,1,5,5,1,0,0,0,5,0,5,1,5,3,
        5,1,5,0,0,0,1,1,5,3,3,5,1,1,1,1,1,5,3,3,3,3,5,5,5,5,5,3,3,2,2,3,3,3,3,3,3,3,3,4,2,3,3,2,2,2,3,3,2,2,2,2,2,2,4,4,2,2,2)

def mod19():
    mod(99,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,1,1,1,1,1,1,3,3,3,3,3,1,
        1,1,1,1,3,3,3,5,3,1,1,1,1,1,3,3,3,3,0,0,3,1,3,3,3,3,3,3,1,1,3,5,3,3,5,3,3,3,3,2,3,3,5,5,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,2,2,3,
        3,3,3,3,3,3,2,2,2,2,3,3,3,3,3,2,2,2,2,2,2,2,0,2,0,2,2,2,2,2,2,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2)

def mod20():
    mod(99,2,2,5,2,2,2,2,4,2,2,2,2,5,5,2,2,4,4,2,2,2,2,5,5,5,4,4,4,2,2,2,5,5,1,5,4,1,4,4,2,2,5,5,5,5,4,4,4,4,2,2,2,5,5,5,4,4,4,2,2,
        2,2,2,5,5,4,4,2,2,2,2,2,5,5,5,4,4,4,2,2,2,2,5,5,5,4,4,4,2,2,2,5,5,5,5,4,4,4,4,2,2,5,5,5,5,4,4,4,4,2,5,5,5,5,5,4,4,4,4,4,5,
        5,5,5,5,4,4,4,4,4,5,5,5,5,5,4,4,4,4,4,5,5,5,5,5,4,4,4,4,4,2,5,5,5,5,4,4,4,4,2,2,2,5,5,5,4,4,4,2,2,2,2,2,2,2,2,2,4,5,4)

def mod21():
    mod(99,2,2,2,2,2,2,2,2,4,4,2,2,2,2,2,2,2,2,4,4,2,2,2,2,2,2,2,2,2,2,2,2,5,5,2,2,5,5,2,2,1,5,3,3,5,5,3,3,5,1,1,5,3,3,5,5,3,3,5,
        1,1,5,3,3,5,5,3,3,5,1,1,5,3,3,5,5,3,3,5,1,1,5,3,3,5,5,3,3,5,1,5,3,3,3,3,3,3,3,3,5,5,3,4,5,3,3,4,5,3,5,5,3,5,5,3,3,5,5,3,
        5,5,3,3,3,3,3,3,3,3,5,5,3,3,3,5,5,3,3,3,5,5,3,3,5,3,3,5,3,3,5,1,5,3,3,3,3,3,3,5,1,1,1,5,5,5,5,5,5,1,1,1,1,1,1,1,1,1,1,1,1)

def mod22():
    mod(99,2,2,1,3,3,3,3,1,2,2,2,2,1,3,3,3,3,1,2,2,2,2,1,3,3,3,3,1,2,2,3,2,2,1,3,3,1,2,2,3,3,3,2,2,3,3,2,2,3,3,3,3,3,2,3,3,2,3,3,3,
        3,3,3,5,5,5,5,3,3,3,3,5,5,0,0,0,0,5,5,3,3,5,0,0,0,0,4,0,5,3,5,0,0,0,0,0,0,0,0,5,5,0,0,5,5,5,5,0,0,5,5,5,5,5,5,5,5,5,5,5,5,
        4,4,5,5,5,5,4,4,5,3,5,4,4,4,4,4,4,5,3,3,5,5,4,4,4,4,5,5,3,3,3,2,5,5,5,5,2,3,3,3,2,1,3,3,3,3,1,2,3,2,1,1,3,3,3,3,1,1,2)

def mod23():
    mod(99,3,3,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,5,5,5,2,2,2,2,2,2,5,1,4,4,5,2,2,2,2,2,5,1,1,4,5,2,2,5,2,2,5,1,1,1,5,2,
        5,4,2,2,5,1,1,1,5,2,5,1,2,2,5,1,1,1,5,2,5,1,2,2,5,1,1,1,5,5,5,1,2,2,5,1,1,1,1,1,1,1,2,2,5,1,1,1,1,5,5,5,2,2,5,1,1,1,1,5,
        2,2,2,2,5,1,1,1,1,5,2,2,2,2,5,1,1,1,1,5,2,2,5,5,5,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0,5,5,5,0,0,0,0,0,0,5,5,3,5,5,5,5,5,5,5,5,3)

def mod24():
    mod(99,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,4,5,1,1,1,1,1,1,1,1,5,5,1,5,5,5,5,5,5,1,5,5,1,5,2,2,2,2,5,1,5,5,1,5,2,2,2,2,5,1,5,
        5,1,5,5,5,5,5,5,1,5,5,1,1,1,1,1,1,1,1,5,5,1,1,1,1,5,5,5,1,5,5,1,1,5,5,5,0,5,1,5,5,1,1,5,0,5,5,5,1,5,5,1,1,5,5,5,1,1,1,5,5,1,
        1,1,1,1,1,1,1,5,5,1,0,0,1,1,1,1,1,5,5,0,0,0,0,1,1,1,1,5,5,0,0,0,0,1,1,1,1,5,5,1,0,0,1,1,1,1,1,5,4,5,5,5,5,5,5,5,5,4)

def mod25():
    mod(99,4,4,2,2,2,2,2,2,2,2,4,4,4,2,2,2,2,2,2,2,4,4,2,2,2,2,2,2,2,2,2,2,0,0,0,1,0,0,4,4,2,0,1,0,0,0,1,0,0,4,2,0,0,1,0,0,0,0,0,4,
        2,0,0,0,0,0,1,0,0,2,4,3,3,3,3,3,3,3,3,2,4,3,3,3,3,3,3,3,3,2,5,4,3,3,3,3,3,3,5,4,5,4,3,3,3,3,3,3,5,4,5,4,5,3,3,3,3,4,5,4,5,
        4,5,3,3,3,3,4,5,4,5,4,5,4,3,3,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,5,4,4,4,5,4,5,4,5,4,5,4)

def mod26():
    mod(99,4,4,3,3,3,3,3,3,4,4,4,3,3,3,3,3,3,3,3,4,3,3,5,5,5,5,5,5,3,3,5,5,5,4,5,5,4,5,5,5,3,3,5,5,5,5,5,5,3,3,3,3,3,3,3,3,3,3,3,
        3,3,3,0,3,3,3,3,0,3,3,3,3,3,0,0,0,0,3,3,3,2,3,3,3,3,3,3,3,3,2,3,2,3,3,3,3,3,3,2,3,3,3,2,2,2,2,2,2,3,3,3,3,2,5,5,5,5,2,3,3,
        3,3,2,5,2,2,5,2,3,3,3,3,2,5,5,5,5,2,3,3,3,3,2,2,2,2,2,2,3,3,5,5,2,2,2,2,2,2,5,5,5,4,5,5,4,4,5,5,4,5,4,5,5,5,4,4,5,5,5,4)

def mod27():
    mod(99,5,5,5,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0,5,5,0,5,5,5,5,5,5,0,5,5,0,5,4,2,2,4,5,0,5,5,0,5,2,4,4,2,5,0,5,5,0,5,5,5,5,5,5,
        0,5,5,0,1,0,1,0,1,0,0,5,5,0,0,1,0,1,0,1,0,5,5,0,0,1,0,1,1,1,0,5,5,0,1,0,0,1,0,1,0,5,5,0,0,0,0,0,0,0,0,5,5,0,0,0,4,4,0,0,
        0,5,5,0,0,4,0,0,4,0,0,5,5,0,0,4,0,0,4,0,0,5,5,0,0,0,4,4,0,0,0,5,5,0,0,0,0,0,0,0,0,5,5,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5)

def mod28():
    mod(99,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,1,1,1,3,3,3,3,3,1,1,1,1,1,1,5,3,5,3,1,1,1,1,1,3,3,3,3,3,1,1,1,1,1,1,3,3,3,3,
        1,1,1,1,1,1,4,4,4,1,1,1,1,1,1,3,3,3,3,3,1,3,2,3,1,3,0,0,0,3,3,5,3,5,3,3,0,0,0,3,1,3,3,3,3,3,0,0,0,3,1,0,3,3,3,0,0,0,0,0,1,2,
        2,2,2,0,0,0,0,0,1,2,2,2,2,1,3,1,3,1,1,3,2,3,2,2,3,1,3,1,1,2,2,2,2,2,3,1,3,1,2,2,2,2,2,2,0,1,0,1,1,1,1,1,1,1,1,1,1,1)

def mod29():
    mod(99,3,2,3,3,3,3,3,3,3,3,2,3,5,5,5,5,5,5,3,3,3,2,5,0,0,0,0,5,3,3,3,5,5,5,5,5,5,5,3,3,5,5,5,5,5,5,5,5,5,3,5,5,4,4,4,4,4,4,5,5,5,
        5,4,5,4,4,5,4,5,5,5,5,4,4,4,4,4,4,5,5,3,5,4,4,0,0,4,4,5,3,3,3,5,4,4,4,4,5,3,3,3,5,2,5,5,5,5,2,5,3,5,0,5,2,5,4,5,2,5,5,0,0,0,
        5,2,5,2,5,0,0,0,5,0,0,5,2,2,0,5,0,0,5,0,5,2,5,0,0,5,0,0,5,5,5,5,5,5,5,5,0,0,5,2,2,2,2,2,2,5,0,0,5,5,5,5,5,5,5,5,0)

def mod30():
    mod(99,3,1,1,3,2,2,3,0,0,3,3,3,5,5,5,5,5,0,3,3,0,5,5,5,4,3,5,5,5,1,5,5,5,5,4,3,5,5,5,5,5,4,4,4,3,3,3,3,3,5,5,5,3,3,3,3,3,3,5,5,2,
        5,5,3,3,3,3,5,5,2,5,5,3,3,3,3,3,3,5,5,5,5,3,3,5,5,3,3,5,5,1,5,5,5,5,5,5,5,5,0,1,1,5,5,3,3,5,5,0,0,1,3,3,0,3,3,1,3,3,0,3,3,0,
        3,3,3,3,1,3,3,3,0,0,3,2,2,3,1,1,3,3,0,0,3,2,2,3,1,1,3,0,0,3,3,2,2,3,3,1,1,0,0,3,2,2,2,2,3,1,1,0,3,3,2,2,2,2,3,3,1)

if Adaptative==1:
    mod2()
elif Adaptative==0:
    mod1()
#exemple() à activer pour la démo pré-test

temps_ecoule()
Fenetre.loop() #permet de faire tourner la fenêtre, doit être à la fin












