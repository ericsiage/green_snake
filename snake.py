import turtle
import time
import random

posponer = 0.1
#configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#cabeza serpiente atributos
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.penup()
cabeza.goto(0,0)
cabeza.color("green")
cabeza.width(30)
cabeza.direction = "stop" 

#comida atributos
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")

#cuerpo serpiente
segmentos = []


#funciones

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

#funcionalidad
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor() #cordenada y
        cabeza.sety(y + 20) #y se mueve 20 pixeles
    
    if cabeza.direction == "down":
        y = cabeza.ycor() #cordenada y
        cabeza.sety(y - 20) #y se mueve 20 pixeles
    
    if cabeza.direction == "left":
        x = cabeza.xcor() #cordenada y
        cabeza.setx(x - 20) #x se mueve 20 pixeles
    
    if cabeza.direction == "right":
        x = cabeza.xcor() #cordenada y
        cabeza.setx(x + 20) #x se mueve 20 pixeles

    

#Funciones de Teclado
wn.listen()
wn.onkeypress(arriba, "w")
wn.onkeypress(abajo, "s")
wn.onkeypress(izquierda, "a")
wn.onkeypress(derecha, "d")


#bucle para actualizar-
while True:
    wn.update()

    if cabeza.distance(comida) < 20:
       x = random.randint(-280,280)#creamos la comida en una ubicacion random
       y = random.randint(-280,280) 
       comida.goto(x,y)

       
       nuevo_segmento = turtle.Turtle()
       nuevo_segmento.speed(0)
       nuevo_segmento.shape("circle")
       nuevo_segmento.penup()
       nuevo_segmento.color("black", "green")
       segmentos.append(nuevo_segmento) #agregamos nuevo_segmento a segmentos

    #mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
        #agregar segmentos a la cabeza
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
                
    for index in range (totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)


        
    mov()
    time.sleep(posponer)

