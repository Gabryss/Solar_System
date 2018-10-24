# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:36:01 2018

@author: Gabriel
"""

#Tests Simulation système solaire (terre)
import turtle
#Definition des curseurs

Soleil = turtle.Turtle()
Soleil.shape("circle")
Soleil.color("yellow")
Soleil.resizemode("user")
Soleil.shapesize(2,2,1)

Terre= turtle.Turtle()
Terre.shape("circle")
Terre.color("blue","green")
Terre.resizemode("user")
Terre.shapesize(5/10,5/10,1)

Lune = turtle.Turtle()
Lune.shape("circle")
Lune.color("grey")
Lune.resizemode("user")
Lune.shapesize(1/10,1/10,1)

Mars = turtle.Turtle()
Mars.shape("circle")
Mars.color("red","grey")
Mars.resizemode("user")
Mars.shapesize(3/10,3/10,1)

#imgsol="Sol.gif"
#turtle.register_shape(imgsol)
#Soleil.shapesize(1/10, 1/10)
#Soleil.shape(imgsol)

turtle.title('Système Solaire v2')
turtle.bgcolor('Black')


#CONDITIONS INITIALES

Astres = [
    {   
        
        "nom": "Soleil",
        "turtle": Soleil,
        "masse":1.989*10**30,
        "pos":turtle.Vec2D(0,0),
        "vit":turtle.Vec2D(0,0),
        "vit_final":turtle.Vec2D(0,0),
        "pos_final":turtle.Vec2D(0,0)
        
    },
    {
     
         "nom": "Terre",
         "turtle": Terre,
         "masse":5.972*10**24,
         "pos":turtle.Vec2D(149.6*10**9,0),
         "vit":turtle.Vec2D(0,30000),
         "vit_final":turtle.Vec2D(0,0),
         "pos_final":turtle.Vec2D(0,0)
     },
     {
     
         "nom":"Lune",
         "turtle": Lune,
         "masse":7.342*10**22,
         "pos":turtle.Vec2D(149.9844*10**9,0),
         "vit":turtle.Vec2D(0,31022.22),
         "vit_final":turtle.Vec2D(0,0),
         "pos_final":turtle.Vec2D(0,0)
          
     },
     {
         "nom":"Mars",
         "turtle": Mars,
         "masse": 6.39*10**23,
         "pos":turtle.Vec2D(227.936637 *10**9,0),
         "vit":turtle.Vec2D(0,24700),
         "vit_final":turtle.Vec2D(0,0),
         "pos_fianl":turtle.Vec2D(0,0)
     },
      
        ]

#PARAMETRE CONSTANT

G= 6.67408 * 10 ** (-11)
dt = 3600
nb_objets=len(Astres)

for t in Astres: 
    t["turtle"].up()
    t["turtle"].speed(0)
    t["turtle"].goto(t["pos"]*1e-9)
    
#Vitesse suivante = Vitesse précédente + deltat * l'accélération
for nbiteration in range (100000):
    
    for i in range(nb_objets):
        acc=turtle.Vec2D(0,0)
        
        
        for j in range(nb_objets):
            if i!=j:
                acceleration= -G * ( (Astres[j]["masse"] )/(abs(Astres[i]["pos"]-Astres[j]["pos"])**3 )) * ((Astres[i]["pos"]-Astres[j]["pos"]))
                acc = acc + acceleration
        print("accélération \n" ,acc )
        
        Astres[i]["vit_final"] = Astres[i]["vit"] + dt * acc
        print("vitesse \n", Astres[i]["vit"])
        
        Astres[i]["pos_final"] = Astres [i]["pos"] + dt * Astres[i]["vit_final"]
        print("position \n", Astres[i]["pos_final"])
        
        Astres[i]["vit"] = Astres[i]["vit_final"]
        Astres[i]["pos"] = Astres[i]["pos_final"]
        
        if nbiteration % 10==0:
            Astres[i]["turtle"].goto(Astres[i]["pos"]*1e-9)


turtle.exitonclick()
turtle.mainloop()