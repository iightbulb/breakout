from turtle import Turtle
from random import choice
import numpy as np

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "violet", "turquoise", "skyblue", "cyan", "magenta",
          "darkgreen", "chocolate"]
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-260, -280)
        self.lives = 3
        self.level = 1
        self.all_blocks = []
        self.pendown()
        self.write(f"Lives: {self.lives}", align="center", font=("Arial", 10, "normal"))
        self.penup()
        self.goto(-200, -280)
        self.pendown()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 10, "normal"))

    def make_blocks(self):
        row = []
        for n in range(5):
            for i in range(10):
                new_block = Turtle("square")
                new_block.shapesize(stretch_wid=1, stretch_len=3)
                new_block.penup()
                new_block.color('white', choice(COLORS))
                new_block.goto(-270+i*60, 290-n*20)
                row.append(new_block)
            self.all_blocks.append(row)
            row = []
        print(self.all_blocks)

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def update_lives(self):
        self.penup()
        self.lives -= 1
        self.clear()
        self.goto(-260, -280)
        self.pendown()
        self.write(f"Lives: {self.lives}", align="center", font=("Arial", 10, "normal"))
        self.penup()
        self.goto(-200, -280)
        self.pendown()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 10, "normal"))

    def level_done(self):
        if not self.all_blocks:
            self.level += 1
            self.clear()
            self.penup()
            self.goto(-200, -280)
            self.pendown()
            self.write(f"Level: {self.level}", align="center", font=("Arial", 10, "normal"))
            return True

    def game_over(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"YOU LOST", align="center", font=("Arial", 24, "normal"))
        self.all_blocks = []
