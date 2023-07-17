from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 265)
        self.lives = 3
        self.all_blocks = []
        self.pendown()
        self.write(f"Lives: {self.lives}", align="center", font=("Arial", 14, "normal"))

    def make_blocks(self):
        for n in range(5):
            for i in range(10):
                new_block = Turtle("square")
                new_block.shapesize(stretch_wid=1, stretch_len=3)
                new_block.penup()
                new_block.color('white', choice(COLORS))
                new_block.goto(-270+i*60, 290-n*20)
                self.all_blocks.append(new_block)

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def update(self):
        self.lives -= 1
        self.clear()
        self.write(f"Level: {self.lives}", align="center", font=("Arial", 14, "normal"))