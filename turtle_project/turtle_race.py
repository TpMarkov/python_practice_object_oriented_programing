from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Witch turtle will win the race. Select color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim = Turtle()
tim.penup()
tim.goto(x=-230, y=-100)

screen.exitonclick()
