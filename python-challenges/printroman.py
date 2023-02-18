list1 = [[0, "", 1, "I", 2, "II", 3, "III", 4, "IV", 5, "V", 6, "VI", 7, "VII", 8, "VIII", 9, "IX", 10, "X"], [0, "", 1, "X", 2, "XX", 3, "XXX", 4, "XL", 5, "L", 6, "LX", 7, "LXX", 8, "LXXX", 9, "XC", 10, "C"], [0, "", 1, "C", 2, "CC", 3, "CCC", 4, "CD", 5, "D", 6, "DC", 7, "DCC", 8, "DCCC", 9, "CM", 10, "M"], [1, "M", 2, "MM", 3, "MMM"]]

def dtor(f):
  a = len(str(f))
  numstr = str(f)
  if a == 1:
    for i in range(10):
      if f == list1[0][(i*2)]:
        print(list1[0][(i*2+1)])
  elif a == 2:
    for j in range(10):
      if int(numstr[0]) == list1[1][(j*2)]:
        b = list1[1][(j*2+1)]
    for i in range(10):
      if int(numstr[1]) == list1[0][(i*2)]:
        c = list1[0][(i*2+1)]
    print(b,c, sep = "")
  elif a == 3:
    for j in range(10):
      if int(numstr[0]) == list1[2][(j*2)]:
        b = list1[2][(j*2+1)]
    for j in range(10):
      if int(numstr[1]) == list1[1][(j*2)]:
        c = list1[1][(j*2+1)]
    for i in range(10):
      if int(numstr[2]) == list1[0][(i*2)]:
        d = list1[0][(i*2+1)]
    print(b,c,d, sep = "")
  elif a == 4:
    for j in range(3):
      if int(numstr[0]) == list1[3][(j*2)]:
        b = list1[3][(j*2+1)]
    for j in range(10):
      if int(numstr[1]) == list1[2][(j*2)]:
        c = list1[2][(j*2+1)]
    for j in range(10):
      if int(numstr[2]) == list1[1][(j*2)]:
        d = list1[1][(j*2+1)]
    for i in range(10):
      if int(numstr[3]) == list1[0][(i*2)]:
        e = list1[0][(i*2+1)]
    print(b,c,d,e, sep = "")

for i in range(1, 101):
  dtor(i)