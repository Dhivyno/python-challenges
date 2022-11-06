lengths = []
sum = 0
with open("rudyard.txt","r") as file:
  for line in file:
    for word in line.split():
      lengths.append(len(word))
for i in range(len(lengths)):
  sum += lengths[i]

average = sum/(len(lengths))
print(average)
