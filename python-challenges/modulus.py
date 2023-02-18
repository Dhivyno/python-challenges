number = int(input('what number do you choose?  '))
if number % 3 == 0:
  print('your number is divisible by 3.')
else:
  print('your number is not divisible by 3 and leaves a remainder of', number % 3)