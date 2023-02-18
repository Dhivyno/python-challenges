print("Think of a number between 1 and 111")
print("When i say a number, you have to tell me if your number is higher or lower than mine and if i get it correct, type 'yes'")
high = 56
num = 56
count = 1
choice = input("56?")
while choice not in ["yes", "Yes"]:
  if choice in ["higher", "Higher", "h"]:
    if high%2 == 0:
      high *= 0.5
    else:
      high = (high+1)/2
    num += high
    num = int(num)
  elif choice in ["lower", "Lower", "l"]:
    if high%2 == 0:
      num -= high/2
    else:
      num -= high/2
    num = int(num)
    high *= 0.5
  choice = input(str(num) + "?")
  count += 1
print("it took me", count, "tries to get your number:", num)