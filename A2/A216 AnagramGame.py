prompt = input("What is your word?  ")

with open("wordlist.txt", "r") as file:
  for line in file:
    for word in line.split():
      count = 0
      if len(prompt) == len(str(word)):
        splitword = [*prompt]
        for i in range(len(splitword)):
          if splitword[i] in word:
            if word[i] in splitword:
              count += 1
        if count == len(prompt):
          print(line, "is an anagram of", prompt)
