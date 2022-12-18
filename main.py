import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

# sets up screen
screen = Screen()
screen.setup(width=600, height=1200)
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.tracer(0)

paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top/bottom wall
    if ball.ycor() > 500 or ball.distance(paddle) < 50:
        ball.bounce_y()

    # detect collision with paddle
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.bounce_x()
 
    # reset ball position if ball goes further than bottom wall
    if ball.ycor() < -500:
        ball.reset_position()

    

screen.exitonclick()