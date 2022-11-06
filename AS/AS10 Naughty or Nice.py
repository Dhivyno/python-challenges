vowels = 0
sameletter = 0
x = 0
a = list(input("What is your word?  "))
for i in range(len(a) - 1):
  b = str(a[i])
  c = str(a[i+1])
  if (b,c) == ('a','b'):
    print("Not a nice word")
    x = 1
  elif (b,c) == ('c','d'):
    print("Not a nice word")
    x = 1
  elif (b,c) == ('p','q'):
    print("Not a nice word")
    x = 1
  elif (b,c) == ('x','y'):
    print("Not a nice word")
    x = 1
  elif b == c:
    sameletter = 1
  if b == 'a' or b == 'e' or b == 'i' or b == 'o' or b == 'u':
    vowels += 1
  
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
  vowels += 1
if sameletter == 1 and vowels >= 3 and x != 1:
  print("nice word")
