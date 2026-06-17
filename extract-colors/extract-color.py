import random
from turtle import Screen, Turtle
from color_extractor import extract_colors

colors = extract_colors("img.png")

print(colors)
colors_list = [(32, 31, 31), (54, 35, 45), (222, 75, 150), (151, 51, 105), (106, 40, 81), (241, 106, 187), (91, 52, 45),
               (34, 33, 39), (115, 67, 59), (250, 205, 237), (237, 147, 74), (250, 149, 225), (251, 236, 188),
               (244, 220, 113), (28, 33, 29), (161, 141, 83), (197, 103, 80), (72, 66, 48), (246, 168, 140)]

brush = Turtle()
screen = Screen()
screen.colormode(255)

brush.penup()
brush.setheading(225)
brush.forward(300)
brush.setheading(0)
number_of_dots = 100
brush.speed(100)

for dot_count in range(1, number_of_dots + 1):

    brush.dot(20, random.choice(colors_list))
    brush.forward(50)

    if dot_count % 10 == 0:
        brush.setheading(90)
        brush.forward(50)
        brush.setheading(180)
        brush.forward(500)
        brush.setheading(0)

screen.exitonclick()
