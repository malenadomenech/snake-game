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



while True:
    wn.update()

 

