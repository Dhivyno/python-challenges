import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

password = ""
check = ""

for i in range(4):
  a = random.choice(alphabets)
  password += a

while check != password:
  check = ""
  for i in range(4):
    check += random.choice(alphabets)

print(password, check)