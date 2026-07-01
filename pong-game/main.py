from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("#111827")
screen.setup(width=800, height=600)
screen.tracer(0)

# Center dashed line
line = Turtle()
line.hideturtle()
line.color("#374151")
line.penup()
line.goto(0, 300)
line.setheading(270)

for _ in range(20):
    line.pendown()
    line.forward(15)
    line.penup()
    line.forward(15)

# Game objects
left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

game_is_on = True

# Game loop
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Right paddle collision
    if (
            ball.xcor() > 330
            and ball.distance(right_paddle) < 60
            and ball.x_move > 0
    ):
        ball.bounce_x()

    # Left paddle collision
    if (
            ball.xcor() < -330
            and ball.distance(left_paddle) < 60
            and ball.x_move < 0
    ):
        ball.bounce_x()

    # Right misses (left player scores)
    if ball.xcor() > 380:
        scoreboard.point_left()
        ball.reset_position()

    # Left misses (right player scores)
    if ball.xcor() < -380:
        scoreboard.point_right()
        ball.reset_position()

screen.exitonclick()
