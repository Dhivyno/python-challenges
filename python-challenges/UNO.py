import random
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "W", "F"]
colors = ["R", "G", "Y", "B"]

player = []
comp = []

def addcard(num, who):
  for i in range(num):
    card = random.choice(numbers) + random.choice(colors)
    who.append(card)
for i in range(7):
  playercard = random.choice(numbers) + random.choice(colors)
  compcard = random.choice(numbers) + random.choice(colors)
  player.append(playercard)
  comp.append(compcard)

currentcard = random.choice(numbers) + random.choice(colors)


  
while len(player) != 0 and len(comp) != 0:
  print("This is the current card: ", currentcard)
  print("This is your hand: ", player)
  playcard = int(input("Which card place do you want to play?  "))
  if player[playcard-1][0] == "F":
    addcard(4, comp)
    colorchange = input("What color do you want to change it to (R, G, Y, B):  ")
    while colorchange not in ["R", "G", "Y", "B"]:
      colorchange = input("Enter a valid color:  ")
    currentcard = currentcard[0] + colorchange
    player.pop(playcard-1)
  elif player[playcard-1][0] == "W":
    colorchange = input("What color do you want to change it to (R, G, Y, B):  ")
    while colorchange not in ["R", "G", "Y", "B"]:
      colorchange = input("Enter a valid color:  ")
    currentcard = currentcard[0] + colorchange
    player.pop(playcard-1)
  elif player[playcard-1][0] == currentcard[0] or player[playcard-1][1] ==   currentcard[1]:
    currentcard = player[playcard-1]
    player.pop(playcard-1)
  else:
    addcard(1, player)
    print("Invalid card play")
