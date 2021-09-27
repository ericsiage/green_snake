import turtle
import time
import random

posponer = 0.1

#configuracion de la ventana
wn = turtle.Screen()
wn.title("Juego snake")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0)

#cabeza serpiente atributos
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.penup()
cabeza.goto(0,0)
cabeza.color("green")
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


#Texto

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntaje: 0         Puntaje maximo: 0", align="center", font=("Arial", 13, "normal"))
#Marcador
score = 0
high_score = 0


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
       x = random.randint(-280,280) #creamos la comida en una ubicacion random
       y = random.randint(-280,280) 
       comida.goto(x,y)

       
       nuevo_segmento = turtle.Turtle()
       nuevo_segmento.speed(0)
       nuevo_segmento.shape("circle")
       nuevo_segmento.penup()
       nuevo_segmento.color("lightgreen")
       segmentos.append(nuevo_segmento) #agregamos nuevo_segmento a segmentos

       #aumentar Marcador
       score += 10
       if score > high_score:
           high_score = score
           texto.clear()
           texto.write("Puntaje: {}         Puntaje maximo: {}".format(score, high_score), align="center", font=("Arial", 13, "normal"))

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

    # colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction("stop")

        #esconder segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
        #limpiar segmentos
        segmentos.clear()

        #resetear marcador
        score = 0
        texto.clear()
        texto.write("Puntaje: {}         Puntaje maximo: {}".format(score, high_score), align="center", font=("Arial", 13, "normal"))
    mov()


    # Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction("stop")

            #esconder segmentos
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            #limpiar los elementos de la lista
            segmentos.clear()


        
    
    time.sleep(posponer)

