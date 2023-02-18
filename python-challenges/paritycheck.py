byte = str(input("What is your byte: "))
count = 0
for i in range(len(byte)):
  if byte[i] == "1":
    count += 1

if count % 2 == 1:
  print(byte, "parity bit: 0")
else:
  print(byte, "parity bit: 1")