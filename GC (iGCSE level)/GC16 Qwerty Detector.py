a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
text = list(input("Enter your text:  "))

for i in range(len(text)):
  if text[i] in ["q", "Q"]:
    a = 1
  if text[i] in ["w", "W"]:
    b = 1
  if text[i] in ["e", "E"]:
    c = 1
  if text[i] in ["r", "R"]:
    d = 1
  if text[i] in ["t", "t"]:
    e = 1
  if text[i] in ["y", "Y"]:
    f = 1

if a+b+c+d+e+f == 6:
  print("all characters in 'qwerty' has been used")
else:
  print("not all characters in 'qwerty' has been used")
