count = 0 
while True:
  MyNumber = input("Please enter a number: ")
  try:
    valid_number = int(MyNumber)
    break
  except ValueError:
    count += 1
    print("Seriously, don't you read the instructions. \nI asked for a number...\nyou have done this", count, "times, try not to do it again")
 
print(valid_number)
