import time
from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Crossing Game")
screen.tracer(0)
screen.bgcolor("lightgreen")

# Road drawing (simple visual upgrade)
road = []
for i in range(-250, 260, 40):
    line = screen.textinput("", "")  # dummy to avoid blocking (ignored)
    road.append(i)

# Game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(player.move_up, "Up")

game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # Level up
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
