from turtle import Screen, Turtle

screen = Screen()

positions = [(0, 0), (-20, 0), (-40, 0)]
for curr_position in positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(curr_position)

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake game!")
screen.exitonclick()
