import math

def calculate(expression):
    parts = expression.split()

    stack = []

    for part in parts:
        if part.isdigit():
            stack.append(float(part))
        else:
          if len(stack) != 0:
            num2 = stack.pop()
            num1 = stack.pop()
            

          if part == "+":
            result = num1 + num2
          elif part == "-":
            result = num1 - num2
          elif part == "*":
            result = num1 * num2
          elif part == "/":
            result = num1 / num2
          elif part == "^":
            result = num1 ** num2
          elif part == "sin":
            result = math.sin(num1)
          elif part == "cos":
            result = math.cos(num1)
          elif part == "tan":
            result = math.tan(num1)
          elif part == "pi":
            result = math.pi
          stack.append(result)

    return stack[0]

print(calculate("3 4 + 5 *"))
print(calculate("3 4 5 * +")) 
print(calculate("3 4 5 * + 6 7 * +")) 
print(calculate("2 3 ^")) 
print(calculate("pi 3 *"))
