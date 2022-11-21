import random 
dividers = []
answers = []
corrects = 0
lengthcheck = 0
num = random.randint(0, 1000)
print(num)
for i in range(1, 13):
  if num%i == 0:
    dividers.append(i)
    print(dividers)
answer = input("Which times tables do you think this number is in? Try to guess all of them one by one between 1 and 12 inclusive in ascending order. enter end to end the guessing")
if answer != "end":
  answers.append(int(answer))
while answer != "end":
  answer = input("What's the next divider?  ")
  if answer != "end":
    answers.append(int(answer))

  for i in range(len(answers)):
    if answers[i] == dividers[i]:
      corrects +=1
    
if corrects == len(dividers):
  print("You got them all right!!!")
elif corrects>0 and corrects<len(dividers):
  print("You got", corrects, "correct but you missed", len(dividers)-corrects, "of them")
else:
  print("You didnt get any correct")
