import turtle
import math
import random


# INITIALIZE WINDOW
window = turtle.Screen()
window.bgcolor("black")


# BUMPER CAR ARENA WALLS
b = turtle.Turtle()
b.color("white")
b.penup()
b.hideturtle()
b.speed(0)
b.setposition(-200, -200)
b.pendown()
b.setposition(-200, 200)
b.setposition(200, 200)
b.setposition(200, -200)
b.setposition(-200, -200)
b.penup()
b.setposition(-50, -50)
b.pendown()
b.setposition(-50, 50)
b.setposition(50, 50)
b.setposition(50, -50)
b.setposition(-50, -50)


# CREATE AND RANDOMLY PLACE 4 COINS WITHIN EACH QUADRANT
c1 = turtle.Turtle()
c1.shape("circle")
c1.color("yellow")
c1.penup()
c1.hideturtle()
c1x = random.randint(50, 150)
c1y = random.randint(75, 175)
c1.speed(0)
c1.setposition(c1x,c1y)
c1.showturtle()

c2 = turtle.Turtle()
c2.shape("circle")
c2.color("yellow")
c2.penup()
c2.hideturtle()
c2x = random.randint(-150, -50)
c2y = random.randint(75, 175)
c2.speed(0)
c2.setposition(c2x,c2y)
c2.showturtle()

c3 = turtle.Turtle()
c3.shape("circle")
c3.color("yellow")
c3.penup()
c3.hideturtle()
c3x = random.randint(-150, -50)
c3y = random.randint(-175, -75)
c3.speed(0)
c3.setposition(c3x,c3y)
c3.showturtle()

c4 = turtle.Turtle()
c4.shape("circle")
c4.color("yellow")
c4.penup()
c4.hideturtle()
c4x = random.randint(50, 150)
c4y = random.randint(-175, -75)
c4.speed(0)
c4.setposition(c4x,c4y)
c4.showturtle()


# CREATE TURTLE 1
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("lightgreen")
t1.speed(0)
t1.penup()
t1.setposition(125, 0)
t1.setheading(90)
t1coins = 0

# TURTLE 1 MOVEMENT WITH ARROW KEYS
def t1Forward():
    t1.forward(5)
def t1Reverse():
    t1.backward(5)
def t1Right():
    t1.right(10)
def t1Left():
    t1.left(10)
window.onkey(t1Forward, "Up")
window.onkey(t1Reverse, "Down")
window.onkey(t1Right, "Right")
window.onkey(t1Left, "Left")


# CREATE TURTLE 2
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red")
t2.speed(0)
t2.penup()
t2.setposition(-125, 0)
t2.setheading(270)
t2coins = 0

# TURTLE 2 MOVEMENT WITH w a s d KEYS
def t2Forward():
    t2.forward(5)
def t2Reverse():
    t2.backward(5)
def t2Right():
    t2.right(10)
def t2Left():
    t2.left(10)
window.onkey(t2Forward, "W")
window.onkey(t2Reverse, "S")
window.onkey(t2Right, "D")
window.onkey(t2Left, "A")


