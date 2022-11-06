def nand(input1, input2):
  if not(input1 == 1 and input2 == 1):
    return 1
  else:
    return 0

a = int(input("What is your first input?  "))
b = int(input("What is your second input?  "))

def orgate(input1, input2):
  print(nand(nand(input1, input1), nand(input2, input2)))

def andgate(input1, input2):
  print(nand(nand(input1, input2), nand(input1, input2)))

def norgate(input1, input2):
  print(nand(nand(nand(input1, input1), nand(input2, input2)), nand(nand(input1, input1), nand(input2, input2))))

def notgate(input1):
  print(nand(input1, input1))

def xorgate(input1, input2):
  print(nand(nand(nand(input1, input2), input1), nand(nand(input1, input2), input2)))

orgate(a, b)
andgate(a, b)
norgate(a, b)
notgate(a)
xorgate(a, b)
