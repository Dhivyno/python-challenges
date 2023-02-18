import random
num = random.randint(1, 100)
count = 0 
while True:
  MyNumber = input("Please enter a number: ")
  try:
    valid_number = int(MyNumber)
    if valid_number < num:
      print("your number is lower than my number, try again with a larger number")
    elif valid_number > num:
      print("your number is larger than my number, try again with a smaller number")
    elif valid_number == num:
      print("yay, you got it, it was", num)
      exit()
  except ValueError:
    count += 1
    print("Seriously, don't you read the instructions. \nI asked for a number...\nyou have done this", count, "times, try not to do it again")

print("")