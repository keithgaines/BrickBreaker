from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(-50,-210)
        self.setheading(random.randint(1,179))
        self.x_move = 6
        self.y_move = 6
        self.move_speed = 0.9


