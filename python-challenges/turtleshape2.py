import turtle as t
num = int(input("How many sides on your polygon?  "))
t.color('red')
for i in range(num):
  t.fd(100)
  t.lt(360/num)
t.done()