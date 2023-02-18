add = 0
for i in range(101, 1000):
  add = 0
  a = i
  a = str(a)
  for j in range(len(a)):
    add += int(a[j])
  if i%add == 0:
    print(i)