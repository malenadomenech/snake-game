import turtle
from turtle import *
import random
import time

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("orange")
wn.setup(width=600, height=600)
wn.tracer(0)

segmentos = []

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("black")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 0)

# Funciones
def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 10)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 10)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 10)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 10)

    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

        for i in range(totalSeg - 1, 0, -1):
            x = segmentos[i - 1].xcor()
            y = segmentos[i - 1].ycor()
            segmentos[i].goto(x, y)

    wn.update()
    
    #Colisiones bordes

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:

        time.sleep(1)

        cabeza.goto(0,0)

        cabeza.direction = "stop"


    # Colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("black")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

    # Llamar a la función mov() nuevamente después de un breve intervalo
    wn.ontimer(mov, 100)

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

# Iniciar el movimiento
mov()

# Iniciar el bucle principal
wn.mainloop()

