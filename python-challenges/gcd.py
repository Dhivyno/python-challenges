gcd = 0
num1 = int(input("Enter your first number:  "))
num2 = int(input("Enter your second number:  "))

if num1 > num2:
  for i in range(1, num1):
    if (num1 % i == 0) and (num2 % i == 0):
      gcd = i
else:
  for i in range(1, num2):
    if (num2 % i == 0) and (num1 % i == 0):
      gcd = i

print("gcd(", num1, ",", num2, ") is", gcd)