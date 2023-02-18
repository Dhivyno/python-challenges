seen_words = []
num_seen_words = []
highest1 = 0
highest2 = 0
highest3 = 0
lowest1 = 100
lowest2 = 100
lowest3 = 100

with open("rudyard.txt", "r") as file:
  for line in file:
    words = line.split()
    for i in range(len(words)):
      if words[i] in seen_words:
        for j in range(len(seen_words)):
          if words[i] == seen_words[j]:
            num_seen_words[j] += 1
      else:
        seen_words.append(words[i])
        num_seen_words.append(1)

print(num_seen_words)
for i in range(len(num_seen_words)):
  if num_seen_words[i] > highest1:
    highestword1 = seen_words[i]
  elif num_seen_words[i] > highest2:
    highestword2 = seen_words[i]
  elif num_seen_words[i] > highest3:
    highestword3 = seen_words[i]
  if num_seen_words[i] < lowest1:
    lowestword1 = seen_words[i]
  elif num_seen_words[i] < lowest2:
    lowestword2 = seen_words[i]
  elif num_seen_words[i] < lowest3:
    lowestword3 = seen_words[i]

print("The most seen words in the text are in order: ", highestword1, highestword2, highestword3)
print("The least seen words in the text are in order: ", lowestword1, lowestword2, lowestword3)