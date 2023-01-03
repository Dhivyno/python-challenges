def gray_codes(n):
    if n == 0:
        return [""]
    else:
        gray_codes_recurr = gray_codes(n - 1)
        return ["0" + code for code in gray_codes_recurr] + ["1" + code for code in reversed(gray_codes_recurr)]

for i in range(10):
  print(gray_codes(i))
