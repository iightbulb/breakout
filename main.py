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

# screen must listen for player moving left/right - only if within walls of playing surface
screen.listen()
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    # move ball
    ball.move_ball()
    time.sleep(ball.move_speed)

    # detect collision of ball with upper wall
    if ball.ycor() > 285:
        ball.bounce_y()
    # detect if collision of ball with l/r walls
    if ball.xcor() > 279 or ball.xcor() < -285:
        ball.bounce_x()
    # detect if player hit ball
    if ball.distance(player) < 37 and ball.ycor() < -225:
        ball.bounce_y()
    # detect if player misses ball and loses life - update life count on scoreboard
    if ball.ycor() < -300:
        ball.reset_game()
        scoreboard.update_lives()

    # detect collision of ball with brick
    for i in range(len(scoreboard.all_blocks)):
        for n in range(len(scoreboard.all_blocks[1])):
            if ball.distance(scoreboard.all_blocks[i][n]) < 30 and scoreboard.all_blocks[i][n].isvisible():
                scoreboard.all_blocks[i][n].hideturtle()
                ball.bounce_y()

    # check if level is done, if done -> new level
    if scoreboard.level_done():
        scoreboard.make_blocks()
        ball.new_level()

    # check if player has lost all 3 lives
    if scoreboard.lives == 0:
        scoreboard.game_over()
        break

screen.exitonclick()
