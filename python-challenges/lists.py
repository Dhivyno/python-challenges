List = ["chocolate", "banana", "apples", "milkshakes", "oranges"]


print(*List[0:4],sep=", ") 


games = ["PUBG", "COD"]
newgame = input("what games do you like?  ")
if newgame in games:
  print("i already have that in my list")
else:
  games.append(newgame)
  print("ok, this is the new list", games)