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
  "Q": 12,
  "K": 13,
  "A": 14
}


def highCard(num):
  highest = 0
  for i in range(5):
    if int(valdict.get(num[i])) > highest:
      highest = int(valdict.get(num[i]))
  return highest

#royal flush
def royalFlush(num, suit):
  if num == ["A", "J", "K", "Q", "T"]:  #checking 5 numbers for royal flush
    if suit[0] == suit[1] and suit[0] == suit[2] and suit[0] == suit[3] and suit[0] == suit[4]:
      return True
      
def straightFlush(num, suit):
  if (int(valdict.get(num[1])) == int(valdict.get(num[0])) + 1 and int(valdict.get(num[2])) == int(valdict.get(num[1])) + 1 and int(valdict.get(num[3])) == int(valdict.get(num[2])) + 1 and int(valdict.get(num[4])) == int(valdict.get(num[3])) + 1) or num == ["9", "J", "K", "Q", "T"] or num == ["8", "9", "J", "Q", "T"] or num == ["7", "8", "9", "T", "J"]:
    if suit[0] == suit[1] and suit[0] == suit[2] and suit[0] == suit[3] and suit[0] == suit[4]:
      return True

def fourOfAKind(num, suit):
  for i in range(5):
    counter = 0
    for j in range(5):
      if num[i] == num[j]:
        counter += 1
    if counter == 4:
      return True

def fullHouse(num, suit):
  removal = []
  copy = list(num)
  for i in range(5):
    counter = 0
    removal = []
    for j in range(i+1, 5):
      if num[i] == num[j]:
        counter += 1
        removal.append(j)
    if counter == 2:
      removal.append(i)
      removal.sort()
      removal[1] -= 1
      removal[2] -= 2
      for k in range(3):
        copy.pop(removal[k])
      break
      if copy[0] == copy[1]:
        print(removal, copy, num)
        return True


def flush(num, suit):
  if suit[0] == suit[1] and suit[0] == suit[2] and suit[0] == suit[3] and suit[0] == suit[4]:
    return True

def straight(num, suit):
  if (int(valdict.get(num[1])) == int(valdict.get(num[0])) + 1 and int(valdict.get(num[2])) == int(valdict.get(num[1])) + 1 and int(valdict.get(num[3])) == int(valdict.get(num[2])) + 1 and int(valdict.get(num[4])) == int(valdict.get(num[3])) + 1) or num == ["9", "J", "K", "Q", "T"] or num == ["8", "9", "J", "Q", "T"] or num == ["7", "8", "9", "T", "J"]:
    return True

def threeOfAKind(num, suit):
  for i in range(5):
    counter = 0
    for j in range(i+1, 5):
      if num[i] == num[j]:
        counter += 1
    if counter == 2:
      return True

def twoPair(num, suit):
  removal = []
  copy = list(num)
  for i in range(5):
    counter = 0
    for j in range(i+1, 5):
      if num[i] == num[j]:
        counter += 1
        removal.append(j)
    if counter == 1:
      removal.append(i)
      removal.sort()
      removal[1] -= 1
      for k in range(2):
        copy.pop(removal[k])
      break
    
  for i in range(3):
    counter = 0
    for j in range(i+1, 3):
      if copy[i] == copy[j]:
        counter += 1
    if counter == 1:
      return True

def onePair(num, suit):
  for i in range(5):
    counter = 0
    for j in range(i+1, 5):
      if num[i] == num[j]:
        counter += 1
    if counter == 1:
      return True

wincount = 0

with open("pokerhand.txt", "r") as file:
  for line in file:
    hand = str(line)
    player1value = 0
    player2value = 0
    numbers1 = []
    suits1 = []
    numbers2 = []
    suits2 = []
    
    
    
    
    for i in range(5):
      numbers1.append(hand[3*i])
      suits1.append(hand[3*i+1])
      numbers2.append(hand[15+3*i])
      suits2.append(hand[15+3*i+1])
    
    numbers1.sort()
    numbers2.sort()
    suits1.sort()
    suits2.sort()
    
    if royalFlush(numbers1, suits1):
      player1value = 10000 + highCard(numbers1)
      print("Royal flush!")
    elif straightFlush(numbers1, suits1):
      player1value = 9000 + highCard(numbers1)
      print("Straight flush!")
    elif fourOfAKind(numbers1, suits1):
      player1value = 8000 + highCard(numbers1)
      print("Four of a kind!")
    elif fullHouse(numbers1, suits1):
      player1value = 7000 + highCard(numbers1)
      print("Full House!")
    elif flush(numbers1, suits1):
      player1value = 6000 + highCard(numbers1)
      print("Flush!")
    elif straight(numbers1, suits1):
      player1value = 5000 + highCard(numbers1)
      print("Straight!")
    elif threeOfAKind(numbers1, suits1):
      player1value = 4000 + highCard(numbers1)
      print("Three of a Kind!")
    elif twoPair(numbers1, suits1):
      player1value = 3000 + highCard(numbers1)
      print("Two Pair!")
    elif onePair(numbers1, suits1):
      player1value = 2000 + highCard(numbers1)
    
    if royalFlush(numbers2, suits2):
      player2value = 10000 + highCard(numbers2)
      print("Royal flush!")
    elif straightFlush(numbers2, suits2):
      player2value = 9000 + highCard(numbers2)
      print("Straight flush!")
    elif fourOfAKind(numbers2, suits2):
      player2value = 8000 + highCard(numbers2)
      print("Four of a kind!")
    elif fullHouse(numbers2, suits2):
      player2value = 7000 + highCard(numbers2)
      print("Full House!")
    elif flush(numbers2, suits2):
      player2value = 6000 + highCard(numbers2)
      print("Flush!")
    elif straight(numbers2, suits2):
      player2value = 5000 + highCard(numbers2)
      print("Straight!")
    elif threeOfAKind(numbers2, suits2):
      player2value = 4000 + highCard(numbers2)
      print("Three of a Kind!")
    elif twoPair(numbers2, suits2):
      player2value = 3000 + highCard(numbers2)
      print("Two Pair!")
    elif onePair(numbers2, suits2):
      player2value = 2000 + highCard(numbers2)
    
    if player1value > player2value:
      wincount += 1
    
    print(wincount)
