import random
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
randomlist = []

for i in range(26):
  a = random.choice(list1)
  randomlist.append(a)
  list1.remove(a)

phrase = input("What is your phrase you want to encrypt?  ")
encrypted = ""
for i in range(len(phrase)):
  for j in range(26):
    if phrase[i] == list2[j]:
      encrypted += randomlist[j]

print(encrypted)
    
  
