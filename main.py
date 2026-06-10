# from turtle import Turtle, Screen
# import another_module
#
# print(another_module.another_variable)
#
# new_turtle = Turtle()
# my_screen = Screen()
#
# new_turtle.shape("turtle")
# new_turtle.color("coral")
# new_turtle.speed(2)
# new_turtle.forward(100)
# my_screen.exitonclick()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)

import prettytable
from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Pokemon-Name", ["Pikachu", "Squirtle", "Charmander"], "l", )
my_table.add_column("Pokemon-Type", ["Electric", "Water", "Fire"], "l")

print(my_table)
