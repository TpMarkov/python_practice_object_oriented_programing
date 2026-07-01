from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

DISTANCE_TO_COLLISION = 18
screen = Screen()
screen.setup(width=650, height=650)
screen.title("🐍 Neon Snake Pro")
screen.tracer(0)

# Background texture
screen.bgpic("assets/bg.gif")

# Border (clean neon frame)
border = Turtle()
border.hideturtle()
border.pensize(3)
border.color("#00ffcc")
border.penup()
border.goto(-300, -300)
border.pendown()

for _ in range(4):
    border.forward(600)
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
    time.sleep(0.08)

    snake.move()

    # Food collision
    if snake.head.distance(food) < DISTANCE_TO_COLLISION:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Wall collision
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        scoreboard.game_over()
        game_is_on = False

    # Tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 12:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()
