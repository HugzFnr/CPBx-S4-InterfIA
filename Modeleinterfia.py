#Modèle interfia

from tkinter import *

from Vueinterfia import *
from Controleurinterfia import *

etat={}
etat["red"]=0
etat["green"]=1
etat["blue"]=2
etat["yellow"]=3
etat["white"]=4
etat["black"]=5

M1=[]
M2=[]
R1=[]
R2=[]

for y in range (0,hauteur,cote_PIXEL):
    M1.append([])
    M2.append([])
    for x in range (0,largeur,cote_PIXEL):
        R1.append(4)
        R2.append(4)