# LISTENER LOOP FOR TURTLE COLLISION EVENTS
while True:
    window.listen()
    window.update()
	
    # COLLISION BETWEEN TURTLES
    dt1t2 = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if dt1t2 < 20:
        t1.setposition(125, 0)
        t1.setheading(90)
        t2.setposition(-125,0)
        t2.setheading(270)
        print("Double-ouch! Both turtles crashed into each other!")
    
    # COLLISION WITH OUTER ARENA WALLS
    if t1.xcor() >= 185 or t1.xcor() <= -185 or t1.ycor() <= -185 or t1.ycor() >= 185:
        t1.setposition(125, 0)
        t1.setheading(90)
        print("Ouch! Green turtle crashed into a wall!")
    if t2.xcor() >= 185 or t2.xcor() <= -185 or t2.ycor() <= -185 or t2.ycor() >= 185:
        t2.setposition(-125, 0)
        t2.setheading(270)
        print("Ouch! Red turtle crashed into a wall!")

    # COLLISION WITH INNER ARENA WALLS
    if t1.xcor() <= 65 and t1.xcor() >= -65 and t1.ycor() <= 65 and t1.ycor() >= -65:
        t1.setposition(125, 0)
        t1.setheading(90)
        print("Ouch! Green turtle crashed into a wall!")
    if t2.xcor() <= 65 and t2.xcor() >= -65 and t2.ycor() <= 65 and t2.ycor() >= -65:
        t2.setposition(-125, 0) 
        t2.setheading(270)
        print("Ouch! Red turtle crashed into a wall!")

    # COLLISION BETWEEN TURTLE 1 AND COINS 1 2 3 OR 4
    dt1c1 = math.sqrt(math.pow(t1.xcor()-c1.xcor(),2) + math.pow(t1.ycor()-c1.ycor(), 2))
    if dt1c1 < 20:
      if c1.isvisible():
        t1coins += 1
        if t1coins > 1:
          print("\033[0;32mCha-ching! Green turtle has " + str(t1coins) + " coins!")
        else:
          print("\033[0;32mCha-ching! Green turtle has 1 coin!\033[0m")
      c1.hideturtle()
    dt1c2 = math.sqrt(math.pow(t1.xcor()-c2.xcor(),2) + math.pow(t1.ycor()-c2.ycor(), 2))
    if dt1c2 < 20:
      if c2.isvisible():
        t1coins += 1
        if t1coins > 1:
          print("\033[0;32mCha-ching! Green turtle has " + str(t1coins) + " coins!\033[0m")
        else:
          print("\033[0;32mCha-ching! Green turtle has 1 coin!\033[0m")
      c2.hideturtle()
    dt1c3 = math.sqrt(math.pow(t1.xcor()-c3.xcor(),2) + math.pow(t1.ycor()-c3.ycor(), 2))
    if dt1c3 < 20:
      if c3.isvisible():
        t1coins += 1
        if t1coins > 1:
          print("\033[0;32mCha-ching! Green turtle has " + str(t1coins) + " coins!\033[0m")
        else:
          print("\033[0;32mCha-ching! Green turtle has 1 coin!\033[0m")
      c3.hideturtle()
    dt1c4 = math.sqrt(math.pow(t1.xcor()-c4.xcor(),2) + math.pow(t1.ycor()-c4.ycor(), 2))
    if dt1c4 < 20:	
      if c4.isvisible():
        t1coins += 1
        if t1coins > 1:
          print("\033[0;32mCha-ching! Green turtle has " + str(t1coins) + " coins!\033[0m")
        else:
          print("\033[0;32mCha-ching! Green turtle has 1 coin!\033[0m")
      c4.hideturtle()
    
    # COLLISION BETWEEN TURTLE 2 AND COINS 1 2 3 OR 4
    dt2c1 = math.sqrt(math.pow(t2.xcor()-c1.xcor(),2) + math.pow(t2.ycor()-c1.ycor(), 2))
    if dt2c1 < 20:
      if c1.isvisible():
        t2coins += 1
        if t2coins > 1:
          print("\033[0;31mCha-ching! Red turtle has " + str(t2coins) + " coins!\033[0m")
        else:
          print("\033[0;31mCha-ching! Red turtle has 1 coin!\033[0m")
      c1.hideturtle()
    dt2c2 = math.sqrt(math.pow(t2.xcor()-c2.xcor(),2) + math.pow(t2.ycor()-c2.ycor(), 2))
    if dt2c2 < 20:
      if c2.isvisible():
        t2coins += 1
        if t2coins > 1:
          print("\033[0;31mCha-ching! Red turtle has " + str(t2coins) + " coins!\033[0m")
        else:
          print("\033[0;31mCha-ching! Red turtle has 1 coin!\033[0m")
      c2.hideturtle()
    dt2c3 = math.sqrt(math.pow(t2.xcor()-c3.xcor(),2) + math.pow(t2.ycor()-c3.ycor(), 2))
    if dt2c3 < 20:
      if c3.isvisible():
        t2coins += 1
        if t2coins > 1:
          print("\033[0;31mCha-ching! Red turtle has " + str(t2coins) + " coins!\033[0m")
        else:
          print("\033[0;31mCha-ching! Red turtle has 1 coin!\033[0m")
      c3.hideturtle()
    dt2c4 = math.sqrt(math.pow(t2.xcor()-c4.xcor(),2) + math.pow(t2.ycor()-c4.ycor(), 2))
    if dt2c4 < 20:	
      if c4.isvisible():
        t2coins += 1
        if t2coins > 1:
          print("\033[0;31mCha-ching! Red turtle has " + str(t2coins) + " coins!\033[0m")
        else:
          print("\033[0;31mCha-ching! Red turtle has 1 coin!\033[0m")
      c4.hideturtle()
    
    # CHECK FOR WINNER
    if not c4.isvisible() and not c1.isvisible() and not c2.isvisible() and not c3.isvisible():
      if t1coins > t2coins:
        print("\n\033[1;32mWoo-hoo! Green turtle wins!")
      elif t2coins > t1coins:
        print("\n\033[1;31mWoo-hoo! Red turtle wins!")
      else:
        print("\n\033[1;34mWoah! Both turtles tied!")
      break
