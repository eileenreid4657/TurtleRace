import time
import turtle
import random
from turtle import Turtle



#Window Setup
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write('Turtle Race', font = ('Ariel', 30, "bold"))
turtle.penup()

#Dirt

turtle.setpos(-400, -180)
turtle.color('chocolate')
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#Finish Line
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line, (150-(i*square_size*2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150-square_size) - (j*square_size*2)))
    turtle.stamp()

turtle.hideturtle()

#Turtle1
tim = Turtle()
tim.speed(0)
tim.color('black')
tim.shape('turtle')
tim.penup()
tim.goto(-250, 100)
tim.pendown()

#Turtle2
dave = Turtle()
dave.speed(0)
dave.color('cyan')
dave.shape('turtle')
dave.penup()
dave.goto(-250, 50)
dave.pendown()

#Turtle3
ed = Turtle()
ed.speed(0)
ed.color('magenta')
ed.shape('turtle')
ed.penup()
ed.goto(-250, 0)
ed.pendown()

#Turtle4
jo = Turtle()
jo.speed(0)
jo.color('yellow')
jo.shape('turtle')
jo.penup()
jo.goto(-250, -50)
jo.pendown()

time.sleep(1) #Pause game for one second before starting

#Move the Turtles

for i in range(145):
    tim.forward(random.randint(1,5))
    dave.forward(random.randint(1,5))
    ed.forward(random.randint(1,5))
    jo.forward(random.randint(1,5))



delay = input('Please push enter to exit!!!')