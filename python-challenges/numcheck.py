count = 0
while True:
  a = input("What is your number?  ")
  try:
      valid_num = int(a)
      break
  except ValueError:
    print("It is not a number, try again")
 
print(a, "is a number")

