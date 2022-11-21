import math
exp = input("Enter your expression: ")
expanded = ""

for i in range(int(exp[6])+1):
  num = int(exp[6])
  current = str(int(math.factorial(num)/(math.factorial(num-i)*math.factorial(i))))+"x^"+str(num-i)+"*y^"+str(i)+ " + "
  expanded += current

print(expanded[0:len(expanded)-3])
