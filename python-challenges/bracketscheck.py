phrase = input("Enter your phrase to be checked:  ")
open = 0
close = 0
for i in range(len(phrase)):
  if phrase[i] == "(":
    open += 1
  if phrase[i] == ")":
    close += 1
if open == close:
  print("Your brackets are balanced")
else:
  print("Your brackets are not balanced")