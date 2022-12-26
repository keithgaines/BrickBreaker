# The Brick Breaker Game
import turtle as tk
import random
from boundary import Boundary
from score import Scoreboard
from paddle import Paddle
from ball import Ball

screen = tk.Screen()
screen.setup(width=600, height=700)
screen.tracer(0)
screen.bgcolor("black")
screen.register_shape("paddle",((0,0),(20,0),(20,100),(0,100)))



boundary = Boundary()
scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()

for x in range(4):
  boundary.forward(500)
  boundary.right(90)
  boundary.begin_fill()
  boundary.end_fill()
  boundary.ht()

screen.update()
# Create an empty list
# add the bricks turtle to the list and set them up
# when setting up create 3 rows of the brick turtles
screen.register_shape("brick",((0,0),(10,0),(10,50),(0,50)))

colors = ["sky blue", "tomato", "lime green","yellow"]
def makeRow(x,y,colors):
  index = random.randint(0,len(colors)-1)
  row = []
  for i in range(8):
    targetT = tk.Turtle()
    targetT.speed(0)
    targetT.shape("brick")
    targetT.color(colors[index])
    targetT.penup()
    targetT.goto(x + 60*i,y)
    targetT.pendown()
    row.append(targetT)
    index = random.randint(0,len(colors)- 1)
  return row


screen.update()

# Write the event Listeners (left and right)
def right():
  paddle.forward(10)

screen.onkey(right, "Right")

def left():
  paddle.backward(10)

screen.onkey(left, "Left")

screen.listen()

# def checkcollison between the ball and obj

# return true or false
def checkCollisonBrick(obj):
  if abs(ball.xcor() - obj.xcor()) < 50 and obj.ycor() <= ball.ycor() <= obj.ycor() + 10 :
    print("colided with the brick:", obj)
    return True
  return False

def checkCollisonPaddle(obj):
  if abs(ball.xcor() - obj.xcor()) < 100 and (obj.ycor() <= ball.ycor() <= obj.ycor() + 20) :
    return True

  return False

def bounce(context):
  #top
  if context == "top" or context == "paddle":
    ball.setheading(360 - ball.heading())
  #top half of screen
  elif 180 > ball.heading() >= 0:
    ball.setheading(180 - ball.heading())
  #bottom half
  elif 180 <= ball.heading() < 360:
    ball.setheading(540 - ball.heading())

screen.update()

def countList():
  count = []
  for i in range(8):
    count.append(0)
  return count

def hitBrick(row, count, goal):
  global score
  for x in range(len(row)):
    #checks to see if this specific brick collided with ball
    if checkCollisonBrick(row[x]):
      #checks if brick should disappear
      if count[x] > goal:
        row[x].ht()
        row[x].penup()
        row[x].goto(-1000,1000)
      else:
        #brick can still be hit more
        count[x] += 1
        bounce("paddle")

      score = updateScore(score)

  return count

def updateScore(score):
  score += 5
  scoreboard.clear()
  scoreboard.write(f"Score: {score}")
  return score

row1 = makeRow(-230,200,colors)
count1 = countList()
row2 = makeRow(-230,170,colors)
count2 = countList()
row3 = makeRow(-230,140,colors)
count3 = countList()
row4 = makeRow(-230,110,colors)
count4 = countList()

score = 0
gameContinue=True

#while loop
while gameContinue:
  ball.forward(5)

  screen.update()
  # if checkcollison with ball and paddle then the ball sould bounce off
  count1 = hitBrick(row1, count1, 4)

  count2 = hitBrick(row2, count2, 3)

  count3 = hitBrick(row3, count3, 2)

  count4 = hitBrick(row4, count4, 1)


  #if score = 100 then boundry turtle will write you win on the screen
  #5 points each time ball hits one brick

  if ball.ycor() < -240:
    boundary.penup()
    boundary.goto(-200,0)
    boundary.color("midnight blue")
    boundary.write("YOU LOSE!")
    gameContinue=False

  if score == 720:
    boundary.penup()
    boundary.goto(-200,0)
    boundary.color("orange")
    boundary.write("You Win!")
    gameContinue=False

  # if the ball hits the top, left, and right side it should bounce back

  #right side
  if ball.xcor() > 240:
    bounce("right")

  #left side
  if ball.xcor() < -240:
    bounce("left")

  #top side
  if ball.ycor() > 240:
    bounce("top")

  #hits paddle
  if checkCollisonPaddle(paddle):
    bounce("paddle")

  #if paddle hits the right edge
  if paddle.xcor() + 100  > 240:
    paddle.backward(10)

  #if paddle hits the left edge
  if paddle.xcor() < -240:
    paddle.forward(10)

  # if the ball hits the botttom of the screen then while loop should stop

  screen.update()

screen.exitonclick()
