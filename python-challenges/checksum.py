number = input("Enter you 5 digit number with the last number being a check number:  ")
multiplier = 5
checksum = 0
for i in range(4):
   checksum += multiplier*int(number[i])
   multiplier -= 1
sumdiv = 11 - checksum%11
if sumdiv == int(number[4]):
  discount = 1
