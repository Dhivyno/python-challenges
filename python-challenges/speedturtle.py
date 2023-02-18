import turtle
turtle.bgcolor("blue")
turtle.speed(0)
print(turtle.screensize())
for i in range(300,-300,-10):
  turtle.pu()
  turtle.goto(-400,i)
  turtle.pd()
  turtle.fd(600)
turtle.rt(90)
for i in range(400, -400, -10):
  turtle.penup()
  turtle.goto(i, 300)
  turtle.pendown()
  turtle.fd(800)
turtle.done()