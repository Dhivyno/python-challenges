import random
floors = int(input("How many floors does your building have?  "))
numlist = []

for i in range(1, floors+1):
  numlist.append(i)

for i in range(len(numlist)):
  choose = random.choice(numlist)
  print(choose)
  numlist.remove(choose)