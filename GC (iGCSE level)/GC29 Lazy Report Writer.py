import random 
students = int(input("how many students are in your class?  "))
list1 = ["attentative", "no attention in class", "moderately attentative"]
list2 = ["unorganised", "moderately organised", "very well organised"]
list3 = ["lazy", "bright", "energetic"]
list4 = ["Overall - good", "overall - very good", "overall - have to improve"]

for i in range(students):
  print("STUDENT", i + 1)
  a = random.randint(0,2)
  print(list1[a])
  b = random.randint(0,2)
  print(list2[b])
  c = random.randint(0,2)
  print(list3[c])
  if a == 1 or b == 0 or c == 0:
    print(list4[2])
  else:
    d = random.randint(0,1)
    print(list4[d])
  print("")
