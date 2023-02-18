phrase = input("What is your phrase in english? ")
changed = ""
for i in range(len(phrase)):
  if phrase[i] in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
    changed += phrase[i]
  else:
    changed += phrase[i]
    changed += "o"
    changed += phrase[i]
print(changed)