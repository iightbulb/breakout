# 80s game breakout written using turtle

import time
from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
ball = Ball()
scoreboard = Scoreboard()

scoreboard.make_blocks()


game_is_on = True
while game_is_on:
    screen.update()
    # move ball
    ball.move_ball()
    time.sleep(0.01)

    # screen must listen for player moving left/right - only if within walls of playing surface
    screen.listen()
    screen.onkeypress(player.move_right, "Right")
    screen.onkeypress(player.move_left, "Left")

    # detect collision of ball with upper wall
    if ball.ycor() > 288:
        ball.bounce_y()
    # detect if collision of ball with l/r walls
    if ball.xcor() > 288 or ball.xcor() < -288:
        ball.bounce_x()
    # detect if player hit ball
    if ball.distance(player) < 40 and ball.ycor() < -225:
        ball.bounce_y()
    # detect if player misses ball and loses life - update life count on scoreboard
    if ball.ycor() < -300:
        ball.reset_game()
        scoreboard.update()


screen.exitonclick()
