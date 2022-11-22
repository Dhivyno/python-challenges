import random 

for i in range(20):
  num = random.randint(1, 20)
  
  if (num % 5 == 0 and num % 3 == 0):
    print(num, "FizzBuzz")
  elif num % 5 == 0:
    print(num, "Buzz")
  elif num % 3 == 0:
    print(num, "Fizz")
  else:
    print(num)
