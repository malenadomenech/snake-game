import turtle
from turtle import *
 

#Configuración de la ventana

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("orange")
wn.setup(width= 600, height= 600)
wn.tracer(0)


#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("black")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Funciones
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
        cabeza.sety(y + 0.10)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 0.10)
    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 0.10)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 0.10)

#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

    



while True:
    mov()
    wn.update()


    


 

