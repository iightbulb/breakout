from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 265)
        self.score = 1
        self.pendown()
        self.write(f"Level: {self.score}", align="center", font=("Arial", 14, "normal"))

    def end_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Arial", 14, "normal"))