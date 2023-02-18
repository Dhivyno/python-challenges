import random
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
player1 = []
player2 = []
value1 = []
value2 = []
wins1 = 0
wins2 = 0

for i in range(5):
  position1 = random.randint(1, 26)
  buffer1 = random.randint(0, 26)
  player1.append(names[(position1+buffer1)%26])
  value1.append(position1)
  position2 = random.randint(1, 26)
  buffer2 = random.randint(0, 26)
  player2.append(names[(position2+buffer2)%26])
  value2.append(position2)

for i in range(5):
  print("Player1: This is your hand: ", player1)
  play1 = int(input("Player1: which card place do you want to play?  "))
  print("Player2: This is your hand: ", player2)
  play2 = int(input("Player2: which card place do you want to play?  "))
  if int(value1[play1-1]) > int(value2[play2-1]):
    wins1 += 1
    print(int(value1[play1-1]), int(value2[play2-1]))
    value1.pop(play1-1)
    player1.pop(play1-1)
    value2.pop(play2-1)
    player2.pop(play2-1)
    print("Player 1 wins!")
  elif int(value1[play1-1]) < int(value2[play2-1]):
    wins2 += 1
    print(int(value1[play1-1]), int(value2[play2-1]))
    value1.pop(play1-1)
    player1.pop(play1-1)
    value2.pop(play2-1)
    player2.pop(play2-1)
    print("Player 2 wins!")
  else:
    print(int(value1[play1-1]), int(value2[play2-1]))
    value1.pop(play1-1)
    player1.pop(play1-1)
    value2.pop(play2-1)
    player2.pop(play2-1)
    print("Tie! No one wins")


if wins1 > wins2:
  print("Player1 Wins the game!")
elif wins1 < wins2:
  print("Player2 Wins the game!")
else:
  print("Tie! No one wins the game.")