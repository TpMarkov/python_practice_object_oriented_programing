from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

DISTANCE_TO_COLLISION = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game")
screen.tracer(0)

# Draw border
border = Turtle()
border.hideturtle()
border.color("gray")
border.penup()
border.goto(-290, -290)
border.pendown()

for _ in range(4):
    border.forward(580)
    border.left(90)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    screen.update()

    speed = max(0.03, 0.10 - scoreboard.score * 0.002)
    time.sleep(speed)

    snake.move()

    # Food collision
    if snake.head.distance(food) < DISTANCE_TO_COLLISION:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Wall collision
    if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
    ):
        scoreboard.game_over()
        game_is_on = False

    # Tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
