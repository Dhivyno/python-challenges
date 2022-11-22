import turtle as t
import random
 
t.screensize(1000, 1000, "white") #Added to make this work on smaller screens
 
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
 
randomr = [r1,r2,r3,r4,r5,r6,r7,r8]
randomt = [t1,t2,t3,t4,t5,t6,t7,t8]
print(randomr)
print(randomt)
 
t.speed(0)
t.up()
t.goto(-400,350)
t.down()
 
for i in range(7):
    t.forward(randomr[i])
    t.up()
    t.forward(randomt[i])
    t.down()
    t.forward(randomt[i])
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(randomr[i])
    t.up()
    t.forward(randomt[i])
    t.down()
    t.forward(randomt[i])
    t.left(90)
    t.forward(40)
    t.left(90)
 
t.forward(r9)
t.up()
t.forward(t9)
t.down()
t.forward(t9)
t.left(90)
t.forward(800)
 
t.up()
t.goto(-400,350)
t.down()
t.back(600)
t.up()
t.color("red")
t.shape("turtle")
t.goto(-400,380)
t.right(90)
t.pendown()



t.fd(r1+0.5*t1)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(2*(r1+0.5*t1)-800)
t.lt(90)
t.fd(40)
for i in range(1, len(randomr)):
  t.rt(90)
  t.fd((800-(randomr[i-1]+0.5*randomt[i-1]))-(randomr[i]+0.5*randomt[i]))
  t.lt(90)
  t.fd(40)
  t.rt(90)
  t.fd(2*(randomr[i]+0.5*randomt[i])-800)
  t.lt(90)
  t.fd(40)
