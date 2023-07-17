from turtle import Turtle

STARTING_POSITION = (0, -240)
MOVE_DISTANCE = 15


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 3)
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(0, -280)

    def hit_ball(self):
        pass


