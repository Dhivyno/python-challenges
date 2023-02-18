phrase = input("What is your phrase?  ")
counter = 0

for i in range(len(phrase)):
  if phrase[i] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
    counter += 1

print(counter, "vowels")