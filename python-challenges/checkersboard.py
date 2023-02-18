col = int(input("How many columns do you want?  "))
rows = int(input("How many rows do you want?  "))

if rows % 2 == 0:
  for i in range(int(rows/2)):
    print("* . "*(int(col/2)))
    print(". * "*(int(col/2)))
else:
  if col % 2 == 0:
    for i in range(int((rows+1)/2)):
      print("* . "*(int(col/2)))
      print(". * "*(int(col/2)))
    print("* . "*(int(col/2)))
  elif col % 2 == 1:
    for i in range(int((rows+1)/2)):
      print("* . "*(int((col-1)/2))+"*")
      print(". * "*(int((col-1)/2))+".")
    print("* . "*(int((col-1)/2))+"*")