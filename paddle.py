from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-100,-240)
        self.color("deep pink")
        self.shape("paddle")
        