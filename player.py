from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_left(self):
        self.left(MOVE_DISTANCE)

    def move_right(self):
        self.right(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(0, -280)

    # potentially create function to prevent player moving off of screen (left/right)