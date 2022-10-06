list = []
repetitions = int(input("how many numbers do you want to input into the list?  "))
for i in range(repetitions):
  choice = input("what do you want to inout into the list?  ")
  list.append(choice)
print("first number is", list[0])
print("last number is", list[repetitions-1])
