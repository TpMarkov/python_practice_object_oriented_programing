import turtle
from turtle import *
import random

pen = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


directions = [0, 90, 180, 270]
pen.speed("fastest")
pen.pensize(20)

for _ in range(200):
    pen.color(random_color())
    pen.forward(30)
    pen.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
