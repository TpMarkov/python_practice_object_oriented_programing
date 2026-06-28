from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Scoreboard

DISTANCE_TO_COLLISION = 15
segments = []
game_is_on = True

new_snake = Snake()
new_food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()

screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    new_snake.move()

    if new_snake.head.distance(new_food) < DISTANCE_TO_COLLISION:
        scoreboard.increase_score()
        new_food.refresh()
        new_snake.extend()
