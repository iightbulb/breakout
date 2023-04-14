from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BlockManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, 0)
