a = 1
for i in range(16, -2, -2):
  list = [0]
  for j in range(1, a+1):
    list.append(j)
  print(" "*i, *list[1::], *list[len(list)-2:0:-1], sep = " ")
  a += 1
for i in range(2, 18, 2):
  list.remove(list[len(list)-1])
  print(" "*i , *list[1 : len(list)],*list[len(list)-2:0:-1], sep = " ")
