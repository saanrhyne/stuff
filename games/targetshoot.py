import turtle
import random
import math
import time

window = turtle.Screen()
score = 0

radius = 135
colors = ["black", "blue", "red", "yellow", "white"]
for i in range(5):
  target = turtle.Turtle()
  target.speed(0)
  target.hideturtle()
  target.penup()
  target.goto(0, 0 - radius)
  target.pendown()
  target.fillcolor(colors[i])
  target.begin_fill()
  target.circle(radius)
  target.end_fill()
  radius -= (6.5 - i)*6

cursor = turtle.Turtle()
cursor.penup()
cursor.shape("classic")
cursor.color("green")

def stopGame():
  global move
  move = False

window.onkey(stopGame, "x")

def scoreCalc():
  distance = math.sqrt(cursor.xcor() ** 2 + cursor.ycor() ** 2)
  if distance <= 15:
    print("white - 5 points 🎯")
    return 5
  elif distance <= 36:
    print("yellow - 4 points 💰")
    return 4
  elif distance <= 63:
    print("red - 3 points 🔥")
    return 3
  elif distance <= 96:
    print("blue - 2 points 👾")
    return 2
  elif distance <= 135:
    print("black - 1 point 😎")
    return 1
  else:
    print("gray - 0 points")
    return 0

for i in range(5):
  window.listen()
  cursor.speed(0)
  cursor.setpos(random.randint(-100, 100), random.randint(-100, 100))
  move = True
  while move:
    cursor.forward(random.randint(0, 25))
    cursor.left(random.randint(0, 360))
    
    if cursor.xcor() > 150 or cursor.xcor() < -150: cursor.setx(random.randint(-100, 100))
    if cursor.ycor() > 150 or cursor.ycor() < -150: cursor.sety(random.randint(-100, 100))

  score += scoreCalc()
  print("You have " + str(score) + " points")
  time.sleep(1)
    
print("Game over")
