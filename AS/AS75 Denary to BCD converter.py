num = int(input("Enter a nunber between 0 and 255:  "))
binary = ""

for i in range(8):
  divisor = 2**(8-i-1)
  binary += str(num//divisor)
  num -= (num//divisor)*divisor

print(binary)
