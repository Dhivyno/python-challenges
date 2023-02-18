import random 
choice = input("Do you want to start the program?  y/n:  ")
while choice in ["yes", "YES", "y", "Y"]:
  #1 is confess and 0 is silent
  p1 = int(input("Confess:1, Silent:0    "))
  p2 = random.randint(0, 1)
  if p1 == 1 and p2 == 1:
    print("Both confessed, 5 years each")
  elif p1 == 0 and p2 == 0:
    print("Both silent, 1 year each")
  elif p1 == 1 and p2 == 0:
    print("Prisoner 2:20 years, prisoner 1: released")
  elif p1 == 0 and p2 == 1:
    print("Prisoner 1:20 years, prisoner 2: released")
  choice = input("Do you want to continue the program?  y/n:  ")
