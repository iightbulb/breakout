from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 100)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 3
        self.y_move = 3

    # continuously move ball
    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    # bounce along y-axis
    def bounce_y(self):
        self.y_move *= -1
        self.xcor() + self.x_move
        self.ycor() + self.y_move

    # bounce along x-axis
    def bounce_x(self):
        self.x_move *= -1
        self.xcor() + self.x_move
        self.ycor() + self.y_move

    # move ball to centre if player loses a life
    def reset_game(self):
        self.goto(0, 100)
        self.bounce_x()
