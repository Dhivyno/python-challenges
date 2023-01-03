import turtle as t

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)


t.speed(0)
for i in range(6):
  koch(t, 3, 100)
  t.right(60)
