balance = 50

withdraw = int(input("How many ringgit do you want to withdraw from your account"))

if withdraw + 0.5 <= 50:
  print("Witdraw successful, please wait for it to appear in the cash opening")
else:
  print("You do not have enough money in your account to do this withdrawal")
