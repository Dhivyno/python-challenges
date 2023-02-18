import turtle

def square_draw(x,y,sz):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(sz)
        turtle.right(90)
        
for y in range (-300,300,20):
    for x in range (-300,300,20):
        square_draw(x,y,10)
