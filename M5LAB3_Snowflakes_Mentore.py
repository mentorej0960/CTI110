#CTI-110 
#M5LAB3- Snowflakes
#Jermine Mentore
#October 15, 2017



import turtle
import random

wn = turtle.Screen()
elsa = turtle.Turtle()
wn.bgcolor("grey")
colors = ["cyan", "purple", "white", "blue", "yellow"]



for i in range(10):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(36)
    elsa.color(random.choice(colors))
elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()
def branch():
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)

for i in range(8):
    branch()
    elsa.left(45)

# elsa.color(random.choice(colors))
    
wn.exitonclick()
