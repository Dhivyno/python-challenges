tic = [["","",""], ["","",""], ["","",""]]

# this does raise the problem that players can rewrite the box that the opponent has already marked but im not sure how to get across that because there is no .freeze feature like in javascript

while True:
  row = int(input("Player 1: Which row do you want to place your marker:"))
  column = int(input("Player 1: Which column do you want to place your marker:"))
  tic[row-1][column-1] = "X"
  print(tic[0])
  print(tic[1])
  print(tic[2])
  if (tic[0][0] == "X" and tic[0][1] == "X" and tic[0][2] == "X") or (tic[1][0] == "X" and tic[1][1] == "X" and tic[1][2] == "X") or (tic[2][0] == "X" and tic[2][1] == "X" and tic[2][2] == "X") or (tic[0][0] == "X" and tic[1][0] == "X" and tic[2][0] == "X") or (tic[0][1] == "X" and tic[1][1] == "X" and tic[2][1] == "X") or (tic[0][2] == "X" and tic[1][2] == "X" and tic[2][2] == "X") or (tic[0][0] == "X" and tic[1][1] == "X" and tic[2][2] == "X") or (tic[0][2] == "X" and tic[1][1] == "X" and tic[2][0] == "X"):
    print("Player 1 won!!")
    break;
  row2 = int(input("Player 2: Which row do you want to place your marker:"))
  column2 = int(input("Player 2: Which column do you want to place your marker:"))
  tic[row2-1][column2-1] = "O"
  print(tic[0])
  print(tic[1])
  print(tic[2])  
  if (tic[0][0] == "O" and tic[0][1] == "O" and tic[0][2] == "O") or (tic[1][0] == "O" and tic[1][1] == "O" and tic[1][2] == "O") or (tic[2][0] == "O" and tic[2][1] == "O" and tic[2][2] == "O") or (tic[0][0] == "O" and tic[1][0] == "O" and tic[2][0] == "O") or (tic[0][1] == "O" and tic[1][1] == "O" and tic[2][1] == "O") or (tic[0][2] == "O" and tic[1][2] == "O" and tic[2][2] == "O") or (tic[0][0] == "O" and tic[1][1] == "O" and tic[2][2] == "O") or (tic[0][2] == "O" and tic[1][1] == "O" and tic[2][0] == "O"):
    print("Player 2 won!!")
    break;
