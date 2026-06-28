from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

        self.direction = RIGHT

    def create_snake(self):
        for i, position in enumerate(STARTING_POSITIONS):
            segment = Turtle("square")
            segment.penup()
            segment.goto(position)

            # realistic python gradient body
            if i == 0:
                segment.shape("circle")
                segment.color("#d4af37")  # golden head
                segment.shapesize(1.1, 1.1)
            else:
                shade = 255 - (i * 18)
                color = f"#{shade:02x}{int(shade * 0.6):02x}{int(shade * 0.3):02x}"
                segment.color(color)

            self.segments.append(segment)

    def add_segment(self):
        tail = self.segments[-1]
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(tail.position())
        new_segment.color("#8b5a2b")
        self.segments.append(new_segment)

    def extend(self):
        for _ in range(2):  # more satisfying growth
            self.add_segment()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
