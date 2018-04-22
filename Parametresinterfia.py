#Paramètres interfia
echelle=1 #valeurs possibles: 1 ou 1.6
Adaptative=1 #1 pour l'interface adaptative, 0 pour la statique
Sequence =1 #1 pour les mod numérotés impairs, 0 pour les pairs
Timer=60*17*1000 #le temps en mili-secondes à la fin duquel la fenêtre se ferme et les logs s'écrivent
Démo=0 #n'importe quelle valeur pour le test normal
if Démo==1:
    Timer=60*5*1000
hauteur = int(630*echelle) #rapport largeur/hauteur de 5/9 pour pour avoir icônes carrées et de la place pour les boutons
largeur = int(350*echelle)
cote_PIXEL = int (35*echelle)
