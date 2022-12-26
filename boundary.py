from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        # Set up the boundry turtle so there will be a boundry for the game
        self.color("blue")
        self.speed(0)
        self.penup()
        self.goto(-250,250)
        self.pendown()
        self.begin_fill()