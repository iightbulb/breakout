# 80s game breakout written using turtle

import time
from turtle import Screen
from player import Player
from block import BlockManager

screen = Screen()
screen.setup(width=300, height=600)
screen.tracer(0)

player = Player()
block = BlockManager()


screen.listen()
# screen must listen for player moving left/right
# screen.onkeypress(player.move_up, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()


screen.exitonclick()