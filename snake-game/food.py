from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("#39ff14")  # neon green
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)

        self.glow_state = 0
        self.refresh()

    def refresh(self):
        x = random.randrange(-260, 261, 20)
        y = random.randrange(-260, 261, 20)
        self.goto(x, y)

    def pulse(self):
        # subtle glow effect
        colors = ["#39ff14", "#2cff00", "#66ff66"]
        self.color(colors[self.glow_state % len(colors)])
        self.glow_state += 1
