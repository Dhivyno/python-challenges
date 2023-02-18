import turtle as t
num = int(input("How many sides on your polygon?  "))
t.color('red')
t.begin_fill()
for i in range(num):
  t.fd(100)
  t.lt(360/num)
t.end_fill()
t.done()