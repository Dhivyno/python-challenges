def bcdToHexaDecimal(s):
     
  len1 = len(s)
  check = 0
  sum = 0
  mul = 1
  ans = []
  
  i = len1 - 1
     
  while(i >= 0):
    sum += (ord(s[i]) - ord('0')) * mul
    mul *= 2
    check += 1

    if (check == 4 or i == 0):
             
      if (sum <= 9):
        ans.append(chr(sum + ord('0')))
      else:
        ans.append(chr(sum + 55));
      check = 0
      sum = 0
      mul = 1
         
    i -= 1
         
  len1 = len(ans)
  i = len1 - 1
     
  while(i >= 0):
    print(ans[i], end = "")
    i -= 1
     
s = input("Enter your BCD:  ")
bcdToHexaDecimal(s)