def add_digits(n):
    if n < 10:
        return n
    else:
      n = int(str(int(str(n)[0])+int(str(n)[1]))+str(n)[2:])
      return add_digits(n)

print(add_digits(123))


