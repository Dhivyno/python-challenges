import random
list = []
for i in range(50):
  a = random.randint(0, 20000)
  list.append(a)

print(min(list))
print(max(list))
print(sum(list)/len(list))
