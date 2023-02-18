myHeight = 140
yourHeight = int(input('what is your height in cm.  '))
if int(yourHeight) > myHeight:
  print('you are taller than me by', yourHeight - myHeight, 'cm')
else:
  difference = myHeight - yourHeight
  print('I am taller than you by', myHeight - int(yourHeight))