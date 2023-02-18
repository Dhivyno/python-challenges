import turtle
import random

turtle.screensize(1000, 1000, "white") #Added to make this work on smaller screens

r1 = random.randint(20,700)
t1 = (800-r1)/2

r2 = random.randint(20,700)
t2 = (800-r2)/2

r3 = random.randint(20,700)
t3 = (800-r3)/2

r4 = random.randint(20,700)
t4 = (800-r4)/2

r5 = random.randint(20,700)
t5 = (800-r5)/2

r6 = random.randint(20,700)
t6 = (800-r6)/2

r7 = random.randint(20,700)
t7 = (800-r7)/2

r8 = random.randint(20,700)
t8 = (800-r8)/2

r9 = random.randint(20,700)
t9 = (800-r9)/2


randomr = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
randomt = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

turtle.speed(10)
turtle.up()
turtle.goto(-400,350)
turtle.down()

for i in range(7):
    turtle.forward(randomr[i])
    turtle.up()
    turtle.forward(randomt[i])
    turtle.down()
    turtle.forward(randomt[i])
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(randomr[i])
    turtle.up()
    turtle.forward(randomt[i])
    turtle.down()
    turtle.forward(randomt[i])
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)

turtle.forward(r9)
turtle.up()
turtle.forward(t9)
turtle.down()
turtle.forward(t9)
turtle.left(90)
turtle.forward(800)

turtle.up()
turtle.goto(-400,350)
turtle.down()
turtle.back(600)
turtle.up()
turtle.color("red")
turtle.shape("turtle")
turtle.goto(-400,380)
turtle.right(90)
turtle.pendown()

turtle.fd(r1+t1/2)
turtle.rt(90)
turtle.fd(50)
if r1>=800/3:
    turtle.rt(90)
    turtle.fd(r1-t1)
    turtle.lt(90)
    turtle.fd(40)
else:
    turtle.lt(90)
    turtle.fd(t1-r1)
    turtle.rt(90)
    turtle.fd(40)

for i in range(1, 7):
    gap = (randomr[i]+0.5*randomt[i])-400
    x, y = turtle.pos()
    if x > 0 and x - gap < 0:
        turtle.lt(90)
        turtle.fd(abs(x - gap))
        turtle.rt(90)
    elif x > 0 and x - gap > 0:
        turtle.rt(90)
        turtle.fd(abs(x - gap))
        turtle.lt(90)
    elif x < 0 and x - gap > 0:
        turtle.rt(90)
        turtle.fd(abs(x - gap))
        turtle.lt(90)
    elif x < 0 and x - gap < 0:
        turtle.lt(90)
        turtle.fd(abs(x - gap))
        turtle.rt(90)
    elif x == 0 and x - gap > 0:
        turtle.rt(90)
        turtle.fd(abs(x - gap))
        turtle.lt(90)
    elif x == 0 and x - gap < 0:
        turtle.lt(90)
        turtle.fd(abs(x - gap))
        turtle.rt(90)
    turtle.fd(40)
    if gap > 0:
        turtle.rt(90)
        turtle.fd(randomr[i]-randomt[i])
        turtle.lt(90)
        turtle.fd(40)
    elif gap < 0:
        turtle.lt(90)
        turtle.fd(randomt[i]-randomr[i])
        turtle.rt(90)
        turtle.fd(40)

gap = (r9+0.5*t9)-400
x, y = turtle.pos()
turtle.rt(90)
turtle.fd(x-gap)
turtle.lt(90)
turtle.fd(40)