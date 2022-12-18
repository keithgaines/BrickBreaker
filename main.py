import time
from turtle import Screen

from paddle import Paddle
from scoreboard import Scoreboard

# sets up screen
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.tracer(0)

screen.exitonclick()