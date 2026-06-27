from turtle import Screen, Turtle
from snake import Snake
import time

segments = []
game_is_on = True
new_snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

screen.listen()

screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
