from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Set up the score turtle to keep track of how many points the player has won
        self.color("light steel blue")
        self.speed(0)
        self.penup()
        self.goto(-250,260)
        score = 0
        self.write(f"Score: + {score}")
        self.ht()