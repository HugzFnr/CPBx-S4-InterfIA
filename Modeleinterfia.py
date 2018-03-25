#Modèle interfia

from tkinter import *
from Parametresinterfia import *

class Modele():
    def __init__(self):
        
        self.valeur={}
        self.valeur["red"]=0 #on associe une valeur numérique à chaque couleur de PIXEL à l'aide du dictionnaire "valeur"
        self.valeur["green"]=1
        self.valeur["blue"]=2
        self.valeur["yellow"]=3
        self.valeur["white"]=4
        self.valeur["black"]=5

        self.inv_valeur={}
        for cle,valeur in self.valeur.items(): #on crée le dictionnaire inverse
            self.inv_valeur[valeur]=cle
        
        self.M=[]
        self.R=[]
        
        for y in range (0,hauteur//cote_PIXEL): #pour pouvoir stocker l'état des deux grilles
            self.M.append([])                      #dans une matrice numérique
            for x in range (0,largeur//cote_PIXEL): 
                self.R.append(4)
                self.M[y].append(self.R[x])

    def actualiser(self,l,c,couleur):
            self.M[l][c]=self.valeur[couleur]
    
    def couleur_PIXEL(self,l,c):
        return self.inv_valeur[self.M[l][c]]

    def prntcouleur_PIXEL(self,l,c):
        print(self.inv_valeur[self.M[l][c]],"ligne=",l,"colonne=",c)
        
    


    


