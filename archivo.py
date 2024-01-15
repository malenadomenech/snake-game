import turtle
from turtle import *
import time
 
posponer = 0.1

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
cabeza.direction = "left"

#Funciones
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    



while True:
    mov()
    wn.update()

time.sleep(posponer)
    


 

