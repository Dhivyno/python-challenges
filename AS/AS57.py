byte = str(input("What is the transmitted byte: "))
count = 0
for i in range(len(byte)):
  if byte[i] == "1":
    count += 1

if count % 2 == 0:
  print("Byte is valid")
else:
  print("Byte is not valid")
