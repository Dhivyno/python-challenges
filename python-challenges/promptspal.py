import random
num = random.randint(1, 50)

counter = 0

with open("promptspal.txt", "r") as file:
  for line in file:
    counter += 1
    if num == counter:
      print(line)
    