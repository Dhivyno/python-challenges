n1, n2 = 0, 1
count = 0


print("Fibonacci sequence:")
while count < 101:
  print(n1)
  nth = n1 + n2
  n1 = n2
  n2 = nth
  count += 1