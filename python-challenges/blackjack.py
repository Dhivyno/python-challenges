import random
valdict = {
  "2": 2,
  "3": 3, 
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "T": 10,
  "J": 11,
  "Q": 11,
  "K": 11,
  "A": 11
}
values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
hand1 = []
hand2 = []

for i in range(2):
  hand1.append(random.choice(values))
  hand2.append(random.choice(values))

def totalval(num):
  sum = 0
  for i in range(len(num)):
    sum += valdict.get(num[i])
  return sum

end = 0
while end != 1:
  menu = input("Keep playing or End (play or end):  ")
  if menu == "end":
    end = 1
    break
  print("Your value is", totalval(hand1))
  menu1 = input("Player 1 Hit or stand:  ")
  if menu1 in ["hit", "Hit", "HIT"]:
    hand1.append(random.choice(values))
    print("Your value is", totalval(hand1))
  elif menu1 in ["stand", "Stand", "STAND"]:
    final1val = totalval(hand1)
  print("Your value is", totalval(hand2))
  menu2 = input("Player 2 Hit or stand:  ")
  if menu2 in ["hit", "Hit", "HIT"]:
    hand2.append(random.choice(values))
    print("Your value is", totalval(hand2))
  elif menu2 in ["stand", "Stand", "STAND"]:
    final2val = totalval(hand2)

if final1val > final2val:
  print("Player 1 wins!")
elif final1val < final2val:
  print("Player 2 wins!")
else: 
  print("Tie!")