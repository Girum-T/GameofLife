from tkinter import *
from functools import partial


def affiche_liste(liste):    #Fonction pour afficher une liste comme un tableau 
    for e in liste:
        print(*e, sep = ' ' )


def afficher_lignes():  #Creation de la grille vide
    global Can          #Toujours la même page tkinter
    global root
    for i in range(n):
        for j in range(p):
            Can.create_rectangle(i*e,j*e,i*e+e,j*e+e,outline='black',fill='white')  #Creation des carrées pour les coordonnées des cellules


def afficher_tableau(tab):   #Affichage du tableau sous la forme de la grille sur tkinter avec les carrées 

    global evol, quitter, title   # Même page tkinter avec mêmes titre et boutton

    for i in range (len(tab[0])):
        for j in range(len(tab)):
            if tab[j][i]== 1:     #Si il y a une cellule vivante
                Can.create_rectangle(i*e,j*e,i*e+e,j*e+e,outline='black',fill='red')   #Crée un carrée rouge
            else:   #Sinon
                Can.create_rectangle(i*e,j*e,i*e+e,j*e+e,outline='black',fill='white')  #Crée un carrée blanc
                
        evol = Button(root, text='EVOLUTION', command= partial(evoluer, tab))     #Creation du boutton pour l'évolution de la grille
        quitter = Button(root, text='Quitter', command= root.destroy)             #Creation du boutton pour quitter la page tkinter

                
    
def nombre_voisins(i, j, tab):
    compteur = 0                                       #Verfifier la présence d'une cellule vivante:
              
    if i > 0 and tab[i-1][j] == 1:                     # - Case en haut   
        compteur+=1
                
    if i < len(tab)-1  and tab[i+1][j] == 1:           # - Case en bas
        compteur+=1
                
    if j > 0 and tab[i][j-1] == 1:                     # - Case à gauche
        compteur+=1
                
    if j < len(tab[0])-1 and tab[i][j+1] == 1:         # - Case à droite
        compteur+=1
                
    if i > 0 and j > 0 and tab[i-1][j-1] == 1:         # - Case en haut à gauche
        compteur+=1
                
    if i > 0 and j < len(tab[0])-1 and tab[i-1][j+1]== 1:        # - Case en haut à droite
        compteur+=1
                
    if i < len(tab)-1 and j > 0 and tab[i+1][j-1]== 1:        # - Case en bas à gauche
        compteur+=1
                
    if i < len(tab)-1 and j< len(tab[0])-1 and tab[i+1][j+1]==1:        # - Case en bas à gauche
        compteur+=1
                
    return compteur


def evoluer(tab):       #Fonction pour le boutton de l'evolution de la grille
    global tableau
    tableau= evolution(tableau)  #On modifie a chaque fois le tableau apres son évolution
    afficher_tableau(tableau)    #Affichage du tableau evolué
    

def evolution(tab):     #Fonction qui modifie ou evolue le tableau principale a chaque fois 

    l= [[0 for i in range(len(tab[0]))] for i in range(len(tab))]   #Creation de la liste finale
    
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            n = nombre_voisins( i, j, tab)
            
            if tab[i][j]== 1 and n==0 or n>3:   #Si la cellule est vivante et si elle a moins de 2 cellules ou plus que 3 cellules voisines vivantes
                l[i][j]=0   #Meurt par  isolement ou  par surpopulation
                
            elif tab[i][j]==0 and n==3: #Si cellules morte a 3 voisines
                l[i][j] = 1 #Nouvelle cellule nait à sa place
            
            else:
                l[i][j] =tab[i][j]


    return l




    

    
n = int(input("Nombres de lignes? "))
p = int(input('Nombres de colonnes? '))
e= 50   #Echelle fixe
tableau = [[0 for i in range(p)] for i in range(n)]  #Creation de tableau de base
affiche_liste(tableau)  #Creation de la grille du tableau
continuer = input("Voulez vous ajouter une cellule vivante Y/N ? ")
affiche_liste(tableau)

while continuer == 'Y':     
    print("Veuillez ecrire les coordonnés de la cellule a deposser ")
    coordonnees = (int(input("X: " ))), (int(input("Y: ")))     #Coordonnées de la cellule à placer
    tableau[coordonnees[0]][coordonnees[1]] = 1
    affiche_liste(tableau)
    continuer = input("Voulez vous ajouter une cellule vivante Y/N ? ")
    

root = Tk()     
Can = Canvas(root, width=p*e, height=n*e, background="white")
Can.pack(fill="both", expand=True)

afficher_tableau(tableau)
root.title("Le jeu de la vie")      #Positionnement du titre et des deux bouttons
evol.pack(side= LEFT)
quitter.pack(side= RIGHT)


root.mainloop()


    

