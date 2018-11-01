# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:36:01 2018

@author: Gabriel
"""

#Tests Simulation système solaire (terre)
import turtle
#INITIALISATION FENETRE

turtle.setup(1000,700)
turtle.title('Système Solaire v2')
turtle.bgcolor('Black')
#turtle.mode("world")

#DONNEES INITIALES ET CONSTANTES

G= 6.67408 * 10 ** (-11)
dt = 36000
 
Astres = [
    {   
        
        "nom": "Soleil",
#        "turtle": Soleil,
        "color":"yellow",
        "masse":1.989*10**30,
        "taille":[2,2,1],
        "pos":turtle.Vec2D(0,0),
        "vit":turtle.Vec2D(0,0),
        "vit_final":turtle.Vec2D(0,0),
        "pos_final":turtle.Vec2D(0,0)
        
    },
    {
         "nom":"Mercure",
#         "turtle": Mercure,
         "color":"grey",
         "masse": 3.3011*10**23 ,
         "taille":[2/10,2/10,1] ,
         "pos":turtle.Vec2D((57.909176*10**9),0),
         "vit":turtle.Vec2D(0,47360),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
    {
         "nom":"Vénus",
#         "turtle": Venus,
         "color":"yellow",
         "masse": 4.8685*10**24,
         "taille":[3/10,3/10,1] ,
         "pos":turtle.Vec2D(108.208930*10**9 ,0),
         "vit":turtle.Vec2D(0,35200),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
    {
     
         "nom": "Terre",
#         "turtle": Terre,
         "color":"blue",
         "masse":5.972*10**24,
         "taille":[4/10,4/10,1] ,
         "pos":turtle.Vec2D(149.6*10**9,0),
         "vit":turtle.Vec2D(0,30000),
         "vit_final":turtle.Vec2D(0,0),
         "pos_final":turtle.Vec2D(0,0)
     },
     {
     
         "nom":"Lune",
         #"turtle": Lune,
         "color":"grey",
         "masse":7.342*10**22,
         "taille":[1/10,1/10,1] ,
         "pos":turtle.Vec2D(149.9844*10**9,0),
         "vit":turtle.Vec2D(0,31022.22),
         "vit_final":turtle.Vec2D(0,0),
         "pos_final":turtle.Vec2D(0,0)
          
     },
     {
         "nom":"Mars",
        # "turtle": Mars,
         "color":"red",
         "masse": 6.39*10**23,
         "taille":[3/10,3/10,1] ,
         "pos":turtle.Vec2D(227.936637 *10**9,0),
         "vit":turtle.Vec2D(0,24700),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
     {
         "nom":"Jupiter",
       #  "turtle": Jupiter,
         "color":"yellow",
         "masse": 1.8986*10**27,
         "taille":[10/10,10/10,1] ,
         "pos":turtle.Vec2D(778.412027*10**9,0),
         "vit":turtle.Vec2D(0,13000),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
     {
         "nom":"Saturne",
        # "turtle": Saturne,
         "color":"yellow",
         "masse": 1.8986*10**27,
         "taille":[7/10,7/10,1] ,
         "pos":turtle.Vec2D(1429.394069*10**9,0),
         "vit":turtle.Vec2D(0,9644.6),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
     {
         "nom":"Uranus",
        # "turtle": Uranus,
         "color":"blue",
         "masse": 8.6810*10**25,
         "taille":[6/10,6/10,1] ,
         "pos":turtle.Vec2D(2870.658186*10**9,0),
         "vit":turtle.Vec2D(0,6800),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
     {
         "nom":"Neptune",
        #"turtle": Neptune,
         "color":"blue",
         "masse": 102.43*10**24,
         "taille":[6/10,6/10,1],
         "pos":turtle.Vec2D(4503.443661*10**9,0),
         "vit":turtle.Vec2D(0,5431.7),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
      
        ]






#Définition des fonctions

#Définitions des curseurs
def curseurs(Astres):
    for Astre in Astres:
        Astre["turtle"]=turtle.Turtle()
        Astre["turtle"].shape("circle")
        Astre["turtle"].color(Astre["color"])
        Astre["turtle"].resizemode("user")
        Astre["turtle"].shapesize(Astre["taille"][0],Astre["taille"][1],Astre["taille"][2])
 
        
def affichage(centre,Astres,Name):
    
    for Astre in Astres:
        Astre["turtle"].goto((Astre["pos"]-centre["pos"])*1e-9)
        centre["turtle"].goto(turtle.Vec2D(0,0))
        if Name!=None:
            Name=erasableWrite(Astre["turtle"], Astre["nom"], font=("Arial", 10, "normal"), align="center", reuse=Name)
    
    
def evolution(Astre): #modifie les vitesses, accélérations, positions du dictionaire à a chaque appel
    d={}
    for i in range (len(Astres)):
        for j in range(i,len(Astres)):
            if Astres[i]!=Astres[j]:
                d[Astres[i]["nom"]+Astres[j]["nom"]]=((abs(Astres[i]["pos"]-Astres[j]["pos"]))**3)
         
    for Astre_in in Astres:
        acc=turtle.Vec2D(0,0)
        print(d)
        #Calcul de la nouvelle accélération
        for Astre_fin in Astres:
            if Astre_in!=Astre_fin and Astre_in["nom"]+Astre_fin["nom"] in d :
                acceleration= -G * ( (Astre_fin["masse"] )/d[Astre_in["nom"]+Astre_fin["nom"]]) * ((Astre_in["pos"]-Astre_fin["pos"]))
                acc = acc + acceleration
            elif Astre_in!=Astre_fin and Astre_in["nom"]+Astre_fin["nom"] not in d :
                acceleration= -G * ( (Astre_fin["masse"] )/d[Astre_fin["nom"]+Astre_in["nom"]]) * ((Astre_in["pos"]-Astre_fin["pos"]))
                acc = acc + acceleration
        print("accélération \n" ,acc, Astre_in["nom"] )
        
        #Calcul de la vitesse finale
        Astre_in["vit_final"] = Astre_in["vit"] + dt * acc
        print("vitesse \n", Astre_in["vit"], Astre_in["nom"])
        
        #Calcul de la position finale
        Astre_in["pos_final"] = Astre_in["pos"] + dt * Astre_in["vit_final"]
        print("position \n", Astre_in["pos_final"], Astre_in["nom"])
        
        #Réinitialisation des variables
        Astre_in["vit"] = Astre_in["vit_final"]
        Astre_in["pos"] = Astre_in["pos_final"]

#Fonction permetant d'effacer le nom des planètes et de le réafficher à chaque itération 
def erasableWrite(turtles, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.color("grey")
    eraser.up()
    eraser.speed(0)
    eraser.setposition(turtles.position())
    eraser.write(name, font=font, align=align)
    return eraser


def main():
    #Initialisation du système
    curseurs(Astres)
    for Astre in Astres: 
        Astre["turtle"].up()
        Astre["turtle"].speed(0)
        Astre["turtle"].goto(Astre["pos"]*1e-9)
        Name=erasableWrite(Astre["turtle"], Astre["nom"], font=("Arial", 10, "normal"), align="center")
        Name.clear()
    Centre=str(input("Quel est l'astre ciblé ? \n"))
    nb_iteration=int(input("Quel est la durée de la simulation ?\n"))
    noms=str(input("Voulez vous le mode optimisé ?\n"))
    
    if noms=="non":
        Name=None
        
    for Astre in Astres:
        if Astre["nom"]==Centre:
            centre=Astre
#        else:
#            print("Vous n'avez pas taper un astre disponible")
        
    for i in range (nb_iteration):
        if Name!=None:
            Name.clear()
        evolution(Astres)
        if i%10==0:
            affichage(centre,Astres,Name)
main()
turtle.exitonclick()
turtle.mainloop()