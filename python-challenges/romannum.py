menu = input("'a':decimal-roman or 'b':roman-decimal.  ")
list1 = [[1, "I", 2, "II", 3, "III", 4, "IV", 5, "V", 6, "VI", 7, "VII", 8, "VIII", 9, "IX", 10, "X"], [1, "X", 2, "XX", 3, "XXX", 4, "XL", 5, "L", 6, "LX", 7, "LXX", 8, "LXXX", 9, "XC", 10, "C"], [1, "C", 2, "CC", 3, "CCC", 4, "CD", 5, "D", 6, "DC", 7, "DCC", 8, "DCCC", 9, "CM", 10, "M"], [1, "M", 2, "MM", 3, "MMM"]]
list2 = []

def dtor():
  num = int(input("give a decimal number,max=3999.  "))
  a = len(str(num))
  numstr = str(num)
  if a == 1:
    for i in range(9):
      if num == list1[0][(i*2)]:
        print(list1[0][(i*2+1)])
  elif a == 2:
    for j in range(9):
      if int(numstr[0]) == list1[1][(j*2)]:
        b = list1[1][(j*2+1)]
    for i in range(9):
      if int(numstr[1]) == list1[0][(i*2)]:
        c = list1[0][(i*2+1)]
    print(b,c, sep = "")
  elif a == 3:
    for j in range(9):
      if int(numstr[0]) == list1[2][(j*2)]:
        b = list1[2][(j*2+1)]
    for j in range(9):
      if int(numstr[1]) == list1[1][(j*2)]:
        c = list1[1][(j*2+1)]
    for i in range(9):
      if int(numstr[2]) == list1[0][(i*2)]:
        d = list1[0][(i*2+1)]
    print(b,c,d, sep = "")
  elif a == 4:
    for j in range(3):
      if int(numstr[0]) == list1[3][(j*2)]:
        b = list1[3][(j*2+1)]
    for j in range(9):
      if int(numstr[1]) == list1[2][(j*2)]:
        c = list1[2][(j*2+1)]
    for j in range(9):
      if int(numstr[2]) == list1[1][(j*2)]:
        d = list1[1][(j*2+1)]
    for i in range(9):
      if int(numstr[3]) == list1[0][(i*2)]:
        e = list1[0][(i*2+1)]
    print(b,c,d,e, sep = "")

list3 = [[1, "I", 2, "I I", 3, "I I I", 4, "I V", 5, "V", 6, "V I", 7, "V I I", 8, "V I I I", 9, "I X"], [1, "X", 2, "X X", 3, "X X X", 4, "X L", 5, "L", 6, "L X", 7, "L X X", 8, "L X X X", 9, "X C"], [1, "C", 2, "C C", 3, "C C C", 4, "C D", 5, "D", 6, "D C", 7, "D C C", 8, "D C C C", 9, "C M"], [1, "M", 2, "M M", 3, "M M M"]]

def value(r):
  if (r == 'I'):
    return 1
  if (r == 'V'):
    return 5
  if (r == 'X'):
    return 10
  if (r == 'L'):
    return 50
  if (r == 'C'):
    return 100
  if (r == 'D'):
    return 500
  if (r == 'M'):
    return 1000
  return -1
 
 
def rtod(str):
  res = 0
  i = 0
 
  while (i < len(str)):
    s1 = value(str[i])
    if (i + 1 < len(str)):
      s2 = value(str[i + 1])
      if (s1 >= s2):
        res = res + s1
        i = i + 1
      else:
        res = res + s2 - s1
        i = i + 2
    else:
      res = res + s1
      i = i + 1
 
  return res












if str(menu) in ["a", "A"]:
  dtor()
elif str(menu) in ["b", "B"]:
  num = input("What is your roman number?")
  rtod(num)
  print("Integer form of Roman Numeral is"),
  print(rtod(num), sep = "")