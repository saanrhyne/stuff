import turtle
import random

window = turtle.Screen()
window.bgcolor("block")
window.tracer(0)

# Tree
t = turtle.Turtle()

def drawTree(x, y):
  t.speed(0)
  t.penup()
  t.goto(x, y)
  t.pendown()
  
  t.color("green")
  t.begin_fill()
  for i in range(3):
    t.forward(100)
    t.left(120)
  t.end_fill()
  
  t.color("brown")
  t.hideturtle()
  t.penup()
  t.goto(x + 40, y - 30)
  t.pendown()
  t.begin_fill()
  
  for i in range(2):
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.left(90)
  t.end_fill()

drawTree(75, -175)

topper = turtle.Turtle()
topper.speed(0)
topper.penup()
topper.shape("turtle")
topper.color("yellow")
topper.setheading(90)
topper.goto(125, -85)

gift1 = turtle.Turtle()
gift1.shape("square")
gift1.penup()
gift1.color("red")
gift1.goto(90, -190)

gift2 = turtle.Turtle()
gift2.shape("square")
gift2.penup()
gift2.color("pink")
gift2.goto(150, -190)

# Create snowflakes
num = 50
snowflakes = []

for i in range(num):
  snowflake = turtle.Turtle()
  snowflake.penup()
  snowflake.shape("turtle")
  snowflake.color("white")
  snowflake.goto(random.randint(-200, 200), random.randint(-200, 200))
  snowflake.setheading(random.randint(0, 360))
  snowflakes.append(snowflake)

# Falling snow animation
while True:
  topper.setheading(topper.heading() + 45)
  
  for snowflake in snowflakes:
    snowflake.sety(snowflake.ycor() - random.randint(1, 4)/2)
    snowflake.setheading(snowflake.heading() + 30)
    
    # Reset snowflake if it reaches the bottom
    if snowflake.ycor() < -200:
      snowflake.goto(random.randint(-200, 200), 200)
  
  window.update() # Update the screen with new snowflake positions
