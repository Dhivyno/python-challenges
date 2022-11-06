numbers = [1, 5, 6, 10, 15]
a = len(numbers)
mini = abs(numbers[0]-numbers[1])
for i in range(a-1):
  for j in range(i+1, a):
    if abs(numbers[i]-numbers[j]) < mini:
      mini = abs(numbers[i]-numbers[j])

print(mini)

